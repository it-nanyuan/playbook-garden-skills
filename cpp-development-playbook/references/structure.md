# C++ Structure Standard

- `include/`：公共头文件
- `src/`：实现
- `tests/`：测试
- `apps/` / `bin/`：入口
- `modules/`：模块划分
- `third_party/`：三方依赖

规则：

- 头文件不暴露不必要实现
- 模块边界稳定
- 实现细节尽量放到 `src/`
