# MCP Radar · 2026-11-27 (UTC)

采集时间：2026-11-27T01:21:10+00:00 · 回看窗口：14 天。

这是公开来源的更新索引和选题素材，不是已经审读、复现的技术结论。标题和摘录来自上游；优先级由可见规则计算。

本次窗口内 476 条记录；本日累计 104 个新增/变更版本；失败端点 38 个；覆盖警告 1 个。

## 覆盖与限制

PR merged 表示代码进入分支，不代表已发布；release 不自动证明符合某协议版本。初次运行只建立窗口基线。

仅跟踪 watchlist 中公开仓库的 PR、指定仓库 issue/commit、release、公开安全公告和订阅源。未提供 API 的社区讨论、社交媒体和完整标准文档变更不在覆盖保证内。RSS 仅提供源当前保留的条目。

- 采集失败：`IBM/mcp-context-forge` / source — The read operation timed out
- 采集失败：`PrefectHQ/fastmcp` / source — The read operation timed out
- 采集失败：`Tencent/AI-Infra-Guard` / pulls — The read operation timed out
- 采集失败：`awslabs/mcp` / source — The read operation timed out
- 采集失败：`cloudflare-mcp` / source — Network error from blog.cloudflare.com/rss/
- 采集失败：`cloudflare/agents` / pulls — The read operation timed out
- 采集失败：`cloudflare/agents` / releases — Remote end closed connection without response
- 采集失败：`cloudflare/workers-oauth-provider` / pulls — The read operation timed out
- 采集失败：`cloudflare/workers-sdk` / pulls — Remote end closed connection without response
- 采集失败：`getsentry/toolkit` / pulls — The read operation timed out
- 采集失败：`mcp-official-blog` / source — Network error from blog.modelcontextprotocol.io/index.xml
- 采集失败：`microsoft/playwright-mcp` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/agents-wg` / commits — The read operation timed out
- 采集失败：`modelcontextprotocol/agents-wg` / releases — The read operation timed out
- 采集失败：`modelcontextprotocol/conformance` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/csharp-sdk` / releases — Remote end closed connection without response
- 采集失败：`modelcontextprotocol/ext-apps` / source — The read operation timed out
- 采集失败：`modelcontextprotocol/ext-skills` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/ext-skills` / releases — The read operation timed out
- 采集失败：`modelcontextprotocol/go-sdk` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/go-sdk` / security-advisories — The read operation timed out
- 采集失败：`modelcontextprotocol/inspector` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/kotlin-sdk` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/mcpb` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/modelcontextprotocol` / issues — The read operation timed out
- 采集失败：`modelcontextprotocol/modelcontextprotocol` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/php-sdk` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/python-sdk` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/registry` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/registry` / releases — The read operation timed out
- 采集失败：`modelcontextprotocol/ruby-sdk` / security-advisories — The read operation timed out
- 采集失败：`modelcontextprotocol/rust-sdk` / source — The read operation timed out
- 采集失败：`modelcontextprotocol/servers` / security-advisories — The read operation timed out
- 采集失败：`modelcontextprotocol/swift-sdk` / releases — The read operation timed out
- 采集失败：`modelcontextprotocol/typescript-sdk` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/typescript-sdk` / releases — The read operation timed out
- 采集失败：`stacklok/toolhive` / pulls — The read operation timed out
- 采集失败：`stacklok/toolhive` / releases — The read operation timed out
- 覆盖提示：`modelcontextprotocol/agents-wg` / source — Repository renamed/redirected to modelcontextprotocol/agents-ig

## 重点 PR / 提案

显示 20 / 97 条；全部数据见当日 JSON。

### [\[P8\] oauth: issuer checks, application\_type, AS migration (SEP-2468/837/2352)](https://github.com/modelcontextprotocol/swift-sdk/pull/363)

`modelcontextprotocol/swift-sdk` · **merged** · new · 分数 108 · 上游时间 2026-11-25T12:38:06Z

入选依据：T3 watchlist; breaking: migration; security: oauth; protocol: conformance, mrtr; proposal: sep-; merged implementation; verify release separately。

> 上游摘录（未审读）：\| \| \| \|---\|---\| \| Part \| P8 of P0–P35, merged into 'rel/1.0.0' in order (previous: P7 (#364) · next: P10 (#362)) \| \| Branch \| 'conformance/p8-oauth' \| \| Base \| 'conformance/p7-mrtr' (stacked: GitHub retargets this PR to 'rel/1.0.0' when the previous part merges) \| \| Commits \| '4f1f67d' oauth: issuer checks, application\_type, AS migration (SEP-2468/837/2352) '82ab1d5' oauth: review fixes 'c6762d9' oauth: compute the P

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[P31\] server cards: serve and fetch Server Cards (SEP-2127)](https://github.com/modelcontextprotocol/swift-sdk/pull/340)

`modelcontextprotocol/swift-sdk` · **merged** · new · 分数 82 · 上游时间 2026-11-25T12:54:19Z

入选依据：T3 watchlist; breaking: deprecat; protocol: conformance; proposal: sep-; merged implementation; verify release separately。

> 上游摘录（未审读）：\| \| \| \|---\|---\| \| Part \| P31 of P0–P35, merged into 'rel/1.0.0' in order (previous: P30 (#341) · next: P32 (#339)) \| \| Branch \| 'conformance/p31-server-cards' \| \| Base \| 'conformance/p30-spec-deprecations' (stacked: GitHub retargets this PR to 'rel/1.0.0' when the previous part merges) \| \| Commits \| 'b433530' server cards: serve and fetch Server Cards (SEP-2127) '9f193d1' server cards: review fixes '90db10a' server c

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[P30\] deprecations: roots, sampling, logging and includeContext (SEP-2577, SEP-2596)](https://github.com/modelcontextprotocol/swift-sdk/pull/341)

`modelcontextprotocol/swift-sdk` · **merged** · new · 分数 82 · 上游时间 2026-11-25T12:53:44Z

入选依据：T3 watchlist; breaking: deprecat; protocol: conformance; proposal: sep-; merged implementation; verify release separately。

> 上游摘录（未审读）：\| \| \| \|---\|---\| \| Part \| P30 of P0–P35, merged into 'rel/1.0.0' in order (previous: P29 (#342) · next: P31 (#340)) \| \| Branch \| 'conformance/p30-spec-deprecations' \| \| Base \| 'conformance/p29-tool-names' (stacked: GitHub retargets this PR to 'rel/1.0.0' when the previous part merges) \| \| Commits \| 'a79cda4' deprecations: roots, sampling, logging and includeContext (SEP-2577, SEP-2596) 'de7b2f3' deprecations: second-p

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix: build the tests with Swift 6.3 and silence deprecation warnings](https://github.com/modelcontextprotocol/swift-sdk/pull/373)

`modelcontextprotocol/swift-sdk` · **merged** · new · 分数 82 · 上游时间 2026-11-26T15:45:42Z

入选依据：T3 watchlist; breaking: deprecat; protocol: protocol; proposal: sep-; merged implementation; verify release separately。

> 上游摘录（未审读）：The 'macos-latest' and 'Apple platforms (iOS)' jobs (Xcode 26.6, Swift 6.3.3) fail to compile 'MCPTests'. Every leg also prints hundreds of deprecation warnings since roots, sampling and logging were deprecated (SEP-2577). This PR fixes both. It changes tests, snippets and the server guide only. No library code or public API changes. ### Errors (Swift 6.3) - 'URLProtocol' is not 'Sendable', so the '@unchecked Sendabl

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[P13\] oauth: DPoP-bound tokens (RFC 9449, SEP-1932)](https://github.com/modelcontextprotocol/swift-sdk/pull/358)

`modelcontextprotocol/swift-sdk` · **merged** · new · 分数 80 · 上游时间 2026-11-25T12:40:55Z

入选依据：T3 watchlist; security: oauth, token; protocol: conformance; proposal: sep-; merged implementation; verify release separately。

> 上游摘录（未审读）：\| \| \| \|---\|---\| \| Part \| P13 of P0–P35, merged into 'rel/1.0.0' in order (previous: P12 (#359) · next: P14 (#357)) \| \| Branch \| 'conformance/p13-dpop' \| \| Base \| 'conformance/p12-enterprise-auth' (stacked: GitHub retargets this PR to 'rel/1.0.0' when the previous part merges) \| \| Commits \| '0679427' oauth: DPoP-bound tokens (RFC 9449, SEP-1932) '7e18ecf' oauth: review fixes '77f5f7d' oauth: second-pass review fixes '

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Add message field to ProgressNotification](https://github.com/modelcontextprotocol/java-sdk/pull/183)

`modelcontextprotocol/java-sdk` · **closed** · new · 分数 72 · 上游时间 2026-11-26T14:12:08Z

入选依据：T3 watchlist; breaking: breaking; protocol: protocol, schema; proposal: specification。

> 上游摘录（未审读）：Add message field to ProgressNotification https://modelcontextprotocol.io/specification/2025-03-26/changelog#other-schema-changes ## Motivation and Context ## How Has This Been Tested? ## Breaking Changes ## Types of changes - \[ \] Bug fix (non-breaking change which fixes an issue) - \[ \] New feature (non-breaking change which adds functionality) - \[ \] Breaking change (fix or feature that would cause existing functiona

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [add AudioContent to McpSchema](https://github.com/modelcontextprotocol/java-sdk/pull/184)

`modelcontextprotocol/java-sdk` · **closed** · new · 分数 72 · 上游时间 2026-11-26T14:11:46Z

入选依据：T3 watchlist; breaking: breaking; protocol: protocol, schema; proposal: specification。

> 上游摘录（未审读）：add AudioContent to McpSchema https://modelcontextprotocol.io/specification/2025-03-26/changelog#other-schema-changes ## Motivation and Context ## How Has This Been Tested? ## Breaking Changes ## Types of changes - \[ \] Bug fix (non-breaking change which fixes an issue) - \[ \] New feature (non-breaking change which adds functionality) - \[ \] Breaking change (fix or feature that would cause existing functionality to chan

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(everything): serve the Events extension (poll and push) on 2026-07-28](https://github.com/modelcontextprotocol/servers/pull/5652)

`modelcontextprotocol/servers` · **merged** · updated · 分数 64 · 上游时间 2026-11-25T05:13:06Z

入选依据：T2 watchlist; protocol: protocol; proposal: sep-, extension; merged implementation; verify release separately。

> 上游摘录（未审读）：Closes #5651 ## Description The everything server now serves the Events extension ('io.modelcontextprotocol/events', \[SEP-3415\](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/3415-events-extension.md), Beta) on protocol version 2026-07-28, with \*\*poll\*\* and \*\*push\*\* delivery. The SDK has no server-side Events support yet (modelcontextprotocol/typescript-sdk#3209 is a draft), so 'server/ev

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[P15\] interop: matrix against the Go and Python SDKs](https://github.com/modelcontextprotocol/swift-sdk/pull/356)

`modelcontextprotocol/swift-sdk` · **merged** · new · 分数 64 · 上游时间 2026-11-25T12:42:32Z

入选依据：T3 watchlist; security: oauth; protocol: conformance; merged implementation; verify release separately。

> 上游摘录（未审读）：\| \| \| \|---\|---\| \| Part \| P15 of P0–P35, merged into 'rel/1.0.0' in order (previous: P14 (#357) · next: P16 (#355)) \| \| Branch \| 'conformance/p15-interop' \| \| Base \| 'conformance/oauth-dpop-validation' (stacked: GitHub retargets this PR to 'rel/1.0.0' when the previous part merges) \| \| Commits \| '8864ff6' interop: matrix against the Go and Python SDKs '1abeca1' interop: review fixes '1d64122' interop: second-pass revi

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[P14\] Fix four client auth findings from testing against independent servers](https://github.com/modelcontextprotocol/swift-sdk/pull/357)

`modelcontextprotocol/swift-sdk` · **merged** · new · 分数 64 · 上游时间 2026-11-25T12:41:55Z

入选依据：T3 watchlist; security: oauth, authorization; protocol: timeout, conformance; merged implementation; verify release separately。

> 上游摘录（未审读）：\| \| \| \|---\|---\| \| Part \| P14 of P0–P35, merged into 'rel/1.0.0' in order (previous: P13 (#358) · next: P15 (#356)) \| \| Branch \| 'conformance/oauth-dpop-validation' \| \| Base \| 'conformance/p13-dpop' (stacked: GitHub retargets this PR to 'rel/1.0.0' when the previous part merges) \| \| Commits \| 'd0945a8' fix: Don't count authorization time against discoveryTimeout '457a3d2' fix: Throw registrationInformationRequired wit

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[P12\] oauth: jwt-bearer grant, token exchange, enterprise-managed authorization](https://github.com/modelcontextprotocol/swift-sdk/pull/359)

`modelcontextprotocol/swift-sdk` · **merged** · new · 分数 64 · 上游时间 2026-11-25T12:40:27Z

入选依据：T3 watchlist; security: oauth, authorization, token; protocol: conformance; merged implementation; verify release separately。

> 上游摘录（未审读）：\| \| \| \|---\|---\| \| Part \| P12 of P0–P35, merged into 'rel/1.0.0' in order (previous: P11 (#360) · next: P13 (#358)) \| \| Branch \| 'conformance/p12-enterprise-auth' \| \| Base \| 'conformance/p11-fixes' (stacked: GitHub retargets this PR to 'rel/1.0.0' when the previous part merges) \| \| Commits \| '68e693f' oauth: jwt-bearer grant, token exchange, enterprise-managed authorization '9431917' oauth: review fixes '47a76d3' oaut

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[P11\] fix: request lifecycle, server replies, OAuth hardening](https://github.com/modelcontextprotocol/swift-sdk/pull/360)

`modelcontextprotocol/swift-sdk` · **merged** · new · 分数 64 · 上游时间 2026-11-25T12:40:07Z

入选依据：T3 watchlist; security: oauth; protocol: lifecycle, conformance; merged implementation; verify release separately。

> 上游摘录（未审读）：\| \| \| \|---\|---\| \| Part \| P11 of P0–P35, merged into 'rel/1.0.0' in order (previous: P9 (#361) · next: P12 (#359)) \| \| Branch \| 'conformance/p11-fixes' \| \| Base \| 'conformance/p9-flip' (stacked: GitHub retargets this PR to 'rel/1.0.0' when the previous part merges) \| \| Commits \| 'f00b681' fix: request lifecycle, server replies, OAuth hardening '3175667' fix: review fixes '6cb3f9f' client: fail pending requests when th

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[P10\] docs: go-sdk layout, feature guides, design notes and process docs](https://github.com/modelcontextprotocol/swift-sdk/pull/362)

`modelcontextprotocol/swift-sdk` · **merged** · new · 分数 64 · 上游时间 2026-11-25T12:39:09Z

入选依据：T3 watchlist; security: oauth; protocol: conformance; merged implementation; verify release separately。

> 上游摘录（未审读）：\| \| \| \|---\|---\| \| Part \| P10 of P0–P35, merged into 'rel/1.0.0' in order (previous: P8 (#363) · next: P9 (#361)) \| \| Branch \| 'conformance/p10-docs' \| \| Base \| 'conformance/p8-oauth' (stacked: GitHub retargets this PR to 'rel/1.0.0' when the previous part merges) \| \| Commits \| 'd2efd2e' docs: go-sdk layout, feature guides, design notes and process docs 'a25ba95' docs: review fixes '90a0bb7' docs: second-pass review f

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add go install as a first-class local install method](https://github.com/github/github-mcp-server/pull/3745)

`github/github-mcp-server` · **open** · updated · 分数 56 · 上游时间 2026-11-26T10:01:34Z

入选依据：T1 watchlist; security: oauth。

> 上游摘录（未审读）：## Summary - Documents 'go install github.com/github/github-mcp-server/v2/cmd/github-mcp-server@latest' as a first-class way to run the local server without Docker. - Keeps 'go build' from a checkout for contributors who need embedded VCS metadata. - Points to the native-binary OAuth flow. Fixes #2364 ## Notes The issue suggested 'github.com/github/github-mcp-server/cmd/...@latest'. That resolves to the pre-v2 module

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[Copilot Dreaming\] Avoid invalid setup and tool use; remove misleading prerequisites](https://github.com/github/github-mcp-server/pull/3954)

`github/github-mcp-server` · **open** · new · 分数 56 · 上游时间 2026-11-26T05:55:57Z

入选依据：T1 watchlist; security: token。

> 上游摘录（未审读）：## 🧠 How this helps Copilot Development guidance can otherwise select no test, point to a retired REST mock, or require unnecessary personal-token setup. Using the supported testing and authentication contracts avoids those misleading starting points. Workflow diagnosis can mistake a partial failed-log result for the whole run. Bounded coverage and a route to other jobs avoid that assumption; removing a duplicate one

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Add Actionable Denials as an experimental extension](https://github.com/modelcontextprotocol/ext-auth/pull/43)

`modelcontextprotocol/ext-auth` · **open** · new · 分数 56 · 上游时间 2026-11-26T17:13:03Z

入选依据：T1 watchlist; protocol: protocol; proposal: sep-, proposal, specification; draft PR。

> 上游摘录（未审读）：Brings Actionable Denials to 'specification/experimental/actionable-denials.mdx', as an Experimental extension under \[SEP-3392\](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3392). The proposals are \[SEP-2643\](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2643) and \[SEP-2848\](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2848). - Takes the Abstract, Specific

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix: make initialize idempotent instead of erroring on repeat calls](https://github.com/modelcontextprotocol/swift-sdk/pull/257)

`modelcontextprotocol/swift-sdk` · **closed** · new · 分数 56 · 上游时间 2026-11-25T16:31:10Z

入选依据：T3 watchlist; breaking: breaking; protocol: protocol, negotiat。

> 上游摘录（未审读）：Repeated 'initialize' requests previously failed with "Server is already initialized", breaking stateless HTTP servers and clients that retry initialization. Per the MCP spec, initialize should be safe to call again, so the server now re-negotiates and returns a fresh result instead of throwing. Fixes modelcontextprotocol/swift-sdk#219 Fixes modelcontextprotocol/swift-sdk#144 ## Motivation and Context Stateless HTTP

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Validate OAuth issuers and registration metadata](https://github.com/modelcontextprotocol/swift-sdk/pull/293)

`modelcontextprotocol/swift-sdk` · **closed** · updated · 分数 54 · 上游时间 2026-11-25T15:33:06Z

入选依据：T3 watchlist; security: oauth, authorization; protocol: sse。

> 上游摘录（未审读）：Checks OAuth issuer metadata and callback issuers before using an authorization code. It also sends the client application type during registration and starts a new registration when the authorization server changes. Related to #231 and #242. The branch is updated to current 'main' and includes the Ubuntu CI setup and client-test timing fixes shared with #307. Tests: 561 Swift tests and DocC passed locally before thi

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[P32\] apps: serve and read MCP Apps views (SEP-1865)](https://github.com/modelcontextprotocol/swift-sdk/pull/339)

`modelcontextprotocol/swift-sdk` · **merged** · new · 分数 54 · 上游时间 2026-11-25T12:54:51Z

入选依据：T3 watchlist; protocol: conformance; proposal: sep-; merged implementation; verify release separately。

> 上游摘录（未审读）：\| \| \| \|---\|---\| \| Part \| P32 of P0–P35, merged into 'rel/1.0.0' in order (previous: P31 (#340) · next: P33 (#338)) \| \| Branch \| 'conformance/p32-apps' \| \| Base \| 'conformance/p31-server-cards' (stacked: GitHub retargets this PR to 'rel/1.0.0' when the previous part merges) \| \| Commits \| '2f3cbb2' apps: serve and read MCP Apps views (SEP-1865) 'b88dd46' apps: review fixes '001a313' apps: second-pass review fixes '40f9

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[P29\] tools: the tool name format (SEP-986)](https://github.com/modelcontextprotocol/swift-sdk/pull/342)

`modelcontextprotocol/swift-sdk` · **merged** · new · 分数 54 · 上游时间 2026-11-25T12:53:17Z

入选依据：T3 watchlist; protocol: conformance; proposal: sep-; merged implementation; verify release separately。

> 上游摘录（未审读）：\| \| \| \|---\|---\| \| Part \| P29 of P0–P35, merged into 'rel/1.0.0' in order (previous: P28 (#343) · next: P30 (#341)) \| \| Branch \| 'conformance/p29-tool-names' \| \| Base \| 'conformance/p28-request-association-warning' (stacked: GitHub retargets this PR to 'rel/1.0.0' when the previous part merges) \| \| Commits \| '069d38c' tools: the tool name format (SEP-986) 'f6ffc28' tools: review fixes '046cb64' tools: second-pass revi

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 发布与安全公告

显示 3 / 3 条；全部数据见当日 JSON。

### [AI-Infra-Guard v4.6.12](https://github.com/Tencent/AI-Infra-Guard/releases/tag/v4.6.12)

`Tencent/AI-Infra-Guard` · **published** · new · 分数 109 · 上游时间 2026-11-26T04:03:59Z

入选依据：T1 watchlist; breaking: breaking; security: security; release。

> 上游摘录（未审读）：## \[v4.6.12\] - 2026-11-26 ### Added - \*\*Agent-Scan\*\*: Add sandboxed --repo source tools and Stage 1 profiling (PR #812, 1ccb658d) - \*\*Skill-Scan\*\*: Add baseline-anchored semantic slicing for pure semantic files (PR #809, cae6e04d) - \*\*MCP\*\*: Add cross-server tool shadowing detection rule (PR #790, 0f53daeb) - \*\*Prompt-Security\*\*: Add RefusalLadderJailbreaking multi-turn attack (PR #780, 8e5e2fd7) ### Fixed - \*\*Docker

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [v1.4.0](https://github.com/cloudflare/workers-oauth-provider/releases/tag/v1.4.0)

`cloudflare/workers-oauth-provider` · **published** · new · 分数 81 · 上游时间 2026-11-25T21:54:08Z

入选依据：T1 watchlist; security: oauth, authorization; release。

> 上游摘录（未审读）：### Minor Changes - \[#434\](https://github.com/cloudflare/workers-oauth-provider/pull/434) \['151220e'\](https://github.com/cloudflare/workers-oauth-provider/commit/151220e1cdf3c2e7528ef5a25f320eb981e37379) Thanks \[@mattzcarey\](https://github.com/mattzcarey)! - A new authorization from a Client ID Metadata Document client no longer revokes the user's other grants from that client. 'revokeExistingGrants' now defaults to

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [http@1.0.0](https://github.com/getsentry/toolkit/releases/tag/http%401.0.0)

`getsentry/toolkit` · **published** · new · 分数 43 · 上游时间 2026-11-27T00:53:46Z

入选依据：T2 watchlist; release。

> 上游摘录（未审读）：### New Features ✨ #### HTTP - Make CacheStore.deleteMatching optional by @BYK with @sentry-junior in \[#2550\](https://github.com/getsentry/toolkit/pull/2550) - Add @sentry/http and move CLI and MCP caching and retries onto it by @BYK with @sentry-junior in \[#2509\](https://github.com/getsentry/toolkit/pull/2509) #### Other - (mcp) Remove search\_attributes experimental flag by @nikkikapadia in \[#2251\](https://github.co

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 协议 / 工作组提交

显示 4 / 4 条；全部数据见当日 JSON。

### [docs: add release cycle page (#3550)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/024d5255eb4466ba4fab21e044b5ba84d6a79327)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 71 · 上游时间 2026-11-26T20:04:01Z

入选依据：T1 watchlist; protocol: protocol; proposal: sep-。

> 上游摘录（未审读）：docs: add release cycle page (#3550) Adds 'docs/community/release-cycle.mdx', the release-cycle documentation required by \[SEP-3398\](https://modelcontextprotocol.io/seps/3398-release-cycle-updates) (Reference Implementation, item 2), and aligns the governance pages that SEP-3398 changes. ## Release cycle page - Schedule: six-month releases, eight-month cycles, and the two-month overlap, with an example timeline (ligh

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [build(deps-dev): bump mint from 4.3.34 to 4.3.75 (#3580)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/bdfe59b8cb25b2182d7617b9426455feb406bc1b)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 59 · 上游时间 2026-11-26T19:13:40Z

入选依据：T1 watchlist; breaking: compatib; security: security; routine maintenance penalty。

> 上游摘录（未审读）：build(deps-dev): bump mint from 4.3.34 to 4.3.75 (#3580) Bumps \[mint\](https://github.com/orgs/mintlify) from 4.3.34 to 4.3.75. Commits See full diff in compare view \[!\[Dependabot compatibility score\](https://dependabot-badges.githubapp.com/badges/compatibility\_score?dependency-name=mint&package-manager=npm\_and\_yarn&previous-version=4.3.34&new-version=4.3.75)\](https://docs.github.com/en/github/managing-security-vulner

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [build(deps-dev): bump typescript-eslint from 8.72.2 to 8.73.0 (#3579)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/29336ab3a9a9ae77152c94a8b35a9e61f3ea69da)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 5 · 上游时间 2026-11-26T19:12:55Z

入选依据：T1 watchlist; routine maintenance penalty。

> 上游摘录（未审读）：build(deps-dev): bump typescript-eslint from 8.72.2 to 8.73.0 (#3579) \[//\]: # (dependabot-start) ⚠️ \*\*Dependabot is rebasing this PR\*\* ⚠️ Rebasing might not happen immediately, so don't worry if this takes some time. Note: if you make any changes to this PR yourself, they will take precedence over the rebase. --- \[//\]: # (dependabot-end) Bumps \[typescript-eslint\](https://github.com/typescript-eslint/typescript-eslint

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [build(deps-dev): bump eslint from 10.14.0 to 10.15.0 (#3578)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/f8c8f485d281ce8eef1f5383628cad5fe4259956)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 5 · 上游时间 2026-11-26T19:11:40Z

入选依据：T1 watchlist; routine maintenance penalty。

> 上游摘录（未审读）：build(deps-dev): bump eslint from 10.14.0 to 10.15.0 (#3578) Bumps \[eslint\](https://github.com/eslint/eslint) from 10.14.0 to 10.15.0. Release notes Sourced from eslint's releases . v10.15.0 Features ec52157 feat: check proto and assignment targets in func-names ( #21521 ) (Lê Văn Xuân Hoàn) 34a8b1b feat: recognize string and computed keys in accessor-pairs descriptors ( #21519 ) (Lê Văn Xuân Hoàn) 663c825 feat: hand

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
