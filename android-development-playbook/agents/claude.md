# Android Development Playbook for Claude

Use this instruction set when implementing Android features with Kotlin, Compose, or View-based projects.

## Core Behavior

- Keep UI, domain, and data responsibilities separated.
- Reuse components, use cases, repositories, and shared logic before duplicating code.
- Comment business state, async behavior, public APIs, and reusable modules clearly.
- If the task includes screen design, also follow the repository's admin UI design standards where relevant.

## Rules

- One primary type per file.
- Keep Compose screens, state, events, repositories, and data sources cleanly separated.
- Prefer modular growth over monolithic screen files.
