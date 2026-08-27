# Changelog

All notable changes to this repository will be documented in this file.

The format loosely follows Keep a Changelog.

## [0.3.4] - 2026-08-27

### Changed

- 重做 `project-memory-playbook` 的习惯校准规则，要求每条 durable habit 写清 `Status`、`Trigger`、`Apply` 和 `Counterexample`
- 将校准重点收敛到自主执行边界、视觉验收、真实 API/地图验证、完整产品闭环、交付节奏和运维保守边界
- 明确普通任务最多问 1-3 个问题，完整习惯画像刷新时只在 `memory/habits.md` 保留 5 个最高价值校准问题

## [0.3.3] - 2026-08-27

### Changed

- 明确项目记忆提交推送节奏：不逐条即时推送，但本轮任务只要改过记忆，结束前必须单独提交并推送
- 长任务在重要里程碑、切换项目或交接前应创建记忆 checkpoint，避免本地记忆未同步到 GitHub
- 同步更新 `project-memory-playbook`、多平台 agents、README、CONTRIBUTING、`skills-index.json` 和各领域 playbook 前置段

## [0.3.2] - 2026-08-27

### Changed

- 为所有非 `project-memory-playbook` 的 playbook 增加 `Project Memory Preflight`，要求真实项目工作先读取私有 `project-memory` 仓库
- 前置段补充习惯校准要求：当 habits、design-style 或项目记录不足以指导当前任务时，不继续猜测偏好
- 更新 README、CONTRIBUTING 和 `skills-index.json`，将项目记忆前置提升为仓库级约束

## [0.3.1] - 2026-08-22

### Added

- 为 `project-memory-playbook` 增加习惯校准流程，在记忆稀疏或用户反馈“不够了解习惯”时主动识别偏好空白
- 新增 `references/habit-calibration.md`，规范 confirmed habit、working style signal 和 needs calibration 的记录方式

### Changed

- 更新 `project-memory-playbook` 的读取顺序，将 `memory/habits.md` 纳入默认记忆来源
- 同步更新多平台 agents、README 和 `skills-index.json`，强调读取、校准和更新项目记忆

## [0.3.0] - 2026-08-18

### Added

- 新增 `project-memory-playbook`，用于在项目工作前读取私有 `project-memory` 仓库，并在开发过程中沉淀耐久偏好、风格和项目决策
- 为 `project-memory-playbook` 补齐 OpenAI、Claude、Copilot、Cursor、Gemini 平台适配入口和平台说明

### Changed

- 更新 `skills-index.json` 与 README，将 `project-memory-playbook` 纳入 collaboration 分类

## [0.2.0] - 2026-07-30

### Added

- 为 `java-development-playbook` 增加 MyBatis-Plus、Mapper XML、Lombok 与构造器决策细则
- 增加 Controller 嵌套传输类型、越层依赖、持久化残留、Mapper/XML 和后台权限的架构门禁建议

### Changed

- 明确单体项目在业务边界未稳定时优先采用单应用技术分层，不为未来微服务提前拆模块
- 收紧 Controller、Service、DTO、VO、Entity、Mapper 和事务职责
- 将后台权限划分为 URL 粗边界、方法级角色和必要的写操作前置拒绝
- 补充 Lombok 只替换机械代码、保留业务构造器和领域约束的规则

## [0.1.0] - 2026-06-23

### Added

- 新增 `skills-index.json`，为整仓 skill 提供机器可读索引
- 新增 `CONTRIBUTING.md`，统一目录约定、更新清单和平台中立规则
- 新增仓库级 `CHANGELOG.md`

### Changed

- 收紧 `git-commit-playbook` 的提交正文换行与执行规则
- 为移动端设计与开发 skill 增加反展示板约束
- 增补“新建文件禁止写入平台来源信息”的规范
