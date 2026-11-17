# MCP Radar · 2026-11-17 (UTC)

采集时间：2026-11-17T01:17:44+00:00 · 回看窗口：14 天。

这是公开来源的更新索引和选题素材，不是已经审读、复现的技术结论。标题和摘录来自上游；优先级由可见规则计算。

本次窗口内 534 条记录；本日累计 31 个新增/变更版本；失败端点 38 个；覆盖警告 0 个。

## 覆盖与限制

PR merged 表示代码进入分支，不代表已发布；release 不自动证明符合某协议版本。初次运行只建立窗口基线。

仅跟踪 watchlist 中公开仓库的 PR、指定仓库 issue/commit、release、公开安全公告和订阅源。未提供 API 的社区讨论、社交媒体和完整标准文档变更不在覆盖保证内。RSS 仅提供源当前保留的条目。

- 采集失败：`IBM/mcp-context-forge` / source — Network error from api.github.com/repos/IBM/mcp-context-forge
- 采集失败：`PrefectHQ/fastmcp` / source — Network error from api.github.com/repos/PrefectHQ/fastmcp
- 采集失败：`Tencent/AI-Infra-Guard` / source — Network error from api.github.com/repos/Tencent/AI-Infra-Guard
- 采集失败：`awslabs/mcp` / source — Network error from api.github.com/repos/awslabs/mcp
- 采集失败：`cloudflare-mcp` / source — Network error from blog.cloudflare.com/rss/
- 采集失败：`cloudflare/agents` / source — Network error from api.github.com/repos/cloudflare/agents
- 采集失败：`cloudflare/workers-oauth-provider` / source — Network error from api.github.com/repos/cloudflare/workers-oauth-provider
- 采集失败：`cloudflare/workers-sdk` / source — Network error from api.github.com/repos/cloudflare/workers-sdk
- 采集失败：`getsentry/toolkit` / source — Network error from api.github.com/repos/getsentry/toolkit
- 采集失败：`github/github-mcp-server` / source — Network error from api.github.com/repos/github/github-mcp-server
- 采集失败：`lastmile-ai/mcp-agent` / source — Network error from api.github.com/repos/lastmile-ai/mcp-agent
- 采集失败：`mcp-official-blog` / source — Network error from blog.modelcontextprotocol.io/index.xml
- 采集失败：`microsoft/playwright-mcp` / source — Network error from api.github.com/repos/microsoft/playwright-mcp
- 采集失败：`modelcontextprotocol/agents-wg` / commits — Network error from api.github.com/repos/modelcontextprotocol/agents-wg/commits
- 采集失败：`modelcontextprotocol/agents-wg` / issues — Network error from api.github.com/repos/modelcontextprotocol/agents-wg/issues
- 采集失败：`modelcontextprotocol/agents-wg` / releases — Network error from api.github.com/repos/modelcontextprotocol/agents-wg/releases
- 采集失败：`modelcontextprotocol/agents-wg` / security-advisories — The read operation timed out
- 采集失败：`modelcontextprotocol/csharp-sdk` / source — Network error from api.github.com/repos/modelcontextprotocol/csharp-sdk
- 采集失败：`modelcontextprotocol/ext-skills` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/ext-skills` / releases — Network error from api.github.com/repos/modelcontextprotocol/ext-skills/releases
- 采集失败：`modelcontextprotocol/ext-skills` / security-advisories — Network error from api.github.com/repos/modelcontextprotocol/ext-skills/security-advisories
- 采集失败：`modelcontextprotocol/go-sdk` / pulls — The read operation timed out
- 采集失败：`modelcontextprotocol/go-sdk` / releases — Network error from api.github.com/repos/modelcontextprotocol/go-sdk/releases
- 采集失败：`modelcontextprotocol/go-sdk` / security-advisories — Network error from api.github.com/repos/modelcontextprotocol/go-sdk/security-advisories
- 采集失败：`modelcontextprotocol/java-sdk` / releases — Network error from api.github.com/repos/modelcontextprotocol/java-sdk/releases
- 采集失败：`modelcontextprotocol/java-sdk` / security-advisories — The read operation timed out
- 采集失败：`modelcontextprotocol/kotlin-sdk` / source — Network error from api.github.com/repos/modelcontextprotocol/kotlin-sdk
- 采集失败：`modelcontextprotocol/mcpb` / source — Network error from api.github.com/repos/modelcontextprotocol/mcpb
- 采集失败：`modelcontextprotocol/modelcontextprotocol` / issues — Unterminated string starting at: line 1 column 15896 (char 15895)
- 采集失败：`modelcontextprotocol/php-sdk` / source — Network error from api.github.com/repos/modelcontextprotocol/php-sdk
- 采集失败：`modelcontextprotocol/ruby-sdk` / source — Network error from api.github.com/repos/modelcontextprotocol/ruby-sdk
- 采集失败：`modelcontextprotocol/rust-sdk` / source — The read operation timed out
- 采集失败：`modelcontextprotocol/servers` / source — Network error from api.github.com/repos/modelcontextprotocol/servers
- 采集失败：`modelcontextprotocol/swift-sdk` / source — Network error from api.github.com/repos/modelcontextprotocol/swift-sdk
- 采集失败：`modelcontextprotocol/typescript-sdk` / security-advisories — The read operation timed out
- 采集失败：`snyk/agent-scan` / source — Network error from api.github.com/repos/snyk/agent-scan
- 采集失败：`sparfenyuk/mcp-proxy` / source — Network error from api.github.com/repos/sparfenyuk/mcp-proxy
- 采集失败：`stacklok/toolhive` / source — Network error from api.github.com/repos/stacklok/toolhive

## 重点 PR / 提案

显示 20 / 29 条；全部数据见当日 JSON。

### [docs: stop presenting deprecated features as current on the spec overview pages](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3552)

`modelcontextprotocol/modelcontextprotocol` · **merged** · updated · 分数 104 · 上游时间 2026-11-16T17:32:46Z

入选依据：T1 watchlist; breaking: deprecat; protocol: protocol; proposal: sep-; merged implementation; verify release separately。

> 上游摘录（未审读）：The architecture and base protocol overview pages are where many people new to MCP start. Both still presented sampling, roots and logging as current features, with no indication that they are deprecated as of '2026-07-28' (SEP-2577). Fixes #3548 ## Architecture page Builds on the branch Lazzaretti proposed in #3548 (their commit is included as-is), which updates the five places the issue lists: - Intro: "context exc

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(server): add SEP-2350 scope challenge scenario](https://github.com/modelcontextprotocol/conformance/pull/481)

`modelcontextprotocol/conformance` · **open** · updated · 分数 92 · 上游时间 2026-11-16T15:00:21Z

入选依据：T1 watchlist; security: oauth, token; protocol: sse, conformance; proposal: sep-。

> 上游摘录（未审读）：## Summary - add a language-neutral server conformance scenario for request-time OAuth 'insufficient\_scope' challenges - exercise 'tools/call', static and templated 'resources/read', and 'prompts/get' with a fixed cross-SDK fixture contract - assert HTTP 403, \*\*\*\*\*\* parameters, the complete required scope set in one challenge, and successful upgraded-token retries - restore 'sep-2350-server-single-challenge' traceabi

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [sep(SEP-2643): Structured Authorization Denials](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2643)

`modelcontextprotocol/modelcontextprotocol` · **open** · updated · 分数 82 · 上游时间 2026-11-16T12:04:35Z

入选依据：T1 watchlist; security: authorization; protocol: protocol, transport; proposal: sep-, proposal; draft PR。

> 上游摘录（未审读）：## Motivation and Context This SEP defines a transport-agnostic authorization denial envelope for the Model Context Protocol. The envelope complements transport-level authorization challenges (HTTP 'WWW-Authenticate' with Protected Resource Metadata), carrying a failure classification, a remediation posture, a retry correlation handle, and an extensible set of structured remediation hints for cases the transport cann

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add troubleshooting entry for empty inputSchema / reading '\_def'](https://github.com/modelcontextprotocol/typescript-sdk/pull/3188)

`modelcontextprotocol/typescript-sdk` · **open** · updated · 分数 78 · 上游时间 2026-11-16T08:11:28Z

入选依据：T1 watchlist; breaking: migration; protocol: schema。

> 上游摘录（未审读）：On v1, passing a ZodObject where a raw shape is expected either crashes tools/list with 'Cannot read properties of null (reading \_def)' (v1 <=1.21) or silently publishes an empty schema (v1 <=1.26). Add troubleshooting entries keyed on both symptoms and a migration-guide warning. Closes #2627.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(server): add tools-call-input-validation scenario (SEP-1303)](https://github.com/modelcontextprotocol/conformance/pull/589)

`modelcontextprotocol/conformance` · **open** · new · 分数 72 · 上游时间 2026-11-16T11:33:49Z

入选依据：T1 watchlist; security: security; proposal: sep-。

> 上游摘录（未审读）：Closes #588. Adds a server scenario for SEP-1303 and the security requirement that servers \*\*MUST\*\* "Validate all tool inputs" ('server/tools', 2025-11-25 and draft). Shape and questions are in #588; happy to adjust. ## What it adds - 'src/scenarios/server/tools-input-validation.ts': scenario 'tools-call-input-validation' ('introducedIn: '2025-11-25'', active suite, not added to any 'requirements/\*.yaml'). One connec

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [SEP-2624: Interceptors for the Model Context Protocol](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2624)

`modelcontextprotocol/modelcontextprotocol` · **open** · updated · 分数 66 · 上游时间 2026-11-16T14:02:12Z

入选依据：T1 watchlist; protocol: protocol, lifecycle; proposal: sep-。

> 上游摘录（未审读）：### Summary This PR introduces a SEP for an interceptor framework for the Model Context Protocol, defining a new MCP primitive that allows context operations to be intercepted, validated, and transformed at key points in the agentic lifecycle. ### Motivation The MCP ecosystem is rapidly developing a sprawling landscape of sidecars, proxies, client-wrappers and gateways to address cross-cutting context governance conc

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add release cycle page](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3550)

`modelcontextprotocol/modelcontextprotocol` · **open** · updated · 分数 66 · 上游时间 2026-11-17T00:11:17Z

入选依据：T1 watchlist; protocol: protocol; proposal: sep-。

> 上游摘录（未审读）：Adds 'docs/community/release-cycle.mdx', the release-cycle documentation required by \[SEP-3398\](https://modelcontextprotocol.io/seps/3398-release-cycle-updates) (Reference Implementation, item 2), and aligns the governance pages that SEP-3398 changes. ## Release cycle page - Schedule: six-month releases, eight-month cycles, and the two-month overlap, with an example timeline (light and dark SVG) of a March and a Sept

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Drop client-side validation of tool results against the output schema](https://github.com/modelcontextprotocol/python-sdk/pull/3865)

`modelcontextprotocol/python-sdk` · **open** · new · 分数 66 · 上游时间 2026-11-16T11:55:28Z

入选依据：T1 watchlist; protocol: schema; proposal: specification。

> 上游摘录（未审读）：'ClientSession.call\_tool' checked every tool result's 'structured\_content' against the 'outputSchema' from 'tools/list', using 'jsonschema'. The server writes both the schema and the result, so the check could only tell you that a server disagrees with itself. It also cost a dependency tree ('jsonschema', 'jsonschema-specifications', 'referencing', 'rpds-py') and an implicit 'tools/list' the first time you called eac

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix: retry token refresh without RFC 8707 resource param when the AS rejects it](https://github.com/modelcontextprotocol/python-sdk/pull/2853)

`modelcontextprotocol/python-sdk` · **open** · new · 分数 56 · 上游时间 2026-11-16T20:28:04Z

入选依据：T1 watchlist; security: oauth, token。

> 上游摘录（未审读）：## Motivation and Context Fixes #2578. Microsoft Entra ID v2.0 rejects the RFC 8707 'resource' parameter on 'refresh\_token' grants ('AADSTS9010010', strictly enforced since March 2026). Because the SDK sends it on every refresh, MCP clients using Entra OAuth lose authentication after ~1 hour: the silent refresh fails, tokens are cleared, and the user is forced through interactive re-auth every hour. At the same time,

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [build(deps-dev): bump mint from 4.3.5 to 4.3.23](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3561)

`modelcontextprotocol/modelcontextprotocol` · **open** · new · 分数 54 · 上游时间 2026-11-16T08:09:54Z

入选依据：T1 watchlist; breaking: compatib; security: security, vulnerab; routine maintenance penalty。

> 上游摘录（未审读）：Bumps \[mint\](https://github.com/mintlify/mint/tree/HEAD/packages/mint) from 4.3.5 to 4.3.23. Commits See full diff in compare view \[!\[Dependabot compatibility score\](https://dependabot-badges.githubapp.com/badges/compatibility\_score?dependency-name=mint&package-manager=npm\_and\_yarn&previous-version=4.3.5&new-version=4.3.23)\](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: link roadmap to release cycle](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3549)

`modelcontextprotocol/modelcontextprotocol` · **open** · updated · 分数 50 · 上游时间 2026-11-16T23:14:27Z

入选依据：T1 watchlist; protocol: protocol, sse。

> 上游摘录（未审读）：Adds a direct link from the roadmap to '/community/release-cycle' so readers can find the release schedule and SEP timing. Depends on https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3550, which adds the new page and must merge first. Validation: 'npm run prep' passes with the proposed page and its images temporarily present. Those files are not included in this PR; without them, the link check repor

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(server): return HTTP 200 for handler-origin INVALID\_PARAMS in modern streamable HTTP](https://github.com/modelcontextprotocol/python-sdk/pull/3864)

`modelcontextprotocol/python-sdk` · **closed** · new · 分数 50 · 上游时间 2026-11-16T11:22:05Z

入选依据：T1 watchlist; protocol: streamable。

> 上游摘录（未审读）：## Summary On the 2026-07-28 modern Streamable HTTP path ('src/mcp/server/\_streamable\_http\_modern.py'), '\_write' previously mapped every 'JSONRPCError' through 'ERROR\_CODE\_HTTP\_STATUS' regardless of error origin. Because 'ERROR\_CODE\_HTTP\_STATUS' maps 'INVALID\_PARAMS' ('-32602') to HTTP '400' for inbound envelope rejections, handler-origin '-32602' errors (such as reading an unknown resource URI via 'MCPServer') were

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(server): initialize completions after registration updates](https://github.com/modelcontextprotocol/typescript-sdk/pull/3187)

`modelcontextprotocol/typescript-sdk` · **open** · updated · 分数 50 · 上游时间 2026-11-16T08:11:25Z

入选依据：T1 watchlist; protocol: schema。

> 上游摘录（未审读）：# fix(server): initialize completions after registration updates Adding a completion callback through 'prompt.update({ argsSchema })' or 'resource.update({ template })' before connecting leaves the server without its completion handler. 'completion/complete' returns '-32601 Method not found', even though registering the same callback initially works. Reuse the existing completion setup for registration and updates. V

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(core-internal): classify an inbound message by its envelope keys](https://github.com/modelcontextprotocol/typescript-sdk/pull/3190)

`modelcontextprotocol/typescript-sdk` · **open** · new · 分数 50 · 上游时间 2026-11-16T08:11:31Z

入选依据：T1 watchlist; protocol: protocol, schema。

> 上游摘录（未审读）：# fix(core-internal): classify an inbound JSON-RPC message by its envelope keys ## What 'Protocol''s 'onmessage' now settles the message kind from its envelope keys before validating, so each inbound message runs one schema walk instead of three or four. - 'result' or 'error' → the result and error response schemas only. - 'method' with 'id' → the request schema only. - 'method' without 'id' → the notification schema

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [test(e2e): close the in-process stdio client the way the real transport does](https://github.com/modelcontextprotocol/typescript-sdk/pull/3192)

`modelcontextprotocol/typescript-sdk` · **open** · new · 分数 50 · 上游时间 2026-11-16T21:35:30Z

入选依据：T1 watchlist; protocol: protocol, transport, sse。

> 上游摘录（未审读）：The e2e 'stdio' leg runs over 'stdioClientOverPipes', a test-only client on in-process pipes, instead of 'StdioClientTransport'. Its 'close()' only ended the server's stdin and never fired 'onclose', so 'typescript:protocol:error:connection-closed' was listed as a known failure on stdio although the real transport passes it. The real transport fires 'onclose' from the child process's 'close' event, and its 'close()'

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: correct 2026-07-28 and draft content](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3516)

`modelcontextprotocol/modelcontextprotocol` · **merged** · updated · 分数 40 · 上游时间 2026-11-16T04:15:12Z

入选依据：T1 watchlist; merged implementation; verify release separately。

> 上游摘录（未审读）：Taking an accuracy pass over the MCP docs.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(sep-2640): grade 13 more rows, including two-server host rules](https://github.com/modelcontextprotocol/conformance/pull/590)

`modelcontextprotocol/conformance` · **open** · new · 分数 36 · 上游时间 2026-11-16T08:46:54Z

入选依据：T1 watchlist; proposal: sep-; draft PR。

> 上游摘录（未审读）：## What changes Grades 13 more 'sep-2640.yaml' rows. The yaml counted 46 of its 89 checks as emitted, and now counts 59. Six server checks join the existing scenarios: - 'enumeration.ts': 'sep-2640-resources-nested-completeness' and 'sep-2640-nested-publication-flat' for nested skills, plus 'sep-2640-error-standard-codes' ('-32602' for a skill file the server does not serve) and 'sep-2640-error-informative-messages'

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(blog): add a quote block for person quotes](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3563)

`modelcontextprotocol/modelcontextprotocol` · **open** · new · 分数 30 · 上游时间 2026-11-17T01:16:31Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：Long quotations from named people were written as plain blockquotes: italic text in quotation marks behind a bar, with a '✦ \*\*Name\*\*, Title, Company' line underneath. In the first anniversary post, eleven of them in a row read as a wall of text. ## What changes - \*\*'quote' shortcode on its own\*\* now renders a quote block: a panel on '--surface' in the text column, with a large opening quotation mark cut by the top ed

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [fix(core-internal): match query variables that expand omitted](https://github.com/modelcontextprotocol/typescript-sdk/pull/3147)

`modelcontextprotocol/typescript-sdk` · **open** · updated · 分数 30 · 上游时间 2026-11-16T15:58:30Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：## What breaks 'UriTemplate' disagrees with itself for query expressions. 'expand' treats a query variable as optional — it drops the pair when the variable is 'undefined': '''ts new UriTemplate('/search{?q,page}').expand({ q: 'test' }); // '/search?q=test' ''' 'match' does not. 'partToRegExp' builds one \*\*mandatory\*\* group per name: '''ts pattern: prefix + this.escapeRegExp(name) + '=(\[^&\]+)' ''' so the matcher dema

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [build(deps-dev): bump typescript-eslint from 8.72.1 to 8.72.2](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3560)

`modelcontextprotocol/modelcontextprotocol` · **open** · new · 分数 28 · 上游时间 2026-11-16T08:09:44Z

入选依据：T1 watchlist; breaking: deprecat; routine maintenance penalty。

> 上游摘录（未审读）：Bumps \[typescript-eslint\](https://github.com/typescript-eslint/typescript-eslint/tree/HEAD/packages/typescript-eslint) from 8.72.1 to 8.72.2. Release notes Sourced from typescript-eslint's releases . v8.72.2 8.72.2 (2026-11-09) 🩹 Fixes eslint-plugin: \[prefer-string-starts-ends-with\] parse RegExps with the v flag in unicode sets mode ( #13102 ) eslint-plugin: \[no-deprecated\] stop on circular alias chains ( #13117 ) es

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 发布与安全公告

显示 0 / 0 条；全部数据见当日 JSON。

本日暂无记录。

## 协议 / 工作组提交

显示 2 / 2 条；全部数据见当日 JSON。

### [docs: stop presenting deprecated features as current on the spec overview pages (#3552)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/de3550c9fea3c5269e42ac95204eef44a2b2cb92)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 99 · 上游时间 2026-11-16T17:32:45Z

入选依据：T1 watchlist; breaking: deprecat; protocol: protocol; proposal: sep-。

> 上游摘录（未审读）：docs: stop presenting deprecated features as current on the spec overview pages (#3552) The architecture and base protocol overview pages are where many people new to MCP start. Both still presented sampling, roots and logging as current features, with no indication that they are deprecated as of '2026-07-28' (SEP-2577). Fixes #3548 ## Architecture page Builds on the branch Lazzaretti proposed in #3548 (their commit

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: correct 2026-07-28 and draft content (#3516)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/ac00313ff7f5e9f47b0e0d1ebdf9c0ad6411380b)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 35 · 上游时间 2026-11-16T04:15:09Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：docs: correct 2026-07-28 and draft content (#3516) Taking an accuracy pass over the MCP docs.

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
