# Libraries

## Common Choices

- State：`flutter_bloc`、`riverpod`
- Routing：`go_router`
- Networking：`dio`
- Serialization：`json_serializable`
- Models：`freezed`
- Images：`cached_network_image`
- Storage：`shared_preferences`、`hive`、`isar`
- Utils：`equatable`、`intl`
- Workspace：`melos`

## Rule

- 优先跟随现有项目技术路线
- 中大型项目避免状态管理方案混用过多
- 同类库能少则少，重点是稳定、可维护、团队熟悉
