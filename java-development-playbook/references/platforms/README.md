# Platform Integration Notes

This skill provides platform-facing Java backend engineering instructions.

## Current Platform Mapping

- `agents/openai.yaml`
- `agents/claude.md`
- `agents/copilot-instructions.md`
- `agents/cursor.mdc`
- `agents/gemini.md`

## Rule

- `SKILL.md` remains the source of Java architecture and engineering rules.
- Preserve an architecture decision already established by the user or repository; ask only when it is unknown.
- Keep platform adapters aligned on monolith layout, Controller boundaries, MyBatis-Plus, Lombok, security, and verification rules.
