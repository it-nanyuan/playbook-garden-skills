# Changelog

All notable changes to this repository will be documented in this file.

The format loosely follows Keep a Changelog.

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
