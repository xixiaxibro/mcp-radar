# MCP Radar · 2026-11-12 (UTC)

采集时间：2026-11-12T01:32:11+00:00 · 回看窗口：14 天。

这是公开来源的更新索引和选题素材，不是已经审读、复现的技术结论。标题和摘录来自上游；优先级由可见规则计算。

本次窗口内 2138 条记录；本日累计 471 个新增/变更版本；失败端点 4 个；覆盖警告 0 个。

## 覆盖与限制

PR merged 表示代码进入分支，不代表已发布；release 不自动证明符合某协议版本。初次运行只建立窗口基线。

仅跟踪 watchlist 中公开仓库的 PR、指定仓库 issue/commit、release、公开安全公告和订阅源。未提供 API 的社区讨论、社交媒体和完整标准文档变更不在覆盖保证内。RSS 仅提供源当前保留的条目。

- 采集失败：`PrefectHQ/fastmcp` / pulls — The read operation timed out
- 采集失败：`awslabs/mcp` / releases — The read operation timed out
- 采集失败：`github/github-mcp-server` / pulls — The read operation timed out
- 采集失败：`snyk/agent-scan` / pulls — The read operation timed out

## 重点 PR / 提案

显示 20 / 439 条；全部数据见当日 JSON。

### [docs: architecture spec page still presents sampling as a core feature, but is depricated](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/3548)

`modelcontextprotocol/modelcontextprotocol` · **open** · new · 分数 94 · 上游时间 2026-11-12T00:32:35Z

入选依据：T1 watchlist; breaking: deprecat; protocol: protocol; proposal: sep-, specification。

> 上游摘录（未审读）：### What's broken? The documentation is wrong or misleading ### Where in the spec or docs? https://modelcontextprotocol.io/specification/draft/architecture ### What should happen? The architecture page should not present Sampling as a core, current feature. SEP-2577 deprecates Sampling and Roots as of '2026-07-28', and they are listed in the \[deprecated features registry\](https://modelcontextprotocol.io/specification

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(server): add SEP-2350 scope challenge scenario](https://github.com/modelcontextprotocol/conformance/pull/481)

`modelcontextprotocol/conformance` · **open** · new · 分数 92 · 上游时间 2026-11-10T21:54:13Z

入选依据：T1 watchlist; security: oauth, token; protocol: sse, conformance; proposal: sep-。

> 上游摘录（未审读）：## Summary - add a language-neutral server conformance scenario for request-time OAuth 'insufficient\_scope' challenges - exercise 'tools/call', static and templated 'resources/read', and 'prompts/get' with a fixed cross-SDK fixture contract - assert HTTP 403, \*\*\*\*\*\* parameters, the complete required scope set in one challenge, and successful upgraded-token retries - restore 'sep-2350-server-single-challenge' traceabi

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [sep(SEP-3543): make the MCP project a CVE Numbering Authority](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3543)

`modelcontextprotocol/modelcontextprotocol` · **open** · new · 分数 92 · 上游时间 2026-11-11T13:49:40Z

入选依据：T1 watchlist; security: security; protocol: protocol; proposal: sep-, specification。

> 上游摘录（未审读）：Proposes that the MCP project applies to the CVE Program to become a CVE Numbering Authority (CNA), so that maintainers assign CVE IDs and publish CVE records for the specification and the 'modelcontextprotocol' repositories without waiting on GitHub's CNA queue. Reports still arrive through GitHub Security Advisories. Only the party that assigns the ID and publishes the record changes. The SEP is in 'seps/0000-mcp-a

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[Client\] Add an 'auth' parameter to 'HttpTransport' with 'BearerToken'](https://github.com/modelcontextprotocol/php-sdk/pull/663)

`modelcontextprotocol/php-sdk` · **merged** · updated · 分数 92 · 上游时间 2026-11-10T12:27:10Z

入选依据：T3 watchlist; breaking: breaking; security: authorization, token; protocol: transport; merged implementation; verify release separately。

> 上游摘录（未审读）：Part of #316 - first slice of the client authorization in chr-hertel/php-sdk#53, which is too big to review in one go. Pass 'auth:' to 'HttpTransport' and every request gets authenticated, a refused one gets retried if the authenticator can do something about it: '''php $transport = new HttpTransport('https://mcp.example.com/mcp', auth: new BearerToken($accessToken)); ''' 'BearerToken' is the only implementation for

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[Server\] Answer an oversized body in 'AuthorizationMiddleware' with '413'](https://github.com/modelcontextprotocol/php-sdk/pull/699)

`modelcontextprotocol/php-sdk` · **merged** · updated · 分数 92 · 上游时间 2026-11-10T12:26:34Z

入选依据：T3 watchlist; breaking: breaking; security: authorization; protocol: transport; merged implementation; verify release separately。

> 上游摘录（未审读）：With a 'ScopePolicy' that has method or tool rules, 'AuthorizationMiddleware' answered a body over its 'maxBodyBytes' with '400' and a 'WWW-Authenticate' challenge - it now logs a warning and answers '413' with a JSON-RPC error, like the transports. The middleware is built before the transport and can't see its limit, so the docs say to set both. \[BC Break\] The status of that answer changes from '400' to '413'.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(deploy): repair Gateway access-log sampling regexes](https://github.com/modelcontextprotocol/registry/pull/1846)

`modelcontextprotocol/registry` · **merged** · new · 分数 88 · 上游时间 2026-11-10T23:53:21Z

入选依据：T1 watchlist; breaking: migration; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：## Problem The Cloud Logging exclusion that keeps about 10% of fast successful Gateway listing records has matched nothing since the Gateway migration, so every access record is being ingested. 'gatewayAccessLogExclusionFilter' is a Go raw string, but its two regexes use doubled backslashes ('\\\\.', '\\\\?'), the way the legacy filter in 'deploy/pkg/traffic/policy.json' has to for JSON. Cloud Logging passes backslashes

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(deploy): log user agent and content encoding at the Gateway](https://github.com/modelcontextprotocol/registry/pull/1851)

`modelcontextprotocol/registry` · **merged** · new · 分数 88 · 上游时间 2026-11-11T14:27:09Z

入选依据：T1 watchlist; breaking: migration; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：## Why About 85% of the registry's outbound traffic goes to one integration, and nearly all of it is uncompressed. Working that out took pre-migration ingress logs (the last ones with a user agent) and inferring compression from response sizes, because the Gateway's JSON access record has neither field. We have asked that integration to send 'Accept-Encoding: gzip' and sync incrementally. These fields let us see when

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(mcp): coordinate OAuth callbacks, refreshes, step-ups and server changes](https://github.com/cloudflare/agents/pull/2863)

`cloudflare/agents` · **merged** · updated · 分数 86 · 上游时间 2026-11-11T17:21:47Z

入选依据：T1 watchlist; security: oauth, authorization, token; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：This fixes races in the MCP client where OAuth callbacks, token refreshes, step-ups and server changes ('closeConnection', 'removeServer', 'migrateServerId', 'configureElicitationHandlers') overlap. Each fix is its own commit with a replay test, mostly in 'authorization-races.test.ts'. Every replay fails on 'main' and passes after its commit. TLA+ models of the module found them. What each did on 'main': - a token re

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v2: Block cloud metadata addresses outside 169.254.0.0/16 in the fetch guard (GHSA-fvg8-f358-w2c8)](https://github.com/modelcontextprotocol/inspector/pull/2942)

`modelcontextprotocol/inspector` · **merged** · new · 分数 86 · 上游时间 2026-11-11T18:47:28Z

入选依据：T1 watchlist; security: ghsa-; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #2947 > The fix was developed and reviewed in the advisory's private fork. These are the reviewed commits, pushed here unchanged. Tracking issue: #2947. Fix for GHSA-fvg8-f358-w2c8 on the v2 line. ## Change 'isBlockedAddress' ('core/mcp/node/fetchGuard.ts') blocked only IPv4 link-local ('169.254.0.0/16') on the IPv4 side. That left reachable the cloud metadata services that sit at a fixed address outside that

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v1: Block cloud metadata addresses outside 169.254.0.0/16 in the proxy guard (GHSA-fvg8-f358-w2c8)](https://github.com/modelcontextprotocol/inspector/pull/2943)

`modelcontextprotocol/inspector` · **merged** · new · 分数 86 · 上游时间 2026-11-11T18:48:11Z

入选依据：T1 watchlist; security: security, ghsa-; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #2951 > The fix was developed and reviewed in the advisory's private fork. These are the reviewed commits, pushed here unchanged. Tracking issue: #2951. Fix for GHSA-fvg8-f358-w2c8 on the v1 line. ## Change 'isBlockedProxyAddress' ('server/src/proxy-security.ts') blocked only IPv4 link-local ('169.254.0.0/16') on the IPv4 side. That left reachable the cloud metadata services that sit at a fixed address outside

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Show env values in the server.json launch preview and confirm runtime-control vars](https://github.com/modelcontextprotocol/inspector/pull/2945)

`modelcontextprotocol/inspector` · **merged** · new · 分数 86 · 上游时间 2026-11-11T21:05:37Z

入选依据：T1 watchlist; security: ghsa-; protocol: sse, stdio; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #2949 > The fix was developed and reviewed in the advisory's private fork. These are the reviewed commits, pushed here unchanged. Tracking issue: #2949. Fix for GHSA-pp85-586h-2m95 (v2 only, affects <= 2.14.0). ## Problem Importing a registry 'server.json' copies each declared environment variable's 'default'/'value' into the saved config's 'env', and the stdio spawn passes it to the launched process. The impo

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(oauth): prefer Client ID Metadata Documents over DCR](https://github.com/IBM/mcp-context-forge/pull/7443)

`IBM/mcp-context-forge` · **merged** · updated · 分数 82 · 上游时间 2026-11-11T11:46:30Z

入选依据：T2 watchlist; breaking: deprecat; security: oauth, authorization; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #5692 Closes #7412 MCP 2026-07-28 deprecates Dynamic Client Registration (RFC 7591) in favor of Client ID Metadata Documents (CIMD). The gateway now prefers CIMD when connecting to upstream authorization servers, retaining DCR as a fallback. ## Registration Strategy ''' GET /oauth/authorize/{gateway\_id} -> load gateway, check access -> oauth\_config has client\_id? -> yes -> use pre-configured credentials -> no

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[Server\] Answer a DELETE of an unknown or ended session with 404](https://github.com/modelcontextprotocol/php-sdk/pull/638)

`modelcontextprotocol/php-sdk` · **merged** · updated · 分数 82 · 上游时间 2026-11-10T12:27:14Z

入选依据：T3 watchlist; breaking: breaking; protocol: protocol, transport, streamable; proposal: specification; merged implementation; verify release separately。

> 上游摘录（未审读）：A 'DELETE' of an unknown or already ended session is answered '200', but once a session is terminated, the server \["MUST respond to requests containing that session ID with HTTP 404 Not Found"\](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#session-management). 'Protocol::destroySession()' now returns whether the session existed, and 'StreamableHttpTransport' answers '404' when the session-

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[Client\]\[Schema\] Reject 'x-mcp-header' annotations outside a chain of 'properties' (SEP-2243)](https://github.com/modelcontextprotocol/php-sdk/pull/711)

`modelcontextprotocol/php-sdk` · **merged** · updated · 分数 82 · 上游时间 2026-11-10T12:26:15Z

入选依据：T3 watchlist; breaking: breaking; protocol: protocol, transport, streamable; proposal: sep-, specification, extension; merged implementation; verify release separately。

> 上游摘录（未审读）：'McpHeader::checkAnnotations()' only walked 'properties', so an annotation under 'items', 'anyOf', '$defs' & co. was never seen and the client kept the tool. The spec says such an annotation makes the tool definition invalid and clients on Streamable HTTP MUST drop it from 'tools/list' (\[x-mcp-header\](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http#schema-extension)). \[BC Bre

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Release 1.10.0](https://github.com/modelcontextprotocol/ruby-sdk/pull/679)

`modelcontextprotocol/ruby-sdk` · **merged** · new · 分数 80 · 上游时间 2026-11-11T14:06:32Z

入选依据：T3 watchlist; security: oauth; protocol: sse, stdio, timeout; proposal: sep-; merged implementation; verify release separately。

> 上游摘录（未审读）：This release validates the 'Mcp-Param-\*' headers of a tool call against its body (SEP-2243) and adds an optional 'issuer:' to the machine-to-machine OAuth providers. The Changed entries alter defaults under the exceptions described in VERSIONING.md: the stdio client passes the server process a reduced environment, a stalled SSE stream is closed after 'stream\_write\_timeout:' seconds, and an elicitation reply that does

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(mcp-scan,skill-scan,agent-scan): normalize hex-suffixed tool-call tags](https://github.com/Tencent/AI-Infra-Guard/pull/752)

`Tencent/AI-Infra-Guard` · **open** · new · 分数 78 · 上游时间 2026-11-11T06:55:26Z

入选依据：T1 watchlist; breaking: compatib; protocol: protocol。

> 上游摘录（未审读）：## Summary Some OpenAI-compatible models answer the text-based tool-call protocol with hex-suffixed tags (' NAME>', ' ... ', etc.) instead of ' V '. The existing parsers do not match them, so 'finish' is never recognized and every stage loops until 'max\_iter' (see #751). This PR adds 'utils/tool\_format\_fix.py' to each of the three scanners. Its 'normalize\_tool\_calls(content) -> (content, fixed)' rewrites the known ma

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(a2a): add top-level skills field to agents](https://github.com/IBM/mcp-context-forge/pull/7433)

`IBM/mcp-context-forge` · **merged** · updated · 分数 76 · 上游时间 2026-11-11T13:10:57Z

入选依据：T2 watchlist; breaking: migration; protocol: capabilit; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary Closes #7349 A2A agents stored skills inside 'capabilities'. An update that sent only 'capabilities' replaced the whole object, so it erased 'streaming' and 'pushNotifications'. ## Changes - Add a nullable 'skills' JSON column to 'a2a\_agents' (migration 'e5a1c7b9d3f2'). - Add 'A2AAgentSkill' and a 'skills' field to 'A2AAgentCreate', 'A2AAgentUpdate', and 'A2AAgentRead'. The API rejects a skill without 'id'

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [chore(sep-2640): repoint the requirements at the Skills beta page](https://github.com/modelcontextprotocol/conformance/pull/511)

`modelcontextprotocol/conformance` · **merged** · new · 分数 76 · 上游时间 2026-11-11T05:50:41Z

入选依据：T1 watchlist; protocol: protocol; proposal: sep-, specification, extension; merged implementation; verify release separately。

> 上游摘录（未审读）：## What changes Repoints 'src/seps/sep-2640.yaml' at the Skills extension's beta page, \['specification/beta/skills.mdx'\](https://github.com/modelcontextprotocol/ext-skills/blob/649f7aee/specification/beta/skills.mdx) at '649f7aee'. Every row now quotes that page instead of the SEP. SEP-3392 classified Skills as Beta, and ext-skills#161 moved the page from 'specification/stable/' to 'specification/beta/'. The WG maint

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Add RFC 9207 iss parameter check to MCP 2026-07-28 conformance test for AS](https://github.com/modelcontextprotocol/conformance/pull/581)

`modelcontextprotocol/conformance` · **open** · new · 分数 76 · 上游时间 2026-11-10T22:01:23Z

入选依据：T1 watchlist; security: authorization; protocol: sse, conformance。

> 上游摘录（未审读）：closes #580 ## Motivation and Context Described in #580 ## How Has This Been Tested? - 'npm test' (Test Files 48 passed, Tests 646 passed) - 'npm start -- list --authorization --spec-version 2026-07-28' and 'npm start -- list --authorization --spec-version 2025-11-25' (same two scenario: authorization-server-metadata-endpoint, authorization-code-grant) ### Test against real AS (keycloak) - MCP 2026-07-28 - 'npm start

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(sep-automation): drop the proposal state and sponsor-hunt comments](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3535)

`modelcontextprotocol/modelcontextprotocol` · **merged** · new · 分数 76 · 上游时间 2026-11-11T01:54:53Z

入选依据：T1 watchlist; protocol: lifecycle; proposal: sep-, proposal; merged implementation; verify release separately。

> 上游摘录（未审读）：\_Requested by \*\*David Soria Parra\*\* · \[Slack thread\](https://ant-mcp-oss.slack.com/archives/C0BDGKP4PC6/p1794253161846999)\_ \*\*Before:\*\* The SEP lifecycle bot treated 'proposal' as the first SEP state. It moved a 'proposal' SEP to 'draft' as soon as one of its assignees was a member of the 'steering-committee' team tree. If a 'proposal' went quiet, the author got a reminder after 90 days that asked "Do you need help f

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 发布与安全公告

显示 15 / 20 条；全部数据见当日 JSON。

### [1.0.5](https://github.com/modelcontextprotocol/inspector/releases/tag/1.0.5)

`modelcontextprotocol/inspector` · **published** · new · 分数 129 · 上游时间 2026-11-11T21:39:41Z

入选依据：T1 watchlist; breaking: deprecat; security: security; protocol: protocol, sse; release。

> 上游摘录（未审读）：## What's Changed ### v1.x security fixes 1.0.5 is a security release for the deprecated v1 line. Upgrade with 'npx @modelcontextprotocol/inspector@v1-latest', or move to v2 ('@latest'). \* \*\*The proxy now refuses two more fixed cloud metadata addresses.\*\* Its connection guard already blocked '169.254.0.0/16'. It now also blocks '100.100.100.200' (Alibaba Cloud ECS) and '192.0.0.192' (Oracle Cloud Classic), including

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [mcp-server-fetch: IPv6 site-local fec0::/10 classified as public (SSRF guard classifier gap, CWE-918)](https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-3rxj-6jhw-qfv7)

`modelcontextprotocol/servers` · **published** · new · 分数 117 · 上游时间 2026-11-11T07:25:01Z

入选依据：T2 watchlist; breaking: deprecat; security: ssrf; protocol: sse; advisory。

> 上游摘录（未审读）：### Summary \_is\_public\_address in mcp-server-fetch omits fec0::/10 (deprecated IPv6 site-local) and ::ffff:0:0/96 from its non-public list and falls back to ip.is\_global, which returns True for fec0::1. A fetch to http://\[fec0::1\]/ passes the SSRF guard. Low real-world reachability on default hosts; this is a classifier-correctness gap, not a proven metadata exploit. ### Details \*\*Server:\*\* fetch ('mcp-server-fetch',

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v4.1.7: Dumpster Dive](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.1.7)

`PrefectHQ/fastmcp` · **published** · new · 分数 101 · 上游时间 2026-11-10T01:59:06Z

入选依据：T1 watchlist; security: oauth; protocol: schema; release。

> 上游摘录（未审读）：FastMCP 4.1.7 backports 42 fixes from the 4.2 line, covering OpenAPI schema and parameter handling, OAuth redirect and consent edge cases, proxy and response caching, and lost-connection errors in the client. It also requires patched joserfc and Authlib releases and closes a redirect URI validation gap for callers that pass raw strings. Thanks to our 41 contributors, including 28 first-time contributors. ## What's Ch

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v4.1.8: Backporch Light](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.1.8)

`PrefectHQ/fastmcp` · **published** · new · 分数 101 · 上游时间 2026-11-10T20:44:13Z

入选依据：T1 watchlist; security: oauth, token; protocol: schema, timeout; release。

> 上游摘录（未审读）：FastMCP 4.1.8 backports 28 fixes from the 4.2 line, led by OAuth proxy token revocation, which now works for the client that owns the token. It also fixes recursive and untyped schema hydration, GitHub sessions across transient verification failures, proxied sampling and prompt arguments, and a set of OpenAPI, client timeout, task and CLI edge cases. Thanks to our 21 contributors, including 9 first-time contributors.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [2.15.0](https://github.com/modelcontextprotocol/inspector/releases/tag/2.15.0)

`modelcontextprotocol/inspector` · **published** · new · 分数 101 · 上游时间 2026-11-12T00:46:29Z

入选依据：T1 watchlist; security: security, vulnerab; protocol: protocol, sse; release。

> 上游摘录（未审读）：## What's Changed ### Security fixes 2.15.0 fixes four vulnerabilities. The fetch-guard and event-stream fixes affect every v2 release from 2.0.0 through 2.14.0, the mcpdo daemon fix affects 2.10.0 through 2.14.0, and the server.json preview fix affects 2.14.0. Upgrade with 'npx @modelcontextprotocol/inspector@latest'. \* \*\*The fetch guard blocks cloud metadata addresses outside '169.254.0.0/16'\*\*, including '100.100.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v1.10.0](https://github.com/modelcontextprotocol/ruby-sdk/releases/tag/v1.10.0)

`modelcontextprotocol/ruby-sdk` · **published** · new · 分数 95 · 上游时间 2026-11-11T14:05:44Z

入选依据：T3 watchlist; security: oauth; protocol: sse, stdio, timeout; proposal: sep-; release。

> 上游摘录（未审读）：This release validates the 'Mcp-Param-\*' headers of a tool call against its body (SEP-2243) and adds an optional 'issuer:' to the machine-to-machine OAuth providers. The Changed entries alter defaults under the exceptions described in \[VERSIONING.md\](VERSIONING.md): the stdio client passes the server process a reduced environment, a stalled SSE stream is closed after 'stream\_write\_timeout:' seconds, and an elicitatio

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [AWS API MCP Server Security Policy Bypass via Incorrect Operation Name Normalization](https://github.com/awslabs/mcp/security/advisories/GHSA-4wq9-grf3-qg2p)

`awslabs/mcp` · **published** · new · 分数 89 · 上游时间 2026-11-10T16:34:58Z

入选依据：T2 watchlist; security: security; protocol: protocol; advisory。

> 上游摘录（未审读）：### Summary AWS API MCP Server is an open source Model Context Protocol (MCP) server that customers run to let AI assistants manage their AWS accounts through AWS API calls. An issue exists where, under certain circumstances, the custom security policy in AWS API MCP Server does not enforce denyList and elicitList entries for AWS API operations whose names contain consecutive capital letters, because the server norma

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v2.4.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.4.0)

`modelcontextprotocol/servers` · **published** · new · 分数 89 · 上游时间 2026-11-11T07:37:43Z

入选依据：T2 watchlist; security: security, vulnerab; protocol: protocol; release。

> 上游摘录（未审读）：## Security fixes v2.4.0 fixes six vulnerabilities in three servers. Upgrade '@modelcontextprotocol/server-filesystem' to 2.3.0, and 'mcp-server-git' and 'mcp-server-fetch' to 2026.11.11. \| Package \| Affected \| Fixed in \| \| --- \| --- \| --- \| \| '@modelcontextprotocol/server-filesystem' \| all versions before 2.3.0, and date versions 2025.1.14 through 2026.8.31 \| 2.3.0 \| \| 'mcp-server-git' \| through 2026.11.4 \| 2026.11.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [mcp-server-git: Incomplete Fix for GHSA-w766-5x43-whvw in validate\_opened\_repo() Allows --repository Confinement Bypass via objects/info/alternates and Linked-Worktree common\_dir Confusion](https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-q74p-4wrc-q7w6)

`modelcontextprotocol/servers` · **published** · new · 分数 89 · 上游时间 2026-11-11T07:27:42Z

入选依据：T2 watchlist; security: ghsa-; protocol: protocol, sse; advisory。

> 上游摘录（未审读）：## Patched versions Fixed in 'mcp-server-git' \*\*2026.11.11\*\* (\[#5514\](https://github.com/modelcontextprotocol/servers/pull/5514)). Upgrade to 2026.11.11 or later. Versions before 2026.10.28 are covered by GHSA-w766-5x43-whvw. Under '--repository', the fix closes both bypasses in this report and the class around them: - A repository whose Git directory names an alternate object store ('objects/info/alternates' or 'obj

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v0.64.0](https://github.com/stacklok/toolhive/releases/tag/v0.64.0)

`stacklok/toolhive` · **published** · new · 分数 89 · 上游时间 2026-11-10T12:22:20Z

入选依据：T2 watchlist; security: authorization, token; protocol: sse; release。

> 上游摘录（未审读）：# 🚀 \*\*Toolhive v0.64.0 is live!\*\* This release hardens the embedded authorization server. It closes a client-assertion replay gap, rejects ID-JAGs presented as access tokens, and stops deeply nested JWTs before fosite parses them. The operator now exposes the auth server's TLS listener port. ## 🆕 New Features - When 'embeddedAuthServer.tlsListener' is enabled, MCPServer, MCPRemoteProxy and VirtualMCPServer workloads

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v0.10.0](https://github.com/modelcontextprotocol/php-sdk/releases/tag/v0.10.0)

`modelcontextprotocol/php-sdk` · **published** · new · 分数 79 · 上游时间 2026-11-10T17:17:19Z

入选依据：T3 watchlist; security: oauth, authorization; protocol: schema; release。

> 上游摘录（未审读）：## What's Changed ### TL;DR \* The SDK is split into the 'Mcp\\Schema', 'Mcp\\Client' and 'Mcp\\Server' namespaces, ahead of separate packages: most imports change \* PHP 8.2 or higher is required, and JSON-RPC batches are gone \* The client authorizes with OAuth: authorization code, client credentials, 'private\_key\_jwt' and experimental cross-app access \* Handshake-era servers over HTTP run without sessions unless 'Builde

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [OAuth middleware endpoints bypass request body limits and allow unauthenticated memory exhaustion](https://github.com/modelcontextprotocol/php-sdk/security/advisories/GHSA-f4rf-6ghj-mhr6)

`modelcontextprotocol/php-sdk` · **published** · new · 分数 79 · 上游时间 2026-11-10T07:59:36Z

入选依据：T3 watchlist; security: oauth, token; protocol: transport, streamable; advisory。

> 上游摘录（未审读）：# OAuth middleware endpoints bypass the request-body limit and allow unauthenticated memory exhaustion ## Summary 'StreamableHttpTransport' documents and enforces a default 4 MiB upper bound for POST request bodies. However, middleware runs before the transport request handler, and the public OAuth '/token' and '/register' middleware endpoints consume their request bodies directly without any size limit. An unauthent

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v1.1.1 - Release 2026-11-10 - Token Exchange Delegation, CEL Tool Validation, A2A v1 Routes, and Security Hardening](https://github.com/IBM/mcp-context-forge/releases/tag/v1.1.1)

`IBM/mcp-context-forge` · **published** · new · 分数 69 · 上游时间 2026-11-10T13:51:19Z

入选依据：T2 watchlist; security: security, oauth, token; release。

> 上游摘录（未审读）：## \[1.1.1\] - 2026-11-10 - Token Exchange Delegation, CEL Tool Validation, A2A v1 Routes, and Security Hardening ### Overview Release 1.1.1 delivers \*\*token exchange delegation and Admin UI support\*\*, \*\*CEL tool validation policies\*\*, \*\*A2A '/v1' task and agent card routes\*\*, and \*\*upstream progress relay to modern clients\*\*. It also hardens ownership, OAuth discovery, credential masking, and token scoping, and it com

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [mcp-server-git: arbitrary command execution via a repository's own Git configuration (core.fsmonitor) during read-only tools](https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-6hqx-gqrx-c5r2)

`modelcontextprotocol/servers` · **published** · new · 分数 63 · 上游时间 2026-11-11T07:25:23Z

入选依据：T2 watchlist; protocol: protocol; advisory。

> 上游摘录（未审读）：## Patched versions Fixed in 'mcp-server-git' \*\*2026.11.11\*\* (\[#5514\](https://github.com/modelcontextprotocol/servers/pull/5514)). Upgrade to 2026.11.11 or later. The report below was written against 2026.11.4, before the fix; its "Fixed versions: none" line predates it. The fix covers every sink the report lists, not only 'core.fsmonitor': - Every Git command the server runs overrides, through 'GIT\_CONFIG\_COUNT' (wh

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [server-filesystem: 'move\_file''s same-device rename leaves the source unpinned — a swapped source parent moves an outside file into the allowed directories, where it becomes readable](https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-7m4x-rv66-mxhh)

`modelcontextprotocol/servers` · **published** · new · 分数 63 · 上游时间 2026-11-11T07:24:37Z

入选依据：T2 watchlist; protocol: sse; advisory。

> 上游摘录（未审读）：### Summary The 'move\_file' handler validates both its source and destination. For a same-device move, however, only the destination parent is pinned: 'renameIntoDirectory' passes the \*\*source\*\* to 'fs.renameSync' as an absolute string, which the kernel resolves at rename time — after validation. A local process that swaps a parent component of the source path for an outside-pointing symlink in that window causes the

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 协议 / 工作组提交

显示 9 / 9 条；全部数据见当日 JSON。

### [fix(sep-automation): drop the proposal state and sponsor-hunt comments (#3535)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/283d8d6a10ca9c4de63bc3a8d798762dfed52e86)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 71 · 上游时间 2026-11-11T01:54:50Z

入选依据：T1 watchlist; protocol: lifecycle; proposal: sep-, proposal。

> 上游摘录（未审读）：fix(sep-automation): drop the proposal state and sponsor-hunt comments (#3535) \_Requested by \*\*David Soria Parra\*\* · \[Slack thread\](https://ant-mcp-oss.slack.com/archives/C0BDGKP4PC6/p1794253161846999)\_ \*\*Before:\*\* The SEP lifecycle bot treated 'proposal' as the first SEP state. It moved a 'proposal' SEP to 'draft' as soon as one of its assignees was a member of the 'steering-committee' team tree. If a 'proposal' wen

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: mark MCP Inspector Apps support as partial (#3540)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/a40b29a92906d43f2ffaff8c9ba8217b5e5a68d4)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 71 · 上游时间 2026-11-11T15:17:30Z

入选依据：T1 watchlist; protocol: protocol; proposal: extension。

> 上游摘录（未审读）：docs: mark MCP Inspector Apps support as partial (#3540) Marks MCP Inspector as partially supporting MCP Apps in the extensions client matrix. The Inspector web client renders MCP Apps and advertises the 'io.modelcontextprotocol/ui' extension by default. See \['core/mcp/extensions.ts'\](https://github.com/modelcontextprotocol/inspector/blob/4d3464cb3/core/mcp/extensions.ts) and \['core/mcp/apps.ts'\](https://github.com/m

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs(community): reconcile working and interest group lists (#3533)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/200d5339bbc7649ee92d6445dc17368e2b5b11ba)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 61 · 上游时间 2026-11-11T01:57:42Z

入选依据：T1 watchlist; security: authorization。

> 上游摘录（未审读）：docs(community): reconcile working and interest group lists (#3533) \_Requested by \*\*David Soria Parra\*\* · \[Slack thread\](https://ant-mcp-oss.slack.com/archives/C0BDGKP4PC6/p1794253161846999)\_ \*\*Before:\*\* The Community pages disagreed about which groups exist. The Enterprise-Managed Authorization IG appeared in the current group list and the sidebar, although its own page and the Authorization IG charter say it was fo

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs(community): fix dead links and anchors in community pages (#3532)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/0b22bfed6e94c0c7751046d2e845fac954cac8a7)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 55 · 上游时间 2026-11-11T19:28:49Z

入选依据：T1 watchlist; protocol: transport。

> 上游摘录（未审读）：docs(community): fix dead links and anchors in community pages (#3532) \_Requested by \*\*David Soria Parra\*\* · \[Slack thread\](https://ant-mcp-oss.slack.com/archives/C0BDGKP4PC6/p1794253161846999)\_ \*\*Before:\*\* Three Community pages had links that resolve to nothing. The Governance WG charter linked to '/community/working-interest-groups#charter-amendments', an anchor that does not exist. The Transports WG charter linked

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(blog): keep code blocks dark in the light theme (#3542)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/751ea06c2310978c85c1bcef7f6e22f9dbf4e2c9)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 55 · 上游时间 2026-11-11T19:24:50Z

入选依据：T1 watchlist; protocol: protocol。

> 上游摘录（未审读）：fix(blog): keep code blocks dark in the light theme (#3542) Code blocks on the blog are hard to read in the light theme: the syntax colors are monokai's (made for a dark background), but the block is drawn on light grey. Example: https://blog.modelcontextprotocol.io/posts/exploring-file-uploads-and-downloads-in-mcp/ ## Cause The inline code rule '.post-content code' sets 'background: var(--surface)', and it also matc

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs(blog): add post on the file uploads and downloads extension (#3515)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/5324218639be4a6c696902d70f98f225326bbe4b)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 51 · 上游时间 2026-11-11T10:59:59Z

入选依据：T1 watchlist; proposal: extension。

> 上游摘录（未审读）：docs(blog): add post on the file uploads and downloads extension (#3515) Adds a blog post about the work-in-progress file uploads and downloads extension, to get early feedback and prototypes from the community. The extension is experimental and hasn't been approved, and the post says so. Before this merges: - \[ \] Merge the extension draft, because the post links to it on 'main' - \[ \] Replace the image placeholder -

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs(blog): announce the MCP release cycle (#3541)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/9a67316897f90f97bcd2ee939ca8e7e1532a27d3)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 51 · 上游时间 2026-11-11T19:27:17Z

入选依据：T1 watchlist; proposal: sep-, proposal, specification。

> 上游摘录（未审读）：docs(blog): announce the MCP release cycle (#3541) ## Summary - Announce the six-month specification release cadence from SEP-3398 and the March 30, 2027 release target. - Introduce Luca Chang as a release manager alongside Den Delimarsky and David Soria Parra for the next specification cycle. - Explain proposal and SDK milestones and point readers to contribution and community resources. - Add a PNG timeline and edi

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs(community): state who can open pull requests and how to get there (#3534)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/c6d8d167677c0bda559ead9daf16f43e75cb71cc)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 35 · 上游时间 2026-11-11T01:55:59Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：docs(community): state who can open pull requests and how to get there (#3534) \_Requested by \*\*David Soria Parra\*\* · \[Slack thread\](https://ant-mcp-oss.slack.com/archives/C0BDGKP4PC6/p1794253161846999)\_ \*\*Before:\*\* The docs gave three answers on who can open a pull request in this repository. 'docs/community/contributing.mdx' said "write access", the contributor ladder said pull requests are "open to all", and 'CONTR

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs(community): add working groups overview page (#3513)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/ddbbf0f8ab3038a3406844e9ee063644eae57cc3)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 35 · 上游时间 2026-11-11T15:50:10Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：docs(community): add working groups overview page (#3513) Add a page that lists the working groups with their leads, Discord channels and focus, and link it from the navigation.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 文章与技术解释

显示 3 / 3 条；全部数据见当日 JSON。

### [The Official Ruby SDK for MCP Reaches Tier 1](https://blog.modelcontextprotocol.io/posts/ruby-sdk-tier-1/)

`mcp-official-blog` · **published** · updated · 分数 76 · 上游时间 2026-10-30T09:00:00+00:00

入选依据：T1 watchlist; security: security; protocol: protocol。

> 上游摘录（未审读）：The official Ruby SDK for Model Context Protocol is now a Tier 1 SDK, as defined in our SDK tiering system . Ruby is not alone here, and joins the company of our TypeScript, Python, C#, Go, and Rust SDKs. When an SDK becomes Tier 1-compliant, it means that it reached the top of the three tiers, reserved for SDKs with the highest level of feature support, responsiveness to bugs and security issues, and alignment with

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Exploring File Uploads and Downloads in MCP](https://blog.modelcontextprotocol.io/posts/exploring-file-uploads-and-downloads-in-mcp/)

`mcp-official-blog` · **published** · new · 分数 50 · 上游时间 2026-11-10T09:00:00+00:00

入选依据：T1 watchlist; protocol: protocol, capabilit。

> 上游摘录（未审读）：The Model Context Protocol (MCP) started out as a simple way to connect models to tools, and that principle is still very much at its heart. Over the past two years, the things people build with the protocol have become more ambitious. Much more ambitious. Many of those MCP server projects now need to work with files - often driven by increasing agent capabilities and autonomy. Saving a PDF from a conversation to clo

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [A More Predictable Release Cycle for MCP](https://blog.modelcontextprotocol.io/posts/mcp-release-cycle/)

`mcp-official-blog` · **published** · new · 分数 50 · 上游时间 2026-11-11T09:00:00+00:00

入选依据：T1 watchlist; protocol: capabilit。

> 上游摘录（未审读）：We’ve spent a lot of time over the past two years talking about ways to improve MCP, add new features and capabilities, and get on a more predictable release cadence. Clearly, there has been no shortage of ideas both from the maintainer and broader developer community. Getting those ideas reviewed, implemented, tested, and into a release is a whole other part of the job, and we want to make that specific part easier

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 博客选题工作台

从上面的重点项挑选，不自动把提案写成已实现功能：

- 协议问题：规范原文、提案状态、旧行为与新行为。
- 实现证据：PR diff、回归测试、客户端/服务端版本。
- 复现：最小实验、消息/HTTP trace、失败与成功条件。
- 结论边界：事实、维护者解释、个人判断分别记录。

模板：[知识库写作模板](https://github.com/xixiaxibro/mcp-knowledge-base/tree/main/templates)。
