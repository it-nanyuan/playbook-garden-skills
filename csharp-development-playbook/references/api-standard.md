# C# API Standard

- 返回结构、错误码、分页对象和 trace 字段统一
- Controller / Endpoint 负责协议层，不负责完整业务编排
- DTO、分页、列表、详情、导入导出接口风格一致
- 高权限接口、批量接口和回调接口明确幂等和鉴权要求
