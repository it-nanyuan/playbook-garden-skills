# Project Memory Playbook Platform Adapters

- OpenAI / Codex：优先 `agents/openai.yaml`
- Claude：优先 `agents/claude.md`
- Cursor：优先 `agents/cursor.mdc`
- Gemini：优先 `agents/gemini.md`
- Copilot：优先 `agents/copilot-instructions.md`

## Design Principle

- `SKILL.md` 是唯一规范源，定义读取、应用和更新项目记忆的核心流程。
- `agents/` 放平台可消费的适配产物。
- `references/platforms/` 放接入说明、使用建议和维护约定。

## Maintenance Rule

当 `SKILL.md` 更新时：

1. 先更新核心记忆工作流。
2. 再同步更新相关 `agents/` 文件。
3. 最后检查本目录的平台说明是否仍然准确。
