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

## Aggregator Project

项目可以采用简单聚合工程，至少建议有：

- `common`
- 业务项目模块，例如 `project-admin`、`project-api`、`project-service`

## Common Module

- 统一返回体
- 错误码
- 基础异常
- 公共配置
- 工具类
- 通用枚举
- 审计字段基类或基础对象

## Rule

- Controller 不写核心业务
- Service 目录放接口，`service.impl` 放实现
- Service 不直接拼复杂 SQL
- Java 代码里不直接写 SQL 字符串
- Mapper 只负责数据访问
- 复杂查询优先放 `mapper.xml`
- Convert 负责对象转换，不要在各层散写转换代码
- `common` 不承载具体业务实现，只承载真正共享的基础能力

## File Bias

- 一个类一个文件
- 命名直接反映职责
- 公共能力放 `common`、`base` 或明确共享模块，不要到处复制
