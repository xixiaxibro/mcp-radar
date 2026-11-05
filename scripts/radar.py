#!/usr/bin/env python3
"""Public-source MCP activity collector. Python 3.9+, no third-party dependencies."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
import hashlib
import html
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
UTC = timezone.utc


def utcnow():
    return datetime.now(UTC)


def parse_date(value):
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(UTC)
    except ValueError:
        from email.utils import parsedate_to_datetime
        parsed = parsedate_to_datetime(value)
        return parsed.replace(tzinfo=UTC) if parsed.tzinfo is None else parsed.astimezone(UTC)


def clean(value, limit=500):
    text = html.unescape(re.sub(r"<[^>]+>", " ", value or ""))
    # Remote source text is data, never a command, workflow input, or instruction.
    text = re.sub(r"[\x00-\x1f\x7f]", " ", text)
    return re.sub(r"\s+", " ", text).strip()[:limit]


def markdown(value):
    return clean(str(value), 2000).replace("\\", "\\\\").replace("|", "\\|").replace("[", "\\[").replace("]", "\\]").replace("`", "'").replace("*", "\\*").replace("_", "\\_")


def read_json(path, default=None):
    return json.loads(path.read_text()) if path.exists() else default


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(path)


def token():
    value = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if value:
        return value
    try:
        result = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10)
        return result.stdout.strip() if result.returncode == 0 else None
    except (OSError, subprocess.TimeoutExpired):
        return None


class SafeRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if urlsplit(newurl).scheme != "https":
            raise ValueError("Refusing HTTPS downgrade")
        redirected = super().redirect_request(req, fp, code, msg, headers, newurl)
        if redirected is not None and urlsplit(newurl).hostname != urlsplit(req.full_url).hostname:
            redirected.remove_header("Authorization")
        return redirected


class PublicAPI:
    def __init__(self, credential=None, max_pages=3, per_page=100):
        self.credential = credential
        self.max_pages = max_pages
        self.per_page = per_page
        self.opener = build_opener(SafeRedirect())

    def request(self, url, github=False):
        parsed = urlsplit(url)
        if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
            raise ValueError("Only credential-free HTTPS source URLs are accepted")
        headers = {"User-Agent": "mcp-radar-public-research/1.0", "Accept": "application/json" if github else "application/rss+xml, application/atom+xml, text/xml"}
        if github:
            if parsed.hostname != "api.github.com":
                raise ValueError("GitHub credentials may only be sent to api.github.com")
            headers["X-GitHub-Api-Version"] = "2022-11-28"
            if self.credential:
                headers["Authorization"] = "Bearer " + self.credential
        for attempt in range(3):
            try:
                with self.opener.open(Request(url, headers=headers), timeout=25) as response:
                    payload = response.read(12_000_001)
                    if len(payload) > 12_000_000:
                        raise ValueError("Source response exceeds 12 MB limit")
                    return json.loads(payload) if github else payload
            except HTTPError as exc:
                if attempt < 2 and (exc.code in (429, 500, 502, 503, 504)):
                    time.sleep(2 ** attempt)
                    continue
                # Do not log response bodies, request headers, or credentials.
                raise RuntimeError(f"HTTP {exc.code} from {parsed.hostname}{parsed.path}") from None
            except (URLError, TimeoutError):
                if attempt == 2:
                    if not github:
                        # Some public feeds negotiate TLS differently with libcurl.
                        # No GitHub credentials are passed to this fallback.
                        try:
                            result = subprocess.run([
                                "curl", "--fail", "--location", "--silent", "--show-error",
                                "--proto", "=https", "--proto-redir", "=https",
                                "--max-time", "25", "--max-redirs", "5", url,
                            ], capture_output=True, timeout=30)
                            if result.returncode == 0 and len(result.stdout) <= 12_000_000:
                                return result.stdout
                        except (OSError, subprocess.TimeoutExpired):
                            pass
                    raise RuntimeError(f"Network error from {parsed.hostname}{parsed.path}") from None
                time.sleep(2 ** attempt)

    def get(self, path, params=None):
        url = "https://api.github.com/" + path
        return self.request(url + ("?" + urlencode(params) if params else ""), github=True)

    def pages(self, path, params, cutoff, date_key="updated_at", ordered=True):
        result = []
        for page in range(1, self.max_pages + 1):
            batch = self.get(path, {**params, "per_page": self.per_page, "page": page})
            if not isinstance(batch, list):
                raise ValueError("Expected paginated list")
            result.extend(batch)
            if len(batch) < self.per_page:
                return result, False
            if ordered and batch and parse_date(batch[-1].get(date_key)) and parse_date(batch[-1].get(date_key)) < cutoff:
                return result, False
        # Reaching the cap is visible; never claim complete coverage.
        return result, True


def matches(text, words):
    return [word for word in words if word.casefold() in text.casefold()]


def rank(item, config):
    text = " ".join([item["title"], item.get("excerpt", ""), " ".join(item.get("labels", []))])
    score = {1: 30, 2: 18, 3: 8}[item["tier"]]
    reasons = [f"T{item['tier']} watchlist"]
    weights = {"breaking": 28, "security": 26, "protocol": 20, "proposal": 16}
    for group, weight in weights.items():
        hits = matches(text, config["keywords"][group])
        if hits:
            score += weight
            reasons.append(group + ": " + ", ".join(hits[:3]))
    if item["kind"] in ("release", "advisory"):
        score += 25
        reasons.append(item["kind"])
    if item["kind"] == "commit":
        score += 5
    if item["status"] == "merged":
        score += 10
        reasons.append("merged implementation; verify release separately")
    if item.get("draft"):
        score -= 10
        reasons.append("draft PR")
    if matches(item["title"], config["keywords"]["noise"]):
        score -= 30
        reasons.append("routine maintenance penalty")
    return max(0, score), reasons


def event_key(item):
    # Reactions, star counts and comment counts do not create changes.
    fields = {k: item.get(k) for k in ("kind", "title", "status", "draft", "labels", "body_hash", "version", "merged_at", "published_at", "prerelease", "withdrawn_at", "head_sha")}
    return hashlib.sha256(json.dumps(fields, sort_keys=True).encode()).hexdigest()[:20]


def make_item(repo, record, kind, title, url, status, body="", **extra):
    return {
        "id": url, "source": repo["repo"], "kind": kind,
        "topic": repo["topic"], "tier": repo["tier"],
        "title": clean(title, 300), "url": url, "status": status,
        "created_at": record.get("created_at"), "updated_at": record.get("updated_at"),
        "excerpt": clean(body, 420),
        "body_hash": hashlib.sha256((body or "").encode()).hexdigest()[:20],
        **extra,
    }


def collect_repo(api, source, cutoff):
    name = source["repo"]
    items, warnings, errors = [], [], []
    coverage = {"source": name, "kind": "repository", "endpoints": {}}
    try:
        meta = api.get("repos/" + name)
        if meta.get("private"):
            raise ValueError("Private repositories are excluded from public output")
    except Exception as exc:
        return [], [{"source": name, "error": str(exc)}], [], {**coverage, "status": "failed"}
    coverage.update(status="ok", canonical_name=meta["full_name"], archived=meta["archived"], default_branch=meta["default_branch"])
    if name.casefold() != meta["full_name"].casefold():
        warnings.append({"source": name, "message": "Repository renamed/redirected to " + meta["full_name"]})
    jobs = [("pulls", {"state": "all", "sort": "updated", "direction": "desc"}, "updated_at", True),
            ("security-advisories", {"state": "published", "sort": "updated", "direction": "desc"}, "updated_at", True)]
    if source.get("releases", True):
        jobs.append(("releases", {}, "published_at", False))
    if source.get("issues"):
        jobs.append(("issues", {"state": "all", "sort": "updated", "direction": "desc"}, "updated_at", True))
    if source.get("commits"):
        jobs.append(("commits", {"since": cutoff.isoformat()}, "unused", False))
    for endpoint, params, date_key, ordered in jobs:
        try:
            rows, capped = api.pages(f"repos/{name}/{endpoint}", params, cutoff, date_key, ordered)
            coverage["endpoints"][endpoint] = {"fetched": len(rows), "capped": capped, "status": "ok"}
            if capped:
                warnings.append({"source": name, "endpoint": endpoint, "message": "Pagination cap reached; coverage may be incomplete. Increase limits or narrow the window."})
        except Exception as exc:
            errors.append({"source": name, "endpoint": endpoint, "error": str(exc)})
            coverage["endpoints"][endpoint] = {"status": "failed"}
            coverage["status"] = "partial"
            continue
        for row in rows:
            if endpoint == "releases" and row.get("draft"):
                continue
            if endpoint == "security-advisories" and row.get("state") != "published":
                continue
            if endpoint == "issues" and "pull_request" in row:
                continue
            if endpoint == "commits":
                timestamp = row.get("commit", {}).get("committer", {}).get("date")
            else:
                timestamp = row.get("updated_at") or row.get("published_at") or row.get("created_at")
            if not timestamp or parse_date(timestamp) < cutoff:
                continue
            title = row.get("title") or row.get("name") or row.get("tag_name") or row.get("summary") or row.get("commit", {}).get("message", "").split("\n")[0]
            body = row.get("body") or row.get("description") or ""
            if source.get("keywords") and not matches(title + " " + body, source["keywords"]):
                continue
            url = row.get("html_url")
            if not url:
                continue
            common = {"labels": sorted(x["name"] for x in row.get("labels", [])), "updated_at": timestamp}
            if endpoint == "pulls":
                status = "merged" if row.get("merged_at") else row["state"]
                item = make_item(source, row, "pull_request", title, url, status, body, number=row["number"], draft=row.get("draft", False), head_sha=row.get("head", {}).get("sha"), merged_at=row.get("merged_at"), **common)
            elif endpoint == "issues":
                item = make_item(source, row, "issue_or_proposal", title, url, row["state"], body, number=row["number"], **common)
            elif endpoint == "releases":
                item = make_item(source, row, "release", title, url, "prerelease" if row.get("prerelease") else "published", body, version=row["tag_name"], prerelease=row.get("prerelease", False), published_at=row.get("published_at"), **common)
            elif endpoint == "commits":
                message = row.get("commit", {}).get("message", "")
                item = make_item(source, row, "commit", title, url, "committed", message, **common)
            else:
                item = make_item(source, row, "advisory", title, url, "withdrawn" if row.get("withdrawn_at") else "published", body, published_at=row.get("published_at"), withdrawn_at=row.get("withdrawn_at"), severity=row.get("severity"), identifiers=row.get("identifiers", []), **common)
            items.append(item)
    return items, errors, warnings, coverage


def parse_feed(payload, source, cutoff):
    # ElementTree does not fetch external entities. Bound payload size at download.
    root = ET.fromstring(payload)
    ns = {"a": "http://www.w3.org/2005/Atom"}
    entries = root.findall("./channel/item")
    atom = root.tag == "{http://www.w3.org/2005/Atom}feed"
    if atom:
        entries = root.findall("a:entry", ns)
    out = []
    for row in entries:
        def text(tag):
            return row.findtext("a:" + tag, default="", namespaces=ns) if atom else row.findtext(tag, default="")
        title = text("title")
        body = text("summary") or text("description") or text("content")
        timestamp = (text("updated") or text("published")) if atom else text("pubDate")
        if not timestamp or parse_date(timestamp) < cutoff:
            continue
        if source.get("keywords") and not matches(title + " " + body, source["keywords"]):
            continue
        if atom:
            links = row.findall("a:link", ns)
            link = next((x.get("href") for x in links if x.get("rel", "alternate") == "alternate"), "")
        else:
            link = text("link")
        if urlsplit(link).scheme != "https":
            continue
        repo = {"repo": source["id"], "topic": source["topics"][0], "tier": source["tier"]}
        out.append(make_item(repo, {"updated_at": parse_date(timestamp).isoformat()}, "article", title, link, "published", body))
    return out, len(entries)


def render_report(run, events):
    lines = [f"# MCP Radar · {run['date']} (UTC)", "", f"采集时间：{run['generated_at']} · 回看窗口：{run['lookback_days']} 天。", "",
             "这是公开来源的更新索引和选题素材，不是已经审读、复现的技术结论。标题和摘录来自上游；优先级由可见规则计算。", "",
             f"本次窗口内 {run['item_count']} 条记录；本日累计 {len(events)} 个新增/变更版本；失败端点 {len(run['errors'])} 个；覆盖警告 {len(run['warnings'])} 个。", "",
             "## 覆盖与限制", "",
             "PR merged 表示代码进入分支，不代表已发布；release 不自动证明符合某协议版本。初次运行只建立窗口基线。", "",
             "仅跟踪 watchlist 中公开仓库的 PR、指定仓库 issue/commit、release、公开安全公告和订阅源。未提供 API 的社区讨论、社交媒体和完整标准文档变更不在覆盖保证内。RSS 仅提供源当前保留的条目。", ""]
    if run["errors"] or run["warnings"]:
        for entry in run["errors"]:
            lines.append(f"- 采集失败：`{markdown(entry['source'])}` / {markdown(entry.get('endpoint', 'source'))} — {markdown(entry['error'])}")
        for entry in run["warnings"]:
            lines.append(f"- 覆盖提示：`{markdown(entry['source'])}` / {markdown(entry.get('endpoint', 'source'))} — {markdown(entry['message'])}")
        lines.append("")
    else:
        lines.extend(["本次未报告采集错误或分页截断；这不代表覆盖整个 MCP 生态。", ""])
    sections = [
        ("重点 PR / 提案", lambda e: e["kind"] in ("pull_request", "issue_or_proposal"), 20),
        ("发布与安全公告", lambda e: e["kind"] in ("release", "advisory"), 15),
        ("协议 / 工作组提交", lambda e: e["kind"] == "commit", 10),
        ("文章与技术解释", lambda e: e["kind"] == "article", 10),
    ]
    ordered = sorted(events, key=lambda x: (-x["score"], x["id"], x["fingerprint"]))
    for heading, accept, limit in sections:
        selection = [e for e in ordered if accept(e)]
        lines.extend(["## " + heading, "", f"显示 {min(len(selection), limit)} / {len(selection)} 条；全部数据见当日 JSON。", ""])
        if not selection:
            lines.extend(["本日暂无记录。", ""])
        for item in selection[:limit]:
            lines.extend([f"### [{markdown(item['title'])}]({item['url']})", "",
                f"`{markdown(item['source'])}` · **{item['status']}** · {item['change_type']} · 分数 {item['score']} · 上游时间 {item.get('updated_at') or item.get('published_at')}", "",
                "入选依据：" + markdown("; ".join(item["reasons"])) + "。", ""])
            if item.get("excerpt"):
                lines.extend(["> 上游摘录（未审读）：" + markdown(item["excerpt"]), ""])
            lines.extend(["待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？", ""])
    lines.extend(["## 博客选题工作台", "", "从上面的重点项挑选，不自动把提案写成已实现功能：", "",
        "- 协议问题：规范原文、提案状态、旧行为与新行为。",
        "- 实现证据：PR diff、回归测试、客户端/服务端版本。",
        "- 复现：最小实验、消息/HTTP trace、失败与成功条件。",
        "- 结论边界：事实、维护者解释、个人判断分别记录。", "",
        "模板：[知识库写作模板](https://github.com/xixiaxibro/mcp-knowledge-base/tree/main/templates)。"])
    return "\n".join(lines) + "\n"


def run_collect(args):
    config = read_json(args.config)
    now = utcnow()
    cutoff = now - timedelta(days=args.days)
    api = PublicAPI(token(), config["limits"]["max_pages"], config["limits"]["per_page"])
    sources = config["repositories"]
    if args.repo:
        sources = [s for s in sources if s["repo"] in args.repo]
        missing = set(args.repo) - {s["repo"] for s in sources}
        if missing:
            raise ValueError("Repository not in public watchlist: " + ", ".join(sorted(missing)))
    items, errors, warnings, coverage = [], [], [], []
    with ThreadPoolExecutor(max_workers=config["limits"]["workers"]) as pool:
        futures = {pool.submit(collect_repo, api, s, cutoff): s for s in sources}
        for future in as_completed(futures):
            result, failed, incomplete, info = future.result()
            items.extend(result); errors.extend(failed); warnings.extend(incomplete); coverage.append(info)
            print(f"{info['source']}: {len(result)} items, {len(failed)} endpoint failures", flush=True)
    if not args.repo:
        for feed in config["feeds"]:
            try:
                found, count = parse_feed(api.request(feed["url"]), feed, cutoff)
                items.extend(found)
                coverage.append({"source": feed["id"], "kind": "feed", "status": "ok", "entries_available": count, "entries_in_window": len(found)})
            except Exception as exc:
                errors.append({"source": feed["id"], "error": str(exc)})
                coverage.append({"source": feed["id"], "kind": "feed", "status": "failed"})
    # A fully failed fetch must not overwrite a previously useful baseline.
    if not any(c["status"] in ("ok", "partial") for c in coverage):
        raise RuntimeError("All sources failed; previous data left intact")
    items = list({i["id"]: i for i in items}.values())
    for item in items:
        item["score"], item["reasons"] = rank(item, config)
        item["fingerprint"] = event_key(item)
    items.sort(key=lambda i: (-i["score"], i["id"]))
    output = args.output
    state = read_json(output / "data/state.json", {"schema_version": 1, "items": {}})
    initial = not state["items"]
    changes = []
    for item in items:
        old = state["items"].get(item["id"])
        if old is None or old["fingerprint"] != item["fingerprint"]:
            changes.append({**item, "change_type": "baseline" if initial else ("new" if old is None else "updated"), "observed_at": now.isoformat(timespec="seconds")})
        state["items"][item["id"]] = {"fingerprint": item["fingerprint"], "last_seen": now.isoformat(timespec="seconds")}
    retention = now - timedelta(days=90)
    state["items"] = {k:v for k,v in state["items"].items() if parse_date(v["last_seen"]) >= retention}
    date = now.date().isoformat()
    run = {"schema_version": 1, "date": date, "generated_at": now.isoformat(timespec="seconds"), "lookback_days": args.days,
           "baseline": initial, "item_count": len(items), "changes_this_run": len(changes),
           "sources": sorted(coverage, key=lambda x:x["source"]), "errors": sorted(errors, key=lambda x:(x['source'],x.get('endpoint',''))),
           "warnings": sorted(warnings, key=lambda x:(x['source'],x.get('endpoint',''))), "items": items}
    # Same-day reruns preserve earlier changes, rather than erasing the day's digest.
    daily_path = output / f"data/daily/{date}.json"
    day = read_json(daily_path, {"date": date, "events": []})
    accumulated = {(i["id"], i["fingerprint"]): i for i in day["events"]}
    for item in changes:
        accumulated[(item["id"], item["fingerprint"])] = item
    day["events"] = sorted(accumulated.values(), key=lambda i:(-i["score"],i["id"],i["fingerprint"]))
    day["last_run"] = {k:v for k,v in run.items() if k!='items'}
    write_json(output / "data/latest.json", run)
    write_json(daily_path, day)
    write_json(output / "data/state.json", state)
    report = render_report(run, day["events"])
    path = output / f"reports/daily/{date}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report)
    (output / "reports/latest.md").write_text(report)
    build_weekly(output, now)
    print(f"{len(items)} observations; {len(changes)} changes this run; {len(errors)} failed endpoints; {len(warnings)} coverage warnings")
    # Fail visibly on partial collection as well; workflow still persists diagnostics.
    return 2 if errors else 0


def build_weekly(output, now):
    start = now.date() - timedelta(days=6)
    all_events = {}
    failures = []
    for path in sorted((output / "data/daily").glob("*.json")):
        if not start.isoformat() <= path.stem <= now.date().isoformat():
            continue
        day = read_json(path)
        failures.extend(day.get('last_run',{}).get('errors',[]))
        for item in day["events"]:
            # Latest observed state per URL, with stable tie-breaking.
            if item['id'] not in all_events or item['observed_at'] > all_events[item['id']]['observed_at']:
                all_events[item['id']] = item
    lines = ["# MCP Radar · 滚动七日选题", "", f"观测日期：{start} 至 {now.date()}（UTC）。仅汇总已经采集的日报，不补造缺失日期。", "",
             f"去重条目 {len(all_events)}；日报记录的失败端点 {len(failures)} 个。分数表示阅读优先级，不表示技术正确性。", "",
             "| 优先级 | 来源 | 状态 | 条目 |", "|---:|---|---|---|"]
    for i in sorted(all_events.values(),key=lambda x:(-x['score'],x['id']))[:40]:
        lines.append(f"| {i['score']} | {markdown(i['source'])} | {i['status']} | [{markdown(i['title'])}]({i['url']}) |")
    lines.extend(["", "写作前检查：规范版本 → PR 与测试 → 发布版本 → 最小复现 → 结论边界。", ""])
    (output / "reports/weekly.md").write_text("\n".join(lines))


def validate_config(config):
    seen = set()
    for repo in config["repositories"]:
        name = repo["repo"]
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", name):
            raise ValueError("Invalid repository name: " + name)
        if name.casefold() in seen:
            raise ValueError("Duplicate repository: " + name)
        seen.add(name.casefold())
        if repo["tier"] not in (1,2,3):
            raise ValueError("Invalid tier")
    if not 1 <= config['limits']['max_pages'] <= 10 or not 1 <= config['limits']['per_page'] <= 100:
        raise ValueError('Invalid pagination limits')
    if not 1 <= config['limits']['workers'] <= 12:
        raise ValueError('Invalid worker count')
    for feed in config["feeds"]:
        if urlsplit(feed["url"]).scheme != "https":
            raise ValueError("Feed must use HTTPS")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    collect = sub.add_parser("collect")
    collect.add_argument("--days", type=int, default=14)
    collect.add_argument("--repo", action="append", help="Limit to configured repositories; skips feeds")
    collect.add_argument("--output", type=Path, default=ROOT)
    collect.add_argument("--config", type=Path, default=ROOT/"config/watchlist.json")
    sub.add_parser("validate")
    args = parser.parse_args()
    config = read_json(getattr(args,"config", ROOT/"config/watchlist.json"))
    validate_config(config)
    if args.command == "validate":
        print(f"Valid: {len(config['repositories'])} repositories, {len(config['feeds'])} feeds")
        return 0
    if not 1 <= args.days <= 90:
        parser.error("--days must be between 1 and 90")
    return run_collect(args)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"Collection failed: {exc}", file=sys.stderr)
        sys.exit(1)
