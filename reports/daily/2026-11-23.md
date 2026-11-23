# MCP Radar · 2026-11-23 (UTC)

采集时间：2026-11-23T01:17:23+00:00 · 回看窗口：14 天。

这是公开来源的更新索引和选题素材，不是已经审读、复现的技术结论。标题和摘录来自上游；优先级由可见规则计算。

本次窗口内 2333 条记录；本日累计 167 个新增/变更版本；失败端点 4 个；覆盖警告 1 个。

## 覆盖与限制

PR merged 表示代码进入分支，不代表已发布；release 不自动证明符合某协议版本。初次运行只建立窗口基线。

仅跟踪 watchlist 中公开仓库的 PR、指定仓库 issue/commit、release、公开安全公告和订阅源。未提供 API 的社区讨论、社交媒体和完整标准文档变更不在覆盖保证内。RSS 仅提供源当前保留的条目。

- 采集失败：`cloudflare/agents` / releases — Unterminated string starting at: line 1 column 543522 (char 543521)
- 采集失败：`modelcontextprotocol/ext-skills` / pulls — Unterminated string starting at: line 1 column 1135648 (char 1135647)
- 采集失败：`modelcontextprotocol/registry` / releases — Unterminated string starting at: line 1 column 2625828 (char 2625827)
- 采集失败：`modelcontextprotocol/rust-sdk` / security-advisories — Remote end closed connection without response
- 覆盖提示：`modelcontextprotocol/agents-wg` / source — Repository renamed/redirected to modelcontextprotocol/agents-ig

## 重点 PR / 提案

显示 20 / 167 条；全部数据见当日 JSON。

### [fix: enforce valid\_scopes for CIMD clients](https://github.com/PrefectHQ/fastmcp/pull/5829)

`PrefectHQ/fastmcp` · **merged** · new · 分数 86 · 上游时间 2026-11-22T19:10:51Z

入选依据：T1 watchlist; security: security, oauth; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #5828 ## Description CIMD clients could bypass the OAuth proxy's scope policy. 'CIMDClientManager' built the synthetic 'ProxyDCRClient' with 'scope=cimd\_doc.scope or self.default\_scope', taking the scope verbatim from the client-hosted metadata document. 'OAuthProxy' never passed its 'valid\_scopes' allowlist to the manager, so a document declaring 'scope="admin"' passed the SDK's 'client.validate\_scope()' gate

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Resolve JSON Schema references through arrays](https://github.com/PrefectHQ/fastmcp/pull/6098)

`PrefectHQ/fastmcp` · **merged** · updated · 分数 86 · 上游时间 2026-11-22T19:11:43Z

入选依据：T1 watchlist; security: token; protocol: schema; merged implementation; verify release separately。

> 上游摘录（未审读）：When schema dereferencing is disabled, a tool can return valid structured content while the client leaves 'result.data' as 'None'. A reference such as '#/properties/template/anyOf/0' reaches an array, but the resolver calls '.get()' on it instead of selecting an element. Resolve array tokens as RFC 6901 indices so the referenced schema can hydrate the result, including values such as 'datetime.date'. Dictionary keys

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Move Think's action tools into action-tools.ts](https://github.com/cloudflare/agents/pull/2983)

`cloudflare/agents` · **merged** · new · 分数 86 · 上游时间 2026-11-22T20:57:42Z

入选依据：T1 watchlist; security: authorization; protocol: timeout; merged implementation; verify release separately。

> 上游摘录（未审读）：The action tools move out of 'think.ts' into 'action-tools.ts': 'compileActionTools' turns 'getActions()' into the turn's tools, with authorization through 'authorizeAction', the approval gate, the timeout and abort race, and the hand-off to the action ledger or a durable pause. The output and abort helpers ('prepareActionOutputForModel', 'safeStringifyActionOutput', 'createActionAbortSignal', the error envelopes) mo

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(core): reject a request sent while not connected with SdkError NotConnected](https://github.com/modelcontextprotocol/typescript-sdk/pull/3225)

`modelcontextprotocol/typescript-sdk` · **open** · new · 分数 78 · 上游时间 2026-11-22T22:24:52Z

入选依据：T1 watchlist; breaking: migration; protocol: transport。

> 上游摘录（未审读）：A request sent while the instance has no transport (before 'connect()', or after 'close()') rejects with a plain 'Error('Not connected')'. The v2 upgrade guide says this case is 'SdkError' with 'SdkErrorCode.NotConnected': > \| Not connected \| 'new Error('Not connected')' \| 'SdkError' + 'SdkErrorCode.NotConnected' \| ('skills/mcp-typescript-sdk-upgrade-to-v2/references/errors.md', rendered into 'docs/migration/upgrade-

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Gggg](https://github.com/github/github-mcp-server/pull/3922)

`github/github-mcp-server` · **closed** · new · 分数 76 · 上游时间 2026-11-22T10:04:43Z

入选依据：T1 watchlist; security: security, token; protocol: schema。

> 上游摘录（未审读）：## Summary ## Why Fixes # ## What changed - - ## MCP impact - \[ \] No tool or API changes - \[x\] Tool schema or behavior changed - \[x\] New tool added ## Prompts tested (tool changes only) - ## Security / limits - \[ \] No security or limits impact - \[x\] Auth / permissions considered - \[x\] Data exposure, filtering, or token/size limits considered ## Tool renaming - \[ \] I am renaming tools as part of this PR (e.g. a part o

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(server/auth): add server-side token audience validation scenario (#78)](https://github.com/modelcontextprotocol/conformance/pull/597)

`modelcontextprotocol/conformance` · **open** · new · 分数 76 · 上游时间 2026-11-22T11:16:44Z

入选依据：T1 watchlist; security: oauth, audience, token; protocol: conformance。

> 上游摘录（未审读）：Closes #78 ## Summary Adds the server-side 'auth/token-audience-validation' conformance scenario ('source: { introducedIn: '2025-06-18' }') to verify that an MCP server acting as an OAuth 2.1 resource server validates presented access tokens against its own intended audience (RFC 8707) and expiration time. A scope note: #78 is open and unassigned with no active PR (closed draft #386 was not merged). This PR stays str

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Require the issuer as the only client assertion aud](https://github.com/stacklok/toolhive/pull/7213)

`stacklok/toolhive` · **merged** · new · 分数 74 · 上游时间 2026-11-22T20:16:33Z

入选依据：T2 watchlist; security: audience, token, injection; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary A 'private\_key\_jwt' client assertion was accepted when its 'aud' was the token endpoint URL, or an array that merely contained the issuer, because fosite only checks that one accepted value is among the 'aud' values. RFC 10070 section 4 closes the audience injection attack (Hosseyni, Küsters and Würtele) by requiring the issuer identifier as the sole 'aud' value and forbidding the token endpoint URL. The i

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Refuse unauthenticated ID-JAG clients and cnf-bound assertions](https://github.com/stacklok/toolhive/pull/7214)

`stacklok/toolhive` · **merged** · new · 分数 74 · 上游时间 2026-11-22T20:16:04Z

入选依据：T2 watchlist; security: oauth; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary ID-JAG redemption at the embedded auth server departed from draft-ietf-oauth-identity-assertion-authz-grant-06 in two places, and both made a leaked ID-JAG a full bearer credential: - \*\*Public clients could redeem.\*\* Draft §4.4 says the server MUST reject a request that has neither client authentication nor a sender-constrained ID-JAG, with 'invalid\_client'. The handler accepted a public client identified

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Agent-tool runs keep their own table and jobs (internal refactor)](https://github.com/cloudflare/agents/pull/2957)

`cloudflare/agents` · **closed** · new · 分数 68 · 上游时间 2026-11-23T00:21:50Z

入选依据：T1 watchlist; breaking: migration; protocol: schema, lifecycle, capabilit; draft PR。

> 上游摘录（未审读）：Parked: waits for the facet lane The parent side of agent-tool runs moves out of 'Agent' into 'AgentRuns' ('packages/agents/src/agent-runs/agent-runs.ts'), an internal Lifecycle capability. It owns 'cf\_agent\_tool\_runs' and its migrations under its own schema key, runs startup recovery as a job once startup has finished, keeps the detached backbone as a job instead of a schedule row, and forwards 'agent-tool-runs/{run

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Fix TokenCache handling for expired access tokens](https://github.com/PrefectHQ/fastmcp/pull/5195)

`PrefectHQ/fastmcp` · **merged** · updated · 分数 66 · 上游时间 2026-11-22T19:10:21Z

入选依据：T1 watchlist; security: token; merged implementation; verify release separately。

> 上游摘录（未审读）：## Description Fixes #5193. 'TokenCache.set()' now treats 'expires\_at=0' as an explicit token expiry instead of falling back to the cache TTL. If the effective expiry is already in the past, the cache removes any existing entry for that token and returns a miss on later reads. ## Contribution type - \[x\] Bug fix (simple, well-scoped fix for a clearly broken behavior) - \[ \] Documentation improvement - \[ \] Enhancement (

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Skip issuer validation in AzureProvider for multi-tenant authorities](https://github.com/PrefectHQ/fastmcp/pull/5694)

`PrefectHQ/fastmcp` · **merged** · updated · 分数 66 · 上游时间 2026-11-22T19:10:29Z

入选依据：T1 watchlist; security: token; merged implementation; verify release separately。

> 上游摘录（未审读）：'AzureProvider' built its token verifier with the issuer 'https://{base\_authority}/{tenant\_id}/v2.0' for every 'tenant\_id'. For the multi-tenant authorities 'organizations', 'consumers' and 'common', Entra puts the signing-in user's tenant GUID in 'iss', so the literal authority name never matches and every token was rejected with an issuer mismatch. 'AzureJWTVerifier' already skips issuer validation for these values

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(auth): render the registration and discovery endpoints on the unregistered-client page](https://github.com/PrefectHQ/fastmcp/pull/5745)

`PrefectHQ/fastmcp` · **merged** · updated · 分数 66 · 上游时间 2026-11-22T19:10:37Z

入选依据：T1 watchlist; security: authorization; merged implementation; verify release separately。

> 上游摘录（未审读）：Fixes #5744 ## Description 'AuthorizationHandler.\_create\_enhanced\_error\_response()' computes a registration endpoint and an authorization-server metadata (discovery) endpoint and hands both to 'create\_unregistered\_client\_html()' for the 'Accept: text/html' branch of the enhanced 400 response. That function documented both parameters and never used either, so the HTML page dropped them. The other two representations o

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(auth): reject malformed URL ports as SSRFError in validate\_url](https://github.com/PrefectHQ/fastmcp/pull/5773)

`PrefectHQ/fastmcp` · **merged** · new · 分数 66 · 上游时间 2026-11-22T19:10:44Z

入选依据：T1 watchlist; security: oauth, ssrf; merged implementation; verify release separately。

> 上游摘录（未审读）：An unauthenticated OAuth request whose 'client\_id' URL carries a malformed port ('https://example.com:70000/…' or ':abc') blew up with HTTP 500 instead of the clean invalid-client rejection every other bad 'client\_id' gets. 'validate\_url' guarded 'urlparse()' against 'ValueError' but read 'parsed.port' outside that guard, so urllib's 'ValueError: Port out of range 0-65535' escaped as a bare exception past the SSRFErr

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Match the query component when validating redirect URIs against allowed patterns](https://github.com/PrefectHQ/fastmcp/pull/6000)

`PrefectHQ/fastmcp` · **merged** · updated · 分数 66 · 上游时间 2026-11-22T19:11:27Z

入选依据：T1 watchlist; security: security; merged implementation; verify release separately。

> 上游摘录（未审读）：'matches\_allowed\_pattern' compared the scheme, host, port, and path of a redirect URI against each allowed pattern, but never looked at the query — so a registered pattern of 'https://app.example.com/cb' also accepted 'https://app.example.com/cb?code\_to=attacker'. RFC 6749 §3.1.2 makes the query part of the registered redirect URI that has to match, so the validator now compares the query component byte-for-byte — wi

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Clarify whether notifications/resources/list\_changed should be sent if the list of resource templates changes](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/3226)

`modelcontextprotocol/modelcontextprotocol` · **open** · new · 分数 66 · 上游时间 2026-11-22T11:45:49Z

入选依据：T1 watchlist; protocol: protocol; proposal: specification。

> 上游摘录（未审读）：### What's broken? The spec is ambiguous or self-contradictory ### Where in the spec or docs? https://modelcontextprotocol.io/specification/2026-07-28/server/resources#list-changed-notification ### What should happen? The spec should explicitly define what a client/server should do about resource template list changes. ### What actually happens? The spec is ambiguous - it doesn't explicitly say what a client/server s

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add VS Code to Skills extension column in client matrix](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3510)

`modelcontextprotocol/modelcontextprotocol` · **open** · updated · 分数 66 · 上游时间 2026-11-22T20:20:12Z

入选依据：T1 watchlist; protocol: protocol; proposal: extension。

> 上游摘录（未审读）：Marks VS Code GitHub Copilot as supporting the \[Skills over MCP\](https://modelcontextprotocol.io/extensions/skills/overview) extension ('io.modelcontextprotocol/skills') in the extension support matrix. Support shipped in VS Code 1.147: \[Skills over MCP are now available in VS Code\](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/skills-over-mcp-are-now-available-in-vs-code/4574580). The 'chat.agentHos

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat: authenticate scan backend calls with a machine token](https://github.com/snyk/agent-scan/pull/558)

`snyk/agent-scan` · **open** · new · 分数 66 · 上游时间 2026-11-22T14:46:28Z

入选依据：T1 watchlist; security: token; protocol: sse; draft PR。

> 上游摘录（未审读）：## Summary The ADS installer now passes Agent Scan either a machine identity ('token\_command', 'tenant\_id', 'base\_url' in 'scan-agent-config.yaml') or a push key, never both (snyk/ads-distribution-service#651, #655). This PR teaches 'scan' the machine identity mode, using the Cerberus tenant routes from snyk/invariant-mcp-scan-backend#842. '''text --token-command / --tenant-id / --base-url all set -> machine mode: be

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Pass the access token to a handler the legacy 'input\_required' shim re-runs](https://github.com/modelcontextprotocol/ruby-sdk/pull/696)

`modelcontextprotocol/ruby-sdk` · **merged** · updated · 分数 64 · 上游时间 2026-11-22T15:04:10Z

入选依据：T3 watchlist; security: token; protocol: lifecycle; merged implementation; verify release separately。

> 上游摘录（未审读）：## Motivation and Context When a handler on the handshake lifecycle returns 'input\_required', the legacy shim sends the embedded requests to the client and runs the handler again with the answers. The re-run was dispatched without the access token of the request, so 'server\_context.auth\_info' was 'nil' on every round after the first: a tool that calls 'server\_context.require\_scopes!' was answered 'insufficient\_scope'

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Accept optional fields in elicitation schemas](https://github.com/PrefectHQ/fastmcp/pull/5907)

`PrefectHQ/fastmcp` · **merged** · updated · 分数 60 · 上游时间 2026-11-22T19:11:13Z

入选依据：T1 watchlist; protocol: schema; merged implementation; verify release separately。

> 上游摘录（未审读）：'ctx.elicit()' builds the form schema with 'ElicitationJsonSchema', and Pydantic renders a field typed 'str \| None = None' as 'anyOf: \[{type: string}, {type: null}\]'. The validator's union branch rejects the 'null' member, so a response model with an ordinary optional field raises 'TypeError' and the tool call fails. The MCP elicitation primitive schemas have no null type, so the right wire form is the inner type, wi

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Apply the client's init\_timeout to each backend in a multi-server MCPConfig](https://github.com/PrefectHQ/fastmcp/pull/6028)

`PrefectHQ/fastmcp` · **merged** · updated · 分数 60 · 上游时间 2026-11-22T19:11:35Z

入选依据：T1 watchlist; protocol: timeout; merged implementation; verify release separately。

> 上游摘录（未审读）：'Client(config, init\_timeout=N)' bounds the handshake with a single-server config, but not with a multi-server one. The composite connects every backend before the outer client's own init timeout starts, and each backend 'StatefulProxyClient' was built without an 'init\_timeout', so it fell back to 'settings.client\_init\_timeout' (unbounded by default). One backend that starts but never answers the handshake therefore

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
