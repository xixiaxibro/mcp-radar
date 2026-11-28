# MCP Radar · 2026-11-28 (UTC)

采集时间：2026-11-28T01:20:45+00:00 · 回看窗口：14 天。

这是公开来源的更新索引和选题素材，不是已经审读、复现的技术结论。标题和摘录来自上游；优先级由可见规则计算。

本次窗口内 942 条记录；本日累计 213 个新增/变更版本；失败端点 37 个；覆盖警告 1 个。

## 覆盖与限制

PR merged 表示代码进入分支，不代表已发布；release 不自动证明符合某协议版本。初次运行只建立窗口基线。

仅跟踪 watchlist 中公开仓库的 PR、指定仓库 issue/commit、release、公开安全公告和订阅源。未提供 API 的社区讨论、社交媒体和完整标准文档变更不在覆盖保证内。RSS 仅提供源当前保留的条目。

- 采集失败：`PrefectHQ/fastmcp` / pulls — \[Errno 54\] Connection reset by peer
- 采集失败：`Tencent/AI-Infra-Guard` / pulls — \[Errno 54\] Connection reset by peer
- 采集失败：`awslabs/mcp` / pulls — \[Errno 54\] Connection reset by peer
- 采集失败：`cloudflare/agents` / pulls — \[Errno 54\] Connection reset by peer
- 采集失败：`cloudflare/agents` / releases — \[Errno 54\] Connection reset by peer
- 采集失败：`cloudflare/workers-oauth-provider` / pulls — The read operation timed out
- 采集失败：`cloudflare/workers-sdk` / pulls — The read operation timed out
- 采集失败：`getsentry/toolkit` / pulls — The read operation timed out
- 采集失败：`github/github-mcp-server` / pulls — The read operation timed out
- 采集失败：`lastmile-ai/mcp-agent` / pulls — The read operation timed out
- 采集失败：`microsoft/playwright-mcp` / security-advisories — The read operation timed out
- 采集失败：`modelcontextprotocol/agents-wg` / issues — \[Errno 54\] Connection reset by peer
- 采集失败：`modelcontextprotocol/agents-wg` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/conformance` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/csharp-sdk` / pulls — \[Errno 54\] Connection reset by peer
- 采集失败：`modelcontextprotocol/ext-auth` / commits — The read operation timed out
- 采集失败：`modelcontextprotocol/ext-auth` / security-advisories — The read operation timed out
- 采集失败：`modelcontextprotocol/ext-skills` / security-advisories — The read operation timed out
- 采集失败：`modelcontextprotocol/ext-tasks` / issues — The read operation timed out
- 采集失败：`modelcontextprotocol/go-sdk` / security-advisories — The read operation timed out
- 采集失败：`modelcontextprotocol/inspector` / pulls — \[Errno 54\] Connection reset by peer
- 采集失败：`modelcontextprotocol/java-sdk` / security-advisories — \[Errno 54\] Connection reset by peer
- 采集失败：`modelcontextprotocol/kotlin-sdk` / security-advisories — \[Errno 54\] Connection reset by peer
- 采集失败：`modelcontextprotocol/mcpb` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/modelcontextprotocol` / issues — The read operation timed out
- 采集失败：`modelcontextprotocol/modelcontextprotocol` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/php-sdk` / security-advisories — The read operation timed out
- 采集失败：`modelcontextprotocol/python-sdk` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/registry` / pulls — \[Errno 54\] Connection reset by peer
- 采集失败：`modelcontextprotocol/rust-sdk` / security-advisories — The read operation timed out
- 采集失败：`modelcontextprotocol/servers` / security-advisories — \[Errno 54\] Connection reset by peer
- 采集失败：`modelcontextprotocol/swift-sdk` / security-advisories — \[Errno 54\] Connection reset by peer
- 采集失败：`modelcontextprotocol/transports-wg` / commits — The read operation timed out
- 采集失败：`modelcontextprotocol/transports-wg` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/typescript-sdk` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/typescript-sdk` / releases — The read operation timed out
- 采集失败：`stacklok/toolhive` / releases — The read operation timed out
- 覆盖提示：`modelcontextprotocol/agents-wg` / source — Repository renamed/redirected to modelcontextprotocol/agents-ig

## 重点 PR / 提案

显示 20 / 185 条；全部数据见当日 JSON。

### [Update skill loading approval requirements](https://github.com/modelcontextprotocol/ext-skills/pull/142)

`modelcontextprotocol/ext-skills` · **open** · new · 分数 92 · 上游时间 2026-11-27T18:14:57Z

入选依据：T2 watchlist; breaking: breaking; security: security; protocol: protocol。

> 上游摘录（未审读）：## Motivation and Context Improves security ## Breaking Changes ## Types of changes - \[ \] Bug fix (non-breaking change which fixes an issue) - \[ \] New feature (non-breaking change which adds functionality) - \[ \] Breaking change (fix or feature that would cause existing functionality to change) - \[X\] Documentation update ## Checklist - \[ \] I have read the \[MCP Documentation\](https://modelcontextprotocol.io) - \[ \] My c

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [auth: drop the query from the 2025-03-26 fallback authorization base URL](https://github.com/modelcontextprotocol/go-sdk/pull/1348)

`modelcontextprotocol/go-sdk` · **open** · updated · 分数 80 · 上游时间 2026-11-27T13:54:22Z

入选依据：T2 watchlist; security: authorization; protocol: protocol; proposal: specification。

> 上游摘录（未审读）：When an MCP server publishes no protected resource metadata, 'AuthorizationCodeHandler' falls back to the \[2025-03-26 rule\](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#server-metadata-discovery): the authorization base URL is the MCP server URL with its path discarded. 'getProtectedResourceMetadata' cleared only the path, so a query or fragment on the server URL stayed in the base URL

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs(implementations): add SkillzBench server](https://github.com/modelcontextprotocol/ext-skills/pull/175)

`modelcontextprotocol/ext-skills` · **merged** · new · 分数 74 · 上游时间 2026-11-27T01:58:57Z

入选依据：T2 watchlist; security: oauth; protocol: protocol; merged implementation; verify release separately。

> 上游摘录（未审读）：Adds SkillzBench to the Servers table in 'docs/implementations.md'. - Hosted MCP server at 'https://mcp.skillzbench.com/mcp' (OAuth or API key). A no-login endpoint with a fixed starter set is at 'https://mcp.skillzbench.com/try', which is the easiest way to check the implementation. - Declares 'io.modelcontextprotocol/skills' and implements 'skills/list', 'skills/get' and 'resources/read' on the TypeScript SDK's ext

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(client): cap list\_all\_\* pagination like the MRTR round cap](https://github.com/modelcontextprotocol/rust-sdk/pull/1457)

`modelcontextprotocol/rust-sdk` · **merged** · updated · 分数 74 · 上游时间 2026-11-25T04:40:27Z

入选依据：T2 watchlist; security: token; protocol: mrtr, pagination; merged implementation; verify release separately。

> 上游摘录（未审读）：Fixes #1456 ## Problem 'list\_all\_tools' / 'list\_all\_prompts' / 'list\_all\_resources' / 'list\_all\_resource\_templates' / 'list\_all\_skills' looped until 'next\_cursor' was 'None'. The spec forbids interpreting the cursor value — '""' is a valid cursor — so a peer that keeps returning one (a fresh token per page, the same token again, or a repeated cursor served from the page cache under a positive 'ttlMs') made the walk a

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(git): GHSA-6663-fm5v-gqm5 - Git LFS runs programs named in a repository's own configuration](https://github.com/modelcontextprotocol/servers/pull/5672)

`modelcontextprotocol/servers` · **merged** · new · 分数 74 · 上游时间 2026-11-27T07:24:13Z

入选依据：T2 watchlist; security: security, ghsa-; protocol: protocol; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #5664 Fix for \[GHSA-6663-fm5v-gqm5\](https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-6663-fm5v-gqm5). It was written and reviewed in the advisory's private fork, where a subagent reviewer stood in for Copilot (which cannot review a private fork) until a clean round. Per the advisory flow this PR gets no Copilot review. The private fork has no Actions, so this PR's CI is the first CI run

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(git): GHSA-3whj-m8jj-x97q - the --repository root can be retargeted to another repository through its .git pointer](https://github.com/modelcontextprotocol/servers/pull/5673)

`modelcontextprotocol/servers` · **merged** · new · 分数 74 · 上游时间 2026-11-27T07:41:14Z

入选依据：T2 watchlist; security: security, ghsa-; protocol: protocol; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #5665 Fix for \[GHSA-3whj-m8jj-x97q\](https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-3whj-m8jj-x97q). It was written and reviewed in the advisory's private fork, where a subagent reviewer stood in for Copilot (which cannot review a private fork) until a clean round. Per the advisory flow this PR gets no Copilot review. The private fork has no Actions, so this PR's CI is the first CI run

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(git): GHSA-wvv2-676g-r57j - git\_remote credential redaction bypassed by a tab in a remote name or a prefixed URL](https://github.com/modelcontextprotocol/servers/pull/5674)

`modelcontextprotocol/servers` · **merged** · new · 分数 74 · 上游时间 2026-11-27T07:23:53Z

入选依据：T2 watchlist; security: security, ghsa-; protocol: protocol, sse; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #5666 Fix for \[GHSA-wvv2-676g-r57j\](https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-wvv2-676g-r57j). It was written and reviewed in the advisory's private fork, where a subagent reviewer stood in for Copilot (which cannot review a private fork) until a clean round. Per the advisory flow this PR gets no Copilot review. The private fork has no Actions, so this PR's CI is the first CI run

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(git): GHSA-f33v-89w7-f9vc - repo\_path expands environment variables and error messages disclose their values](https://github.com/modelcontextprotocol/servers/pull/5675)

`modelcontextprotocol/servers` · **merged** · new · 分数 74 · 上游时间 2026-11-27T07:24:23Z

入选依据：T2 watchlist; security: security, ghsa-; protocol: protocol; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #5667 Fix for \[GHSA-f33v-89w7-f9vc\](https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-f33v-89w7-f9vc). It was written and reviewed in the advisory's private fork, where a subagent reviewer stood in for Copilot (which cannot review a private fork) until a clean round. Per the advisory flow this PR gets no Copilot review. The private fork has no Actions, so this PR's CI is the first CI run

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(memory): GHSA-48j5-hj63-c82c - a race on saveGraph's temporary file can change the permissions of a file outside the memory path](https://github.com/modelcontextprotocol/servers/pull/5676)

`modelcontextprotocol/servers` · **merged** · new · 分数 74 · 上游时间 2026-11-27T07:23:30Z

入选依据：T2 watchlist; security: security, ghsa-; protocol: protocol; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #5668 Fix for \[GHSA-48j5-hj63-c82c\](https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-48j5-hj63-c82c). It was written and reviewed in the advisory's private fork, where a subagent reviewer stood in for Copilot (which cannot review a private fork) until a clean round. Per the advisory flow this PR gets no Copilot review. The private fork has no Actions, so this PR's CI is the first CI run

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(git): GHSA-5pwg-5xfw-x322 - a concurrent alternates rewrite lets tools read objects outside --repository](https://github.com/modelcontextprotocol/servers/pull/5677)

`modelcontextprotocol/servers` · **merged** · new · 分数 74 · 上游时间 2026-11-27T08:11:55Z

入选依据：T2 watchlist; security: security, ghsa-; protocol: protocol; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #5669 Fix for \[GHSA-5pwg-5xfw-x322\](https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-5pwg-5xfw-x322). It was written and reviewed in the advisory's private fork, where a subagent reviewer stood in for Copilot (which cannot review a private fork) until a clean round. Per the advisory flow this PR gets no Copilot review. The private fork has no Actions, so this PR's CI is the first CI run

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(fetch): GHSA-g7v6-hfx3-8rv6 - robots.txt check misses backslash and path-parameter spellings (incomplete fix for GHSA-3rxj-6jhw-qfv7)](https://github.com/modelcontextprotocol/servers/pull/5678)

`modelcontextprotocol/servers` · **merged** · new · 分数 74 · 上游时间 2026-11-27T07:23:41Z

入选依据：T2 watchlist; security: security, ghsa-; protocol: protocol, sse; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #5670 Fix for \[GHSA-g7v6-hfx3-8rv6\](https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-g7v6-hfx3-8rv6). It was written and reviewed in the advisory's private fork, where a subagent reviewer stood in for Copilot (which cannot review a private fork) until a clean round. Per the advisory flow this PR gets no Copilot review. The private fork has no Actions, so this PR's CI is the first CI run

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(git): GHSA-qf89-h82f-h5r5 - git\_merge overwrites ignored local files on a merge commit](https://github.com/modelcontextprotocol/servers/pull/5679)

`modelcontextprotocol/servers` · **merged** · new · 分数 74 · 上游时间 2026-11-27T07:24:03Z

入选依据：T2 watchlist; security: security, ghsa-; protocol: protocol; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #5671 Fix for \[GHSA-qf89-h82f-h5r5\](https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-qf89-h82f-h5r5). It was written and reviewed in the advisory's private fork, where a subagent reviewer stood in for Copilot (which cannot review a private fork) until a clean round. Per the advisory flow this PR gets no Copilot review. The private fork has no Actions, so this PR's CI is the first CI run

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Filter SSE list answers on the event stream](https://github.com/stacklok/toolhive/pull/6949)

`stacklok/toolhive` · **merged** · updated · 分数 74 · 上游时间 2026-11-26T17:08:37Z

入选依据：T2 watchlist; security: authorization; protocol: streamable, sse; merged implementation; verify release separately。

> 上游摘录（未审读）：Fixes #6926. Includes the POST-path hardening first proposed in #7211 (closed unmerged). ## Summary \*\*Why:\*\* Over SSE, list answers (tools, prompts, resources, resource templates, skills) reached the client on the GET event stream, which was not filtered. \*\*What:\*\* Each GET event is now filtered as it arrives, with the same per-entry authorization as the streamable path. The filter is picked from the shape of each re

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Make secondary chain legs optionally non-fatal](https://github.com/stacklok/toolhive/pull/7311)

`stacklok/toolhive` · **merged** · updated · 分数 74 · 上游时间 2026-11-26T14:10:22Z

入选依据：T2 watchlist; security: authorization; protocol: cancel; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary - Today any failed leg of a multi-upstream chain ends the whole authorization. A user who cancels a secondary provider's consent screen, or hits a secondary provider outage, gets no authorization code and loses every upstream, the identity provider included. Embedders that already present a missing upstream in-band (for example a connect link in a tool-call response) can complete the authorization without

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Retry LLM proxy test binds that lose their port](https://github.com/stacklok/toolhive/pull/7329)

`stacklok/toolhive` · **merged** · new · 分数 74 · 上游时间 2026-11-26T13:18:55Z

入选依据：T2 watchlist; security: token; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary The LLM proxy tests pick a port with 'freePort', which binds '127.0.0.1:0', closes the listener and returns the port number. 'New' then binds that port. Another test running in parallel can take the port between those two steps. That failed 'TestHandler\_Returns502OnTokenError' in CI with 'bind: address already in use' (seen on #4844, where a re-run passed). - Add 'newProxyOnFreePort'. It builds the config

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Accept a call's messages after its token expires](https://github.com/stacklok/toolhive/pull/7339)

`stacklok/toolhive` · **merged** · new · 分数 74 · 上游时间 2026-11-27T16:25:51Z

入选依据：T2 watchlist; security: authorization, token; protocol: cancel; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary A call-bound access token (an RFC 9396 'authorization\_details' entry of type 'https://toolhive.dev/mcp\_tool\_call') may start one call before its 'exp'. A tool call can run longer than its token lives. Today, every message the client sends for that call after 'exp' gets the token validator's 401. The client then cannot cancel the call, answer an elicitation, reconnect the stream that carries the call's mess

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Bound per-user upstream token reads by context](https://github.com/stacklok/toolhive/pull/7351)

`stacklok/toolhive` · **merged** · new · 分数 74 · 上游时间 2026-11-27T10:03:54Z

入选依据：T2 watchlist; security: token; protocol: timeout; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary - The per-user upstream token read ('GetValidTokensForUser') kept waiting on the refresher after the caller's context ended, up to the refresher's 30s timeout. The refresh-grant guard worked around that with its own goroutine and 'select', so any other caller of the reader would have hung. This moves the bound into the reader. - 'GetValidTokensForUser' returns when the caller's context ends. The refresh ru

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Surface delegated credential errors in vMCP](https://github.com/stacklok/toolhive/pull/7353)

`stacklok/toolhive` · **merged** · new · 分数 74 · 上游时间 2026-11-27T14:12:15Z

入选依据：T2 watchlist; security: token; protocol: transport; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary The delegated credential read (Part of "Ownership-checked credential read for delegated tokens, keyed by user and routed provider") needs a call that fails on the user's credential to look different from a backend failure. Clients should see "connect provider X" or a fixed "credential unavailable", not transport text, workflow wrapping or a Legacy-fallback retry. Today every such failure goes through the g

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [chore: update 0.7.2 changelog with Guard machine identity and token refresh](https://github.com/snyk/agent-scan/pull/573)

`snyk/agent-scan` · **merged** · new · 分数 66 · 上游时间 2026-11-27T10:50:05Z

入选依据：T1 watchlist; security: security, token; merged implementation; verify release separately。

> 上游摘录（未审读）：0.7.2 was never published, so the unreleased changes merged since the release prep go into the same version. --- > \[!NOTE\] > \*\*Low Risk\*\* > Documentation-only change to CHANGELOG.md with no runtime or security behavior changes. > > \*\*Overview\*\* > \*\*Updates the unreleased '0.7.2' changelog entry\*\* so it matches what shipped in the unreleased branch (0.7.2 was not published earlier). > > The \*\*scheduled scan machine-id

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [chore: share one SigV4 redaction-name constant across redaction lists](https://github.com/IBM/mcp-context-forge/pull/7695)

`IBM/mcp-context-forge` · **open** · new · 分数 64 · 上游时间 2026-11-27T13:12:09Z

入选依据：T2 watchlist; security: security, token; protocol: sse。

> 上游摘录（未审读）：# Pull Request ## 🔗 Related Issue Closes #7640 --- ## 📝 Summary Seven places each kept a hand-edited copy of the SigV4 redaction names. A new SigV4 secret name needed an edit in every copy, and a missed copy leaked the value. This PR adds 'SIGV4\_REDACT\_NAMES' in 'mcpgateway/utils/sigv4.py'. It holds 'secret\_access\_key' and 'session\_token' (from 'SIGV4\_SENSITIVE\_KEYS'), 'x-amz-security-token', 'x-amz-signature' and 'x

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 发布与安全公告

显示 15 / 25 条；全部数据见当日 JSON。

### [1.0.7](https://github.com/modelcontextprotocol/inspector/releases/tag/1.0.7)

`modelcontextprotocol/inspector` · **published** · new · 分数 129 · 上游时间 2026-11-27T07:18:52Z

入选依据：T1 watchlist; breaking: deprecat; security: security, ssrf; protocol: protocol, sse; release。

> 上游摘录（未审读）：## What's Changed ### v1.x security fixes 1.0.7 is a security release for the deprecated v1 line. Upgrade with 'npx @modelcontextprotocol/inspector@v1-latest', or move to v2 ('@latest'). \* \*\*The proxy no longer lets a NAT64 or other IPv4-embedding IPv6 address reach cloud metadata.\*\* The SSRF guard used to match IPv6 addresses by how they were written. It now parses each address into its eight 16-bit groups and match

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [2.17.0](https://github.com/modelcontextprotocol/inspector/releases/tag/2.17.0)

`modelcontextprotocol/inspector` · **published** · new · 分数 129 · 上游时间 2026-11-27T10:07:31Z

入选依据：T1 watchlist; breaking: deprecat; security: security, vulnerab, ssrf; protocol: protocol, sse; release。

> 上游摘录（未审读）：## What's Changed ### Security fixes 2.17.0 fixes one vulnerability reported privately against v2. Upgrade with 'npx @modelcontextprotocol/inspector@latest'. It also affects the deprecated v1 line, where it is fixed in 1.0.7 ('@v1-latest'). \* \*\*The SSRF guard now refuses NAT64 and other IPv4-embedding IPv6 addresses that point at cloud metadata.\*\* It used to match IPv6 addresses by how they were written. It now parse

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [OAuth destination guard does not recognize the NAT64 well-known prefix (64:ff9b::/96), letting a malicious MCP server reach cloud metadata on NAT64/DNS64 egress](https://github.com/modelcontextprotocol/inspector/security/advisories/GHSA-v2gx-m79c-pvxj)

`modelcontextprotocol/inspector` · **published** · new · 分数 101 · 上游时间 2026-11-27T10:08:18Z

入选依据：T1 watchlist; security: oauth; protocol: sse; advisory。

> 上游摘录（未审读）：## Summary 'core/mcp/node/fetchGuard.ts''s 'isBlockedAddress()' blocks '169.254.0.0/16', two named cloud-metadata IPv4 addresses, their IPv4-mapped-IPv6 forms, 'fe80::/10' and 'fd00:ec2::254' — but not RFC 6052's NAT64 well-known prefix '64:ff9b::/96', which embeds an IPv4 address in its low 32 bits. A malicious or compromised MCP server that names a NAT64 address (e.g. '64:ff9b::a9fe:a9fe', the NAT64 form of '169.25

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Open redirect via protocol-relative path in trailing-slash middleware](https://github.com/modelcontextprotocol/registry/security/advisories/GHSA-v8vw-gw5j-w7m6)

`modelcontextprotocol/registry` · **published** · new · 分数 101 · 上游时间 2026-11-27T13:36:48Z

入选依据：T1 watchlist; security: vulnerab; protocol: protocol; advisory。

> 上游摘录（未审读）：### Summary The TrailingSlashMiddleware in internal/api/server.go is vulnerable to an open redirect attack. An attacker can craft a URL with a protocol-relative path (e.g., //evil.com/) that, after trailing slash removal, results in a Location header of //evil.com — which browsers interpret as an absolute URL to an external domain. ### Details The TrailingSlashMiddleware strips trailing slashes from request paths and

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v2.5.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.5.0)

`modelcontextprotocol/servers` · **published** · updated · 分数 89 · 上游时间 2026-11-27T21:07:33Z

入选依据：T2 watchlist; security: security, vulnerab; protocol: protocol; release。

> 上游摘录（未审读）：## Security fixes v2.5.0 fixes eight vulnerabilities in three servers. Upgrade 'mcp-server-git' to 2026.11.18, '@modelcontextprotocol/server-filesystem' to 2.4.0 and '@modelcontextprotocol/server-everything' to 2.3.1. \| Package \| Affected \| Fixed in \| \| --- \| --- \| --- \| \| 'mcp-server-git' \| through 2026.11.11 \| 2026.11.18 \| \| '@modelcontextprotocol/server-filesystem' \| all versions before 2.4.0, and date versions 20

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v2.6.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.6.0)

`modelcontextprotocol/servers` · **published** · new · 分数 89 · 上游时间 2026-11-27T09:58:10Z

入选依据：T2 watchlist; security: security, vulnerab; protocol: protocol; release。

> 上游摘录（未审读）：## Security fixes v2.6.0 fixes eight vulnerabilities in three servers, and completes two fixes that v2.5.0 left open. Upgrade 'mcp-server-git' to 2026.11.27, '@modelcontextprotocol/server-memory' to 2.2.2 and 'mcp-server-fetch' to 2026.11.27; on Windows, also '@modelcontextprotocol/server-filesystem' to 2.4.1. \| Package \| Affected \| Fixed in \| \| --- \| --- \| --- \| \| 'mcp-server-git' \| through 2026.11.18 \| 2026.11.27 \|

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Generic OIDC authentication can panic when matching list-valued claims](https://github.com/modelcontextprotocol/registry/security/advisories/GHSA-rxhc-fwc2-57jq)

`modelcontextprotocol/registry` · **published** · new · 分数 81 · 上游时间 2026-11-27T16:48:59Z

入选依据：T1 watchlist; security: token; advisory。

> 上游摘录（未审读）：### Impact MCP Registry deployments using generic OpenID Connect (OIDC) could fail a token exchange when both a configured extra-claim rule and the corresponding claim in a trusted token contained lists of scalar values, such as group names. The comparison could panic during that request. This finding concerns availability of the affected login flow. ### Affected versions and fix Versions '>= 0.0.1, < 1.7.7' are affe

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Generic OIDC authentication could panic when comparing object-valued claims](https://github.com/modelcontextprotocol/registry/security/advisories/GHSA-v3gx-9qjq-qw99)

`modelcontextprotocol/registry` · **published** · new · 分数 81 · 上游时间 2026-11-27T20:30:37Z

入选依据：T1 watchlist; security: token; advisory。

> 上游摘录（未审读）：### Impact In MCP Registry server versions before v1.8.20, a generic OIDC token exchange could panic while comparing an object-valued extra claim with an object-valued rule. This required a deployment configured with an affected rule and an otherwise valid token from its trusted issuer. The confirmed impact was failure of the affected authentication request. The hosted registry uses a scalar Google Workspace domain r

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v4.2.6: Turn of Events](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.6)

`PrefectHQ/fastmcp` · **published** · new · 分数 75 · 上游时间 2026-11-25T03:05:45Z

入选依据：T1 watchlist; protocol: protocol, transport, schema; release。

> 上游摘录（未审读）：This release adds an experimental 'CodeModeClient', which wraps a 'Client' or 'ClientGroup' and runs CodeMode on the client side, so an agent gets the search, schema and execute meta-tools over servers that don't run CodeMode themselves, and one 'execute' block can chain tools across servers. Server spans now carry 'network.transport' and, over HTTP, 'network.protocol.name' and 'network.protocol.version'. Fixes cover

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v4.2.7a1: Slashdance](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.7a1)

`PrefectHQ/fastmcp` · **prerelease** · new · 分数 75 · 上游时间 2026-11-26T01:00:18Z

入选依据：T1 watchlist; protocol: protocol; release。

> 上游摘录（未审读）：Skills proxies now skip discovery on backends that use older MCP protocol versions and keep valid skills when a backend returns malformed entries. FastMCP also accepts percent-encoded slashes in skill URI prefixes, so clients can discover and read skills published under those URIs. Thanks to our 3 contributors. ## What's Changed ### Fixes 🐞 \* Skip legacy backends and omit invalid entries in proxied skills/list by @pa

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v1.8.17](https://github.com/modelcontextprotocol/registry/releases/tag/v1.8.17)

`modelcontextprotocol/registry` · **published** · new · 分数 75 · 上游时间 2026-11-27T10:59:50Z

入选依据：T1 watchlist; protocol: protocol; release。

> 上游摘录（未审读）：## What's Changed \* Prepare staging workload identities for usage jobs by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1911 \* Preview candidate production settings from main by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1913 \* Promote registry v1.8.16 to production by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1912 \* Switch staging usage jobs to

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v1.8.18](https://github.com/modelcontextprotocol/registry/releases/tag/v1.8.18)

`modelcontextprotocol/registry` · **published** · new · 分数 75 · 上游时间 2026-11-27T16:25:45Z

入选依据：T1 watchlist; protocol: protocol; release。

> 上游摘录（未审读）：## What's Changed \* Promote registry v1.8.17 to production by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1925 \* Enforce the publisher metadata size limit on server edits by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1926 \*\*Full Changelog\*\*: https://github.com/modelcontextprotocol/registry/compare/v1.8.17...v1.8.18

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v1.8.19](https://github.com/modelcontextprotocol/registry/releases/tag/v1.8.19)

`modelcontextprotocol/registry` · **published** · new · 分数 75 · 上游时间 2026-11-27T17:25:02Z

入选依据：T1 watchlist; protocol: protocol; release。

> 上游摘录（未审读）：## What's Changed \* Promote registry v1.8.18 to production by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1927 \* Bound distinct package ownership checks on publish and edit by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1928 \*\*Full Changelog\*\*: https://github.com/modelcontextprotocol/registry/compare/v1.8.18...v1.8.19

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v1.8.20](https://github.com/modelcontextprotocol/registry/releases/tag/v1.8.20)

`modelcontextprotocol/registry` · **published** · new · 分数 75 · 上游时间 2026-11-27T20:22:26Z

入选依据：T1 watchlist; protocol: protocol; release。

> 上游摘录（未审读）：## What's Changed \* Promote registry v1.8.19 to production by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1929 \* Validate generic OIDC extra claim types before matching by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1930 \*\*Full Changelog\*\*: https://github.com/modelcontextprotocol/registry/compare/v1.8.19...v1.8.20

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v1.8.21](https://github.com/modelcontextprotocol/registry/releases/tag/v1.8.21)

`modelcontextprotocol/registry` · **published** · new · 分数 75 · 上游时间 2026-11-27T21:34:14Z

入选依据：T1 watchlist; protocol: protocol; release。

> 上游摘录（未审读）：## What's Changed \* Promote registry v1.8.20 to production by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1931 \* Bound server record and nested string sizes on publish and edit by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1932 \* Apply publish size limits to /validate on both API versions by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1933 \*\*Ful

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 协议 / 工作组提交

显示 3 / 3 条；全部数据见当日 JSON。

### [docs: link roadmap to release cycle (#3549)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/c0bdba6e1e168f8e3b3198be03282c4c0065837f)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 55 · 上游时间 2026-11-27T20:48:42Z

入选依据：T1 watchlist; protocol: protocol, sse。

> 上游摘录（未审读）：docs: link roadmap to release cycle (#3549) Adds a direct link from the roadmap to '/community/release-cycle' so readers can find the release schedule and SEP timing. Depends on https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3550, which adds the new page and must merge first. Validation: 'npm run prep' passes with the proposed page and its images temporarily present. Those files are not included in

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add OpenCode to the extension client matrix (#3595)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/bd5bc16fb0b4eee9e0a1994ffaa1d67f213865ac)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 51 · 上游时间 2026-11-27T17:21:14Z

入选依据：T1 watchlist; proposal: extension。

> 上游摘录（未审读）：docs: add OpenCode to the extension client matrix (#3595) \_Requested by \*\*Peter\*\* · \[project thread\](https://claude.ai/code/project/chan\_013VZyPu2nt8YAcwA65s6UqV?thread=cmsg\_013VZyPu2nt8YAcwA65s6UqV1JLFG6FjRyFjTm74P4oiBo)\_ ## Summary Adds an OpenCode row to the extension client matrix: - \*\*Skills:\*\* supported, from anomalyco/opencode#66201. It is behind OpenCode's experimental 'mcp\_skills' flag. - \*\*Events:\*\* Partial

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add a site-wide Discord banner (#3597)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/fdc75bd0668db05f5b43e4fc76c2e5aa54296a42)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 35 · 上游时间 2026-11-27T21:20:47Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：docs: add a site-wide Discord banner (#3597) Adds a dismissible site-wide banner to the docs that links to the MCP Contributor Discord, using Mintlify's 'banner' setting in 'docs/docs.json'.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 文章与技术解释

显示 0 / 0 条；全部数据见当日 JSON。

本日暂无记录。

## 博客选题工作台

从上面的重点项挑选，不自动把提案写成已实现功能：

- 协议问题：规范原文、提案状态、旧行为与新行为。
- 实现证据：PR diff、回归测试、客户端/服务端版本。
- 复现：最小实验、消息/HTTP trace、失败与成功条件。
- 结论边界：事实、维护者解释、个人判断分别记录。

模板：[知识库写作模板](https://github.com/xixiaxibro/mcp-knowledge-base/tree/main/templates)。
