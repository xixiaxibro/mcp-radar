# MCP Radar · 2026-11-15 (UTC)

采集时间：2026-11-15T01:29:52+00:00 · 回看窗口：14 天。

这是公开来源的更新索引和选题素材，不是已经审读、复现的技术结论。标题和摘录来自上游；优先级由可见规则计算。

本次窗口内 1538 条记录；本日累计 52 个新增/变更版本；失败端点 4 个；覆盖警告 0 个。

## 覆盖与限制

PR merged 表示代码进入分支，不代表已发布；release 不自动证明符合某协议版本。初次运行只建立窗口基线。

仅跟踪 watchlist 中公开仓库的 PR、指定仓库 issue/commit、release、公开安全公告和订阅源。未提供 API 的社区讨论、社交媒体和完整标准文档变更不在覆盖保证内。RSS 仅提供源当前保留的条目。

- 采集失败：`IBM/mcp-context-forge` / pulls — Unterminated string starting at: line 1 column 1198043 (char 1198042)
- 采集失败：`PrefectHQ/fastmcp` / pulls — The read operation timed out
- 采集失败：`getsentry/toolkit` / pulls — Unterminated string starting at: line 1 column 16754 (char 16753)
- 采集失败：`stacklok/toolhive` / pulls — Unterminated string starting at: line 1 column 92783 (char 92782)

## 重点 PR / 提案

显示 20 / 52 条；全部数据见当日 JSON。

### [docs(http): document --authorization-server for RFC 7591 DCR clients](https://github.com/github/github-mcp-server/pull/3847)

`github/github-mcp-server` · **open** · new · 分数 76 · 上游时间 2026-11-14T09:29:58Z

入选依据：T1 watchlist; security: oauth, authorization, token; protocol: streamable。

> 上游摘录（未审读）：## Summary Clarifies 'docs/streamable-http.md' to document using '--authorization-server' ('GITHUB\_AUTHORIZATION\_SERVER') with an external OAuth 2.1 + Dynamic Client Registration (RFC 7591) proxy when self-hosting HTTP mode for MCP clients that require automated DCR and JSON token/refresh responses. Related to #3519 and #2532. ## Why In addition to GitHub Enterprise Server deployments, 'https://github.com/login/oauth

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [sep(SEP-3415): Events Extension](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3415)

`modelcontextprotocol/modelcontextprotocol` · **open** · updated · 分数 66 · 上游时间 2026-11-14T20:22:50Z

入选依据：T1 watchlist; protocol: protocol, schema; proposal: sep-, extension。

> 上游摘录（未审读）：Defines Events, an extension ('io.modelcontextprotocol/events') that lets an MCP client subscribe to things that happen in an upstream system, such as a Slack message, a repository push or a PagerDuty incident, and have an agent react without the user being present. - A server lists event types with 'events/list': a name, an 'inputSchema' for subscription arguments, a 'payloadSchema', and the delivery modes it suppor

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add release cycle page](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3550)

`modelcontextprotocol/modelcontextprotocol` · **open** · new · 分数 66 · 上游时间 2026-11-14T03:58:41Z

入选依据：T1 watchlist; protocol: protocol; proposal: sep-。

> 上游摘录（未审读）：Adds 'docs/community/release-cycle.mdx', the release-cycle documentation required by \[SEP-3398\](https://modelcontextprotocol.io/seps/3398-release-cycle-updates) (Reference Implementation, item 2). - Schedule: six-month releases, eight-month cycles, and the two-month overlap, with an example timeline from the release cycle blog post. - Milestones table with the timing and outcome of each milestone. - Steps for getting

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[wrangler\] Reuse OAuth credentials refreshed by another process](https://github.com/cloudflare/workers-sdk/pull/16874)

`cloudflare/workers-sdk` · **merged** · updated · 分数 64 · 上游时间 2026-11-14T08:27:38Z

入选依据：T3 watchlist; security: oauth, token; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：Addresses #15089. Alternative approach to #15136. When another Wrangler process has already refreshed our credentials, reuse its valid access token instead of immediately refreshing again. This prevents an unnecessary extra rotation that can leave an already-used refresh token on disk. ### How the failure happens The expiry check and refresh-token read currently happen separately. A process can decide to refresh usin

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Fix/3748 omit directory download url](https://github.com/github/github-mcp-server/pull/3848)

`github/github-mcp-server` · **open** · new · 分数 56 · 上游时间 2026-11-14T09:10:08Z

入选依据：T1 watchlist; security: token。

> 上游摘录（未审读）：## Summary Fixes #3748. Omit credential-bearing 'download\_url' values from 'get\_file\_contents' directory listings by default. Callers can still explicitly request this field through 'fields: \["download\_url"\]'. ## Why GitHub's Contents API can return short-lived tokenized raw-content URLs for files in private repositories. Directory listings generally need metadata such as names, paths, sizes, and SHAs—not bearer URLs

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(server-legacy): serve the RFC 8414 issuer without a trailing slash](https://github.com/modelcontextprotocol/typescript-sdk/pull/3184)

`modelcontextprotocol/typescript-sdk` · **open** · new · 分数 56 · 上游时间 2026-11-14T22:19:28Z

入选依据：T1 watchlist; security: oauth, authorization。

> 上游摘录（未审读）：## Summary 'createOAuthMetadata' wrote 'issuer: issuerUrl.href', and 'new URL('https://host').href' normalizes to 'https://host/' — so an authorization server constructed from a slash-less origin string advertised a \*\*slashed\*\* issuer. RFC 8414 §2 forbids a trailing slash on the issuer identifier, and §3.3 requires the metadata 'issuer' to be byte-identical to the URL the well-known document was fetched from. The pra

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Resume SSE streams from 'Last-Event-ID' in the Streamable HTTP transport](https://github.com/modelcontextprotocol/ruby-sdk/pull/681)

`modelcontextprotocol/ruby-sdk` · **merged** · updated · 分数 54 · 上游时间 2026-11-14T03:03:00Z

入选依据：T3 watchlist; protocol: transport, streamable, sse; proposal: sep-; merged implementation; verify release separately。

> 上游摘录（未审读）：## Motivation and Context MCP 2025-11-25 (SEP-1699) lets a client whose SSE connection dropped reconnect with a GET carrying 'Last-Event-ID' and receive what it missed, and lets a server close a connection on purpose during a long operation so the client polls instead of holding it open. The TypeScript, Python, Go, and Rust SDKs implement it with an event store on the server transport, a priming event carrying 'retry

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Accept every 'Origin' with 'allowed\_origins: :any' and keep the 'Host' check](https://github.com/modelcontextprotocol/ruby-sdk/pull/685)

`modelcontextprotocol/ruby-sdk` · **open** · new · 分数 54 · 上游时间 2026-11-14T15:24:11Z

入选依据：T3 watchlist; security: token; protocol: transport, streamable。

> 上游摘录（未审读）：## Motivation and Context 'StreamableHTTPTransport' accepts a cross-origin request only when its 'Origin' is listed in 'allowed\_origins:'. A remote server that browser-based clients on any origin may call, authenticated by a bearer token alone, had two ways to admit them: 'dns\_rebinding\_protection: false', which also turns off the 'Host' check, or building the transport per request with that request's own 'Origin' in

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(transport): answer an unparsable Streamable HTTP body with 400](https://github.com/modelcontextprotocol/rust-sdk/pull/1413)

`modelcontextprotocol/rust-sdk` · **closed** · updated · 分数 54 · 上游时间 2026-11-14T02:15:47Z

入选依据：T2 watchlist; protocol: protocol, transport, streamable; proposal: specification。

> 上游摘录（未审读）：## Motivation and Context 'StreamableHttpService' answers a POST whose body isn't a JSON-RPC message (invalid JSON, empty, 'null', '"jsonrpc":"1.0"') with 415 Unsupported Media Type, although the 'Content-Type: application/json' check already passed. The \[transports spec\](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports#sending-messages-to-the-server) asks for 400 here, optionally with a JSON

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(mcp-scan): accept tool inputSchema without "properties"](https://github.com/Tencent/AI-Infra-Guard/pull/763)

`Tencent/AI-Infra-Guard` · **open** · new · 分数 50 · 上游时间 2026-11-14T14:59:24Z

入选依据：T1 watchlist; protocol: schema。

> 上游摘录（未审读）：## Summary 'describe\_mcp\_tools' read 't.input\_schema\["properties"\]'. The MCP spec makes 'properties' optional in a tool's 'inputSchema', so a tool with no arguments declared as '{"type": "object"}' raised 'KeyError: 'properties''. A server that sends '"properties": null' raised 'AttributeError'. In dynamic scan this broke the connection check in 'ToolDispatcher.\_ensure\_mcp\_manager', so the whole server could not be s

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat: Support choosing the merge commit author email](https://github.com/github/github-mcp-server/pull/3852)

`github/github-mcp-server` · **open** · new · 分数 50 · 上游时间 2026-11-14T21:31:39Z

入选依据：T1 watchlist; protocol: sse。

> 上游摘录（未审读）：## Summary Allow 'merge\_pull\_request' callers to choose the merge commit's author email with an optional 'author\_email' argument. Calls that omit the email retain the existing REST merge path. ## Why Fixes #3814. Accounts with multiple verified email addresses need to select the appropriate work or noreply address when merging through MCP, as they can in GitHub's web UI. ## What changed - Add the optional argument to

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(server): stamp resultType on the hand-written stateless tool results](https://github.com/modelcontextprotocol/conformance/pull/563)

`modelcontextprotocol/conformance` · **open** · new · 分数 50 · 上游时间 2026-11-14T15:25:14Z

入选依据：T1 watchlist; protocol: sse。

> 上游摘录（未审读）：Fixes #562. ## Problem 'test\_logging\_tool' and 'test\_streaming\_elicitation' are the two stateless 'tools/call' branches that write their response by hand: each emits a notification line first, so it cannot use 'res.json()'. Writing directly with 'res.end(JSON.stringify(...))' also bypassed 'normalizeStatelessResponse', so their results came back without 'resultType': ''' { "jsonrpc": "2.0", "id": 1, "result": { "cont

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [MCP protocol lacks a mechanism for tools to stream incremental results](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/2932)

`modelcontextprotocol/modelcontextprotocol` · **open** · new · 分数 50 · 上游时间 2026-11-14T21:03:46Z

入选依据：T1 watchlist; protocol: protocol, sse, capabilit。

> 上游摘录（未审读）：The current tool call flow in MCP is strictly request-response. A client sends tools/call and waits for a full response. For long-running tools this means the client sees nothing until the tool completes completely. This is inconsistent with how MCP already handles prompt/message streaming via SSE. Tools should have a similar streaming capability. A practical approach: add a notifications/tool/progress message that s

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Record tool error results on the client OpenTelemetry span](https://github.com/modelcontextprotocol/python-sdk/pull/3859)

`modelcontextprotocol/python-sdk` · **closed** · new · 分数 50 · 上游时间 2026-11-14T04:46:54Z

入选依据：T1 watchlist; protocol: protocol。

> 上游摘录（未审读）：Fixes #3810 Records tool error results on the client OpenTelemetry span when 'CallToolResult.isError' is 'True'. ## Motivation and Context In MCP, application-level tool errors return a successful JSON-RPC response containing 'isError=True' in the result payload rather than a JSON-RPC 'ErrorData' protocol error. Previously, 'send\_raw\_request' only checked if 'outcome' was an 'ErrorData' instance to record errors on t

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add a Go stdio publishing example for OCI packages](https://github.com/modelcontextprotocol/registry/pull/1757)

`modelcontextprotocol/registry` · **open** · updated · 分数 50 · 上游时间 2026-11-14T04:58:39Z

入选依据：T1 watchlist; protocol: protocol, stdio。

> 上游摘录（未审读）：Adds a Go + OCI path to the publishing quickstart: a minimal stdio server using the official Go SDK, a Dockerfile with the required 'io.modelcontextprotocol.server.name' annotation, an OCI 'server.json', and the build/publish/verify commands. Also links the walkthrough from the OCI section of the package types page. The Go snippet builds against the current SDK, and the 'server.json' example validates against the cur

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add SourceWeft MCP Directory to community projects](https://github.com/modelcontextprotocol/registry/pull/1858)

`modelcontextprotocol/registry` · **open** · new · 分数 50 · 上游时间 2026-11-14T13:01:33Z

入选依据：T1 watchlist; protocol: protocol。

> 上游摘录（未审读）：## Motivation and Context Adds the SourceWeft MCP Directory to the "Browsers" section of the community projects list. The directory at https://sourceweft.com/mcp is a web browser for the official MCP Registry: its entries are federated from 'registry.modelcontextprotocol.io' (the sync lives in 'apps/backend/src/modules/market/federation.ts' of the linked repository). Each server page shows the tools the server expose

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(core-internal): use an already-converted JSON Schema document directly](https://github.com/modelcontextprotocol/typescript-sdk/pull/3138)

`modelcontextprotocol/typescript-sdk` · **open** · updated · 分数 50 · 上游时间 2026-11-14T07:52:08Z

入选依据：T1 watchlist; protocol: schema。

> 上游摘录（未审读）：## Summary 'registerTool()' / 'registerPrompt()' schemas (and elicitation 'requestedSchema') that are themselves already-converted JSON Schema documents — most prominently the output of zod's 'toJSONSchema()', which retains a '~standard' prop whose converters reference the original zod schema — were re-converted through those converters on every 'tools/list' and 'toolInputSchemaJson()' call, instead of being used dir

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(uri-template): support the ';' operator and RFC 6570 empty-list expansion](https://github.com/modelcontextprotocol/typescript-sdk/pull/3183)

`modelcontextprotocol/typescript-sdk` · **open** · new · 分数 50 · 上游时间 2026-11-15T01:17:22Z

入选依据：T1 watchlist; protocol: protocol。

> 上游摘录（未审读）：Fixes #3182 Per 'CONTRIBUTING.md' ("Before starting work, comment on the issue so we can assign it to you"), I asked for assignment in https://github.com/modelcontextprotocol/typescript-sdk/issues/3182#issuecomment-6871957250; the issue is still unassigned, so I'm opening this small, test-covered fix now and will hand it over if a maintainer prefers to assign it to someone else. ## Root cause 'packages/core-internal/

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Accept names under 'localhost' for the URLs Protected Resource Metadata publishes](https://github.com/modelcontextprotocol/ruby-sdk/pull/683)

`modelcontextprotocol/ruby-sdk` · **merged** · updated · 分数 44 · 上游时间 2026-11-14T17:39:12Z

入选依据：T3 watchlist; security: authorization; merged implementation; verify release separately。

> 上游摘录（未审读）：## Motivation and Context 'ProtectedResourceMetadata' refused a plain-http 'resource' or 'authorization\_servers' entry unless its host was 'localhost' or a loopback address, so a server that gives each tenant a subdomain could not be run in development as 'http://acme.localhost:3000/mcp': neither the metadata document nor the '401' challenge could be built. Every name under 'localhost' is reserved for loopback and ca

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [mcp: preserve wrapped protocol errors from typed tools](https://github.com/modelcontextprotocol/go-sdk/pull/1528)

`modelcontextprotocol/go-sdk` · **closed** · new · 分数 38 · 上游时间 2026-11-14T12:42:45Z

入选依据：T2 watchlist; protocol: protocol。

> 上游摘录（未审读）：Fixes #1529 Typed tool handlers that wrap a '\*jsonrpc.Error' currently return an 'isError' tool result instead of a JSON-RPC error. Recognize wrapped errors with 'errors.As' and return the underlying protocol error, preserving its code, message, and data. Add a client/server regression test for single, nested, and joined errors.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 发布与安全公告

显示 0 / 0 条；全部数据见当日 JSON。

本日暂无记录。

## 协议 / 工作组提交

显示 0 / 0 条；全部数据见当日 JSON。

本日暂无记录。

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
