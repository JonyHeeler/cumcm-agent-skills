# CUMCM Agent Skills

给 Codex 的数学建模指导技能，配合 [MathModelAgent](https://github.com/jihe520/MathModelAgent) 使用，也可单独辅助修改已有论文。

## 安装

完整建模先按 MathModelAgent 的说明安装旧技能，再安装本套件。私有仓库需要访问权限。

```sh
git clone https://github.com/JonyHeeler/cumcm-agent-skills.git
cd cumcm-agent-skills
python install.py
```

安装到 `~/.agents/skills` 后重开 Codex 会话。仅用于某项目时执行 `python install.py --dest "项目路径/.agents/skills"`。脚本不会覆盖同名文件；更新本套件前先备份并移走待替换的同名 `cumcm-*` 目录，保留 MathModelAgent 旧技能。

## 给 Codex 的执行说明

完整任务由 `1start-mathmodel` 调度，保留旧阶段、文件、模板和验收约定。本套件在对应阶段提供指导，不另起总控，不修改旧技能；具体协作规则先读 `cumcm-paper`。

| 旧阶段 | 按需读取的新技能 |
| --- | --- |
| 1start-mathmodel | cumcm-paper |
| 2analysis-modeling | cumcm-problem-restatement、cumcm-problem-analysis、cumcm-modeling |
| 3coding-visual | cumcm-solving、cumcm-results、cumcm-validation |
| 4drawio | cumcm-results（图示表达建议） |
| 5writing | cumcm-abstract、cumcm-results、cumcm-model-evaluation、cumcm-writing-style；按需补读重述与分析 |
| 6verity | cumcm-validation、cumcm-paper |

组合使用提示：`按 MathModelAgent 完成任务，在各阶段按需读取 cumcm-* 技能辅助；遵守 cumcm-paper 的协作规则。`

独立修稿提示：`使用 cumcm-paper 审查这篇已有论文，只调用相关专项技能，保留现有结构，不启动完整建模流程。` 也可直接指定 `$cumcm-abstract` 等专项技能；只修稿无需安装旧套件。

完整复制各技能目录及其 references。参考文件中的论文编号只是来源线索，无需原始语料；实际计算与编译使用项目现有工具。
