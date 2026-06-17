# PHP Testing Standard

## Testing Scope

- Service 核心流程
- Repository 复杂查询
- 参数校验与异常分支
- 支付回调、Webhook、队列任务、定时任务
- DTO / Resource 转换和关键边界条件

## Suggested Tools

- `PHPUnit`
- `Pest`
- 框架提供的测试基类和 HTTP 测试工具

## Rules

- 单元测试聚焦业务规则和边界
- 集成测试验证数据库、缓存、队列、第三方依赖集成点
- 关键接口与支付链路至少要有可重复执行的验证方式
- 测试数据构造统一，不要在每个测试里手写一大堆重复初始化
