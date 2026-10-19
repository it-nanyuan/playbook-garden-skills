# Admin UI Design Playbook for Claude

Use this instruction set when the task involves admin UI, dashboard UI, business consoles, management systems, or backend web layouts.

## Core Behavior

- Clarify product type, users, core tasks, style direction, and competitors before designing.
- If the user cannot describe style well, ask for products they think look professional.
- Avoid text-heavy mockups, oversized titles, and card walls.
- Prioritize commercial credibility, layout order, information density, and realistic workflows.

## Design Rules

- For admin systems, prefer structured layouts, stable navigation, clear filters, readable tables, and restrained typography.
- In existing systems, inspect and reuse the actual shell and list-page pattern; dashboards start with compact KPI/content and management lists avoid persistent explanation banners.
- For enterprise mobile operations, prefer compact blue-white workflow screens with dense KPIs, charts, maps, progress, filters, bottom tabs, and consistent status colors.
- Avoid turning admin pages into marketing hero sections.
- When the task involves backend consoles, follow the repository's admin UI rules for top nav, tag bars, side menus, and table behavior.
- Keep explanations short and let structure carry the interface.

## Output Expectations

- Summarize the product context briefly.
- State the design direction clearly.
- Explain the page structure and key regions.
- If producing code, align the implementation with the same design constraints.

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。
