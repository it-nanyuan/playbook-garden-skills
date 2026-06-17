# Go Framework And Stack Selection

## Ask First

- 当前项目是 API、微服务、Worker、CLI，还是基础设施工具？
- 团队更偏向轻量标准库，还是依赖成熟生态快速交付？
- 当前是否已有统一日志、配置、数据库和中间件方案？

## HTTP Layer

- `gin`
  - 适合多数业务 API、后台服务和团队协作项目
  - 生态成熟，中间件丰富

- `echo`
  - 适合追求直接开发体验和较轻学习成本的项目
  - 对中小型服务足够实用

- `chi`
  - 更轻量、更接近标准库风格
  - 适合希望中间件和路由组合更可控的项目

- 标准库 `net/http`
  - 适合基础设施工具、轻服务或团队已有强公共基建时
  - 需要自行补齐更多规范和封装

## Database Layer

- `gorm`
  - 开发效率高
  - 复杂查询和性能敏感场景要更谨慎

- `sqlx`
  - 更贴近 SQL
  - 适合强调查询可控、开发者具备 SQL 能力的团队

- `ent`
  - 类型安全和 schema 管理更强
  - 适合大型长期维护项目

## Logging And Config

- 日志优先统一一种：`zap`、`zerolog` 或 `slog`
- 配置优先统一一种：`viper` 或团队已有配置封装
