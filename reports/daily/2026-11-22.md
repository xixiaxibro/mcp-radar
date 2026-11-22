# MCP Radar · 2026-11-22 (UTC)

采集时间：2026-11-22T01:17:07+00:00 · 回看窗口：14 天。

这是公开来源的更新索引和选题素材，不是已经审读、复现的技术结论。标题和摘录来自上游；优先级由可见规则计算。

本次窗口内 2303 条记录；本日累计 170 个新增/变更版本；失败端点 0 个；覆盖警告 1 个。

## 覆盖与限制

PR merged 表示代码进入分支，不代表已发布；release 不自动证明符合某协议版本。初次运行只建立窗口基线。

仅跟踪 watchlist 中公开仓库的 PR、指定仓库 issue/commit、release、公开安全公告和订阅源。未提供 API 的社区讨论、社交媒体和完整标准文档变更不在覆盖保证内。RSS 仅提供源当前保留的条目。

- 覆盖提示：`modelcontextprotocol/agents-wg` / source — Repository renamed/redirected to modelcontextprotocol/agents-ig

## 重点 PR / 提案

显示 20 / 161 条；全部数据见当日 JSON。

### [docs: update Discord invite link](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3577)

`modelcontextprotocol/modelcontextprotocol` · **merged** · new · 分数 102 · 上游时间 2026-11-22T00:30:26Z

入选依据：T1 watchlist; security: security; protocol: protocol; proposal: sep-; merged implementation; verify release separately。

> 上游摘录（未审读）：Replaces the old Discord invite ('discord.gg/6CSzBmMkjX') with 'https://discord.gg/modelcontextprotocol' across the blog, docs, 'SECURITY.md', and SEP-2149.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Add refresh token reuse detection and family revocation to OAuthProxy](https://github.com/PrefectHQ/fastmcp/pull/6660)

`PrefectHQ/fastmcp` · **closed** · new · 分数 84 · 上游时间 2026-11-21T22:09:55Z

入选依据：T1 watchlist; breaking: backward, compatib; security: oauth, token。

> 上游摘录（未审读）：Added refresh-token reuse detection to 'OAuthProxy' (OAuth 2.1 §4.3.1): - Added optional 'active\_access\_jti', 'active\_refresh\_jti', and 'active\_refresh\_token\_hash' fields to 'UpstreamTokenSet' and 'rotated\_at' to 'JTIMapping' in 'fastmcp.server.auth.oauth\_proxy.models' (defaulting to 'None' for backwards compatibility with existing stored records). - During 'exchange\_refresh\_token()', the losing atomic 'delete()' rac

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Add client\_registration\_ttl option to OAuthProxy and OIDCProxy](https://github.com/PrefectHQ/fastmcp/pull/6659)

`PrefectHQ/fastmcp` · **closed** · new · 分数 76 · 上游时间 2026-11-21T22:04:34Z

入选依据：T1 watchlist; security: oauth; protocol: sse。

> 上游摘录（未审读）：Added an optional 'client\_registration\_ttl: int \| None = None' parameter to 'OAuthProxy' (and forwarded it through 'OIDCProxy') so persistent client stores can bound the lifetime of unauthenticated DCR registrations. 'register\_client()' passes 'ttl=self.\_client\_registration\_ttl' when storing 'ProxyDCRClient' records in 'self.\_client\_store', and active DCR clients have their registration TTL refreshed via '\_renew\_clie

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix: redact task context credentials from repr](https://github.com/PrefectHQ/fastmcp/pull/6666)

`PrefectHQ/fastmcp` · **closed** · new · 分数 76 · 上游时间 2026-11-22T01:10:25Z

入选依据：T1 watchlist; security: token; protocol: sse。

> 上游摘录（未审读）：Fixes #6631 ## Summary - exclude serialized access tokens and HTTP headers from 'TaskContextSnapshot.\_\_repr\_\_' - preserve both sensitive fields for JSON serialization, equality, and worker restoration - add a regression test proving bearer credentials are absent from the representation ## Testing - isolated 'TaskContextSnapshot' repr regression passed - 'python -m ruff check fastmcp\_tasks/fastmcp\_tasks/context.py tes

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Add image to README for visual enhancement](https://github.com/github/github-mcp-server/pull/3913)

`github/github-mcp-server` · **closed** · new · 分数 76 · 上游时间 2026-11-21T08:10:44Z

入选依据：T1 watchlist; security: security, token; protocol: schema。

> 上游摘录（未审读）：## Summary ## Why Fixes # ## What changed - - ## MCP impact - \[ \] No tool or API changes - \[ \] Tool schema or behavior changed - \[ \] New tool added ## Prompts tested (tool changes only) - ## Security / limits - \[ \] No security or limits impact - \[ \] Auth / permissions considered - \[ \] Data exposure, filtering, or token/size limits considered ## Tool renaming - \[ \] I am renaming tools as part of this PR (e.g. a part o

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Pending changes exported from your codespace](https://github.com/github/github-mcp-server/pull/3921)

`github/github-mcp-server` · **open** · new · 分数 76 · 上游时间 2026-11-21T21:42:29Z

入选依据：T1 watchlist; security: security, token; protocol: schema。

> 上游摘录（未审读）：## Summary ## Why Fixes # ## What changed - - ## MCP impact - \[ \] No tool or API changes - \[ \] Tool schema or behavior changed - \[ \] New tool added ## Prompts tested (tool changes only) - ## Security / limits - \[ \] No security or limits impact - \[ \] Auth / permissions considered - \[ \] Data exposure, filtering, or token/size limits considered ## Tool renaming - \[ \] I am renaming tools as part of this PR (e.g. a part o

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Redeem OAuth proxy codes and refresh tokens once under concurrency](https://github.com/PrefectHQ/fastmcp/pull/6614)

`PrefectHQ/fastmcp` · **merged** · new · 分数 66 · 上游时间 2026-11-21T02:41:26Z

入选依据：T1 watchlist; security: oauth, authorization, token; merged implementation; verify release separately。

> 上游摘录（未审读）：\_Requested by \*\*nate\*\* · \[project thread\](https://claude.ai/code/project/chan\_01EkwKAptPX4vtXECnAMud7W?thread=cmsg\_01EkwKAptPX4vtXECnAMud7W3ESW5AxBi1SuchpSGJaTFh)\_ ## Description Two overlapping '/token' requests could both redeem one authorization code or refresh token, because the proxy read the record and deleted it without checking that the delete removed anything. Both paths now require 'delete()' to report remo

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Keep a revoked OAuth proxy access token revoked after a refresh](https://github.com/PrefectHQ/fastmcp/pull/6620)

`PrefectHQ/fastmcp` · **merged** · new · 分数 66 · 上游时间 2026-11-21T04:48:26Z

入选依据：T1 watchlist; security: oauth, token; merged implementation; verify release separately。

> 上游摘录（未审读）：\_Requested by \*\*nate\*\* · \[project thread\](https://claude.ai/code/project/chan\_019cwEtYLabHxMVmRUt5Ds2g?thread=cmsg\_019cwEtYLabHxMVmRUt5Ds2g5pkRq1TttdZcjUaPkx1J9J)\_ Every FastMCP access token the OAuth proxy issues for one grant maps, through its JTI, to the grant's single upstream token record, and a refresh rewrites that record with the new upstream token. Revoking an access token revoked the upstream token and left

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [End a grant's access tokens when its refresh token is revoked](https://github.com/PrefectHQ/fastmcp/pull/6627)

`PrefectHQ/fastmcp` · **merged** · new · 分数 66 · 上游时间 2026-11-22T00:31:48Z

入选依据：T1 watchlist; security: oauth, token; merged implementation; verify release separately。

> 上游摘录（未审读）：\_Requested by \*\*nate\*\* · \[project thread\](https://claude.ai/code/project/chan\_01EkwKAptPX4vtXECnAMud7W?thread=cmsg\_01EkwKAptPX4vtXECnAMud7W3ESW5AxBi1SuchpSGJaTFh)\_ Revoking an OAuth proxy refresh token removed the refresh token and revoked the upstream refresh token, but the access tokens issued alongside it kept validating until they expired. That's a logout that doesn't log out: a client that revokes its refresh to

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: remove PostHog Code from the extension support matrix](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/3576)

`modelcontextprotocol/modelcontextprotocol` · **open** · new · 分数 66 · 上游时间 2026-11-22T00:37:36Z

入选依据：T1 watchlist; protocol: protocol; proposal: extension。

> 上游摘录（未审读）：### What's broken? The documentation is wrong or misleading ### Where in the spec or docs? https://modelcontextprotocol.io/extensions/client-matrix ### What should happen? PostHog Code should not appear in the extension support matrix. ### What actually happens? The matrix lists PostHog Code as supporting MCP Apps. PostHog is withdrawing this listing. We're not working on PostHog Code anymore and, therefore, doesn't

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [sep(SEP-2792): Per-Request User Language Preference](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2792)

`modelcontextprotocol/modelcontextprotocol` · **open** · updated · 分数 66 · 上游时间 2026-11-21T08:04:13Z

入选依据：T1 watchlist; protocol: protocol, transport; proposal: sep-。

> 上游摘录（未审读）：## Summary SEP-2792 defines transport-neutral propagation of a user's natural-language preference on each MCP request: - 'params.\_meta\["io.modelcontextprotocol/acceptLanguage"\]' reuses the HTTP 'Accept-Language' grammar and semantics, including weighted language ranges and wildcard matching under \[RFC 4647\]. - Response '\_meta\["io.modelcontextprotocol/contentLanguage"\]' reports the language actually used with 'Content

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [chore: remove outdated tests/compliance suite](https://github.com/IBM/mcp-context-forge/pull/5935)

`IBM/mcp-context-forge` · **open** · updated · 分数 64 · 上游时间 2026-11-21T11:28:05Z

入选依据：T2 watchlist; security: authorization; protocol: protocol, transport, lifecycle。

> 上游摘录（未审读）：Closes #5835 ## Summary The old 'tests/compliance/mcp\_2025\_11\_25/' tree was excluded from the default pytest run and duplicated the live-gateway suite's coverage of the same surfaces (lifecycle, transport semantics, ping/notifications, discovery, PRM/authorization). Reworked on top of #6125, which landed first and removed 'tests/live\_gateway/protocol\_compliance/' along with the 'make test-protocol-compliance\*' target

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(well-architected-security): stop print() from corrupting stdio](https://github.com/awslabs/mcp/pull/5037)

`awslabs/mcp` · **open** · updated · 分数 64 · 上游时间 2026-11-21T20:25:13Z

入选依据：T2 watchlist; security: security; protocol: stdio。

> 上游摘录（未审读）：﻿ Fixes #4991 ## Summary ### Changes The well-architected-security-mcp-server runs over stdio, where stdout carries the JSON-RPC stream. The tool code path had 151 bare 'print()' calls across 'server.py' (43), 'util/security\_services.py' (46), 'util/network\_security.py' (32) and 'util/storage\_security.py' (30), and each one wrote plain text into that stream. This change replaces them with 'loguru' logger calls. 'serv

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(client): cap list\_all\_\* pagination like the MRTR round cap](https://github.com/modelcontextprotocol/rust-sdk/pull/1457)

`modelcontextprotocol/rust-sdk` · **open** · updated · 分数 64 · 上游时间 2026-11-21T17:30:01Z

入选依据：T2 watchlist; security: token; protocol: mrtr, pagination。

> 上游摘录（未审读）：Fixes #1456 ## Problem 'list\_all\_tools' / 'list\_all\_prompts' / 'list\_all\_resources' / 'list\_all\_resource\_templates' / 'list\_all\_skills' looped until 'next\_cursor' was 'None'. The spec forbids interpreting the cursor value — '""' is a valid cursor — so a peer that keeps returning one (a fresh token per page, the same token again, or a repeated cursor served from the page cache under a positive 'ttlMs') made the walk a

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Filter SSE list answers on the event stream](https://github.com/stacklok/toolhive/pull/6949)

`stacklok/toolhive` · **open** · updated · 分数 64 · 上游时间 2026-11-21T23:33:06Z

入选依据：T2 watchlist; security: authorization; protocol: streamable, sse。

> 上游摘录（未审读）：Fixes #6926. ## Summary \*\*Why:\*\* Over SSE, list answers (tools, prompts, resources, resource templates, skills) reached the client on the GET event stream, which was not filtered. \*\*What:\*\* Each GET event is now filtered as it arrives, with the same per-entry authorization as the streamable path. The filter is picked from the shape of each result. ## Does this introduce a user-facing change? - \*\*SSE list answers.\*\* B

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Keep the caller's object when a merged default breaks it](https://github.com/PrefectHQ/fastmcp/pull/6582)

`PrefectHQ/fastmcp` · **merged** · updated · 分数 60 · 上游时间 2026-11-21T02:00:45Z

入选依据：T1 watchlist; protocol: schema; merged implementation; verify release separately。

> 上游摘录（未审读）：\_Requested by \*\*nate\*\* · \[project thread\](https://claude.ai/code/project/chan\_019cwEtYLabHxMVmRUt5Ds2g?thread=cmsg\_019cwEtYLabHxMVmRUt5Ds2g47c1hg8Cirkva2mCFgmnaZ)\_ ## Description When a tool's output schema gives an object property an object 'default', the client merges that default into whatever object the server sent. That's fine until the default itself doesn't satisfy the schema: with typed 'additionalProperties'

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [refactor(chat): one turn core for AIChatAgent and Think](https://github.com/cloudflare/agents/pull/2868)

`cloudflare/agents` · **merged** · updated · 分数 60 · 上游时间 2026-11-21T13:13:08Z

入选依据：T1 watchlist; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：'AIChatAgent' and 'Think' now run their turns on one shared core, 'ChatTurns' in 'agents/chat'. It owns the turn queue, abort registry, submit concurrency, continuation slots, pre-stream set and tool-result apply chain, plus the rules across them, and it runs a client chat request start to finish ('runClientRequest'). Where the two classes behaved differently for no chosen reason, both now do the stricter thing. No p

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [refactor(chat): one recovery attempt sequence for AIChatAgent and Think](https://github.com/cloudflare/agents/pull/2873)

`cloudflare/agents` · **merged** · updated · 分数 60 · 上游时间 2026-11-21T13:13:08Z

入选依据：T1 watchlist; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：'AIChatAgent' and 'Think' now run chat recovery through the shared 'ChatRecoveryEngine'. It owns three sequences both classes used to write out themselves: a recovery attempt ('recovery-attempt.ts'), the routing of a live stall or transient error into recovery ('recovery-route.ts'), and the dispatch of a recovery callback. Each host binds its turn machinery once in the adapter and passes hooks for what differs, which

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [refactor(chat): the auto-continuation turn runs and settles in the turn core](https://github.com/cloudflare/agents/pull/2876)

`cloudflare/agents` · **merged** · updated · 分数 60 · 上游时间 2026-11-21T13:13:10Z

入选依据：T1 watchlist; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：On top of #2870, the auto-continuation turn moves into the turn core. 'ChatTurns.runContinuationTurn' owns it from the moment a tool result fires it to the moment it settles, and both classes run it through the turn body #2870 gave every other turn ('\_runServerTurnReply', '\_runModelTurn'). 'Think''s connection-less continuation is the same turn with no pending continuation. 'AIChatAgent' and 'Think' each wrote this l

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(chat): a stop drops the continuations that were waiting when it landed](https://github.com/cloudflare/agents/pull/2881)

`cloudflare/agents` · **merged** · updated · 分数 60 · 上游时间 2026-11-21T13:13:10Z

入选依据：T1 watchlist; protocol: sse, cancel; merged implementation; verify release separately。

> 上游摘录（未审读）：On top of #2876: stopping the turn that is running also drops the auto-continuations that were waiting when the stop landed. A tool result answered while the reply streamed, or one that arrived while a continuation ran before it was stopped, no longer starts the model again. The drop is one place in the turn core ('ChatTurns.cancel', 'stopAll', 'linkExternal'), for 'AIChatAgent' and 'Think'. Both classes did the oppo

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 发布与安全公告

显示 5 / 5 条；全部数据见当日 JSON。

### [v4.2.4: Burn After Reading](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.4)

`PrefectHQ/fastmcp` · **published** · new · 分数 109 · 上游时间 2026-11-21T05:24:22Z

入选依据：T1 watchlist; breaking: breaking; security: ghsa-, oauth, authorization; release。

> 上游摘录（未审读）：Fixes a race where two concurrent token requests could redeem one OAuth proxy authorization code or refresh token twice (GHSA-78c8-3jhx-5mg7), and keeps a revoked proxy access token from validating again after a refresh. Also, a tool transform that can't apply now hides only its own tool instead of breaking every listing, plus a few mounted and versioned component fixes. Thanks to our 4 contributors, including 2 firs

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [OAuthProxy redeems one authorization code more than once under concurrency](https://github.com/PrefectHQ/fastmcp/security/advisories/GHSA-78c8-3jhx-5mg7)

`PrefectHQ/fastmcp` · **published** · new · 分数 81 · 上游时间 2026-11-21T05:31:47Z

入选依据：T1 watchlist; security: oauth, authorization, token; advisory。

> 上游摘录（未审读）：### Summary 'OAuthProxy' consumes an authorization code with a non-atomic get-then-delete on its code store. When two token requests present the same code concurrently, both read it before either deletes it, and the proxy issues two independent tokens from one code. This breaks single-use (RFC 6749 §4.1.2). The default, out-of-the-box configuration is affected; no special backend is required. ### Details 'exchange\_au

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v1.8.11](https://github.com/modelcontextprotocol/registry/releases/tag/v1.8.11)

`modelcontextprotocol/registry` · **published** · new · 分数 75 · 上游时间 2026-11-21T14:26:05Z

入选依据：T1 watchlist; protocol: protocol; release。

> 上游摘录（未审读）：## What's Changed \* Increase isolated production database to eight vCPUs by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1873 \* Promote registry v1.8.10 to production by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1874 \* Provision the UI-built Grafana dashboards from the repository by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1875 \* Provision th

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Docker Desktop host-access IP bypasses ToolHive's default egress-proxy host isolation](https://github.com/stacklok/toolhive/security/advisories/GHSA-3x8v-rx4w-6mf9)

`stacklok/toolhive` · **published** · new · 分数 63 · 上游时间 2026-11-21T20:39:53Z

入选依据：T2 watchlist; protocol: sse; advisory。

> 上游摘录（未审读）：### Summary With network isolation enabled (the default) and the default 'network' permission profile, ToolHive's egress proxy is meant to keep a containerized MCP workload from reaching host-local services. It blocks the host by \*\*hostname\*\* ('host.docker.internal', 'gateway.docker.internal', 'host.containers.internal') and by the \*\*collected Docker bridge-gateway IPs\*\*. On the \*\*Docker runtime\*\*, however, the Docke

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v0.67.1](https://github.com/stacklok/toolhive/releases/tag/v0.67.1)

`stacklok/toolhive` · **published** · new · 分数 43 · 上游时间 2026-11-21T20:32:07Z

入选依据：T2 watchlist; release。

> 上游摘录（未审读）：## What's Changed \* Confine .thvignore overlays to the mounted directory by @rdimitrov in https://github.com/stacklok/toolhive/pull/7196 \* Refuse ID-JAGs with a multi-valued aud by @jhrozek in https://github.com/stacklok/toolhive/pull/7204 \* Release v0.67.1 by @toolhive-release-app\[bot\] in https://github.com/stacklok/toolhive/pull/7212 \*\*Full Changelog\*\*: https://github.com/stacklok/toolhive/compare/v0.67.0...v0.67.1

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 协议 / 工作组提交

显示 4 / 4 条；全部数据见当日 JSON。

### [docs: update Discord invite link (#3577)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/af66e6fd44a2b8f945d90a4c4ff1086cd5fbd2e1)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 97 · 上游时间 2026-11-22T00:30:23Z

入选依据：T1 watchlist; security: security; protocol: protocol; proposal: sep-。

> 上游摘录（未审读）：docs: update Discord invite link (#3577) Replaces the old Discord invite ('discord.gg/6CSzBmMkjX') with 'https://discord.gg/modelcontextprotocol' across the blog, docs, 'SECURITY.md', and SEP-2149.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: align FSIG charter with problem-first, WG-led governance (#3572)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/2f3a95074916f092cd58dc06ede6a748f681a6ef)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 51 · 上游时间 2026-11-21T05:32:38Z

入选依据：T1 watchlist; proposal: extension。

> 上游摘录（未审读）：docs: align FSIG charter with problem-first, WG-led governance (#3572) ## Summary Proposes an amendment to the Financial Services Interest Group charter to make problem identification, sharing existing MCP implementation approaches, and routing unresolved needs to WGs the default path. - Preserve exploratory solution discussions, prototypes, and extension work where useful for validating requirements. - Prefer existi

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add Archestra.AI and mcp-use to the extension client matrix (#3574)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/862397cec702e8f828713071da501cf56158e8fc)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 51 · 上游时间 2026-11-22T00:31:13Z

入选依据：T1 watchlist; proposal: extension。

> 上游摘录（未审读）：docs: add Archestra.AI and mcp-use to the extension client matrix (#3574) Fills in Skills support for Archestra and also adds a row for mcp-use, covering both Apps and Skills. - Archestra.AI, Skills: \[Skills from MCP Servers\](https://archestra.ai/docs/agents/skills/importing) - mcp-use, MCP Apps: \[Debug widgets in the Inspector\](https://docs.mcp-use.com/inspector/debugging-chatgpt-apps) --------- Co-authored-by: Clau

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs(community): say who can open GitHub Discussions and what they are for (#3573)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/b7e13978aa0bd092baa98190d58825e7863d6ee1)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 35 · 上游时间 2026-11-21T18:39:40Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：docs(community): say who can open GitHub Discussions and what they are for (#3573) \*\*Before:\*\* The Channels table on the Communication page lists GitHub Discussions for "Ideas, feature requests with rationale, questions, roadmap discussion, announcements and releases, and meeting agendas and notes". \*\*After:\*\* The row lists meeting agendas and notes, in the Meeting Notes categories, and announcements. It says only pe

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
