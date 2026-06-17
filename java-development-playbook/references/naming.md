# Naming

## Goal

命名的目标是降低理解成本，让人不用跳来跳去猜职责。

## Rule

- 类名体现职责
- 方法名体现动作
- DTO、VO、Entity、Enum、Convert 命名直接反映用途
- 常量名表达业务含义，不只表达技术类型
- 包名保持稳定，不频繁改来改去

## Good Bias

- `OrderCreateRequest` 比 `OrderDTO` 更明确时优先更明确命名
- `OrderStatusEnum` 比 `StatusEnum` 更稳定
- `UserLoginService` 比 `UserService2` 更可维护

## Avoid

- 模糊缩写
- 同一含义多个名字
- 一个名字在不同层代表不同东西

## MQ Naming

- Topic、Tag、Consumer Group、消息 Key 都要体现业务语义
- 命名建议至少体现：系统、业务域、动作
- 示例：
  - Topic：`order-status-change`
  - Tag：`paid`
  - Consumer Group：`order-status-sync-group`
- 不使用 `test-topic`、`demo-tag`、`group1` 这类无语义命名
