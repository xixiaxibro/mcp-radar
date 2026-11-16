# MCP Radar · 2026-11-16 (UTC)

采集时间：2026-11-16T01:17:05+00:00 · 回看窗口：14 天。

这是公开来源的更新索引和选题素材，不是已经审读、复现的技术结论。标题和摘录来自上游；优先级由可见规则计算。

本次窗口内 2445 条记录；本日累计 138 个新增/变更版本；失败端点 1 个；覆盖警告 0 个。

## 覆盖与限制

PR merged 表示代码进入分支，不代表已发布；release 不自动证明符合某协议版本。初次运行只建立窗口基线。

仅跟踪 watchlist 中公开仓库的 PR、指定仓库 issue/commit、release、公开安全公告和订阅源。未提供 API 的社区讨论、社交媒体和完整标准文档变更不在覆盖保证内。RSS 仅提供源当前保留的条目。

- 采集失败：`PrefectHQ/fastmcp` / releases — Unterminated string starting at: line 1 column 688660 (char 688659)

## 重点 PR / 提案

显示 20 / 136 条；全部数据见当日 JSON。

### [docs: stop presenting deprecated features as current on the spec overview pages](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3552)

`modelcontextprotocol/modelcontextprotocol` · **open** · new · 分数 94 · 上游时间 2026-11-15T19:55:09Z

入选依据：T1 watchlist; breaking: deprecat; protocol: protocol; proposal: sep-。

> 上游摘录（未审读）：The architecture and base protocol overview pages are where many people new to MCP start. Both still presented sampling, roots and logging as current features, with no indication that they are deprecated as of '2026-07-28' (SEP-2577). Fixes #3548 ## Architecture page Builds on the branch Lazzaretti proposed in #3548 (their commit is included as-is), which updates the five places the issue lists: - Intro: "context exc

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Runtime enforcement: the Security section's missing layer](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/3538)

`modelcontextprotocol/modelcontextprotocol` · **closed** · updated · 分数 92 · 上游时间 2026-11-15T21:05:30Z

入选依据：T1 watchlist; security: security, authorization; protocol: protocol; proposal: specification。

> 上游摘录（未审读）：The specification's Security and Trust & Safety section states that MCP itself cannot enforce its security principles at the protocol level, and that implementors SHOULD build consent and authorization flows, access controls, and documentation. That leaves the enforcement question to each implementor, with no shared account of what enforcement must look like to hold. Once a host connects an agent to tools, the agent'

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [sep(SEP-2643): Structured Authorization Denials](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2643)

`modelcontextprotocol/modelcontextprotocol` · **open** · updated · 分数 82 · 上游时间 2026-11-15T21:45:04Z

入选依据：T1 watchlist; security: authorization; protocol: protocol, transport; proposal: sep-, proposal; draft PR。

> 上游摘录（未审读）：## Motivation and Context This SEP defines a transport-agnostic authorization denial envelope for the Model Context Protocol. The envelope complements transport-level authorization challenges (HTTP 'WWW-Authenticate' with Protected Resource Metadata), carrying a failure classification, a remediation posture, a retry correlation handle, and an extensible set of structured remediation hints for cases the transport cann

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Output Schema: say how a server can change a tool's 'outputSchema' without breaking clients that cached it](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/3554)

`modelcontextprotocol/modelcontextprotocol` · **open** · new · 分数 78 · 上游时间 2026-11-15T22:50:57Z

入选依据：T1 watchlist; breaking: breaking; protocol: schema。

> 上游摘录（未审读）：The Output Schema section says servers \*\*MUST\*\* return structured results that conform to the schema, and clients \*\*SHOULD\*\* validate them against it. It doesn't say which schema applies when the two sides hold different versions. Clients cache tool lists, so after a server changes a tool, a client can validate a new result against the old schema. What happened to us: our server removed two fields that a tool's 'outp

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add troubleshooting entry for empty inputSchema / reading '\_def'](https://github.com/modelcontextprotocol/typescript-sdk/pull/3188)

`modelcontextprotocol/typescript-sdk` · **open** · new · 分数 78 · 上游时间 2026-11-15T15:57:21Z

入选依据：T1 watchlist; breaking: migration; protocol: schema。

> 上游摘录（未审读）：On v1, passing a ZodObject where a raw shape is expected either crashes tools/list with 'Cannot read properties of null (reading \_def)' (v1 <=1.21) or silently publishes an empty schema (v1 <=1.26). Add troubleshooting entries keyed on both symptoms and a migration-guide warning. Closes #2627.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(fingerprint): add MCP Inspector fingerprint and CVE-2025-49596 rule](https://github.com/Tencent/AI-Infra-Guard/pull/768)

`Tencent/AI-Infra-Guard` · **open** · new · 分数 76 · 上游时间 2026-11-15T21:25:43Z

入选依据：T1 watchlist; security: cve-, ghsa-; protocol: protocol, transport。

> 上游摘录（未审读）：## Summary Adds detection for MCP Inspector ('@modelcontextprotocol/inspector'), the official MCP debugging tool, plus a rule for CVE-2025-49596 / GHSA-7f8r-222p-6f5g. Nothing under 'data/' mentions Inspector today. - 'data/fingerprints/mcp-inspector.yaml': 'GET /config' on the proxy (port 6277) returns 'defaultEnvironment', 'defaultCommand' and 'defaultArgs' but not 'defaultTransport'. - 'data/vuln/mcp-inspector/CVE

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Move OAuth error classification to oauthproto](https://github.com/stacklok/toolhive/pull/7131)

`stacklok/toolhive` · **merged** · updated · 分数 74 · 上游时间 2026-11-14T16:39:01Z

入选依据：T2 watchlist; security: oauth, token; protocol: protocol; merged implementation; verify release separately。

> 上游摘录（未审读）：## Summary The OAuth token-endpoint error predicates lived in 'pkg/auth/oautherr'. Code in 'pkg/authserver' and the DCR probe that classifies upstream failures therefore had to import the client-side 'pkg/auth' tree. As a result, the OAuth protocol and authserver packages cannot be used without 'pkg/auth'. - Move 'IsTransientRetrieveError', 'IsPermanentCredentialError', 'IsRejectedRefreshGrant', and 'IsParseError' to

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(auth): relax revoked\_by FK and persist revocations for trust-mode principals](https://github.com/IBM/mcp-context-forge/pull/6747)

`IBM/mcp-context-forge` · **open** · updated · 分数 72 · 上游时间 2026-11-15T14:31:23Z

入选依据：T2 watchlist; breaking: migration; security: token。

> 上游摘录（未审读）：One idempotent migration ('f7a8b9c0d1e2', parent 'e5f6a7b8c9d0') makes 'TokenRevocation.revoked\_by' nullable and drops the FK to 'email\_users.email' — trust-mode principals have no user row, and the old NOT-NULL FK broke every revocation insert for them (the idle path silently swallowed the failure). The 'revoker' relationship that depended on the FK is removed. All six revocation insert sites now store the canonical

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Restore Marvin labeling and reopen disputed duplicates](https://github.com/PrefectHQ/fastmcp/pull/6495)

`PrefectHQ/fastmcp` · **merged** · new · 分数 66 · 上游时间 2026-11-15T08:14:06Z

入选依据：T1 watchlist; security: token; merged implementation; verify release separately。

> 上游摘录（未审读）：Marvin now returns a structured list of labels. GitHub Actions validates the selection against its allowlist and existing repository labels, then applies the labels to the triggering issue or PR using a separate write token. Duplicate auto-closure now checks the full comment and reaction history. After Marvin closes a duplicate, a new comment from the reporter, a repository contributor, or a maintainer reopens it for

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add release cycle page](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3550)

`modelcontextprotocol/modelcontextprotocol` · **open** · updated · 分数 66 · 上游时间 2026-11-16T01:08:30Z

入选依据：T1 watchlist; protocol: protocol; proposal: sep-。

> 上游摘录（未审读）：Adds 'docs/community/release-cycle.mdx', the release-cycle documentation required by \[SEP-3398\](https://modelcontextprotocol.io/seps/3398-release-cycle-updates) (Reference Implementation, item 2). - Schedule: six-month releases, eight-month cycles, and the two-month overlap, with an example timeline (light and dark SVG) of a March and a September cycle. - Milestones table with the timing and outcome of each milestone

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs(auth): document JWT-trust mode and complete validation gate](https://github.com/IBM/mcp-context-forge/pull/6755)

`IBM/mcp-context-forge` · **open** · updated · 分数 64 · 上游时间 2026-11-15T14:31:24Z

入选依据：T2 watchlist; security: token; protocol: sse。

> 上游摘录（未审读）：Completes Epic 2 (#5885): executable tests for every disabled-with-clear-error row of the feature-mode matrix, the trust-mode documentation sweep, and the validation gate in both modes. Matrix coverage: 20 tests in 'tests/unit/mcpgateway/test\_trust\_mode\_disabled\_surfaces.py' assert BOTH the status code and the exact message for all seven disabled rows (TDD: 17 red first). Only the token-catalog row had landed with #5

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add add-apps-to-host skill for building MCP Apps hosts](https://github.com/modelcontextprotocol/ext-apps/pull/859)

`modelcontextprotocol/ext-apps` · **closed** · new · 分数 64 · 上游时间 2026-11-15T03:39:50Z

入选依据：T2 watchlist; security: security; protocol: protocol。

> 上游摘录（未审读）：## Problem The repo ships skills for building MCP Apps (create-mcp-app, add-app-to-server, convert-web-app, migrate-oai-app). Nothing covers the other side of the protocol: a chat client that wants to render MCP Apps. Host authors have to reverse-engineer examples/basic-host and the spec to learn which pieces to build, in what order, and which security rules are mandatory. Most mistakes happen in the browser parts, t

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(auth): omit scope on refresh unless caller sets one](https://github.com/modelcontextprotocol/rust-sdk/pull/1433)

`modelcontextprotocol/rust-sdk` · **open** · updated · 分数 64 · 上游时间 2026-11-15T18:06:34Z

入选依据：T2 watchlist; security: authorization; protocol: transport。

> 上游摘录（未审读）：fixes #1408 refresh was always sending 'scope' from the stored grant, which some servers (salesforce) reject. rfc 6749 §6 says scope is optional on refresh and leaving it out keeps the original grant. now refresh omits 'scope' unless the caller sets it via 'AuthorizationManager::set\_refresh\_scopes()'. when set, only scopes from the original grant get sent (keeps the #1331 behaviour). if none of them are in the grant,

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(auth): avoid refreshing short-lived access tokens on every call](https://github.com/modelcontextprotocol/rust-sdk/pull/1450)

`modelcontextprotocol/rust-sdk` · **open** · updated · 分数 64 · 上游时间 2026-11-16T00:37:41Z

入选依据：T2 watchlist; security: token; protocol: transport。

> 上游摘录（未审读）：Fixes #1442 ## Problem get\_access\_token refreshes whenever remaining < 30s. Tokens with expires\_in <= 30s are always inside the window, so every call triggers a refresh (and a rotated refresh token each time). ## Change - Buffer is now min(REFRESH\_BUFFER\_SECS, expires\_in / 2), as agreed in the issue. - Added remaining == 0 so expired tokens with expires\_in <= 1 (buffer 0) still refresh/re-auth instead of being return

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(client): cap list\_all\_\* pagination like the MRTR round cap](https://github.com/modelcontextprotocol/rust-sdk/pull/1457)

`modelcontextprotocol/rust-sdk` · **open** · new · 分数 64 · 上游时间 2026-11-15T13:19:15Z

入选依据：T2 watchlist; security: token; protocol: mrtr, pagination。

> 上游摘录（未审读）：Fixes #1456 ## Problem 'list\_all\_tools' / 'list\_all\_prompts' / 'list\_all\_resources' / 'list\_all\_resource\_templates' / 'list\_all\_skills' looped until 'next\_cursor' was 'None'. The spec forbids interpreting the cursor value — '""' is a valid cursor — so a peer that keeps returning one (a fresh token per page, the same token again, or a repeated cursor served from the page cache under a positive 'ttlMs') made the walk a

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Filter SSE list answers on the event stream](https://github.com/stacklok/toolhive/pull/6949)

`stacklok/toolhive` · **open** · updated · 分数 64 · 上游时间 2026-11-14T01:27:53Z

入选依据：T2 watchlist; security: authorization; protocol: streamable, sse。

> 上游摘录（未审读）：Fixes #6926. ## Summary \*\*Why:\*\* Over SSE, list answers (tools, prompts, resources, resource templates, skills) reached the client on the GET event stream, which was not filtered. \*\*What:\*\* Each GET event is now filtered as it arrives, with the same per-entry authorization as the streamable path. The filter is picked from the shape of each result. ## Does this introduce a user-facing change? - \*\*SSE list answers.\*\* B

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Give triage's assess agent public facts about the people on an issue](https://github.com/PrefectHQ/fastmcp/pull/6486)

`PrefectHQ/fastmcp` · **merged** · new · 分数 60 · 上游时间 2026-11-14T01:40:39Z

入选依据：T1 watchlist; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：the assess agent never saw who it was assessing. intake collected each author's login and nothing else, and the prompt told the agent to "check unfamiliar contributors" with commands it has no credential to run. a maintainer skimming an issue sees in a second that the reporter has 3,000 followers, or that the PR author filed the issue an hour before their own fix and opens PRs across dozens of repos. the assess conte

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Add the Events extension with poll and push delivery (SEP-3415)](https://github.com/PrefectHQ/fastmcp/pull/6489)

`PrefectHQ/fastmcp` · **open** · new · 分数 56 · 上游时间 2026-11-14T07:29:09Z

入选依据：T1 watchlist; protocol: protocol; proposal: sep-, proposal, extension; draft PR。

> 上游摘录（未审读）：A server has no way to tell a client that something happened outside a request: an alert fired, a build finished. The Events extension (\[SEP-3415\](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3415), accepted, not yet merged) defines event types a client subscribes to, with poll, push and webhook delivery. This adds poll and push delivery ('events/list', 'events/poll', 'events/stream') as an 'Even

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix: deliver progress notifications that share a read with their response](https://github.com/modelcontextprotocol/typescript-sdk/pull/3023)

`modelcontextprotocol/typescript-sdk` · **open** · updated · 分数 56 · 上游时间 2026-11-15T20:43:30Z

入选依据：T1 watchlist; security: token。

> 上游摘录（未审读）：## Summary Fixes #3018. '\_onnotification' deferred handlers with 'Promise.resolve()', while '\_onresponse' runs synchronously and deletes the matching progress handler. When a progress notification and its response arrive in the same read/turn, the response cleared the handler before the deferred notification ran, so progress was dropped and 'onerror' reported an unknown token. This dispatches notification handlers sy

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(server-legacy): serve the RFC 8414 issuer without a trailing slash](https://github.com/modelcontextprotocol/typescript-sdk/pull/3184)

`modelcontextprotocol/typescript-sdk` · **open** · updated · 分数 56 · 上游时间 2026-11-15T08:08:53Z

入选依据：T1 watchlist; security: oauth, authorization。

> 上游摘录（未审读）：## Summary 'createOAuthMetadata' wrote 'issuer: issuerUrl.href', and 'new URL('https://host').href' normalizes to 'https://host/' — so an authorization server constructed from a slash-less origin string advertised a \*\*slashed\*\* issuer. RFC 8414 §2 forbids a trailing slash on the issuer identifier, and §3.3 requires the metadata 'issuer' to be byte-identical to the URL the well-known document was fetched from. The pra

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 发布与安全公告

显示 0 / 0 条；全部数据见当日 JSON。

本日暂无记录。

## 协议 / 工作组提交

显示 2 / 2 条；全部数据见当日 JSON。

### [feat(blog): draw a share card for every post (#3553)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/2be673cfa63064b243a6016588411343c0f9fdee)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 35 · 上游时间 2026-11-15T21:39:00Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：feat(blog): draw a share card for every post (#3553) Every page on the blog shared one static 'og-image.png': the wordmark on a dark ground. This draws a share card for each post at build time and fills in the image metadata that was missing. ## The card A 1200x630 PNG on the blog's dark ground. It carries the blog's name, the post's title, its date, and its authors one to a line. There is no description on it. The l

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(blog): open search in a dialog and even out the header buttons (#3551)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/4414a49c82d7fcc5f2a2ed9ddfc76139a09c1789)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 35 · 上游时间 2026-11-15T19:26:14Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：feat(blog): open search in a dialog and even out the header buttons (#3551) Two changes to the blog's header and search. ## Header buttons The social icons sat in 32px boxes 4px apart, while search and the theme switch were 40px boxes in their own grid columns with 16px gaps, so those two stood about twice as far apart as the rest. All five are now one row of 32px boxes with 4px gaps, in the same order. On phones the

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
