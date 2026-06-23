---
name: frontend-development-playbook
description: Build professional, maintainable frontend applications with clear design and engineering standards. Use when planning or implementing web pages, admin systems, dashboards, or business frontends, especially when the user wants better structure, reusable components, stronger comments, and more commercial-quality UI than generic AI output.
---

# Frontend Development Playbook

## Overview

这个 skill 用来约束前端项目的设计质量和工程质量，尤其适合后台网页、管理系统、业务前端和中后台。它既关注 UI 是否专业，也关注代码结构、组件复用、注释、状态管理、目录组织和可维护性。

## Workflow

1. 先判断项目类型：官网、营销页、业务前台、后台管理系统、数据看板还是 H5。
2. 如果是后台或业务系统，先明确目标用户、主任务、信息密度和竞品参考。
3. 如果用户描述含糊，优先提问，不直接生成“卡片墙 + 大标题”的空洞页面。
4. 已有项目先跟随现有框架、组件库、设计系统和状态管理方案。
5. 新项目根据类型决定框架、组件库、目录结构和状态管理方式。
6. 开发时同样重视注释、组件边界、复用、模块化和样式一致性。

## Core Rules

- 项目重要的不只是页面能显示，更重要的是代码结构和后续可维护性
- 注释必须写清组件职责、复杂交互、状态含义和业务约束
- 页面、组件、hooks、services、types、utils、store 按职责拆开
- 优先复用组件和业务容器，不要复制页面改样式改字段
- 后台系统优先保证信息架构、交互秩序和数据操作效率
- 设计和实现都避免大标题、大段说明、无意义卡片堆砌
- 新建代码文件、样式文件、README 片段、模板和注释中，默认禁止写 `Codex` 或其他平台来源信息

## Comments Standard

- 组件注释：说明职责、适用场景、关键 props
- 方法 / hooks 注释：说明输入、输出、副作用、依赖和边界
- 字段 / state 注释：说明业务语义、枚举状态、单位或特殊约束
- 复杂交互、表格列逻辑、权限逻辑、缓存逻辑和数据映射优先补注释

详细见 `references/comments.md`。
跨语言注释母规范参考 `comment-style-playbook`。

## Structure Standard

- 页面文件只负责页面组织，不承担全部逻辑
- 复杂页面必须拆分成子组件、hooks 和业务服务
- `api`、`services`、`hooks`、`components`、`stores`、`types`、`utils` 分层清楚
- 公共状态、请求封装、表格容器、筛选容器、表单容器优先抽象
- 一个文件一个主组件，避免超长单文件

详细结构见 `references/structure.md`。

## UI And Product Quality

- 后台默认偏专业、克制、可商用，不做概念图式页面
- 复杂项目优先采用分栏布局或多级菜单
- Logo 区和顶部导航默认可采用 `68px` 高度
- 顶部导航和 tag 固定，菜单区和内容区独立滚动
- 表格过宽时固定操作列，其他列允许横向滚动
- 页面不要依赖大段提示文字解释自己

UI 相关规范可参考 `admin-ui-design-playbook`，本 skill 主要补工程实现层。

## Embedded UI Baseline

即使没有单独安装 `admin-ui-design-playbook`，这个 skill 也默认内置下面这些核心 UI 规则：

- 先判断页面属于官网、业务前台、后台管理系统、工作台还是数据看板
- 如果风格、竞品、用户或主任务不明确，先补关键问题，不直接开始画页面
- 避免大标题、大段说明文字、卡片墙和“AI 感很重”的空洞页面
- 优先用布局、层级、分组、筛选、表格、状态和操作区组织复杂信息
- 后台页面重点关注导航秩序、tag、筛选区、列表区、固定操作列和滚动规则
- 页面要看起来像真实业务系统，而不是视觉概念图

## Design Dependency

如果任务涉及页面设计、界面布局、交互结构、后台视觉层级或组件呈现方式，默认同时遵循 `admin-ui-design-playbook`。

执行规则：

- 如果用户没有单独点 UI 设计 skill，但当前任务明显涉及页面设计，也要主动沿用 `admin-ui-design-playbook`
- 如果风格、竞品、信息密度或后台布局要求不明确，先按 UI 设计 skill 的提问方式补齐上下文
- 后台项目的导航、tag、筛选区、列表区、表格滚动和固定区规则默认跟随 UI 设计 skill
- 本 skill 负责工程实现层，`admin-ui-design-playbook` 负责设计判断和视觉结构标准

## Recommended Stack

- `React + TypeScript + Ant Design`
- `Vue 3 + TypeScript + Element Plus`
- 状态管理按项目现状选择 `Zustand`、`Redux Toolkit`、`Pinia`
- 路由、请求、表格、表单、校验优先跟随成熟生态

详细见 `references/stack-selection.md`。

## Reuse And Modularity

- 公共布局、表格容器、筛选容器、弹窗表单、空状态、错误态优先抽组件
- 相同业务流程优先抽 hooks 或 services
- 通用枚举、字典、格式化逻辑和权限判断优先抽共享层
- 不要让页面直接散写请求、数据转换、权限和 UI 拼装全部逻辑

## When To Use

在这些场景触发这个 skill：

- 用户要做前端页面、后台系统、管理台、数据看板或业务前端
- 用户抱怨页面“不专业”“太乱”“商用价值差”
- 用户要统一前端注释、组件拆分、复用和结构规范
- 用户要在 `React` / `Vue` 项目里形成更完整的工程约束
- 用户既关心界面质量，也关心代码质量

## References

- `references/comments.md`
- `references/structure.md`
- `references/stack-selection.md`
- `references/backend-admin.md`

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
