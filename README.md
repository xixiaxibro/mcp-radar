# MCP Radar

为协议学习、工程维护和原创博客提供可追溯的 MCP 更新素材。配套：[MCP Knowledge Base](https://github.com/xixiaxibro/mcp-knowledge-base)。

**这不是自动写博客的 Agent。** 它采集公开记录、保存状态、用透明规则筛选，并列出值得深读的 PR、提案、发布、安全公告和文章。规范解释、复现和文章由维护者完成。

## 阅读入口

- [最新日报](reports/latest.md)：按 PR/提案、发布/公告、工作组提交、文章分组，保留原始链接和入选依据。
- [滚动七日选题](reports/weekly.md)：按 URL 去重后的重点素材。
- [逐日历史](reports/daily/) 与 [当日结构化数据](data/daily/)：同一天重复运行不会抹掉早先变化。
- [最近完整观测窗口](data/latest.json)：包含所有观测条目、来源覆盖、失败与分页上限信息。
- [跟踪清单](config/watchlist.json) / [筛选规则](docs/methodology.md) / [运维](docs/operations.md)。

## 当前范围

36 个公开仓库、2 个 RSS/Atom 源。主线为 MCP 规范、Python/TS SDK、conformance、Inspector、Registry、授权与任务扩展；同时关注其他官方 SDK、Cloudflare OAuth/Agents、Tencent AI-Infra-Guard、FastMCP、真实服务和网关。

T1 是主线，T2 是专题，T3 是补充对照。大仓库设置 MCP 关键词过滤，减少无关流量。首次运行建立最近 14 天的基线；后续比较内容、PR head commit、状态和标签，仅保留新条目与实际变更。评论数量和 Star 变化不会产生技术更新。

当前正式协议基线记录为 `2026-07-28`，只是收录基准，不自动推断每个项目的兼容性。规范新版本仍需人工核实并更新配置。

## 本地运行

Python 3.11+，标准库实现，无需 LLM API Key。公开订阅源遇到本机 TLS 问题时会尝试系统 `curl`（可选；GitHub Actions 环境已提供）。通过 `GH_TOKEN` / `GITHUB_TOKEN` 或本机已登录的 `gh` 获得 GitHub API 权限；凭证只发送给 GitHub API，不写入输出。

```bash
python3 scripts/radar.py validate
python3 -m unittest discover -s tests -v
python3 scripts/radar.py collect --days 14
```

试跑单个项目，输出到临时目录，避免改变正式基线：

```bash
python3 scripts/radar.py collect --days 7 \
  --repo modelcontextprotocol/python-sdk --output /tmp/mcp-radar-trial
```

部分来源失败时退出码为 2，仍保存可用结果与诊断；所有来源失败时退出码为 1，保留旧数据。分页到达上限会显式警告，退出码仍为 0（若无采集失败）。

## 自动跟踪

GitHub Actions 每天 **01:17 UTC / 北京时间 09:17** 调度，并支持手动运行。使用仓库自动提供的 `GITHUB_TOKEN`，不需要额外的模型或第三方付费凭证。工作流只提交 `data/`、`reports/`，使用并发锁防止相互覆盖。

Actions 定时任务可能延迟；公开仓库长期无活动时 GitHub 可能停用 schedule。是否正常运行以 [Actions](https://github.com/xixiaxibro/mcp-radar/actions) 和报告时间为准。仓库管理员禁用 Actions 或限制 token 写权限也会影响更新。

## 边界

- 仅采集公开资料，不查询私人仓库，不运行上游代码，不扫描第三方 MCP 服务。
- 重点 PR 由规则筛选；不是已完成代码审查，也不自动判定漏洞。
- open、draft、merged、closed、prerelease、published 分开记录；merged 不代表包已发布。
- GitHub Discussions、社交媒体、未入 watchlist 的来源和完整互联网不在覆盖保证内。
- RSS 受源保留条数影响；分页被截断或接口失败会进入报告。
- 排名只基于标题、有限摘录、标签、来源和状态；深层 diff 语义需要人工阅读。
- 第三方短摘录保留源链接，原文版权属于原作者；不镜像全文。

原创文档使用 [CC BY 4.0](CONTENT-LICENSE.md)，代码使用 [MIT](LICENSE)。
