# iOS Development Playbook for Gemini

Use these instructions when building iOS features.

## Workflow

1. Confirm whether the project is SwiftUI, UIKit, or mixed.
2. Split code by view, model, service, routing, and shared components.
3. Reuse modules and shared pieces before creating local duplicates.
4. If the task includes screen design, also follow the repository's admin UI quality standards.

## Rules

- Keep one main type per file.
- Use extensions to separate responsibilities.
- Comment shared APIs, async behavior, and business-critical state.
