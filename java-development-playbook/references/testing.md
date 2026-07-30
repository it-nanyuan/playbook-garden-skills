# Testing

## Goal

测试不是为了凑覆盖率，而是为了保护核心业务规则和重构安全。

## Focus

- 核心业务流程
- 幂等逻辑
- 状态流转
- 数据转换
- 参数边界
- 异常分支

## Rule

- 核心领域逻辑优先单元测试
- 数据访问、事务、集成链路按需要做集成测试
- 关键接口变更后至少做核心链路验证
- 批量架构改造先记录基线，再用静态门禁或架构测试阻止指标回退
- MyBatis 改造要验证 Entity 反射实例化、Mapper 接口、XML statement 和数据库迁移
- Lombok 构造器改造要执行编译和持久化集成测试，不能只依赖 IDE 无报错
- Spring Security 改造要验证角色矩阵，以及无权请求是否在参数校验前返回 403

## Architecture Gate

可按项目需要检查：

- Controller 中不存在嵌套 Request、View、DTO、VO
- Controller 不依赖 Mapper、Repository、Service 实现类
- `service` 只放契约，`service.impl` 只放实现
- MyBatis 项目不存在 JPA 引用、Repository 文件和 Java 内联 SQL
- 每个自定义 Mapper 方法都有对应 XML statement，XML 不存在孤儿 statement
- Entity 不再手写空无参构造，Spring 组件不再手写纯赋值依赖注入构造器
- 后台路由不存在遗漏 `@PreAuthorize` 的 handler

已有项目无法一次清零时，记录当前数值并采用只降不升的 ratchet；不要因为门禁暂时不完美而放弃建立约束。

## Avoid

- 只测 happy path
- 复杂规则完全不测
- 测试名称看不出业务意图
- 只跑编译，不跑 Mapper、权限和核心业务集成测试
