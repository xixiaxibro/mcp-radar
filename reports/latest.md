# MCP Radar · 2026-11-06 (UTC)

采集时间：2026-11-06T01:19:59+00:00 · 回看窗口：14 天。

这是公开来源的更新索引和选题素材，不是已经审读、复现的技术结论。标题和摘录来自上游；优先级由可见规则计算。

本次窗口内 2107 条记录；本日累计 105 个新增/变更版本；失败端点 4 个；覆盖警告 0 个。

## 覆盖与限制

PR merged 表示代码进入分支，不代表已发布；release 不自动证明符合某协议版本。初次运行只建立窗口基线。

仅跟踪 watchlist 中公开仓库的 PR、指定仓库 issue/commit、release、公开安全公告和订阅源。未提供 API 的社区讨论、社交媒体和完整标准文档变更不在覆盖保证内。RSS 仅提供源当前保留的条目。

- 采集失败：`IBM/mcp-context-forge` / pulls — The read operation timed out
- 采集失败：`PrefectHQ/fastmcp` / security-advisories — The read operation timed out
- 采集失败：`getsentry/toolkit` / pulls — The read operation timed out
- 采集失败：`stacklok/toolhive` / pulls — The read operation timed out

## 重点 PR / 提案

显示 20 / 100 条；全部数据见当日 JSON。

### [Omit app-only ui\_get unless the client advertises MCP Apps](https://github.com/github/github-mcp-server/pull/3687)

`github/github-mcp-server` · **open** · new · 分数 92 · 上游时间 2026-11-05T15:41:08Z

入选依据：T1 watchlist; security: token; protocol: protocol, capabilit; proposal: extension。

> 上游摘录（未审读）：## Summary Do not list the app-only 'ui\_get' tool to clients that lack MCP Apps support. ## Why 'ui\_get' is marked '\_meta.ui.visibility: \["app"\]'. Apps hosts hide that from the model; other clients ignore the meta and hand the helper to the model, wasting tokens. A client that supports Apps declares 'extensions\["io.modelcontextprotocol/ui"\]'. The remote server already parses those capabilities on 'tools/list', but th

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(token): allow public clients that present a spurious credential](https://github.com/cloudflare/workers-oauth-provider/pull/411)

`cloudflare/workers-oauth-provider` · **open** · new · 分数 84 · 上游时间 2026-11-05T14:51:47Z

入选依据：T1 watchlist; breaking: breaking, backward, compatib; security: authorization, token。

> 上游摘录（未审读）：## Summary Restores backward compatibility for public clients ('token\_endpoint\_auth\_method: "none"') that send a 'client\_secret' or Basic 'Authorization' header at '/token'. Since 1.x (#276, #287), these requests are rejected with '401 invalid\_client' ('token\_endpoint\_auth\_method\_mismatch'), breaking integrations that unconditionally include credentials. Empty 'client\_secret=' is already handled (filtered as omitted

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(server): type registerTool structuredContent from outputSchema](https://github.com/modelcontextprotocol/typescript-sdk/pull/2449)

`modelcontextprotocol/typescript-sdk` · **open** · updated · 分数 78 · 上游时间 2026-11-05T15:05:04Z

入选依据：T1 watchlist; breaking: deprecat; protocol: schema。

> 上游摘录（未审读）：'McpServer.registerTool' now type-checks a callback's successful result against the tool's 'outputSchema'. 'structuredContent' is required and must match the schema, for Standard Schema and the deprecated raw-shape overload. 'isError: true' results, input-required results and tools without an 'outputSchema' keep their current types. Types only: runtime behaviour is unchanged. Closes #2754. '''ts server.registerTool('

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [SEP-XXXX: Separating Data Model from Transport Representation](https://github.com/modelcontextprotocol/transports-wg/pull/58)

`modelcontextprotocol/transports-wg` · **merged** · updated · 分数 76 · 上游时间 2026-11-05T20:12:44Z

入选依据：T1 watchlist; protocol: transport; proposal: sep-; merged implementation; verify release separately。

> 上游摘录（未审读）：Draft of an SEP to separate MCP's data model from it's transport representation.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat: add injectable SDK logger](https://github.com/modelcontextprotocol/typescript-sdk/pull/2370)

`modelcontextprotocol/typescript-sdk` · **open** · updated · 分数 76 · 上游时间 2026-11-05T14:25:14Z

入选依据：T1 watchlist; security: oauth; protocol: protocol, transport, streamable。

> 上游摘录（未审读）：Adds a 'logger' option to 'Client', 'McpServer', 'createMcpHandler' and 'OAuthClientProvider', so the SDK's own diagnostics go to a logger you choose instead of straight to 'console'. Fixes #1262. '''ts import { createMcpHandler, McpServer, type SdkLogger } from '@modelcontextprotocol/server'; import { Client, ClientCredentialsProvider, StreamableHTTPClientTransport } from '@modelcontextprotocol/client'; // The SDK l

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(model): don't treat \_meta alone as a CallToolResult](https://github.com/modelcontextprotocol/rust-sdk/pull/1405)

`modelcontextprotocol/rust-sdk` · **merged** · updated · 分数 72 · 上游时间 2026-11-05T15:41:30Z

入选依据：T2 watchlist; breaking: breaking; proposal: extension; merged implementation; verify release separately。

> 上游摘录（未审读）：## Motivation and Context There is existing logic to avoid 'CallToolResult' from shadowing 'CustomResult'. However, since any type can hold '\_meta' this doesn't really work. In real world I am trying to use the skills extension deserialized into 'CustomResult'. When '\_meta' is present this fails. ## How Has This Been Tested? Manually tested end to end + added/updated unit tests ## Breaking Changes No ## Types of chan

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(mcp): re-authorization and connection failures for the MCP client](https://github.com/cloudflare/agents/pull/2782)

`cloudflare/agents` · **merged** · updated · 分数 66 · 上游时间 2026-11-05T18:20:46Z

入选依据：T1 watchlist; security: authorization; merged implementation; verify release separately。

> 上游摘录（未审读）：Fixes #2658, #2822 and #2824. When an MCP server needs the user to authorize again partway through a session, the agent now says so. The request throws 'MCPAuthorizationRequiredError' with a link, the server moves to 'authenticating', and clients see the link through 'getMcpServers()'. Connection failures are recorded and stay put, the same as in Claude Code. A connect makes a few quick attempts, then the server is '

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs(examples): Reconnect buttons for MCP servers](https://github.com/cloudflare/agents/pull/2783)

`cloudflare/agents` · **merged** · updated · 分数 66 · 上游时间 2026-11-05T18:37:03Z

入选依据：T1 watchlist; security: oauth; merged implementation; verify release separately。

> 上游摘录（未审读）：Adds a Reconnect button for MCP servers to the 'mcp-client', 'ai-chat' and 'codemode' examples. Each one gets a 'reconnectServer' callable that calls 'reconnectMcpServer(id)', and a Reconnect button on 'failed' servers that opens the new link if one comes back. The playground's OAuth demo now describes the server states as they behave after #2782. After #2782, a failed MCP server stays failed until something calls 'r

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [After a subscriptions/listen reconnect, how does a client learn about transitions it missed?](https://github.com/modelcontextprotocol/ext-tasks/issues/24)

`modelcontextprotocol/ext-tasks` · **open** · new · 分数 66 · 上游时间 2026-11-05T19:07:25Z

入选依据：T1 watchlist; protocol: transport, sse; proposal: specification。

> 上游摘录（未审读）：### Context - 'notifications/tasks' carries a complete 'DetailedTask', "identical to what 'tasks/get' would have returned at that moment" ('specification/2026-07-28/tasks.md:477'). Clients "\*\*MAY\*\* continue polling 'tasks/get' in addition to subscribing … but need not do so" (':505'). - In core MCP 2026-07-28, an abrupt transport drop ends a subscription ('basic/patterns/subscriptions.mdx:125'). The client "\*\*MAY\*\* t

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [mcpdo: relay destination-guard refusal warnings from the detached sign-in helper](https://github.com/modelcontextprotocol/inspector/pull/2918)

`modelcontextprotocol/inspector` · **merged** · new · 分数 66 · 上游时间 2026-11-05T14:40:12Z

入选依据：T1 watchlist; security: oauth; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #2905 On a non-TTY 'mcpdo connect' without forced auto-open, OAuth runs in the detached sign-in helper, which is spawned with stderr ignored. So the 'Warning: Refused to fetch : ' line from #2846 was lost, and the caller saw only the later failure. ### Changes - 'authorizeInFrontend' ('clients/mcpdo/src/connection/authorize.ts') takes an optional 'onFetchRefusal' sink. When it is set, refusals go to the sink.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(core): keep a URL-valued secret whole in embedded-URL redaction](https://github.com/modelcontextprotocol/inspector/pull/2920)

`modelcontextprotocol/inspector` · **merged** · new · 分数 66 · 上游时间 2026-11-05T15:32:31Z

入选依据：T1 watchlist; security: token; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #2907 ## Problem The free-text URL matcher in 'core/mcp/fetchTracking.ts' ended a match wherever a second 'http(s)://' began. That rule exists so comma-joined URLs get redacted separately. It also meant a sensitive query value that is itself a URL was cut short, and its tail was printed verbatim: ''' https://as.example/token?client\_secret=https://secret.example/private -> https://as.example/token?client\_secret

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat: Tasks extension for server and client (ext/tasks subpaths)](https://github.com/modelcontextprotocol/typescript-sdk/pull/2782)

`modelcontextprotocol/typescript-sdk` · **open** · updated · 分数 66 · 上游时间 2026-11-05T14:47:43Z

入选依据：T1 watchlist; protocol: protocol; proposal: sep-, extension。

> 上游摘录（未审读）：Adds the \[Tasks extension\](https://github.com/modelcontextprotocol/ext-tasks) ('io.modelcontextprotocol/tasks', SEP-2663) as '@modelcontextprotocol/server/ext/tasks' and '@modelcontextprotocol/client/ext/tasks'. Stacked on #3066 and #2820; review the top commit. '''ts const store = new InMemoryTaskStore(); const tasks = new TasksExtension(store); const server = new McpServer(info, { extensions: \[tasks\] }); server.reg

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Reject non-positive event retention limits](https://github.com/PrefectHQ/fastmcp/pull/5535)

`PrefectHQ/fastmcp` · **merged** · updated · 分数 60 · 上游时间 2026-11-05T18:19:33Z

入选依据：T1 watchlist; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：## Description Validate 'max\_events\_per\_stream' at construction and reject values below one. Document the minimum so zero cannot silently disable trimming while retaining every event ID. Closes #5534 ## Contribution type - \[x\] Bug fix (simple, well-scoped fix for a clearly broken behavior) - \[ \] Documentation improvement - \[ \] Enhancement ## Checklist - \[x\] This PR addresses an existing issue (or fixes a self-evident

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(agents): type LifecycleCapability.onStart as MaybePromise](https://github.com/cloudflare/agents/pull/2827)

`cloudflare/agents` · **merged** · new · 分数 60 · 上游时间 2026-11-05T18:21:34Z

入选依据：T1 watchlist; protocol: lifecycle, capabilit; merged implementation; verify release separately。

> 上游摘录（未审读）：Fixes #2825. 'LifecycleCapability.onStart()' was typed to return 'void', but the capability runner awaits it, 'DurableObjectCapability.onStart' returns 'MaybePromise ', and 'MCPClientManager' overrides it as 'async'. It now returns 'MaybePromise '. This is a type-only change with no runtime effect. 'onStart' is the only hook that 'LifecycleCapability' declares. The other hooks ('onRequest', 'onAlarm', 'onJob', 'dispo

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [TUI: multi-select for array-of-choices form fields (#2904)](https://github.com/modelcontextprotocol/inspector/pull/2919)

`modelcontextprotocol/inspector` · **merged** · new · 分数 60 · 上游时间 2026-11-05T15:09:41Z

入选依据：T1 watchlist; protocol: schema; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #2904 ## What changed ink-form has no multi-select, so 'schemaToForm' rendered an array-of-choices property ('{ type: "array", items: { enum: \[...\] } }') as a \*\*single\*\* select. A tool argument could carry one value at most, and since #2829 a multi-select elicitation was answered with a one-element array, with 'minItems'/'maxItems' never checked. - \*\*New custom field manager\*\* ('clients/tui/src/components/Mult

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(core): terminate the Streamable HTTP session on disconnect](https://github.com/modelcontextprotocol/inspector/pull/2926)

`modelcontextprotocol/inspector` · **merged** · new · 分数 60 · 上游时间 2026-11-05T18:17:37Z

入选依据：T1 watchlist; protocol: transport, streamable; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #2924 ## What 'InspectorClient.disconnect()' closed the SDK client but never sent the Streamable HTTP session-terminating 'DELETE', so a stateful server kept every session the Inspector opened (and '--load-connections' / '--load-churn' exhausted session caps). Now every disconnect path ends the server-side session first. - \*\*'core/mcp/sessionTermination.ts'\*\* (new): 'terminateSessionBestEffort(transport)' call

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(load): --load-subscribe notification fan-out load](https://github.com/modelcontextprotocol/inspector/pull/2927)

`modelcontextprotocol/inspector` · **merged** · new · 分数 60 · 上游时间 2026-11-05T19:03:05Z

入选依据：T1 watchlist; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #2913 '--load-subscribe ' adds notification fan-out load to '--load' in the one-shot CLI and in 'mcpdo tools/call --load'. It opens '--load-subscribers' sessions, subscribes each to the resource, and measures how 'notifications/resources/updated' reaches them: per-notification delivery latency, missed notifications per session, and the subscribe cost. ## Design - \*\*Triggered mode\*\* (a tool name or '--load-scen

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(load): --load-workers multi-process load generator](https://github.com/modelcontextprotocol/inspector/pull/2930)

`modelcontextprotocol/inspector` · **merged** · new · 分数 60 · 上游时间 2026-11-05T21:31:23Z

入选依据：T1 watchlist; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #2914 '--load-workers ' spreads one '--load' run over 'n' generator processes and merges their results into one summary, for when a single Node process rather than the server is the bottleneck. ## How it works - \*\*Parent:\*\* the CLI the user ran connects once, so any login is done first. It then re-runs its own command ('process.argv', minus '--load-workers') as 'n' forked children with 'MCP\_INSPECTOR\_LOAD\_SHAR

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Redact passwords from the worker's backend URL](https://github.com/PrefectHQ/fastmcp/pull/6113)

`PrefectHQ/fastmcp` · **open** · updated · 分数 56 · 上游时间 2026-11-05T18:16:15Z

入选依据：T1 watchlist; security: security。

> 上游摘录（未审读）：The worker startup banner could print Redis credentials from userinfo or query parameters, including Sentinel and TLS private-key passwords. Redact password fields after decoding their query keys, and hide malformed backend URLs rather than risking a credential leak. Password-free backend URLs retain their original spelling. Closes #6112. Carries forward regression coverage and implementation work from #6164, includi

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(server): add protected resource metadata discovery scenario](https://github.com/modelcontextprotocol/conformance/pull/572)

`modelcontextprotocol/conformance` · **open** · new · 分数 56 · 上游时间 2026-11-05T14:10:07Z

入选依据：T1 watchlist; security: token。

> 上游摘录（未审读）：closes #565 adds 'auth/protected-resource-metadata', a server scenario. the harness plays a client with no token. one unauthenticated post, then metadata discovery in client order: 'resource\_metadata' from the challenge, the path well-known url, the root one. six checks come out of that. 'server-auth-401': 401 plus a 'WWW-Authenticate' header. 'server-prm-discovery': the metadata can be found; at 2025-06-18 the chall

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 发布与安全公告

显示 4 / 4 条；全部数据见当日 JSON。

### [rmcp-v3.9.0](https://github.com/modelcontextprotocol/rust-sdk/releases/tag/rmcp-v3.9.0)

`modelcontextprotocol/rust-sdk` · **published** · new · 分数 79 · 上游时间 2026-11-05T16:07:21Z

入选依据：T2 watchlist; protocol: protocol, transport; proposal: sep-, extension; release。

> 上游摘录（未审读）：### Added - \*(auth)\* structure protected resource discovery errors (\[#1305\](https://github.com/modelcontextprotocol/rust-sdk/pull/1305)) - \*(transport)\* log followed same-origin redirects at debug level (\[#1417\](https://github.com/modelcontextprotocol/rust-sdk/pull/1417)) - support the Skills extension (SEP-2640) (\[#1392\](https://github.com/modelcontextprotocol/rust-sdk/pull/1392)) ### Fixed - \*(model)\* don't treat \_

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [rmcp-macros-v3.9.0](https://github.com/modelcontextprotocol/rust-sdk/releases/tag/rmcp-macros-v3.9.0)

`modelcontextprotocol/rust-sdk` · **published** · new · 分数 63 · 上游时间 2026-11-05T16:06:51Z

入选依据：T2 watchlist; protocol: protocol; release。

> 上游摘录（未审读）：### Other - add Voltip to built with rmcp list (\[#1401\](https://github.com/modelcontextprotocol/rust-sdk/pull/1401))

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Unbounded response-body buffering in rmcp Streamable HTTP clients allows memory exhaustion](https://github.com/modelcontextprotocol/rust-sdk/security/advisories/GHSA-c9f9-cp8h-jcj5)

`modelcontextprotocol/rust-sdk` · **published** · new · 分数 63 · 上游时间 2026-11-05T16:46:53Z

入选依据：T2 watchlist; protocol: transport, streamable; advisory。

> 上游摘录（未审读）：### Summary The built-in Streamable HTTP clients in rmcp read non-streaming HTTP response bodies into memory with no size limit. A malicious or compromised MCP server can make a client buffer an arbitrarily large body and exhaust its memory (CWE-400, CWE-770). ### Details Both built-in 'StreamableHttpClient' implementations are affected: \*\*reqwest client\*\* ('transport-streamable-http-client-reqwest'), 'crates/rmcp/sr

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [cli@0.48.0](https://github.com/getsentry/toolkit/releases/tag/cli%400.48.0)

`getsentry/toolkit` · **published** · new · 分数 43 · 上游时间 2026-11-05T20:19:53Z

入选依据：T2 watchlist; release。

> 上游摘录（未审读）：### New Features ✨ #### Agent Conversation - Filter list by project by @vgrozdanic in \[#1459\](https://github.com/getsentry/toolkit/pull/1459) - Show aggregate metrics and costs by @vgrozdanic in \[#1458\](https://github.com/getsentry/toolkit/pull/1458) #### Cli - Cache telemetry that fails to send and retry it on the next run by @BYK with @sentry-junior in \[#1963\](https://github.com/getsentry/toolkit/pull/1963) - Add e

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 协议 / 工作组提交

显示 1 / 1 条；全部数据见当日 JSON。

### [SEP-XXXX: Separating Data Model from Transport Representation (#58)](https://github.com/modelcontextprotocol/transports-wg/commit/bb57534ac838326a2f9d7ee8d6cb86697a79e9d8)

`modelcontextprotocol/transports-wg` · **committed** · new · 分数 71 · 上游时间 2026-11-05T20:12:40Z

入选依据：T1 watchlist; protocol: transport; proposal: sep-。

> 上游摘录（未审读）：SEP-XXXX: Separating Data Model from Transport Representation (#58) Draft of an SEP to separate MCP's data model from it's transport representation.

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
