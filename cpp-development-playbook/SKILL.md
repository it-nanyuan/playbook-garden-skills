---
name: cpp-development-playbook
description: Build maintainable C++ services, libraries, desktop modules, and system-level components with clear architecture and coding standards. Use when planning or implementing C++ backends, SDKs, libraries, performance-sensitive modules, desktop components, or system tools, and always clarify whether the project is a library, service, desktop module, algorithm component, or system-level program before choosing module structure, build system, and runtime conventions.
---

# C++ Development Playbook

## Overview

这个 skill 用来为 C++ 项目建立稳定、可维护、偏工程化的开发规范。它默认强调先判断项目形态、构建系统和资源管理方式，再决定模块边界、异常策略、内存与生命周期约束、测试和性能策略。

## Workflow

1. 先确认项目类型：服务端组件、桌面模块、SDK、类库、算法模块，还是系统级工具。
2. 再确认使用 `CMake`、`Bazel`、现有工程系统，还是平台自带工程。
3. 再确认项目是否使用异常、智能指针、协程、线程池、第三方容器或平台框架。
4. 根据业务判断是否需要数据库、缓存、网络库、序列化、IPC 和性能分析工具。
5. 已有项目优先跟随现有编码风格、命名约定、构建规则和目录结构。
6. 编码时必须重视注释、资源管理、边界、测试和稳定性。

## First Question

做 C++ 项目时，第一优先级问题是：

- 这是库、服务、桌面模块、系统工具，还是性能敏感组件？

第二优先级问题是：

- 当前项目使用什么构建系统？是否允许异常？内存管理和线程模型有什么既有约束？

如果用户没说明清楚，就先问；不要直接默认工程规则。

## Core Rules

- 一个类只承担一个主要职责
- 资源获取与释放策略要明确，优先 RAII
- 不把网络、数据库、缓存、算法和业务编排堆进一个类
- 头文件与实现文件职责清晰，避免不必要暴露
- 接口设计优先稳定、清晰和可测试
- 性能优化要有证据，不做没有测量依据的“玄学优化”

## Comments Standard

- 类注释说明职责、边界、所有权和线程安全约束
- 方法注释说明输入、输出、副作用、异常策略和复杂度
- 成员注释重点说明生命周期、所有权、状态值和特殊约束
- 并发逻辑、锁、缓存、对象池、手动内存管理和性能优化优先补齐注释

详细见 `references/comments.md`。  
跨语言注释母规范参考 `comment-style-playbook`。

## Structure Standard

- `include/`：公共头文件
- `src/`：实现
- `tests/`：测试
- `apps/` / `bin/`：可执行入口
- `modules/`：业务模块或领域模块
- `third_party/`：三方依赖接入

详细见 `references/structure.md`。

## API And Error Standard

- 接口边界、错误返回、异常策略和日志策略要统一
- 公共头文件不暴露不必要实现细节
- 明确使用异常、错误码、`expected` 风格还是混合方案

详细见 `references/api-standard.md` 与 `references/error-handling.md`。

## Resource And Concurrency Standard

- 统一资源所有权策略，优先 RAII 和智能指针
- 明确线程模型、锁策略、对象生命周期和并发边界
- 多线程、对象池、缓存和异步任务要特别关注死锁、竞态和释放顺序

详细见 `references/resource-concurrency.md`。

## Logging And Diagnostics

- 日志、断言、诊断信息和崩溃排查策略要统一
- 关键路径、线程切换、I/O、外部依赖和异常场景要可观测

详细见 `references/logging-diagnostics.md`。

## Testing And Performance Standard

- 核心业务、边界条件、错误分支、并发逻辑和性能关键路径要有测试
- 区分单元测试、集成测试、回归测试和 benchmark
- 性能优化要有 profile、基准或压测依据

详细见 `references/testing-performance.md`。

## Security Standard

- 输入边界、文件操作、命令执行、网络协议处理和内存安全风险要统一考虑
- 不在日志和错误信息中泄露敏感数据
- 高风险模块优先减少裸指针和手动资源泄露风险

详细见 `references/security.md`。

## Recommended Stack

- Build：`CMake`
- Testing：`GoogleTest`
- Benchmark：`Google Benchmark`
- Formatting：`clang-format`
- Lint：`clang-tidy`
- Serialization：`protobuf`、`json`
- Logging：项目统一日志方案

详细见 `references/framework-selection.md`。

## When To Use

- 用户要开始一个 C++ 类库、SDK、服务端模块、桌面模块或系统工具项目
- 用户要统一资源管理、异常策略、生命周期、并发边界和测试规范
- 用户要在 `CMake / GoogleTest / clang-format / clang-tidy` 这类常见工具链里建立工程标准
- 用户要做偏性能敏感、系统级或内存管理要求较高的工程

## References

- `references/comments.md`
- `references/structure.md`
- `references/api-standard.md`
- `references/error-handling.md`
- `references/resource-concurrency.md`
- `references/logging-diagnostics.md`
- `references/testing-performance.md`
- `references/security.md`
- `references/framework-selection.md`

## Platform Adapters

- 核心规范始终以当前 `SKILL.md` 为准
- 平台可消费产物放在 `agents/`
- 平台接入说明放在 `references/platforms/`
