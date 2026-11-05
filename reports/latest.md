# MCP Radar · 2026-11-05 (UTC)

采集时间：2026-11-05T13:52:53+00:00 · 回看窗口：14 天。

这是公开来源的更新索引和选题素材，不是已经审读、复现的技术结论。标题和摘录来自上游；优先级由可见规则计算。

本次窗口内 2695 条记录；本日累计 2730 个新增/变更版本；失败端点 0 个；覆盖警告 0 个。

## 覆盖与限制

PR merged 表示代码进入分支，不代表已发布；release 不自动证明符合某协议版本。初次运行只建立窗口基线。

仅跟踪 watchlist 中公开仓库的 PR、指定仓库 issue/commit、release、公开安全公告和订阅源。未提供 API 的社区讨论、社交媒体和完整标准文档变更不在覆盖保证内。RSS 仅提供源当前保留的条目。

本次未报告采集错误或分页截断；这不代表覆盖整个 MCP 生态。

## 重点 PR / 提案

显示 20 / 2576 条；全部数据见当日 JSON。

### [SEP-2076: Agent Skills as a First-Class MCP Primitive](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2076)

`modelcontextprotocol/modelcontextprotocol` · **closed** · baseline · 分数 120 · 上游时间 2026-10-23T03:02:24Z

入选依据：T1 watchlist; breaking: compatib; security: security; protocol: capabilit; proposal: sep-, proposal。

> 上游摘录（未审读）：## Summary - add a draft SEP that defines Agent Skills as a first-class MCP primitive - specify skills/list + skills/get, notifications, capabilities, and data types - document mapping to SKILL.md plus security, compatibility, and testing guidance ## Motivation Agent skills are widely adopted but fragmented; MCP lacks a standard way to distribute skills across existing servers and clients. ## Testing - Not run (docum

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [SEP-2778: Adding Type Constraints to the MCP](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2778)

`modelcontextprotocol/modelcontextprotocol` · **open** · baseline · 分数 120 · 上游时间 2026-11-02T09:09:03Z

入选依据：T1 watchlist; breaking: backward, compatib; security: security, injection; protocol: schema; proposal: sep-。

> 上游摘录（未审读）：By adding constraints this SEP : - Introduces 30+ JSDoc security constraint annotations in 'schema/draft/schema.ts' - Enhances validation rules to mitigate common attack vectors (XSS, open redirects, injection, DoS) - Establishes clear expectations for message formats and limits to improve client/server alignment and interoperability - Ensures backward compatibility while enforcing new constraints for improved securi

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Harmonizing requriements across documents and the conformance suite](https://github.com/modelcontextprotocol/ext-auth/pull/36)

`modelcontextprotocol/ext-auth` · **open** · baseline · 分数 104 · 上游时间 2026-11-02T19:08:14Z

入选依据：T1 watchlist; breaking: breaking; security: security; protocol: conformance。

> 上游摘录（未审读）：Clarified DPoP proof validation requirements and replay protection mechanisms for MCP servers, emphasizing the rejection of invalid 'iat' claims and the use of nonces for enhanced security. ## Motivation and Context ## How Has This Been Tested? ## Breaking Changes ## Types of changes - \[ \] Bug fix (non-breaking change which fixes an issue) - \[ \] New feature (non-breaking change which adds functionality) - \[ \] Breakin

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(client): detect authorization-server migration from fresh PRM](https://github.com/modelcontextprotocol/typescript-sdk/pull/2450)

`modelcontextprotocol/typescript-sdk` · **closed** · baseline · 分数 104 · 上游时间 2026-10-27T10:48:12Z

入选依据：T1 watchlist; breaking: migration; security: authorization; protocol: sse。

> 上游摘录（未审读）：## Previously unaddressed #2358 isolated credentials by issuer once the current authorization server was known, but cached discovery could keep the client pinned to AS-A after a fresh 'resource\_metadata' challenge selected AS-B. Existing tests had to clear discovery manually before migration was detected. ## This PR - re-probes cached discovery only for a fresh resource-metadata challenge - compares the newly PRM-val

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(auth): expose identity assertions on OAuth provider wrappers](https://github.com/PrefectHQ/fastmcp/pull/6006)

`PrefectHQ/fastmcp` · **merged** · baseline · 分数 102 · 上游时间 2026-10-26T04:58:20Z

入选依据：T1 watchlist; security: oauth; protocol: sse; proposal: sep-; merged implementation; verify release separately。

> 上游摘录（未审读）：Fixes #6005 ## Summary 'OAuthProxy' and 'OIDCProxy' already support SEP-990 ID-JAG through 'identity\_assertion', but provider-specific constructors reject the option. Forward the optional configuration from all ten provider wrappers to their proxy base constructors, with no change when it is omitted. - Expose 'identity\_assertion: IdentityAssertion \| None = None' in Google, GitHub, Azure, Discord, Hugging Face, WorkOS

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(mysql-mcp-server): reject mutating keywords split by any whitespace](https://github.com/awslabs/mcp/pull/4837)

`awslabs/mcp` · **merged** · baseline · 分数 102 · 上游时间 2026-10-27T17:09:22Z

入选依据：T2 watchlist; breaking: breaking; security: cve-; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：Read-only mode built its keyword patterns with 're.escape' over the whole phrase, baking in a single literal space, so a multi-word keyword separated by two spaces / a tab / a newline (e.g. 'LOAD DATA') bypassed the gate. The builder now joins words with '\\s+', so any whitespace between the words is matched. Whitespace variant of CVE-2026-85788 (CWE-184). Non-breaking. User experience: with read-only mode enabled, wr

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add Kiro Crew to extension support matrix](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3461)

`modelcontextprotocol/modelcontextprotocol` · **merged** · baseline · 分数 102 · 上游时间 2026-10-28T17:23:01Z

入选依据：T1 watchlist; security: oauth; protocol: protocol, stdio; proposal: extension; merged implementation; verify release separately。

> 上游摘录（未审读）：Add Kiro Crew after PostHog Code with MCP Apps support. Kiro Crew renders MCP Apps ('io.modelcontextprotocol/ui', 2026-01-26 stable) for stdio servers routed through its gateway: https://github.com/kirodotdev/KiroCrew/blob/main/src/kiro\_crew/docs/mcp-apps.md Quick check on the other extensions across Kiro products (2026-10-28): Kiro Crew - OAuth Client Credentials: no. The only client\_credentials grant is for its Mic

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Wire OIDC transport flags into thv run auth middleware config](https://github.com/stacklok/toolhive/pull/6529)

`stacklok/toolhive` · **merged** · baseline · 分数 102 · 上游时间 2026-10-23T13:30:54Z

入选依据：T2 watchlist; breaking: deprecat; security: token; protocol: transport; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary 'thv run' accepts '--thv-ca-bundle', '--jwks-auth-token-file' and '--oidc-insecure-allow-http', but none of them reach the token validator. The CLI builds the OIDC config twice: 'WithOIDCConfig' fills the deprecated top-level 'RunConfig.OIDCConfig' with every field, while 'setupOIDCConfiguration' → 'createOIDCConfig' builds the 'TokenValidatorConfig' that 'WithMiddlewareFromFlags' serializes into the auth

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [SEP-3149: Require Token Endpoint Auth Methods Supported in CIMD](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3149)

`modelcontextprotocol/modelcontextprotocol` · **open** · baseline · 分数 100 · 上游时间 2026-10-31T06:41:53Z

入选依据：T1 watchlist; breaking: deprecat; security: token; proposal: sep-。

> 上游摘录（未审读）：## Motivation and Context This SEP makes the 'token\_endpoint\_auth\_methods\_supported' metadata parameter a required property of MCP Client ID Metadata Documents (CIMD), and creates a deprecation path for the singular 'token\_endpoint\_auth\_method' parameter, mirroring the guidance in \[OpenID Connect RP Metadata Choices 1.0\](https://openid.net/specs/openid-connect-rp-metadata-choices-1\_0-final.html). This enables a CIMD

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[Server\] Bind Streamable HTTP sessions to the principal that opened them](https://github.com/modelcontextprotocol/php-sdk/pull/627)

`modelcontextprotocol/php-sdk` · **open** · baseline · 分数 98 · 上游时间 2026-11-04T22:04:00Z

入选依据：T3 watchlist; breaking: breaking; security: security; protocol: protocol, streamable; proposal: specification。

> 上游摘录（未审读）：Fixes #529 A handshake-era session now only serves the principal that opened it, as the \[security best practices\](https://modelcontextprotocol.io/specification/2025-11-25/basic/security\_best\_practices#session-hijacking) recommend. When another principal sends the session id, the server answers 404 like for an unknown session, and its 'DELETE' doesn't end the session. I found this while building an MCP server for the

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Streamable HTTP: no precedence between UnsupportedProtocolVersionError (-32022) and HeaderMismatch (-32020) when an unsupported version arrives without the modern headers](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/3449)

`modelcontextprotocol/modelcontextprotocol` · **open** · baseline · 分数 94 · 上游时间 2026-11-04T17:11:31Z

入选依据：T1 watchlist; breaking: compatib; protocol: protocol, transport, streamable; proposal: specification。

> 上游摘录（未审读）：### What's broken? The spec is ambiguous or self-contradictory ### Where in the spec or docs? https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http#protocol-version-header (also '#server-validation' on the same page, and https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning#compatibility-matrix). The 'draft' pages have the same text. ### What should happen? The

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [SEP-2293: Add Support for Completions Metadata](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2293)

`modelcontextprotocol/modelcontextprotocol` · **open** · baseline · 分数 94 · 上游时间 2026-11-02T09:09:12Z

入选依据：T1 watchlist; breaking: breaking; protocol: protocol; proposal: sep-。

> 上游摘录（未审读）：This supercedes #589 authored by @kentcdodds to bring it to the new SEP format. The text below is broadly the same. This adds (non-breaking) support for 'title' and 'description' in the completions server response which clients can use to display something different for a value than the value itself. : https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1440 ## Motivation and Context @connor4312 \[demo

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Fix helm chart deployments to OC](https://github.com/IBM/mcp-context-forge/pull/4954)

`IBM/mcp-context-forge` · **open** · baseline · 分数 92 · 上游时间 2026-10-22T16:00:21Z

入选依据：T2 watchlist; breaking: migration; security: security; protocol: timeout。

> 上游摘录（未审读）：## 🔗 Related Issue Closes #4952 --- ## 📝 Summary Fixes OpenShift deployment failures caused by hardcoded UID/GID values in pod security contexts that conflict with OpenShift's Security Context Constraints (SCC). Problems Fixed: Migration job timeout: Job pods would never start in OpenShift, timing out after 5 minutes with no activity Wrong image version pulled: Deployment upgrades would show the correct image tag in

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Update clients page link in README.md](https://github.com/modelcontextprotocol/ext-apps/pull/838)

`modelcontextprotocol/ext-apps` · **merged** · baseline · 分数 92 · 上游时间 2026-11-03T23:29:41Z

入选依据：T2 watchlist; breaking: breaking; protocol: protocol; proposal: extension; merged implementation; verify release separately。

> 上游摘录（未审读）：Replace modelcontextprotocol.io/clients (which currently redirects to the introductory docs) with modelcontextprotocol.io/extensions/client-matrix to point directly to the relevant client matrix information. ## Motivation and Context ## How Has This Been Tested? ## Breaking Changes ## Types of changes - \[ \] Bug fix (non-breaking change which fixes an issue) - \[ \] New feature (non-breaking change which adds functional

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [redirect URIs using localhost](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/3223)

`modelcontextprotocol/modelcontextprotocol` · **closed** · baseline · 分数 92 · 上游时间 2026-10-31T06:41:55Z

入选依据：T1 watchlist; security: oauth, authorization; protocol: protocol; proposal: specification。

> 上游摘录（未审读）：### What's broken? The spec conflicts with an RFC or standard it references ### Where in the spec or docs? https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration#client-id-metadata-documents ### What should happen? Redirect URIs using localhost go against recommendations given by \[Section 8.3\](https://datatracker.ietf.org/doc/html/rfc8252#section-8.3) of OAuth 2.0 for Native

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [A list of Implementation Requirements for OAuth Client ID Metadata Document](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/3224)

`modelcontextprotocol/modelcontextprotocol` · **closed** · baseline · 分数 92 · 上游时间 2026-10-31T06:41:55Z

入选依据：T1 watchlist; security: oauth, authorization; protocol: protocol; proposal: specification。

> 上游摘录（未审读）：### What's broken? The spec is ambiguous or self-contradictory ### Where in the spec or docs? https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration ### What should happen? MCP Clients should include property 'redirect\_uris' + at least one element in it (redirect\_uri). 'redirect\_uris' is a JSON array that can be empty. ### What actually happens? A list of requirements include

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Access Token Privilege Restriction: does "MUST NOT pass through" cover an API of the same authorization server/project (Supabase Edge MCP pattern)?](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/3413)

`modelcontextprotocol/modelcontextprotocol` · **open** · baseline · 分数 92 · 上游时间 2026-11-03T01:15:02Z

入选依据：T1 watchlist; security: security, authorization, token; protocol: protocol; proposal: specification。

> 上游摘录（未审读）：### What's broken? The spec is ambiguous or self-contradictory ### Where in the spec or docs? https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations#access-token-privilege-restriction ### What should happen? The spec should state clearly whether "The MCP server \*\*MUST NOT\*\* pass through the token it received from the MCP client" applies when the "upstream" API is part of

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Icon origin guidance differs between basic/index and Icon.src](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/3486)

`modelcontextprotocol/modelcontextprotocol` · **open** · baseline · 分数 92 · 上游时间 2026-11-04T17:10:20Z

入选依据：T1 watchlist; security: security; protocol: protocol, schema; proposal: specification。

> 上游摘录（未审读）：### What's broken? The JSON schema disagrees with the spec prose ### Where in the spec or docs? https://modelcontextprotocol.io/specification/2026-07-28/basic/index (section 'icons', "Security considerations"; schema.ts 'Icon.src') ### What should happen? State one policy for remotely fetched icons in both places, define which origin the check uses, and, if trusted external origins are allowed, say how a consumer dec

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Tool annotations: the spec does not say how the untrusted-annotations rule applies to clients that force a tool call](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/3492)

`modelcontextprotocol/modelcontextprotocol` · **open** · baseline · 分数 92 · 上游时间 2026-11-04T17:08:03Z

入选依据：T1 watchlist; security: security; protocol: protocol; proposal: specification。

> 上游摘录（未审读）：### What's broken? The spec doesn't cover a case it clearly should ### Where in the spec or docs? https://modelcontextprotocol.io/specification/2026-07-28/server/tools#tool (the Warning under 'annotations') and https://modelcontextprotocol.io/specification/2026-07-28/server/tools#security-considerations ### What should happen? A short note after the Warning, for example: > Note: because annotations from untrusted ser

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [SEP-1932: DPoP Profile for MCP](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1932)

`modelcontextprotocol/modelcontextprotocol` · **open** · baseline · 分数 92 · 上游时间 2026-11-02T09:08:58Z

入选依据：T1 watchlist; security: security, authorization, token; protocol: protocol, sse; proposal: sep-, specification, extension。

> 上游摘录（未审读）：## Motivation and Context This extension defines DPoP (Demonstrating Proof-of-Possession) support for the Model Context Protocol, enabling sender-constrained access tokens that prevent token replay attacks. This extension builds upon the baseline authorization requirements defined in the main Authorization specification. DPoP binds access tokens to a cryptographic key pair controlled by the client. When accessing MCP

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 发布与安全公告

显示 15 / 96 条；全部数据见当日 JSON。

### [1.0.4](https://github.com/modelcontextprotocol/inspector/releases/tag/1.0.4)

`modelcontextprotocol/inspector` · **published** · baseline · 分数 129 · 上游时间 2026-11-04T23:28:28Z

入选依据：T1 watchlist; breaking: deprecat; security: security; protocol: protocol, schema; release。

> 上游摘录（未审读）：## What's Changed ### v1.x security fixes 1.0.4 is a security release for the deprecated v1 line. Upgrade with 'npx @modelcontextprotocol/inspector@v1-latest', or move to v2 ('@latest'). \* \*\*Server-supplied 'pattern' regexes are no longer evaluated.\*\* Patterns in a tool's output schema and in an elicitation's requested schema are stripped before validation, including patterns reachable through '$ref', and the elicita

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [2.14.0](https://github.com/modelcontextprotocol/inspector/releases/tag/2.14.0)

`modelcontextprotocol/inspector` · **published** · baseline · 分数 129 · 上游时间 2026-11-04T23:55:33Z

入选依据：T1 watchlist; breaking: deprecat; security: security, vulnerab, ghsa-; protocol: protocol; release。

> 上游摘录（未审读）：## What's Changed ### Security fixes 2.14.0 fixes three vulnerabilities reported privately against v2. Upgrade with 'npx @modelcontextprotocol/inspector@latest'. One of them, GHSA-2fw8-7jmw-r937, also affects the deprecated v1 line, where it is fixed in 1.0.4 ('@v1-latest'). \* \*\*An MCP App can no longer navigate its sandbox frame away from the policy it was given.\*\* The proxy enforces a frame policy built from the ap

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [AI-Infra-Guard v4.6.9](https://github.com/Tencent/AI-Infra-Guard/releases/tag/v4.6.9)

`Tencent/AI-Infra-Guard` · **published** · baseline · 分数 103 · 上游时间 2026-11-05T04:02:08Z

入选依据：T1 watchlist; breaking: compatib; protocol: timeout; release。

> 上游摘录（未审读）：## \[v4.6.9\] - 2026-11-05 ### Added - \*\*Agent-Scan\*\*: Add CloudGPU provider preset (PR #734, 1c69920f) ### Fixed - \*\*Utils\*\*: Add timeouts to task-server HTTP clients (PR #740, de5d9f4f) - \*\*MCP-Scan\*\*: Accept XML-attribute parameter tags from OpenAI-compatible models (PR #739, 7e6df02a) - \*\*MCP-Scan\*\*: Normalize mixed-case MCP SARIF rule IDs (PR #733, 4bb6ac21) - \*\*Agent-Scan\*\*: Accept null content deltas and usage-o

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v4.1.4: Token Gesture](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.1.4)

`PrefectHQ/fastmcp` · **published** · baseline · 分数 101 · 上游时间 2026-10-26T06:23:37Z

入选依据：T1 watchlist; security: oauth, token; protocol: transport, sse; release。

> 上游摘录（未审读）：Generated CLIs now preserve remote transports, empty arrays, and parameters whose names collide with their own helpers; mounted servers honor session visibility and 'mounted\_components\_raise\_on\_load\_error', a stale client context no longer closes a newer session, and OAuth provider wrappers accept identity assertions. Tasks accept a redis-py credential provider that returns current credentials for each new connection

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [HTTP client transports followed cross-origin redirects carrying custom headers and bodies](https://github.com/modelcontextprotocol/python-sdk/security/advisories/GHSA-5h93-6whr-6q8j)

`modelcontextprotocol/python-sdk` · **published** · baseline · 分数 101 · 上游时间 2026-10-27T19:22:57Z

入选依据：T1 watchlist; security: oauth; protocol: transport, streamable, sse; advisory。

> 上游摘录（未审读）：### Summary In affected versions, the SDK's Streamable HTTP and SSE client transports followed HTTP redirects to any host. If the configured MCP endpoint answered with a redirect to a different origin: - custom headers set on the client (for example an 'X-API-Key' credential) were sent to that origin, and - on a '307' or '308' redirect the request body was re-sent there too. The SDK's OAuth client providers followed

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [@modelcontextprotocol/client@2.4.0](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/%40modelcontextprotocol/client%402.4.0)

`modelcontextprotocol/typescript-sdk` · **published** · baseline · 分数 101 · 上游时间 2026-10-23T18:19:05Z

入选依据：T1 watchlist; security: authorization, token; protocol: protocol; release。

> 上游摘录（未审读）：### Minor Changes - \[#3085\](https://github.com/modelcontextprotocol/typescript-sdk/pull/3085) \['a633756'\](https://github.com/modelcontextprotocol/typescript-sdk/commit/a63375661399956a744ff8b34d03d36e3d09e98a) Thanks \[@claude\](https://github.com/apps/claude)! - Add an opt-in for sending 'scope' on refresh-token requests, for authorization servers that reject a refresh without it (Microsoft Entra ID answers 'AADSTS900

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [0.16.0](https://github.com/modelcontextprotocol/kotlin-sdk/releases/tag/0.16.0)

`modelcontextprotocol/kotlin-sdk` · **published** · baseline · 分数 97 · 上游时间 2026-10-27T17:57:11Z

入选依据：T3 watchlist; breaking: breaking, deprecat; protocol: protocol, transport, streamable; proposal: sep-; release。

> 上游摘录（未审读）：## Description This release closes memory-exhaustion holes in the WebSocket and Streamable HTTP servers, deprecates the SSE transport in favor of Streamable HTTP, moves APIs deprecated in 0.9.0–0.13.0 to 'ERROR', and adds experimental SEP-2575 discovery types. ### Breaking Changes \*\*Streamable HTTP sessions expire when idle and are capped\*\* by @devcrocod in \[#1032\](https://github.com/modelcontextprotocol/kotlin-sdk/p

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [@modelcontextprotocol/core@2.4.0](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/%40modelcontextprotocol/core%402.4.0)

`modelcontextprotocol/typescript-sdk` · **published** · baseline · 分数 91 · 上游时间 2026-10-23T18:19:02Z

入选依据：T1 watchlist; protocol: protocol; proposal: sep-, extension; release。

> 上游摘录（未审读）：### Minor Changes - \[#3047\](https://github.com/modelcontextprotocol/typescript-sdk/pull/3047) \['46d9c99'\](https://github.com/modelcontextprotocol/typescript-sdk/commit/46d9c9921b6542e813c1ecc5f9fc964085e8e3bb) Thanks \[@KKonstantinov\](https://github.com/KKonstantinov), \[@tobi-oye\](https://github.com/tobi-oye), \[@mattzcarey\](https://github.com/mattzcarey)! - Add the Skills extension (SEP-2640), reachable through new 'e

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [AWS API MCP Server OAuth Token Audience Validation Bypass](https://github.com/awslabs/mcp/security/advisories/GHSA-4prq-p2x5-w9fh)

`awslabs/mcp` · **published** · baseline · 分数 89 · 上游时间 2026-10-27T18:11:12Z

入选依据：T2 watchlist; security: oauth, audience, token; protocol: protocol, transport, streamable; advisory。

> 上游摘录（未审读）：### Summary The AWS API MCP Server is an open source Model Context Protocol (MCP) server that enables AI assistants to interact with AWS services and resources through AWS CLI commands. An issue exists where, when the server is configured to use the streamable-http transport with OAuth authentication, a bearer token that the configured identity provider issued to a different application in the same tenant is accepted

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [rmcp-v3.7.0](https://github.com/modelcontextprotocol/rust-sdk/releases/tag/rmcp-v3.7.0)

`modelcontextprotocol/rust-sdk` · **published** · baseline · 分数 89 · 上游时间 2026-10-22T20:07:24Z

入选依据：T2 watchlist; security: token; protocol: protocol, transport; release。

> 上游摘录（未审读）：### Added - \*(auth)\* support OIDC ID-token subjects in enterprise exchange (\[#1385\](https://github.com/modelcontextprotocol/rust-sdk/pull/1385)) ### Fixed - \*(auth)\* allow cross-origin resource\_metadata urls (\[#1302\](https://github.com/modelcontextprotocol/rust-sdk/pull/1302)) - \*(transport)\* keep 401/403 status when the body is a JSON-RPC error (\[#1341\](https://github.com/modelcontextprotocol/rust-sdk/pull/1341)) ##

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [OAuth authorization-server metadata SSRF filter checks host strings, not resolved addresses (incomplete fix of GHSA-c9xm-49cp-xcr9)](https://github.com/modelcontextprotocol/rust-sdk/security/advisories/GHSA-5p52-q7pq-9fq2)

`modelcontextprotocol/rust-sdk` · **published** · baseline · 分数 89 · 上游时间 2026-10-22T20:27:37Z

入选依据：T2 watchlist; security: ghsa-, oauth, authorization; protocol: transport, sse; advisory。

> 上游摘录（未审读）：## Summary The fix for GHSA-c9xm-49cp-xcr9 (#935) closed the 'resource\_metadata' path with a same-origin requirement, but the 'authorization\_servers' path it also hardened is guarded by a host-string denylist only. A hostname that resolves to a disallowed address passes the check, and the client fetches it. ## Details 'is\_allowed\_authorization\_server\_metadata\_url' ('crates/rmcp/src/transport/auth.rs') guards authoriz

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v2.1.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.1.0)

`modelcontextprotocol/servers` · **published** · baseline · 分数 89 · 上游时间 2026-10-25T00:03:20Z

入选依据：T2 watchlist; security: security, vulnerab; protocol: protocol; release。

> 上游摘录（未审读）：## Security fixes v2.1.0 fixes eight vulnerabilities in three servers. Upgrade '@modelcontextprotocol/server-filesystem' and '@modelcontextprotocol/server-everything' to 2.0.1, and 'mcp-server-fetch' to 2026.10.24. \| Package \| Affected \| Fixed in \| \| --- \| --- \| --- \| \| '@modelcontextprotocol/server-filesystem' \| 1.0.0 through 2.0.0, and date versions through 2026.8.31 \| 2.0.1 \| \| '@modelcontextprotocol/server-everyt

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v0.13.2](https://github.com/sparfenyuk/mcp-proxy/releases/tag/v0.13.2)

`sparfenyuk/mcp-proxy` · **published** · baseline · 分数 89 · 上游时间 2026-11-01T21:56:54Z

入选依据：T2 watchlist; security: security, ghsa-; protocol: sse; release。

> 上游摘录（未审读）：Security patch: upgrade certifi to 2026.10.19 and require that minimum for new installations. This removes trust in the compromised emSign ECC Root CA - G3 while retaining unaffected emSign roots. Addresses GHSA-6q48-6c7w-9gw2 and Dependabot alert 55. Existing security dependency minimums remain unchanged. Upgrade existing installations, for example with 'uv tool upgrade mcp-proxy', or rebuild containers against this

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v0.13.3](https://github.com/sparfenyuk/mcp-proxy/releases/tag/v0.13.3)

`sparfenyuk/mcp-proxy` · **published** · baseline · 分数 89 · 上游时间 2026-11-02T08:02:08Z

入选依据：T2 watchlist; security: security; protocol: transport; release。

> 上游摘录（未审读）：Security hardening for HTTP transports and diagnostic logging. - Validate Host and Origin before routing, session creation and backend forwarding, including default and named servers. - Require MCP SDK 1.30 or newer for its redirect and request-body protections; raw HTTP clients no longer follow redirects automatically. - Keep credentials, query values, session IDs and payloads out of routine transport diagnostics; p

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Routine transport diagnostics disclose credentials, query values and MCP session or payload data](https://github.com/sparfenyuk/mcp-proxy/security/advisories/GHSA-4h57-262x-9x24)

`sparfenyuk/mcp-proxy` · **published** · baseline · 分数 89 · 上游时间 2026-11-02T08:17:14Z

入选依据：T2 watchlist; security: token; protocol: transport, sse; advisory。

> 上游摘录（未审读）：### Impact Routine diagnostics could expose arbitrary custom credential headers and URL userinfo/query values. The custom client logged request headers at INFO and masked only a short list of conventional names; headers such as Private-Token and X-Auth-Token were not protected. Default HTTPX diagnostics could also include the full request URL. Server/client SDK DEBUG paths emitted message bodies or SSE endpoint/sessi

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 协议 / 工作组提交

显示 10 / 57 条；全部数据见当日 JSON。

### [Move OAuth Client Credentials to stable](https://github.com/modelcontextprotocol/ext-auth/commit/a90221ae4e42582e3e038b42ff1e6b0ca28ccdcb)

`modelcontextprotocol/ext-auth` · **committed** · baseline · 分数 97 · 上游时间 2026-10-23T15:33:52Z

入选依据：T1 watchlist; security: oauth; protocol: protocol; proposal: sep-, specification, extension。

> 上游摘录（未审读）：Move OAuth Client Credentials to stable Move the specification from specification/draft/ to specification/stable/oauth-client-credentials/2026-07-28/ and add a draft/ copy beside it. SEP-3392 classifies both ext-auth extensions as Stable. The text is unchanged apart from the protocol revision in the Info line.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Publish Enterprise-Managed Authorization as a dated revision](https://github.com/modelcontextprotocol/ext-auth/commit/f58587c41323f4cb06e3016c10c1e86f613196a1)

`modelcontextprotocol/ext-auth` · **committed** · baseline · 分数 97 · 上游时间 2026-10-23T15:33:31Z

入选依据：T1 watchlist; security: authorization; protocol: protocol; proposal: sep-, specification, extension。

> 上游摘录（未审读）：Publish Enterprise-Managed Authorization as a dated revision Move the specification to specification/stable/enterprise-managed-authorization/2026-07-28/ and add a draft/ copy beside it, the layout SEP-3392 describes for a Stable extension. The text is unchanged apart from the Info line, which now states the protocol revision.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add Kiro Crew to extension support matrix (#3461)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/f66b955ef9c42b87c856c5640ac09b425cbb4d44)

`modelcontextprotocol/modelcontextprotocol` · **committed** · baseline · 分数 97 · 上游时间 2026-10-28T17:23:00Z

入选依据：T1 watchlist; security: oauth; protocol: protocol, stdio; proposal: extension。

> 上游摘录（未审读）：docs: add Kiro Crew to extension support matrix (#3461) Add Kiro Crew after PostHog Code with MCP Apps support. Kiro Crew renders MCP Apps ('io.modelcontextprotocol/ui', 2026-01-26 stable) for stdio servers routed through its gateway: https://github.com/kirodotdev/KiroCrew/blob/main/src/kiro\_crew/docs/mcp-apps.md Quick check on the other extensions across Kiro products (2026-10-28): Kiro Crew - OAuth Client Credentia

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: fix client-credentials samples and pin the issuer (#3472)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/da72d8e77a619b3213f1d31fdaa5a3a43c97a14c)

`modelcontextprotocol/modelcontextprotocol` · **committed** · baseline · 分数 89 · 上游时间 2026-10-30T18:12:49Z

入选依据：T1 watchlist; breaking: deprecat; security: oauth。

> 上游摘录（未审读）：docs: fix client-credentials samples and pin the issuer (#3472) The Python samples on the OAuth Client Credentials page pass scopes= to ClientCredentialsOAuthProvider and PrivateKeyJWTOAuthProvider, which raises TypeError on mcp 2.3.0 (the parameter is scope=). With that fixed, omitting issuer= emits MCPDeprecationWarning and will be required in 3.0. The TypeScript samples construct ClientCredentialsProvider and Priv

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: bring the Inspector pages up to 2.13.0 (#3483)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/c1c81072057ed9a3eb40a1213eb7577651c1937b)

`modelcontextprotocol/modelcontextprotocol` · **committed** · baseline · 分数 81 · 上游时间 2026-10-31T07:38:00Z

入选依据：T1 watchlist; security: security; protocol: protocol。

> 上游摘录（未审读）：docs: bring the Inspector pages up to 2.13.0 (#3483) Pages touched, in both docs/docs/2026-07-28 and docs/docs/draft: inspector/cli.mdx, inspector/configuration.mdx, inspector/mcpdo.mdx, inspector/protocol-eras.mdx, inspector/recipes.mdx, inspector/security.mdx, inspector/web.mdx. Claude-Session: https://claude.ai/code/session\_016HDqNadqLF55K3ioiJHQwA Co-authored-by: Claude

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: fix dead links to the ext-auth specifications (#3470)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/0b5e9de21a432aae0d778f169b8973567144bf11)

`modelcontextprotocol/modelcontextprotocol` · **committed** · baseline · 分数 77 · 上游时间 2026-10-30T08:04:34Z

入选依据：T1 watchlist; security: oauth; proposal: sep-, specification, extension。

> 上游摘录（未审读）：docs: fix dead links to the ext-auth specifications (#3470) ext-auth moved its specification files on 2026-10-23 to the SEP-3392 layout, specification/stable/ / / .mdx. GitHub does not redirect moved files, so the previous links returned 404. Updated links in: - docs/extensions/auth/oauth-client-credentials.mdx - docs/extensions/auth/overview.mdx - blog/content/posts/enterprise-managed-auth/index.md - seps/2133-exten

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Add Glean to extension support matrix (#3495)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/66c6a64582db1cffb744f03cf5273304a5931959)

`modelcontextprotocol/modelcontextprotocol` · **committed** · baseline · 分数 77 · 上游时间 2026-11-03T00:42:30Z

入选依据：T1 watchlist; security: authorization; proposal: extension。

> 上游摘录（未审读）：Add Glean to extension support matrix (#3495) Glean supports MCP Apps, Enterprise-Managed Authorization, Skills and Tasks, as reported by the Glean team. Co-authored-by: Claude Opus 5.5

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Merge pull request #37 from modelcontextprotocol/paulc/sep3392-alignment](https://github.com/modelcontextprotocol/ext-auth/commit/15ca394e00a66434520b9ade26294999295a43ae)

`modelcontextprotocol/ext-auth` · **committed** · baseline · 分数 71 · 上游时间 2026-10-23T16:24:05Z

入选依据：T1 watchlist; protocol: protocol; proposal: sep-, extension。

> 上游摘录（未审读）：Merge pull request #37 from modelcontextprotocol/paulc/sep3392-alignment Align stable extensions with conventions in SEP-3392

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix: keep extension fields on CreateTaskResult and GetTaskResult (#32)](https://github.com/modelcontextprotocol/ext-tasks/commit/5f68e144656118bd3f20a0713700219d4a114370)

`modelcontextprotocol/ext-tasks` · **committed** · baseline · 分数 71 · 上游时间 2026-11-04T20:58:08Z

入选依据：T1 watchlist; protocol: schema; proposal: extension。

> 上游摘录（未审读）：fix: keep extension fields on CreateTaskResult and GetTaskResult (#32) Both results extend the open Result type, but their v2 schemas were plain z.object wrappers, so unknown top-level keys were stripped on the polling path. The notification params schema already uses openObject for the same reason. Use it for both results as well, so projectTask() sees the same extension fields whether a task arrives by tasks/get or

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: point legacy extension negotiation at graceful degradation](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/04bd3f462497858d5f7758e7fffe6946c200e0c9)

`modelcontextprotocol/modelcontextprotocol` · **committed** · baseline · 分数 71 · 上游时间 2026-10-27T02:34:04Z

入选依据：T1 watchlist; protocol: negotiat; proposal: extension。

> 上游摘录（未审读）：docs: point legacy extension negotiation at graceful degradation Co-Authored-By: Claude Opus 5.5 (1M context)

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 文章与技术解释

显示 1 / 1 条；全部数据见当日 JSON。

### [The Official Ruby SDK for MCP Reaches Tier 1](https://blog.modelcontextprotocol.io/posts/ruby-sdk-tier-1/)

`mcp-official-blog` · **published** · baseline · 分数 66 · 上游时间 2026-10-30T09:00:00+00:00

入选依据：T1 watchlist; protocol: protocol, conformance; proposal: specification。

> 上游摘录（未审读）：The official Ruby SDK for the Model Context Protocol is now a Tier 1 SDK under the MCP SDK tiering system, with full support for the 2026-07-28 MCP specification and a 100% conformance pass rate across both scored spec versions.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 博客选题工作台

从上面的重点项挑选，不自动把提案写成已实现功能：

- 协议问题：规范原文、提案状态、旧行为与新行为。
- 实现证据：PR diff、回归测试、客户端/服务端版本。
- 复现：最小实验、消息/HTTP trace、失败与成功条件。
- 结论边界：事实、维护者解释、个人判断分别记录。

模板：[知识库写作模板](https://github.com/xixiaxibro/mcp-knowledge-base/tree/main/templates)。
