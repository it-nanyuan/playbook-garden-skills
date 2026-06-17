---
name: comment-style-playbook
description: Write useful engineering comments across languages and stacks. Use when defining or applying comment standards for classes, methods, fields, components, hooks, services, SQL-adjacent logic, asynchronous flows, or complex business rules so comments explain intent and constraints instead of repeating obvious code.
---

# Comment Style Playbook

## Overview

这个 skill 用来统一“什么注释该写、怎么写才有价值”。它默认反对逐行翻译代码、反对废话注释，强调让注释解释职责、边界、副作用、状态变化、异步行为和业务意图。

## Workflow

1. 先判断当前代码属于哪一类：类 / 结构体 / 组件 / 方法 / hook / service / 字段 / SQL 邻近逻辑 / 异步流程。
2. 再判断这段代码是否真的需要注释，而不是默认所有代码都加注释。
3. 优先给公共 API、复杂业务、异步行为、状态机、共享组件和高风险逻辑写注释。
4. 注释重点写“为什么”“约束是什么”“副作用是什么”，不写显而易见的表面动作。

## Core Rules

- 注释的目标是降低理解成本，不是把代码再翻译一遍
- 类注释写职责和边界
- 方法注释写输入、输出、副作用、异步行为、事务、状态影响
- 字段注释只在业务含义、单位、状态值或约束不直观时写
- 复杂分支、兼容逻辑、缓存更新、MQ、定时任务、桥接层、权限判断优先补注释
- 公共模块的注释优先级高于页面内部小函数

## What To Comment

- 类、结构体、接口、协议、枚举、组件
- 公共方法和共享 hook
- 事务边界、异步流程、回调、副作用
- 状态机、复杂条件分支、兼容逻辑
- 重要缓存逻辑、消息消费、定时任务
- 对团队复用的基础能力和公共组件

## What Not To Comment

避免这些低质量写法：

- `// set value`
- `// update ui`
- `// fetch data`
- `// loop list`
- `// call api`

如果注释只是把代码动作重复一遍，通常不该写。

## Comment Language

- 跟随团队已有语言习惯
- 同一项目尽量统一语言，不中英混杂
- 如果项目没有明确规范，优先选择团队最常用且维护成本最低的语言

## Good Bias

- 解释业务意图
- 解释特殊约束
- 解释为什么不能直接改
- 解释状态和值的真实含义
- 解释失败、重试、补偿和副作用

示例参考见 `references/examples.md`。

## When To Use

- 用户要制定统一注释规范
- 用户要评估当前代码的注释质量
- 用户要约束类注释、方法注释、字段注释和复杂逻辑注释
- 用户要把前端、移动端、后端注释规范拉到同一套母标准上

## References

- `references/examples.md`

## Platform Adapters

如果需要把这个 skill 接到不同平台：

- 核心规范始终以当前 `SKILL.md` 为准
- 平台可消费产物放在 `agents/`
- 平台接入说明放在 `references/platforms/`

优先查看：

- `references/platforms/README.md`
- `references/platforms/openai.md`
- `references/platforms/claude.md`
- `references/platforms/cursor.md`
- `references/platforms/gemini.md`
- `references/platforms/copilot.md`
