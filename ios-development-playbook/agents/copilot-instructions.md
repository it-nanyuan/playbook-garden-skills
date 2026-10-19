# iOS Development Playbook for GitHub Copilot

Apply these rules when planning or implementing iOS features.

## Workflow

- Identify whether the project uses SwiftUI, UIKit, or both.
- Keep comments, extensions, component reuse, and modular boundaries clear.
- When page or screen design is involved, also align with the repository's admin UI design standards.

## Engineering Standard

- One primary type per file.
- Keep views, view models, services, models, and routing separated.
- Reuse shared components and common services before duplicating code.
- Native SwiftUI screens should follow system navigation, list, sheet, and progress conventions rather than web-admin chrome.

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。
