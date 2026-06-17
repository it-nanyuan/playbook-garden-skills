# Comments

## Goal

项目重要的不只是把接口写出来，更重要的是后续别人能看懂、敢改、能排障。

## Required

- 类注释：写职责和适用场景
- 方法注释：写参数、返回值、事务、副作用、异常、缓存或消息影响
- 字段注释：写业务含义、单位、状态枚举语义、特殊约束

## Priorities

- Controller 暴露接口
- Service 核心业务
- MQ 消费者
- 定时任务
- ES 同步逻辑
- 缓存更新逻辑

## Avoid

- `// query list`
- `// save data`
- `// update status`

## Good Bias

- 重点写业务规则和边界，不写表面动作
- 复杂分支、兜底逻辑、兼容逻辑附近可补短注释
