# C# Cache And Messaging Standard

- Redis key、queue、topic、consumer group 命名统一
- 缓存更新、失效和数据库一致性策略要统一
- 消费逻辑必须考虑幂等、重试、死信和失败告警
- 长任务拆分处理，不在单个消息里堆过重业务
