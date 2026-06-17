---
name: devops-playbook
description: Operate applications and environments with strong safety and maintainability standards. Use when planning or executing deployment, CI/CD, environment management, monitoring, logging, rollback, configuration, container, or service availability work, especially when the user needs disciplined DevOps procedures instead of ad hoc operations.
---

# Devops Playbook

## Overview

这个 skill 用来约束运维和交付工作的稳定性。它默认强调环境隔离、变更审核、发布回滚、监控告警、日志可观测性、配置管理和操作留痕，不接受“先上线试试”的粗放运维方式。

## Workflow

1. 先确认环境：开发、测试、预发、生产。
2. 先确认任务类型：部署、发布、扩缩容、配置调整、证书、域名、监控、日志、故障处理还是回滚。
3. 如果是生产操作，先确认变更窗口、回滚方案、影响范围和负责人。
4. 执行前先确认健康检查、依赖服务、配置差异和监控状态。
5. 执行后要验证服务健康、核心链路、日志和告警。

## Core Rules

- 生产变更必须有回滚方案
- 环境配置必须可追踪，不允许口头配置
- 重要发布前后都要做健康检查
- 监控、日志、告警是基础能力，不是可选项
- 运维文档和注释同样重要，尤其是脚本、配置项和故障处理步骤

## Comments Standard

- 部署脚本要说明用途、参数、影响范围
- 配置项要写业务含义和环境差异
- 监控规则和告警阈值要写原因
- 故障处理步骤要写前置条件和影响

详细见 `references/comments.md`。

## Common Areas

- CI/CD
- 容器与镜像
- 环境配置
- 监控与告警
- 日志与可观测性
- 发布与回滚
- 故障处理与恢复

## Safety Rules

- 生产发布前检查依赖服务状态
- 回滚脚本或回滚版本必须提前准备
- 敏感配置和密钥必须规范管理
- 不直接在生产手改长期配置
- 重大操作要保留记录和结果验证

## Common DevOps Stack

- CI/CD：`Jenkins`、`GitHub Actions`、`GitLab CI`
- Containers：`Docker`
- Orchestration：`Kubernetes`
- Reverse Proxy / Gateway：`Nginx`、云负载均衡
- Artifact / Image Registry：`Harbor`、云镜像仓库
- IaC / Provisioning：`Terraform`、`Ansible`

## Common Operations Tools

- 日志：`ELK` / `EFK`
- 监控：`Prometheus`、`Grafana`
- 链路：`SkyWalking`、`Jaeger`
- 告警：`Alertmanager`、企业 IM / Pager 工具
- 发布与集群管理：`kubectl`、`Helm`
- 密钥与配置：云密钥管理、配置中心、Secret 管理方案

详细见 `references/tools.md`。

## Docker Standard

- 镜像构建必须可复现，避免手工改容器后直接当结果使用
- `Dockerfile` 要清楚、分层合理、尽量控制镜像体积
- 运行时配置通过环境变量、配置挂载或 Secret 管理，不把敏感配置写死进镜像
- 基础镜像、JDK 版本、时区、字符集和启动参数应尽量统一

详细见 `references/docker.md`。

## Kubernetes Standard

- `K8s` 已经纳入这套规范，不只是写了名字，推荐用明确的资源模板和发布约束
- Deployment、Service、Ingress、ConfigMap、Secret、HPA、Job 等资源职责要清楚
- 就绪探针、存活探针、资源限制、滚动发布、命名空间隔离和日志采集要有默认标准
- 不直接在生产集群手改长期配置，优先通过 GitOps、Helm 或受控发布流程落变更

详细见 `references/kubernetes.md`。

## When To Use

- 用户要做部署、发布、运维、监控、回滚或环境配置
- 用户要建立标准化运维流程
- 用户要统一脚本、配置、监控和日志规范
- 用户需要更稳的生产操作约束

## References

- `references/comments.md`
- `references/deployment.md`
- `references/observability.md`
- `references/configuration.md`
- `references/tools.md`
- `references/docker.md`
- `references/kubernetes.md`

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
