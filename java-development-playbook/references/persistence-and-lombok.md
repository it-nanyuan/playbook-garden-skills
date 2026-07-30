# Persistence And Lombok

## Stack Boundary

- 先确认项目使用 `MyBatis-Plus`、JPA 还是其他持久化方案，再改数据访问层。
- 项目明确选择 `MyBatis-Plus` 时，不要保留或新增 JPA Entity 注解、Repository、Specification 等旁路。
- 不要为了“框架完整”同时维护 MyBatis 和 JPA 两套持久化模型。

## MyBatis-Plus

- 基础 CRUD 可复用 `BaseMapper<T>`，自定义查询和写入通过语义明确的 Mapper 方法表达。
- 复杂查询、动态 SQL、联表、批量写入和数据库特性 SQL 放在 `mapper.xml`。
- Java 业务代码和 Mapper 注解里不要散落 SQL 字符串。
- Mapper XML 的 `namespace` 必须匹配接口全限定名，自定义方法必须有同名 statement。
- 列名和属性名不完全一致、查询结果复杂或需要稳定映射时，显式定义 `resultMap`。
- Entity 与 Mapper、Mapper XML 的覆盖关系应可检查，避免只建接口、不建 XML 或 XML 存在孤儿 statement。

## Lombok Decision

按语义选择 Lombok，不要只追求文件更短：

| 场景 | 推荐做法 |
| --- | --- |
| Spring 组件只有 `final` 依赖注入 | 使用 `@RequiredArgsConstructor` |
| 类中只有样板日志字段 | 使用 `@Slf4j` |
| 简单持久化模型需要访问器 | 项目约定允许时使用 `@Data`，否则组合 `@Getter` / `@Setter` |
| MyBatis Entity 已存在业务构造器 | 使用 `@NoArgsConstructor(access = AccessLevel.PROTECTED)` 提供反射入口 |
| 构造器覆盖本类全部字段且只做同名赋值 | 可以使用 `@AllArgsConstructor` |
| 构造器设置默认状态、时间、版本或执行校验 | 保留显式业务构造器 |

## Constructor Boundary

- MyBatis 反射实例化需要可用无参构造；优先让 Lombok 生成受保护无参构造，不要在每个 Entity 中手写空方法。
- `@AllArgsConstructor` 只替代机械的全字段赋值构造器，不替代业务构造器。
- 不要为了删除构造器而把领域字段改成 `final`，也不要用类级 `@Builder` 绕过状态初始化和业务校验。
- 新增字段后重新检查 `@AllArgsConstructor` 的调用语义；如果“全部字段”已不再代表合法创建入口，就恢复显式业务构造器。
- Entity 继承基础审计对象时，明确 `equals`、`hashCode` 和 `toString` 是否应包含父类字段，不要仅为消除 Lombok 警告改变相等性语义。

## Mechanical Simplification

- 只删除可证明等价的样板代码。
- 批量替换前先把构造器分类为：空构造、全字段赋值构造、业务构造。
- 批量替换后至少执行编译、Mapper 集成测试和核心业务测试。
- 可增加静态守卫，禁止重新出现手写空 Entity 构造器、手写依赖注入构造器和手写 logger。
