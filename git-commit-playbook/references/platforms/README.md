# Platform Integration Notes

这组文档说明 `git-commit-playbook` 如何接入不同平台，以及 `agents/` 目录中的文件各自扮演什么角色。

## Design Principle

- `SKILL.md` 是唯一规范源，定义核心规则。
- `agents/` 放平台可消费的适配产物。
- `references/platforms/` 放接入说明、使用建议和维护约定。

## Current Platform Mapping

- `agents/openai.yaml` 对应 OpenAI / Codex 风格的结构化 skill 元信息
- `agents/claude.md` 对应 Claude 可直接读取或转成项目指令的文本规则
- `agents/cursor.mdc` 对应 Cursor Rules 风格的规则文件
- `agents/gemini.md` 对应 Gemini 可消费的指令文本
- `agents/copilot-instructions.md` 对应 GitHub Copilot 指令文件内容

## Maintenance Rule

当 `SKILL.md` 更新时：

1. 先更新核心规范
2. 再同步更新相关 `agents/` 文件
3. 最后检查本目录下的平台说明是否仍然准确

## Compatibility Guideline

- 如果某个平台支持结构化配置，优先使用平台官方支持的结构化格式
- 如果某个平台主要消费文本指令，就维护一份最贴近该平台使用方式的说明文件
- 不要为了“看起来统一”而伪造平台并不识别的配置格式
