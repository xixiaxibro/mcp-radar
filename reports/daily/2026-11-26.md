# MCP Radar · 2026-11-26 (UTC)

采集时间：2026-11-26T01:18:32+00:00 · 回看窗口：14 天。

这是公开来源的更新索引和选题素材，不是已经审读、复现的技术结论。标题和摘录来自上游；优先级由可见规则计算。

本次窗口内 884 条记录；本日累计 125 个新增/变更版本；失败端点 37 个；覆盖警告 0 个。

## 覆盖与限制

PR merged 表示代码进入分支，不代表已发布；release 不自动证明符合某协议版本。初次运行只建立窗口基线。

仅跟踪 watchlist 中公开仓库的 PR、指定仓库 issue/commit、release、公开安全公告和订阅源。未提供 API 的社区讨论、社交媒体和完整标准文档变更不在覆盖保证内。RSS 仅提供源当前保留的条目。

- 采集失败：`PrefectHQ/fastmcp` / source — Network error from api.github.com/repos/PrefectHQ/fastmcp
- 采集失败：`Tencent/AI-Infra-Guard` / source — Network error from api.github.com/repos/Tencent/AI-Infra-Guard
- 采集失败：`cloudflare/agents` / source — Network error from api.github.com/repos/cloudflare/agents
- 采集失败：`cloudflare/workers-oauth-provider` / source — Network error from api.github.com/repos/cloudflare/workers-oauth-provider
- 采集失败：`cloudflare/workers-sdk` / source — Network error from api.github.com/repos/cloudflare/workers-sdk
- 采集失败：`modelcontextprotocol/agents-wg` / source — Network error from api.github.com/repos/modelcontextprotocol/agents-wg
- 采集失败：`modelcontextprotocol/conformance` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/csharp-sdk` / source — Network error from api.github.com/repos/modelcontextprotocol/csharp-sdk
- 采集失败：`modelcontextprotocol/ext-apps` / source — The read operation timed out
- 采集失败：`modelcontextprotocol/ext-auth` / commits — Network error from api.github.com/repos/modelcontextprotocol/ext-auth/commits
- 采集失败：`modelcontextprotocol/ext-auth` / issues — Network error from api.github.com/repos/modelcontextprotocol/ext-auth/issues
- 采集失败：`modelcontextprotocol/ext-auth` / pulls — Network error from api.github.com/repos/modelcontextprotocol/ext-auth/pulls
- 采集失败：`modelcontextprotocol/ext-auth` / releases — Network error from api.github.com/repos/modelcontextprotocol/ext-auth/releases
- 采集失败：`modelcontextprotocol/ext-auth` / security-advisories — Network error from api.github.com/repos/modelcontextprotocol/ext-auth/security-advisories
- 采集失败：`modelcontextprotocol/ext-skills` / source — Network error from api.github.com/repos/modelcontextprotocol/ext-skills
- 采集失败：`modelcontextprotocol/ext-tasks` / source — Network error from api.github.com/repos/modelcontextprotocol/ext-tasks
- 采集失败：`modelcontextprotocol/go-sdk` / source — Network error from api.github.com/repos/modelcontextprotocol/go-sdk
- 采集失败：`modelcontextprotocol/inspector` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/java-sdk` / source — Network error from api.github.com/repos/modelcontextprotocol/java-sdk
- 采集失败：`modelcontextprotocol/kotlin-sdk` / source — Network error from api.github.com/repos/modelcontextprotocol/kotlin-sdk
- 采集失败：`modelcontextprotocol/mcpb` / source — Network error from api.github.com/repos/modelcontextprotocol/mcpb
- 采集失败：`modelcontextprotocol/modelcontextprotocol` / commits — Network error from api.github.com/repos/modelcontextprotocol/modelcontextprotocol/commits
- 采集失败：`modelcontextprotocol/modelcontextprotocol` / issues — Network error from api.github.com/repos/modelcontextprotocol/modelcontextprotocol/issues
- 采集失败：`modelcontextprotocol/modelcontextprotocol` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/modelcontextprotocol` / releases — Network error from api.github.com/repos/modelcontextprotocol/modelcontextprotocol/releases
- 采集失败：`modelcontextprotocol/modelcontextprotocol` / security-advisories — Network error from api.github.com/repos/modelcontextprotocol/modelcontextprotocol/security-advisories
- 采集失败：`modelcontextprotocol/php-sdk` / source — Network error from api.github.com/repos/modelcontextprotocol/php-sdk
- 采集失败：`modelcontextprotocol/python-sdk` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/registry` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/ruby-sdk` / source — Network error from api.github.com/repos/modelcontextprotocol/ruby-sdk
- 采集失败：`modelcontextprotocol/rust-sdk` / source — Network error from api.github.com/repos/modelcontextprotocol/rust-sdk
- 采集失败：`modelcontextprotocol/servers` / source — Network error from api.github.com/repos/modelcontextprotocol/servers
- 采集失败：`modelcontextprotocol/swift-sdk` / source — Network error from api.github.com/repos/modelcontextprotocol/swift-sdk
- 采集失败：`modelcontextprotocol/transports-wg` / commits — Network error from api.github.com/repos/modelcontextprotocol/transports-wg/commits
- 采集失败：`modelcontextprotocol/transports-wg` / issues — The read operation timed out
- 采集失败：`modelcontextprotocol/typescript-sdk` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/typescript-sdk` / releases — The read operation timed out

## 重点 PR / 提案

显示 20 / 122 条；全部数据见当日 JSON。

### [fix: accept the swift ecosystem in list\_global\_security\_advisories](https://github.com/github/github-mcp-server/pull/3937)

`github/github-mcp-server` · **merged** · new · 分数 86 · 上游时间 2026-11-24T15:17:25Z

入选依据：T1 watchlist; security: security; protocol: schema; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary 'list\_global\_security\_advisories' now accepts 'ecosystem: "swift"'. The GitHub Advisory Database has a Swift ecosystem and the REST API accepts it, but the tool's enum left it out, so every Swift request was rejected by schema validation before reaching the API. ## Why The ecosystem enum lists 12 values ending at 'rust'. The REST endpoint's own error message lists 13: 'rubygems, npm, pip, maven, nuget, com

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(mcp-cloudflare): Drop an unnecessary non-null assertion in the CIMD test](https://github.com/getsentry/toolkit/pull/2499)

`getsentry/toolkit` · **merged** · new · 分数 74 · 上游时间 2026-11-25T12:59:36Z

入选依据：T2 watchlist; security: oauth; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：The 'Test' workflow has failed on 'main' since #2283. Its "Repository quality" job fails at 'pnpm run lint': ''' packages/mcp-cloudflare/src/server/oauth/client-metadata-failure.integration.test.ts:33:10: This assertion is unnecessary since it does not change the type of the expression. ''' 'handler.fetch' is already typed as defined, so 'handler.fetch!(…)' trips 'typescript(no-unnecessary-type-assertion)'. The PR's

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Let Cedar read user claims the upstream asserts only in its ID token](https://github.com/stacklok/toolhive/pull/6054)

`stacklok/toolhive` · **merged** · updated · 分数 74 · 上游时间 2026-11-25T19:22:16Z

入选依据：T2 watchlist; security: token; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary Cedar read group and role claims from the pinned upstream's \*\*access token\*\* only, so a provider that asserts group membership in its 'id\_token' produced an empty group set and every 'principal in THVGroup::"..."' policy denied for every user, with no diagnostic beyond the 'has' guard failing. Same shape as #5916 — a claim the upstream does assert, in a token ToolHive already holds, that the authorizer nev

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat: authenticate scan backend calls with a machine token](https://github.com/snyk/agent-scan/pull/558)

`snyk/agent-scan` · **merged** · updated · 分数 66 · 上游时间 2026-11-25T14:47:07Z

入选依据：T1 watchlist; security: token; merged implementation; verify release separately。

> 上游摘录（未审读）：## What 'scan' can now authenticate to the backend with a machine identity instead of a push key. The ADS installer sets it up with two values in 'scan-agent-config.yaml' (snyk/ads-distribution-service#651, #655): - 'token\_command': the absolute path of the installer command that prints a bearer token - 'tenant\_id': the tenant the scan reports to Set both to use a machine identity. With only one set, the scan warns a

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(postgres-mcp-server): accept username-only secret for PG\_WIRE\_IAM\_PROTOCOL](https://github.com/awslabs/mcp/pull/4829)

`awslabs/mcp` · **open** · updated · 分数 64 · 上游时间 2026-11-25T20:04:11Z

入选依据：T2 watchlist; security: token; protocol: protocol。

> 上游摘录（未审读）：Fixes #4824 ## Summary ### Changes With '--connection\_method PG\_WIRE\_IAM\_PROTOCOL', the password is a generated IAM auth token, so the '--secret\_arn' secret only needs a 'username'. Both IAM code paths, however, read the secret through 'get\_credentials\_from\_secret()', which raises when there is no 'password' key. - 'connection/psycopg\_pool\_connection.py': the secret parsing moves into a private '\_read\_credentials\_fro

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(ecs-mcp-server): honor end\_time and paginate stopped tasks in fetch\_task\_failures](https://github.com/awslabs/mcp/pull/5177)

`awslabs/mcp` · **open** · new · 分数 64 · 上游时间 2026-11-25T04:06:26Z

入选依据：T2 watchlist; security: token; protocol: sse。

> 上游摘录（未审读）：## Summary ### Changes 'fetch\_task\_failures' accepts 'end\_time' and computes 'actual\_end\_time', but the value was never used, so tasks stopped after the requested window were still returned. The helper also called 'ListTasks' once (max 100 ARNs per page, 'nextToken' ignored) and passed every ARN to a single 'DescribeTasks' call (limit 100), so clusters with many stopped tasks were silently truncated or hit a validati

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Filter SSE list answers on the event stream](https://github.com/stacklok/toolhive/pull/6949)

`stacklok/toolhive` · **open** · updated · 分数 64 · 上游时间 2026-11-25T23:21:15Z

入选依据：T2 watchlist; security: authorization; protocol: streamable, sse。

> 上游摘录（未审读）：Fixes #6926. ## Summary \*\*Why:\*\* Over SSE, list answers (tools, prompts, resources, resource templates, skills) reached the client on the GET event stream, which was not filtered. \*\*What:\*\* Each GET event is now filtered as it arrives, with the same per-entry authorization as the streamable path. The filter is picked from the shape of each result. ## Does this introduce a user-facing change? - \*\*SSE list answers.\*\* B

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Add per-client vMCP scope challenge responses](https://github.com/stacklok/toolhive/pull/7190)

`stacklok/toolhive` · **open** · updated · 分数 64 · 上游时间 2026-11-25T11:20:10Z

入选依据：T2 watchlist; security: oauth, authorization; protocol: transport。

> 上游摘录（未审读）：## Summary Clients use different signals to request additional OAuth consent. Add transport support for the scope policy merged in #7170 so they can share one vMCP gateway URL while authorization stays in the core. - Default to HTTP 403 with an 'insufficient\_scope' challenge containing the full required scopes and gateway resource metadata. - Support forced 'tool-result' and opt-in 'auto': exact configured client nam

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Make secondary chain legs optionally non-fatal](https://github.com/stacklok/toolhive/pull/7311)

`stacklok/toolhive` · **open** · new · 分数 64 · 上游时间 2026-11-25T21:28:31Z

入选依据：T2 watchlist; security: authorization; protocol: cancel。

> 上游摘录（未审读）：## Summary - Today any failed leg of a multi-upstream chain ends the whole authorization. A user who cancels a secondary provider's consent screen, or hits a secondary provider outage, gets no authorization code and loses every upstream, the identity provider included. Embedders that already present a missing upstream in-band (for example a connect link in a tool-call response) can complete the authorization without

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Add list\_code\_quality\_findings tool to code\_quality toolset](https://github.com/github/github-mcp-server/pull/3564)

`github/github-mcp-server` · **merged** · updated · 分数 60 · 上游时间 2026-11-25T15:04:33Z

入选依据：T1 watchlist; protocol: pagination; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary Adds a read-only 'list\_code\_quality\_findings' tool to the 'code\_quality' toolset. It lists a repository's code quality findings through 'GET /repos/{owner}/{repo}/code-quality/findings' and supports the 'state' and 'direction' filters plus cursor pagination. ## Why Closes #3560 ## What changed - Added 'ListCodeQualityFindings' in 'pkg/github/code\_quality.go', modelled on 'list\_dependabot\_alerts': - Uses 'W

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add go install as a first-class local install method](https://github.com/github/github-mcp-server/pull/3745)

`github/github-mcp-server` · **open** · updated · 分数 56 · 上游时间 2026-11-25T10:04:44Z

入选依据：T1 watchlist; security: oauth。

> 上游摘录（未审读）：## Summary - Documents 'go install github.com/github/github-mcp-server/v2/cmd/github-mcp-server@latest' as a first-class way to run the local server without Docker. - Keeps 'go build' from a checkout for contributors who need embedded VCS metadata. - Points to the native-binary OAuth flow. Fixes #2364 ## Notes The issue suggested 'github.com/github/github-mcp-server/cmd/...@latest'. That resolves to the pre-v2 module

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Fail closed when the token scope fetch errors](https://github.com/github/github-mcp-server/pull/3932)

`github/github-mcp-server` · **open** · new · 分数 56 · 上游时间 2026-11-24T15:16:23Z

入选依据：T1 watchlist; security: oauth, token。

> 上游摘录（未审读）：Fixes #3929 ## Problem When the token scope fetch returns an error, two code paths fail open: - 'WithScopeChallenge' forwarded OAuth 'tools/call' requests to the next handler without the '403 insufficient\_scope' challenge. - 'PATScopeFilter' returned the unfiltered tool inventory, exposing scope-gated tools to a classic PAT whose scopes could not be verified. ## Root cause Both error branches called the success path

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Stop the DCR recheck tests racing their loop](https://github.com/stacklok/toolhive/pull/7172)

`stacklok/toolhive` · **merged** · updated · 分数 54 · 上游时间 2026-11-25T16:45:16Z

入选依据：T2 watchlist; security: token; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary 'TestEmbeddedAuthServer\_DCRRecheckFollowsMovedTokenEndpoint' failed once in CI with a data race and 'expected: \["iat-1","iat-2"\] actual: \["iat-1","iat-1"\]'. The test builds an embedded auth server with 'RegistrationProbeInterval: "1m"', which also starts the background re-check loop. The loop's first tick fires at a random point in the first minute, and the test calls 'tick' by hand as well. When the loop'

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Keep one user per upstream identity](https://github.com/stacklok/toolhive/pull/7277)

`stacklok/toolhive` · **merged** · updated · 分数 54 · 上游时间 2026-11-25T09:29:34Z

入选依据：T2 watchlist; security: authorization; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary Clients compare a user's 'sub\_id' to decide who owns a session, and the agent check compares it with a grant's user. Both assume one upstream identity never maps to two authorization-server users. The code mostly guaranteed this, but nothing tested it, and three gaps could still break it: a Redis link write that was not atomic with its reverse index, a failed link write that could roll back the user that o

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Add the MCP tool-call details type](https://github.com/stacklok/toolhive/pull/7283)

`stacklok/toolhive` · **merged** · updated · 分数 54 · 上游时间 2026-11-25T08:39:02Z

入选依据：T2 watchlist; security: authorization, token; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary - \*\*Why:\*\* a client that redeems an ID-JAG at the gateway's authorization server gets an access token that is good for any call until it expires. To narrow that token to the one MCP call an authorizer approved ("Authorization server: narrow a JWT-bearer access token to one MCP call with authorization\_details" (#7061)), the authorization server and the vMCP need a shared 'authorization\_details' type that de

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Add a per-client access token lifespan for ID-JAG redemption](https://github.com/stacklok/toolhive/pull/7284)

`stacklok/toolhive` · **merged** · updated · 分数 54 · 上游时间 2026-11-25T08:38:14Z

入选依据：T2 watchlist; security: authorization, token; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary A client that redeems ID-JAGs to make one MCP call wants a token that lives for seconds, while every other client keeps the server's access-token lifespan. Today there is one lifespan for the whole server, so a narrow per-call token lives as long as any other token. "Authorization server: narrow a JWT-bearer access token to one MCP call with authorization\_details" (#7061) asks for a per-client lifetime. Th

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Record how a token was admitted on Identity](https://github.com/stacklok/toolhive/pull/7287)

`stacklok/toolhive` · **merged** · updated · 分数 54 · 上游时间 2026-11-25T10:39:42Z

入选依据：T2 watchlist; security: token; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary A delegated token (an access token from ID-JAG redemption that names a real user) has no 'tsid', so the vMCP has no way to tell it apart from any other session-less token, and nothing downstream can decide to read that user's stored credential for it. Part C of "Ownership-checked credential read for delegated tokens, keyed by user and routed provider" (#6407), session binding in "vMCP: bind sessions to the

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Process the ID-JAG authorization\_details claim](https://github.com/stacklok/toolhive/pull/7290)

`stacklok/toolhive` · **merged** · updated · 分数 54 · 上游时间 2026-11-25T13:33:39Z

入选依据：T2 watchlist; security: authorization; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary \*\*Review commit by commit.\*\* The PR is above the usual size, so it is split into two commits: "Keep the raw authorization\_details bytes" (about 60 non-test lines, no behaviour change: the validator keeps the claim's raw bytes so integer precision survives) and "Process the ID-JAG authorization\_details claim" (the processing, refusals, wiring and docs). After those: a merge of main (the per-client lifespan

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Accept a trailing slash on an origin-only DCR issuer](https://github.com/stacklok/toolhive/pull/7292)

`stacklok/toolhive` · **merged** · updated · 分数 54 · 上游时间 2026-11-25T12:51:28Z

入选依据：T2 watchlist; security: oauth; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary - A DCR upstream configured with 'dcrConfig.discoveryUrl' could not register against servers built on FastMCP's OAuth proxy. Those servers publish '"issuer": "https://host.example.com/"' for a root deployment, while ToolHive derives 'https://host.example.com' from the discovery URL and compared the two byte for byte. Registration failed with 'issuer mismatch (RFC 8414 §3.3)'. - 'fetchDiscoveryDocument' now

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Add README for pkg/authserver](https://github.com/stacklok/toolhive/pull/7301)

`stacklok/toolhive` · **merged** · new · 分数 54 · 上游时间 2026-11-25T16:26:00Z

入选依据：T2 watchlist; security: oauth, authorization; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary Embedders of 'pkg/authserver' currently have to read the code to learn what the package offers, how to mount it, and where the architecture docs live. This adds a README that serves as the single entry point for prospective adopters. - Describes 'pkg/authserver' as an embeddable Go OAuth 2.0 authorization server built on Ory Fosite, with no MCP or ToolHive proxy dependency. - Covers the supported grants an

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 发布与安全公告

显示 3 / 3 条；全部数据见当日 JSON。

### [v1.1.2 - Release 2026-11-25 - MCP Subscriptions, A2A Agent Cards, AWS SigV4, and Security Hardening](https://github.com/IBM/mcp-context-forge/releases/tag/v1.1.2)

`IBM/mcp-context-forge` · **published** · new · 分数 89 · 上游时间 2026-11-25T09:38:04Z

入选依据：T2 watchlist; security: security, oauth; protocol: protocol, transport; release。

> 上游摘录（未审读）：## \[1.1.2\] - MCP Subscriptions, A2A Agent Cards, AWS SigV4, and Security Hardening ### Overview Release 1.1.2 adds \*\*MCP subscriptions\*\*, \*\*A2A Agent Cards\*\*, \*\*AWS Signature V4 authentication\*\*, and \*\*Redis Cluster support\*\*. It also changes tool response filters to CEL and adds approval for virtual-server OAuth. This section covers \*\*78 PRs merged directly into 'main'\*\*. - \*\*Protocol & Transport\*\* - Modern MCP clie

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [MCPOIDCConfig kubernetesServiceAccount does not restrict which service accounts can authenticate](https://github.com/stacklok/toolhive/security/advisories/GHSA-q656-jppg-j2qr)

`stacklok/toolhive` · **published** · new · 分数 89 · 上游时间 2026-11-23T14:07:57Z

入选依据：T2 watchlist; security: audience, token; protocol: sse; advisory。

> 上游摘录（未审读）：### Summary In the ToolHive Kubernetes operator, an 'MCPOIDCConfig' of type 'kubernetesServiceAccount' has 'serviceAccount' and 'namespace' fields. They were documented as selecting whose service-account tokens a workload accepts, but they were never enforced. The operator dropped both fields when it built the runtime OIDC configuration, and the token validator checked only signature, issuer, audience and expiry. Kub

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v0.69.1](https://github.com/stacklok/toolhive/releases/tag/v0.69.1)

`stacklok/toolhive` · **published** · new · 分数 69 · 上游时间 2026-11-25T15:26:44Z

入选依据：T2 watchlist; security: token; release。

> 上游摘录（未审读）：## What's Changed \* Document the code mode split behind the vMCP optimizer by @rdimitrov in https://github.com/stacklok/toolhive/pull/7294 \* Add a per-client access token lifespan for ID-JAG redemption by @rdimitrov in https://github.com/stacklok/toolhive/pull/7284 \* Add the MCP tool-call details type by @rdimitrov in https://github.com/stacklok/toolhive/pull/7283 \* Keep one user per upstream identity by @jhrozek in

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

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
