# Gemini

## Purpose

Gemini 场景下当前采用文本型适配，因此使用 `agents/gemini.md` 提供平台可消费的行为说明。

## Consumed File

- `agents/gemini.md`

## Recommended Use

- 将该文件作为 Gemini 工作区提示、共享系统指令或团队内部模板使用
- 在需要从仓库改动生成提交说明时，把这份规则与真实 diff 一起提供给 Gemini

## Maintenance Notes

- 保持规则聚焦在“看 diff 后写 commit message”这一件事上
- 如果 Gemini 后续支持明确的结构化 agent 配置，再补对应格式文件
