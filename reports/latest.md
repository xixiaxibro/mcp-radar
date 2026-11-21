# MCP Radar · 2026-11-21 (UTC)

采集时间：2026-11-21T01:17:06+00:00 · 回看窗口：14 天。

这是公开来源的更新索引和选题素材，不是已经审读、复现的技术结论。标题和摘录来自上游；优先级由可见规则计算。

本次窗口内 2254 条记录；本日累计 675 个新增/变更版本；失败端点 0 个；覆盖警告 1 个。

## 覆盖与限制

PR merged 表示代码进入分支，不代表已发布；release 不自动证明符合某协议版本。初次运行只建立窗口基线。

仅跟踪 watchlist 中公开仓库的 PR、指定仓库 issue/commit、release、公开安全公告和订阅源。未提供 API 的社区讨论、社交媒体和完整标准文档变更不在覆盖保证内。RSS 仅提供源当前保留的条目。

- 覆盖提示：`modelcontextprotocol/agents-wg` / source — Repository renamed/redirected to modelcontextprotocol/agents-ig

## 重点 PR / 提案

显示 20 / 622 条；全部数据见当日 JSON。

### [fix(auth): accept same-origin issuers at any address](https://github.com/modelcontextprotocol/rust-sdk/pull/1467)

`modelcontextprotocol/rust-sdk` · **merged** · updated · 分数 102 · 上游时间 2026-11-20T23:17:21Z

入选依据：T2 watchlist; breaking: breaking; security: oauth, authorization; protocol: transport; merged implementation; verify release separately。

> 上游摘录（未审读）：## Motivation and Context Following up on #1393, OAuth discovery now accepts an authorization server on the resource’s own origin, regardless of its IP address type. ## How Has This Been Tested? Added tests ## Breaking Changes None. ## Types of changes - \[x\] Bug fix (non-breaking change which fixes an issue) - \[ \] New feature (non-breaking change which adds functionality) - \[ \] Breaking change (fix or feature that wo

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(prompt-security): add RefusalLadderJailbreaking multi-turn attack](https://github.com/Tencent/AI-Infra-Guard/pull/780)

`Tencent/AI-Infra-Guard` · **merged** · new · 分数 94 · 上游时间 2026-11-20T01:38:59Z

入选依据：T1 watchlist; breaking: breaking; security: security; merged implementation; verify release separately。

> 上游摘录（未审读）：## What Adds a new multi-turn attack operator \*\*'RefusalLadderJailbreaking'\*\* to AIG-PromptSecurity. When the target model refuses, it automatically climbs an ordered \*\*remediation ladder\*\*, re-rolling on a clean session at each rung, and stops at the first non-refusal: 'baseline → retry → prefill → authorized\_framing → simulator rewrite' ## Why Modern jailbreak tooling (local proxies / request rewriters) pairs a pay

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Omit app-only ui\_get unless the client advertises MCP Apps](https://github.com/github/github-mcp-server/pull/3687)

`github/github-mcp-server` · **open** · updated · 分数 92 · 上游时间 2026-11-18T18:06:48Z

入选依据：T1 watchlist; security: token; protocol: protocol, stdio; proposal: extension。

> 上游摘录（未审读）：## Summary Do not list the app-only 'ui\_get' tool to clients that lack MCP Apps support, on both the remote (HTTP) server and the local stdio server. ## Why 'ui\_get' is marked '\_meta.ui.visibility: \["app"\]'. Apps hosts hide that from the model; other clients ignore the meta and hand the helper to the model, wasting tokens. A client that supports Apps declares 'extensions\["io.modelcontextprotocol/ui"\]'. The remote ser

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(transport): answer malformed Streamable HTTP bodies with 400](https://github.com/modelcontextprotocol/rust-sdk/pull/1464)

`modelcontextprotocol/rust-sdk` · **merged** · updated · 分数 92 · 上游时间 2026-11-20T23:16:58Z

入选依据：T2 watchlist; breaking: breaking; protocol: protocol, transport, streamable; proposal: specification; merged implementation; verify release separately。

> 上游摘录（未审读）：## Motivation and Context According to the \[transport spec\](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports#sending-messages-to-the-server), 'StreamableHttpService' should respond to a POST body that isn’t a JSON-RPC message with 400 Bad Request and a JSON-RPC parse error, instead of 415 Unsupported Media Type. ## How Has This Been Tested? Added tests ## Breaking Changes None ## Types of cha

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs(examples): add skills server and client examples](https://github.com/modelcontextprotocol/rust-sdk/pull/1466)

`modelcontextprotocol/rust-sdk` · **merged** · updated · 分数 92 · 上游时间 2026-11-20T23:17:10Z

入选依据：T2 watchlist; breaking: breaking; protocol: stdio; proposal: extension; merged implementation; verify release separately。

> 上游摘录（未审读）：## Motivation and Context 'skills-fs' shipped in v3.10.0 with a wiring snippet in the module docs but no runnable example. This adds a stdio server that serves a skill folder and a client that walks the extension from the host side. ## How Has This Been Tested? ## Breaking Changes None. ## Types of changes - \[ \] Bug fix (non-breaking change which fixes an issue) - \[ \] New feature (non-breaking change which adds funct

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(auth): accept AS-granted scopes beyond the ID-JAG in EMA flow](https://github.com/modelcontextprotocol/rust-sdk/pull/1481)

`modelcontextprotocol/rust-sdk` · **open** · new · 分数 92 · 上游时间 2026-11-20T14:28:22Z

入选依据：T2 watchlist; breaking: breaking; security: token; protocol: transport。

> 上游摘录（未审读）：The resource AS decides which scopes end up on the access token, so rejecting scopes the ID-JAG doesn't carry was too strict and out of line with the other MCP SDKs. This shouldn't be a breaking change, since the SDK is becoming more lenient. Fixes #1480

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(mcp-scan,skill-scan): stop reading a reply that only repeats closing tags](https://github.com/Tencent/AI-Infra-Guard/pull/769)

`Tencent/AI-Infra-Guard` · **merged** · updated · 分数 88 · 上游时间 2026-11-18T02:16:20Z

入选依据：T1 watchlist; breaking: compatib; protocol: timeout; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary After a finished tool call, some models keep writing a run of closing tags until the server cuts the stream: ''' ... ... (about 220,000 characters) ''' Observed with 'hy4-flash' through an OpenAI-compatible gateway. Effects: - One reply takes 200-220 s to receive. The 300 s 'stream\_timeout' does not help, because the stream ends by itself before the deadline. - The whole reply, junk included, is appended t

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[Copilot Dreaming\] Avoid invalid tool workflows and remove stale or duplicate guidance](https://github.com/github/github-mcp-server/pull/3894)

`github/github-mcp-server` · **merged** · new · 分数 88 · 上游时间 2026-11-19T17:50:57Z

入选依据：T1 watchlist; breaking: migration, compatib; protocol: schema; merged implementation; verify release separately。

> 上游摘录（未审读）：## 🧠 How this helps Copilot Tool migrations can otherwise return an unregistrable value, copy an incompatible schema default, or regenerate snapshots for ordering alone. Following the current constructor and schema contracts avoids those misleading migration steps. Development guidance can send Copilot to a missing package, an incorrect workflow trigger or toolchain, an unsupported test-package convention, or a bare

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(server): type registerTool structuredContent from outputSchema](https://github.com/modelcontextprotocol/typescript-sdk/pull/2449)

`modelcontextprotocol/typescript-sdk` · **merged** · updated · 分数 88 · 上游时间 2026-11-18T15:32:17Z

入选依据：T1 watchlist; breaking: deprecat; protocol: schema; merged implementation; verify release separately。

> 上游摘录（未审读）：'McpServer.registerTool' now type-checks a callback's successful result against the tool's 'outputSchema'. 'structuredContent' is required and must match the schema, for Standard Schema and the deprecated raw-shape overload. 'isError: true' results, input-required results and tools without an 'outputSchema' keep their current types. Types only: runtime behaviour is unchanged. Closes #2754. '''ts server.registerTool('

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(core): cap SSE line length and event size on every SDK transport stream (v2)](https://github.com/modelcontextprotocol/inspector/pull/2993)

`modelcontextprotocol/inspector` · **merged** · new · 分数 86 · 上游时间 2026-11-18T07:10:45Z

入选依据：T1 watchlist; security: ghsa-; protocol: transport, sse; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #2991 The v2 fix for GHSA-3xgv-mvj6-g78r, developed and reviewed in the advisory's private fork (inspector-ghsa-3xgv-mvj6-g78r#2) and landed here as an ordinary PR. The commits are the fork branch's, unchanged. The v1 fix is tracked in #2992. ## Problem A malicious upstream server can open an SSE stream, send a valid 'endpoint' event, and then stream 'data: ' followed by megabytes with no line terminator. It c

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix: cap upstream SSE line length and event size in the proxy (v1)](https://github.com/modelcontextprotocol/inspector/pull/2994)

`modelcontextprotocol/inspector` · **merged** · new · 分数 86 · 上游时间 2026-11-18T07:14:02Z

入选依据：T1 watchlist; security: ghsa-; protocol: transport, streamable, sse; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #2992 The v1 fix for GHSA-3xgv-mvj6-g78r, developed and reviewed in the advisory's private fork (inspector-ghsa-3xgv-mvj6-g78r#1) and landed here as an ordinary PR. The commits are the fork branch's, unchanged. The v2 fix is tracked in #2991. ## Problem A malicious upstream on the 'sse' (or 'streamable-http') transport can open an event stream and then send 'data: ' followed by an endless run of bytes with no

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Cap SSE line and event size on every SDK transport stream (GHSA-3xgv-mvj6-g78r)](https://github.com/modelcontextprotocol/inspector/pull/2997)

`modelcontextprotocol/inspector` · **merged** · new · 分数 86 · 上游时间 2026-11-18T07:10:44Z

入选依据：T1 watchlist; security: ghsa-; protocol: transport, sse; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #2991 > The fix was developed and reviewed in the advisory's private fork. These are the reviewed commits, pushed here unchanged. Tracking issue: #2991. Advisory: GHSA-3xgv-mvj6-g78r (v2; v1 is fixed separately for #2992). ## Problem A malicious upstream server can open an SSE stream, send a valid 'endpoint' event, and then stream 'data: ' followed by megabytes with no line terminator. It can do the same with

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v1: Cap upstream SSE line and event size in the proxy (GHSA-3xgv-mvj6-g78r)](https://github.com/modelcontextprotocol/inspector/pull/2998)

`modelcontextprotocol/inspector` · **merged** · new · 分数 86 · 上游时间 2026-11-18T07:14:00Z

入选依据：T1 watchlist; security: ghsa-; protocol: transport, streamable, sse; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #2992 > The fix was developed and reviewed in the advisory's private fork. These are the reviewed commits, pushed here unchanged. Tracking issue: #2992. Advisory: GHSA-3xgv-mvj6-g78r (v1; v2 is fixed separately for #2991). ## Problem A malicious upstream on the 'sse' (or 'streamable-http') transport can open an event stream and then send 'data: ' followed by an endless run of bytes with no line terminator. The

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Send custom headers to same-origin OAuth requests (#2985)](https://github.com/modelcontextprotocol/inspector/pull/3014)

`modelcontextprotocol/inspector` · **merged** · new · 分数 86 · 上游时间 2026-11-18T19:54:21Z

入选依据：T1 watchlist; security: oauth, authorization; protocol: transport; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #2985 ## What was wrong A server's custom headers are handed to the transport ('requestInit'), so they reach the MCP endpoint. The OAuth requests the Inspector makes itself — protected-resource and authorization-server discovery, dynamic client registration, the code exchange, refresh, revocation — run on a separate fetch chain ('InspectorClient.effectiveAuthFetch') that never saw them. A deployment that route

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add a config reference for the composable test server](https://github.com/modelcontextprotocol/inspector/pull/3016)

`modelcontextprotocol/inspector` · **merged** · new · 分数 86 · 上游时间 2026-11-18T19:55:42Z

入选依据：T1 watchlist; security: oauth, token; protocol: transport, stdio; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #2980 Adds a \*\*Config reference\*\* section to 'docs/test-servers.md', so a config for the composable test server can be written without reading the TypeScript: - how to run a config, with 'configs/demo.json' as the minimal stdio example (suggested in the issue's comments) - every top-level key, and 'transport' including the 'modern' options - the 'oauth' block field by field: mode, discovery overrides, token va

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Keep custom headers on the server's origin for the SDK's own OAuth requests](https://github.com/modelcontextprotocol/inspector/pull/3019)

`modelcontextprotocol/inspector` · **merged** · new · 分数 86 · 上游时间 2026-11-18T21:27:26Z

入选依据：T1 watchlist; security: oauth, authorization, token; protocol: transport; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #3018 ## What A server's custom headers no longer reach an authorization server on another origin through the OAuth work the SDK runs from inside the transport. 'createTransportNode' handed the headers to the SDK transport as 'requestInit.headers'. The transport reads them there for its MCP requests, but it also builds the fetch for its own OAuth requests (discovery and token refresh behind a '401', when an 'a

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat: add injectable SDK logger](https://github.com/modelcontextprotocol/typescript-sdk/pull/2370)

`modelcontextprotocol/typescript-sdk` · **merged** · updated · 分数 86 · 上游时间 2026-11-18T16:20:12Z

入选依据：T1 watchlist; security: oauth; protocol: protocol, streamable; merged implementation; verify release separately。

> 上游摘录（未审读）：Adds a 'logger' option to 'Client', 'McpServer', 'createMcpHandler' and the built-in OAuth providers, plus an optional 'sdkLogger' property on 'OAuthClientProvider', so the SDK's own diagnostics go to a logger you choose instead of straight to 'console'. Fixes #1262. '''ts import { createMcpHandler, McpServer, type SdkLogger } from '@modelcontextprotocol/server'; import { Client, ClientCredentialsProvider, Streamable

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [search: fence call\_tool to searchable tools and annotate it](https://github.com/PrefectHQ/fastmcp/pull/5263)

`PrefectHQ/fastmcp` · **open** · new · 分数 84 · 上游时间 2026-11-19T19:43:15Z

入选依据：T1 watchlist; breaking: breaking; security: security。

> 上游摘录（未审读）：the search transform's 'call\_tool' proxy now reaches only the tools search can return, and its annotations describe them. before, it listed with no annotations (so hosts read it as a destructive write) and could run 'always\_visible' tools too, so one approval of the proxy covered every tool on the server, including the ones pinned so they would be approved individually. '''python @mcp.tool(annotations={"readOnlyHint"

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(cloudflare): Stop advertising plain PKCE in scoped OAuth metadata](https://github.com/getsentry/toolkit/pull/2403)

`getsentry/toolkit` · **merged** · new · 分数 82 · 上游时间 2026-11-19T06:42:49Z

入选依据：T2 watchlist; breaking: compatib; security: oauth, authorization, pkce; merged implementation; verify release separately。

> 上游摘录（未审读）：The path-scoped authorization server metadata ('/.well-known/oauth-authorization-server/mcp/...') is a compatibility document we build by hand, and it advertised 'code\_challenge\_methods\_supported: \["plain", "S256"\]'. workers-oauth-provider rejects 'plain' unless 'allowPlainPKCE' is set, and we don't set it. Clients that picked 'plain' from this document had their authorization requests rejected, and those rejections

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(server): let a low-level Server take part in HTTP preflight checks](https://github.com/modelcontextprotocol/typescript-sdk/pull/3128)

`modelcontextprotocol/typescript-sdk` · **open** · updated · 分数 82 · 上游时间 2026-11-18T16:13:09Z

入选依据：T1 watchlist; security: oauth; protocol: schema; proposal: sep-; draft PR。

> 上游摘录（未审读）：Implements the handler-free option from #3126: 'createMcpHandler' ran SEP-2243 'Mcp-Param-\*' header validation and OAuth scope challenges only when the factory returned an 'McpServer', so a factory returning a low-level 'Server' skipped both without notice. ## Change - 'Server' gains 'setToolInputSchemaResolver(resolver)' and 'setScopeChallengeHandler(handler)'. - 'McpServer' sets both on its own 'Server' from its re

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 发布与安全公告

显示 15 / 43 条；全部数据见当日 JSON。

### [1.0.3](https://github.com/modelcontextprotocol/inspector/releases/tag/1.0.3)

`modelcontextprotocol/inspector` · **published** · new · 分数 129 · 上游时间 2026-11-18T14:43:46Z

入选依据：T1 watchlist; breaking: deprecat; security: security, ghsa-; protocol: protocol; release。

> 上游摘录（未审读）：## What's Changed ### v1.x security fixes 1.0.3 is a security release for the deprecated v1 line. Upgrade with 'npx @modelcontextprotocol/inspector@v1-latest', or move to v2 ('@latest'). \* \*\*Proxy rejects browser requests without an allowed Origin when authentication is disabled\*\*, and 'DANGEROUSLY\_OMIT\_AUTH' is read strictly (only 'true', '1' or 'yes') (\[GHSA-wmjf-2m46-2352\](https://github.com/modelcontextprotocol/i

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [1.0.4](https://github.com/modelcontextprotocol/inspector/releases/tag/1.0.4)

`modelcontextprotocol/inspector` · **published** · updated · 分数 129 · 上游时间 2026-11-18T14:43:43Z

入选依据：T1 watchlist; breaking: deprecat; security: security; protocol: protocol, schema; release。

> 上游摘录（未审读）：## What's Changed ### v1.x security fixes 1.0.4 is a security release for the deprecated v1 line. Upgrade with 'npx @modelcontextprotocol/inspector@v1-latest', or move to v2 ('@latest'). \* \*\*Server-supplied 'pattern' regexes are no longer evaluated.\*\* Patterns in a tool's output schema and in an elicitation's requested schema are stripped before validation, including patterns reachable through '$ref', and the elicita

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [1.0.5](https://github.com/modelcontextprotocol/inspector/releases/tag/1.0.5)

`modelcontextprotocol/inspector` · **published** · updated · 分数 129 · 上游时间 2026-11-18T14:43:41Z

入选依据：T1 watchlist; breaking: deprecat; security: security; protocol: protocol, sse; release。

> 上游摘录（未审读）：## What's Changed ### v1.x security fixes 1.0.5 is a security release for the deprecated v1 line. Upgrade with 'npx @modelcontextprotocol/inspector@v1-latest', or move to v2 ('@latest'). \* \*\*The proxy now refuses two more fixed cloud metadata addresses.\*\* Its connection guard already blocked '169.254.0.0/16'. It now also blocks '100.100.100.200' (Alibaba Cloud ECS) and '192.0.0.192' (Oracle Cloud Classic), including

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [1.0.6](https://github.com/modelcontextprotocol/inspector/releases/tag/1.0.6)

`modelcontextprotocol/inspector` · **published** · new · 分数 129 · 上游时间 2026-11-18T14:43:38Z

入选依据：T1 watchlist; breaking: deprecat; security: security; protocol: protocol, sse; release。

> 上游摘录（未审读）：## What's Changed ### v1.x security fixes 1.0.6 is a security release for the deprecated v1 line. Upgrade with 'npx @modelcontextprotocol/inspector@v1-latest', or move to v2 ('@latest'). \* \*\*A malicious MCP server can no longer crash the proxy by streaming an unbounded server-sent event.\*\* The proxy now caps how much of an upstream SSE stream it will buffer. A single line, or a single event, longer than 16 MiB closes

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [2.14.0](https://github.com/modelcontextprotocol/inspector/releases/tag/2.14.0)

`modelcontextprotocol/inspector` · **published** · updated · 分数 129 · 上游时间 2026-11-18T14:37:50Z

入选依据：T1 watchlist; breaking: deprecat; security: security, vulnerab, ghsa-; protocol: protocol; release。

> 上游摘录（未审读）：## What's Changed ### Security fixes 2.14.0 fixes three vulnerabilities reported privately against v2. Upgrade with 'npx @modelcontextprotocol/inspector@latest'. One of them, GHSA-2fw8-7jmw-r937, also affects the deprecated v1 line, where it is fixed in 1.0.4 ('@v1-latest'). \* \*\*An MCP App can no longer navigate its sandbox frame away from the policy it was given.\*\* The proxy enforces a frame policy built from the ap

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [2.16.0](https://github.com/modelcontextprotocol/inspector/releases/tag/2.16.0)

`modelcontextprotocol/inspector` · **published** · new · 分数 103 · 上游时间 2026-11-18T14:37:45Z

入选依据：T1 watchlist; breaking: deprecat; protocol: protocol, schema; release。

> 上游摘录（未审读）：## What's Changed \* Key a budget-declined pattern to its own schema by @cliffhall in https://github.com/modelcontextprotocol/inspector/pull/2969 \* Show the target rate in a stepped --load run's text header by @cliffhall in https://github.com/modelcontextprotocol/inspector/pull/2970 \* Add a v1 npm deprecate step to the release skill by @cliffhall in https://github.com/modelcontextprotocol/inspector/pull/2968 \* Validat

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [2.12.0](https://github.com/modelcontextprotocol/inspector/releases/tag/2.12.0)

`modelcontextprotocol/inspector` · **published** · new · 分数 101 · 上游时间 2026-11-18T14:37:54Z

入选依据：T1 watchlist; security: security, vulnerab, oauth; protocol: protocol; release。

> 上游摘录（未审读）：## What's Changed ### Security fixes 2.12.0 fixes three vulnerabilities that affect every v2 release from 2.0.0 through 2.11.0. Upgrade with 'npx @modelcontextprotocol/inspector@latest'. \* \*\*Opening a URL is restricted to 'http(s)', and the Inspector opens the URL it checked rather than the raw input.\*\* A remote server's OAuth authorization URL can no longer run commands through the opener on Windows and WSL. 'open'

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [2.15.0](https://github.com/modelcontextprotocol/inspector/releases/tag/2.15.0)

`modelcontextprotocol/inspector` · **published** · updated · 分数 101 · 上游时间 2026-11-18T14:37:48Z

入选依据：T1 watchlist; security: security, vulnerab; protocol: protocol, sse; release。

> 上游摘录（未审读）：## What's Changed ### Security fixes 2.15.0 fixes four vulnerabilities. The fetch-guard and event-stream fixes affect every v2 release from 2.0.0 through 2.14.0, the mcpdo daemon fix affects 2.10.0 through 2.14.0, and the server.json preview fix affects 2.14.0. Upgrade with 'npx @modelcontextprotocol/inspector@latest'. \* \*\*The fetch guard blocks cloud metadata addresses outside '169.254.0.0/16'\*\*, including '100.100.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [2.6.0](https://github.com/modelcontextprotocol/inspector/releases/tag/2.6.0)

`modelcontextprotocol/inspector` · **published** · new · 分数 101 · 上游时间 2026-11-18T14:38:08Z

入选依据：T1 watchlist; security: oauth; protocol: protocol; release。

> 上游摘录（未审读）：## What's Changed \* fix(web): reset pending OAuth slots during render, not in an effect by @cliffhall in https://github.com/modelcontextprotocol/inspector/pull/2237 \* fix: terminate the OAuth connection-details refresh promise chain by @cliffhall in https://github.com/modelcontextprotocol/inspector/pull/2236 \* fix: key the OAuth clear's active-session check on the storage key by @cliffhall in https://github.com/model

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [2.7.0](https://github.com/modelcontextprotocol/inspector/releases/tag/2.7.0)

`modelcontextprotocol/inspector` · **published** · new · 分数 101 · 上游时间 2026-11-18T14:38:06Z

入选依据：T1 watchlist; security: ghsa-; protocol: protocol; release。

> 上游摘录（未审读）：## What's Changed \* chore: bump the vitest trio to 4.1.11 past GHSA-82fw-gwwq-j7x9 by @cliffhall in https://github.com/modelcontextprotocol/inspector/pull/2315 \* feat(test-servers): a CIMD showcase fixture that serves its own client metadata document by @cliffhall in https://github.com/modelcontextprotocol/inspector/pull/2307 \* chore: land the #2247 round-9 review findings on v2/main by @cliffhall in https://github.c

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [A malicious MCP server can crash the Inspector backend via an unbounded long-lived (GET event-stream) read, bypassing the GHSA-9w48 cap](https://github.com/modelcontextprotocol/inspector/security/advisories/GHSA-3xgv-mvj6-g78r)

`modelcontextprotocol/inspector` · **published** · new · 分数 101 · 上游时间 2026-11-18T09:29:59Z

入选依据：T1 watchlist; security: ghsa-; protocol: transport, sse; advisory。

> 上游摘录（未审读）：### Summary A connected MCP server reached over the legacy 'sse' transport can make the Inspector web backend buffer its server->client stream with no size cap, growing backend memory until the Node process exits with a JavaScript heap OOM and drops every session on that backend. The attacker is the upstream server; it needs no Inspector credentials. This is the same weakness class as GHSA-9w48-x22j-rrm7, through a d

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v0.67.0](https://github.com/stacklok/toolhive/releases/tag/v0.67.0)

`stacklok/toolhive` · **published** · new · 分数 97 · 上游时间 2026-11-20T14:08:59Z

入选依据：T2 watchlist; breaking: breaking; security: token; release。

> 上游摘录（未审读）：# 🚀 \*\*Toolhive v0.67.0 is live!\*\* This release expands SPIFFE workload identity with a new 'client\_credentials' grant and operator support for choosing grant types per association. It tightens token-exchange and ID-JAG redemption with clearer refusal reasons, adds structured findings and link and script checks to skill validation, and sets default resource limits for 'MCPRemoteProxy'. ## ⚠️ Breaking Changes - \*\*SPIFF

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v2.5.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.5.0)

`modelcontextprotocol/servers` · **published** · new · 分数 89 · 上游时间 2026-11-18T09:29:05Z

入选依据：T2 watchlist; security: security, vulnerab; protocol: protocol; release。

> 上游摘录（未审读）：## Security fixes v2.5.0 fixes eight vulnerabilities in three servers. Upgrade 'mcp-server-git' to 2026.11.18, '@modelcontextprotocol/server-filesystem' to 2.4.0 and '@modelcontextprotocol/server-everything' to 2.3.1. \| Package \| Affected \| Fixed in \| \| --- \| --- \| --- \| \| 'mcp-server-git' \| through 2026.11.11 \| 2026.11.18 \| \| '@modelcontextprotocol/server-filesystem' \| all versions before 2.4.0, and date versions 20

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [server-everything: gzip fetch SSRF guard still treats the NAT64 well-known prefix (64:ff9b::/96) as public — the instance of the class fixed for fetch in GHSA-66qx-2266-pmj6 remains in the second guard implementation](https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-38j4-j742-j7r3)

`modelcontextprotocol/servers` · **published** · new · 分数 89 · 上游时间 2026-11-18T09:26:31Z

入选依据：T2 watchlist; security: ghsa-, ssrf; protocol: sse; advisory。

> 上游摘录（未审读）：### Summary This is a precedent-consistency report, not a novel class: the identical NAT64 well-known-prefix gap in the sibling fetch server's SSRF guard was accepted by this repository, published as GHSA-66qx-2266-pmj6, and fixed in v2.1.0 (#5238). The everything server's gzip fetch guard (tools/gzip-file-as-resource.ts) still classifies addresses in 64:ff9b::/96 as public, because the prefix is never unwrapped to t

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [AI-Infra-Guard v4.6.11](https://github.com/Tencent/AI-Infra-Guard/releases/tag/v4.6.11)

`Tencent/AI-Infra-Guard` · **published** · new · 分数 81 · 上游时间 2026-11-19T04:02:59Z

入选依据：T1 watchlist; security: security, cve-, injection; release。

> 上游摘录（未审读）：## \[v4.6.11\] - 2026-11-19 ### Added - \*\*Prompt-Security\*\*: Add single-turn static CoTInjection operator (PR #775, 26c9e138) - \*\*Vuln\*\*: Add one-api CVE-2026-81027 channel-pinning authz rule (PR #774, 1a0c3de6) - \*\*Fingerprints\*\*: Add MCP Inspector fingerprint and CVE-2025-49596 rule (PR #768, cfc2e629) - \*\*Fingerprints\*\*: Add one-api fingerprint rule (PR #756, 95814491) - \*\*Data\*\*: Add 24 AI product CVE advisories fr

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 协议 / 工作组提交

显示 10 / 10 条；全部数据见当日 JSON。

### [sep(SEP-3415): Events Extension (#3415)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/8a18b4b3292b9f9b3aee73f6325f9f62f19a89f9)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 71 · 上游时间 2026-11-19T15:06:34Z

入选依据：T1 watchlist; protocol: protocol, schema; proposal: sep-, extension。

> 上游摘录（未审读）：sep(SEP-3415): Events Extension (#3415) Defines Events, an extension ('io.modelcontextprotocol/events') that lets an MCP client subscribe to things that happen in an upstream system, such as a Slack message, a repository push or a PagerDuty incident, and have an agent react without the user being present. - A server lists event types with 'events/list': a name, an 'inputSchema' for subscription arguments, a 'payloadS

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs(SEP-3415): register the Events extension (#3568)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/bbc31f8ded5762eae4df115b93942f5e71c8b3a7)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 71 · 上游时间 2026-11-20T10:50:43Z

入选依据：T1 watchlist; protocol: protocol; proposal: sep-, specification, extension。

> 上游摘录（未审读）：docs(SEP-3415): register the Events extension (#3568) \_Requested by \*\*Peter\*\* · \[project thread\](https://claude.ai/code/project/chan\_013VZyPu2nt8YAcwA65s6UqV?thread=cmsg\_013VZyPu2nt8YAcwA65s6UqVJyt1MeecHy1rTFjH8sxiG5)\_ ## Summary Registers the Events extension ('io.modelcontextprotocol/events') now that \[SEP-3415\](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3415) is Final. The specification itse

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs(inspector): add load testing and Active Sessions docs (#3503)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/c5c0da721c2e08390dbe172a6ccffdb53348c2a4)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 35 · 上游时间 2026-11-18T20:28:59Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：docs(inspector): add load testing and Active Sessions docs (#3503) Adds a dedicated \*\*Load testing\*\* page, and an \*\*Active sessions\*\* section on the web client page. The load mode is run by the web client's Load test panel, the CLI ('--load') and mcpdo ('tools/call --load') on one shared engine. Active Sessions is a new web-client view of every session the backend holds open, with a way to end one (modelcontextprotoc

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [build(deps-dev): bump glob from 14.0.4 to 14.0.6 (#3558)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/f34ae49d339832ae0a87b28891f7f250cda48697)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 31 · 上游时间 2026-11-18T19:06:30Z

入选依据：T1 watchlist; security: security, ghsa-; routine maintenance penalty。

> 上游摘录（未审读）：build(deps-dev): bump glob from 14.0.4 to 14.0.6 (#3558) Bumps \[glob\](https://github.com/isaacs/node-glob) from 14.0.4 to 14.0.6. Release notes Sourced from glob's releases . v14.0.6 ignore patterns lack the braceExpandMax limit applied to pattern Fixes GHSA-qxr8-q827-836c: https://github.com/isaacs/node-glob/security/advisories/GHSA-qxr8-q827-836c Commits 908e616 14.0.6 17cb207 ignore patterns lack the braceExpandMa

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Add packages folder](https://github.com/modelcontextprotocol/agents-ig/commit/deb54f490a4b732638cccff889a3daeb447cdee2)

`modelcontextprotocol/agents-wg` · **committed** · new · 分数 23 · 上游时间 2026-11-20T19:48:18Z

入选依据：T2 watchlist。

> 上游摘录（未审读）：Add packages folder

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: fix links, examples, and typos in the 2026-07-28 and draft docs (#3556)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/51735935c3b64787340bfbd23ec3e7292711f7fc)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 21 · 上游时间 2026-11-18T18:56:30Z

入选依据：T1 watchlist; proposal: specification; routine maintenance penalty。

> 上游摘录（未审读）：docs: fix links, examples, and typos in the 2026-07-28 and draft docs (#3556) Correct anchor links, examples that don't match the specification, stale instructions in the build and connect guides, and typos. No requirement changes. --------- Co-authored-by: Den Delimarsky

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [build(deps): bump peter-evans/create-pull-request from 8.1.1 to 8.1.3 (#3557)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/40bb4f23f6c51ce484f810658c8b53c0b38717de)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 5 · 上游时间 2026-11-18T19:02:32Z

入选依据：T1 watchlist; routine maintenance penalty。

> 上游摘录（未审读）：build(deps): bump peter-evans/create-pull-request from 8.1.1 to 8.1.3 (#3557) Bumps \[peter-evans/create-pull-request\](https://github.com/peter-evans/create-pull-request) from 8.1.1 to 8.1.3. Release notes Sourced from peter-evans/create-pull-request's releases . Create Pull Request v8.1.3 What's Changed fix: check git ref directly when pushing signed commits by @​peter-evans in peter-evans/create-pull-request#4521 Up

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [build(deps-dev): bump mint from 4.3.5 to 4.3.34 (#3561)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/553d5cc4da7bb074c8e43471361632fb2b098282)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 5 · 上游时间 2026-11-18T19:31:17Z

入选依据：T1 watchlist; routine maintenance penalty。

> 上游摘录（未审读）：build(deps-dev): bump mint from 4.3.5 to 4.3.34 (#3561) Bumps \[mint\](https://github.com/orgs/mintlify) from 4.3.5 to 4.3.34. Commits See full diff in compare view Signed-off-by: dependabot\[bot\] Co-authored-by: dependabot\[bot\] Co-authored-by: Den

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [build(deps-dev): bump typescript-eslint from 8.72.1 to 8.72.2 (#3560)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/5c9593cb64824474020da83ecfbddbb09aea7fe2)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 5 · 上游时间 2026-11-18T19:28:43Z

入选依据：T1 watchlist; routine maintenance penalty。

> 上游摘录（未审读）：build(deps-dev): bump typescript-eslint from 8.72.1 to 8.72.2 (#3560) Bumps \[typescript-eslint\](https://github.com/typescript-eslint/typescript-eslint/tree/HEAD/packages/typescript-eslint) from 8.72.1 to 8.72.2. Release notes Sourced from typescript-eslint's releases . v8.72.2 8.72.2 (2026-11-09) 🩹 Fixes eslint-plugin: \[prefer-string-starts-ends-with\] parse RegExps with the v flag in unicode sets mode ( #13102 ) esli

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [build(deps-dev): bump prettier from 3.9.10 to 3.10.1 (#3559)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/c511d9a4a56c7a90117eea959da412f2f0425bd6)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 5 · 上游时间 2026-11-18T19:25:30Z

入选依据：T1 watchlist; routine maintenance penalty。

> 上游摘录（未审读）：build(deps-dev): bump prettier from 3.9.10 to 3.10.1 (#3559) Bumps \[prettier\](https://github.com/prettier/prettier) from 3.9.10 to 3.10.1. Release notes Sourced from prettier's releases . 3.10.1 GraphQL: Fix empty selection set with comments ( #20504 by @​fisker ) 🔗 Changelog 3.10.0 diff 🔗 Prettier 3.10: New Flow syntax, new JavaScript syntax, and new plugin powered by Yuku Changelog Sourced from prettier's changelog

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
