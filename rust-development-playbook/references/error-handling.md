# Rust Error Handling Standard

- 区分参数错误、业务错误、权限错误、系统错误和第三方依赖错误
- `Result` 语义要清晰，不用模糊错误兜底一切
- 公共错误类型、错误转换和对外错误映射统一
