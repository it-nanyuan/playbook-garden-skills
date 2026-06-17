# PHP Development Playbook Platform Adapters

这个目录说明不同平台消费 `php-development-playbook` 时优先读取哪些文件。

## Core Rule

- 所有平台都应以 `../SKILL.md` 作为规范本体
- `agents/` 目录提供平台入口版本
- 本目录提供平台接入提示

## Suggested Mapping

- OpenAI / Codex：优先 `agents/openai.yaml`
- Claude：优先 `agents/claude.md`
- Cursor：优先 `agents/cursor.mdc`
- Gemini：优先 `agents/gemini.md`
- GitHub Copilot：优先 `agents/copilot-instructions.md`

## Important Note

- 这些文件是平台适配说明，不代表平台一定支持自动安装
- 是否可直接导入、自动发现或自动启用，取决于平台本身能力
