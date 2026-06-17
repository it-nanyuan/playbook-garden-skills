# Git Commit Playbook for Claude

Use this instruction set when the user asks for a Git commit message or wants the current changes summarized for commit.

## Core Behavior

- Inspect the actual Git changes before writing the commit message.
- Review `git status`, staged diff, and unstaged diff when available.
- Reuse the user's confirmed commit message language when available.
- If the language is unclear, ask once whether the commit message should be written in Chinese or English before drafting.
- If unrelated changes are mixed together, recommend splitting the commit before drafting.
- If the user says not to commit yet, only draft the message and do not run Git write commands.

## Required Output Format

Return the commit message in this exact structure:

```text
<type>: <one-line summary>

1. <specific change 1>
2. <specific change 2>
3. <specific change 3>
```

## Prefix Rules

The title must always use one of these prefixes:

- `feat:`
- `fix:`
- `refactor:`
- `docs:`
- `style:`
- `test:`
- `build:`
- `ci:`
- `chore:`
- `perf:`
- `revert:`

Choose the prefix based on the main purpose of the change.

## Writing Rules

- Make the title specific enough that someone can understand the main change without opening the diff.
- Write 2 to 6 numbered lines when the diff supports that level of detail.
- Each numbered line should describe one concrete change.
- Keep the title and numbered lines in the language the user selected.
- Prefer explicit verbs such as "新增", "支持", "优化", "修复", "调整", or "重构" when writing in Chinese.
- Do not write vague summaries like "修改代码" or "优化功能".
- If the change includes `.gitignore` updates, mention that explicitly in the numbered list.
