# MCP Radar · 2026-11-11 (UTC)

采集时间：2026-11-11T01:20:50+00:00 · 回看窗口：14 天。

这是公开来源的更新索引和选题素材，不是已经审读、复现的技术结论。标题和摘录来自上游；优先级由可见规则计算。

本次窗口内 612 条记录；本日累计 55 个新增/变更版本；失败端点 34 个；覆盖警告 0 个。

## 覆盖与限制

PR merged 表示代码进入分支，不代表已发布；release 不自动证明符合某协议版本。初次运行只建立窗口基线。

仅跟踪 watchlist 中公开仓库的 PR、指定仓库 issue/commit、release、公开安全公告和订阅源。未提供 API 的社区讨论、社交媒体和完整标准文档变更不在覆盖保证内。RSS 仅提供源当前保留的条目。

- 采集失败：`IBM/mcp-context-forge` / source — Network error from api.github.com/repos/IBM/mcp-context-forge
- 采集失败：`PrefectHQ/fastmcp` / source — Network error from api.github.com/repos/PrefectHQ/fastmcp
- 采集失败：`Tencent/AI-Infra-Guard` / pulls — The read operation timed out
- 采集失败：`Tencent/AI-Infra-Guard` / releases — Network error from api.github.com/repos/Tencent/AI-Infra-Guard/releases
- 采集失败：`Tencent/AI-Infra-Guard` / security-advisories — Network error from api.github.com/repos/Tencent/AI-Infra-Guard/security-advisories
- 采集失败：`awslabs/mcp` / source — Network error from api.github.com/repos/awslabs/mcp
- 采集失败：`cloudflare-mcp` / source — Network error from blog.cloudflare.com/rss/
- 采集失败：`cloudflare/agents` / releases — The read operation timed out
- 采集失败：`cloudflare/workers-sdk` / pulls — The read operation timed out
- 采集失败：`cloudflare/workers-sdk` / security-advisories — Network error from api.github.com/repos/cloudflare/workers-sdk/security-advisories
- 采集失败：`getsentry/toolkit` / source — Network error from api.github.com/repos/getsentry/toolkit
- 采集失败：`github/github-mcp-server` / source — Network error from api.github.com/repos/github/github-mcp-server
- 采集失败：`lastmile-ai/mcp-agent` / source — Network error from api.github.com/repos/lastmile-ai/mcp-agent
- 采集失败：`mcp-official-blog` / source — Network error from blog.modelcontextprotocol.io/index.xml
- 采集失败：`microsoft/playwright-mcp` / source — Network error from api.github.com/repos/microsoft/playwright-mcp
- 采集失败：`modelcontextprotocol/conformance` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/ext-auth` / security-advisories — The read operation timed out
- 采集失败：`modelcontextprotocol/inspector` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/mcpb` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/mcpb` / releases — Network error from api.github.com/repos/modelcontextprotocol/mcpb/releases
- 采集失败：`modelcontextprotocol/mcpb` / security-advisories — Network error from api.github.com/repos/modelcontextprotocol/mcpb/security-advisories
- 采集失败：`modelcontextprotocol/modelcontextprotocol` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/php-sdk` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/php-sdk` / releases — Network error from api.github.com/repos/modelcontextprotocol/php-sdk/releases
- 采集失败：`modelcontextprotocol/php-sdk` / security-advisories — Network error from api.github.com/repos/modelcontextprotocol/php-sdk/security-advisories
- 采集失败：`modelcontextprotocol/python-sdk` / pulls — \[Errno 54\] Connection reset by peer
- 采集失败：`modelcontextprotocol/registry` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/servers` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/servers` / releases — Network error from api.github.com/repos/modelcontextprotocol/servers/releases
- 采集失败：`modelcontextprotocol/servers` / security-advisories — Network error from api.github.com/repos/modelcontextprotocol/servers/security-advisories
- 采集失败：`modelcontextprotocol/typescript-sdk` / pulls — The read operation timed out
- 采集失败：`snyk/agent-scan` / source — Network error from api.github.com/repos/snyk/agent-scan
- 采集失败：`sparfenyuk/mcp-proxy` / source — Network error from api.github.com/repos/sparfenyuk/mcp-proxy
- 采集失败：`stacklok/toolhive` / source — Network error from api.github.com/repos/stacklok/toolhive

## 重点 PR / 提案

显示 20 / 52 条；全部数据见当日 JSON。

### [(implementation): SEP-2352 - Clarify authorization server binding and migration](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/2880)

`modelcontextprotocol/modelcontextprotocol` · **closed** · new · 分数 120 · 上游时间 2026-11-10T10:47:53Z

入选依据：T1 watchlist; breaking: migration; security: authorization; protocol: protocol; proposal: sep-。

> 上游摘录（未审读）：### Where was this agreed? https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2352 ### Description Implement \[SEP-2352\](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2352). - \[x\] modelcontextprotocol/typescript-sdk#2201 - \[x\] modelcontextprotocol/csharp-sdk#1634 - \[x\] modelcontextprotocol/go-sdk#978 - \[ \] modelcontextprotocol/java-sdk#1007 - \[ \] modelcontextprotocol/kotlin-sdk#811 -

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Runtime enforcement: the Security section's missing layer](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/3538)

`modelcontextprotocol/modelcontextprotocol` · **open** · new · 分数 92 · 上游时间 2026-11-11T01:27:43Z

入选依据：T1 watchlist; security: security, authorization; protocol: protocol; proposal: specification。

> 上游摘录（未审读）：The specification's Security and Trust & Safety section states that MCP itself cannot enforce its security principles at the protocol level, and that implementors SHOULD build consent and authorization flows, access controls, and documentation. That leaves the enforcement question to each implementor, with no shared account of what enforcement must look like to hold. Once a host connects an agent to tools, the agent'

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix: narrow DCR grant types to the subset this server supports](https://github.com/cloudflare/workers-oauth-provider/pull/423)

`cloudflare/workers-oauth-provider` · **merged** · updated · 分数 86 · 上游时间 2026-11-10T19:49:39Z

入选依据：T1 watchlist; security: oauth, authorization, token; protocol: negotiat, capabilit; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #422. DCR currently refuses VS Code's published client metadata because it declares 'urn:ietf:params:oauth:grant-type:device\_code' alongside 'authorization\_code' and 'refresh\_token', and 'negotiateDynamicClientRegistrationCapabilities' hands the full list to 'validateClientCapabilities', which throws on the first unsupported entry. RFC 7591 §3.2.1 allows the server to ignore unsupported requested values, and C

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(mcp): coordinate OAuth callbacks, refreshes, step-ups and server changes](https://github.com/cloudflare/agents/pull/2863)

`cloudflare/agents` · **open** · new · 分数 76 · 上游时间 2026-11-10T16:25:40Z

入选依据：T1 watchlist; security: oauth, authorization, token; protocol: sse。

> 上游摘录（未审读）：This fixes eight races in the MCP client where OAuth callbacks, token refreshes, step-ups and server changes ('closeConnection', 'removeServer', 'migrateServerId', 'configureElicitationHandlers') overlap. Each fix is its own commit with a replay test in 'authorization-races.test.ts'. Every replay fails on 'main' and passes after its commit. TLA+ models of the module found them. What each race did on 'main': - a token

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(server)!: return INVALID\_PARAMS for unknown resources](https://github.com/modelcontextprotocol/kotlin-sdk/pull/1172)

`modelcontextprotocol/kotlin-sdk` · **open** · new · 分数 72 · 上游时间 2026-11-10T17:11:55Z

入选依据：T3 watchlist; breaking: breaking; protocol: protocol; proposal: sep-。

> 上游摘录（未审读）：Per SEP-2164, 'resources/read' for an unknown URI now fails with '-32602' (Invalid Params) instead of '-32002', on every protocol version. The error data still carries the 'uri'. ## Breaking Changes 'Client.readResource' for a missing resource throws 'McpException' with 'INVALID\_PARAMS' instead of 'RESOURCE\_NOT\_FOUND'. Clients matching on '-32002' should also accept '-32602'. Closes #805

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Mark DPoP as experimental extension](https://github.com/modelcontextprotocol/ext-auth/pull/38)

`modelcontextprotocol/ext-auth` · **open** · updated · 分数 66 · 上游时间 2026-11-10T14:56:42Z

入选依据：T1 watchlist; protocol: protocol; proposal: sep-, proposal, specification。

> 上游摘录（未审读）：Brings @PieterKas's DPoP profile to 'specification/experimental/dpop.mdx', as an Experimental extension under \[SEP-3392\](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3392). The proposal is \[SEP-1932\](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1932). - Merges 'pieterkas-dpop-extension' and the heads of #33, #35 and #36, keeping all 18 of his commits. - Moves the file, runs P

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [(implementation): SEP-2468 - Recommend Issuer (iss) Parameter in MCP Auth Responses](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/2881)

`modelcontextprotocol/modelcontextprotocol` · **closed** · new · 分数 66 · 上游时间 2026-11-10T10:47:50Z

入选依据：T1 watchlist; protocol: protocol; proposal: sep-。

> 上游摘录（未审读）：### Where was this agreed? https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2468 ### Description Implement \[SEP-2468\](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2468). - \[x\] modelcontextprotocol/typescript-sdk#2197 - \[x\] modelcontextprotocol/csharp-sdk#1571 - \[x\] modelcontextprotocol/go-sdk#941 - \[ \] modelcontextprotocol/java-sdk#1008 - \[ \] modelcontextprotocol/kotlin-sdk#812 -

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(auth): omit scope on refresh unless caller sets one](https://github.com/modelcontextprotocol/rust-sdk/pull/1433)

`modelcontextprotocol/rust-sdk` · **open** · updated · 分数 64 · 上游时间 2026-11-10T04:06:25Z

入选依据：T2 watchlist; security: authorization; protocol: transport。

> 上游摘录（未审读）：fixes #1408 refresh was always sending 'scope' from the stored grant, which some servers (salesforce) reject. rfc 6749 §6 says scope is optional on refresh and leaving it out keeps the original grant. now refresh omits 'scope' unless the caller sets it via 'AuthorizationManager::set\_refresh\_scopes()'. when set, only scopes from the original grant get sent (keeps the #1331 behaviour). if none of them are in the grant,

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(mcp): start clean when a server is removed and added again under the same id](https://github.com/cloudflare/agents/pull/2856)

`cloudflare/agents` · **merged** · new · 分数 60 · 上游时间 2026-11-10T11:56:08Z

入选依据：T1 watchlist; protocol: lifecycle; merged implementation; verify release separately。

> 上游摘录（未审读）：An MCP server removed and added again under the same id ('addMcpServer(..., { id })') now starts clean, even while a connect for the removed server is still running. 'bringUp' remembers the connection it started on and stops with 'removed' once the id holds another one. 'removeServer' no longer deletes the row of a server registered again while it cleared credentials. A TLA+ model of the server lifecycle found three

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat: add weekly meeting notes (2026-07-24 to 2026-11-06)](https://github.com/modelcontextprotocol/transports-wg/pull/73)

`modelcontextprotocol/transports-wg` · **merged** · updated · 分数 60 · 上游时间 2026-11-10T08:44:38Z

入选依据：T1 watchlist; protocol: transport; merged implementation; verify release separately。

> 上游摘录（未审读）：Adds weekly MCP Transport Working Group meeting summaries from July through November 2026: - 'meetings/2026-07-24\_weekly.md' - 'meetings/2026-07-31\_weekly.md' - 'meetings/2026-08-14\_weekly.md' - 'meetings/2026-08-21\_weekly.md' - 'meetings/2026-08-28\_weekly.md' - 'meetings/2026-09-04\_weekly.md' - 'meetings/2026-09-25\_weekly.md' - 'meetings/2026-10-02\_weekly.md' - 'meetings/2026-10-09\_weekly.md' - 'meetings/2026-10-16\_

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat: keep CIMD clients signed in while their document's host is down](https://github.com/cloudflare/workers-oauth-provider/pull/426)

`cloudflare/workers-oauth-provider` · **open** · updated · 分数 56 · 上游时间 2026-11-10T20:00:46Z

入选依据：T1 watchlist; security: oauth。

> 上游摘录（未审读）：The provider now keeps the last validated copy of each Client ID Metadata Document in 'OAUTH\_KV', and uses it when the origin times out, fails at the network level, or answers 404, 408, 429 or 5xx. It is always on, with no option. The copy expires 24 hours after the last successful fetch. 401, 403 and other 4xx responses, and fresh documents that fail to parse or validate, never fall back. A 410 deletes the copy, so

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Return 400 for unreadable strings in Streamable HTTP POST validation](https://github.com/modelcontextprotocol/csharp-sdk/pull/2014)

`modelcontextprotocol/csharp-sdk` · **open** · new · 分数 54 · 上游时间 2026-11-10T06:34:46Z

入选依据：T3 watchlist; security: token; protocol: streamable。

> 上游摘录（未审读）：Fixes #1984 ## Problem 'HandlePostRequestAsync' reads some request values as strings while it validates the headers against the body. Two kinds of input make those reads throw 'InvalidOperationException', which the handler does not catch (it only catches 'JsonException'), so the request returns \*\*500\*\*: - \*\*A string that is not valid UTF-8.\*\* 'Utf8JsonReader' accepts the bytes inside a string token and only validates

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [mcp/experimental: add ServerCard convenience helper (SEP-2127)](https://github.com/modelcontextprotocol/go-sdk/pull/1024)

`modelcontextprotocol/go-sdk` · **open** · new · 分数 54 · 上游时间 2026-11-10T15:18:22Z

入选依据：T2 watchlist; protocol: protocol; proposal: sep-。

> 上游摘录（未审读）：## Summary Draft Go reference implementation for SEP-2127 MCP Server Cards. This adds an experimental 'mcp/experimental/servercard' package that ports the server-side convenience helper from modelcontextprotocol/python-sdk#2951 for building a static Server Card from 'mcp.Implementation' metadata and serving it with the discovery CORS/cache headers. ## Tracking / coordination - SEP-2127: MCP Server Cards - Spec/source

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Add a modern client for MCP 2026-07-28](https://github.com/modelcontextprotocol/java-sdk/pull/1325)

`modelcontextprotocol/java-sdk` · **open** · new · 分数 54 · 上游时间 2026-11-10T15:18:27Z

入选依据：T3 watchlist; security: authorization; protocol: protocol, transport。

> 上游摘录（未审读）：The latest protocol revision introduced a stateless incarnation of the protocol. It requires no initialization handshake or session management, and it doesn't allow server-to-client requests. An instance of the modern client is meant to stand for one user. It does no I/O when built and can share its transport with other clients, so an application that handles authorization creates one per user over a single HTTP tran

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(client): resume Streamable HTTP SSE streams independently](https://github.com/modelcontextprotocol/kotlin-sdk/pull/1171)

`modelcontextprotocol/kotlin-sdk` · **open** · new · 分数 54 · 上游时间 2026-11-10T16:22:56Z

入选依据：T3 watchlist; security: token; protocol: protocol, transport, streamable。

> 上游摘录（未审读）：Run the standalone GET stream and each resumed request stream in separate jobs, so resuming one no longer cancels the others. A resumption stops when its request is cancelled. 'Protocol' no longer sends 'notifications/cancelled' with the request's resumption token, which made the transport resume a stream instead of sending the cancel. fixes #1170 ## How Has This Been Tested? Integration tests against a scripted serv

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs(samples): add simple OAuth client sample (#166)](https://github.com/modelcontextprotocol/kotlin-sdk/pull/1173)

`modelcontextprotocol/kotlin-sdk` · **open** · new · 分数 54 · 上游时间 2026-11-10T21:20:41Z

入选依据：T3 watchlist; security: oauth, authorization, token; protocol: streamable。

> 上游摘录（未审读）：Closes #166. Adds 'samples/simple-oauth-client', a command-line client that signs in to an OAuth-protected MCP server over Streamable HTTP. The SDK doesn't ship client-side OAuth yet, so the sample implements the MCP authorization flow with plain Ktor: - A Ktor 'HttpSend' interceptor adds the bearer token. On '401' it runs the flow and retries once. - It discovers the protected resource metadata (RFC 9728), using the

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(agents): support Pi 1.5.1](https://github.com/cloudflare/agents/pull/2855)

`cloudflare/agents` · **closed** · new · 分数 50 · 上游时间 2026-11-10T15:28:43Z

入选依据：T1 watchlist; protocol: schema。

> 上游摘录（未审读）：## Summary \*\*Moves 'agents/models/pi-ai', 'agents/harness/pi' and the pi tool adapters from Pi 1.5.0 to Pi 1.5.1.\*\* \| Package \| From \| To \| \| --- \| --- \| --- \| \| '@earendil-works/pi-ai', 'pi-durable', 'chord', 'pi-schema', 'pi-codemode' (lockfile; dev and peer ranges stay '~1.5.0') \| 1.5.0 \| 1.5.1 \| \| '@earendil-works/pi-tui' (dev, exact) \| 1.5.0 \| 1.5.1 \| \| '@earendil-works/pi-telemetry', 'pi-agent-core' (examples,

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(agents): support Pi 1.5.2](https://github.com/cloudflare/agents/pull/2862)

`cloudflare/agents` · **open** · new · 分数 50 · 上游时间 2026-11-10T15:30:10Z

入选依据：T1 watchlist; protocol: schema。

> 上游摘录（未审读）：## Summary \*\*Moves 'agents/models/pi-ai', 'agents/harness/pi' and the pi tool adapters from Pi 1.5.0 to Pi 1.5.2.\*\* \| Package \| From \| To \| \| --- \| --- \| --- \| \| '@earendil-works/pi-ai', 'pi-durable', 'chord', 'pi-schema', 'pi-codemode' (lockfile; dev and peer ranges stay '~1.5.0') \| 1.5.0 \| 1.5.2 \| \| '@earendil-works/pi-tui' (dev, exact) \| 1.5.0 \| 1.5.2 \| \| '@earendil-works/pi-telemetry', 'pi-agent-core' (examples,

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Add WIF extension based on WAG as experimental](https://github.com/modelcontextprotocol/ext-auth/pull/42)

`modelcontextprotocol/ext-auth` · **open** · updated · 分数 46 · 上游时间 2026-11-10T14:38:42Z

入选依据：T1 watchlist; proposal: extension。

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [build: require Kotlin 2.3 and stop core from pulling in the Ktor server](https://github.com/modelcontextprotocol/kotlin-sdk/pull/1163)

`modelcontextprotocol/kotlin-sdk` · **merged** · updated · 分数 46 · 上游时间 2026-11-10T17:12:12Z

入选依据：T3 watchlist; breaking: breaking; merged implementation; verify release separately。

> 上游摘录（未审读）：The SDK is now compiled with Kotlin language and API version 2.3. JVM consumers already needed Kotlin 2.3: kotlin-stdlib 2.4 and kotlinx-serialization 1.12.0 carry 2.4 metadata, which a 2.2 compiler cannot read. 'kotlin-sdk-core' now depends on 'ktor-websockets' instead of 'ktor-server-websockets', so client-only consumers no longer pull in the Ktor server. ## Breaking Changes The minimum Kotlin version is now 2.3. #

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 发布与安全公告

显示 2 / 2 条；全部数据见当日 JSON。

### [v1.8.9](https://github.com/modelcontextprotocol/registry/releases/tag/v1.8.9)

`modelcontextprotocol/registry` · **published** · new · 分数 75 · 上游时间 2026-11-10T11:13:38Z

入选依据：T1 watchlist; protocol: pagination; release。

> 上游摘录（未审读）：Optimize incremental-sync pagination by selecting indexed page keys before fetching payloads, while retaining prepared statement reuse. Includes staged production autoscaling configuration and deployment guardrails. See #1840 for validation and rollout details.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v2.1.0](https://github.com/modelcontextprotocol/ext-apps/releases/tag/v2.1.0)

`modelcontextprotocol/ext-apps` · **published** · new · 分数 43 · 上游时间 2026-11-10T23:38:20Z

入选依据：T2 watchlist; release。

> 上游摘录（未审读）：## What's Changed Minor release: the SDK gains WebMCP interoperability, and the pdf-server example gets strict annotation validation. ### Features - \*\*WebMCP interoperability\*\* — instead of choosing between 'App.registerTool' and \[WebMCP\](https://webmachinelearning.github.io/webmcp/), the SDK now bridges them in both directions: tools registered with 'App.registerTool()' are mirrored into 'document.modelContext' when

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 协议 / 工作组提交

显示 1 / 1 条；全部数据见当日 JSON。

### [feat: add weekly meeting notes (2026-07-24 to 2026-11-06) (#73)](https://github.com/modelcontextprotocol/transports-wg/commit/a433b1bb9995427b2cce27407605782b0526f292)

`modelcontextprotocol/transports-wg` · **committed** · new · 分数 55 · 上游时间 2026-11-10T08:44:35Z

入选依据：T1 watchlist; protocol: transport。

> 上游摘录（未审读）：feat: add weekly meeting notes (2026-07-24 to 2026-11-06) (#73) Adds weekly MCP Transport Working Group meeting summaries from July through November 2026: - 'meetings/2026-07-24\_weekly.md' - 'meetings/2026-07-31\_weekly.md' - 'meetings/2026-08-14\_weekly.md' - 'meetings/2026-08-21\_weekly.md' - 'meetings/2026-08-28\_weekly.md' - 'meetings/2026-09-04\_weekly.md' - 'meetings/2026-09-25\_weekly.md' - 'meetings/2026-10-02\_week

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
