# MCP Radar · 2026-11-07 (UTC)

采集时间：2026-11-07T01:26:09+00:00 · 回看窗口：14 天。

这是公开来源的更新索引和选题素材，不是已经审读、复现的技术结论。标题和摘录来自上游；优先级由可见规则计算。

本次窗口内 2564 条记录；本日累计 332 个新增/变更版本；失败端点 3 个；覆盖警告 0 个。

## 覆盖与限制

PR merged 表示代码进入分支，不代表已发布；release 不自动证明符合某协议版本。初次运行只建立窗口基线。

仅跟踪 watchlist 中公开仓库的 PR、指定仓库 issue/commit、release、公开安全公告和订阅源。未提供 API 的社区讨论、社交媒体和完整标准文档变更不在覆盖保证内。RSS 仅提供源当前保留的条目。

- 采集失败：`Tencent/AI-Infra-Guard` / pulls — The read operation timed out
- 采集失败：`github/github-mcp-server` / pulls — The read operation timed out
- 采集失败：`snyk/agent-scan` / releases — The read operation timed out

## 重点 PR / 提案

显示 20 / 300 条；全部数据见当日 JSON。

### [fix: give app callbacks stable public tool names](https://github.com/PrefectHQ/fastmcp/pull/6334)

`PrefectHQ/fastmcp` · **open** · new · 分数 94 · 上游时间 2026-11-06T17:48:10Z

入选依据：T1 watchlist; breaking: breaking; security: authorization; protocol: protocol, sse; draft PR。

> 上游摘录（未审读）：Two distinct apps can both register 'save', but their UI callback references must also appear in 'tools/list' for a host that forwards only listed tools. Today the protocol listing collapses the local names while the UIs retain different identity addresses. This draft publishes the existing '\_\_ \_ ' addresses consistently for app callbacks, retaining identity metadata, transforms, visibility and authorization. Explici

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[4.1\] Require patched Authlib in client and server extras](https://github.com/PrefectHQ/fastmcp/pull/6338)

`PrefectHQ/fastmcp` · **merged** · new · 分数 94 · 上游时间 2026-11-06T23:46:15Z

入选依据：T1 watchlist; breaking: migration; security: security, oauth, token; merged implementation; verify release separately。

> 上游摘录（未审读）：The published 4.1 client and server extras allow Authlib releases affected by published JOSE advisories. Backport the Authlib 1.9.5 minimum from #6337 and refresh the workspace lock so the next 4.1 patch excludes those releases. FastMCP already verifies JWTs with joserfc. This preserves its remaining Authlib token generator and OAuthError behavior, with no runtime API migration. Existing 4.1 installations can also up

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [chore(deploy): promote registry v1.8.8 to production](https://github.com/modelcontextprotocol/registry/pull/1811)

`modelcontextprotocol/registry` · **merged** · new · 分数 94 · 上游时间 2026-11-06T14:17:05Z

入选依据：T1 watchlist; breaking: migration; security: security; merged implementation; verify release separately。

> 上游摘录（未审读）：Promote the registry application from 1.8.7 to 1.8.8, built from staging-validated commit d6b071e520de72dd6c10731bfa3aa017a5c06373. This changes only the production image tag and retains the deployed security patches, compression, monitoring, and capacity settings. The release allows remote URLs to be shared across server names and updates dependencies; no database migration is required. Consumers must not assume a r

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [SEP-3279 - Negotiated Tool Result Variants](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3279)

`modelcontextprotocol/modelcontextprotocol` · **closed** · new · 分数 92 · 上游时间 2026-11-06T18:30:14Z

入选依据：T1 watchlist; security: audience; protocol: negotiat; proposal: sep-。

> 上游摘录（未审读）：This SEP introduces negotiated tool result variants. Tools advertise supported output representations, clients select the outputs needed for each call, and hosts route each result by audience. ## Motivation and Context The current relationship between content and structuredContent is ambiguous. Clients handle them differently, which can duplicate model context, discard structured results, or route data to the wrong c

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [SEP-XXXX: Ending Subscription Streams with an Authorization Reason](https://github.com/modelcontextprotocol/transports-wg/pull/67)

`modelcontextprotocol/transports-wg` · **open** · updated · 分数 92 · 上游时间 2026-11-06T16:53:52Z

入选依据：T1 watchlist; security: authorization, token; protocol: protocol; proposal: sep-。

> 上游摘录（未审读）：The original issue is described in #62 This is a split from #63 ## Motivation and Context The current protocol for 'subscriptions/listen' does not define what the server is supposed to do when the token used to open the stream becomes invalid or insufficient (due to expiry, revocation, etc.). More importantly, it does not define how the server tells the client what has happened if it closes the stream for one of thes

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [SEP-3149: Require Token Endpoint Auth Methods Supported in CIMD](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3149)

`modelcontextprotocol/modelcontextprotocol` · **open** · updated · 分数 90 · 上游时间 2026-11-06T15:06:38Z

入选依据：T1 watchlist; breaking: deprecat; security: token; proposal: sep-; draft PR。

> 上游摘录（未审读）：## Motivation and Context This SEP makes the 'token\_endpoint\_auth\_methods\_supported' metadata parameter a required property of MCP Client ID Metadata Documents (CIMD), and creates a deprecation path for the singular 'token\_endpoint\_auth\_method' parameter, mirroring the guidance in \[OpenID Connect RP Metadata Choices 1.0\](https://openid.net/specs/openid-connect-rp-metadata-choices-1\_0-final.html). This enables a CIMD

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Update example locks past the schema-parsing security fix](https://github.com/PrefectHQ/fastmcp/pull/6339)

`PrefectHQ/fastmcp` · **merged** · new · 分数 86 · 上游时间 2026-11-07T00:37:28Z

入选依据：T1 watchlist; security: security, ghsa-; protocol: schema; merged implementation; verify release separately。

> 上游摘录（未审读）：The testing demo and smart-home example lockfiles still select FastMCP versions affected by \[GHSA-gpgx-58w2-xwwf\](https://github.com/PrefectHQ/fastmcp/security/advisories/GHSA-gpgx-58w2-xwwf). Update testing\_demo from 3.2.0 to the patched 3.4.8 release and smart\_home from 4.0.10 to 4.0.11, preserving each example's major version and the existing Authlib 1.9.5 locks. Raise both examples' FastMCP dependency minimums to

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(release): support conventional release PR titles](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3506)

`modelcontextprotocol/modelcontextprotocol` · **merged** · updated · 分数 84 · 上游时间 2026-11-06T10:19:04Z

入选依据：T1 watchlist; breaking: breaking; proposal: specification; merged implementation; verify release separately。

> 上游摘录（未审读）：Updates release publication to use the release branch instead of the PR title. When a 'release/YYYY-MM-DD' PR merges into 'main', the workflow publishes its merge commit. Release PRs now use 'chore(release): publish YYYY-MM-DD specification', allowing conventional titles without breaking release publication.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(cli): Hide deprecated --access-token from sentry mcp help](https://github.com/getsentry/toolkit/pull/2057)

`getsentry/toolkit` · **merged** · new · 分数 82 · 上游时间 2026-11-06T19:08:01Z

入选依据：T2 watchlist; breaking: deprecat; security: token; merged implementation; verify release separately。

> 上游摘录（未审读）：'sentry mcp --help' listed '--access-token', although it's deprecated. The other deprecated mcp flags ('--host', '--url', '--insecure-http', '--organization-slug', '--project-slug') are hidden. \*\*What changed\*\* - '--access-token' now uses the hidden 'deprecatedStringFlag("SENTRY\_AUTH\_TOKEN")' helper. Before, it used a visible 'stringFlag'. Parsing, the single deprecation warning (in 'lib/mcp.ts') and telemetry redact

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [SEP-2487: Add execution.requirements field to Tool for preconditions](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2487)

`modelcontextprotocol/modelcontextprotocol` · **open** · new · 分数 82 · 上游时间 2026-11-06T15:07:02Z

入选依据：T1 watchlist; security: oauth; protocol: capabilit; proposal: sep-, proposal; draft PR。

> 上游摘录（未审读）：## Preamble - Status: Draft - Type: Standards Track - Created: 2026-03-27 - Author(s): Zachary German - Sponsor: TBD - Discussion: TBD --- ## Summary Add an optional 'execution.requirements' field to tool definitions: '''json { "name": "launch\_rocket", "execution": { "requirements": \[ "auth:oauth2", "auth:claim:role:mission\_control", "capability:rocket.launch", "env:production", "state:weather.clear", "feature:launch

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [SEP-2643: Structured Authorization Denials](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2643)

`modelcontextprotocol/modelcontextprotocol` · **open** · new · 分数 82 · 上游时间 2026-11-06T15:07:09Z

入选依据：T1 watchlist; security: authorization; protocol: protocol, transport; proposal: sep-, proposal; draft PR。

> 上游摘录（未审读）：## Motivation and Context This SEP defines a transport-agnostic authorization denial envelope for the Model Context Protocol. The envelope complements transport-level authorization challenges (HTTP 'WWW-Authenticate' with Protected Resource Metadata), carrying a failure classification, a remediation posture, a retry correlation handle, and an extensible set of structured remediation hints for cases the transport cann

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [SEP-2848: Asynchronous Approval for Tool Calls](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2848)

`modelcontextprotocol/modelcontextprotocol` · **open** · updated · 分数 82 · 上游时间 2026-11-06T16:53:09Z

入选依据：T1 watchlist; security: authorization; protocol: protocol; proposal: sep-, proposal, extension; draft PR。

> 上游摘录（未审读）：## Summary Draft \*\*Extensions Track\*\* SEP introducing an experimental extension, 'io.modelcontextprotocol/tool-approval', that lets an MCP server gate a tool call on an \*\*out-of-band approval\*\* without keeping the original request open. When the server's authorization decision is a denial that is \*requestable\* (something can still approve it), the server returns a task handle (SEP-2663 Tasks) in place of the tool res

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Move upstream filter contracts out of handlers](https://github.com/stacklok/toolhive/pull/7059)

`stacklok/toolhive` · **merged** · new · 分数 82 · 上游时间 2026-11-06T10:30:00Z

入选依据：T2 watchlist; breaking: compatib; security: authorization; merged implementation; verify release separately。

> 上游摘录（未审读）：Let embedders configure upstream filters without importing HTTP handlers. Retain handler aliases and existing authorization behavior, and cover the public and compatibility paths. Co-authored-by: Mecatl

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(tools): preserve empty output for None-returning tools and transforms](https://github.com/PrefectHQ/fastmcp/pull/6333)

`PrefectHQ/fastmcp` · **closed** · new · 分数 78 · 上游时间 2026-11-06T17:16:31Z

入选依据：T1 watchlist; breaking: compatib; protocol: sse, schema。

> 上游摘录（未审读）：A '-> None' tool should return empty content, but adding 'from \_\_future\_\_ import annotations' currently infers a wrapped null output schema and emits '{"result": null}'. Resolve 'NoneType' the same way as 'None'. For transformed tools, an explicit void return also suppresses parent-schema inheritance; otherwise removing the inferred null schema can make a void transform inherit an incompatible integer schema. Unannot

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: record HTTP over STDIO negotiation decision](https://github.com/modelcontextprotocol/transports-wg/pull/61)

`modelcontextprotocol/transports-wg` · **open** · new · 分数 78 · 上游时间 2026-11-06T15:30:28Z

入选依据：T1 watchlist; breaking: migration, deprecat; protocol: protocol, transport, stdio。

> 上游摘录（未审读）：Compares startup protocol negotiation with explicit transport selection through user configuration. Recommends introducing stdio-v2 experimentally, followed by migration under MCP's deprecation policy.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: propose HTTP over STDIO negotiation](https://github.com/modelcontextprotocol/transports-wg/pull/66)

`modelcontextprotocol/transports-wg` · **open** · updated · 分数 78 · 上游时间 2026-11-06T15:30:29Z

入选依据：T1 watchlist; breaking: compatib; protocol: transport, stdio, negotiat。

> 上游摘录（未审读）：Proposes using 'server/discover' and 'supportedVersions' to select an HTTP-only MCP revision, then sending the HTTP/2 preface on the same pipes. Compatible clients and servers can switch without restarting the process or introducing a separate transport capability or upgrade RPC. Covers HTTP/STDIO/Both compatibility, existing stateful/stateless negotiation, parser handoff and failure boundaries, and direct HTTP/2 sta

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: create storage directory in FileTreeStore examples](https://github.com/PrefectHQ/fastmcp/pull/6324)

`PrefectHQ/fastmcp` · **closed** · new · 分数 76 · 上游时间 2026-11-06T11:41:43Z

入选依据：T1 watchlist; security: oauth, token; protocol: sse。

> 上游摘录（未审读）：Fixes #6323 ## Summary The three 'FileTreeStore' examples in 'docs/servers/storage-backends.mdx' fail on a fresh machine with 'FileNotFoundError', because the directory passed to the sanitization strategies is never created: - the File storage example ('Path("/var/cache/fastmcp")') - the response caching example ('Path("cache")') - the client-side OAuth token storage example ('Path("~/.local/share/fastmcp/tokens")')

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(schema): close oneOf type-check bypass and render SEP-2106 Tool examples](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3185)

`modelcontextprotocol/modelcontextprotocol` · **merged** · new · 分数 76 · 上游时间 2026-11-06T14:45:26Z

入选依据：T1 watchlist; protocol: sse, schema; proposal: sep-; merged implementation; verify release separately。

> 上游摘录（未审读）：This addresses an issue where the 'find\_resource' example distinguished its 'oneOf' branches with branch-local 'properties'. Failing a branch on a type error is exactly what makes 'oneOf' succeed, so a wrongly-typed value in the inactive branch was accepted, eg: ''' {"id": "r1", "name": 123} validated {"id": 123, "name": "alpha"} validated ''' This means that the mutual exclusivity the example is meant to demonstrate

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(auth): accept trusted external-IdP bearer tokens on /mcp](https://github.com/IBM/mcp-context-forge/pull/7450)

`IBM/mcp-context-forge` · **merged** · updated · 分数 74 · 上游时间 2026-11-06T14:05:37Z

入选依据：T2 watchlist; security: token; protocol: streamable; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary A trusted external-IdP bearer token ('SSO\_API\_TOKEN\_AUTH\_ENABLED=true', provider 'trusted\_for\_api\_auth=true') now authenticates on '/mcp' and '/servers/{id}/mcp', the same as on REST and '/rpc'. PR #6424 fixed REST and '/rpc' for #6396 and left '/mcp' open. Closes #7435 ## Root cause The streamable HTTP auth handler used a different verifier than '/rpc': - '\_StreamableHttpAuthHandler.\_route\_idp\_issued\_toke

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(tools): Add structured output to create\_project](https://github.com/getsentry/toolkit/pull/2013)

`getsentry/toolkit` · **merged** · new · 分数 74 · 上游时间 2026-11-05T22:09:35Z

入选依据：T2 watchlist; security: security; protocol: schema; merged implementation; verify release separately。

> 上游摘录（未审读）：'create\_project' now declares an 'outputSchema' and returns 'structuredResult()' on every success path, following the Structured Content policy in 'docs/contributing/tool-responses.md'. Output shape: '{ project: { id, slug, name }, dsn: string \| null, repository: { name, linked } \| null }'. - \*\*Public DSN only.\*\* 'dsn' is 'clientKey.dsn.public'. The client key secret, secret DSN, security/CSP endpoints, rate limit an

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 发布与安全公告

显示 4 / 4 条；全部数据见当日 JSON。

### [v1.8.8](https://github.com/modelcontextprotocol/registry/releases/tag/v1.8.8)

`modelcontextprotocol/registry` · **published** · new · 分数 103 · 上游时间 2026-11-06T14:12:19Z

入选依据：T1 watchlist; breaking: migration; protocol: protocol; release。

> 上游摘录（未审读）：This release uses the source commit validated in staging. Different server names may now share a remote URL; consumers should key listings by server name and version rather than assuming URL uniqueness. No database migration is required. ## What's Changed \* Stage v1.8.7 in production with prepared reads disabled by @rdimitrov in https://github.com/modelcontextprotocol/registry/pull/1769 \* Enable prepared listing JSON

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [List response filter passes compressed responses through unfiltered](https://github.com/stacklok/toolhive/security/advisories/GHSA-v869-pp2g-ff4q)

`stacklok/toolhive` · **published** · new · 分数 89 · 上游时间 2026-11-06T13:14:13Z

入选依据：T2 watchlist; security: authorization; protocol: transport, sse; advisory。

> 上游摘录（未审读）：### Summary When Cedar authorization filters list responses, ToolHive forwarded a compressed list response to the client without filtering it. The client decompressed the body and saw every tool, prompt, resource and skill, including those its policy hides. ### Details The transparent proxy forwarded the client's 'Accept-Encoding' header to the backend. Go's HTTP transport decompresses a response only when it added '

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Tool filter passes an unfiltered tools/list through on a decode type error or a case-folded 'tools' alias](https://github.com/stacklok/toolhive/security/advisories/GHSA-v9xx-q4mg-gwmv)

`stacklok/toolhive` · **published** · new · 分数 89 · 上游时间 2026-11-06T13:14:11Z

入选依据：T2 watchlist; security: ghsa-; protocol: sse; advisory。

> 上游摘录（未审读）：### Summary With a tool filter configured ('thv run --tools', or 'toolConfigRef' -> 'MCPToolConfig.toolsFilter' in the operator), two shapes of 'tools/list' response make the filter forward the backend's list unfiltered, so a client sees and is offered the tools the operator hid. The filter is documented as an access control ('docs/middleware.md:294'). GHSA-9v4w-3mqh-6vmm reported the same fail-open for a body 'encod

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v0.63.0](https://github.com/stacklok/toolhive/releases/tag/v0.63.0)

`stacklok/toolhive` · **published** · new · 分数 43 · 上游时间 2026-11-06T13:04:28Z

入选依据：T2 watchlist; release。

> 上游摘录（未审读）：## What's Changed \* Deny local webhook errors under ignore failure policy by @rdimitrov in https://github.com/stacklok/toolhive/pull/7055 \* Leave user-owned Bedrock keys alone in llm setup by @aponcedeleonch in https://github.com/stacklok/toolhive/pull/7051 \* fix: address open code scanning alerts by @stacklokbot in https://github.com/stacklok/toolhive/pull/7056 \* Validate vMCP incoming OIDC CA references by @Sanskar

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 协议 / 工作组提交

显示 10 / 28 条；全部数据见当日 JSON。

### [fix(schema): close oneOf type-check bypass and render SEP-2106 Tool examples (#3185)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/38353251fab3bdeead03dd8283b9e66076ce1a7f)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 71 · 上游时间 2026-11-06T14:45:22Z

入选依据：T1 watchlist; protocol: schema; proposal: sep-。

> 上游摘录（未审读）：fix(schema): close oneOf type-check bypass and render SEP-2106 Tool examples (#3185) \* fix(schema): close type-check bypass in composition inputSchema example The 'find\_resource' example distinguished its 'oneOf' branches with branch-local 'properties'. Failing a branch on a type error is exactly what makes 'oneOf' succeed, so a wrongly-typed value in the inactive branch was accepted: {"id": "r1", "name": 123} valida

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(schema): restore optional \_meta on input requests and responses (#3469)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/c9b51b3a02f3851f9821d5191718652bab97adac)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 71 · 上游时间 2026-11-06T15:57:15Z

入选依据：T1 watchlist; protocol: schema; proposal: sep-。

> 上游摘录（未审读）：fix(schema): restore optional \_meta on input requests and responses (#3469) SEP-2322 stopped these types from being standalone JSON-RPC messages: the request params no longer extend TaskAugmentedRequestParams (3443ffac) and the results no longer extend Result (2d37d9de). Both base types carried '\_meta', so it was dropped as a side effect from CreateMessageRequestParams, ElicitRequestFormParams, ElicitRequestURLParams

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(release): create conventional release PRs with an App token](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/bf2c1bc3f37a0bf7c4ea60ad7dfc1b8698d80863)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 61 · 上游时间 2026-11-04T23:56:37Z

入选依据：T1 watchlist; security: token。

> 上游摘录（未审读）：fix(release): create conventional release PRs with an App token

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Merge pull request #3507 from modelcontextprotocol/ci/conventional-pr-titles](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/1e69fea8ee88fff4c2d5a64b78f01ee61eb373a9)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 55 · 上游时间 2026-11-06T13:31:40Z

入选依据：T1 watchlist; protocol: protocol。

> 上游摘录（未审读）：Merge pull request #3507 from modelcontextprotocol/ci/conventional-pr-titles ci: check conventional PR titles

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: update the Rust server tutorial to rmcp 3](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/21a8a3eba3b6929793b59342d9e5856b671856a7)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 55 · 上游时间 2026-10-31T07:21:54Z

入选依据：T1 watchlist; protocol: protocol, negotiat。

> 上游摘录（未审读）：docs: update the Rust server tutorial to rmcp 3 Rebuild the Rust tab of build-server.mdx from weather-server-rust in quickstart-resources at 99a4ea1. The tab pinned rmcp 0.3, which knows no protocol revision newer than 2025-03-26 and fails version negotiation with current clients. The Cargo.toml and src/main.rs now match upstream (rmcp = "3.4", resolving to 3.8.0), and the minimum Rust version is the one the SDK decl

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Merge pull request #3482 from modelcontextprotocol/docs/client-tutorial-tool-loop](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/22bb5b965a58e7f502deb184b51a8a4b8bf6067a)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 55 · 上游时间 2026-11-06T14:16:51Z

入选依据：T1 watchlist; protocol: protocol。

> 上游摘录（未审读）：Merge pull request #3482 from modelcontextprotocol/docs/client-tutorial-tool-loop docs: run a full tool loop in the client tutorial

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Merge pull request #3479 from modelcontextprotocol/docs/rust-server-tutorial-rmcp-3](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/352c0c9fc451387788fe8a0121184c944f1c82b7)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 55 · 上游时间 2026-11-06T14:02:48Z

入选依据：T1 watchlist; protocol: protocol。

> 上游摘录（未审读）：Merge pull request #3479 from modelcontextprotocol/docs/rust-server-tutorial-rmcp-3 docs: update the Rust server tutorial to rmcp 3

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Merge pull request #3506 from modelcontextprotocol/fix/release-pr-metadata](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/d9d26ddbbe8e0bc97b4f365b4445b2642e664fef)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 55 · 上游时间 2026-11-06T10:19:00Z

入选依据：T1 watchlist; protocol: protocol。

> 上游摘录（未审读）：Merge pull request #3506 from modelcontextprotocol/fix/release-pr-metadata fix(release): support conventional release PR titles

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: explain the Kotlin client's protocol revision in the tutorial note](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/ea7dca839fbc6a1e6ad5009602612b41034a2ea8)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 55 · 上游时间 2026-10-31T14:54:34Z

入选依据：T1 watchlist; protocol: protocol。

> 上游摘录（未审读）：docs: explain the Kotlin client's protocol revision in the tutorial note

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [chore: update repo structure and membership (#71)](https://github.com/modelcontextprotocol/transports-wg/commit/205d03deb1ca819d4b18c96e7cc2e11c041442ae)

`modelcontextprotocol/transports-wg` · **committed** · new · 分数 51 · 上游时间 2026-11-06T15:28:30Z

入选依据：T1 watchlist; proposal: proposal。

> 上游摘录（未审读）：chore: update repo structure and membership (#71) Make the README the entry point for meetings, Discord, contribution guidance, and current work. Group proposal material by project, clarify which drafts have official upstream SEPs, and update the roadmap to March 2027. - Link to the published MCP charter and consolidate CONTRIBUTING into the README. - Refresh WG Members, Working Group Leads, and Emeritus rosters; lin

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
