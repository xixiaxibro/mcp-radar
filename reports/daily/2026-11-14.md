# MCP Radar · 2026-11-14 (UTC)

采集时间：2026-11-14T01:17:16+00:00 · 回看窗口：14 天。

这是公开来源的更新索引和选题素材，不是已经审读、复现的技术结论。标题和摘录来自上游；优先级由可见规则计算。

本次窗口内 2423 条记录；本日累计 203 个新增/变更版本；失败端点 6 个；覆盖警告 0 个。

## 覆盖与限制

PR merged 表示代码进入分支，不代表已发布；release 不自动证明符合某协议版本。初次运行只建立窗口基线。

仅跟踪 watchlist 中公开仓库的 PR、指定仓库 issue/commit、release、公开安全公告和订阅源。未提供 API 的社区讨论、社交媒体和完整标准文档变更不在覆盖保证内。RSS 仅提供源当前保留的条目。

- 采集失败：`awslabs/mcp` / releases — Expecting value: line 1 column 1 (char 0)
- 采集失败：`cloudflare/workers-oauth-provider` / source — The read operation timed out
- 采集失败：`lastmile-ai/mcp-agent` / source — Remote end closed connection without response
- 采集失败：`modelcontextprotocol/kotlin-sdk` / releases — The read operation timed out
- 采集失败：`modelcontextprotocol/servers` / pulls — The read operation timed out
- 采集失败：`stacklok/toolhive` / security-advisories — Unterminated string starting at: line 1 column 54681 (char 54680)

## 重点 PR / 提案

显示 20 / 198 条；全部数据见当日 JSON。

### [(implementation): SEP-2577 - Deprecate Roots, Sampling, and Logging](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/2885)

`modelcontextprotocol/modelcontextprotocol` · **closed** · new · 分数 94 · 上游时间 2026-11-13T13:45:26Z

入选依据：T1 watchlist; breaking: deprecat; protocol: protocol; proposal: sep-。

> 上游摘录（未审读）：### Where was this agreed? https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2577 ### Description Implement \[SEP-2577\](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2577). - \[x\] modelcontextprotocol/typescript-sdk#2195 - \[x\] modelcontextprotocol/csharp-sdk#1588 - \[x\] modelcontextprotocol/go-sdk#995 - \[x\] modelcontextprotocol/java-sdk#1012 - \[ \] modelcontextprotocol/kotlin-sdk#816 -

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Omit app-only ui\_get unless the client advertises MCP Apps](https://github.com/github/github-mcp-server/pull/3687)

`github/github-mcp-server` · **open** · updated · 分数 92 · 上游时间 2026-11-13T17:21:01Z

入选依据：T1 watchlist; security: token; protocol: protocol, stdio; proposal: extension。

> 上游摘录（未审读）：## Summary Do not list the app-only 'ui\_get' tool to clients that lack MCP Apps support, on both the remote (HTTP) server and the local stdio server. ## Why 'ui\_get' is marked '\_meta.ui.visibility: \["app"\]'. Apps hosts hide that from the model; other clients ignore the meta and hand the helper to the model, wasting tokens. A client that supports Apps declares 'extensions\["io.modelcontextprotocol/ui"\]'. The remote ser

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Ignore stray ResourceWarnings in CLI OAuth warning checks](https://github.com/PrefectHQ/fastmcp/pull/6474)

`PrefectHQ/fastmcp` · **merged** · new · 分数 86 · 上游时间 2026-11-13T05:11:19Z

入选依据：T1 watchlist; security: oauth; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：'test\_encrypted\_oauth\_reused\_by\_fresh\_client' failed intermittently on Windows 3.14, on main and on PRs. it records every warning in its block and asserts none, so a 'ResourceWarning' for a localhost socket leaked by an earlier test fails it whenever garbage collection finalizes that socket inside the block. this ignores 'ResourceWarning' there and in the two sibling blocks that make the same assertion; the storage w

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Drop GC ResourceWarnings at the assertion in CLI OAuth warning checks](https://github.com/PrefectHQ/fastmcp/pull/6481)

`PrefectHQ/fastmcp` · **merged** · new · 分数 86 · 上游时间 2026-11-13T14:24:34Z

入选依据：T1 watchlist; security: oauth; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：#6474 didn't close the OAuth warning flake: it failed again on main at 7d0455cbd, the commit that landed it. this time the leaked socket was finalized while 'filterwarnings()' itself was compiling its regex ('re/\_parser.py'), before the 'ResourceWarning' ignore was installed. any allocation inside the block can trigger that GC, so no filter order closes the window. the three blocks now record everything and drop 'Res

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add EU Cyber Resilience Act stewardship guidance](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3526)

`modelcontextprotocol/modelcontextprotocol` · **merged** · updated · 分数 82 · 上游时间 2026-11-13T23:58:30Z

入选依据：T1 watchlist; security: security; proposal: specification; merged implementation; verify release separately。

> 上游摘录（未审读）：Human: @localden \_Requested by \*\*Den\*\* · \[project thread\](https://claude.ai/code/project/chan\_01Bzyr6VAkCeeUXG84MjhGvn?thread=cmsg\_01Bzyr6VAkCeeUXG84MjhGvn5k6yDdsYhrcEf6CJAKPEuC)\_ Add the Linux Foundation EU Cyber Resilience Act (CRA) stewardship notice to the specification repository, which represents the project. - 'SECURITY.md' states that the project's software is ultimately intended for commercial activities and

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Migrate to GitHub REST API version 2026-03-10](https://github.com/github/github-mcp-server/pull/3038)

`github/github-mcp-server` · **open** · updated · 分数 76 · 上游时间 2026-11-13T20:13:52Z

入选依据：T1 watchlist; security: token; protocol: stdio。

> 上游摘录（未审读）：## Summary Use REST API version '2026-03-10' for GitHub.com and GitHub Enterprise Cloud, while keeping GitHub Enterprise Server on '2022-11-28'. Apply the host-aware policy to stdio and per-request REST clients, scope discovery, and GitHub App installation-token requests. ## Why Fixes #3037. The pinned 'go-github/v92 v92.0.0' supports '2026-03-10' but still defaults requests to '2022-11-28'. It exposes a per-request

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(client): deduplicate concurrent OAuth refreshes](https://github.com/modelcontextprotocol/typescript-sdk/pull/2757)

`modelcontextprotocol/typescript-sdk` · **open** · new · 分数 76 · 上游时间 2026-11-13T01:44:57Z

入选依据：T1 watchlist; security: oauth, authorization, token; protocol: sse。

> 上游摘录（未审读）：## Summary Prevent overlapping OAuth refresh calls from redeeming the same rotating refresh token. Equivalent calls sharing a provider share one pending result; calls with different auth options are serialized and execute their own discovery and validation. Authorization-code exchanges and forced reauthorization remain distinct operations. Hosts sharing credentials across processes can implement the optional 'withAut

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(auth): relax revoked\_by FK and persist revocations for trust-mode principals](https://github.com/IBM/mcp-context-forge/pull/6747)

`IBM/mcp-context-forge` · **open** · updated · 分数 72 · 上游时间 2026-11-13T14:52:35Z

入选依据：T2 watchlist; breaking: migration; security: token。

> 上游摘录（未审读）：One idempotent migration ('f7a8b9c0d1e2', parent 'e5f6a7b8c9d0') makes 'TokenRevocation.revoked\_by' nullable and drops the FK to 'email\_users.email' — trust-mode principals have no user row, and the old NOT-NULL FK broke every revocation insert for them (the idle path silently swallowed the failure). The 'revoker' relationship that depended on the FK is removed. All six revocation insert sites now store the canonical

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Updates to conform to section 3.1 of the OAuth 2.1 specification](https://github.com/modelcontextprotocol/python-sdk/pull/3858)

`modelcontextprotocol/python-sdk` · **closed** · new · 分数 72 · 上游时间 2026-11-13T16:42:54Z

入选依据：T1 watchlist; security: oauth, authorization; proposal: specification。

> 上游摘录（未审读）：Fixes #3856 and #2776 Added some helper functions in src/mcp/shared/auth\_utils.py to add, remove and replace query params to a URL and then used those in src/mcp/client/auth/oauth2.py in \_perform\_authorization\_code\_grant to conform to the rules in section 3.1 of the OAuth 2.1 spec. There is one change to check if a fragment has been added to the authorization\_url and if so to reject it. You could also make an argumen

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [SEP-XXXX: Asynchronous Errors](https://github.com/modelcontextprotocol/transports-wg/pull/76)

`modelcontextprotocol/transports-wg` · **open** · new · 分数 72 · 上游时间 2026-11-13T16:36:40Z

入选依据：T1 watchlist; security: authorization; proposal: sep-。

> 上游摘录（未审读）：Based on the feedback on #67 at the 2026-11-06 working group meeting, this SEP extends its error reporting model in two ways: 1. Beyond subscriptions, to any operation the server has already accepted, such as a streamed 'tools/call', a task, or an event subscription 2. Beyond authorization errors ## Motivation and Context Several MCP operations outlive the moment at which a server can refuse them. When a server resta

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add primitive versioning problem statement](https://github.com/modelcontextprotocol/transports-wg/pull/74)

`modelcontextprotocol/transports-wg` · **open** · updated · 分数 68 · 上游时间 2026-11-13T17:03:28Z

入选依据：T1 watchlist; breaking: compatib; protocol: pagination; draft PR。

> 上游摘录（未审读）：Clients can prepare calls from definitions that change before execution, and refreshing can return another incompatible catalog during a rollout. This problem statement covers tool, prompt, resource-template, and skill-content changes, along with paused calls, gateways, pagination, and requests that omit definition references. It records the required behavior and leaves tag scope, adoption, and enforcement open. The

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(sep-1932): DPoP discovery signals (stacked on #528)](https://github.com/modelcontextprotocol/conformance/pull/529)

`modelcontextprotocol/conformance` · **open** · new · 分数 66 · 上游时间 2026-11-13T09:41:51Z

入选依据：T1 watchlist; protocol: protocol, sse; proposal: sep-。

> 上游摘录（未审读）：Stacked on #528 -> #527 -> #395. Rebase onto 'main' once #528, #527, and #395 merge. Review the commits after '9771ecb' ('5d213b9' onward). Everything before that belongs to the PRs below it in the stack. The grading follows the "MCP Server DPoP Advertisement" section of SEP-1932 proposed in modelcontextprotocol/ext-auth#33, and the yaml rows quote it word for word. ## What each check asserts #395 checks that a malfo

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix: send error on SSE disconnect without resumption token](https://github.com/modelcontextprotocol/python-sdk/pull/1838)

`modelcontextprotocol/python-sdk` · **closed** · new · 分数 66 · 上游时间 2026-11-13T14:22:18Z

入选依据：T1 watchlist; security: token; protocol: sse; draft PR。

> 上游摘录（未审读）：## Summary Fixes #1811 When an SSE stream disconnects before the server sends any events with IDs (no resumption token), the client now sends a JSONRPCError to the session layer instead of hanging indefinitely. ## Changes - Added error handling in '\_handle\_sse\_response' for streams that close without sending resumption tokens - Error response uses 'CONNECTION\_CLOSED' (-32000) error code with descriptive message - Add

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [SEP-XXXX: Required Capabilities for Tools](https://github.com/modelcontextprotocol/transports-wg/pull/31)

`modelcontextprotocol/transports-wg` · **open** · updated · 分数 66 · 上游时间 2026-11-13T03:35:08Z

入选依据：T1 watchlist; protocol: protocol, capabilit; proposal: sep-。

> 上游摘录（未审读）：This is a draft SEP addressing cross-request capability coordination for the per-request client capabilities introduced by \[SEP-2575\](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/2575). ## Motivation and Context SEP-2575 moves client capabilities from a single initialization handshake to per-request declarations in '\_meta', but some requests (notably 'tools/list') need to know what capabilities

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs(auth): document JWT-trust mode and complete validation gate](https://github.com/IBM/mcp-context-forge/pull/6755)

`IBM/mcp-context-forge` · **open** · updated · 分数 64 · 上游时间 2026-11-13T14:52:51Z

入选依据：T2 watchlist; security: token; protocol: sse。

> 上游摘录（未审读）：Completes Epic 2 (#5885): executable tests for every disabled-with-clear-error row of the feature-mode matrix, the trust-mode documentation sweep, and the validation gate in both modes. Matrix coverage: 20 tests in 'tests/unit/mcpgateway/test\_trust\_mode\_disabled\_surfaces.py' assert BOTH the status code and the exact message for all seven disabled rows (TDD: 17 red first). Only the token-catalog row had landed with #5

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [mcp: reject unencoded non-ASCII characters in Mcp-Param headers](https://github.com/modelcontextprotocol/go-sdk/pull/1521)

`modelcontextprotocol/go-sdk` · **merged** · updated · 分数 64 · 上游时间 2026-11-13T12:00:59Z

入选依据：T2 watchlist; protocol: protocol; proposal: specification; merged implementation; verify release separately。

> 上游摘录（未审读）：Fixes #1520. 'validateParamHeaders' decodes an 'Mcp-Param-{Name}' value when it contains the '=?base64?...?=' wrapper, and otherwise compares it directly with the body value. Therefore, with protocol version 2026-07-28, a value with characters outside visible ASCII, sent unencoded, is accepted if it matches the body argument: 'Mcp-Param-Region: café' with '"region": "café"' runs the tool. The specification requires t

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(auth): omit scope on refresh unless caller sets one](https://github.com/modelcontextprotocol/rust-sdk/pull/1433)

`modelcontextprotocol/rust-sdk` · **open** · updated · 分数 64 · 上游时间 2026-11-13T22:53:18Z

入选依据：T2 watchlist; security: authorization; protocol: transport。

> 上游摘录（未审读）：fixes #1408 refresh was always sending 'scope' from the stored grant, which some servers (salesforce) reject. rfc 6749 §6 says scope is optional on refresh and leaving it out keeps the original grant. now refresh omits 'scope' unless the caller sets it via 'AuthorizationManager::set\_refresh\_scopes()'. when set, only scopes from the original grant get sent (keeps the #1331 behaviour). if none of them are in the grant,

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(auth): avoid refreshing short-lived access tokens on every call](https://github.com/modelcontextprotocol/rust-sdk/pull/1450)

`modelcontextprotocol/rust-sdk` · **open** · new · 分数 64 · 上游时间 2026-11-13T19:04:12Z

入选依据：T2 watchlist; security: token; protocol: transport。

> 上游摘录（未审读）：Fixes #1442 ## Problem get\_access\_token refreshes whenever remaining < 30s. Tokens with expires\_in <= 30s are always inside the window, so every call triggers a refresh (and a rotated refresh token each time). ## Change - Buffer is now min(REFRESH\_BUFFER\_SECS, expires\_in / 2), as agreed in the issue. - Added remaining == 0 so expired tokens with expires\_in <= 1 (buffer 0) still refresh/re-auth instead of being return

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Filter SSE list answers on the event stream](https://github.com/stacklok/toolhive/pull/6949)

`stacklok/toolhive` · **open** · updated · 分数 64 · 上游时间 2026-11-14T00:52:09Z

入选依据：T2 watchlist; security: authorization; protocol: streamable, sse。

> 上游摘录（未审读）：Fixes #6926. ## Summary \*\*Why:\*\* Over SSE, list answers (tools, prompts, resources, resource templates, skills) reached the client on the GET event stream, which was not filtered. \*\*What:\*\* Each GET event is now filtered as it arrives, with the same per-entry authorization as the streamable path. The filter is picked from the shape of each result. ## Does this introduce a user-facing change? - \*\*SSE list answers.\*\* B

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Move OAuth error classification to oauthproto](https://github.com/stacklok/toolhive/pull/7131)

`stacklok/toolhive` · **open** · new · 分数 64 · 上游时间 2026-11-13T13:34:12Z

入选依据：T2 watchlist; security: oauth, token; protocol: protocol。

> 上游摘录（未审读）：## Summary The OAuth token-endpoint error predicates lived in 'pkg/auth/oautherr'. Code in 'pkg/authserver' and the DCR probe that classifies upstream failures therefore had to import the client-side 'pkg/auth' tree. As a result, the OAuth protocol and authserver packages cannot be used without 'pkg/auth'. - Move 'IsTransientRetrieveError', 'IsPermanentCredentialError', 'IsRejectedRefreshGrant', and 'IsParseError' to

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 发布与安全公告

显示 3 / 3 条；全部数据见当日 JSON。

### [v2.2.0-M2](https://github.com/modelcontextprotocol/java-sdk/releases/tag/v2.2.0-M2)

`modelcontextprotocol/java-sdk` · **prerelease** · new · 分数 81 · 上游时间 2026-11-13T18:31:51Z

入选依据：T3 watchlist; breaking: breaking; protocol: protocol, capabilit; release。

> 上游摘录（未审读）：## What's Changed ### ⚠️ Breaking changes This affects the modern server (2026-07-28 preview).: \* Return a handler from 'find' in modern server repositories by @chemicL in https://github.com/modelcontextprotocol/java-sdk/pull/1282 ### 🚀 New features These affect the modern server (2026-07-28 preview).: \* Enforce required client capabilities in the modern server by @chemicL in https://github.com/modelcontextprotocol/j

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v0.65.0](https://github.com/stacklok/toolhive/releases/tag/v0.65.0)

`stacklok/toolhive` · **published** · new · 分数 63 · 上游时间 2026-11-13T11:45:54Z

入选依据：T2 watchlist; protocol: sse; release。

> 上游摘录（未审读）：## What's Changed \* Allow clock skew on private\_key\_jwt assertions by @jhrozek in https://github.com/stacklok/toolhive/pull/7088 \* Record trace and span IDs on audit events by @reyortiz3 in https://github.com/stacklok/toolhive/pull/7102 \* Borrow caller-supplied authserver storage by @jhrozek in https://github.com/stacklok/toolhive/pull/7104 \* Decouple DCR keys from auth storage by @jhrozek in https://github.com/stack

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v4.2.0: Mad Skills](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.2.0)

`PrefectHQ/fastmcp` · **published** · new · 分数 55 · 上游时间 2026-11-14T00:12:23Z

入选依据：T1 watchlist; release。

> 上游摘录（未审读）：FastMCP 4.2 serves agent skills from the server. A skill used to live in a folder on each machine, so every agent kept its own copy and an update meant asking everyone to reinstall. Now the server holds one copy next to the tools the skill describes, and a deploy updates every agent that reads it. '''python from fastmcp import FastMCP, Skill from fastmcp.skills.provider import SkillCatalogProvider deploy = Skill.from

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 协议 / 工作组提交

显示 2 / 2 条；全部数据见当日 JSON。

### [docs: add EU Cyber Resilience Act stewardship guidance (#3526)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/122e27e869b71a7947661b60c1cb10dc512346fa)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 77 · 上游时间 2026-11-13T23:58:26Z

入选依据：T1 watchlist; security: security; proposal: specification。

> 上游摘录（未审读）：docs: add EU Cyber Resilience Act stewardship guidance (#3526) Human: @localden \_Requested by \*\*Den\*\* · \[project thread\](https://claude.ai/code/project/chan\_01Bzyr6VAkCeeUXG84MjhGvn?thread=cmsg\_01Bzyr6VAkCeeUXG84MjhGvn5k6yDdsYhrcEf6CJAKPEuC)\_ Add the Linux Foundation EU Cyber Resilience Act (CRA) stewardship notice to the specification repository, which represents the project. - 'SECURITY.md' states that the project'

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [ci: build and validate website content (#3509)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/0175d20f8b2c49e0402c37c37ed39ae2be47277e)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 55 · 上游时间 2026-11-14T00:02:45Z

入选依据：T1 watchlist; protocol: schema。

> 上游摘录（未审读）：ci: build and validate website content (#3509) Adds a read-only CI job that validates source and runs the existing 'generate' and 'check' commands to confirm documentation builds successfully. The generated output is discarded. Makes schema generator failures and malformed MDX fail the build. Based on #3508; merge that PR first, then retarget this PR to 'main'.

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
