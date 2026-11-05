# 采集与筛选方法

## 数据来源

每个配置仓库先读取公开元数据，确认不是私有仓库，再读取 PR、release、公开安全公告；协议与工作组额外读取 issue 和 commit。`releases: false` 可关闭发布采集：当前仅对 `cloudflare/workers-sdk` 使用，因为它的大量非 MCP 包发布会淹没窗口，保留其 MCP 相关 PR 和公告。RSS/Atom 读取源当前提供的条目。仓库重定向会报告规范名称。

`keywords` 为空表示所有条目进入窗口；非空时先用标题/正文做大小写不敏感子串过滤。随后排名仅使用标题、420 字符清理后摘录和标签。PR、issue 不下载或运行源码；commit 收录仅用于跟踪指定规范/工作组仓库。

## 排名可解释

| 信号 | 分数 |
|---|---:|
| T1 / T2 / T3 来源 | 30 / 18 / 8 |
| breaking / migration / deprecation 等 | +28，每组只加一次 |
| security / OAuth / token / audience 等 | +26 |
| transport / schema / cancel / conformance 等 | +20 |
| SEP / proposal / specification / extension | +16 |
| release 或 advisory | +25 |
| merged PR | +10 |
| 指定仓库 commit | +5 |
| draft PR | -10 |
| 常规依赖升级、格式、错字、版本发布机器人标题 | -30 |

最终分数最低为 0。详细词表在 `config/watchlist.json`；每条记录保存实际命中的理由。词匹配会有误报和漏报，分数不表示漏洞严重性或真实技术价值。

日报分别显示前 20 个 PR/提案、15 个 release/advisory、10 个 commit、10 篇文章；未显示条目仍保留在当日 JSON。滚动七日最多列出 40 项。

## 状态与去重

按 URL 标识来源事件。指纹覆盖标题、状态、标签、正文哈希、PR head commit、release 版本与发布时间等。评论、反应、star、普通更新时间变化不单独触发技术更新。内容变化不等于行为一定变化。

第一次标为 baseline；之后标为 new / updated。同日重跑保留所有已观察到的不同版本；周报按 URL 保留最后观察的状态。索引状态保留 90 天，超过期限后重新遇到可能再次标为 new。

普通关闭和合并分别记录，不能只凭 closed 判断贡献没有采用；需要阅读项目的同步策略。

## 覆盖完整性

GitHub 每个端点默认最多 8 页，每页 100 条。按 updated 降序的列表在进入窗口外后可以提前停止；无明确时间排序保证的 release/advisory 列表保守采集，达到页数上限报告可能不完整。大型仓库可增加上限或缩短窗口；关键词过滤发生在采集之后，不提高 API 覆盖。

每个端点记录 fetched/capped/status。部分失败保留结果且让 Actions 显示失败；全部失败不覆盖旧数据。**零条结果、源失败、关键词未命中、分页上限是不同情况。**

## 博客使用流程

1. 从周报选择一个实际问题，不逐条改写标题。
2. 打开原始 issue/PR、diff、测试和讨论，固定 commit。
3. 对照对应规范，而不是只打开 latest。
4. 核实包版本与 release，必要时做最小实验。
5. 在知识库记录事实、维护者解释、实验和个人判断，最后写文章。
