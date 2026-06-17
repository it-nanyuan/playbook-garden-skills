---
name: dba-playbook
description: Manage database work with strong safety, review, and maintainability standards. Use when planning or executing schema changes, SQL optimization, indexing, backup, restore, migration, or production data operations, especially when the user needs conservative DBA discipline instead of ad hoc SQL changes.
---

# Dba Playbook

## Overview

这个 skill 用来约束数据库相关工作的安全性和可维护性。它默认强调生产安全、变更评估、备份回滚、SQL 审核、索引设计、执行计划分析和注释说明，不接受“先改了再说”的数据库操作方式。

## Workflow

1. 先确认环境：开发、测试、预发还是生产。
2. 先确认任务类型：建表、改表、加索引、改 SQL、数据修复、迁移、备份恢复还是性能排查。
3. 如果是生产环境，优先评估风险、窗口期、备份和回滚方案。
4. 执行前先审 SQL、看执行计划、看影响范围，不盲目直上。
5. 数据变更完成后要检查结果、记录影响、保留回滚或审计信息。

## Core Rules

- 生产数据库操作必须先确认影响范围
- 重要变更必须有备份或可回滚方案
- 大表变更、索引变更、批量更新删除要特别谨慎
- 不能把排查 SQL、修复 SQL、清理 SQL 混着直接执行
- 注释同样重要，表、字段、状态值和复杂 SQL 都应有清晰说明

## Comments Standard

- 表注释：说明业务含义
- 字段注释：说明含义、单位、状态枚举、是否允许为空
- SQL 注释：复杂查询、修复脚本、迁移脚本要写目的和风险
- 索引说明：写清服务于什么查询场景

详细见 `references/comments.md`。

## Common Tasks

- 表结构设计与审查
- 索引设计与优化
- 慢 SQL 分析
- 数据修复与批量变更
- 备份与恢复
- 数据迁移与归档

## Safety Rules

- 生产 `UPDATE` / `DELETE` 默认要求明确 `WHERE`
- 批量变更优先分批执行
- 大表结构变更先评估锁表和执行窗口
- 执行前先看 `EXPLAIN`
- 重要操作前先确认备份、快照或回滚脚本

## Common Database Stack

- 关系型数据库：`MySQL`、`PostgreSQL`
- 缓存 / 键值：`Redis`
- 搜索分析：`Elasticsearch`
- 数据库连接池与中间层：按项目现状选择 `HikariCP`、`ProxySQL`、`ShardingSphere`
- 迁移工具：`Flyway`、`Liquibase`

## Common DBA Tools

- SQL 客户端：`DataGrip`、`DBeaver`、`Navicat`
- 备份恢复：`mysqldump`、`xtrabackup`、云厂商快照或托管备份
- 性能排查：`EXPLAIN`、慢查询日志、`pt-query-digest`
- 表结构与数据比对：`pt-online-schema-change`、`gh-ost`、数据比对工具
- 监控：`Prometheus`、`Grafana`、云监控或数据库托管平台监控

详细见 `references/tools.md`。

## When To Use

- 用户要做数据库设计、SQL 优化、索引调整
- 用户要执行数据修复、迁移、清理或恢复
- 用户要建立 DBA 工作规范
- 用户需要生产数据库安全操作约束

## References

- `references/comments.md`
- `references/safety.md`
- `references/schema.md`
- `references/performance.md`
- `references/tools.md`

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
