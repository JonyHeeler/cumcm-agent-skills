# CUMCM Agent Skills

10 个中文数学建模竞赛技能，覆盖建模、求解、验证与论文写作。从本地优秀论文语料中提炼决策规则，并补充数学正确性检查。经验不代表官方要求，也不保证获奖。

## 安装到 Codex

需要 Git 和 Python 3.9+。私有仓库需先获得仓库访问权限并完成 GitHub 登录。

```sh
git clone https://github.com/JonyHeeler/cumcm-agent-skills.git
cd cumcm-agent-skills
python install.py
```

默认复制到 `~/.agents/skills`，供本机 Codex 发现。安装后开启新会话。Windows 如果没有 `python` 命令，可用 `py -3`；macOS/Linux 可用 `python3`。

仅供某个项目使用时，指定该项目的技能目录：

```sh
python install.py --dest "D:/your-project/.agents/skills"
```

macOS/Linux 将目标替换为项目中的 `.agents/skills`。团队也可以把安装后的 `.agents/skills` 提交到项目仓库，让队友克隆项目后由 Codex 发现。

不想运行脚本时，可直接把 `skills/` 内的十个完整目录复制到目标 `.agents/skills/`。必须连同各自 `references/` 一起复制，不能只复制 `SKILL.md`。安装脚本提前检查同名冲突，发现已有目录或文件会退出，不覆盖已有安装；更新时先备份并移走准备替换的十个目录，再重新安装。磁盘/权限错误可能留下部分已复制目录，修复后检查这些目录再重试。

安装路径依据：[OpenAI 技能文档](https://learn.chatgpt.com/docs/build-skills)（核对日期：2026-09-08）。

## 使用

在 Codex 中可输入 `$cumcm-paper` 启动全文工作流，或明确要求使用某个专项技能，例如“使用 cumcm-validation 检查本项目模型”。安装后开启新会话；以 Codex 实际发现列表为准。

| 技能 | 用途 |
| --- | --- |
| cumcm-paper | 全文协调与验收 |
| cumcm-problem-restatement | 题意与需求重述 |
| cumcm-problem-analysis | 瓶颈、路线与验证计划 |
| cumcm-modeling | 假设、符号与数学模型 |
| cumcm-solving | 可复现求解与算法说明 |
| cumcm-results | 结果、图表与答案表达 |
| cumcm-validation | 风险对应的验证与证据边界 |
| cumcm-model-evaluation | 有依据的优缺点与改进 |
| cumcm-abstract | 摘要与关键词 |
| cumcm-writing-style | 不改变数学含义的表达精修 |

这些是指令和参考资料，安装本身不需要第三方 Python 包。实际计算、作图和编译按项目需要配置工具。仓库不包含论文原始语料、比赛题面、数据或他人的模板。参考资料中的论文编号是研究来源标记，不是运行时文件依赖。

如果已使用 `1start-mathmodel` 至 `6verity`，两套工作流有触发重叠和部分规范差异。建议在任务提示中明确由哪套技能协调，保留项目现有产物约定；不要假设安装在不同目录就消除了指令差异。此仓库没有修改或覆盖旧技能。

## 检查安装脚本

```sh
python test_install.py
```

检查在临时目录中完成，不写入个人技能目录。
