# OpenAI / Codex

## Purpose

OpenAI / Codex 集成当前通过 `agents/openai.yaml` 暴露基础元信息，包括展示名、短描述和默认提示词。

## Consumed File

- `agents/openai.yaml`

## Recommended Use

- 在支持 skills 或 agent metadata 的 OpenAI / Codex 环境中直接引用这份配置
- 将 `SKILL.md` 作为详细行为规范来源
- 当平台允许默认提示词时，优先使用 `openai.yaml` 中的 `default_prompt`

## Maintenance Notes

- 这里只放平台可读的元信息，不要把大段规范复制进 `yaml`
- 核心规则变化后，优先检查 `default_prompt` 是否仍能准确概括 skill 的用途
