# API Standard

## Goal

接口规范的目标不是让 Controller 更漂亮，而是让调用方、前端、测试和后续维护都能预期一致。

## Response

- 统一返回结构
- 统一分页对象
- 统一列表、详情、创建、更新、删除接口风格
- 错误码和错误信息要有稳定策略

## Recommended Conventions

- 返回体统一使用项目级包装对象，例如 `ApiResponse<T>`、`CommonResult<T>` 一类
- 分页对象命名统一，例如 `PageRequest`、`PageResult<T>`，不要同项目里混用多套名字
- 错误码模板要有清晰分段，例如系统类、参数类、权限类、业务类
- 错误信息返回粒度对外保持稳定，对内日志保留更完整上下文

## DTO And VO

- 入参用 DTO
- 出参用 VO
- 不直接把 Entity 裸暴露给外部
- 对象转换统一收敛，不在 Controller 和 Service 到处散写

## Idempotency

- 创建、支付、回调、重试类接口要考虑幂等
- 重复请求的处理方式要明确

## Versioning

- 有长期演进诉求的外部接口要考虑版本策略
- 不要在不兼容改动时直接静默覆盖旧行为
