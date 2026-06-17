# Go Cache And Messaging Standard

## Cache

- Redis key 前缀统一体现系统、环境、业务域和资源语义
- TTL 不能随意写死，热点缓存、详情缓存、统计缓存分开设计
- 先删缓存还是先更新数据库，要在项目级统一
- Cache miss、击穿、穿透和雪崩风险要有明确处理策略

## Messaging

- topic、consumer group、stream、subject 命名统一
- 消费逻辑必须幂等，重试策略、超时和失败转移方式要明确
- 大任务要拆分，避免一个消息承载过重业务
- 关键事件流要有可追踪 ID，便于串联日志和排查链路

## Common Scenarios

- 订单类事件：优先保证幂等和顺序性要求
- 统计类事件：允许异步聚合，但要明确延迟容忍度
- 回调型消费：先验签或校验来源，再做状态更新
