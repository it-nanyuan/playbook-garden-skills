# Kubernetes

## Goal

Kubernetes 规范的目标是让集群内应用发布、伸缩、配置和恢复都有稳定约束。

## Common Resources

- `Deployment`
- `StatefulSet`
- `Service`
- `Ingress`
- `ConfigMap`
- `Secret`
- `Job` / `CronJob`
- `HPA`

## Rule

- 资源命名清晰统一
- namespace 划分明确
- `requests` / `limits` 要有合理默认值
- readiness / liveness probe 不省略
- 日志采集和监控暴露要有默认接入方案
- 发布优先走滚动发布或受控发布，不直接手工替换 Pod

## Good Bias

- 配置通过 `ConfigMap` / `Secret` 管理
- 发布通过 `Helm`、GitOps 或标准流水线管理
- 集群问题排查优先看事件、探针、日志、资源限制和依赖服务状态
