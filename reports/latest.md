# MCP Radar · 2026-11-25 (UTC)

采集时间：2026-11-25T01:17:10+00:00 · 回看窗口：14 天。

这是公开来源的更新索引和选题素材，不是已经审读、复现的技术结论。标题和摘录来自上游；优先级由可见规则计算。

本次窗口内 1494 条记录；本日累计 302 个新增/变更版本；失败端点 13 个；覆盖警告 1 个。

## 覆盖与限制

PR merged 表示代码进入分支，不代表已发布；release 不自动证明符合某协议版本。初次运行只建立窗口基线。

仅跟踪 watchlist 中公开仓库的 PR、指定仓库 issue/commit、release、公开安全公告和订阅源。未提供 API 的社区讨论、社交媒体和完整标准文档变更不在覆盖保证内。RSS 仅提供源当前保留的条目。

- 采集失败：`IBM/mcp-context-forge` / releases — Remote end closed connection without response
- 采集失败：`PrefectHQ/fastmcp` / source — Remote end closed connection without response
- 采集失败：`Tencent/AI-Infra-Guard` / pulls — Unterminated string starting at: line 1 column 161681 (char 161680)
- 采集失败：`cloudflare/agents` / pulls — Expecting value: line 1 column 1 (char 0)
- 采集失败：`cloudflare/workers-sdk` / pulls — Remote end closed connection without response
- 采集失败：`github/github-mcp-server` / pulls — Unterminated string starting at: line 1 column 1944664 (char 1944663)
- 采集失败：`modelcontextprotocol/conformance` / pulls — Unterminated string starting at: line 1 column 1781266 (char 1781265)
- 采集失败：`modelcontextprotocol/mcpb` / security-advisories — Remote end closed connection without response
- 采集失败：`modelcontextprotocol/modelcontextprotocol` / security-advisories — Remote end closed connection without response
- 采集失败：`modelcontextprotocol/registry` / security-advisories — Remote end closed connection without response
- 采集失败：`modelcontextprotocol/typescript-sdk` / pulls — Unterminated string starting at: line 1 column 14192 (char 14191)
- 采集失败：`sparfenyuk/mcp-proxy` / releases — Unterminated string starting at: line 1 column 30989 (char 30988)
- 采集失败：`stacklok/toolhive` / security-advisories — Remote end closed connection without response
- 覆盖提示：`modelcontextprotocol/agents-wg` / source — Repository renamed/redirected to modelcontextprotocol/agents-ig

## 重点 PR / 提案

显示 20 / 281 条；全部数据见当日 JSON。

### [feat(web): Events tab (SEP-3415, #3026 phase 3)](https://github.com/modelcontextprotocol/inspector/pull/3038)

`modelcontextprotocol/inspector` · **merged** · new · 分数 102 · 上游时间 2026-11-24T13:16:53Z

入选依据：T1 watchlist; security: oauth; protocol: protocol, capabilit; proposal: sep-, extension; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #3030 Phase 3 of #3026: a web client \*\*Events\*\* tab for the Events extension ('io.modelcontextprotocol/events', SEP-3415), built on the phase 1/2 core APIs. ## What changed - \*\*Tab gating.\*\* '"Events"' is added to 'INSPECTOR\_TAB\_IDS' (with its lifted 'EventsUiState', OAuth-resume snapshot and reset). 'InspectorView' shows it only when 'isEventsSupported(capabilities, protocolEra)' holds: modern era and an adve

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add Gravitee Access Management to the Enterprise-Managed Authorization implementation table](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/3583)

`modelcontextprotocol/modelcontextprotocol` · **open** · new · 分数 92 · 上游时间 2026-11-24T10:33:44Z

入选依据：T1 watchlist; security: oauth, authorization, token; protocol: protocol; proposal: extension。

> 上游摘录（未审读）：### What's broken? The documentation is wrong or misleading ### Where in the spec or docs? https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization#implementation-support ### What should happen? The Implementation support table lists Gravitee Access Management. Since 4.13, its public documentation covers both roles: it issues ID-JAGs through OAuth 2.0 token exchange, and it accepts them for it

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Test/session group oauth refresh](https://github.com/modelcontextprotocol/python-sdk/pull/3908)

`modelcontextprotocol/python-sdk` · **closed** · new · 分数 84 · 上游时间 2026-11-24T20:13:50Z

入选依据：T1 watchlist; breaking: breaking; security: oauth。

> 上游摘录（未审读）：Fixes # ## Motivation and Context ## How Has This Been Tested? ## Breaking Changes ## Types of changes - \[ \] Bug fix (non-breaking change which fixes an issue) - \[ \] New feature (non-breaking change which adds functionality) - \[ \] Breaking change (fix or feature that would cause existing functionality to change) - \[ \] Documentation update ## Checklist - \[ \] I am assigned to the linked issue (or it is labeled 'help wa

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: fix small errors in the 2026-07-28 and draft specification](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3586)

`modelcontextprotocol/modelcontextprotocol` · **merged** · new · 分数 82 · 上游时间 2026-11-24T21:51:29Z

入选依据：T1 watchlist; security: oauth, token; proposal: specification; merged implementation; verify release separately。

> 上游摘录（未审读）：Fixes items b to i of #3491 in the 2026-07-28 and draft versions. Item a was fixed in #3516, so this closes the issue. No requirement changes. Fixes #3491 - \*\*b)\*\* The "Client Features" card on the specification index links to the elicitation page. Its old target does not exist. - \*\*c)\*\* The "Refresh Tokens" reference uses 'draft-ietf-oauth-v2-1-13', like the other OAuth 2.1 references. - \*\*d)\*\* The changelog item on

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [auth: drop the query from the 2025-03-26 fallback authorization base URL](https://github.com/modelcontextprotocol/go-sdk/pull/1348)

`modelcontextprotocol/go-sdk` · **open** · new · 分数 80 · 上游时间 2026-11-24T04:12:57Z

入选依据：T2 watchlist; security: authorization; protocol: protocol; proposal: specification。

> 上游摘录（未审读）：When an MCP server publishes no protected resource metadata, 'AuthorizationCodeHandler' falls back to the \[2025-03-26 rule\](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#server-metadata-discovery): the authorization base URL is the MCP server URL with its path discarded. 'getProtectedResourceMetadata' cleared only the path, so a query or fragment on the server URL stayed in the base URL

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(test-servers): Events extension fixture (SEP-3415, #3026 phase 0)](https://github.com/modelcontextprotocol/inspector/pull/3033)

`modelcontextprotocol/inspector` · **merged** · new · 分数 76 · 上游时间 2026-11-24T07:20:27Z

入选依据：T1 watchlist; protocol: protocol; proposal: sep-, extension; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #3027 Part of #3026. Adds a server-side implementation of the \*\*Events extension\*\* ('io.modelcontextprotocol/events', SEP-3415, Beta) to the composable test server. Phase 1 (#3028) and later phases build against it. No SDK implements Events, so 'test-servers/src/events.ts' is written directly against the spec. It is served as Express middleware ahead of the SDK handler: the modern leg builds a fresh 'McpServer

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(events): core protocol layer for the Events extension (#3028)](https://github.com/modelcontextprotocol/inspector/pull/3036)

`modelcontextprotocol/inspector` · **merged** · new · 分数 76 · 上游时间 2026-11-24T08:28:50Z

入选依据：T1 watchlist; protocol: protocol; proposal: sep-, extension; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #3028 Part of #3026. \*\*Stacked on #3033\*\* (phase 0, the Events test fixture): the base branch is 'v2/feat/3027-events-test-fixture', and the integration tests run against that fixture. Retarget to 'v2/main' once #3033 merges. Phase 1 of the Events extension ('io.modelcontextprotocol/events', SEP-3415, Beta): the core protocol layer. There is no UI here. The SDK has no Events API, so requests go through 'client

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add VS Code to Skills extension column in client matrix](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3510)

`modelcontextprotocol/modelcontextprotocol` · **merged** · updated · 分数 76 · 上游时间 2026-11-23T08:54:11Z

入选依据：T1 watchlist; protocol: protocol; proposal: extension; merged implementation; verify release separately。

> 上游摘录（未审读）：Marks VS Code GitHub Copilot as supporting the \[Skills over MCP\](https://modelcontextprotocol.io/extensions/skills/overview) extension ('io.modelcontextprotocol/skills') in the extension support matrix. Support shipped in VS Code 1.147: \[Skills over MCP are now available in VS Code\](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/skills-over-mcp-are-now-available-in-vs-code/4574580). The 'chat.agentHos

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: mark Skills support for Claude and Claude Code in the extension matrix](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3588)

`modelcontextprotocol/modelcontextprotocol` · **merged** · new · 分数 76 · 上游时间 2026-11-24T21:48:40Z

入选依据：T1 watchlist; protocol: protocol; proposal: extension; merged implementation; verify release separately。

> 上游摘录（未审读）：Marks Claude (web) and Claude Code as supporting the \[Skills over MCP\](https://modelcontextprotocol.io/extensions/skills/overview) extension ('io.modelcontextprotocol/skills') in the extension support matrix. Skills over MCP entered public beta in Claude and Claude Code on 2026-11-24: \[MCP servers can now ship skills, run tasks, and more with Claude\](https://claude.com/resources/articles/skills-over-mcp-tasks-and-mor

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Release/1.1.2](https://github.com/IBM/mcp-context-forge/pull/7659)

`IBM/mcp-context-forge` · **merged** · new · 分数 74 · 上游时间 2026-11-24T17:07:08Z

入选依据：T2 watchlist; security: security, oauth; protocol: protocol, transport; merged implementation; verify release separately。

> 上游摘录（未审读）：## \[1.1.2\] - MCP Subscriptions, A2A Agent Cards, AWS SigV4, and Security Hardening ### Overview Release 1.1.2 adds \*\*MCP subscriptions\*\*, \*\*A2A Agent Cards\*\*, \*\*AWS Signature V4 authentication\*\*, and \*\*Redis Cluster support\*\*. It also changes tool response filters to CEL and adds approval for virtual-server OAuth. This section covers \*\*78 PRs merged directly into 'main'\*\*. - \*\*Protocol & Transport\*\* - Modern MCP clie

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [auth: add ErrForbidden for valid tokens the resource must refuse](https://github.com/modelcontextprotocol/go-sdk/pull/1544)

`modelcontextprotocol/go-sdk` · **merged** · new · 分数 74 · 上游时间 2026-11-24T12:54:11Z

入选依据：T2 watchlist; security: oauth, authorization, token; protocol: protocol; merged implementation; verify release separately。

> 上游摘录（未审读）：Fixes #1543 'TokenVerifier' can currently signal an invalid token (401), an OAuth protocol error (400), or a verifier failure (500). A valid token that the resource server must refuse — for example one issued to a client the server does not serve — has no way to reach the 403 that the MCP authorization spec asks for. This adds 'auth.ErrForbidden': when a verifier error unwraps to it, 'RequireBearerToken' answers 403

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Grant pods/attach only for stdio transport](https://github.com/stacklok/toolhive/pull/6841)

`stacklok/toolhive` · **merged** · new · 分数 74 · 上游时间 2026-11-23T05:10:01Z

入选依据：T2 watchlist; security: security; protocol: transport, streamable, sse; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary The operator currently grants 'pods/attach' ('create', 'get') to every MCPServer proxy-runner Role. Only stdio transport needs this permission; 'streamable-http' and 'sse' communicate with the backend over the network. Unnecessary attach permissions can trigger security audit findings, as reported with Polaris. This change separates the attach rule from the shared RBAC rules and includes it only for stdio

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Pass the JWKS auth token path to vMCP](https://github.com/stacklok/toolhive/pull/7221)

`stacklok/toolhive` · **merged** · new · 分数 74 · 上游时间 2026-11-23T14:02:11Z

入选依据：T2 watchlist; security: token; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary - \*\*Why:\*\* A VirtualMCPServer whose 'incomingAuth.oidcConfigRef' points at an 'MCPOIDCConfig' of type 'kubernetesServiceAccount' rejects every caller with 401. The OIDC resolver sets the pod's service-account token path ('/var/run/secrets/kubernetes.io/serviceaccount/token') so OIDC discovery and JWKS requests can authenticate to the Kubernetes API server. The vMCP converter drops that path and the vMCP co

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Send KSA service account token only to the in-cluster API server](https://github.com/stacklok/toolhive/pull/7248)

`stacklok/toolhive` · **merged** · new · 分数 74 · 上游时间 2026-11-23T15:38:45Z

入选依据：T2 watchlist; security: token; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary For an 'MCPOIDCConfig' of type 'kubernetesServiceAccount', 'useClusterAuth' defaults to true. The workload's own service account token was then attached to every OIDC discovery, JWKS and introspection request, whatever host the 'issuer', 'jwksUrl' or 'introspectionUrl' named. The token was added so a workload could fetch JWKS from the Kubernetes API server, which needs authentication (#978). But the token

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Extract the shared JWT-bearer redemption tail](https://github.com/stacklok/toolhive/pull/7249)

`stacklok/toolhive` · **merged** · new · 分数 74 · 上游时间 2026-11-23T14:37:00Z

入选依据：T2 watchlist; security: audience, token; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary The plain RFC 7523 JWT-bearer handler and the ID-JAG handler each kept their own copy of the steps that run after their checks: consume the assertion, cap the token lifetime at the assertion's expiry, build the session, set the granted audience, and issue the token. On top of that, 'IDJAGHandler' held a whole '\*JWTBearerHandler' as 'core' and reached into its fields ('h.core.policies', 'h.core.consumer', '

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Keep token-file HTTP clients on same-host redirects](https://github.com/stacklok/toolhive/pull/7252)

`stacklok/toolhive` · **merged** · new · 分数 74 · 上游时间 2026-11-23T16:53:34Z

入选依据：T2 watchlist; security: oauth, authorization, token; protocol: transport, sse; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary - \*\*Why:\*\* when a token validator is configured with an auth token file ('--jwks-auth-token-file', 'jwksAuthTokenPath', or the service-account token used for 'kubernetesServiceAccount' MCPOIDCConfigs), 'HttpClientBuilder' attaches that token through 'oauth2.Transport'. The transport re-adds the 'Authorization' header on every round trip, including each redirect hop, so Go's built-in stripping of 'Authoriza

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Resolve ID-JAG subjects and issue marked tokens behind the gate](https://github.com/stacklok/toolhive/pull/7262)

`stacklok/toolhive` · **merged** · new · 分数 74 · 上游时间 2026-11-24T12:05:39Z

入选依据：T2 watchlist; security: authorization, token; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary When the gateway's authorization server redeems an ID-JAG, it can't say which of its own users the assertion is for. The token's 'sub' is always ' # ', so the gateway can't find the user's stored connections and no token can name a real user. This change makes redemption map the ID-JAG's 'upstream\_subject' to a local user and, when everything checks out, issue the delegated-access marker that lets the gate

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(auth): send DPoP proofs on token requests (SEP-1932)](https://github.com/modelcontextprotocol/rust-sdk/pull/1495)

`modelcontextprotocol/rust-sdk` · **open** · new · 分数 70 · 上游时间 2026-11-24T23:45:54Z

入选依据：T2 watchlist; security: authorization, token; protocol: transport; proposal: sep-; draft PR。

> 上游摘录（未审读）：Part of #1472. Stacked on #1494; please review only the last commit, "feat(auth): send DPoP proofs on token requests (SEP-1932)". Stack: 1. #1491: 'DPoP-Nonce' on 401 auth challenges 2. #1494: DPoP signer types 3. this PR: DPoP proofs on token requests 4. #1496: DPoP-bound tokens on MCP requests With a signer set by 'AuthorizationManager::set\_dpop\_signer', every token request carries a DPoP proof (RFC 9449 §5). This

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(auth): send DPoP-bound tokens on MCP requests (SEP-1932)](https://github.com/modelcontextprotocol/rust-sdk/pull/1496)

`modelcontextprotocol/rust-sdk` · **open** · new · 分数 70 · 上游时间 2026-11-24T23:45:56Z

入选依据：T2 watchlist; security: authorization, token; protocol: transport; proposal: sep-; draft PR。

> 上游摘录（未审读）：Part of #1472. Stacked on #1495; please review only the last commit, "feat(auth): send DPoP-bound tokens on MCP requests (SEP-1932)". Stack: 1. #1491: 'DPoP-Nonce' on 401 auth challenges 2. #1494: DPoP signer types 3. #1495: DPoP proofs on token requests 4. this PR: DPoP-bound tokens on MCP requests 'AuthClient' now sends a DPoP-bound access token as 'Authorization: DPoP' with a proof on every request (RFC 9449 §7).

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Prepare staging workload identities for usage jobs](https://github.com/modelcontextprotocol/registry/pull/1911)

`modelcontextprotocol/registry` · **merged** · new · 分数 68 · 上游时间 2026-11-23T13:51:53Z

入选依据：T1 watchlist; breaking: migration; merged implementation; verify release separately。

> 上游摘录（未审读）：Prepare staging for the usage credential migration from #1909. Enable the GKE workload pool and worker metadata server, and provision separate Kubernetes service accounts and IAM grants. Both scheduled jobs continue using their current credential during this phase. The worker update is planned for the staging maintenance window. Verify the refreshed preview, worker readiness, registry health, and both permission prob

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 发布与安全公告

显示 13 / 13 条；全部数据见当日 JSON。

### [mcp-server-fetch: IPv6 site-local fec0::/10 classified as public (SSRF guard classifier gap, CWE-918)](https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-3rxj-6jhw-qfv7)

`modelcontextprotocol/servers` · **published** · updated · 分数 117 · 上游时间 2026-11-24T21:55:15Z

入选依据：T2 watchlist; breaking: deprecat; security: ssrf; protocol: sse; advisory。

> 上游摘录（未审读）：### Summary \_is\_public\_address in mcp-server-fetch omits fec0::/10 (deprecated IPv6 site-local) and ::ffff:0:0/96 from its non-public list and falls back to ip.is\_global, which returns True for fec0::1. A fetch to http://\[fec0::1\]/ passes the SSRF guard. Low real-world reachability on default hosts; this is a classifier-correctness gap, not a proven metadata exploit. ### Details \*\*Server:\*\* fetch ('mcp-server-fetch',

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v0.69.0](https://github.com/stacklok/toolhive/releases/tag/v0.69.0)

`stacklok/toolhive` · **published** · new · 分数 89 · 上游时间 2026-11-24T23:15:08Z

入选依据：T2 watchlist; security: authorization, token; protocol: sse; release。

> 上游摘录（未审读）：## Behavior changes \*\*The embedded authorization server refuses tokens and assertions that carry 'authorization\_details'\*\* (\[#7282\](https://github.com/stacklok/toolhive/pull/7282)). Before, the claim was dropped and the request succeeded, so a token restricted by 'authorization\_details' could be exchanged for one without the restriction. Now these requests are refused: - RFC 8693 token exchange whose 'subject\_token'

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v1.3.0](https://github.com/cloudflare/workers-oauth-provider/releases/tag/v1.3.0)

`cloudflare/workers-oauth-provider` · **published** · new · 分数 81 · 上游时间 2026-11-23T15:37:30Z

入选依据：T1 watchlist; security: oauth; release。

> 上游摘录（未审读）：### Minor Changes - \[#426\](https://github.com/cloudflare/workers-oauth-provider/pull/426) \['dbd149a'\](https://github.com/cloudflare/workers-oauth-provider/commit/dbd149a21962f02d732dfa98ae7b2316a814d6ba) Thanks \[@mattzcarey\](https://github.com/mattzcarey)! - Client ID Metadata Document clients stay signed in while their document's host is down. The provider keeps the last validated copy of each document in 'OAUTH\_KV'

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [GitHub MCP Server 2.3.0](https://github.com/github/github-mcp-server/releases/tag/v2.3.0)

`github/github-mcp-server` · **published** · new · 分数 81 · 上游时间 2026-11-24T15:32:07Z

入选依据：T1 watchlist; security: security; release。

> 上游摘录（未审读）：## Highlights - Security product update tools - Swift added global security advisories - Lots of dependency upgrades ## What's Changed \* Remove thread\_resolution\_reason feature flag by @cagesellchen in https://github.com/github/github-mcp-server/pull/3727 \* Add experimental pull request artifact tools by @talum in https://github.com/github/github-mcp-server/pull/3843 \* Add Dependabot alert update tool by @belaltaher8

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v1.8.12](https://github.com/modelcontextprotocol/registry/releases/tag/v1.8.12)

`modelcontextprotocol/registry` · **published** · new · 分数 75 · 上游时间 2026-11-22T08:43:44Z

入选依据：T1 watchlist; protocol: protocol; release。

> 上游摘录（未审读）：## What's Changed \* Promote registry v1.8.11 to production and switch on the usage collector by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1886 \* Remove four dashboard panels that their neighbours already cover by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1887 \* Manage production's alert rules and Discord contact point from the repository by @rdimitrov in https://git

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v1.8.13](https://github.com/modelcontextprotocol/registry/releases/tag/v1.8.13)

`modelcontextprotocol/registry` · **published** · new · 分数 75 · 上游时间 2026-11-22T16:35:18Z

入选依据：T1 watchlist; protocol: protocol; release。

> 上游摘录（未审读）：## What's Changed \* Promote registry v1.8.12 to production and switch on the malware sweep by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1891 \* Describe the malware sweep as it now runs in production by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1892 \* Start every malware alert's email subject with the cluster's name by @rdimitrov in https://github.com/modelcontextpro

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v1.8.14](https://github.com/modelcontextprotocol/registry/releases/tag/v1.8.14)

`modelcontextprotocol/registry` · **published** · new · 分数 75 · 上游时间 2026-11-22T21:07:50Z

入选依据：T1 watchlist; protocol: protocol; release。

> 上游摘录（未审读）：## What's Changed \* Promote registry v1.8.13 to production by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1897 \* Run the staging malware sweep on demand by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1899 \* Fix moderation guidance, warning event counts, and idle-day collection by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1900 \*\*Full Changelog\*\*

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v1.8.15](https://github.com/modelcontextprotocol/registry/releases/tag/v1.8.15)

`modelcontextprotocol/registry` · **published** · new · 分数 75 · 上游时间 2026-11-22T22:06:14Z

入选依据：T1 watchlist; protocol: protocol; release。

> 上游摘录（未审读）：## What's Changed \* Use imageTag alone with the next production release by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1901 \* Confirm missing packages before sending sweep findings by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1902 \*\*Full Changelog\*\*: https://github.com/modelcontextprotocol/registry/compare/v1.8.14...v1.8.15

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v1.8.16](https://github.com/modelcontextprotocol/registry/releases/tag/v1.8.16)

`modelcontextprotocol/registry` · **published** · new · 分数 75 · 上游时间 2026-11-23T13:54:26Z

入选依据：T1 watchlist; protocol: protocol; release。

> 上游摘录（未审读）：## What's Changed \* Promote registry v1.8.15 to production by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1904 \* Reduce database work during edits and skip documentation-only staging deploys by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1908 \* Separate the usage collector and backup identities in stages by @rdimitrov in https://github.com/modelcontextprotocol/registry/

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [cli@0.51.0](https://github.com/getsentry/toolkit/releases/tag/cli%400.51.0)

`getsentry/toolkit` · **published** · new · 分数 69 · 上游时间 2026-11-24T18:14:26Z

入选依据：T2 watchlist; security: oauth; release。

> 上游摘录（未审读）：Developer workflows gain broader setup, chart, authentication, deployment, and issue handling, while fixes and tooling updates improve consistency and correctness. ### New Features ✨ CLI setup and detection, stable MCP charts, and OAuth hint forwarding expand developer workflows. #### CLI CLI handoffs can use device approval when a claim lacks a setup code, printing the approval URL and code before continuing setup.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Sensitive data redaction bypass in the troubleshooting tool in Amazon ECS MCP Server](https://github.com/awslabs/mcp/security/advisories/GHSA-ppc7-5jf2-gcfc)

`awslabs/mcp` · **published** · new · 分数 63 · 上游时间 2026-11-24T19:18:10Z

入选依据：T2 watchlist; protocol: protocol; advisory。

> 上游摘录（未审读）：### Summary Amazon ECS MCP Server is an open-source Model Context Protocol server that lets AI agents and assistants manage and troubleshoot Amazon ECS workloads using the operator's AWS credentials. An issue exists where, under certain circumstances, the troubleshooting tool of the Amazon ECS MCP Server returns cleartext container environment variable values and secret references from ECS task definitions even when

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [mcp-server-git: nested gitdir file bypasses --repository confinement](https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-w766-5x43-whvw)

`modelcontextprotocol/servers` · **published** · updated · 分数 63 · 上游时间 2026-11-24T21:54:02Z

入选依据：T2 watchlist; protocol: sse; advisory。

> 上游摘录（未审读）：# 'mcp-server-git': nested gitdir file bypasses '--repository' confinement \*\*Report date:\*\* 2026-10-27 \*\*Reporter:\*\* ShieldPi \*\*Affected package:\*\* 'mcp-server-git' \*\*Confirmed package version:\*\* 2026.10.19 \*\*Tested source commit:\*\* '82acf2aabf47bd462606a0d879e4849c26b2afae' ('v2/main') \*\*Also affected:\*\* 'ef9808f71090d0db3eda99e2af2ba78f1086f4fb' ('main'); the complete 'src/git/src/mcp\_server\_git/server.py' file has

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v0.68.0](https://github.com/stacklok/toolhive/releases/tag/v0.68.0)

`stacklok/toolhive` · **published** · new · 分数 63 · 上游时间 2026-11-23T14:22:10Z

入选依据：T2 watchlist; protocol: sse; release。

> 上游摘录（未审读）：## What's Changed \* Gate ID-JAG by issuer assertion types by @jhrozek in https://github.com/stacklok/toolhive/pull/6678 \* Log routine vMCP cache sync messages at debug by @FOWEPJF255 in https://github.com/stacklok/toolhive/pull/7216 \* Refuse unauthenticated ID-JAG clients and cnf-bound assertions by @jhrozek in https://github.com/stacklok/toolhive/pull/7214 \* Require the issuer as the only client assertion aud by @jh

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 协议 / 工作组提交

显示 7 / 7 条；全部数据见当日 JSON。

### [docs: fix small errors in the 2026-07-28 and draft specification (#3586)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/2bbace557bbf2cb5d03d6f9b48905415cd7607b0)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 77 · 上游时间 2026-11-24T21:51:25Z

入选依据：T1 watchlist; security: oauth, token; proposal: specification。

> 上游摘录（未审读）：docs: fix small errors in the 2026-07-28 and draft specification (#3586) Fixes items b to i of #3491 in the 2026-07-28 and draft versions. Item a was fixed in #3516, so this closes the issue. No requirement changes. Fixes #3491 - \*\*b)\*\* The "Client Features" card on the specification index links to the elicitation page. Its old target does not exist. - \*\*c)\*\* The "Refresh Tokens" reference uses 'draft-ietf-oauth-v2-1

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add VS Code to Skills extension column in client matrix (#3510)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/1c5f400671ba9ac6d558de907b815be4d2c37548)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 71 · 上游时间 2026-11-23T08:54:08Z

入选依据：T1 watchlist; protocol: protocol; proposal: extension。

> 上游摘录（未审读）：docs: add VS Code to Skills extension column in client matrix (#3510) Marks VS Code GitHub Copilot as supporting the \[Skills over MCP\](https://modelcontextprotocol.io/extensions/skills/overview) extension ('io.modelcontextprotocol/skills') in the extension support matrix. Support shipped in VS Code 1.147: \[Skills over MCP are now available in VS Code\](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/ski

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: mark Skills support for Claude and Claude Code in the extension matrix (#3588)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/3c8eb0c4e70b0b3af6471fc0cf3419c7098fdf39)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 71 · 上游时间 2026-11-24T21:48:36Z

入选依据：T1 watchlist; protocol: protocol; proposal: extension。

> 上游摘录（未审读）：docs: mark Skills support for Claude and Claude Code in the extension matrix (#3588) Marks Claude (web) and Claude Code as supporting the \[Skills over MCP\](https://modelcontextprotocol.io/extensions/skills/overview) extension ('io.modelcontextprotocol/skills') in the extension support matrix. Skills over MCP entered public beta in Claude and Claude Code on 2026-11-24: \[MCP servers can now ship skills, run tasks, and

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs(community): align IG charters with SEP sponsorship guidelines (#3531)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/b878313e34638206d13ddd9df57501567fac58fc)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 61 · 上游时间 2026-11-24T17:39:34Z

入选依据：T1 watchlist; security: authorization。

> 上游摘录（未审读）：docs(community): align IG charters with SEP sponsorship guidelines (#3531) \_Requested by \*\*David Soria Parra\*\* · \[Slack thread\](https://ant-mcp-oss.slack.com/archives/C0BDGKP4PC6/p1794253161846999)\_ \*\*Before:\*\* The Authorization IG charter said SEP sponsorship remains with Maintainers and Core Maintainers and that a proposer "finds a sponsor". The Financial Services IG charter said SEPs move toward the core specifica

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: fix small errors in the 2026-07-28 and draft docs (#3587)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/b7a22b5b15a5db59de002a08699091e0808b7784)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 51 · 上游时间 2026-11-24T21:47:46Z

入选依据：T1 watchlist; proposal: sep-。

> 上游摘录（未审读）：docs: fix small errors in the 2026-07-28 and draft docs (#3587) Fixes small errors found in a sweep of the docs, in the 2026-07-28 and draft versions. The changelog edits are in 2026-07-28 only. \*\*Please look at these:\*\* - Caching: the page now says that 'notifications/resources/updated' is the relevant notification for a cached 'resources/read' result. The existing rule only says "a relevant notification". SEP-2549

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs(blog): celebrate two years of MCP (#3584)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/50145009cb63c9363962408fcdb0758adcadc87b)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 35 · 上游时间 2026-11-24T17:43:14Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：docs(blog): celebrate two years of MCP (#3584) ## Summary Adds the blog post for the second anniversary of MCP, with an animated header, images, and a quote from Angie Jones. It looks back at the year through the people building on MCP and the community that shapes it. Merging publishes the post right away. This stays a draft until the author completes the contribution disclosure. ## Validation - Built the blog and c

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs(community): add Core Primitives WG charter (#3545)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/b0be8f0f2481be8d5ea5294cf3fa57cd03cedc48)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 35 · 上游时间 2026-11-23T15:22:02Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：docs(community): add Core Primitives WG charter (#3545) \_Requested by \*\*David Soria Parra\*\* · \[Slack thread\](https://ant-mcp-oss.slack.com/archives/C0BDGKP4PC6/p1793975038956449)\_ Follow-up to #3513. Follows #3544. \*\*Before:\*\* The Core Primitives WG has leads, a repository and a weekly meeting. It has no charter page, nav entry or Current groups line. \*\*After:\*\* The group has a charter built from the \[charter templat

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 文章与技术解释

显示 1 / 1 条；全部数据见当日 JSON。

### [Two Years of MCP Builders](https://blog.modelcontextprotocol.io/posts/mcp-turns-two/)

`mcp-official-blog` · **published** · new · 分数 50 · 上游时间 2026-11-24T09:00:00+00:00

入选依据：T1 watchlist; protocol: protocol。

> 上游摘录（未审读）：This week, our little open-source project, the Model Context Protocol (MCP), turns two years old . And what better way to mark this occasion than by celebrating the people who helped us build it and everyone building with it. When MCP first launched, we could not have imagined how creative and ambitious the community would get with it, or how many people would jump in to help make it become what it is today. Develope

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 博客选题工作台

从上面的重点项挑选，不自动把提案写成已实现功能：

- 协议问题：规范原文、提案状态、旧行为与新行为。
- 实现证据：PR diff、回归测试、客户端/服务端版本。
- 复现：最小实验、消息/HTTP trace、失败与成功条件。
- 结论边界：事实、维护者解释、个人判断分别记录。

模板：[知识库写作模板](https://github.com/xixiaxibro/mcp-knowledge-base/tree/main/templates)。
