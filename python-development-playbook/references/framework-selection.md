# Python Framework And Dependency Selection

## Ask First

- 项目是 API、后台系统、Worker、CLI，还是脚本集合？
- 团队当前使用什么依赖管理方式？
- 是否已有 ORM、缓存、任务队列和日志方案？

## Web Framework

- `FastAPI`
  - 适合现代 API、异步接口、类型提示和自动文档
  - 中大型 API 项目常用

- `Flask`
  - 轻量灵活
  - 适合结构较轻或历史项目

- `Django`
  - 适合后台系统、内容管理、ORM 和 Admin 能力要求较强的项目
  - 需要注意不要把所有逻辑都堆进 `views.py` 或 `models.py`

## Worker

- `Celery`
  - 适合成熟异步任务体系
  - 需要补齐监控、告警、幂等和重试策略

- `RQ`
  - 更轻量
  - 适合简单队列任务

## Dependency Management

- `uv`：更现代、速度快，适合新项目
- `poetry`：常见于需要清晰依赖管理和打包能力的项目
- `pip-tools`：适合强调锁定依赖和兼容现有 `requirements` 流程
- 已有项目优先跟随现有方案，不轻易切换
