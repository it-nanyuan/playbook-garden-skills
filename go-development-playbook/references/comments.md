# Comments

## Goal

Go 注释应帮助理解职责、边界、副作用和并发语义，而不是翻译 obvious code。

## Required

- package 注释
- exported type / function 注释
- 复杂并发、重试、状态转换、共享组件注释

## Avoid

- `// set value`
- `// call repo`
- `// loop list`
