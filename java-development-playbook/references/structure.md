# Structure

## Common Packages

- `controller`
- `service`
- `service.impl`
- `manager`
- `mapper`
- `entity`
- `dto`
- `vo`
- `convert`
- `config`
- `job`
- `consumer`

## Monolith Layout

业务边界尚未稳定的单体项目优先保持一个应用模块：

- `controller` 只负责 HTTP 边界
- `service` 只放接口，`service.impl` 放实现
- `manager` 承担跨资源或外部能力协调
- `mapper` 和 `mapper.xml` 承担数据访问
- `entity`、`dto`、`vo`、`convert` 分开
- `common` 只作为共享 package，不强制拆成独立构建模块

不要为了未来可能拆微服务，提前创建没有独立职责的业务顶层 package。只有存在稳定领域边界、独立构建或交付诉求时，才采用聚合工程。

## Common Module

- 统一返回体
- 错误码
- 基础异常
- 公共配置
- 工具类
- 通用枚举
- 审计字段基类或基础对象

## Rule

- Controller 只做参数校验、认证上下文获取、Service 调用和统一响应组装
- Controller 不直接依赖 Mapper、Service 实现类或持久化查询对象
- Controller 内不定义 Request、Response、View、DTO、VO 等嵌套类型
- Request / Command 放 `dto`，对外展示对象放 `vo`，每个顶层类型独立文件
- Service 目录放接口，`service.impl` 放实现
- Service 实现负责业务编排和事务边界，Controller 不承担事务
- Service 不直接拼复杂 SQL
- Java 代码里不直接写 SQL 字符串
- Mapper 只负责数据访问
- 复杂查询优先放 `mapper.xml`
- Convert 负责对象转换，不要在各层散写转换代码
- `common` 不承载具体业务实现，只承载真正共享的基础能力
- Spring 组件只有 `final` 依赖时优先用 `@RequiredArgsConstructor`，不要保留纯赋值依赖注入构造器

## File Bias

- 一个类一个文件
- 命名直接反映职责
- 公共能力放 `common`、`base` 或明确共享模块，不要到处复制
- 创建 DTO / VO 前先搜索已有类型，只复用语义和校验约束完全一致的模型
