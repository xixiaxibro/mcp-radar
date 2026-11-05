# 运行与维护

## 每日工作流

`radar.yml` 由 schedule / workflow_dispatch 触发；`ci.yml` 负责脚本测试。自动采集不因普通 PR 触发，也不执行跟踪项目提供的代码。工作流的 GitHub Token 用于读取公开数据和提交本仓库结果，不需要添加个人 PAT。

定时收集失败时，检查 `data/latest.json` 的 sources/errors/warnings。失败报告仍会提交，最终作业显示失败。全部失败时不覆盖旧基线，具体错误留在 Actions 日志。

如果仓库策略禁止 token 推送，需由仓库管理员调整 Actions workflow permissions；若有分支保护，应改为由维护者合并更新分支，不绕过保护。当前默认在 main 上提交数据。

## macOS 本机调度

`install_launchd.py` 生成当前用户的 `~/Library/LaunchAgents/org.xixiaxibro.mcp-radar.plist`，默认本地时间 09:17；不需要 root，不存凭证。`run_scheduled.py` 用文件锁防止本机重叠，要求 main 和干净工作区，先 `git pull --ff-only`，采集后仅提交生成目录并通过已有 SSH 连接推送。

安装与关闭命令见 README。首次可用 `launchctl kickstart gui/$(id -u)/org.xixiaxibro.mcp-radar` 测试；日志在 `~/Library/Logs/mcp-radar/`。本机调度依赖登录、网络、GitHub 授权与 SSH，不是常在线云服务。修改工作时间、移动仓库或更换 Python 后，remove 再 install。

选择一个主要调度器；恢复 GitHub Actions 后可移除本机任务，避免两端同时提交。文件锁只保护本机进程，GitHub 的 concurrency 只保护云端任务，两者不能构成跨机器锁；推送冲突会失败并保留本地提交，不强推。

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
