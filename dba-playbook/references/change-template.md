# 数据库变更模板

数据库相关交付默认尽量使用下面这类结构，方便评审、执行和回滚：

1. 变更目标
2. 影响环境
3. 影响表 / 库 / 数据范围
4. 执行 SQL 或迁移步骤
5. 风险说明
6. 备份方式
7. 回滚 SQL 或回滚步骤
8. 验证 SQL
9. 执行结果记录

示例骨架：

```text
变更目标：
为订单表补充支付流水号索引，降低支付结果回查延迟。

影响环境：
预发、生产

影响对象：
trade_order.payment_serial_no

执行 SQL：
ALTER TABLE trade_order ADD INDEX idx_payment_serial_no (payment_serial_no);

风险说明：
大表加索引存在执行窗口要求，需要避开交易高峰。

备份方式：
提前保留库级快照，并记录执行前索引状态。

回滚 SQL：
ALTER TABLE trade_order DROP INDEX idx_payment_serial_no;

验证 SQL：
SHOW INDEX FROM trade_order;
EXPLAIN SELECT * FROM trade_order WHERE payment_serial_no = ?;
```
