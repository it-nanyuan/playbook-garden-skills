# Stack Selection

## Common Base

- `Spring Boot`
- `Lombok`
- `MyBatis-Plus`
- `mapper.xml`
- `MySQL`
- `Redis`

## Monolith Recommendation

- `Spring Boot`
- `Lombok`
- `MyBatis-Plus`
- `mapper.xml`
- `MySQL`
- `Redis`
- `springdoc-openapi`
- `jakarta validation`

适合：

- 中小型业务系统
- 团队规模有限
- 部署链路希望简单

## Microservices Recommendation

- `Spring Boot`
- `Spring Cloud` 或 `Spring Cloud Alibaba`
- `Nacos` / `Eureka`
- `OpenFeign`
- `Spring Cloud Gateway`
- `Sentinel` / `Resilience4j`
- `Redis`
- `MySQL`
- `RabbitMQ` / `RocketMQ` / `Kafka`
- `XXL-Job`
- `SkyWalking` / `Micrometer`

适合：

- 多服务协作
- 业务边界清晰
- 需要独立部署和治理能力

## Add As Needed

- 搜索：`Elasticsearch`
- 异步消息：`RabbitMQ`、`RocketMQ`、`Kafka`
- API 文档：`springdoc-openapi`
- 参数校验：`jakarta validation`
- 任务调度：`Spring Scheduling`
- 鉴权：`Spring Security`、`Sa-Token`、`JWT`
- 注册中心 / 配置中心：`Nacos`、`Eureka`、`Apollo`
- 服务调用：`OpenFeign`
- 网关：`Spring Cloud Gateway`
- 限流熔断：`Sentinel`、`Resilience4j`
- 分布式事务：`Seata`
- 链路追踪：`SkyWalking`、`Zipkin`

## Rule

- 根据项目目标选择，不为“完整”而全加
- 先判断业务场景，再决定要不要 MQ、ES、搜索、同步任务
- 先确认单体还是微服务，再决定是否引入治理类组件
