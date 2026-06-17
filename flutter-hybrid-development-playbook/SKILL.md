---
name: flutter-hybrid-development-playbook
description: Build maintainable Flutter-based hybrid applications with modular engineering standards. Use when planning or implementing Flutter features, organizing monorepos with melos, defining comments and file rules, improving reuse and componentization, or choosing common Flutter libraries for medium and large projects.
---

# Flutter Hybrid Development Playbook

## Overview

这个 skill 用来约束 `Flutter` 混合开发的工程质量，重点面向中大型项目。它默认强调功能拆分、组件复用、模块化、`melos` 管理、多 package 组织和稳定三方库选择，避免把所有页面、状态和服务都塞在一个 `lib/` 目录里野蛮生长。

## Workflow

1. 先判断项目形态：纯 Flutter、嵌入原生 iOS/Android 的混合应用，还是多业务 package 的 monorepo。
2. 如果是已有项目，先跟随既有状态管理、路由和目录约定。
3. 新增需求前先判断这次能力属于页面、组件、领域模块、基础设施还是宿主桥接能力。
4. 优先拆分功能、组件和 package，而不是把所有逻辑塞到一个 feature 页面里。
5. 对中大型项目优先考虑 `melos` 管理 workspace 和 package 生命周期。
6. 输出结果除了功能代码，还要说明复用点、模块边界和 package 归属。

## Core Rules

- 一个文件默认一个主类、主 widget、主 controller 或主 model
- 大 widget 必须拆分，不要让单个文件无限增长
- 页面、状态、服务、模型、路由、组件按职责分离
- 优先做功能复用、组件化和模块化，不接受大量复制页面改名字
- 中大型项目优先 package 化和 workspace 化管理
- 混合开发项目中的 Flutter 与原生桥接边界要清楚，不要随意跨层互相侵入

## Comments Standard

- 类、widget、controller、service、model 需要有职责注释
- 方法注释重点写输入、输出、副作用、异步行为和状态影响
- 字段注释只解释业务语义、单位、约束或宿主交互含义
- 公共 package、共享组件、桥接层、复杂状态管理优先补齐注释

详细注释规范见 `references/comments.md`。
跨语言注释母规范参考 `comment-style-playbook`。

## Structure Standard

- feature 按业务拆分，shared 按跨业务复用能力拆分
- 页面 widget、局部 widget、state、controller、repository、service、model 分开
- 一个功能复杂时优先拆成独立 package，而不是继续堆在主 app 内
- 原生桥接能力、埋点、网络、设计系统、认证、存储优先独立为共享模块

详细结构规则见 `references/structure.md`。

## Reuse And Modularity

- 相同样式和行为的 widget 必须优先抽公共组件
- 相同业务流程优先抽 shared flow、form section、state container
- 与平台相关的桥接逻辑集中到 bridge 层，不散落在页面里
- 中大型项目优先 `design_system`、`core_network`、`core_storage`、`feature_*` 这类 package 组织方式

## Embedded UI Baseline

即使没有单独安装 `admin-ui-design-playbook`，这个 skill 也默认内置下面这些核心 UI 规则：

- 先判断页面属于业务前台、后台工作台、数据页还是跨端工具页
- 如果风格、竞品、用户和核心任务不明确，先补关键上下文再设计
- 避免大标题、大段说明文字、卡片墙和没有结构的页面输出
- 页面重点应放在信息组织、组件层级、状态反馈和操作效率上
- 对后台、工作台和数据密集型页面，默认采用专业、克制、真实业务系统风格
- 通过共享组件、分组和布局表达层次，不靠装饰性和文字堆砌

## Design Dependency

如果任务涉及 Flutter 界面设计、组件呈现、业务页面结构、后台工作台或跨端视觉规范，默认同时参考 `admin-ui-design-playbook`。

执行规则：

- 不要只做功能拆分，也要保证页面呈现符合商用品质标准
- 如果用户没说明风格、竞品或信息密度，先按 UI 设计 skill 的方式提问
- 对后台、工作台、数据密集型页面，默认避免大标题、卡片墙和说明文字堆砌
- 本 skill 负责 Flutter 的工程拆分、package 边界和复用，设计规则由 `admin-ui-design-playbook` 补足

## Melos And Monorepo

- 多模块 Flutter 项目默认优先考虑 `melos`
- 用 `melos` 管理 package bootstrap、脚本、lint、测试和版本协同
- 不要把所有业务、公共组件和基础设施都堆在一个 package
- package 边界要清楚：feature、core、shared、bridge、app 各司其职

详细见 `references/melos.md`。

## Recommended Stack

- State：`flutter_bloc`、`riverpod` 按项目现状选择
- Routing：`go_router`
- Networking：`dio`
- Serialization：`json_serializable`
- Models：`freezed`
- Storage：`shared_preferences`、`hive`、必要时 `isar`
- Images：`cached_network_image`
- UI Helpers：`flutter_screenutil` 仅在项目已采用时跟随，避免滥用
- Utilities：`equatable`、`intl`

常用库建议见 `references/libraries.md`。

## When To Use

在这些场景触发这个 skill：

- 用户要创建或重构 Flutter 页面、组件、状态管理或 package
- 用户要设计混合开发项目里的 Flutter 与原生边界
- 用户要统一 Flutter 注释、单文件单类、拆分和复用规范
- 用户要推动 Flutter 项目组件化、模块化、`melos` 化
- 用户要选择或限制 Flutter 常用三方库

## References

- `references/comments.md`
- `references/structure.md`
- `references/melos.md`
- `references/libraries.md`

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
