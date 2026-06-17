# Melos

## When To Use

只要 Flutter 项目进入中大型阶段，或存在多个 feature、shared、core package，就优先使用 `melos`。

## Why

- 统一管理 workspace
- 统一 bootstrap、lint、test、format、gen 命令
- 让 package 依赖关系更清楚
- 降低多人协作时的脚本分裂

## Suggested Packages

- `app_main`
- `feature_order`
- `feature_user`
- `shared_ui`
- `shared_utils`
- `core_network`
- `core_storage`
- `bridge_host`

## Rule

- 新功能先判断放进已有 package 还是新建 feature package
- 不要让 `app` 直接承载所有业务
- 不要把临时代码长期留在壳工程里
