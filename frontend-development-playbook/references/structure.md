# Structure

## Common Layers

- `pages`
- `components`
- `layouts`
- `hooks`
- `services` / `api`
- `stores`
- `types`
- `utils`
- `constants`

## Rule

- 一个文件一个主组件
- 页面负责拼装，不负责承载全部业务逻辑
- 请求、状态、格式化、权限、映射尽量拆层
- 通用业务容器优先沉淀复用

## Reuse Bias

- 通用表格、筛选区、分页容器、弹窗表单优先抽象
- 相似业务流程优先抽 hooks
- 字典映射、格式化、权限判断优先共享
