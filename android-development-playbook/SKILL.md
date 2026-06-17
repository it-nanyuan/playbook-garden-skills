---
name: android-development-playbook
description: Build maintainable Android applications with clear engineering standards. Use when planning or implementing Kotlin-based Android features, organizing code structure, defining comments and file rules, choosing libraries, or improving reuse, componentization, and modular boundaries in Android projects.
---

# Android Development Playbook

## Overview

这个 skill 用来约束 Android 工程的可维护性，避免 Activity、Fragment、ViewModel、Adapter、网络和业务逻辑全部缠在一起。它默认强调 Kotlin 工程化、单文件单主类、清晰注释、组件复用、模块拆分和稳定的三方库选择。

## Workflow

1. 先判断项目是传统 View 系统、`Jetpack Compose`，还是混合状态。
2. 已有项目优先跟随既有架构和模块方式，不随意另起炉灶。
3. 新增需求前先判断属于页面、组件、领域逻辑、数据层还是基础设施。
4. 优先把复用组件、通用业务能力和公共数据处理抽离出来。
5. 编码时保持注释、命名、文件组织、模块边界一致。
6. 输出结果除了功能代码，还要体现结构拆分和复用意图。

## Core Rules

- 一个文件默认只放一个主类、主接口、主 Compose 组件或主对象
- Activity / Fragment 负责容器，不负责承载全部业务逻辑
- 页面状态、事件处理、数据请求、持久化职责要拆清
- 优先用组件化和模块化解决重复开发
- 注释要解释业务含义、状态、副作用和边界，而不是重复代码表面意思

## Comments Standard

- 类、接口、数据结构、Compose 组件需要有职责注释
- 方法注释重点写业务作用、参数含义、返回结果、线程或状态影响
- 字段注释只用于解释业务语义或特殊约束
- 公共组件、基础库、领域服务、复杂状态管理优先补齐注释

详细注释规范见 `references/comments.md`。

## Structure Standard

- UI 层、Domain 层、Data 层职责清晰
- Compose 组件、ViewModel、UseCase、Repository、DataSource 不要杂糅
- 同一类型职责过大时按状态、事件、映射、扩展方法拆分
- 通用列表、状态页、空态、按钮、表单控件优先沉淀复用
- 业务复杂时优先 feature module 拆分，而不是单模块无限膨胀

详细结构规则见 `references/structure.md`。

## Reuse And Modularity

- 通用 UI、设计 token、网络封装、错误处理、权限、埋点优先平台级统一
- 相似业务页优先抽共用组件和状态容器
- 多页面重复逻辑优先抽 `UseCase`、`Mapper`、`Repository` 或公共工具层
- 不要为了赶进度复制一整套 Adapter、Fragment 或 Compose 页面再改名字

## Embedded UI Baseline

即使没有单独安装 `admin-ui-design-playbook`，这个 skill 也默认内置下面这些核心 UI 规则：

- 先判断页面属于业务执行页、管理页、工作台还是数据密集型页面
- 如果风格、竞品、目标用户或高频任务不明确，先补关键问题再设计
- 避免大标题、过多说明文字、无意义卡片和没有信息层级的页面
- 页面重点应落在任务流、状态、操作效率和内容组织上，而不是视觉热闹
- 后台或工作台型页面默认追求专业、克制、可信、可商用
- 用布局、分组、列表、状态标签和操作区表达复杂度，不靠文字堆砌

## Design Dependency

如果任务涉及 Android 界面设计、Compose 页面结构、视觉层级、信息密度或业务页面呈现方式，默认同时参考 `admin-ui-design-playbook`。

执行规则：

- 不只关注功能和代码结构，也要关注页面是否专业、克制、可商用
- 如果风格和竞品不明确，先沿用 UI 设计 skill 的提问规则
- 涉及管理台、工作台、业务后台型页面时，避免大标题、无意义卡片和过多说明文字
- 本 skill 负责 Android 工程实现与模块边界，设计判断由 `admin-ui-design-playbook` 提供

## Recommended Stack

- Language：`Kotlin`
- UI：`Jetpack Compose` 优先，必要时兼容 `View`
- Architecture：`ViewModel` + `StateFlow` / `Flow`
- DI：`Hilt`
- Networking：`Retrofit` + `OkHttp`
- Serialization：`kotlinx.serialization` 或 `Moshi`
- Images：`Coil`
- Database：`Room`
- Async：`Coroutines`
- Navigation：`Navigation Compose` 或项目现有方案

常用库建议见 `references/libraries.md`。

## When To Use

在这些场景触发这个 skill：

- 用户要创建或重构 Android 页面、组件、数据层或模块
- 用户要统一 Kotlin 注释、文件拆分和模块结构
- 用户要提升 Android 代码复用、组件化、模块化程度
- 用户要在 Compose 项目里保持工程边界清晰
- 用户要选择或限制 Android 常用三方库

## References

- `references/comments.md`
- `references/structure.md`
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
