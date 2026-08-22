# Habit Calibration

Use this reference when memory exists but does not yet understand NAN's habits well enough to guide work.

## Calibration Triggers

- NAN says the agent does not understand their habits, taste, or preferences.
- `memory/habits.md`, `memory/design-style.md`, or project-specific memory is empty or mostly unknown.
- NAN gives corrective feedback such as "not this style", "should be consistent", "why can't I see it", "push it", or "install it".
- A task depends on a preference that is not recorded and guessing would likely create rework.

## What To Inspect

Before asking questions, inspect available evidence:

- Recent user instructions in the current conversation.
- Relevant files in `project-memory`, especially `memory/habits.md`, `memory/preferences.md`, `memory/design-style.md`, and the project note.
- Repository conventions such as naming, structure, changelog style, commit style, test expectations, and platform adapters.

## How To Capture

Write habits as short evidence-backed entries:

- **Confirmed habit:** The user stated it directly or approved it.
- **Working style signal:** Repeated behavior suggests it, but it has not been explicitly confirmed.
- **Needs calibration:** The area is important but still lacks examples.

Prefer these categories:

- Communication language and tone.
- Autonomy versus questions.
- Naming and repository organization.
- Design taste and disliked styles.
- Engineering structure and testing expectations.
- Review depth, delivery cadence, commits, and pushing behavior.

## How To Ask

Ask only when the missing preference changes the current work. Keep questions small:

- Ask 1 to 3 questions at a time.
- Prefer concrete contrasts over broad preference surveys.
- Offer to infer from examples when the user does not want to answer.

Useful question shapes:

- "这次更希望我先直接改，还是先给你两个方向选？"
- "这个项目你更想要偏克制工具型，还是偏有品牌感？"
- "我看到这个偏好还没记录，是否以后都按这个来？"

## What Not To Do

- Do not invent taste just to make memory look complete.
- Do not turn one-off frustration into a universal rule.
- Do not store sensitive personal details, secrets, credentials, or private account data.
- Do not flood memory with transcripts; record the durable rule, not the whole conversation.
