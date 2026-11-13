# MCP Radar · 2026-11-13 (UTC)

采集时间：2026-11-13T01:29:29+00:00 · 回看窗口：14 天。

这是公开来源的更新索引和选题素材，不是已经审读、复现的技术结论。标题和摘录来自上游；优先级由可见规则计算。

本次窗口内 2592 条记录；本日累计 478 个新增/变更版本；失败端点 0 个；覆盖警告 0 个。

## 覆盖与限制

PR merged 表示代码进入分支，不代表已发布；release 不自动证明符合某协议版本。初次运行只建立窗口基线。

仅跟踪 watchlist 中公开仓库的 PR、指定仓库 issue/commit、release、公开安全公告和订阅源。未提供 API 的社区讨论、社交媒体和完整标准文档变更不在覆盖保证内。RSS 仅提供源当前保留的条目。

本次未报告采集错误或分页截断；这不代表覆盖整个 MCP 生态。

## 重点 PR / 提案

显示 20 / 465 条；全部数据见当日 JSON。

### [Omit app-only ui\_get unless the client advertises MCP Apps](https://github.com/github/github-mcp-server/pull/3687)

`github/github-mcp-server` · **open** · updated · 分数 92 · 上游时间 2026-11-10T05:16:10Z

入选依据：T1 watchlist; security: token; protocol: protocol, stdio; proposal: extension。

> 上游摘录（未审读）：## Summary Do not list the app-only 'ui\_get' tool to clients that lack MCP Apps support, on both the remote (HTTP) server and the local stdio server. ## Why 'ui\_get' is marked '\_meta.ui.visibility: \["app"\]'. Apps hosts hide that from the model; other clients ignore the meta and hand the helper to the model, wasting tokens. A client that supports Apps declares 'extensions\["io.modelcontextprotocol/ui"\]'. The remote ser

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [sep(SEP-3543): make the MCP project a CVE Numbering Authority](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3543)

`modelcontextprotocol/modelcontextprotocol` · **open** · updated · 分数 92 · 上游时间 2026-11-12T14:35:02Z

入选依据：T1 watchlist; security: security; protocol: protocol; proposal: sep-, specification。

> 上游摘录（未审读）：Proposes that the MCP project applies to the CVE Program to become a CVE Numbering Authority (CNA), so that maintainers assign CVE IDs and publish CVE records for the specification and the 'modelcontextprotocol' repositories without waiting on GitHub's CNA queue. Reports still arrive through GitHub Security Advisories. Only the party that assigns the ID and publishes the record changes. The SEP is in 'seps/0000-mcp-a

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(proxy): relay non-object tool results across MCP versions](https://github.com/PrefectHQ/fastmcp/pull/5763)

`PrefectHQ/fastmcp` · **merged** · new · 分数 88 · 上游时间 2026-11-10T19:50:36Z

入选依据：T1 watchlist; breaking: compatib; protocol: schema; merged implementation; verify release separately。

> 上游摘录（未审读）：## Description Fixes #5762 A proxy could advertise a backend's non-object output schema to an older MCP client, causing 'tools/list' to fail. Non-object structured results also raised while FastMCP built a 'ToolResult'. The proxy now advertises a 'result' wrapper for older clients and exposes the original structured value to 2026-07-28 clients and response middleware. Compatibility wrapping happens at the outgoing MC

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Fix the CLI .js deprecation warning and a dead error-message link](https://github.com/PrefectHQ/fastmcp/pull/6453)

`PrefectHQ/fastmcp` · **merged** · new · 分数 88 · 上游时间 2026-11-11T23:34:03Z

入选依据：T1 watchlist; breaking: deprecat; protocol: transport, stdio; merged implementation; verify release separately。

> 上游摘录（未审读）：two user-facing messages were wrong. 'fastmcp list ./server.js' and 'fastmcp call ./server.js' printed a 'FastMCPDeprecationWarning' telling the user to pass 'pathlib.Path(...)', advice a CLI user can't act on, because the CLI handed the raw string to 'Client'. the CLI now builds the same 'NodeStdioTransport' that 'Client' would infer, without the warning. separately, the ASGI lifespan error linked to 'gofastmcp.com/

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(mcp-scan,skill-scan,agent-scan): normalize hex-suffixed tool-call tags](https://github.com/Tencent/AI-Infra-Guard/pull/752)

`Tencent/AI-Infra-Guard` · **merged** · updated · 分数 88 · 上游时间 2026-11-12T02:17:24Z

入选依据：T1 watchlist; breaking: compatib; protocol: protocol; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary Some OpenAI-compatible models answer the text-based tool-call protocol with hex-suffixed tags (' NAME>', ' ... ', etc.) instead of ' V '. The existing parsers do not match them, so 'finish' is never recognized and every stage loops until 'max\_iter' (see #751). This PR adds 'utils/tool\_format\_fix.py' to each of the three scanners. Its 'normalize\_tool\_calls(content) -> (content, fixed)' rewrites the known ma

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Add a v1 npm deprecate step to the release skill](https://github.com/modelcontextprotocol/inspector/pull/2968)

`modelcontextprotocol/inspector` · **merged** · new · 分数 88 · 上游时间 2026-11-12T05:56:04Z

入选依据：T1 watchlist; breaking: deprecat; protocol: protocol; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #2954 Adds \*\*v1-6. Deprecate the version just published\*\* to the 'release' skill's v1 flow, after v1-5 (Verify). The old v1-6 (release notes for unpublished advisories) becomes v1-7; nothing outside the skill referenced the step numbers. The new step covers each acceptance criterion: - \*\*Exact version, all four packages\*\*: '@modelcontextprotocol/{inspector,inspector-cli,inspector-client,inspector-server}@X.Y.Z

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: clarify that deprecation does not remove the latest flag](https://github.com/modelcontextprotocol/registry/pull/1854)

`modelcontextprotocol/registry` · **merged** · new · 分数 88 · 上游时间 2026-11-12T18:12:14Z

入选依据：T1 watchlist; breaking: deprecat; protocol: lifecycle; merged implementation; verify release separately。

> 上游摘录（未审读）：A deprecated server version can remain 'isLatest: true', which led clients in #1819 to interpret latest as active. Clarify that deprecation alone does not remove the flag and that clients must check lifecycle status separately. Explain that selecting an older active version requires inspecting version history and applying a client policy. Update the API reference, metadata guide, checked-in OpenAPI description, and r

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(auth): include DNS in SSRF deadline](https://github.com/PrefectHQ/fastmcp/pull/5509)

`PrefectHQ/fastmcp` · **merged** · new · 分数 86 · 上游时间 2026-11-10T19:31:17Z

入选依据：T1 watchlist; security: security, ssrf; protocol: timeout; merged implementation; verify release separately。

> 上游摘录（未审读）：## Description The SSRF fetch helper's 'overall\_timeout' does not bound DNS resolution. A slow DNS lookup can keep the request running well beyond the configured overall limit. Apply the overall deadline to the full operation, including DNS resolution. Closes #5508 ## Contribution type - \[x\] Bug fix (simple, well-scoped fix for a clearly broken behavior) - \[ \] Documentation improvement - \[ \] Enhancement ## Checklist

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix: decode URI fragments before schema reference hydration](https://github.com/PrefectHQ/fastmcp/pull/5561)

`PrefectHQ/fastmcp` · **merged** · new · 分数 86 · 上游时间 2026-11-10T19:30:25Z

入选依据：T1 watchlist; security: token; protocol: schema; merged implementation; verify release separately。

> 上游摘录（未审读）：Fixes #5560. When an output schema retains a reference such as '#/$defs/Observation%20time', 'Client.call\_tool(...).data' keeps the referenced date-time as a string. Decode the URI fragment once before splitting its JSON Pointer path and unescaping tokens, so the referenced type and constraints survive hydration. Remove only the leading '#/' prefix; default schema dereferencing and ordinary/tilde-escaped references r

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Fix #5563: OTel: prefer 'AccessToken.subject' over 'client\_id' for 'enduser.id'](https://github.com/PrefectHQ/fastmcp/pull/5565)

`PrefectHQ/fastmcp` · **merged** · new · 分数 86 · 上游时间 2026-11-10T19:30:14Z

入选依据：T1 watchlist; security: token; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：Fixes #5563 ## What changed Set OTel 'enduser.id' to 'token.subject or token.client\_id' in 'get\_auth\_span\_attributes()', added subject-preference/fallback tests, and updated telemetry docs. ## Verification 'python -m pytest -q -x tests/telemetry/test\_module.py' passed

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: clarify tool errors and middleware transformations](https://github.com/PrefectHQ/fastmcp/pull/5566)

`PrefectHQ/fastmcp` · **merged** · new · 分数 86 · 上游时间 2026-11-10T19:30:06Z

入选依据：T1 watchlist; security: authorization; protocol: protocol; merged implementation; verify release separately。

> 上游摘录（未审读）：## Description 'ToolError' can report a business error the LLM can recover from, but the error-handling docs leave exception choice, protocol responses, logging, and telemetry easy to conflate. Clarify those distinctions in the existing Tools and Middleware sections, with a date-range example and guidance for validation, authorization, and missing entities. Explain 'ErrorHandlingMiddleware''s cause-based conversions,

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix: preserve referenced schema definitions](https://github.com/PrefectHQ/fastmcp/pull/5588)

`PrefectHQ/fastmcp` · **merged** · updated · 分数 86 · 上游时间 2026-11-10T19:50:50Z

入选依据：T1 watchlist; security: token; protocol: schema; merged implementation; verify release separately。

> 上游摘录（未审读）：## Description Fixes #5587. Renaming a tool could remove definitions still referenced by its input schema: '#/$defs/Display~1name' lost 'Display/name', and '#/$defs/Envelope/properties/name' lost 'Envelope'. Schema compression now decodes the fragment and JSON Pointer token before tracking the owning definition, preserving valid references while continuing to prune unused definitions. This follows \[RFC 6901's pointer

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [test: isolate consent checks and preserve OpenAPI download budget](https://github.com/PrefectHQ/fastmcp/pull/5664)

`PrefectHQ/fastmcp` · **merged** · new · 分数 86 · 上游时间 2026-11-10T19:36:18Z

入选依据：T1 watchlist; security: authorization, token; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：Consent-binding tests currently contact GitHub with fake authorization codes, so a slow token endpoint can prevent them from reaching their consent assertions. Mock only the external token exchange and additionally assert that it was awaited with the expected code and returned the intended 500 response. The consent, cookie, and callback paths remain real. The OpenAPI performance test also grants its download thirty s

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(client): preserve a caller-provided OAuth httpx client factory when verify is set](https://github.com/PrefectHQ/fastmcp/pull/5849)

`PrefectHQ/fastmcp` · **merged** · new · 分数 86 · 上游时间 2026-11-10T08:16:41Z

入选依据：T1 watchlist; security: oauth; protocol: transport, timeout; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #5848 ## Description 'Client(transport, verify=True)' silently replaced an OAuth 'httpx\_client\_factory' supplied by the caller, losing proxy, mTLS, header, timeout or retry behavior for OAuth discovery/preflight requests. The transports themselves preserve caller factories and only inject a verify factory over the bare default; the Client-level resync lacked that distinction. ## What changed - Transport-genera

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Accept WorkOS tokens when required\_scopes is set](https://github.com/PrefectHQ/fastmcp/pull/5881)

`PrefectHQ/fastmcp` · **merged** · new · 分数 86 · 上游时间 2026-11-10T19:44:53Z

入选依据：T1 watchlist; security: oauth, token; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：WorkOSProvider passed its required\_scopes into WorkOSTokenVerifier, which compares them against a 'scope' or 'scopes' field in the '/oauth2/userinfo' response. That endpoint returns identity claims only, so every token looked scope-less and was rejected whenever required\_scopes was non-empty, including the '\["openid", "profile", "email"\]' setup shown in the WorkOS docs. The check exists so the verifier no longer clai

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Forward URL-mode elicitation through the proxy](https://github.com/PrefectHQ/fastmcp/pull/5980)

`PrefectHQ/fastmcp` · **merged** · updated · 分数 86 · 上游时间 2026-11-10T19:44:06Z

入选依据：T1 watchlist; security: oauth; protocol: schema; merged implementation; verify release separately。

> 上游摘录（未审读）：## Description The proxy's elicitation relay only knew form mode: for a URL-mode elicitation (new in 2025-11-25) it sent the client a form request with an empty schema, dropping the URL and the elicitation ID. The client showed an empty form instead of the link, so OAuth or payment flows behind a proxy could not happen. The relay now forwards URL-mode requests with 'session.elicit\_url': '''python # backend: context.s

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(transforms): enforce wall-clock timeout and external callback limit in MontySandboxProvider and CodeMode](https://github.com/PrefectHQ/fastmcp/pull/6063)

`PrefectHQ/fastmcp` · **merged** · updated · 分数 86 · 上游时间 2026-11-10T19:31:57Z

入选依据：T1 watchlist; security: security; protocol: timeout; merged implementation; verify release separately。

> 上游摘录（未审读）：### Summary In FastMCP's experimental CodeMode, untrusted model-generated code runs in pydantic-monty sandbox while tool calls are bridged via asynchronous host callbacks. While Monty enforces instruction and feed duration limits internally, Monty's max\_feed\_duration\_secs excludes time spent awaiting host callbacks. Consequently: 1. Long-running or hanging host callbacks are decoupled from sandbox time limits, allowi

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Authenticate and pin the schema download in the OpenAPI performance test](https://github.com/PrefectHQ/fastmcp/pull/6177)

`PrefectHQ/fastmcp` · **merged** · updated · 分数 86 · 上游时间 2026-11-10T16:53:29Z

入选依据：T1 watchlist; security: token; protocol: schema; merged implementation; verify release separately。

> 上游摘录（未审读）：\_Requested by \*\*nate\*\* · \[project thread\](https://claude.ai/code/project/chan\_01EkwKAptPX4vtXECnAMud7W?thread=cmsg\_01EkwKAptPX4vtXECnAMud7W98PGEF3PwGdwYJ7cd3UmWP)\_ ## Description 'test\_github\_api\_schema\_performance' downloads GitHub's ~10MB API schema from raw.githubusercontent.com anonymously on every run. On #6175 it failed twice in a row with '429 Too Many Requests'. The job already has 'FASTMCP\_GITHUB\_TOKEN', so

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(auth): Add KeystoneTokenVerifier](https://github.com/PrefectHQ/fastmcp/pull/6264)

`PrefectHQ/fastmcp` · **merged** · updated · 分数 86 · 上游时间 2026-11-10T19:26:24Z

入选依据：T1 watchlist; security: token; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：## Description Closes #6262 ## Contribution type - \[x\] Enhancement (maintainers typically implement enhancements — see \[CONTRIBUTING.md\](../CONTRIBUTING.md)) ## Checklist - \[x\] This PR addresses an existing issue (or fixes a self-evident bug) - \[x\] I have read \[CONTRIBUTING.md\](../CONTRIBUTING.md) - \[x\] I have added tests that cover my changes - \[x\] I have run 'uv run prek run --all-files' and all checks pass - \[x\] I

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Normalize raw-string redirect URIs through AnyUrl before validation](https://github.com/PrefectHQ/fastmcp/pull/6315)

`PrefectHQ/fastmcp` · **merged** · updated · 分数 86 · 上游时间 2026-11-10T00:38:42Z

入选依据：T1 watchlist; security: security; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：Fixes #6295 ## User-visible change A plain-string redirect URI validated differently than the same URI passed as 'AnyUrl'. 'AnyUrl' applies WHATWG-style normalization (backslash in the authority becomes a path separator, '..' segments are resolved, IPv4 shorthand like '127.1' is expanded, trailing C0 characters are stripped), while raw strings went straight to 'urlparse'. An attacker-controlled spelling such as 'http

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 发布与安全公告

显示 9 / 9 条；全部数据见当日 JSON。

### [\[paths.ts\] CWE-863 Authorization Bypass](https://github.com/modelcontextprotocol/inspector/security/advisories/GHSA-5572-x678-xmv8)

`modelcontextprotocol/inspector` · **published** · new · 分数 81 · 上游时间 2026-11-12T01:33:54Z

入选依据：T1 watchlist; security: security, vulnerab, authorization; advisory。

> 上游摘录（未审读）：# Security Advisory: \[paths.ts\] CWE-863 Authorization Bypass ## 1. Executive Summary & Affected Component - \*\*Advisory ID:\*\* 'AUTO-66' - \*\*Ecosystem / Program:\*\* Anthropic Bug Bounty (Official MCP) - \*\*Severity:\*\* 'HIGH' - \*\*Vulnerability Classification:\*\* CWE-863 Authorization Bypass - \*\*Verified Target Source File:\*\* 'clients/mcpdo/src/daemon/paths.ts' - \*\*Affected Lines / Boundary:\*\* 'getDaemonSocketPath Windows b

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[fetchGuard.ts\] CWE-918: Server-Side Request Forgery (SSRF)](https://github.com/modelcontextprotocol/inspector/security/advisories/GHSA-fvg8-f358-w2c8)

`modelcontextprotocol/inspector` · **published** · new · 分数 81 · 上游时间 2026-11-12T01:33:28Z

入选依据：T1 watchlist; security: security, vulnerab, ssrf; advisory。

> 上游摘录（未审读）：# Security Advisory: \[fetchGuard.ts\] CWE-918: Server-Side Request Forgery (SSRF) ## 1. Executive Summary & Affected Component - \*\*Advisory ID:\*\* 'AUTO-391' - \*\*Ecosystem / Program:\*\* Anthropic Bug Bounty (Official MCP) - \*\*Severity:\*\* 'HIGH' - \*\*Vulnerability Classification:\*\* CWE-918: Server-Side Request Forgery (SSRF) - \*\*Verified Target Source File:\*\* 'core/mcp/node/fetchGuard.ts' - \*\*Affected Lines / Boundary:\*\*

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [server.json import: declared environment-variable defaults change what the reviewed command runs (NODE\_OPTIONS, npm\_config\_registry), outside the 2.14 launch preview](https://github.com/modelcontextprotocol/inspector/security/advisories/GHSA-pp85-586h-2m95)

`modelcontextprotocol/inspector` · **published** · new · 分数 81 · 上游时间 2026-11-12T01:33:39Z

入选依据：T1 watchlist; security: ghsa-; advisory。

> 上游摘录（未审读）：### Summary 2.14.0 (GHSA-rwv7-mh2c-ff2p) added a "Command to Run" preview to the web client's server.json import, described in the UI as exactly what will be saved and run, and validates the package identifier/version and env-var \*names\* so a document can't smuggle runtime flags. The preview lists env vars by name only, but 'environmentVariables\[\].default' / '.value' is copied verbatim into the saved config's 'env',

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [A malicious MCP server can crash the Inspector proxy and all its sessions via an unbounded POST SSE response](https://github.com/modelcontextprotocol/inspector/security/advisories/GHSA-9w48-x22j-rrm7)

`modelcontextprotocol/inspector` · **published** · new · 分数 75 · 上游时间 2026-11-12T01:34:05Z

入选依据：T1 watchlist; protocol: sse; advisory。

> 上游摘录（未审读）：### Summary A connected MCP server that answers a JSON-RPC request with a 'text/event-stream' POST response, withholds the final reply, and keeps the stream open makes the Inspector web backend buffer the whole stream with no size cap. Backend memory grows until the Node process exits with a JavaScript heap OOM, dropping every session on that backend. The attacker is the upstream server; it needs no Inspector credent

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [2026.11.20261109200750](https://github.com/awslabs/mcp/releases/tag/2026.11.20261109200750)

`awslabs/mcp` · **published** · new · 分数 63 · 上游时间 2026-11-09T23:42:08Z

入选依据：T2 watchlist; protocol: sse; release。

> 上游摘录（未审读）：# 2026.11.20261109200750 ## What's Changed \* fix(amazon-sns-sqs-mcp-server): remove pytest from runtime dependencies by @kluacisco888 in https://github.com/awslabs/mcp/pull/4557 \* fix(billing-cost-management-mcp-server): aws-pricing tells filter misses from bad service codes by @finklen-amazon in https://github.com/awslabs/mcp/pull/4895 \* fix(billing-cost-management-mcp-server): document COA account scope and criteri

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [rmcp-macros-v3.10.0](https://github.com/modelcontextprotocol/rust-sdk/releases/tag/rmcp-macros-v3.10.0)

`modelcontextprotocol/rust-sdk` · **published** · new · 分数 63 · 上游时间 2026-11-12T22:15:10Z

入选依据：T2 watchlist; protocol: protocol, stdio, lifecycle; release。

> 上游摘录（未审读）：### Other - \*(macros)\* document the Send limitation on async #\[tool\]/#\[prompt\] bodies (\[#1396\](https://github.com/modelcontextprotocol/rust-sdk/pull/1396)) - \*(service)\* clarify startup and stdio lifecycle (\[#1387\](https://github.com/modelcontextprotocol/rust-sdk/pull/1387))

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [rmcp-v3.10.0](https://github.com/modelcontextprotocol/rust-sdk/releases/tag/rmcp-v3.10.0)

`modelcontextprotocol/rust-sdk` · **published** · new · 分数 63 · 上游时间 2026-11-12T22:15:38Z

入选依据：T2 watchlist; protocol: protocol; release。

> 上游摘录（未审读）：### Added - load skills from a directory tree (\[#1409\](https://github.com/modelcontextprotocol/rust-sdk/pull/1409)) ### Fixed - preserve tools with dependency property-name maps (\[#1428\](https://github.com/modelcontextprotocol/rust-sdk/pull/1428)) ### Other - \*(macros)\* document the Send limitation on async #\[tool\]/#\[prompt\] bodies (\[#1396\](https://github.com/modelcontextprotocol/rust-sdk/pull/1396)) - \*(service)\* cl

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v4.2.0a5: Skillium Fancyson](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.0a5)

`PrefectHQ/fastmcp` · **prerelease** · new · 分数 55 · 上游时间 2026-11-13T00:34:20Z

入选依据：T1 watchlist; release。

> 上游摘录（未审读）：FastMCP 4.2.0a5 adds 'SkillManifestProvider', which serves skills from their manifests (frontmatter plus each file's digest and size) and reads a file only when a client reads it, so skills kept in a bucket or database don't have to be loaded to answer 'skills/list'. 'SkillCatalogProvider' now builds on it and no longer re-hashes every file on each request. Since a4, a dependency can own the tool argument it reads th

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [AI-Infra-Guard v4.6.10](https://github.com/Tencent/AI-Infra-Guard/releases/tag/v4.6.10)

`Tencent/AI-Infra-Guard` · **published** · new · 分数 55 · 上游时间 2026-11-12T04:08:36Z

入选依据：T1 watchlist; release。

> 上游摘录（未审读）：## \[v4.6.10\] - 2026-11-12 ### Added - \*\*Data\*\*: Add 19 AI product CVE advisories from NVD (PR #749, c33f4116) - \*\*Compliance\*\*: Add a local generative AI safety self-check (PR #748, 970bea9f) - \*\*Data\*\*: Add 15 AI product CVE advisories from NVD (PR #745, 29b004de) - \*\*Data\*\*: Add 33 AI product CVE advisories from NVD (PR #743, 6ee3cde7) - \*\*Data\*\*: Add 35 AI product CVE advisories from NVD (PR #742, 1050abe7) - \*\*Da

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 协议 / 工作组提交

显示 4 / 4 条；全部数据见当日 JSON。

### [docs: working-group sponsored SEP process (#3529)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/99a8e4605c4278b6f905c98e585f98b393b15623)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 55 · 上游时间 2026-11-12T12:37:38Z

入选依据：T1 watchlist; protocol: protocol。

> 上游摘录（未审读）：docs: working-group sponsored SEP process (#3529) \_Requested by \*\*David Soria Parra\*\* · \[Slack thread\](https://ant-mcp-oss.slack.com/archives/C0BDGKP4PC6/p1794253161846999)\_ \*\*Before:\*\* The contributing page told protocol-change proposers to discuss the idea, build a prototype, and then find a sponsor. The SEP guidelines defined a sponsor as an individual Core Maintainer, Maintainer or WG Lead whom the author found b

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs(seps): fix dead link targets in SEP documents (#3547)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/2eb3a8e345aaee53461a3c5c5f6900659d3ecb27)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 51 · 上游时间 2026-11-12T12:31:12Z

入选依据：T1 watchlist; proposal: sep-。

> 上游摘录（未审读）：docs(seps): fix dead link targets in SEP documents (#3547) \_Requested by \*\*David Soria Parra\*\* · \[Slack thread\](https://ant-mcp-oss.slack.com/archives/C0BDGKP4PC6/p1794253161846999)\_ \*\*Before:\*\* The link scan over the rendered SEP pages reports 46 dead links across six SEPs (SEP-2640, SEP-1865, SEP-1577, SEP-2133, SEP-2575 and SEP-3398). A reader who clicks one lands on a GitHub 404 page, or nothing happens because t

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: pull registry docs from v1.8.9 (#3480)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/06e923405df3df242f1471b9300d9db90ebd10fd)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 35 · 上游时间 2026-11-12T13:28:21Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：docs: pull registry docs from v1.8.9 (#3480) \_Requested by \*\*Den Delimarsky, David Soria Parra\*\* · \[Slack thread\](https://ant-mcp-oss.slack.com/archives/C0BDGKP4PC6/p1793430342149349)\_ Squash-merge with this description as the commit message. The two trailers on the last lines must stay in it, so that the next subtree pull starts from this one. \*\*Before:\*\* 'docs/registry/' reflects the registry docs as of 2026-01-22

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs(community): list Core Primitives WG on working groups overview (#3544)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/d72c778b468f82b2c6431e5d64f7524c4ad01374)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 35 · 上游时间 2026-11-12T12:32:45Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：docs(community): list Core Primitives WG on working groups overview (#3544) \_Requested by \*\*David Soria Parra\*\* · \[Slack thread\](https://ant-mcp-oss.slack.com/archives/C0BDGKP4PC6/p1793975038956449)\_ Follow-up to #3513. \*\*Before:\*\* The working groups overview lists 14 working groups and omits Core Primitives. The roadmap names the group, and it has leads, a repository and a weekly meeting. \*\*After:\*\* The overview has

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
