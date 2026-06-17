# Playbook Garden Skills

一个面向团队协作与 AI 平台消费的规范仓库，用来持续沉淀设计、开发、提交、数据库与运维等工作流标准。

这里的每个目录都是一个独立 skill。  
目标不是“收集建议”，而是把高频工作先收敛成清晰规则，让平台或 AI 在真正动手前先按统一标准思考、提问、设计、编码、审查和交付。

## Overview

这个仓库适合解决这类问题：

- 页面能出，但看起来不专业，没有商用品质
- 代码能跑，但结构松散、复用差、后续难维护
- 提交记录混乱，历史里看不出一次改动到底做了什么
- 数据库和运维操作缺少审查、回滚、留痕和统一流程

这套 skill 的作用，就是把这些关键环节标准化。

## Core Principles

| 原则 | 说明 |
| --- | --- |
| 先提问再执行 | 需求不清楚时先补上下文，不直接输出看起来完整但实际不专业的结果 |
| 规范优先 | 风格、命名、结构、注释、边界、回滚策略都先于临时发挥 |
| 商用品质 | 默认面向真实业务系统和长期协作，而不是一次性 Demo |
| 可维护性 | 代码、SQL、脚本、文档、配置都要考虑后续接手成本 |
| 平台可消费 | skill 既能给人读，也尽量整理成平台容易接入的结构 |

## Skill Map

### Collaboration

| Skill | 方向 | 主要用途 | 关键约束 |
| --- | --- | --- | --- |
| `git-commit-playbook` | Git 提交规范 | 统一提交标题、前缀、正文和语言确认流程 | 标题强制 `type: summary`；正文必须编号列出改动；语言不明确时先确认中文或英文 |
| `comment-style-playbook` | 跨语言注释规范 | 统一类、方法、字段、模块和复杂逻辑的注释写法 | 关键公共能力必须写职责；复杂流程必须写意图；注释强调边界、副作用和约束 |

### Design

| Skill | 方向 | 主要用途 | 关键约束 |
| --- | --- | --- | --- |
| `admin-ui-design-playbook` | 商用后台 UI 设计 | 设计控制台、管理系统、数据后台和运营平台 | 先问风格、竞品、用户与任务；避免大标题、卡片墙和文字堆砌；强调后台布局、导航、tag、筛选区和表格规范 |

### Frontend And Mobile

| Skill | 方向 | 主要用途 | 关键约束 |
| --- | --- | --- | --- |
| `frontend-development-playbook` | 前端开发规范 | 规范业务前端、后台前端和中后台工程实现 | 强调注释、分层、组件复用、表格与筛选容器抽象，并内嵌精简版 UI 基线 |
| `ios-development-playbook` | iOS 开发规范 | 规范 Swift / SwiftUI / UIKit 项目开发 | 单文件单主类型；扩展拆分；注释、复用、组件化、模块化，并内嵌精简版 UI 基线 |
| `android-development-playbook` | Android 开发规范 | 规范 Kotlin / Compose / Android 工程开发 | 单文件单主类型；UI / Domain / Data 分层；组件化与状态边界清晰，并内嵌精简版 UI 基线 |
| `flutter-hybrid-development-playbook` | Flutter 混合开发规范 | 规范中大型 Flutter 和混合应用开发 | 强调功能拆分、组件化、package 化、桥接边界和 `melos` 管理，并内嵌精简版 UI 基线 |
| `go-development-playbook` | Go 开发规范 | 规范 Go API、服务、任务和基础设施工具开发 | 强调 package 边界、错误处理、context 传递、日志、测试和生产可观测性 |
| `python-development-playbook` | Python 开发规范 | 规范 Python API、worker、脚本服务和工具开发 | 强调模块职责、依赖管理、类型意识、测试、配置边界和可维护性 |
| `php-development-playbook` | PHP 开发规范 | 规范 PHP API、后台系统、任务和业务模块开发 | 先问 `Laravel / Symfony / Hyperf / ThinkPHP`；强调分层、注释、测试、缓存队列和安全边界 |

### Backend

| Skill | 方向 | 主要用途 | 关键约束 |
| --- | --- | --- | --- |
| `java-development-playbook` | Java 后端开发规范 | 规范单体与微服务 Java 项目开发 | 先问单体还是微服务；`service` 必须配 `service.impl`；统一接口、事务、异常、日志、缓存、命名和微服务组件约束 |
| `go-development-playbook` | Go 后端开发规范 | 规范 Go API、服务、微服务和基础设施工具开发 | handler / service / repository 分层清晰；统一错误、日志、超时、测试和依赖边界 |
| `python-development-playbook` | Python 后端开发规范 | 规范 Python API、worker、自动化工具和服务开发 | router / service / repository 分层清晰；统一校验、异常、测试、依赖和配置方式 |
| `php-development-playbook` | PHP 后端开发规范 | 规范 PHP API、后台系统、异步任务和业务服务开发 | 先问框架类型；统一 Controller / Service / Repository 边界、异常、缓存、队列和安全策略 |

### Data And Operations

| Skill | 方向 | 主要用途 | 关键约束 |
| --- | --- | --- | --- |
| `dba-playbook` | DBA 规范 | 规范表设计、SQL 优化、索引、数据修复和生产库操作 | 先看环境和影响范围；重视备份、回滚、`EXPLAIN`、分批执行、工具链和注释 |
| `devops-playbook` | 运维 / DevOps 规范 | 规范部署、发布、监控、回滚和环境管理 | 生产变更必须有回滚方案；配置可追踪；监控、日志、Docker、K8s 和健康检查是基础能力 |

## Choose By Scenario

| 你现在要做什么 | 建议优先使用 |
| --- | --- |
| 写规范化 commit message | `git-commit-playbook` |
| 统一跨语言注释风格 | `comment-style-playbook` |
| 设计后台、工作台、控制台 UI | `admin-ui-design-playbook` |
| 做 React / Vue 页面或中后台前端 | `frontend-development-playbook` |
| 做 iOS 页面或功能开发 | `ios-development-playbook` |
| 做 Android 页面或功能开发 | `android-development-playbook` |
| 做 Flutter / 混合应用开发 | `flutter-hybrid-development-playbook` |
| 做 Java 单体或微服务后端 | `java-development-playbook` |
| 做 Go API、服务或内部工具 | `go-development-playbook` |
| 做 Python API、worker 或自动化服务 | `python-development-playbook` |
| 做 PHP API、后台系统或异步任务 | `php-development-playbook` |
| 做 SQL、索引、迁移、生产数据修复 | `dba-playbook` |
| 做发布、监控、回滚、集群与环境配置 | `devops-playbook` |

## Repository Structure

通常每个 skill 由三层结构组成：

| 路径 | 作用 |
| --- | --- |
| `SKILL.md` | 核心规范、工作流、触发场景和硬规则 |
| `agents/` | 面向不同平台的消费入口产物 |
| `references/` | 更细的规则、技术栈选择、结构说明和扩展文档 |

这种组织方式的目标是：

- `SKILL.md` 保持清晰，适合直接触发
- `references/` 承接细则，避免主文件臃肿
- `agents/` 方便多平台接入，而不是每次临时拼提示词

## Platform Adapters

大多数 skill 现在都带有一层多平台适配结构，例如：

- `agents/openai.yaml`
- `agents/claude.md`
- `agents/copilot-instructions.md`
- `agents/cursor.mdc`
- `agents/gemini.md`
- `references/platforms/README.md`

这些文件的作用是：

- 给不同平台准备更接近真实消费方式的适配产物
- 说明每个平台应优先读取哪份文件
- 让同一个 skill 在多平台下更容易复用

需要特别注意：

- 平台适配文件 `!=` 平台自动安装协议
- 仓库里存在这些文件，不代表 Claude、Gemini、Copilot、Cursor 会自动从 GitHub 安装 skill
- 是否支持自动安装、导入或发现 skill，取决于平台本身能力

更准确的理解是：

- `SKILL.md`：规范本体
- `agents/*`：平台消费入口
- `references/platforms/*`：平台接入说明
- 自动安装能力：由平台决定，不由这些文件单独决定

## Install Modes

### Whole Repository

如果平台支持按仓库导入，那这整个仓库可以作为一组规范来源。  
这种方式适合你希望平台长期发现多个 skill 的场景。

### Single Skill

如果平台只支持“单个 skill 安装”，建议这样理解：

- 开发类 skill 尽量自带自己的核心规则
- `frontend / ios / android / flutter` 已经内嵌了精简版 UI 核心规则
- `admin-ui-design-playbook` 仍然是总设计规范，但不是单装开发 skill 时唯一的 UI 规则来源

推荐组合：

| 主 Skill | 建议同时参考 |
| --- | --- |
| `frontend-development-playbook` | `admin-ui-design-playbook` |
| `ios-development-playbook` | `admin-ui-design-playbook` |
| `android-development-playbook` | `admin-ui-design-playbook` |
| `flutter-hybrid-development-playbook` | `admin-ui-design-playbook` |

## Recommended Usage

### For Humans

1. 找到对应 skill。
2. 先看 `SKILL.md` 理解核心规则。
3. 需要细节时再读 `references/`。
4. 新增规范时尽量保持和现有 skill 同一组织方式。

### For AI Platforms

1. 在真正执行前先加载对应 skill。
2. 如果需求不明确，优先按 skill 要求提问。
3. 输出时遵守 skill 的结构、命名、注释和交互规范。
4. 不要跳过 skill 直接自由发挥。

## Current Scope

目前这套仓库已经覆盖：

- Git 提交规范
- 跨语言注释规范
- 商用后台 UI 设计规范
- 前端工程规范
- iOS / Android / Flutter 开发规范
- Java / Go / Python / PHP 后端规范
- DBA 规范
- 运维 / DevOps 规范

后续可以继续扩展到：

- 测试规范
- API 设计规范
- 安全规范
- 产品需求文档规范
- 发布流程规范

## Philosophy

好的规范不是为了限制创造力，而是为了把真正重要的经验固定下来。  
当平台、AI 和团队成员都先按同一套规则工作，项目会更稳定、更专业、更可复用，也更像一个真实可持续演进的工程体系。
