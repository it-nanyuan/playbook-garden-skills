# Platform Integration Notes

This skill provides platform-facing database safety instructions.

## Current Platform Mapping

- `agents/openai.yaml`
- `agents/claude.md`
- `agents/copilot-instructions.md`
- `agents/cursor.mdc`
- `agents/gemini.md`

## Rule

- `SKILL.md` remains the source of DBA discipline.
- Preserve production safety, review, backup, and rollback emphasis across platforms.

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。 细则保持在统一标准 skill 中，本适配入口不复制参数表。
