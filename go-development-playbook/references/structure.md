# Structure

## Common Layout

- `cmd/`
- `internal/`
- `pkg/`
- `api/`
- `configs/`

## Split Rules

- handler 只处理协议层
- service 只处理业务编排
- repository 只处理数据访问
- client 只处理外部依赖
- 不把所有逻辑堆在一个 package
