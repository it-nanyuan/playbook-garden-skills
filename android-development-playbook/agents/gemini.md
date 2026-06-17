# Android Development Playbook for Gemini

Use these instructions when building Android features.

## Workflow

1. Confirm the UI stack: Compose, Views, or mixed.
2. Split the work across UI, domain, and data responsibilities.
3. Reuse shared pieces before duplicating code.
4. If the task includes screen design, also follow the repository's admin UI quality standards.

## Rules

- Keep one main type per file.
- Separate screens, state, events, repositories, and data sources.
- Comment business-critical states and reusable APIs.
