# MCP Radar · 2026-11-10 (UTC)

采集时间：2026-11-10T01:28:35+00:00 · 回看窗口：14 天。

这是公开来源的更新索引和选题素材，不是已经审读、复现的技术结论。标题和摘录来自上游；优先级由可见规则计算。

本次窗口内 1297 条记录；本日累计 120 个新增/变更版本；失败端点 22 个；覆盖警告 0 个。

## 覆盖与限制

PR merged 表示代码进入分支，不代表已发布；release 不自动证明符合某协议版本。初次运行只建立窗口基线。

仅跟踪 watchlist 中公开仓库的 PR、指定仓库 issue/commit、release、公开安全公告和订阅源。未提供 API 的社区讨论、社交媒体和完整标准文档变更不在覆盖保证内。RSS 仅提供源当前保留的条目。

- 采集失败：`IBM/mcp-context-forge` / source — Network error from api.github.com/repos/IBM/mcp-context-forge
- 采集失败：`PrefectHQ/fastmcp` / pulls — The read operation timed out
- 采集失败：`PrefectHQ/fastmcp` / releases — Network error from api.github.com/repos/PrefectHQ/fastmcp/releases
- 采集失败：`PrefectHQ/fastmcp` / security-advisories — Network error from api.github.com/repos/PrefectHQ/fastmcp/security-advisories
- 采集失败：`Tencent/AI-Infra-Guard` / releases — The read operation timed out
- 采集失败：`awslabs/mcp` / source — Network error from api.github.com/repos/awslabs/mcp
- 采集失败：`cloudflare-mcp` / source — Network error from blog.cloudflare.com/rss/
- 采集失败：`cloudflare/agents` / releases — Network error from api.github.com/repos/cloudflare/agents/releases
- 采集失败：`cloudflare/workers-sdk` / pulls — The read operation timed out
- 采集失败：`cloudflare/workers-sdk` / security-advisories — Network error from api.github.com/repos/cloudflare/workers-sdk/security-advisories
- 采集失败：`getsentry/toolkit` / source — Network error from api.github.com/repos/getsentry/toolkit
- 采集失败：`github/github-mcp-server` / pulls — Network error from api.github.com/repos/github/github-mcp-server/pulls
- 采集失败：`github/github-mcp-server` / releases — Network error from api.github.com/repos/github/github-mcp-server/releases
- 采集失败：`github/github-mcp-server` / security-advisories — Network error from api.github.com/repos/github/github-mcp-server/security-advisories
- 采集失败：`lastmile-ai/mcp-agent` / source — Network error from api.github.com/repos/lastmile-ai/mcp-agent
- 采集失败：`mcp-official-blog` / source — Network error from blog.modelcontextprotocol.io/index.xml
- 采集失败：`microsoft/playwright-mcp` / source — Network error from api.github.com/repos/microsoft/playwright-mcp
- 采集失败：`snyk/agent-scan` / pulls — The read operation timed out
- 采集失败：`snyk/agent-scan` / releases — Network error from api.github.com/repos/snyk/agent-scan/releases
- 采集失败：`snyk/agent-scan` / security-advisories — Network error from api.github.com/repos/snyk/agent-scan/security-advisories
- 采集失败：`sparfenyuk/mcp-proxy` / source — Network error from api.github.com/repos/sparfenyuk/mcp-proxy
- 采集失败：`stacklok/toolhive` / source — Network error from api.github.com/repos/stacklok/toolhive

## 重点 PR / 提案

显示 20 / 104 条；全部数据见当日 JSON。

### [Clean up completed Gateway migration operations](https://github.com/modelcontextprotocol/registry/pull/1830)

`modelcontextprotocol/registry` · **merged** · new · 分数 94 · 上游时间 2026-11-09T11:43:48Z

入选依据：T1 watchlist; breaking: migration; security: security; merged implementation; verify release separately。

> 上游摘录（未审读）：Both hosted environments now run Gateway Fabric, but the deployment guide still described pending cutover and retired capacity experiments. This cleanup records the completed migration and functional checks, documents current two-node staging and preserved production capacity, and removes five unused one-off deployment helpers with their tests and exact-transition security allowlist. Omit empty public Certificate own

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[v1.x\] fix(auth): reject non-loopback http and fragment redirect URIs at registration](https://github.com/modelcontextprotocol/typescript-sdk/pull/3143)

`modelcontextprotocol/typescript-sdk` · **open** · updated · 分数 92 · 上游时间 2026-11-09T11:05:57Z

入选依据：T1 watchlist; security: security, authorization; protocol: protocol, schema; proposal: specification。

> 上游摘录（未审读）：Fixes #3142. The registration handler of 'mcpAuthRouter' validated 'redirect\_uris' only with 'SafeUrlSchema', so it registered 'http://attacker.example.com/callback' and 'https://client.example.com/callback#fragment' with 201. The spec requires HTTPS or a loopback host for redirect URIs (\[Communication Security\](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization#communication-security)), and

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Adopt production Gateway IP and certificates while retaining ingress traffic](https://github.com/modelcontextprotocol/registry/pull/1827)

`modelcontextprotocol/registry` · **merged** · new · 分数 88 · 上游时间 2026-11-09T09:50:44Z

入选依据：T1 watchlist; breaking: migration; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：Start the first production Gateway migration phase using the verified existing public IP reservation and Service UID. Pulumi imports and protects the address plus both public Certificates; the public Service continues selecting ingress-nginx. Application release 1.8.8, database and production capacity settings are unchanged. Validation: production endpoint/certificate and scaling preflights passed, all 11 public conn

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Prepare production certificate ownership for Gateway migration](https://github.com/modelcontextprotocol/registry/pull/1828)

`modelcontextprotocol/registry` · **merged** · new · 分数 88 · 上游时间 2026-11-09T10:04:41Z

入选依据：T1 watchlist; breaking: migration; protocol: protocol; merged implementation; verify release separately。

> 上游摘录（未审读）：Changes production Gateway migration from 'adopt' to 'managed' after #1827. This disables the old Ingress certificate shim and declares explicit empty Certificate owner lists in Pulumi. Traffic continues through ingress-nginx. Validation after the successful \[production adoption deployment\](https://github.com/modelcontextprotocol/registry/actions/runs/42596490262): - Existing public Service UID, IP, selector, ports a

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [SEP: Structured Tool-Failure Classification (ToolFailure)](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3313)

`modelcontextprotocol/modelcontextprotocol` · **open** · updated · 分数 82 · 上游时间 2026-11-09T19:18:59Z

入选依据：T1 watchlist; security: authorization; protocol: protocol, schema; proposal: sep-, sep:; draft PR。

> 上游摘录（未审读）：## Summary Draft SEP-3313 for structured tool-failure metadata. The original schema prototype is #3312, preserved in the \[fork branch\](https://github.com/johnyzaguirre-glean/modelcontextprotocol/tree/draft/tool-failure-classification). This remains in draft pending Core Primitives discussion. Authorization cases need alignment with #2643, and the broader vocabulary and retry semantics with the \[shared error-policy dr

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: update OAuth Client ID Metadata Document references](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3521)

`modelcontextprotocol/modelcontextprotocol` · **merged** · new · 分数 82 · 上游时间 2026-11-09T03:02:27Z

入选依据：T1 watchlist; security: oauth; proposal: specification; merged implementation; verify release separately。

> 上游摘录（未审读）：Human: @localden \_Requested by \*\*Den\*\* · \[project thread\](https://claude.ai/code/project/chan\_01Bzyr6VAkCeeUXG84MjhGvn?thread=cmsg\_01Bzyr6VAkCeeUXG84MjhGvn82J5jHhiUk1WhNasRfmhT2)\_ Update the draft specification and guides from version 00 to \[version 03\](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-client-id-metadata-document-03) of the OAuth Client ID Metadata Document, published on 2 November 2026. Release

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs: add EU Cyber Resilience Act stewardship guidance](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3526)

`modelcontextprotocol/modelcontextprotocol` · **open** · new · 分数 72 · 上游时间 2026-11-09T19:47:15Z

入选依据：T1 watchlist; security: security; proposal: specification。

> 上游摘录（未审读）：Human: @localden \_Requested by \*\*Den\*\* · \[project thread\](https://claude.ai/code/project/chan\_01Bzyr6VAkCeeUXG84MjhGvn?thread=cmsg\_01Bzyr6VAkCeeUXG84MjhGvn5k6yDdsYhrcEf6CJAKPEuC)\_ Add the Linux Foundation EU Cyber Resilience Act (CRA) stewardship notice to the specification repository, which represents the project. - 'SECURITY.md' states that the project's software is ultimately intended for commercial activities and

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Prepare package slicing by strict namespace refactoring into Client, Schema, and Server](https://github.com/modelcontextprotocol/php-sdk/pull/493)

`modelcontextprotocol/php-sdk` · **open** · updated · 分数 72 · 上游时间 2026-11-09T01:45:21Z

入选依据：T3 watchlist; breaking: breaking; protocol: schema; proposal: proposal。

> 上游摘录（未审读）：Proposal to rework namespaces in favor of slicing 'mcp/sdk' package, see #489 1. Moved everything below 'Mcp\\Client', 'Mcp\\Schema', or 'Mcp\\Server' 2. Distributed 'Mcp\\Exception' into component specific namespaces --- Next steps would be: \* introduce composer setups per component \* configure split.sh \* ???

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Prepare production Gateway migration and validate ingress behavior parity](https://github.com/modelcontextprotocol/registry/pull/1825)

`modelcontextprotocol/registry` · **merged** · updated · 分数 68 · 上游时间 2026-11-09T09:29:40Z

入选依据：T1 watchlist; breaking: migration; merged implementation; verify release separately。

> 上游摘录（未审读）：Production depends on ingress-nginx, while the standalone Gateway configuration previously supported only staging. Add guarded adoption, managed-certificate preparation and standalone phases, with activation disabled in production. Preserve the public Service/IP/ports, both registry aliases, Grafana, TLS Secrets and production node-pool limits. Release workflows and application image settings remain unchanged. Use th

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Fix zero-replica restart and enable weekly staging refresh](https://github.com/modelcontextprotocol/registry/pull/1837)

`modelcontextprotocol/registry` · **merged** · new · 分数 68 · 上游时间 2026-11-09T22:33:46Z

入选依据：T1 watchlist; breaking: migration; merged implementation; verify release separately。

> 上游摘录（未审读）：Enable the staging refresh CronJob for Sundays at 06:00 UTC. Fix restarting from zero: Kubernetes omits spec.replicas in the Scale response at zero, so use a resourceVersion check and an add operation instead of testing an absent field. Validation: the full live restore completed unattended in 1m55s, with every container exiting successfully. Restored 234,888 registry rows and 18 migrations; application listing check

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [feat(agents): conformance scenarios for agent discovery (agents-wg#22)](https://github.com/modelcontextprotocol/conformance/pull/556)

`modelcontextprotocol/conformance` · **open** · updated · 分数 66 · 上游时间 2026-11-09T01:48:23Z

入选依据：T1 watchlist; protocol: protocol, conformance; proposal: sep-, extension。

> 上游摘录（未审读）：Closes #576. agents-wg#22 merged on 2026-10-20, so this is ready for review. ## What changes Adds a requirement-traceability yaml for the agent discovery extension, \[agents-wg#22\](https://github.com/modelcontextprotocol/agents-wg/pull/22), and two server scenarios that grade an implementation against it, plus 40 negative controls. \| Scenario \| What it grades \| Checks \| \| --- \| --- \| --- \| \| 'sep-9998-agents-discovery

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [SEP-2792: Per-Request User Language Preference](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2792)

`modelcontextprotocol/modelcontextprotocol` · **open** · updated · 分数 66 · 上游时间 2026-11-09T12:30:23Z

入选依据：T1 watchlist; protocol: protocol, transport; proposal: sep-。

> 上游摘录（未审读）：## Summary SEP-2792 defines transport-neutral propagation of a user's natural-language preference on each MCP request: - 'params.\_meta\["io.modelcontextprotocol/acceptLanguage"\]' reuses the HTTP 'Accept-Language' grammar and semantics, including weighted language ranges and wildcard matching under \[RFC 4647\]. - Response '\_meta\["io.modelcontextprotocol/contentLanguage"\]' reports the language actually used with 'Content

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [SEP-3405: Conformance-Driven SDK Tiers](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3405)

`modelcontextprotocol/modelcontextprotocol` · **open** · updated · 分数 66 · 上游时间 2026-11-09T19:48:58Z

入选依据：T1 watchlist; protocol: sse, conformance; proposal: sep-。

> 上游摘录（未审读）：Draft SEP. Supersedes SEP-1730. An SDK's tier is decided only by the conformance scenarios it passes: which scenarios, on which spec versions, and by when. Process requirements no longer affect a tier. An automated run computes every tier. The SEP opens with a table of what changes from today. Open questions are listed at the end. Work in progress. Not ready for review.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Add SkillCatalog and FilesystemSkillProvider for serving skills from a directory](https://github.com/modelcontextprotocol/python-sdk/pull/3795)

`modelcontextprotocol/python-sdk` · **open** · updated · 分数 66 · 上游时间 2026-11-09T12:03:03Z

入选依据：T1 watchlist; protocol: protocol; proposal: extension。

> 上游摘录（未审读）：Fixes #3683 Adds an optional helper that serves a directory of skills through the existing 'Skills' extension, without changing the protocol or the 'Skills' API. 'mcp/server/skills.py' becomes a package; 'from mcp.server.skills import Skills' and the handler aliases still work. ## Motivation and Context Serving skills from disk currently means writing handlers and registering every file as a resource by hand. This ad

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Complete production Gateway Fabric cutover](https://github.com/modelcontextprotocol/registry/pull/1829)

`modelcontextprotocol/registry` · **merged** · new · 分数 66 · 上游时间 2026-11-09T10:43:09Z

入选依据：T1 watchlist; security: authorization; merged implementation; verify release separately。

> 上游摘录（未审读）：Production now serves both registry hostnames and Grafana through OSS NGINX Gateway Fabric, with Vector supplying edge metrics. This changes 'gatewayProductionPhase' from 'managed' to 'standalone'; normal application releases and production capacity limits remain unchanged. Merged with explicit administrator-merge/cutover authorization after CI and Copilot review. The \[production workflow\](https://github.com/modelcon

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [SEP-XXXX: Required Capabilities for Tools](https://github.com/modelcontextprotocol/transports-wg/pull/31)

`modelcontextprotocol/transports-wg` · **open** · updated · 分数 66 · 上游时间 2026-11-09T23:48:08Z

入选依据：T1 watchlist; protocol: protocol, capabilit; proposal: sep-。

> 上游摘录（未审读）：This is a draft SEP addressing cross-request capability coordination for the per-request client capabilities introduced by \[SEP-2575\](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/2575). ## Motivation and Context SEP-2575 moves client capabilities from a single initialization handshake to per-request declarations in '\_meta', but some requests (notably 'tools/list') need to know what capabilities

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [\[Client\] Add OAuth authorization with the authorization code flow](https://github.com/modelcontextprotocol/php-sdk/pull/666)

`modelcontextprotocol/php-sdk` · **merged** · updated · 分数 64 · 上游时间 2026-11-09T23:38:35Z

入选依据：T3 watchlist; security: oauth, authorization, token; protocol: transport; merged implementation; verify release separately。

> 上游摘录（未审读）：Part of #316, #319, #320, #321, #322 & #323 - third slice of the client authorization in chr-hertel/php-sdk#53. Follows #663 & #664. '''php $client->connect(new HttpTransport('https://mcp.example.com/mcp', auth: OAuth::forApplication('My App')->build())); ''' A '401' now leads to discovery, client registration, the browser, a token and a retry - nothing else changes at the call site. Refresh, step-up and 'offline\_acc

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Apply max\_message\_bytes to remaining HTTP client responses](https://github.com/modelcontextprotocol/ruby-sdk/pull/673)

`modelcontextprotocol/ruby-sdk` · **merged** · updated · 分数 64 · 上游时间 2026-11-09T04:07:05Z

入选依据：T3 watchlist; security: oauth; protocol: protocol; merged implementation; verify release separately。

> 上游摘录（未审读）：## Motivation and Context This completes the client-side response limit introduced in \[459\](https://github.com/modelcontextprotocol/ruby-sdk/pull/459) and extended to OAuth requests in \[520\](https://github.com/modelcontextprotocol/ruby-sdk/pull/520). 'MCP::Client::HTTP' already applies 'max\_message\_bytes:' to message responses. Notification posts, replies to server-to-client requests (including pong), and session DEL

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Retire legacy backup assets and add weekly staging database refresh](https://github.com/modelcontextprotocol/registry/pull/1835)

`modelcontextprotocol/registry` · **merged** · new · 分数 60 · 上游时间 2026-11-09T22:08:33Z

入选依据：T1 watchlist; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：Staging had an obsolete disabled sync workflow and unused legacy backup credentials. Retire those credentials and replace the sync path with a staging-only CronJob that reads the active production Restic repository, validates the archive, stops staging, restores using its existing app role, and verifies the restarted application. The schedule ships suspended until the first live restore succeeds. A dedicated reader h

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Increase Gateway public listing cache TTL to 60 seconds](https://github.com/modelcontextprotocol/registry/pull/1839)

`modelcontextprotocol/registry` · **merged** · new · 分数 60 · 上游时间 2026-11-10T00:08:22Z

入选依据：T1 watchlist; protocol: sse; merged implementation; verify release separately。

> 上游摘录（未审读）：Increase the shared Gateway public-read policy’s successful-response cache lifetime from 30 to 60 seconds to reduce repeated origin reads. Staging and production use the same policy; cache keys, credential/cookie bypass, background refresh and stale-on-error behavior remain unchanged. Update the asset checksum and document the freshness tradeoff, including that stale serving can exceed the TTL. Validation: 'go -C dep

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

## 发布与安全公告

显示 0 / 0 条；全部数据见当日 JSON。

本日暂无记录。

## 协议 / 工作组提交

显示 10 / 16 条；全部数据见当日 JSON。

### [docs: update OAuth Client ID Metadata Document references to draft 03 (#3521)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/222640c8e771dd57f41e655d3c3eef6e5dec8b34)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 77 · 上游时间 2026-11-09T03:02:24Z

入选依据：T1 watchlist; security: oauth; proposal: specification。

> 上游摘录（未审读）：docs: update OAuth Client ID Metadata Document references to draft 03 (#3521) The draft specification and guides cited version 00 of the IETF draft. Point them at version 03 and its new section numbers, and record the change in the draft changelog. Released versions are unchanged.

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Merge main into the community docs restructure](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/d3bcb0d593f486ea689bd615ec88e362c2862bb0)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 71 · 上游时间 2026-11-09T08:34:45Z

入选依据：T1 watchlist; protocol: sse; proposal: extension。

> 上游摘录（未审读）：Merge main into the community docs restructure Catches the branch up on 101 commits and re-lands four rules that merged after the branch point and that the restructure would otherwise drop. Same failure mode the earlier reconcile commit addressed. SEP guidelines: - an accepted Extensions Track SEP moves the extension to Beta and a second one moves it to Stable; the anchor also moved from #creating-extensions to #exte

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Merge pull request #2 from modelcontextprotocol/localden/contributing-steps](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/329a210d877cd582b7215828715103cc068a43ab)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 55 · 上游时间 2026-11-09T08:25:48Z

入选依据：T1 watchlist; protocol: protocol。

> 上游摘录（未审读）：Merge pull request #2 from modelcontextprotocol/localden/contributing-steps docs(community): rewrite contributing page as concise steps

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Merge pull request #3525 from modelcontextprotocol/dependabot/npm\_and\_yarn/eslint-10.14.0](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/632a0c9a65c9b4fbc889d8aface5c9cf5edef3b7)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 55 · 上游时间 2026-11-09T17:21:26Z

入选依据：T1 watchlist; protocol: protocol。

> 上游摘录（未审读）：Merge pull request #3525 from modelcontextprotocol/dependabot/npm\_and\_yarn/eslint-10.14.0 build(deps-dev): bump eslint from 10.13.0 to 10.14.0

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Merge pull request #3524 from modelcontextprotocol/dependabot/npm\_and\_yarn/glob-14.0.4](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/a8df9b04df17305a0e4e67be0d54ae4c818b36c8)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 55 · 上游时间 2026-11-09T17:21:01Z

入选依据：T1 watchlist; protocol: protocol。

> 上游摘录（未审读）：Merge pull request #3524 from modelcontextprotocol/dependabot/npm\_and\_yarn/glob-14.0.4 build(deps-dev): bump glob from 14.0.3 to 14.0.4

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Merge pull request #3523 from modelcontextprotocol/dependabot/github\_actions/actions/github-script-9.0.0](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/c1d7587934b7b8568c47ae86161c3c16d8b050ee)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 55 · 上游时间 2026-11-09T17:19:32Z

入选依据：T1 watchlist; protocol: protocol。

> 上游摘录（未审读）：Merge pull request #3523 from modelcontextprotocol/dependabot/github\_actions/actions/github-script-9.0.0 build(deps): bump actions/github-script from 8.0.0 to 9.0.0

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Update docs/community/contributing.mdx](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/10897920871fbd92772cd4a06d314e1bc4395e4c)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 35 · 上游时间 2026-11-08T04:57:37Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：Update docs/community/contributing.mdx Co-authored-by: Sarah Novotny

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Merge pull request #3441 from sarahnovotny/pr-3363-rebase](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/394567887feccae8b3e27c7c84106edb5fbac116)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 35 · 上游时间 2026-11-09T13:28:26Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：Merge pull request #3441 from sarahnovotny/pr-3363-rebase docs(community): restructure community docs (rebase of #3363)

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [Update docs/community/contributing.mdx](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/5e49a92ff67f54b1e2c0decd4992137c202f0d86)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 35 · 上游时间 2026-11-08T04:57:20Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：Update docs/community/contributing.mdx Co-authored-by: Sarah Novotny

待核实：对应哪一版规范？改变了什么可观察行为？是否有测试、兼容范围和正式发布？

### [docs(community): reconcile when a sponsor appears in the SEP process](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/7827b68705e7fcaa024fc76ebfddc027cc37227d)

`modelcontextprotocol/modelcontextprotocol` · **committed** · new · 分数 35 · 上游时间 2026-11-09T09:31:44Z

入选依据：T1 watchlist。

> 上游摘录（未审读）：docs(community): reconcile when a sponsor appears in the SEP process The Sponsors section told authors to find a sponsor by posting "the PR with its prototype in the group's Discord channel" and tagging at most two Maintainers on the PR. That assumes the author already has a pull request. Pull request creation is limited to collaborators, so for most authors there is no pull request to post or to be tagged on, and th

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
