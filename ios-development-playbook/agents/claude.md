# iOS Development Playbook for Claude

Use this instruction set when implementing iOS features in Swift, SwiftUI, or UIKit projects.

## Core Behavior

- Follow single-responsibility structure and extension-based organization.
- Reuse components and shared services before writing local copies.
- Comment public APIs, complex state, async behavior, and shared modules clearly.
- When the task includes interface design, also follow the repository's admin UI quality baseline where relevant.

## Rules

- Keep one primary type per file.
- Split UI, state, services, models, and routing cleanly.
- Prefer reusable components and modular boundaries over page-local one-off code.
- For native SwiftUI screens, use system navigation, lists, separators, sheets, and progress patterns where they fit the task.

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。
