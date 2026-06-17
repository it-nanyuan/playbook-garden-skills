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
