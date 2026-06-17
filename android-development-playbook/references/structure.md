# Structure

## File Rules

- 一个文件一个主类型
- Compose 页面、状态对象、事件对象、ViewModel、Repository 分开
- 不把 Activity、Adapter、网络和数据映射塞进一个文件

## Suggested Split

- `OrderListScreen.kt`
- `OrderListViewModel.kt`
- `OrderListState.kt`
- `OrderListEvent.kt`
- `OrderRepository.kt`
- `OrderRemoteDataSource.kt`
- `OrderMapper.kt`

## Reuse Bias

- 列表项、状态组件、筛选容器、空状态优先抽成可复用组件
- 领域逻辑优先沉淀 `UseCase`
- 通用数据转换优先抽 `Mapper`
