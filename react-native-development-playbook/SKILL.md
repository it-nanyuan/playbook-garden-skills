---
name: react-native-development-playbook
description: Build maintainable React Native applications with modular engineering standards. Use when planning or implementing React Native screens, shared business features, hybrid mobile modules, navigation flows, or reusable components, and always clarify whether the project uses Expo, bare React Native, or an existing hybrid architecture before choosing structure, state management, navigation, and native bridge boundaries.
---

# React Native Development Playbook

## Overview

这个 skill 用来把 React Native 开发从“页面能跑起来”拉回到“可维护、可复用、可协作”的工程标准。它默认强调模块边界、组件复用、导航结构、状态管理、原生桥接和商用品质，而不是把页面、请求、状态和平台差异全部堆在一个 screen 文件里。

## Workflow

1. 先判断项目形态：`Expo`、裸 `React Native`，还是嵌入原生 iOS/Android 的混合应用。
2. 如果是已有项目，先跟随现有状态管理、导航、目录和原生桥接约定。
3. 在动手前先判断这次需求属于页面、组件、领域模块、导航流程、状态管理、基础设施还是桥接能力。
4. 优先拆分可复用组件、hooks、service、feature module，而不是把逻辑直接塞进 screen。
5. 对中大型项目优先明确 feature 边界、shared module 和 bridge 边界。
6. 输出结果除了代码，还要体现结构意图，例如为什么拆 screen、为什么抽 hook、为什么单独做 bridge。

## First Question

做 React Native 项目时，第一优先级问题是：

- 这是 `Expo`、裸 `React Native`，还是混合架构项目？

第二优先级问题是：

- 当前项目使用什么导航和状态管理方案？是 `React Navigation`、`Expo Router`、`Zustand`、`Redux Toolkit`、`MobX`，还是已有内部封装？

判断规则：

- `Expo`：适合快速交付、常见业务 App、原生能力需求相对可控的项目
- 裸 `React Native`：适合原生能力较多、定制化较强或已有原生工程的项目
- 混合架构：重点在于 React Native 与原生宿主边界清晰，不互相侵入

如果用户没说明清楚，就先问；不要一边写代码一边默认架构和状态方案。

## Core Rules

- 一个文件默认只放一个主 screen、主组件、主 hook、主 store 或主 service
- 大 screen 必须拆分，不要让单个页面文件无限膨胀
- 页面组件、业务逻辑、状态、网络请求、模型和桥接逻辑按职责分离
- 优先做组件化、模块化和 hook 化，不接受大量复制页面改名字
- 导航结构、状态容器、网络层、埋点、权限、存储和桥接能力要有清晰边界
- 混合项目中的 RN 与原生桥接边界要清楚，不要随意跨层互相侵入

## Comments Standard

- 组件、screen、hook、store、service、bridge module 需要有职责注释
- 方法注释重点写输入、输出、副作用、异步行为、状态影响和平台差异
- 字段注释只解释业务语义、单位、状态值、bridge 参数或宿主交互含义
- 公共组件、导航容器、bridge 层、复杂状态管理、性能优化点优先补齐注释

详细注释规范见 `references/comments.md`。  
跨语言注释母规范参考 `comment-style-playbook`。

## Structure Standard

- feature 按业务拆分，shared 按跨业务复用能力拆分
- `screen`、`components`、`hooks`、`store`、`service`、`model`、`navigation`、`bridge` 分开
- 一个功能复杂时优先拆成独立 feature module，而不是继续堆在 app 根目录
- 原生桥接能力、埋点、网络、设计系统、认证、存储优先独立为共享层

详细结构规则见 `references/structure.md`。

## Reuse And Modularity

- 相同样式和行为的 UI 必须优先抽公共组件
- 相同业务流程优先抽 shared flow、form section、state container
- 与平台相关的桥接逻辑集中到 bridge 层，不散落在页面里
- 中大型项目优先 `design_system`、`core_network`、`core_storage`、`feature_*` 这类组织方式

## Navigation And State Standard

- 导航栈、tab、modal、auth flow、deep link 边界要提前规划
- 局部状态、页面状态、跨页面状态和全局状态不要混用
- store 优先按业务域拆分，不把所有状态都塞进一个全局大 store
- 异步请求状态、缓存状态、表单状态和导航状态职责分离

详细见 `references/navigation-state.md`。

## Bridge And Runtime Standard

- 原生桥接能力要有明确接口、参数、返回值和错误语义
- `Expo` 能力与裸 RN 原生模块要区分处理
- 后台任务、推送、文件、相机、定位、权限、WebView 和支付能力要特别关注平台差异
- 发布时要明确 JS bundle、原生版本、环境配置和回滚策略

详细见 `references/bridge-runtime.md`。

## Embedded UI Baseline

即使没有单独安装 `admin-ui-design-playbook`，这个 skill 也默认内置下面这些核心 UI 规则：

- 先判断页面属于业务前台、工具页、工作台、表单流还是数据密集型页面
- 如果风格、竞品、用户和核心任务不明确，先补关键上下文再设计
- 避免大标题、大段说明文字、卡片墙和没有结构的页面输出
- 页面重点应放在信息组织、组件层级、状态反馈和操作效率上
- 对后台、工作台和数据密集型页面，默认采用专业、克制、真实业务系统风格
- 通过共享组件、分组和布局表达层次，不靠装饰性和文字堆砌

## Design Dependency

如果任务涉及 React Native 界面设计、组件呈现、业务页面结构、工作台风格或跨端视觉规范，默认同时参考 `admin-ui-design-playbook`。

这意味着即使用户只安装 `react-native-development-playbook`，也仍然会先按当前 skill 内嵌的 UI 基线工作；而在需要更完整设计规则时，再继续联动 `admin-ui-design-playbook` 作为总设计规范。

执行规则：

- 不要只做功能拆分，也要保证页面呈现符合商用品质标准
- 如果用户没说明风格、竞品或信息密度，先按 UI 设计 skill 的方式提问
- 对后台、工作台、数据密集型页面，默认避免大标题、卡片墙和说明文字堆砌
- 本 skill 负责 React Native 的工程拆分、导航、状态和 bridge 边界，设计规则由 `admin-ui-design-playbook` 补足

## Recommended Stack

- Navigation：`React Navigation`，必要时跟随项目使用 `Expo Router`
- State：`Zustand`、`Redux Toolkit`，按项目现状选择
- Networking：`axios`
- Async Cache / Query：`@tanstack/react-query`
- Forms：`react-hook-form`
- Validation：`zod`、`yup`
- Storage：`@react-native-async-storage/async-storage`、必要时 `MMKV`
- UI Helpers：`react-native-safe-area-context`、`react-native-gesture-handler`、`react-native-reanimated`
- Images：`react-native-fast-image` 或项目既有方案

常用库建议见 `references/libraries.md`。

## When To Use

在这些场景触发这个 skill：

- 用户要创建或重构 React Native 页面、组件、hooks、store 或 feature module
- 用户要设计 React Native 与原生 iOS/Android 的桥接边界
- 用户要统一 React Native 注释、单文件单主类型、拆分和复用规范
- 用户要推动 React Native 项目组件化、模块化和导航 / 状态边界清晰
- 用户要选择或限制 React Native 常用三方库

## References

- `references/comments.md`
- `references/structure.md`
- `references/navigation-state.md`
- `references/bridge-runtime.md`
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
