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
- For native SwiftUI screens, preserve system navigation, grouped lists, sheets, separators, and progress behavior when suitable.

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。
