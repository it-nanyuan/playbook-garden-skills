# Cursor

## Purpose

Cursor 更适合通过规则文件驱动行为，因此这里提供 `agents/cursor.mdc` 作为第一版接入产物。

## Consumed File

- `agents/cursor.mdc`

## Recommended Use

- 将 `cursor.mdc` 内容放入项目级 Cursor Rules，或作为团队共享规则文件使用
- 适合约束 Cursor 在生成 commit message 时遵守统一前缀和编号正文格式

## Maintenance Notes

- 如果仓库后续拆成多个规则文件，保留这份文件只关注 commit message 场景
- 当 `SKILL.md` 修改前缀集合或输出格式时，同步更新 `cursor.mdc`
