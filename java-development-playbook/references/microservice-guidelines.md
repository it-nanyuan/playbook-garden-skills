# Microservice Guidelines

## Split Rules

- 按业务域拆分服务
- 按团队协作边界和发布边界拆分
- 不按数据库表数量机械拆服务

## Calling Rules

- 同步调用链不要无限拉长
- 超时、重试、降级、幂等要统一约束
- Feign 调用要重视 fallback 和失败语义

## Infrastructure Rules

- 注册中心、配置中心、网关、限流熔断、链路追踪要统一方案
- MQ 用于异步解耦，不用来掩盖糟糕的服务边界
- 分布式事务只在必要时引入，优先考虑最终一致性

## Good Bias

- 服务职责小而清楚
- 依赖关系尽量稳定
- 治理组件按真实复杂度引入，不为“高级”而堆砌
