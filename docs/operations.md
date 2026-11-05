# 运行与维护

## 每日工作流

`radar.yml` 由 schedule / workflow_dispatch 触发；`ci.yml` 负责脚本测试。自动采集不因普通 PR 触发，也不执行跟踪项目提供的代码。工作流的 GitHub Token 用于读取公开数据和提交本仓库结果，不需要添加个人 PAT。

定时收集失败时，检查 `data/latest.json` 的 sources/errors/warnings。失败报告仍会提交，最终作业显示失败。全部失败时不覆盖旧基线，具体错误留在 Actions 日志。

如果仓库策略禁止 token 推送，需由仓库管理员调整 Actions workflow permissions；若有分支保护，应改为由维护者合并更新分支，不绕过保护。当前默认在 main 上提交数据。

## 配置

- 新项目：编辑 `repositories`，填写主题、tier、是否收集 issue/commit、关键词。只接受公开仓库。
- 新技术：调整 keywords 分组；说明为什么提高优先级。
- 新文章源：添加 RSS/Atom，使用 HTTPS；不要用普通 HTML 页面伪装 feed。
- 初始窗口：14 天；手动 `--days 1..90`，较长窗口可能触及分页上限。
- 深入某个项目：用 `--repo` 和独立 `--output` 试跑，避免正式历史混入实验。

## 保留与成本

`state.json` 保留最近 90 天状态；逐日 JSON 和 Markdown 历史暂不自动删除。`latest.json` 每次覆盖为最近窗口，周报从现有逐日数据构建。后续数据量显著增大时，再引入月度压缩或归档；不先引入数据库和付费服务。

GitHub API 调用量取决于仓库、端点和页数，约数百次/轮。有限线程、请求超时和短重试用于控制负载；HTTP 403、权限和 API 配额错误直接记录，不无限重试。GitHub Actions 用量以账户政策为准。

## 诊断

- `validate`：检查 watchlist 的名称、重复项、tier 和分页配置。
- `unittest`：用离线替身验证去重、时间窗口、合并状态、部分失败、排序与 feed 解析。
- 单项目试跑：验证当前 API 和行为。
- 全量运行：检查失败来源、分页上限、日报状态和周报。

报告输出可能包含上游不可信标题/摘录；它们只作为数据保存，不作为 shell、工具调用或操作指令执行。仓库可公开访问，提交前不要加入本地配置、凭证或内部材料。
