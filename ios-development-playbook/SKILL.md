---
name: ios-development-playbook
description: Build maintainable iOS applications with clear engineering standards. Use when planning or implementing Swift and SwiftUI/UIKit features, organizing project structure, defining comments and file rules, choosing libraries, or improving reuse, modularization, and extension-based code organization in iOS projects.
---

# Ios Development Playbook

## Overview

这个 skill 用来把 iOS 开发从“功能先跑起来”拉回到“可维护、可复用、可协作”的工程标准。它默认强调清晰目录、单文件单类、扩展拆分、适量注释、组件复用和模块边界，而不是把所有逻辑堆在一个页面或一个 ViewModel 里。

## Workflow

1. 先判断项目形态：是 `SwiftUI`、`UIKit`，还是混合使用。
2. 如果是已有项目，先跟随现有架构、命名习惯和模块边界，不随意重造体系。
3. 在动手前先判断这次需求属于页面、组件、服务、模型、状态管理还是基础设施。
4. 优先拆出可复用组件、公共能力和扩展，而不是把逻辑直接塞进单个页面文件。
5. 编码时严格遵守注释、文件组织、命名和扩展规则。
6. 输出结果除了代码，还要体现结构意图，例如为什么拆文件、为什么提取组件、为什么抽公共服务。

## Core Rules

- 一个文件默认只放一个主类、主结构体或主视图
- 同一个类型的扩展能力优先用 `extension` 拆到语义清晰的位置
- 页面代码、业务逻辑、网络请求、模型定义不要杂糅在一个文件
- 先考虑复用，再考虑局部临时写法
- 优先做组件化和模块化，而不是把所有页面都写成孤岛
- 注释是为了帮助协作和维护，不是为了把显而易见的代码再写一遍

## Comments Standard

- 类、结构体、枚举、协议需要有类注释，说明职责和适用范围
- 方法注释重点写输入、输出、副作用、异步行为和边界条件
- 字段或属性只在业务含义不直观时加注释，不要对显然变量逐字翻译
- 公共 API、基础组件、服务层、复杂状态机优先补齐注释
- 复杂布局、状态切换或线程处理附近可以加短注释说明意图

详细注释规范见 `references/comments.md`。
跨语言注释母规范参考 `comment-style-playbook`。

## Structure Standard

- 页面、组件、模型、服务、扩展按职责拆分
- `View`、`ViewModel`、`Service`、`Model`、`Router`、`Component` 不要混在一起
- 同一类型如果扩展较多，可按协议实现、事件处理、UI 构建、私有方法分别用 extension 拆开
- 公共样式、公共组件、网络层、日志、埋点、权限、路由能力应尽量沉淀到共享层
- 新功能优先判断是否适合独立模块或 feature package

详细结构规则见 `references/structure.md`。

## Reuse And Modularity

- 相似页面先抽通用容器、通用筛选区、通用表单项、通用状态视图
- 网络、缓存、鉴权、埋点、错误处理等横切能力优先平台级统一
- 对多个业务线复用的能力，优先抽公共模块，不要复制粘贴
- 如果需求只是局部定制，优先在公共组件上加配置，不要再复制一份组件

## Embedded UI Baseline

即使没有单独安装 `admin-ui-design-playbook`，这个 skill 也默认内置下面这些核心 UI 规则：

- 先判断当前页面是工具型页面、业务执行页、工作台还是数据密集型页面
- 如果风格、竞品、用户或核心任务不明确，先补关键上下文，不直接开始堆界面
- 避免大标题、大段说明文字、卡片墙和没有层级的页面结构
- App 页面默认强制禁止“大标题 + 小标题 + 功能描述”这类展示板式写法
- 除非用户明确要求活动页、专题页、引导页，否则不要在页面里写功能介绍文案
- 让页面重点落在内容结构、状态反馈、主操作、次操作和信息扫描路径上
- 如果是后台风格或工作台风格页面，优先追求专业、克制、可商用品质，而不是装饰性
- 用组件、留白和分组表达层级，不靠解释文字补救设计

## Design Dependency

如果任务涉及 iOS 界面设计、页面结构、视觉层级、信息密度或组件呈现方式，默认同时参考 `admin-ui-design-playbook` 的设计原则。

执行规则：

- 不要只把功能实现出来而忽略页面专业度
- 如果用户没有明确风格或竞品，先按 UI 设计 skill 的思路补齐上下文
- 涉及后台风格 App、管理台、工作台、数据型页面时，优先遵守那套克制、专业、避免堆字和卡片墙的标准
- 涉及 App 页面设计时，默认只输出真实页面本身，不输出功能介绍板、概念展示板或说明型标题区
- 本 skill 负责 iOS 工程实现、模块边界和复用，UI 设计标准由 `admin-ui-design-playbook` 提供

## Recommended Stack

- UI：`SwiftUI` 优先，其次按项目现状兼容 `UIKit`
- Networking：`Alamofire` 或基于 `URLSession` 的轻封装
- Images：`Kingfisher`、`SDWebImageSwiftUI`
- Layout / Utilities：`SnapKit`（UIKit 项目）、`Then`
- Persistence：`RealmSwift`、`SQLite.swift`、`Core Data` 按项目现状选择
- Reactive / State：`Combine`、必要时跟随项目使用 `RxSwift`
- Logging / Diagnostics：`OSLog`

常用库建议见 `references/libraries.md`。

## When To Use

在这些场景触发这个 skill：

- 用户要创建或重构 iOS 页面、组件、服务或模块
- 用户要统一 Swift 注释、文件拆分、扩展组织方式
- 用户要让 iOS 代码更可复用、更组件化、更模块化
- 用户要选择或约束常用 iOS 三方库
- 用户抱怨 iOS 工程越来越大、页面越来越臃肿、代码难维护

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
