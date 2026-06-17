# Structure

## File Rules

- 一个文件一个主 widget / 主类
- 大 widget 拆成局部 widget
- 页面、controller、state、service、repository、model、route 分开

## Suggested Split

- `order_list_page.dart`
- `order_list_view.dart`
- `widgets/order_filter_bar.dart`
- `widgets/order_table.dart`
- `bloc/order_list_cubit.dart`
- `models/order_item.dart`
- `repository/order_repository.dart`

## Package Bias

- `app_*`：壳工程
- `feature_*`：业务功能
- `shared_*`：跨业务组件和工具
- `core_*`：网络、存储、日志、配置
- `bridge_*`：原生桥接能力
