---
name: python-development-playbook
description: Build maintainable Python services with clear engineering standards. Use when planning or implementing Python backend services, APIs, workers, automation tools, or data-adjacent application code that needs strong structure, comments, testing, dependency discipline, and maintainable module boundaries.
---

# Python Development Playbook

## Overview

这个 skill 用来为 Python 服务和应用代码建立稳定、可维护的工程规范。它默认强调模块职责、注释、类型意识、测试、依赖管理和运行时边界，而不是把脚本、业务逻辑、数据库访问和外部调用全部堆在一个文件里。

## Workflow

1. 先判断项目类型：API 服务、任务 worker、自动化工具、CLI、数据处理服务还是脚本集合。
2. 如果是已有项目，先跟随现有框架、依赖管理和目录结构。
3. 新增需求前先判断属于 router、service、repository、schema、task、client 还是 shared module。
4. 优先按模块职责拆分代码，不让单个 `app.py` 或 `service.py` 无限膨胀。
5. 编码时重视注释、错误处理、测试、配置管理和依赖约束。

## Core Rules

- 模块职责清晰，不把接口层、业务层、数据层和第三方调用层揉在一起
- 优先写可维护的模块，而不是只追求“脚本先跑起来”
- 公共逻辑优先抽 shared module，不复制粘贴
- 关键函数、公共类、复杂业务流程和副作用逻辑要有注释
- 依赖和环境管理要统一，不同模块不各自发明一套运行方式
- 数据库访问、外部请求、配置读取和任务调度要有清晰边界

## Comments Standard

- 模块、类、公共函数优先补职责注释
- 方法注释重点写输入、输出、副作用、异常行为和边界条件
- 字段注释只在业务语义、单位、状态值或约束不明显时写
- 异步任务、重试、缓存、回调、批处理和复杂数据转换优先补齐注释

详细注释规范见 `references/comments.md`。  
跨语言注释母规范参考 `comment-style-playbook`。

## Structure Standard

- `app/` 或业务主包承载应用代码
- `api/`：接口层或路由层
- `service/`：业务编排
- `repository/`：数据访问
- `schema/` 或 `models/`：数据结构
- `client/`：第三方依赖调用
- `tasks/`：异步任务或调度任务
- `common/` 或 `shared/`：公共能力

详细见 `references/structure.md`。

## API And Error Standard

- 返回结构、分页对象、错误响应和校验失败风格要统一
- API 层不承载完整业务实现
- 参数错误、业务错误、权限错误、系统错误要有清晰区分

详细见 `references/api-standard.md` 与 `references/error-handling.md`。

## Testing Standard

- 核心业务、边界条件、异常分支、数据转换和关键任务逻辑要有测试
- 区分单元测试、集成测试和关键链路验证
- 不追求无意义覆盖率，但核心流程不能裸奔

详细见 `references/testing.md`。

## Security And Dependency Standard

- 敏感配置、权限边界、参数校验、外部调用超时和重试要统一
- 依赖管理优先统一工具链和锁文件，不允许环境漂移过大
- 不在日志、异常或响应中泄露敏感信息

详细见 `references/security.md` 与 `references/dependencies.md`。

## Recommended Stack

- API：`FastAPI`、`Flask`、`Django` 按项目现状选择
- Validation / Schema：`pydantic`
- ORM / DB：`SQLAlchemy`、`Django ORM`
- Cache：`redis-py`
- Async / Worker：`Celery`、`RQ`
- HTTP Client：`httpx`、`requests`
- Config：`pydantic-settings`、`.env` 方案
- Testing：`pytest`
- Logging：标准库 `logging` 或结构化日志方案

详细见 `references/libraries.md`。

## When To Use

- 用户要开始一个 Python 服务、API、worker 或工具项目
- 用户要统一 Python 项目的结构、注释、测试和依赖规范
- 用户要为 FastAPI / Flask / Django 类服务建立工程标准
- 用户要选择 Python 常用框架和基础库

## References

- `references/comments.md`
- `references/structure.md`
- `references/api-standard.md`
- `references/error-handling.md`
- `references/testing.md`
- `references/security.md`
- `references/dependencies.md`
- `references/libraries.md`

## Platform Adapters

如果需要把这个 skill 接到不同平台：

- 核心规范始终以当前 `SKILL.md` 为准
- 平台可消费产物放在 `agents/`
- 平台接入说明放在 `references/platforms/`

优先查看：

- `references/platforms/README.md`
- `references/platforms/openai.md`
- `references/platforms/claude.md`
- `references/platforms/cursor.md`
- `references/platforms/gemini.md`
- `references/platforms/copilot.md`
