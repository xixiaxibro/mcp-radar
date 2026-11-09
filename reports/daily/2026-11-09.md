# MCP Radar · 2026-11-09 (UTC)

采集时间：2026-11-09T01:17:09+00:00 · 回看窗口：14 天。

这是公开来源的更新索引和选题素材，不是已经审读、复现的技术结论。标题和摘录来自上游；优先级由可见规则计算。

本次窗口内 2650 条记录；本日累计 242 个新增/变更版本；失败端点 0 个；覆盖警告 0 个。

## 覆盖与限制

PR merged 表示代码进入分支，不代表已发布；release 不自动证明符合某协议版本。初次运行只建立窗口基线。

仅跟踪 watchlist 中公开仓库的 PR、指定仓库 issue/commit、release、公开安全公告和订阅源。未提供 API 的社区讨论、社交媒体和完整标准文档变更不在覆盖保证内。RSS 仅提供源当前保留的条目。

本次未报告采集错误或分页截断；这不代表覆盖整个 MCP 生态。

## 重点 PR / 提案

显示 20 / 230 条；全部数据见当日 JSON。

### [docs: rework the authorization guide for the 2026-07-28 specification](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3518)

`modelcontextprotocol/modelcontextprotocol` · **merged** · new · 分数 110 · 上游时间 2026-11-08T01:19:30Z

入选依据：T1 watchlist; breaking: deprecat; security: authorization, audience; proposal: specification; merged implementation; verify release separately。

> 上游摘录（未审读）：Make Client ID Metadata Documents the main registration path and mark Dynamic Client Registration deprecated. Replace the vendor walkthrough with provider-agnostic requirements, and move the TypeScript, Python and C# examples to the v2 SDKs with audience, issuer, scope and origin checks.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[Server\] Bind Streamable HTTP sessions to the principal that opened them](https://github.com/modelcontextprotocol/php-sdk/pull/627)

`modelcontextprotocol/php-sdk` · **merged** · updated · 分数 108 · 上游时间 2026-11-08T13:04:09Z

入选依据：T3 watchlist; breaking: breaking; security: security; protocol: protocol, streamable; proposal: specification; merged implementation; verify release separately。

> 上游摘录（未审读）：Fixes #529 A handshake-era session now only serves the principal that opened it, as the \[security best practices\](https://modelcontextprotocol.io/specification/2025-11-25/basic/security\_best\_practices#session-hijacking) recommend. When another principal sends the session id, the server answers 404 like for an unknown session, and its 'DELETE' doesn't end the session. I found this while building an MCP server for the

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Migrate to GitHub REST API version 2026-03-10](https://github.com/github/github-mcp-server/pull/3038)

`github/github-mcp-server` · **open** · new · 分数 104 · 上游时间 2026-11-08T02:58:40Z

入选依据：T1 watchlist; breaking: deprecat, compatib; security: token; protocol: stdio, schema。

> 上游摘录（未审读）：## Summary - use REST API version '2026-03-10' for GitHub.com and GitHub Enterprise Cloud - pin GitHub Enterprise Server requests to the compatible '2022-11-28' API version - apply the host-aware policy to stdio and per-request REST clients, scope discovery, and GitHub App installation-token requests - remove the deprecated singular 'assignee' field from issue and pull-request search field schemas - add regression co

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Point Skills specification links at specification/beta/](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3466)

`modelcontextprotocol/modelcontextprotocol` · **merged** · updated · 分数 102 · 上游时间 2026-11-08T05:01:56Z

入选依据：T1 watchlist; security: security; protocol: protocol, lifecycle; proposal: sep-, specification, extension; merged implementation; verify release separately。

> 上游摘录（未审读）：Under \[SEP-3392\](https://modelcontextprotocol.io/seps/3392-extension-lifecycle), the Skills extension is Beta. modelcontextprotocol/ext-skills#161 moves its specification from 'specification/stable/' to 'specification/beta/'. GitHub does not redirect moved paths, so this PR updates the three links on the website that point at the old path: - 'docs/extensions/skills/overview.mdx': the security requirements link and th

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(deploy): complete standalone staging Gateway migration](https://github.com/modelcontextprotocol/registry/pull/1822)

`modelcontextprotocol/registry` · **merged** · new · 分数 94 · 上游时间 2026-11-08T18:36:24Z

入选依据：T1 watchlist; breaking: migration; security: security; merged implementation; verify release separately。

> 上游摘录（未审读）：Completes the staging-only retirement of ingress-nginx and the duplicate canary while preserving the public Service/IP, trusted Certificates, security upgrades and normal release flow. Four single-worker Gateway proxies remain on the same two Gateway nodes. Native Gateway HTTP01 and cert-manager-managed internal mTLS replace the legacy solver/bootstrap resources. \*\*Live checks completed:\*\* caching/headers/limits; 500

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Tool annotations: the spec does not say how the untrusted-annotations rule applies to clients that force a tool call](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/3492)

`modelcontextprotocol/modelcontextprotocol` · **open** · updated · 分数 92 · 上游时间 2026-11-07T14:56:04Z

入选依据：T1 watchlist; security: security; protocol: protocol; proposal: specification。

> 上游摘录（未审读）：### What's broken? The spec doesn't cover a case it clearly should ### Where in the spec or docs? https://modelcontextprotocol.io/specification/2026-07-28/server/tools#tool (the Warning under 'annotations') and https://modelcontextprotocol.io/specification/2026-07-28/server/tools#security-considerations ### What should happen? A short note after the Warning, for example: > Note: because annotations from untrusted ser

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[Server\] Serve handshake-era clients without sessions](https://github.com/modelcontextprotocol/php-sdk/pull/645)

`modelcontextprotocol/php-sdk` · **merged** · updated · 分数 82 · 上游时间 2026-11-08T17:35:15Z

入选依据：T3 watchlist; breaking: breaking; protocol: protocol, transport; proposal: specification; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #644. A session is optional in the handshake era: a server \["MAY assign a session ID at initialization time"\](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports#session-management). The SDK always creates one on 'initialize' and refuses every later request without it, so a horizontally scaled server has to share a session store and lock only to serve handshake-era clients. Sessions over

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Release v2.4.0](https://github.com/modelcontextprotocol/csharp-sdk/pull/2001)

`modelcontextprotocol/csharp-sdk` · **merged** · new · 分数 80 · 上游时间 2026-11-07T03:51:19Z

入选依据：T3 watchlist; security: oauth; protocol: protocol, transport; proposal: extension; merged implementation; verify release separately。

> 上游摘录（未审读）：# Release v2.4.0 \*\*MCP Skills\*\* support is introduced with experimental APIs in the new \[ModelContextProtocol.Extensions.Skills\](https://nuget.org/packages/ModelContextProtocol.Extensions.Skills) package. The release also strengthens OAuth handling and improves transport/session reliability/discovery. MCP Apps now match protocol property names case-sensitively. ## What's Changed \* Add the experimental MCP Skills exte

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(sse): add configurable max\_sse\_event\_size to sse\_client and SseSe…](https://github.com/modelcontextprotocol/python-sdk/pull/3832)

`modelcontextprotocol/python-sdk` · **closed** · new · 分数 78 · 上游时间 2026-11-07T12:59:19Z

入选依据：T1 watchlist; breaking: breaking; protocol: sse。

> 上游摘录（未审读）：…rverParameters (fixes #3803) Fixes # ## Motivation and Context ## How Has This Been Tested? ## Breaking Changes ## Types of changes - \[ \] Bug fix (non-breaking change which fixes an issue) - \[ \] New feature (non-breaking change which adds functionality) - \[ \] Breaking change (fix or feature that would cause existing functionality to change) - \[ \] Documentation update ## Checklist - \[ \] I am assigned to the linked is

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix: address log limits, OAuth callbacks, job pagination, and CRLF icons](https://github.com/github/github-mcp-server/pull/3731)

`github/github-mcp-server` · **open** · new · 分数 76 · 上游时间 2026-11-08T08:23:08Z

入选依据：T1 watchlist; security: oauth; protocol: cancel, pagination。

> 上游摘录（未审读）：## Summary Make Actions log downloads cancellable and bounded, keep unrelated OAuth callbacks from aborting login, retrieve failed jobs across every page, and normalize embedded icon data across Windows and Unix line endings. ## Why Log reads could continue after their MCP call was cancelled and retain excessive text. A run whose failed job appeared after the first page could incorrectly report no failures, and unrel

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: document working-group-based contribution policy](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3514)

`modelcontextprotocol/modelcontextprotocol` · **merged** · updated · 分数 76 · 上游时间 2026-11-08T04:53:54Z

入选依据：T1 watchlist; protocol: protocol, sse; proposal: proposal, specification; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary Updates the contribution guidelines to reflect that contributions go through working groups and issues. \*\*CONTRIBUTING.md\*\* - Specification proposals must be discussed in, and explicitly approved by, the relevant working group before a SEP pull request is opened. - Only members of the 'modelcontextprotocol' GitHub organization may open pull requests. Membership is requested in the \[access repository\](https

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Pass httpx auth through ClientSessionGroup HTTP parameters](https://github.com/modelcontextprotocol/python-sdk/pull/3840)

`modelcontextprotocol/python-sdk` · **open** · new · 分数 76 · 上游时间 2026-11-08T23:29:18Z

入选依据：T1 watchlist; security: oauth, token; protocol: streamable, sse。

> 上游摘录（未审读）：Fixes #1723 ## Summary 'ClientSessionGroup' could not carry an 'httpx2.Auth'. Callers had to put a bearer token in 'headers', so an 'OAuthClientProvider' (discovery, refresh) could not run from a session group. 'SseServerParameters' and 'StreamableHttpParameters' now take an optional 'auth'. 'connect\_to\_server' passes it to 'sse\_client' and 'create\_mcp\_http\_client'. 'auth' is omitted from 'model\_dump()', 'model\_dump\_

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Prepare package slicing by strict namespace refactoring into Client, Schema, and Server](https://github.com/modelcontextprotocol/php-sdk/pull/493)

`modelcontextprotocol/php-sdk` · **open** · new · 分数 72 · 上游时间 2026-11-09T01:17:32Z

入选依据：T3 watchlist; breaking: breaking; protocol: schema; proposal: proposal。

> 上游摘录（未审读）：Proposal to rework namespaces in favor of slicing 'mcp/sdk' package, see #489 1. Moved everything below 'Mcp\\Client', 'Mcp\\Schema', or 'Mcp\\Server' 2. Distributed 'Mcp\\Exception' into component specific namespaces --- Next steps would be: \* introduce composer setups per component \* configure split.sh \* ???

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Dependabot/go modules/golang.org/x/net 0.62.0](https://github.com/github/github-mcp-server/pull/3714)

`github/github-mcp-server` · **open** · new · 分数 66 · 上游时间 2026-11-07T09:35:26Z

入选依据：T1 watchlist; security: security, token; protocol: schema; draft PR。

> 上游摘录（未审读）：## Summary ## Why Fixes # ## What changed - - ## MCP impact - \[ \] No tool or API changes - \[ \] Tool schema or behavior changed - \[ \] New tool added ## Prompts tested (tool changes only) - ## Security / limits - \[ \] No security or limits impact - \[ \] Auth / permissions considered - \[ \] Data exposure, filtering, or token/size limits considered ## Tool renaming - \[ \] I am renaming tools as part of this PR (e.g. a part o

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(sep-3415): Conformance suite for triggers and events](https://github.com/modelcontextprotocol/conformance/pull/521)

`modelcontextprotocol/conformance` · **open** · new · 分数 66 · 上游时间 2026-11-09T00:39:54Z

入选依据：T1 watchlist; protocol: protocol, conformance; proposal: sep-。

> 上游摘录（未审读）：## What changes Adds a requirement-traceability yaml for MCP Events and the five server scenarios that score an implementation against it, plus 150 negative controls and one runner change. The rows were first extracted from the design sketch on 'main' of \['modelcontextprotocol/experimental-ext-triggers-events'\](https://github.com/modelcontextprotocol/experimental-ext-triggers-events), as amended by \[PR 7\](https://git

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(skills): check ttlMs/cacheScope on resources/directory/read results](https://github.com/modelcontextprotocol/conformance/pull/559)

`modelcontextprotocol/conformance` · **open** · new · 分数 66 · 上游时间 2026-11-09T00:07:28Z

入选依据：T1 watchlist; protocol: protocol, negotiat; proposal: sep-。

> 上游摘录（未审读）：ext-skills#157 made ReadResourceDirectoryResult extend CacheableResult, so from protocol 2026-07-28 a directory read result MUST carry ttlMs and cacheScope, matching resources/list and the existing skills/list and skills/get checks. Adds sep-2640-directory-read-cache-attributes to the directory scenario, gated on the negotiated protocol version like its skills/list and skills/get siblings, the matching row in sep-264

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [SEP-3094: Granular Citations Format](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3094)

`modelcontextprotocol/modelcontextprotocol` · **closed** · updated · 分数 66 · 上游时间 2026-11-08T05:05:16Z

入选依据：T1 watchlist; protocol: protocol; proposal: sep-, sep:, proposal。

> 上游摘录（未审读）：# SEP: Granular citations format - \*\*Status\*\*: Draft - \*\*Type\*\*: Standards Track - \*\*Created\*\*: 2026-07-15 - \*\*Author(s)\*\*: Karthik Palaniappan (karthik.palaniappan@thomsonreuters.com) (@karth295) - \*\*Sponsor\*\*: None - \*\*PR\*\*: https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3094 Many popular MCP clients (e.g. ChatGPT, Copilot) have \*\*bespoke\*\* formats for MCP servers to return rich citations. Other

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[Server\]\[Client\] Remove JSON-RPC batch support](https://github.com/modelcontextprotocol/php-sdk/pull/680)

`modelcontextprotocol/php-sdk` · **merged** · new · 分数 66 · 上游时间 2026-11-08T12:50:06Z

入选依据：T3 watchlist; breaking: breaking; protocol: protocol, negotiat; merged implementation; verify release separately。

> 上游摘录（未审读）：MCP removed batching in '2025-06-18', so a JSON array is refused with '-32600' for every protocol version - that includes '2025-03-26', which requires batches and which we still negotiate. I didn't find a well-adopted client that sends them, but can't see into the closed-source ones. \[BC Break\] 'MessageFactory::create()' returns one message and throws on invalid input, '$maxBatchSize' is gone - see 'CHANGELOG.md'.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(oauth): add extra\_auth\_params for provider authorization parameters](https://github.com/IBM/mcp-context-forge/pull/7490)

`IBM/mcp-context-forge` · **open** · new · 分数 64 · 上游时间 2026-11-08T09:56:23Z

入选依据：T2 watchlist; security: oauth, authorization, token; protocol: schema。

> 上游摘录（未审读）：Closes #4044 Closes #4115 ## Problem The gateway builds the authorization URL from a fixed set of parameters, so a provider that needs one more cannot be configured. Google returns no refresh token without 'access\_type=offline', and Atlassian requires 'prompt=consent'. ## Solution 1. 'oauth\_config.extra\_auth\_params' takes string names and string values and adds them to the authorization URL. 2. The schema rejects nam

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(postgres-mcp-server): accept username-only secret for PG\_WIRE\_IAM\_PROTOCOL](https://github.com/awslabs/mcp/pull/4829)

`awslabs/mcp` · **open** · updated · 分数 64 · 上游时间 2026-11-07T02:40:21Z

入选依据：T2 watchlist; security: token; protocol: protocol。

> 上游摘录（未审读）：Fixes #4824 ## Summary ### Changes With '--connection\_method PG\_WIRE\_IAM\_PROTOCOL', the password is a generated IAM auth token, so the '--secret\_arn' secret only needs a 'username'. Both IAM code paths, however, read the secret through 'get\_credentials\_from\_secret()', which raises when there is no 'password' key. - 'connection/psycopg\_pool\_connection.py': the secret parsing moves into a private '\_read\_credentials\_fro

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 发布与安全公告

显示 3 / 3 条；全部数据见当日 JSON。

### [v2.4.0](https://github.com/modelcontextprotocol/csharp-sdk/releases/tag/v2.4.0)

`modelcontextprotocol/csharp-sdk` · **published** · new · 分数 95 · 上游时间 2026-11-07T04:26:54Z

入选依据：T3 watchlist; security: oauth; protocol: protocol, transport; proposal: extension; release。

> 上游摘录（未审读）：Version 2.4.0 adds experimental MCP Skills support through the new \[ModelContextProtocol.Extensions.Skills\](https://nuget.org/packages/ModelContextProtocol.Extensions.Skills) package, alongside OAuth hardening and reliability improvements for transport, session, and discovery flows. MCP Apps also now match protocol property names case-sensitively. ## What's Changed \* Add the experimental MCP Skills extension #1856 by

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v0.15.0](https://github.com/sparfenyuk/mcp-proxy/releases/tag/v0.15.0)

`sparfenyuk/mcp-proxy` · **published** · new · 分数 89 · 上游时间 2026-11-07T14:20:38Z

入选依据：T2 watchlist; security: token; protocol: transport; release。

> 上游摘录（未审读）：## What's new - Optional Bearer authentication for inbound HTTP transports, configured through 'MCP\_PROXY\_AUTH\_TOKEN'. - New container flavors: Debian for glibc-dependent Python servers, and Debian with Node.js/npm/npx for Node-based servers. Existing Alpine images and startup commands remain supported. - Better named-server isolation: a backend that fails during startup no longer prevents healthy backends from servi

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [cli@0.49.0](https://github.com/getsentry/toolkit/releases/tag/cli%400.49.0)

`getsentry/toolkit` · **published** · new · 分数 63 · 上游时间 2026-11-07T10:07:53Z

入选依据：T2 watchlist; protocol: capabilit; release。

> 上游摘录（未审读）：New CLI, MCP, search, profiling, and evaluation capabilities, paired with safer persistence, diagnostics, and workflow tooling, improve testing, setup, and development. ### New Features ✨ CLI, MCP, search, profiling, and evaluation updates add structured outputs, safer persistence, replayable testing, and clearer setup guidance. #### Cli CLI updates add the sentry\\'…\\' tag for command hints, linting, and correct npx

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 协议 / 工作组提交

显示 9 / 9 条；全部数据见当日 JSON。

### [docs: rework the authorization guide for the 2026-07-28 specification (#3518)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/fd502785f2732ae0028de7e9fa34d6ebcd950c65)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 105 · 上游时间 2026-11-08T01:19:26Z

入选依据：T1 watchlist; breaking: deprecat; security: authorization, audience; proposal: specification。

> 上游摘录（未审读）：docs: rework the authorization guide for the 2026-07-28 specification (#3518) \* docs: rework the authorization guide for the 2026-07-28 specification Make Client ID Metadata Documents the main registration path and mark Dynamic Client Registration deprecated. Replace the vendor walkthrough with provider-agnostic requirements, and move the TypeScript, Python and C# examples to the v2 SDKs with audience, issuer, scope

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Merge pull request #3508 from modelcontextprotocol/ci/adopt-checked-squash-merges](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/cf59bb0d8b43e711420f5f7313aa6cca3f1e1898)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 55 · 上游时间 2026-11-07T11:03:06Z

入选依据：T1 watchlist; protocol: protocol。

> 上游摘录（未审读）：Merge pull request #3508 from modelcontextprotocol/ci/adopt-checked-squash-merges ci: pin documentation build tools

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Document working-group-based contribution policy (#3514)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/e5a28a6841fd85b4624399c77d1d7ce764dc5420)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 55 · 上游时间 2026-11-08T04:53:50Z

入选依据：T1 watchlist; protocol: protocol。

> 上游摘录（未审读）：Document working-group-based contribution policy (#3514) Require working group approval and modelcontextprotocol org membership before opening pull requests, point non-members to issues and working groups, and summarize the policy in the README.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Point Skills specification links at specification/beta/ (#3466)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/94f4ebc8ecb3764584bc30d5139d57c03692b734)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 51 · 上游时间 2026-11-08T05:01:53Z

入选依据：T1 watchlist; proposal: sep-, specification, extension。

> 上游摘录（未审读）：Point Skills specification links at specification/beta/ (#3466) The Skills extension is Beta under SEP-3392, and ext-skills moves its specification from specification/stable/ to specification/beta/.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [ci: adopt checked squash merges and conventional bot titles](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/1103ff1264dfabe5c5fb3a3ea4ada2769e61cdb1)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 35 · 上游时间 2026-11-04T23:29:29Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：ci: adopt checked squash merges and conventional bot titles

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [build: pin documentation build tools](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/77d4f1afd50e3563dc26cefef106e79c049a4a99)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 35 · 上游时间 2026-11-05T13:00:49Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：build: pin documentation build tools

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Merge main into ci/adopt-checked-squash-merges](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/781687f6c996b7a641b8416de2c0fd5f6fd04b08)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 35 · 上游时间 2026-11-06T18:47:22Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：Merge main into ci/adopt-checked-squash-merges Co-authored-by: den

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [ci: narrow adoption PR to SEP verification](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/ed94711ea227e882ea7c2b3c76c586bf76cda095)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 35 · 上游时间 2026-11-04T23:56:37Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：ci: narrow adoption PR to SEP verification

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [build(deps): bump adm-zip (#3519)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/92e1221b3d915ca3e08b77d36e64a57412363dce)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 5 · 上游时间 2026-11-08T04:55:44Z

入选依据：T1 watchlist; routine maintenance penalty。

> 上游摘录（未审读）：build(deps): bump adm-zip (#3519) Bumps the npm\_and\_yarn group with 1 update in the / directory: \[adm-zip\](https://github.com/cthackers/adm-zip). Removes 'adm-zip' --- updated-dependencies: - dependency-name: adm-zip dependency-version: dependency-type: indirect dependency-group: npm\_and\_yarn ... Signed-off-by: dependabot\[bot\] Co-authored-by: dependabot\[bot\]

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
