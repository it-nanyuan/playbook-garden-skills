---
name: git-commit-playbook
description: Draft clear, structured Git commit messages for code changes. Use when the user asks to write a commit message, summarize staged or unstaged changes for a commit, or enforce a team standard where the first line briefly states what was done and the body lists concrete changes item by item.
---

# Git Commit Playbook

## Overview

这个 skill 用来为 Git 代码提交起草清晰、可复查的提交说明。它的默认目标不是“自动提交”，而是先根据实际改动生成一版高质量提交文案，方便用户检查后再决定是否执行 `git commit`。

## Workflow

1. 先检查实际改动，再写提交说明。
2. 优先阅读 `git status`、已暂存 diff 和未暂存 diff，确认本次提交的真实范围。
3. 如果改动涉及新建仓库、初始化项目、补基础设施文件，主动检查是否需要补充 `.gitignore`，至少覆盖当前仓库会用到的常见语言、框架和工具产物。
4. 如果当前改动混杂了多个互不相关主题，先提醒用户拆分提交；只有在用户明确接受合并提交时，才为整批改动写一条说明。
5. 输出时必须先给一个总标题，再逐条列出本次做了什么，避免空泛描述。

## Output Format

默认输出使用下面这个结构：

```text
<type>: <标题：一句话概括这次提交做了什么>

1. <具体改动 1>
2. <具体改动 2>
3. <具体改动 3>
```

格式要求：

- 标题必须使用前缀格式：`<type>: <summary>`。
- 标题用一行写清主动作和主要范围，让人不看 diff 也知道这次提交的大意。
- 正文逐条列出具体改动，通常写 2 到 6 条。
- 每一条都要落到真实变更上，例如模块、流程、交互、校验、文案、数据结构、测试，而不是泛泛写“优化代码”。
- 如果本次改动没有合适的分条内容，不要硬凑；宁可少写，也不要写空话。
- 必须根据改动性质选择合适前缀，不允许省略前缀。
- 如果本次提交包含补充 `.gitignore`，正文里要明确写出这件事，不要把它省略成“补充配置”。

## Writing Rules

- 标题先选对前缀，再说结果和范围，例如 `feat: 增强验收控制台执行流程编排` 比“修改一些验收逻辑”更好。
- 分条按用户最关心的顺序写，优先行为变化、业务流程变化、可见交互变化，再写内部整理。
- 一条只说一件事，避免把多个独立改动塞进同一句话。
- 尽量使用“新增 / 支持 / 优化 / 调整 / 修复 / 重构”这类明确动词开头。
- 如果从 diff 无法确定意图，要明确说明是基于代码推断，不要假装知道业务背景。
- 如果用户说“先别提交”，就只输出提交文案草稿，不执行任何 Git 写操作。
- 如果仓库是新建的，或首次引入某类技术栈，优先补上常用 `.gitignore` 规则，至少考虑下面这些类别：
  `macOS`、编辑器和 IDE、日志文件、环境变量文件、Node.js、Python、构建产物、缓存目录、临时文件。

## Commit Prefixes

提交标题必须从下面前缀里选择，按最主要的改动意图归类：

- `feat:` 新功能、新能力、新流程、新交互
- `fix:` 缺陷修复、异常处理、兼容性修正
- `refactor:` 重构实现，不直接改变对外行为
- `docs:` 文档、说明、注释、规范文本更新
- `style:` 纯格式整理，不涉及逻辑变化
- `test:` 测试用例、测试工具、测试基建调整
- `build:` 构建脚本、打包逻辑、依赖构建配置变更
- `ci:` CI/CD、自动化流水线、检查规则调整
- `chore:` 杂项维护、脚手架、小型配置整理
- `perf:` 性能优化
- `revert:` 回滚历史提交

选择规则：

- 有用户可感知的新功能时优先用 `feat:`
- 有明确问题修复时优先用 `fix:`
- 只补 `.gitignore`、工程配置、目录整理，通常使用 `chore:` 或 `build:`
- 更新 skill、规范、README、注释时优先用 `docs:`
- 如果一次提交同时包含多类改动，按最核心、最值得在历史里被检索到的意图选前缀

## Gitignore Baseline

当任务涉及仓库初始化、工程脚手架、或“补齐基础规范”时，把 `.gitignore` 视为默认检查项。

常见应覆盖内容：

- `macOS`：`.DS_Store`
- 编辑器：`.vscode/`、`.idea/`、交换文件、临时备份文件
- 环境变量：`.env`、`.env.*`，但保留 `.env.example`、`.env.sample`
- 日志：`*.log`、`npm-debug.log*`、`yarn-error.log*`、`pnpm-debug.log*`
- Node.js：`node_modules/`、`.npm/`、`.pnpm-store/`、`.yarn/`、`.next/`、`dist/`、`build/`、`coverage/`
- Python：`__pycache__/`、`*.pyc`、`.pytest_cache/`、`.mypy_cache/`、`.ruff_cache/`、`.venv/`
- 临时和压缩文件：`*.tmp`、`*.temp`、`*.bak`、`*.zip`

如果仓库只用到其中一部分，不必机械全加；但至少要覆盖已经出现或明确即将使用的技术栈。

## Quality Bar

避免这些低质量写法：

- “修改代码”
- “优化功能”
- “处理一些问题”
- “更新逻辑”

更好的写法应该能回答下面两个问题：

1. 这次主要改了哪块？
2. 具体新增、调整、优化了什么？

## Example

```text
docs: 初始化提交规范并补齐基础忽略规则

1. 新增 Git 提交说明 skill，要求提交标题先概括本次改动主题
2. 约定提交正文按编号逐条列出具体变更，避免只写笼统描述
3. 补充仓库初始化场景下的 `.gitignore` 检查要求，覆盖常见语言和工具产物
4. 明确用户未确认前只起草提交文案，不直接执行提交
```

## When To Use

在这些场景触发这个 skill：

- 用户要求“帮我写 commit message”
- 用户要求“按团队规范整理本次提交说明”
- 用户要求“根据当前 diff 总结提交内容”
- 用户强调“标题先概括，再一条条列出做了什么”
- 用户要求“提交标题必须带 `feat:`、`fix:` 一类前缀”

## Platform Adapters

如果需要把这个 skill 接到不同平台：

- 核心规范始终以当前 `SKILL.md` 为准
- 平台可消费产物放在 `agents/`
- 平台接入说明放在 `references/platforms/`

优先查看：

- `references/platforms/README.md`
- `references/platforms/openai.md`
- `references/platforms/claude.md`
- `references/platforms/cursor.md`
- `references/platforms/gemini.md`
- `references/platforms/copilot.md`
