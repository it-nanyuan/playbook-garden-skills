# React Native Development Playbook

Apply this playbook when working on React Native screens, shared mobile features, navigation flows, state containers, native bridges, or hybrid app modules.

Start by clarifying:

1. Is the project Expo, bare React Native, or part of a hybrid native app?
2. Which navigation and state management solution is in use?
3. Is the work a screen, component, hook, store, service, bridge, or feature module?

Rules:

- Respect the existing navigation, state, and bridge boundaries
- Keep screens thin and move business logic into hooks, services, and stores
- Do not mix API calls, navigation, state orchestration, and rendering into one file
- Treat native bridge boundaries as first-class architecture concerns

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。
