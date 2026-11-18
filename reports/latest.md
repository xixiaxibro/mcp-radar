# MCP Radar · 2026-11-18 (UTC)

采集时间：2026-11-18T01:17:06+00:00 · 回看窗口：14 天。

这是公开来源的更新索引和选题素材，不是已经审读、复现的技术结论。标题和摘录来自上游；优先级由可见规则计算。

本次窗口内 2247 条记录；本日累计 370 个新增/变更版本；失败端点 2 个；覆盖警告 0 个。

## 覆盖与限制

PR merged 表示代码进入分支，不代表已发布；release 不自动证明符合某协议版本。初次运行只建立窗口基线。

仅跟踪 watchlist 中公开仓库的 PR、指定仓库 issue/commit、release、公开安全公告和订阅源。未提供 API 的社区讨论、社交媒体和完整标准文档变更不在覆盖保证内。RSS 仅提供源当前保留的条目。

- 采集失败：`modelcontextprotocol/ruby-sdk` / releases — The read operation timed out
- 采集失败：`modelcontextprotocol/servers` / pulls — The read operation timed out

## 重点 PR / 提案

显示 20 / 358 条；全部数据见当日 JSON。

### [docs: architecture spec page still presents sampling as a core feature, but is depricated](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/3548)

`modelcontextprotocol/modelcontextprotocol` · **closed** · updated · 分数 94 · 上游时间 2026-11-16T17:32:48Z

入选依据：T1 watchlist; breaking: deprecat; protocol: protocol; proposal: sep-, specification。

> 上游摘录（未审读）：### What's broken? The documentation is wrong or misleading ### Where in the spec or docs? https://modelcontextprotocol.io/specification/draft/architecture ### What should happen? The architecture page should not present Sampling as a core, current feature. SEP-2577 deprecates Sampling and Roots as of '2026-07-28', and they are listed in the \[deprecated features registry\](https://modelcontextprotocol.io/specification

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Omit app-only ui\_get unless the client advertises MCP Apps](https://github.com/github/github-mcp-server/pull/3687)

`github/github-mcp-server` · **open** · updated · 分数 92 · 上游时间 2026-11-16T16:58:55Z

入选依据：T1 watchlist; security: token; protocol: protocol, stdio; proposal: extension。

> 上游摘录（未审读）：## Summary Do not list the app-only 'ui\_get' tool to clients that lack MCP Apps support, on both the remote (HTTP) server and the local stdio server. ## Why 'ui\_get' is marked '\_meta.ui.visibility: \["app"\]'. Apps hosts hide that from the model; other clients ignore the meta and hand the helper to the model, wasting tokens. A client that supports Apps declares 'extensions\["io.modelcontextprotocol/ui"\]'. The remote ser

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(auth): accept same-origin issuers at any address](https://github.com/modelcontextprotocol/rust-sdk/pull/1467)

`modelcontextprotocol/rust-sdk` · **open** · new · 分数 92 · 上游时间 2026-11-17T15:19:33Z

入选依据：T2 watchlist; breaking: breaking; security: oauth, authorization; protocol: transport。

> 上游摘录（未审读）：## Motivation and Context Following up on #1393, OAuth discovery now accepts an authorization server on the resource’s own origin, regardless of its IP address type. ## How Has This Been Tested? Added tests ## Breaking Changes None. ## Types of changes - \[x\] Bug fix (non-breaking change which fixes an issue) - \[ \] New feature (non-breaking change which adds functionality) - \[ \] Breaking change (fix or feature that wo

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Raise opentelemetry-api floor past traceparent ReDoS](https://github.com/PrefectHQ/fastmcp/pull/6513)

`PrefectHQ/fastmcp` · **merged** · new · 分数 86 · 上游时间 2026-11-17T06:41:46Z

入选依据：T1 watchlist; security: security, ghsa-; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：\_Requested by \*\*nate\*\* · \[project thread\](https://claude.ai/code/project/chan\_01EkwKAptPX4vtXECnAMud7W?thread=cmsg\_01EkwKAptPX4vtXECnAMud7WKQkjNJULhP3qTKG2vgzT6T)\_ ## Description 'extract\_trace\_context' passes a client's 'params.\_meta.traceparent' straight to the W3C propagator, which is exactly the path \[GHSA-mf5v-w3w3-f6cg\](https://github.com/advisories/GHSA-mf5v-w3w3-f6cg) describes: a crafted traceparent (long wh

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[4.1\] Raise opentelemetry-api floor past traceparent ReDoS](https://github.com/PrefectHQ/fastmcp/pull/6514)

`PrefectHQ/fastmcp` · **merged** · new · 分数 86 · 上游时间 2026-11-17T06:41:51Z

入选依据：T1 watchlist; security: security, ghsa-; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：\_Requested by \*\*nate\*\* · \[project thread\](https://claude.ai/code/project/chan\_01EkwKAptPX4vtXECnAMud7W?thread=cmsg\_01EkwKAptPX4vtXECnAMud7WKQkjNJULhP3qTKG2vgzT6T)\_ ## Description Backport to 'release/4.1'. 'extract\_trace\_context' passes a client's 'params.\_meta.traceparent' straight to the W3C propagator, which is exactly the path \[GHSA-mf5v-w3w3-f6cg\](https://github.com/advisories/GHSA-mf5v-w3w3-f6cg) describes: a c

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Keep provider required\_scopes when a custom token\_verifier is passed](https://github.com/PrefectHQ/fastmcp/pull/6535)

`PrefectHQ/fastmcp` · **merged** · new · 分数 86 · 上游时间 2026-11-17T18:44:14Z

入选依据：T1 watchlist; security: security, token; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：\_Requested by \*\*nate\*\* · \[project thread\](https://claude.ai/code/project/chan\_01EkwKAptPX4vtXECnAMud7W?thread=cmsg\_01EkwKAptPX4vtXECnAMud7WVfK2vaQQebD7SUMTYsjCQx)\_ 'AuthKitProvider', 'SupabaseProvider', 'KeycloakAuthProvider', 'ScalekitProvider', 'DescopeProvider' and 'Auth0MCPProvider' accept both 'required\_scopes' and 'token\_verifier', but when a custom verifier was passed, 'RemoteAuthProvider' took its scopes from

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(fingerprint): add MCP Inspector fingerprint and CVE-2025-49596 rule](https://github.com/Tencent/AI-Infra-Guard/pull/768)

`Tencent/AI-Infra-Guard` · **merged** · updated · 分数 86 · 上游时间 2026-11-17T02:09:33Z

入选依据：T1 watchlist; security: cve-, ghsa-; protocol: protocol, transport; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary Adds detection for MCP Inspector ('@modelcontextprotocol/inspector'), the official MCP debugging tool, plus a rule for CVE-2025-49596 / GHSA-7f8r-222p-6f5g. Nothing under 'data/' mentions Inspector today. - 'data/fingerprints/mcp-inspector.yaml': 'GET /config' on the proxy (port 6277) returns 'defaultEnvironment', 'defaultCommand' and 'defaultArgs' but not 'defaultTransport'. - 'data/vuln/mcp-inspector/CVE

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(transport): answer malformed Streamable HTTP bodies with 400](https://github.com/modelcontextprotocol/rust-sdk/pull/1464)

`modelcontextprotocol/rust-sdk` · **open** · new · 分数 82 · 上游时间 2026-11-16T19:31:04Z

入选依据：T2 watchlist; breaking: breaking; protocol: protocol, transport, streamable; proposal: specification。

> 上游摘录（未审读）：## Motivation and Context According to the \[transport spec\](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports#sending-messages-to-the-server), 'StreamableHttpService' should respond to a POST body that isn’t a JSON-RPC message with 400 Bad Request and a JSON-RPC parse error, instead of 415 Unsupported Media Type. ## How Has This Been Tested? Added tests ## Breaking Changes None ## Types of cha

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs(examples): add skills server and client examples](https://github.com/modelcontextprotocol/rust-sdk/pull/1466)

`modelcontextprotocol/rust-sdk` · **open** · new · 分数 82 · 上游时间 2026-11-16T20:09:10Z

入选依据：T2 watchlist; breaking: breaking; protocol: stdio; proposal: extension。

> 上游摘录（未审读）：## Motivation and Context 'skills-fs' shipped in v3.10.0 with a wiring snippet in the module docs but no runnable example. This adds a stdio server that serves a skill folder and a client that walks the extension from the host side. ## How Has This Been Tested? ## Breaking Changes None. ## Types of changes - \[ \] Bug fix (non-breaking change which fixes an issue) - \[ \] New feature (non-breaking change which adds funct

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(mcp-scan,skill-scan): stop reading a reply that only repeats closing tags](https://github.com/Tencent/AI-Infra-Guard/pull/769)

`Tencent/AI-Infra-Guard` · **open** · new · 分数 78 · 上游时间 2026-11-17T03:43:03Z

入选依据：T1 watchlist; breaking: compatib; protocol: timeout。

> 上游摘录（未审读）：## Summary After a finished tool call, some models keep writing a run of closing tags until the server cuts the stream: ''' ... ... (about 220,000 characters) ''' Observed with 'hy4-flash' through an OpenAI-compatible gateway. Effects: - One reply takes 200-220 s to receive. The 300 s 'stream\_timeout' does not help, because the stream ends by itself before the deadline. - The whole reply, junk included, is appended t

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Output Schema: say how a server can change a tool's 'outputSchema' without breaking clients that cached it](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/3554)

`modelcontextprotocol/modelcontextprotocol` · **open** · updated · 分数 78 · 上游时间 2026-11-16T17:32:27Z

入选依据：T1 watchlist; breaking: breaking; protocol: schema。

> 上游摘录（未审读）：The Output Schema section says servers \*\*MUST\*\* return structured results that conform to the schema, and clients \*\*SHOULD\*\* validate them against it. It doesn't say which schema applies when the two sides hold different versions. Clients cache tool lists, so after a server changes a tool, a client can validate a new result against the old schema. What happened to us: our server removed two fields that a tool's 'outp

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Add opt-in GraphQL query and mutation tools](https://github.com/github/github-mcp-server/pull/3877)

`github/github-mcp-server` · **open** · new · 分数 76 · 上游时间 2026-11-17T22:56:42Z

入选依据：T1 watchlist; security: oauth; protocol: sse, capabilit。

> 上游摘录（未审读）：Addresses #2437 and builds on the use case in #645. We run the server as a remote OAuth connector. When GitHub ships a new API capability, agents can already use it through the CLI, but MCP clients need a dedicated tool or another integration. Direct GraphQL would let those clients use the same GitHub credential to read or change issues and projects. This adds a server-side opt-in and a separate GraphQL toolset. Quer

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Strengthen protocol stewardship language in role definitions and details](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2201)

`modelcontextprotocol/modelcontextprotocol` · **merged** · new · 分数 76 · 上游时间 2026-11-17T16:03:29Z

入选依据：T1 watchlist; protocol: protocol; proposal: proposal; merged implementation; verify release separately。

> 上游摘录（未审读）：Following discussion in the main PR thread, this adds language emphasizing protocol stewardship responsibilities alongside technical excellence. \*\*Changes:\*\* - Role Definitions table: Updated Maintainer and Core Maintainer summaries to reflect governance and protocol dimensions - Maintainer responsibilities: Added ecosystem engagement and proposal refinement expectations - Core Maintainer responsibilities: Added emph

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: align the extensions overview with SEP-3392](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3565)

`modelcontextprotocol/modelcontextprotocol` · **merged** · new · 分数 76 · 上游时间 2026-11-17T17:06:54Z

入选依据：T1 watchlist; protocol: lifecycle; proposal: sep-, extension; merged implementation; verify release separately。

> 上游摘录（未审读）：SEP-3392 (Extension Lifecycle) asks for 'docs/extensions/overview.mdx' to be updated to match it once it reaches Final. The overview already follows the SEP's structure, but several details had drifted from the final text. This PR brings them back in line. ## Changes - \*\*Experimental entry\*\*: the stage table now also covers any Maintainer creating an 'experimental-ext-' repository, matching the SEP's stage table and

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(auth): allow same-origin IPv6 ULA issuers](https://github.com/modelcontextprotocol/rust-sdk/pull/1393)

`modelcontextprotocol/rust-sdk` · **merged** · updated · 分数 74 · 上游时间 2026-11-16T19:50:54Z

入选依据：T2 watchlist; security: oauth, authorization; protocol: transport; merged implementation; verify release separately。

> 上游摘录（未审读）：## Motivation and context A resource configured at 'https://\[fd00::1\]:8443/mcp' can advertise 'https://\[fd00::1\]:8443' as its OAuth issuer. In rmcp 3.7, discovery skips that issuer when it appears in 'authorization\_servers'. If it’s the only entry, login fails before the SDK requests its metadata. Allow a native IPv6 unique-local issuer ('fc00::/7') when its scheme, IP address and effective port match the configured

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(auth): omit scope on refresh unless caller sets one](https://github.com/modelcontextprotocol/rust-sdk/pull/1433)

`modelcontextprotocol/rust-sdk` · **merged** · updated · 分数 74 · 上游时间 2026-11-17T02:44:22Z

入选依据：T2 watchlist; security: authorization; protocol: transport; merged implementation; verify release separately。

> 上游摘录（未审读）：fixes #1408 refresh was always sending 'scope' from the stored grant, which some servers (salesforce) reject. rfc 6749 §6 says scope is optional on refresh and leaving it out keeps the original grant. now refresh omits 'scope' unless the caller sets it via 'AuthorizationManager::set\_refresh\_scopes()'. when set, only scopes from the original grant get sent (keeps the #1331 behaviour). if none of them are in the grant,

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(auth): avoid refreshing short-lived access tokens on every call](https://github.com/modelcontextprotocol/rust-sdk/pull/1450)

`modelcontextprotocol/rust-sdk` · **merged** · updated · 分数 74 · 上游时间 2026-11-17T14:58:21Z

入选依据：T2 watchlist; security: token; protocol: transport; merged implementation; verify release separately。

> 上游摘录（未审读）：Fixes #1442 ## Problem get\_access\_token refreshes whenever remaining < 30s. Tokens with expires\_in <= 30s are always inside the window, so every call triggers a refresh (and a rotated refresh token each time). ## Change - Buffer is now min(REFRESH\_BUFFER\_SECS, expires\_in / 2), as agreed in the issue. - Added remaining == 0 so expired tokens with expires\_in <= 1 (buffer 0) still refresh/re-auth instead of being return

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Add default resource limits for MCPRemoteProxy](https://github.com/stacklok/toolhive/pull/7137)

`stacklok/toolhive` · **merged** · updated · 分数 74 · 上游时间 2026-11-16T16:55:48Z

入选依据：T2 watchlist; security: security; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary 'MCPRemoteProxy' has no default resource requests or limits, so a proxy whose CR omits 'spec.resources' runs unbounded. That is the same operational and security gap #2873 closed for 'VirtualMCPServer'. This picks up #5998 by @clxstart (their commit is preserved) and addresses the open review feedback on it. - Apply proxy-runner defaults (requests '50m' CPU / '64Mi' memory, limits '200m' CPU / '256Mi' memo

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Test that act survives ID-JAG redemption](https://github.com/stacklok/toolhive/pull/7156)

`stacklok/toolhive` · **merged** · new · 分数 74 · 上游时间 2026-11-16T22:49:50Z

入选依据：T2 watchlist; security: token; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary A post-merge review of #7147 asked whether the actor named in an ID-JAG reaches the access token issued when the ID-JAG is redeemed. #7149 puts 'act' in the ID-JAG and the redemption handler copies it into the session, but no test followed it all the way to a signed access token. 'TestIDJAGRedemptionAcrossTwoServers' uses a client without an actor profile and asserts there is no 'act', and the handler unit

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(core): add SEP-2549 cache hints to list and read results](https://github.com/modelcontextprotocol/kotlin-sdk/pull/1185)

`modelcontextprotocol/kotlin-sdk` · **open** · new · 分数 72 · 上游时间 2026-11-16T13:04:46Z

入选依据：T3 watchlist; breaking: breaking; protocol: protocol; proposal: sep-。

> 上游摘录（未审读）：Closes #813 ## Breaking Changes None ## Types of changes - \[x\] Bug fix (non-breaking change which fixes an issue) - \[x\] New feature (non-breaking change which adds functionality) - \[x\] Breaking change (fix or feature that would cause existing functionality to change) - \[x\] Documentation update ## Checklist - \[x\] I have read the \[MCP Documentation\](https://modelcontextprotocol.io) - \[x\] My code follows the repository'

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 发布与安全公告

显示 10 / 10 条；全部数据见当日 JSON。

### [v1.9.0-pre.1](https://github.com/modelcontextprotocol/go-sdk/releases/tag/v1.9.0-pre.1)

`modelcontextprotocol/go-sdk` · **prerelease** · new · 分数 105 · 上游时间 2026-11-17T10:02:09Z

入选依据：T2 watchlist; security: oauth; protocol: protocol, negotiat, mrtr; proposal: sep-; release。

> 上游摘录（未审读）：In this release we introduce fixes, hardening, and small API additions on top of \[v1.8.0\](https://github.com/modelcontextprotocol/go-sdk/releases/tag/v1.8.0). It adds no new protocol revision: '2026-07-28' remains the newest version the SDK negotiates. Most changes tighten spec compliance (standard JSON-RPC error codes, exact JSON number decoding without 'float64' rounding, SEP-2243 HTTP headers, MRTR, and OAuth/OIDC

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v2.2.0](https://github.com/modelcontextprotocol/java-sdk/releases/tag/v2.2.0)

`modelcontextprotocol/java-sdk` · **published** · new · 分数 97 · 上游时间 2026-11-16T10:37:02Z

入选依据：T3 watchlist; breaking: breaking; protocol: protocol, streamable; proposal: specification; release。

> 上游摘录（未审读）：## Highlights This release adds support for the \*\*2026-07-28\*\* MCP specification revision: a stateless server and a client in 'io.modelcontextprotocol.modern', next to the existing (legacy) client and server, which are unchanged. The \*\*2026-07-28\*\* specification brought breaking changes to the protocol, and completely revamped the Streamable HTTP. This new protocol is stateless, and drops the concept of session entir

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Improper restriction of intended endpoints in AWS Labs Timestream for InfluxDB MCP Server](https://github.com/awslabs/mcp/security/advisories/GHSA-2f9r-g4f3-wc2j)

`awslabs/mcp` · **published** · new · 分数 89 · 上游时间 2026-11-16T20:40:49Z

入选依据：T2 watchlist; security: token; protocol: protocol; advisory。

> 上游摘录（未审读）：## Summary The AWS Labs Timestream for InfluxDB MCP Server (awslabs.timestream-for-influxdb-mcp-server) is an open source Model Context Protocol (MCP) server that lets MCP clients, such as AI assistants, manage Amazon Timestream for InfluxDB resources and read and write InfluxDB data. An issue exists where, under certain circumstances, the server sends its configured InfluxDB API token to an endpoint that is not the

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [rmcp-v3.11.0](https://github.com/modelcontextprotocol/rust-sdk/releases/tag/rmcp-v3.11.0)

`modelcontextprotocol/rust-sdk` · **published** · new · 分数 89 · 上游时间 2026-11-17T15:33:09Z

入选依据：T2 watchlist; security: token; protocol: protocol, transport; release。

> 上游摘录（未审读）：### Added - \*(client)\* merge cache hints across list pages (\[#1429\](https://github.com/modelcontextprotocol/rust-sdk/pull/1429)) ### Fixed - \*(auth)\* avoid refreshing short-lived access tokens on every call (\[#1450\](https://github.com/modelcontextprotocol/rust-sdk/pull/1450)) - \*(service)\* expose auth challenge on ServiceError::TransportSend (\[#1462\](https://github.com/modelcontextprotocol/rust-sdk/pull/1462)) - \*(au

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v4.2.1: 4, 2, 1... Liftoff](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.1)

`PrefectHQ/fastmcp` · **published** · new · 分数 81 · 上游时间 2026-11-17T20:03:46Z

入选依据：T1 watchlist; security: security, oauth, token; release。

> 上游摘录（未审读）：FastMCP 4.2.1 is a security and correctness patch on top of 4.2.0. It tightens OAuth and token handling: JWTs aren't accepted before their 'nbf', provider 'required\_scopes' survive a custom verifier, pre-registered OAuth clients can be pinned to their issuer, and consent, metadata forwarding and upstream claims in the OAuth proxy are hardened. It also raises the 'opentelemetry-api' floor past a traceparent ReDoS. If

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v0.66.0](https://github.com/stacklok/toolhive/releases/tag/v0.66.0)

`stacklok/toolhive` · **published** · new · 分数 69 · 上游时间 2026-11-16T14:31:22Z

入选依据：T2 watchlist; security: oauth; release。

> 上游摘录（未审读）：## What's Changed \* Add opt-in read-only rootfs for Docker workloads by @sathvik8317 in https://github.com/stacklok/toolhive/pull/7128 \* Render -32042 for Legacy clients that declared URL elicitation by @tgrunnagle in https://github.com/stacklok/toolhive/pull/7114 \* Move OAuth error classification to oauthproto by @jhrozek in https://github.com/stacklok/toolhive/pull/7131 \* Let embedders set the Legacy URL fallback t

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Path traversal and arbitrary file write in the cost report generator of aws-pricing-mcp-server](https://github.com/awslabs/mcp/security/advisories/GHSA-mqm3-w68j-75mw)

`awslabs/mcp` · **published** · new · 分数 63 · 上游时间 2026-11-16T20:08:01Z

入选依据：T2 watchlist; protocol: protocol, capabilit; advisory。

> 上游摘录（未审读）：## Summary AWS Pricing MCP Server is an open source Model Context Protocol (MCP) server that provides real-time AWS pricing information and cost analysis capabilities to AI assistants. An issue exists where, under certain circumstances, the cost report generation tool of the AWS Pricing MCP Server before version 1.0.31 might allow an actor who can influence the MCP agent to write threat actor controlled content to lo

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [rmcp-macros-v3.11.0](https://github.com/modelcontextprotocol/rust-sdk/releases/tag/rmcp-macros-v3.11.0)

`modelcontextprotocol/rust-sdk` · **published** · new · 分数 63 · 上游时间 2026-11-17T15:32:37Z

入选依据：T2 watchlist; protocol: protocol; release。

> 上游摘录（未审读）：### Fixed - \*(client)\* keep private scope when merging pages (\[#1463\](https://github.com/modelcontextprotocol/rust-sdk/pull/1463)) ### Other - add polymarket-agent and tokio-prompt-orchestrator to built with rmcp list (\[#1459\](https://github.com/modelcontextprotocol/rust-sdk/pull/1459))

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [GitHub MCP Server 2.2.0](https://github.com/github/github-mcp-server/releases/tag/v2.2.0)

`github/github-mcp-server` · **published** · new · 分数 55 · 上游时间 2026-11-16T23:30:46Z

入选依据：T1 watchlist; release。

> 上游摘录（未审读）：## 2.2.0 "The one with Skills" ## What's Changed \* fix: return non-nil empty completion results by @omgitsads in https://github.com/github/github-mcp-server/pull/3665 \* Avoid overflow in validation error capacity by @omgitsads in https://github.com/github/github-mcp-server/pull/3772 \* feat(skills): replace server instructions with filtered MCP skills by @SamMorrowDrums in https://github.com/github/github-mcp-server/p

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [2026.11.20261117195521](https://github.com/awslabs/mcp/releases/tag/2026.11.20261117195521)

`awslabs/mcp` · **published** · new · 分数 43 · 上游时间 2026-11-17T23:54:53Z

入选依据：T2 watchlist; release。

> 上游摘录（未审读）：# 2026.11.20261117195521 ## What's Changed \* chore(aws-dataprocessing-mcp): make codeowners changes by @naikvaib in https://github.com/awslabs/mcp/pull/5068 \* fix(billing-cost-management-mcp-server): give sp-explorer start/end filters the form plans return by @finklen-amazon in https://github.com/awslabs/mcp/pull/5039 \* chore(oracle-mcp-server): add code owners by @RobinGolden in https://github.com/awslabs/mcp/pull/5

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 协议 / 工作组提交

显示 2 / 2 条；全部数据见当日 JSON。

### [docs: align the extensions overview with SEP-3392 (#3565)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/d4b317231161ee96d3eefb2448bda4230c76f4c6)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 71 · 上游时间 2026-11-17T17:06:53Z

入选依据：T1 watchlist; protocol: lifecycle; proposal: sep-, extension。

> 上游摘录（未审读）：docs: align the extensions overview with SEP-3392 (#3565) SEP-3392 (Extension Lifecycle) asks for 'docs/extensions/overview.mdx' to be updated to match it once it reaches Final. The overview already follows the SEP's structure, but several details had drifted from the final text. This PR brings them back in line. ## Changes - \*\*Experimental entry\*\*: the stage table now also covers any Maintainer creating an 'experime

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(blog): add a quote block for person quotes (#3563)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/05aeb07b2db0c02adc4813a7c09f208ca8774152)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 35 · 上游时间 2026-11-17T01:20:41Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：feat(blog): add a quote block for person quotes (#3563) Long quotations from named people were written as plain blockquotes: italic text in quotation marks behind a bar, with a '✦ \*\*Name\*\*, Title, Company' line underneath. In the first anniversary post, eleven of them in a row read as a wall of text. ## What changes - \*\*'quote' shortcode on its own\*\* now renders a quote block: a panel on '--surface' in the text colum

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
