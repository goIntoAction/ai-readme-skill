#!/usr/bin/env python3
"""
AI README Generator - Python version
Generates AI-friendly project documentation
"""

import os
import sys
import json
import glob
import argparse
from pathlib import Path
from datetime import datetime

# Progressive guide template - 放在每个文档开头
PROGRESSIVE_GUIDE = """<!--
┌─────────────────────────────────────────────────────────────────┐
│                    🤖 AI 渐进式补全指南                          │
├─────────────────────────────────────────────────────────────────┤
│ 本文档采用渐进式补全，请按以下步骤填充内容：                        │
│                                                                 │
│ 【第一步：快速扫描】                                             │
│   - 使用 Glob 找到相关文件                                       │
│   - 使用 Grep 搜索关键模式                                       │
│   - 建立文件与功能的对应关系                                     │
│                                                                 │
│ 【第二步：深入阅读】                                             │
│   - 使用 Read 读取关键文件完整内容                                │
│   - 理解代码逻辑和设计意图                                       │
│   - 追踪调用链和依赖关系                                         │
│                                                                 │
│ 【第三步：归纳总结】                                             │
│   - 用自然语言描述发现的内容                                     │
│   - 绘制必要的图表辅助说明                                       │
│   - 补充细节和示例代码                                           │
│                                                                 │
│ 【业务维度提取】                                                 │
│   - 搜索硬编码的数字：timeout=30, limit=100, expire=7*24*3600    │
│   - 查找配置类中的常量字段                                        │
│   - 分析 @Value 注解读取的配置项                                  │
│   - 查找枚举类中的状态定义                                        │
│   - 识别触发状态变更的事件                                        │
│   - 查找参数校验的边界值                                          │
│                                                                 │
│ 【输出要求】                                                     │
│   - 每个段落至少 3-5 句话，避免单句段落                           │
│   - 每个模块/接口/函数的描述要包含：是什么、为什么、怎么用         │
│   - 代码示例要有上下文和注释说明                                 │
│   - 表格中的每一项都要有具体内容，不能是"待分析"                  │
│   - 每个业务规则都要有具体的数值和代码位置                         │
│   - 每个状态都要有明确的含义和触发条件                             │
└─────────────────────────────────────────────────────────────────┘
-->
"""

# Document templates - 详细的 TS 版本模板内容
TEMPLATES = {
    "project-structure": """{progressive_guide}
# 项目结构

## 基本信息

| 项目 | 值 |
|------|-----|
| **项目名称** | {name} |
| **根目录** | `{root_path}` |
| **扫描时间** | {scan_time} |
| **语言** | {languages_str} |

## 快速导航

- [模块划分](#模块划分)
- [目录结构](#目录结构)
- [入口文件](#入口文件)
- [配置文件](#配置文件)

---

## 模块划分

{modules}

---

## 模块详细分析

> 🤖 **AI 填充指南**：针对每个模块，请按以下结构输出：
>
> 1. **职责概述**（2-3 句话）：这个模块是做什么的？在整体架构中扮演什么角色？
> 2. **关键文件说明**（表格形式）：列出核心文件，说明每个文件的作用
> 3. **依赖关系**（文字描述 + 可选图表）：依赖哪些模块？被哪些模块依赖？
> 4. **设计特点**（1-2 句话）：有什么特别的设计模式或注意事项？

### 主要模块

> 🤖 AI 待分析：读取源文件后补充模块详细分析

**职责概述**: 🤖 AI 待填充

**关键文件**:

| 文件 | 作用 |
|------|------|
| 🤖 AI 待填充 | 🤖 AI 待填充 |

**依赖关系**:

- **依赖**: 🤖 AI 待分析
- **被依赖**: 🤖 AI 待分析

---

## 目录结构

```
{directory_tree}
```

> 🤖 **AI 待填充**：对目录结构进行简要说明，解释各主要目录的用途和组织逻辑

---

## 入口文件

{entry_points_str}

> 🤖 **AI 填充指南**：分析每个入口文件：
> 1. 这个入口是做什么的？（主入口 / CLI 入口 / 测试入口 等）
> 2. 启动时做了哪些初始化工作？
> 3. 关键代码片段（带注释）

<!--
🤖 AI 填充示例：

### main.ts（主入口）

**作用**：应用主入口，负责启动 HTTP 服务器和初始化核心模块。

**初始化流程**：
1. 加载环境变量配置
2. 创建 NestJS 应用实例
3. 注册全局中间件（日志、错误处理、CORS）
4. 连接数据库
5. 启动监听端口

**关键代码**：
```typescript
async function bootstrap() {{
  const app = await NestFactory.create(AppModule);
  app.useLogger(new CustomLogger());  // 自定义日志
  app.enableCors({{ origin: config.corsOrigins }});  // CORS 配置
  await app.listen(3000);
}}
```
-->

🤖 AI 待填充

---

## 配置文件

> 🤖 **AI 探索提示**：
> - 找 package.json, build.gradle.kts, pom.xml, go.mod, Cargo.toml
> - 分析项目依赖和脚本命令

<!--
🤖 AI 填充示例：

### package.json

**路径**: `package.json`

**内容解析**：
- `name`: "my-project" - 项目名称
- `scripts.dev`: 开发环境启动命令
- `dependencies`: 核心运行时依赖
- `devDependencies`: 开发工具依赖

**关键配置说明**：
- 使用 TypeScript 编译，输出到 dist 目录
- 测试框架使用 Jest，覆盖率报告输出到 coverage 目录
- ESLint 配置继承自 @typescript-eslint/recommended
-->

**配置文件位置**: 🤖 AI 待查找

---

*此文档由 AI README 生成骨架 - 等待 AI 使用 Read/Glob/Grep 工具分析源文件后填充*
""",

    "tech-architecture": """{progressive_guide}
# 技术架构

> 🤖 **AI 填充指南**：本章需要分析项目的技术选型和架构设计，请按以下步骤渐进式填充：
>
> **第一步**：读取配置文件，列出所有依赖
> **第二步**：分析源码目录结构，推断架构模式
> **第三步**：追踪 import 语句，绘制依赖关系
> **第四步**：总结技术决策和权衡

## 技术栈总览

### 编程语言

| 语言 | 文件数 | 主要用途 |
|------|--------|----------|
{languages_table}

### 框架与库

> 🤖 **AI 探索提示**：
> - 前端：读取 package.json 的 dependencies 和 devDependencies
> - 后端：读取 package.json / build.gradle.kts / pom.xml / go.mod / Cargo.toml
> - 客户端：读取 build.gradle / Podfile / Package.swift / pubspec.yaml

<!--
🤖 AI 填充示例：

#### 核心框架

| 框架 | 版本 | 用途 |
|------|------|------|
| NestJS | ^10.0.0 | 后端框架，提供依赖注入、模块化架构 |
| TypeORM | ^0.3.0 | ORM 框架，处理数据库操作 |
| class-validator | ^0.14.0 | 数据校验，配合 DTO 使用 |

#### 工具库

| 库 | 版本 | 用途 |
|------|------|------|
| lodash | ^4.17.21 | 通用工具函数 |
| dayjs | ^1.11.0 | 日期处理 |
| uuid | ^9.0.0 | 唯一 ID 生成 |

#### 为什么选择这些技术？
- 选择 NestJS 是因为其完善的依赖注入和模块化设计，适合中大型项目
- TypeORM 支持 TypeScript 类型推断，与 NestJS 集成良好
- 整体技术栈以 TypeScript 为主，保证类型安全
-->

#### 核心依赖

| 依赖 | 版本 | 用途 |
|------|------|------|
| 🤖 AI 待填充 | 🤖 AI 待填充 | 🤖 AI 待填充 |

#### 技术选型理由

🤖 AI 待填充

---

## 架构分层

> 🤖 **AI 探索提示**：
> - 看到 Intent/State/Event → 可能是 MVI
> - 看到 ViewModel + LiveData/StateFlow → 可能是 MVVM
> - 看到 Controller/Service/Repository → 可能是分层架构
> - 看到 domain/data/presentation 目录 → 可能是整洁架构
> - 看到 pages/components/hooks → 可能是 React/Vue 组件化架构
> - 看到 routes/handlers/middleware → 可能是后端路由分层

<!--
🤖 AI 填充示例：

项目采用经典的分层架构（Layered Architecture），分为以下四层：

```mermaid
graph TB
    subgraph 表现层
        A[Controllers / Routes]
    end
    subgraph 业务层
        B[Services / Use Cases]
    end
    subgraph 数据层
        C[Repositories / DAO]
    end
    subgraph 基础设施层
        D[Database / Cache / MQ]
    end
    A --> B
    B --> C
    C --> D
```

### 各层职责

| 层级 | 目录 | 职责 |
|------|------|------|
| 表现层 | controllers/ | 处理 HTTP 请求，参数校验，响应格式化 |
| 业务层 | services/ | 业务逻辑处理，事务管理，权限校验 |
| 数据层 | repositories/ | 数据持久化操作，查询封装 |
| 基础设施层 | infrastructure/ | 数据库连接、缓存、消息队列等技术实现 |
-->

**架构模式**: 🤖 AI 待分析

**架构图**: 🤖 AI 待绘制 (Mermaid)

### 各层职责

| 层级 | 目录/文件 | 职责 |
|------|-----------|------|
| 🤖 AI 待填充 | 🤖 AI 待填充 | 🤖 AI 待填充 |

---

## 依赖关系

> 🤖 **AI 探索方法**：
> 1. 使用 Grep 搜索 `import` `require` `use` 等导入语句
> 2. 分析模块间的引用关系
> 3. 绘制依赖关系图

<!--
🤖 AI 填充示例：

**依赖模块**：
- `common` 模块：使用通用工具函数和基础类型
- `config` 模块：读取数据库连接配置
- `logger` 模块：记录操作日志

**被依赖**：
- `api` 模块：所有 API 处理器依赖本模块进行数据操作
- `migration` 模块：数据库迁移脚本依赖本模块的实体定义
-->

**依赖**: 🤖 AI 待分析

**被依赖**: 🤖 AI 待分析

### 模块依赖图

<!--
🤖 AI 填充示例：
```mermaid
graph LR
    A[api] --> B[service]
    B --> C[repository]
    C --> D[database]
    B --> E[cache]
    A --> F[auth]
```
-->

🤖 AI 待绘制 (Mermaid)

---

## 数据流向

> 🤖 **AI 探索方法**：
> 1. 从入口追踪一个完整请求的处理过程
> 2. 找到数据转换的关键节点
> 3. 标注数据格式变化

<!--
🤖 AI 填充示例：

### 请求处理流程

```mermaid
sequenceDiagram
    participant C as Client
    participant R as Router
    participant M as Middleware
    participant S as Service
    participant Repo as Repository
    participant DB as Database

    C->>R: HTTP Request
    R->>M: Auth & Validation
    M->>S: Call Service Method
    S->>Repo: Query Data
    Repo->>DB: SQL Query
    DB-->>Repo: Result Set
    Repo-->>S: Entity Object
    S-->>M: DTO Object
    M-->>R: Response JSON
    R-->>C: HTTP Response
```

### 关键数据转换

| 阶段 | 数据格式 | 说明 |
|------|----------|------|
| 请求接收 | HTTP Request | 原始 HTTP 请求 |
| 参数解析 | RequestDTO | 经过校验的参数对象 |
| 业务处理 | Entity | 数据库实体对象 |
| 响应返回 | ResponseDTO | 格式化的响应对象 |
-->

**数据流向图**: 🤖 AI 待绘制 (Mermaid)

**关键数据转换**: 🤖 AI 待分析

---

*此文档由 AI README 生成骨架 - 等待 AI 分析源文件后填充*
""",

    "core-flow": """{progressive_guide}
# 核心流程

> 🤖 **AI 填充指南**：本章需要追踪代码调用链，请按以下步骤渐进式填充：
>
> **第一步**：找到核心业务入口（如登录、下单、查询等）
> **第二步**：使用 Read 读取入口文件，理解触发条件
> **第三步**：使用 Grep 追踪函数调用链
> **第四步**：绘制序列图，描述完整流程

## 核心业务流程

> 🤖 **AI 探索提示**：
> - 前端：从页面组件的事件处理函数开始追踪
> - 后端：从路由/Controller 开始追踪
> - 客户端：从用户交互事件开始追踪

<!--
🤖 AI 填充示例：

### 用户登录流程

```mermaid
sequenceDiagram
    participant U as 用户
    participant P as 登录页面
    participant A as Auth Service
    participant T as Token Service
    participant D as Database

    U->>P: 输入账号密码
    P->>P: 表单校验
    P->>A: 调用登录接口
    A->>D: 查询用户信息
    D-->>A: 返回用户数据
    A->>A: 验证密码
    A->>T: 生成 JWT Token
    T-->>A: 返回 Token
    A-->>P: 返回用户信息 + Token
    P->>P: 存储 Token 到 LocalStorage
    P-->>U: 跳转到首页
```

**流程说明**：

1. **表单校验阶段**：用户输入账号密码后，前端先进行基本格式校验（邮箱格式、密码长度等）
2. **请求发送阶段**：校验通过后，调用后端登录接口，传输加密后的凭证
3. **后端验证阶段**：后端查询用户信息，使用 bcrypt 比对密码哈希
4. **Token 生成阶段**：验证通过后，生成包含用户 ID 和权限的 JWT Token
5. **状态持久化阶段**：前端将 Token 存储到 LocalStorage，并更新全局用户状态

**关键代码位置**：
- 前端入口：`src/pages/login/LoginPage.tsx` 的 `handleLogin` 函数
- 后端接口：`src/controllers/auth.controller.ts` 的 `login` 方法
- Token 生成：`src/services/token.service.ts` 的 `generateToken` 方法
-->

### 业务流程 1：🤖 AI 待命名

**流程描述**: 🤖 AI 待填充

**序列图**: 🤖 AI 待绘制

**关键代码位置**: 🤖 AI 待填充

---

## 关键函数分析

> 🤖 **AI 探索方法**：
> 1. 使用 Grep 搜索函数定义
> 2. 使用 Read 读取完整函数体
> 3. 分析函数签名、参数、返回值、副作用

<!--
🤖 AI 填充示例：

### 函数：createOrder（创建订单）

**位置**：`src/services/order.service.ts`

**签名**：
```typescript
async createOrder(userId: string, items: OrderItem[], options?: CreateOrderOptions): Promise<Order>
```

**参数说明**：
| 参数 | 类型 | 说明 |
|------|------|------|
| userId | string | 用户 ID，从 Token 中解析 |
| items | OrderItem[] | 订单商品列表，包含商品 ID 和数量 |
| options | CreateOrderOptions | 可选配置，如优惠券、备注等 |

**返回值**：返回创建的订单对象，包含订单号、总价、状态等信息

**核心逻辑**：
```typescript
async createOrder(userId, items, options) {{
  // 1. 校验商品库存
  await this.validateInventory(items);

  // 2. 计算订单总价
  const total = await this.calculateTotal(items, options?.couponId);

  // 3. 创建订单记录（事务）
  const order = await this.transaction(async (tx) => {{
    const order = await tx.order.create({{ userId, items, total }});
    await tx.inventory.deduct(items);  // 扣减库存
    return order;
  }});

  // 4. 发送订单创建事件
  await this.eventBus.emit('order.created', order);

  return order;
}}
```

**注意事项**：
- 使用事务保证订单创建和库存扣减的原子性
- 库存不足时会抛出 InsufficientInventoryError
- 订单创建后会异步通知物流系统
-->

### 函数：🤖 AI 待命名

**位置**: 🤖 AI 待填充

**签名**: 🤖 AI 待填充

**核心逻辑**: 🤖 AI 待填充

---

## 状态管理

> 🤖 **AI 探索提示**：
> - **前端项目**：搜索 `useState` `useReducer` `Redux` `Vuex` `Pinia` `MobX` `zustand`
> - **后端项目**：搜索 Session 管理、缓存使用、数据库事务
> - **客户端项目**：搜索 `StateFlow` `LiveData` `Bloc` `Provider` `Riverpod`

<!--
🤖 AI 填充示例：

### 状态管理方案

项目采用 **Pinia + Composition API** 进行状态管理。

**全局 Store 列表**：

| Store | 文件位置 | 管理的状态 |
|-------|----------|------------|
| useUserStore | stores/user.ts | 用户信息、登录状态、权限列表 |
| useCartStore | stores/cart.ts | 购物车商品、数量、选中状态 |
| useAppStore | stores/app.ts | 主题、语言、侧边栏状态 |

**用户状态流转图**：
```mermaid
stateDiagram-v2
    [*] --> 未登录
    未登录 --> 登录中：输入凭证
    登录中 --> 已登录：验证成功
    登录中 --> 登录失败：验证失败
    登录失败 --> 登录中：重试
    已登录 --> 未登录：退出登录
    已登录 --> Token 过期：Token 过期
    Token 过期 --> 登录中：刷新 Token
```

**关键代码**：
```typescript
// stores/user.ts
export const useUserStore = defineStore('user', () => {{
  const user = ref<User | null>(null);
  const isLoggedIn = computed(() => !!user.value);

  async function login(credentials: LoginCredentials) {{
    const response = await authApi.login(credentials);
    user.value = response.user;
    localStorage.setItem('token', response.token);
  }}

  function logout() {{
    user.value = null;
    localStorage.removeItem('token');
  }}

  return {{ user, isLoggedIn, login, logout }};
}});
```
-->

**状态管理方式**: 🤖 AI 待分析

**全局状态列表**: 🤖 AI 待填充

**状态流转图**: 🤖 AI 待绘制

---

## 业务状态机

> 🤖 **AI 探索提示**：
> - 搜索状态枚举定义：`enum Status`, `@EnumValue`, `status = {`
> - 查找状态流转代码：`setStatus`, `updateStatus`, `changeState`
> - 分析状态校验逻辑：哪些操作允许在哪些状态下执行

### 订单状态机

```mermaid
stateDiagram-v2
    [*] --> 待支付: 创建订单
    待支付 --> 已取消: 超时未支付 / 主动取消
    待支付 --> 待发货: 支付成功
    待发货 --> 已发货: 商家发货
    已发货 --> 已完成: 用户确认 / 自动确认(7天)
    已发货 --> 售后中: 申请售后
    售后中 --> 已完成: 售后完成
    售后中 --> 已关闭: 售后关闭
```

**状态说明**:

| 状态 | 含义 | 允许的操作 | 触发条件 |
|------|------|-----------|---------|
| 待支付 | 订单创建未付款 | 支付、取消 | 订单创建 |
| 待发货 | 已支付待发货 | 发货、退款 | 支付成功 |
| 已发货 | 已发货待收货 | 确认收货、申请售后 | 商家发货 |
| 已完成 | 订单完成 | 评价、再次购买 | 确认收货/售后完成 |
| 已取消 | 订单已取消 | 删除 | 取消/超时 |
| 售后中 | 售后处理中 | 查看进度 | 申请售后 |

🤖 AI 待填充其他实体的状态机

---

## 异常流程

> 🤖 **AI 探索提示**：
> - 搜索异常处理：`catch`, `try-catch`, `@ExceptionHandler`
> - 查找补偿机制：`compensate`, `rollback`, `undo`
> - 分析重试逻辑：`retry`, `@Retryable`, `while (retryCount < maxRetry)`

### 支付异常处理

| 异常场景 | 触发条件 | 处理方式 | 补偿机制 |
|---------|---------|---------|---------|
| 支付超时 | 用户支付后回调延迟 | 查询支付状态 | 定时任务补偿 |
| 支付重复 | 同一订单多次支付 | 幂等校验 | 退款处理 |
| 支付失败 | 余额不足/银行拒绝 | 提示用户 | 订单保持待支付 |
| 系统异常 | 网络中断/服务宕机 | 记录日志 | 异步重试 |

### 库存异常处理

| 异常场景 | 触发条件 | 处理方式 | 补偿机制 |
|---------|---------|---------|---------|
| 库存不足 | 并发扣减导致负库存 | 抛出异常回滚 | 订单取消释放库存 |
| 库存超时 | 锁库存后未支付 | 定时任务释放 | 自动回滚 |
| 库存不一致 | 数据库与缓存不一致 | 对账补偿 | 手动修复 |

🤖 AI 待填充其他异常流程

---

*此文档由 AI README 生成骨架 - 等待 AI 分析源代码后填充*
""",

    "api-convention": """{progressive_guide}
# 接口约定

> 🤖 **AI 填充指南**：本章需要分析项目的接口定义，请按以下步骤渐进式填充：
>
> **第一步**：找到接口定义文件（api/services/controllers 目录）
> **第二步**：列出所有接口，记录路径、方法、参数、返回值
> **第三步**：分析请求封装和拦截器
> **第四步**：分析鉴权机制和 Token 处理

## 接口定义位置

> 🤖 **AI 探索提示**：
> - **前端项目**：找 `api/` `services/` `request/` 目录，搜索 `fetch` `axios` `http`
> - **后端项目**：找 `routes/` `controllers/` `handlers/`，搜索 `@GetMapping` `@Post` `router.get`
> - **客户端项目**：找 `api/` `network/` `service/`，找 Retrofit 接口、OkHttp 调用

<!--
🤖 AI 填充示例：

接口定义分布在以下位置：

| 位置 | 类型 | 包含接口 |
|------|------|----------|
| src/api/user.ts | 前端 API | 用户相关：登录、注册、获取用户信息 |
| src/api/product.ts | 前端 API | 商品相关：列表、详情、搜索 |
| src/controllers/auth.controller.ts | 后端路由 | 认证接口：/api/auth/* |
| src/controllers/user.controller.ts | 后端路由 | 用户接口：/api/users/* |
-->

**接口定义位置**: 🤖 AI 待查找

---

## 接口列表

> 🤖 **AI 填充指南**：
> - 列出所有接口，不要遗漏
> - 包含：接口名称、HTTP 方法、路径、用途、关键参数

<!--
🤖 AI 填充示例：

### 用户模块接口

| 接口名称 | 方法 | 路径 | 用途 | 关键参数 |
|----------|------|------|------|----------|
| 登录 | POST | /api/auth/login | 用户登录 | username, password |
| 注册 | POST | /api/auth/register | 用户注册 | username, email, password |
| 登出 | POST | /api/auth/logout | 退出登录 | - |
| 刷新 Token | POST | /api/auth/refresh | 刷新访问令牌 | refreshToken |
| 获取用户信息 | GET | /api/users/me | 获取当前用户 | - |
| 更新用户信息 | PUT | /api/users/me | 更新资料 | nickname, avatar |

### 商品模块接口

| 接口名称 | 方法 | 路径 | 用途 | 关键参数 |
|----------|------|------|------|----------|
| 商品列表 | GET | /api/products | 分页查询商品 | page, size, category |
| 商品详情 | GET | /api/products/:id | 获取单个商品 | id |
| 搜索商品 | GET | /api/products/search | 搜索商品 | keyword |
-->

### 模块：🤖 AI 待命名

| 接口名称 | 方法 | 路径 | 用途 | 关键参数 |
|----------|------|------|------|----------|
| 🤖 AI 待填充 | 🤖 AI 待填充 | 🤖 AI 待填充 | 🤖 AI 待填充 | 🤖 AI 待填充 |

---

## 请求规范

> 🤖 **AI 探索提示**：
> - 搜索 `interceptor` `middleware` `headers` `Authorization` `Bearer`
> - 找请求封装函数或类

<!--
🤖 AI 填充示例：

### 请求封装

项目使用 Axios 作为 HTTP 客户端，封装在 `src/utils/request.ts`：

```typescript
// src/utils/request.ts
const request = axios.create({{
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 10000,
  headers: {{
    'Content-Type': 'application/json',
  }},
}});

// 请求拦截器：自动添加 Token
request.interceptors.request.use((config) => {{
  const token = localStorage.getItem('token');
  if (token) {{
    config.headers.Authorization = `Bearer ${{token}}`;
  }}
  return config;
}});

// 响应拦截器：统一错误处理
request.interceptors.response.use(
  (response) => response.data,
  (error) => {{
    if (error.response?.status === 401) {{
      // Token 过期，跳转登录
      router.push('/login');
    }}
    return Promise.reject(error);
  }}
);
```

### 请求头规范

| Header | 值 | 说明 |
|--------|-----|------|
| Content-Type | application/json | 请求体格式 |
| Authorization | Bearer {{token}} | 认证令牌 |
| X-Request-ID | UUID | 请求追踪 ID |
| Accept-Language | zh-CN | 语言偏好 |

### 超时设置

- 普通请求：10 秒
- 文件上传：60 秒
- 长轮询请求：120 秒
-->

**请求封装位置**: 🤖 AI 待查找

**请求拦截处理**: 🤖 AI 待分析

---

## 响应处理

> 🤖 **AI 探索提示**：
> - 搜索响应拦截器、错误处理函数
> - 找错误码定义文件

<!--
🤖 AI 填充示例：

### 统一响应格式

```typescript
interface ApiResponse<T> {{
  code: number;      // 业务状态码
  message: string;   // 提示信息
  data: T;          // 业务数据
  timestamp: number; // 响应时间戳
}}
```

### 错误码定义

| 错误码 | 含义 | 处理方式 |
|--------|------|----------|
| 0 | 成功 | - |
| 1001 | 参数错误 | 提示用户检查输入 |
| 1002 | 未授权 | 跳转登录页 |
| 1003 | 禁止访问 | 提示无权限 |
| 2001 | 用户不存在 | 提示注册 |
| 2002 | 密码错误 | 提示重新输入 |
| 5000 | 服务器错误 | 提示稍后重试 |

### 错误响应示例

```json
{{
  "code": 1002,
  "message": "登录已过期，请重新登录",
  "data": null,
  "timestamp": 1699876543210
}}
```
-->

**响应拦截位置**: 🤖 AI 待查找

**错误码定义**: 🤖 AI 待分析

---

## 鉴权机制

> 🤖 **AI 探索提示**：
> - 搜索 `login` `auth` `token` `session` `JWT` `OAuth`

<!--
🤖 AI 填充示例：

### 鉴权方式

采用 **JWT (JSON Web Token)** 进行无状态认证。

### Token 结构

```typescript
interface JwtPayload {{
  sub: string;      // 用户 ID
  username: string; // 用户名
  roles: string[];  // 角色列表
  iat: number;      // 签发时间
  exp: number;      // 过期时间
}}
```

### Token 存储方式

| Token 类型 | 存储位置 | 过期时间 | 用途 |
|-----------|----------|----------|------|
| Access Token | LocalStorage | 2 小时 | 接口请求认证 |
| Refresh Token | HttpOnly Cookie | 7 天 | 刷新 Access Token |

### Token 刷新流程

```mermaid
sequenceDiagram
    participant C as Client
    participant A as API
    participant R as Redis

    C->>A: 请求 + Access Token
    A->>A: Token 过期
    A-->>C: 401 Unauthorized
    C->>A: 请求刷新 (Refresh Token)
    A->>R: 验证 Refresh Token
    R-->>A: 有效
    A-->>C: 新 Access Token
    C->>A: 重试原请求
```
-->

**鉴权方式**: 🤖 AI 待分析

**登录流程**: 🤖 AI 待分析

---

*此文档由 AI README 生成骨架 - 等待 AI 分析源文件后填充*
""",

    "api-examples": """{progressive_guide}
# 接口示例

> 🤖 **AI 填充指南**：本章需要提供具体接口的请求/响应示例，请按以下步骤：
>
> **第一步**：找到接口 Controller/Handler 代码
> **第二步**：分析请求参数和响应结构
> **第三步**：构造真实的 JSON 示例

---

## 接口示例列表

### 订单创建 `POST /api/order`

#### 请求示例

```json
{{
  "skuId": 12345,
  "count": 2,
  "addressId": 67890,
  "remark": "请尽快发货"
}}
```

#### 响应示例

**成功 (200)**:
```json
{{
  "code": 0,
  "message": "success",
  "data": {{
    "orderId": "ORD-2024032212345678",
    "totalAmount": 299.00,
    "status": "UNPAID",
    "createTime": "2024-03-22T10:30:00Z"
  }}
}}
```

**失败 - 库存不足 (400)**:
```json
{{
  "code": 2001,
  "message": "库存不足，当前库存：1",
  "data": null
}}
```

**字段说明**:

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| skuId | number | 是 | 商品 SKU ID |
| count | number | 是 | 购买数量 |
| addressId | number | 是 | 收货地址 ID |
| remark | string | 否 | 订单备注 |

---

### 支付回调 `POST /payment/notice`

#### 请求示例 (支付宝)

```json
{{
  "out_trade_no": "ORD-2024032212345678",
  "trade_no": "2024032222001156789012345678",
  "total_amount": "299.00",
  "trade_status": "TRADE_SUCCESS",
  "sign": "xxx..."
}}
```

#### 响应示例

**成功**:
```text
success
```

---

## 常见错误码

| 错误码 | 含义 | 场景 |
|--------|------|------|
| 0 | 成功 | - |
| 1001 | 参数错误 | 必填参数缺失 |
| 1002 | 未授权 | Token 过期或无效 |
| 1003 | 禁止访问 | 无权限访问该资源 |
| 2001 | 库存不足 | 商品库存不足 |
| 2002 | 订单已取消 | 订单状态不正确 |
| 5000 | 服务器内部错误 | 系统异常 |

---

*此文档由 AI README 生成骨架 - 等待 AI 分析源文件后填充*
""",

    "data-model": """{progressive_guide}
# 数据模型

> 🤖 **AI 填充指南**：本章需要分析项目中的数据结构，请按以下步骤渐进式填充：
>
> **第一步**：找到类型定义/实体类文件
> **第二步**：列出核心数据模型，描述字段含义
> **第三步**：分析模型间的关系
> **第四步**：追踪数据的存取方式

## 数据模型位置

> 🤖 **AI 探索提示**：
> - **前端项目**：找 `types/` `models/` `interfaces/`，搜索 `interface` `type`
> - **后端项目**：找 `entities/` `models/` `domain/`，搜索 `@Entity` `@Table` `schema.prisma`
> - **客户端项目**：找 `model/` `entity/` `dto/`，搜索 `data class` `struct`

<!--
🤖 AI 填充示例：

数据模型分布在以下位置：

| 位置 | 类型 | 包含模型 |
|------|------|----------|
| src/types/user.ts | TypeScript 接口 | User, UserProfile, UserRole |
| src/types/product.ts | TypeScript 接口 | Product, ProductCategory, Sku |
| src/entities/order.entity.ts | ORM 实体 | Order（数据库映射） |
| src/dto/create-order.dto.ts | DTO | CreateOrderDto（请求参数） |
-->

**数据模型位置**: 🤖 AI 待查找

---

## 核心数据结构

> 🤖 **AI 填充指南**：
> - 列出每个模型的所有字段
> - 说明字段类型、是否必填、默认值
> - 解释字段用途

<!--
🤖 AI 填充示例：

### User（用户）

**位置**：`src/types/user.ts`

```typescript
interface User {{
  id: string;           // 用户唯一标识，UUID 格式
  username: string;     // 用户名，4-20 字符，唯一
  email: string;        // 邮箱地址，用于登录和通知
  password?: string;    // 密码哈希，返回时不包含
  nickname?: string;    // 昵称，可选，默认同 username
  avatar?: string;      // 头像 URL
  roles: UserRole[];    // 角色列表，默认 ['user']
  status: UserStatus;   // 状态：active/inactive/banned
  createdAt: Date;      // 注册时间
  updatedAt: Date;      // 更新时间
}}
```

**字段说明**：

| 字段 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| id | string | 是 | UUID | 用户唯一标识 |
| username | string | 是 | - | 登录用户名，唯一 |
| email | string | 是 | - | 邮箱，唯一 |
| password | string | 是 | - | bcrypt 哈希后的密码 |
| nickname | string | 否 | username | 显示昵称 |
| avatar | string | 否 | 默认头像 URL | 头像地址 |
| roles | UserRole[] | 是 | ['user'] | 用户角色 |
| status | UserStatus | 是 | 'active' | 账户状态 |
-->

### 模型：🤖 AI 待命名

**位置**: 🤖 AI 待填充

**类型定义**: 🤖 AI 待填充

**字段说明**:

| 字段 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| 🤖 AI 待填充 | 🤖 AI 待填充 | 🤖 AI 待填充 | 🤖 AI 待填充 | 🤖 AI 待填充 |

---

## 数据关系

> 🤖 **AI 探索方法**：
> - 分析模型中的外键引用
> - 查找关联装饰器：`@OneToMany` `@ManyToOne` `@ManyToMany`
> - 查找 TypeScript 中的嵌套类型

<!--
🤖 AI 填充示例：

### 实体关系图

```mermaid
erDiagram
    User ||--o{{ Order : places
    User ||--o{{ Address : has
    Order ||--|{{ OrderItem : contains
    OrderItem }}o--|| Product : references
    Product }}o--|| Category : belongs_to
    Product ||--o{{ Sku : has
```

### 关系说明

| 关系 | 类型 | 说明 |
|------|------|------|
| User → Order | 一对多 | 一个用户可以有多个订单 |
| User → Address | 一对多 | 一个用户可以有多个地址 |
| Order → OrderItem | 一对多 | 一个订单包含多个商品项 |
| OrderItem → Product | 多对一 | 多个订单项可关联同一商品 |
| Product → Category | 多对一 | 多个商品属于同一分类 |
| Product → Sku | 一对多 | 一个商品有多个 SKU |
-->

**实体关系图**: 🤖 AI 待绘制 (Mermaid ER 图)

**关系说明**: 🤖 AI 待分析

---

## 数据存储

> 🤖 **AI 探索提示**：
> - **前端项目**：找 LocalStorage/SessionStorage、IndexedDB、状态持久化
> - **后端项目**：找数据库配置、ORM 连接、缓存使用
> - **客户端项目**：找 SQLite/Realm/CoreData、SharedPreferences

<!--
🤖 AI 填充示例：

### 数据库

**类型**：PostgreSQL 15

**连接配置**：
```typescript
// config/database.ts
export default {{
  type: 'postgres',
  host: process.env.DB_HOST || 'localhost',
  port: parseInt(process.env.DB_PORT) || 5432,
  username: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  synchronize: false,  // 生产环境禁用自动同步
  logging: true,
}};
```

### 缓存

**类型**：Redis

**用途**：
- 用户 Session 存储
- 接口响应缓存
- 分布式锁

### 前端存储

| 存储方式 | 用途 | 过期策略 |
|----------|------|----------|
| LocalStorage | Token、用户偏好 | 手动清除 |
| SessionStorage | 临时表单数据 | 关闭标签页 |
| IndexedDB | 离线数据缓存 | 手动清除 |
-->

**数据存储方式**: 🤖 AI 待分析

**数据库类型**: 🤖 AI 待分析

---

## 数据校验

> 🤖 **AI 探索提示**：
> - 搜索 `validate` `schema` `Zod` `Yup` `Joi` `class-validator`
> - 找表单校验逻辑

<!--
🤖 AI 填充示例：

### 校验框架

使用 **Zod** 进行运行时类型校验。

### 校验规则示例

```typescript
// schemas/user.schema.ts
import {{ z }} from 'zod';

export const createUserSchema = z.object({{
  username: z.string()
    .min(4, '用户名至少 4 个字符')
    .max(20, '用户名最多 20 个字符')
    .regex(/^[a-zA-Z0-9_]+$/, '只能包含字母、数字、下划线'),

  email: z.string()
    .email('请输入有效的邮箱地址'),

  password: z.string()
    .min(8, '密码至少 8 个字符')
    .regex(/[A-Z]/, '密码必须包含大写字母')
    .regex(/[0-9]/, '密码必须包含数字'),
}});
```

### 校验时机

| 时机 | 校验内容 | 失败处理 |
|------|----------|----------|
| 前端表单提交 | 格式校验 | 显示错误提示 |
| 后端接口入参 | 格式 + 业务规则 | 返回 400 错误 |
| 数据库写入 | 约束校验 | 抛出异常 |
-->

**数据校验方式**: 🤖 AI 待分析

**校验规则位置**: 🤖 AI 待查找

---

## 数据转换

> 🤖 **AI 探索提示**：
> - 搜索 `mapper` `converter` `transform` `serialize` `deserialize`

<!--
🤖 AI 填充示例：

### 数据流转过程中的转换

```
Request JSON → DTO → Entity → Database
                    ↓
              Response DTO ← Entity
```

### 转换规则

| 转换 | 位置 | 说明 |
|------|------|------|
| Request → DTO | Controller | 参数解析和初步校验 |
| DTO → Entity | Service | 业务逻辑处理，设置默认值 |
| Entity → Response DTO | Service | 过滤敏感字段，格式化输出 |
| Entity → JSON | Serializer | 处理日期、循环引用等 |

### 敏感字段处理

```typescript
// 返回用户信息时排除密码
@Entity()
export class User {{
  @Exclude()
  password: string;

  @Expose()
  id: string;

  @Expose()
  username: string;
}}

// 使用 class-transformer
const userDto = plainToClass(User, userEntity, {{ excludeExtraneousValues: true }});
```
-->

**数据转换位置**: 🤖 AI 待查找

---

*此文档由 AI README 生成骨架 - 等待 AI 分析源文件后填充*
""",

    "database-doc": """{progressive_guide}
# 数据库文档

> 🤖 **AI 填充指南**：本章需要分析数据库设计和使用，请按以下步骤渐进式填充：
>
> **第一步**：找到数据库实体/Model 文件
> **第二步**：分析表结构和字段含义
> **第三步**：找到索引定义
> **第四步**：分析数据字典（枚举值含义）

---

## 数据库设计

### 分库分表策略

> 🤖 **AI 探索提示**：
> - 搜索 `@TableName` `@Entity` `@Table` 注解
> - 查找分库分表配置（ShardingSphere、MyCat 等）

| 库/表 | 说明 | 包含实体 |
|------|------|---------|
| 主库 | 用户、商品基础数据 | user, product |
| 订单库 | 订单相关数据 | orders, order_item |

🤖 AI 待分析

### ER 图

```mermaid
erDiagram
    USER ||--o{{ ORDER : places
    ORDER ||--|{{ ORDER_ITEM : contains
```

🤖 AI 待绘制完整 ER 图

---

## 数据字典

### 枚举值定义

> 🤖 **AI 探索提示**：搜索枚举类定义、常量定义

#### 订单状态 (order_status)

| 值 | 含义 | 说明 |
|----|------|------|
| 0 | 待支付 | 订单创建未支付 |
| 1 | 待发货 | 已支付等待发货 |
| 2 | 已发货 | 商家已发货 |
| 3 | 已完成 | 已确认收货 |
| 4 | 已取消 | 订单已取消 |

🤖 AI 待填充其他枚举定义

---

## 索引设计

> 🤖 **AI 探索提示**：
> - 搜索 `@Index` `@Table(indexes=...)` 注解
> - 查找 DDL 文件中的 CREATE INDEX 语句

| 表名 | 索引名 | 字段 | 类型 | 用途 |
|------|-------|------|------|------|
| orders | idx_user_id | user_id | 普通索引 | 用户订单查询 |
| orders | idx_order_no | order_no | 唯一索引 | 订单号唯一 |

🤖 AI 待分析

---

## 初始化数据

> 🤖 **AI 探索提示**：
> - 查找 `data.sql` `seed.sql` 等初始化脚本
> - 查找默认数据插入语句

| 数据类型 | 说明 | 位置 |
|---------|------|------|
| 默认角色 | admin, user | `data.sql:45` |
| 系统配置 | 超时时间等 | `sys_config.sql` |

🤖 AI 待查找

---

*此文档由 AI README 生成骨架 - 等待 AI 分析源文件后填充*
""",

    "error-handling": """{progressive_guide}
# 错误处理

> 🤖 **AI 填充指南**：本章需要分析项目的错误处理机制，请按以下步骤渐进式填充：
>
> **第一步**：找到错误类型定义和异常类
> **第二步**：找到全局错误处理器/拦截器
> **第三步**：分析日志记录方式
> **第四步**：找到监控和告警配置

## 错误处理位置

> 🤖 **AI 探索提示**：
> - **前端项目**：找 Error Boundary、`try-catch`、`onerror`、`unhandledrejection`
> - **后端项目**：找异常处理中间件、`@ExceptionHandler`、全局错误处理类
> - **客户端项目**：找 `UncaughtExceptionHandler`、Crash 收集 SDK

<!--
🤖 AI 填充示例：

错误处理相关代码分布在以下位置：

| 位置 | 类型 | 作用 |
|------|------|------|
| src/errors/ | 自定义异常类 | 定义业务异常类型 |
| src/middleware/error.middleware.ts | 全局错误处理 | 捕获并统一处理异常 |
| src/components/ErrorBoundary.tsx | React 错误边界 | 捕获组件渲染错误 |
| src/utils/logger.ts | 日志工具 | 统一日志记录 |
-->

**错误处理位置**: 🤖 AI 待查找

---

## 错误类型

> 🤖 **AI 探索方法**：
> - 搜索 `Error` `Exception` `throw` 关键字
> - 找自定义异常类定义

<!--
🤖 AI 填充示例：

### 自定义异常类

```typescript
// errors/base.error.ts
export class AppError extends Error {{
  constructor(
    public code: number,
    message: string,
    public statusCode: number = 500,
  ) {{
    super(message);
    this.name = 'AppError';
  }}
}}

// errors/business.error.ts
export class BusinessError extends AppError {{
  constructor(code: number, message: string) {{
    super(code, message, 400);
    this.name = 'BusinessError';
  }}
}}

// errors/not-found.error.ts
export class NotFoundError extends AppError {{
  constructor(resource: string) {{
    super(1004, `${{resource}}不存在`, 404);
    this.name = 'NotFoundError';
  }}
}}

// errors/auth.error.ts
export class UnauthorizedError extends AppError {{
  constructor(message: string = '未授权') {{
    super(1002, message, 401);
    this.name = 'UnauthorizedError';
  }}
}}
```

### 错误类型列表

| 错误类 | HTTP 状态码 | 业务码 | 使用场景 |
|--------|-------------|--------|----------|
| BusinessError | 400 | 1000-1999 | 业务逻辑错误 |
| UnauthorizedError | 401 | 1002 | 未登录或 Token 过期 |
| ForbiddenError | 403 | 1003 | 无权限访问 |
| NotFoundError | 404 | 1004 | 资源不存在 |
| ValidationError | 400 | 1001 | 参数校验失败 |
| DatabaseError | 500 | 3000 | 数据库操作失败 |
-->

### 自定义错误类型

| 错误类型 | 代码/标识 | 含义 | 处理方式 |
|----------|-----------|------|----------|
| 🤖 AI 待填充 | 🤖 AI 待填充 | 🤖 AI 待填充 | 🤖 AI 待填充 |

---

## 全局错误处理

> 🤖 **AI 探索方法**：
> - 找最外层的 try-catch 或错误处理中间件
> - 分析错误如何被捕获和转换

<!--
🤖 AI 填充示例：

### 全局错误处理中间件

```typescript
// middleware/error.middleware.ts
@Catch()
export class GlobalExceptionFilter implements ExceptionFilter {{
  catch(exception: unknown, host: ArgumentsHost) {{
    const ctx = host.switchToHttp();
    const response = ctx.getResponse();
    const request = ctx.getRequest();

    // 标准化错误响应
    let status = 500;
    let code = 5000;
    let message = '服务器内部错误';

    if (exception instanceof AppError) {{
      status = exception.statusCode;
      code = exception.code;
      message = exception.message;
    }} else if (exception instanceof ValidationError) {{
      status = 400;
      code = 1001;
      message = exception.message;
    }}

    // 记录错误日志
    this.logger.error(`${{request.method}} ${{request.url}}`, exception);

    // 返回统一格式
    response.status(status).json({{
      code,
      message,
      timestamp: Date.now(),
      path: request.url,
    }});
  }}
}}
```

### 错误处理流程

```mermaid
graph TD
    A[异常抛出] --> B{{异常类型}}
    B -->|AppError| C[提取错误信息]
    B -->|ValidationError| D[格式化校验错误]
    B -->|其他错误| E[记录未知错误]
    C --> F[返回标准响应]
    D --> F
    E --> F
    F --> G{{是否需要告警}}
    G -->|是 | H[发送告警]
    G -->|否 | I[结束]
    H --> I
```
-->

**全局错误处理机制**: 🤖 AI 待分析

---

## 用户提示

> 🤖 **AI 探索提示**：
> - 搜索 `toast` `message` `alert` `snackbar` `notification`

<!--
🤖 AI 填充示例：

### 提示组件

使用 Ant Design 的 `message` 组件：

```typescript
// 成功提示
message.success('操作成功');

// 错误提示
message.error('操作失败，请稍后重试');

// 警告提示
message.warning('该操作不可撤销');

// 加载提示
const hide = message.loading('正在处理...');
await doSomething();
hide();
```

### 错误提示策略

| 错误类型 | 提示方式 | 持续时间 |
|----------|----------|----------|
| 网络错误 | Toast | 3 秒 |
| 业务错误 | Toast | 3 秒 |
| 表单校验错误 | 字段下方红字 | 持续显示 |
| 系统错误 | 弹窗 | 手动关闭 |
-->

**用户提示方式**: 🤖 AI 待分析

**提示组件位置**: 🤖 AI 待查找

---

## 错误边界

> 🤖 **AI 探索提示**：
> - **前端项目**：找 React Error Boundary、Vue errorCaptured
> - **后端项目**：找降级逻辑、熔断机制、重试策略
> - **客户端项目**：找 try-catch 包裹的关键逻辑

<!--
🤖 AI 填充示例：

### React Error Boundary

```tsx
// components/ErrorBoundary.tsx
class ErrorBoundary extends React.Component {{
  state = {{ hasError: false }};

  static getDerivedStateFromError(error: Error) {{
    return {{ hasError: true }};
  }}

  componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {{
    // 上报错误到监控系统
    reportError(error, errorInfo);
  }}

  render() {{
    if (this.state.hasError) {{
      return <ErrorFallback onRetry={{() => this.setState({{ hasError: false }})}} />;
    }}
    return this.props.children;
  }}
}}

// 使用
<ErrorBoundary>
  <App />
</ErrorBoundary>
```

### 关键逻辑的保护

| 位置 | 保护方式 | 降级策略 |
|------|----------|----------|
| 组件渲染 | Error Boundary | 显示错误提示页 |
| API 请求 | try-catch | 显示错误 Toast |
| 数据解析 | try-catch | 使用默认值 |
| 支付流程 | 重试机制 | 最大重试 3 次 |
-->

**错误边界位置**: 🤖 AI 待查找

---

## 日志记录

> 🤖 **AI 探索提示**：
> - 搜索 `log` `logger` `console` `Logcat`

<!--
🤖 AI 填充示例：

### 日志框架

使用 **Winston** 作为日志框架。

### 日志配置

```typescript
// utils/logger.ts
const logger = winston.createLogger({{
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json(),
  ),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({{ filename: 'logs/error.log', level: 'error' }}),
    new winston.transports.File({{ filename: 'logs/combined.log' }}),
  ],
}});
```

### 日志级别

| 级别 | 使用场景 | 示例 |
|------|----------|------|
| error | 系统错误、异常 | 数据库连接失败 |
| warn | 潜在问题 | Token 即将过期 |
| info | 关键操作 | 用户登录成功 |
| debug | 调试信息 | 请求参数详情 |

### 日志格式

```json
{{
  "level": "error",
  "message": "Database connection failed",
  "timestamp": "2024-01-15T10:30:00.000Z",
  "context": {{
    "host": "localhost",
    "port": 5432,
    "error": "Connection refused"
  }}
}}
```
-->

**日志框架**: 🤖 AI 待分析

**日志级别**: 🤖 AI 待分析

---

## 监控与告警

> 🤖 **AI 探索提示**：
> - 找监控 SDK：Sentry、Bugly、Firebase、Prometheus
> - 搜索埋点相关代码

<!--
🤖 AI 填充示例：

### 监控工具

| 工具 | 用途 | 配置位置 |
|------|------|----------|
| Sentry | 错误监控和追踪 | src/config/sentry.ts |
| Prometheus | 性能指标采集 | src/metrics/ |
| Grafana | 监控面板 | 部署配置 |

### Sentry 配置

```typescript
// main.ts
Sentry.init({{
  dsn: process.env.SENTRY_DSN,
  environment: process.env.NODE_ENV,
  tracesSampleRate: 0.1,
}});

// 错误上报
Sentry.captureException(error);
```

### 告警规则

| 触发条件 | 告警方式 | 接收人 |
|----------|----------|--------|
| 错误率 > 1% | 钉钉 + 邮件 | 开发组 |
| 接口超时 > 5s | 钉钉 | 值班人员 |
| 服务不可用 | 电话 | 负责人 |
-->

**监控工具**: 🤖 AI 待分析

**告警方式**: 🤖 AI 待分析

---

*此文档由 AI README 生成骨架 - 等待 AI 分析源文件后填充*
""",

    "dev-guide": """{progressive_guide}
# 开发运行

> 🤖 **AI 填充指南**：本章需要分析项目的开发和运行方式，请按以下步骤渐进式填充：
>
> **第一步**：找到配置文件，分析环境要求和依赖
> **第二步**：找到启动脚本，理解运行流程
> **第三步**：找到构建配置，理解打包方式

## 环境要求

> 🤖 **AI 探索提示**：
> - 查看 `package.json` 的 `engines` 字段
> - 查看 `.nvmrc` `.python-version` `.sdkmanrc`
> - 查看 Dockerfile 中的基础镜像

<!--
🤖 AI 填充示例：

### 运行环境

| 环境 | 版本要求 | 说明 |
|------|----------|------|
| Node.js | >= 18.0.0 | 运行时环境 |
| npm | >= 9.0.0 | 包管理器 |
| PostgreSQL | >= 14.0 | 数据库 |
| Redis | >= 6.0 | 缓存服务 |

### 版本管理

- 使用 `.nvmrc` 固定 Node.js 版本
- 使用 pnpm 作为包管理器（更快的依赖安装）

### 开发工具

| 工具 | 用途 |
|------|------|
| VS Code | 推荐 IDE |
| ESLint | 代码检查 |
| Prettier | 代码格式化 |
| Docker | 容器化运行 |
-->

**语言/运行时版本**: 🤖 AI 待分析

**包管理器**: 🤖 AI 待分析

---

## 快速开始

> 🤖 **AI 探索提示**：
> - 查看 `package.json` scripts、`Makefile`、`gradlew`、`build.sh`

<!--
🤖 AI 填充示例：

### 安装依赖

```bash
# 推荐使用 pnpm
pnpm install

# 或使用 npm
npm install
```

### 启动开发环境

```bash
# 启动后端服务
pnpm dev

# 启动前端开发服务器（另一个终端）
cd frontend && pnpm dev

# 启动本地数据库（Docker）
docker-compose up -d db redis
```

### 访问服务

| 服务 | 地址 | 说明 |
|------|------|------|
| 前端 | http://localhost:5173 | Vite 开发服务器 |
| 后端 API | http://localhost:3000 | NestJS 服务 |
| API 文档 | http://localhost:3000/api | Swagger 文档 |
| 数据库管理 | http://localhost:8080 | Adminer |
-->

### 安装依赖

```bash
🤖 AI 待填充
```

### 启动开发环境

```bash
🤖 AI 待填充
```

---

## 构建与打包

> 🤖 **AI 探索提示**：
> - 查看 `build` `dist` `release` 等构建脚本
> - 查看 webpack/vite/rollup 配置

<!--
🤖 AI 填充示例：

### 构建命令

```bash
# 构建生产版本
pnpm build

# 构建并分析产物
pnpm build:analyze

# 仅构建前端
pnpm build:frontend

# 仅构建后端
pnpm build:backend
```

### 构建配置

**前端 (Vite)**：
```typescript
// vite.config.ts
export default defineConfig({{
  build: {{
    outDir: 'dist',
    sourcemap: false,
    rollupOptions: {{
      output: {{
        manualChunks: {{
          vendor: ['react', 'react-dom'],
          utils: ['lodash', 'dayjs'],
        }},
      }},
    }},
  }},
}});
```

### 构建产物

| 产物 | 大小 | 说明 |
|------|------|------|
| dist/assets/index-xxx.js | ~150KB | 入口 JS |
| dist/assets/vendor-xxx.js | ~200KB | 第三方库 |
| dist/assets/index-xxx.css | ~50KB | 样式文件 |
-->

**构建命令**: 🤖 AI 待分析

**构建产物位置**: 🤖 AI 待分析

---

## 环境变量

> 🤖 **AI 探索提示**：
> - 找 `.env` `.env.example` `.env.local`
> - 搜索 `process.env` `import.meta.env` `System.getenv`

<!--
🤖 AI 填充示例：

### 环境变量文件

| 文件 | 用途 | 是否提交 Git |
|------|------|-------------|
| .env.example | 模板文件 | 是 |
| .env.development | 开发环境 | 否 |
| .env.production | 生产环境 | 否 |
| .env.local | 本地覆盖 | 否 |

### 环境变量列表

| 变量名 | 必填 | 默认值 | 说明 |
|--------|------|--------|------|
| NODE_ENV | 是 | development | 运行环境 |
| PORT | 否 | 3000 | 服务端口 |
| DATABASE_URL | 是 | - | 数据库连接串 |
| REDIS_URL | 是 | - | Redis 连接串 |
| JWT_SECRET | 是 | - | JWT 密钥 |
| JWT_EXPIRES_IN | 否 | 2h | Token 过期时间 |
| SENTRY_DSN | 否 | - | Sentry 监控地址 |

### 使用示例

```typescript
// 配置读取
const config = {{
  port: parseInt(process.env.PORT || '3000'),
  database: {{
    url: process.env.DATABASE_URL,
  }},
  jwt: {{
    secret: process.env.JWT_SECRET,
    expiresIn: process.env.JWT_EXPIRES_IN || '2h',
  }},
}};
```
-->

**环境变量文件**: 🤖 AI 待查找

| 变量名 | 用途 | 默认值 |
|--------|------|--------|
| 🤖 AI 待填充 | 🤖 AI 待填充 | 🤖 AI 待填充 |

---

## 常用脚本

> 🤖 **AI 探索提示**：
> - 查看 `package.json` scripts、`Makefile`、`gradle tasks`

<!--
🤖 AI 填充示例：

### npm scripts

| 命令 | 作用 |
|------|------|
| `pnpm dev` | 启动开发服务器，支持热重载 |
| `pnpm build` | 构建生产版本 |
| `pnpm start` | 启动生产服务器 |
| `pnpm test` | 运行单元测试 |
| `pnpm test:e2e` | 运行端到端测试 |
| `pnpm lint` | 代码检查 |
| `pnpm format` | 代码格式化 |
| `pnpm db:migrate` | 执行数据库迁移 |
| `pnpm db:seed` | 填充测试数据 |

### Makefile 命令

| 命令 | 作用 |
|------|------|
| `make install` | 安装依赖 |
| `make dev` | 启动开发环境 |
| `make build` | 构建生产版本 |
| `make deploy` | 部署到生产环境 |
| `make clean` | 清理构建产物 |
-->

| 命令 | 作用 |
|------|------|
| 🤖 AI 待填充 | 🤖 AI 待填充 |

---

## 开发工具配置

> 🤖 **AI 探索提示**：
> - 找 `.vscode/` `.idea/` `.editorconfig`
> - 找 ESLint/Prettier 配置
> - 找 Git hooks 配置 (`.husky/`)

<!--
🤖 AI 填充示例：

### VS Code 配置

推荐插件（`.vscode/extensions.json`）：
```json
{{
  "recommendations": [
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode",
    "ms-vscode.vscode-typescript-next"
  ]
}}
```

工作区设置（`.vscode/settings.json`）：
```json
{{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.codeActionsOnSave": {{
    "source.fixAll.eslint": true
  }}
}}
```

### 代码规范

| 工具 | 配置文件 | 作用 |
|------|----------|------|
| ESLint | .eslintrc.js | 代码检查 |
| Prettier | .prettierrc | 代码格式化 |
| EditorConfig | .editorconfig | 编辑器配置 |

### Git Hooks

使用 Husky + lint-staged：

```json
// package.json
{{
  "lint-staged": {{
    "*.{ts,tsx}": ["eslint --fix", "prettier --write"],
    "*.{json,md}": ["prettier --write"]
  }}
}}
```

提交前自动执行：
- ESLint 检查并修复
- Prettier 格式化
- 单元测试（可选）
-->

**IDE 配置**: 🤖 AI 待分析

**代码规范工具**: 🤖 AI 待分析

---

*此文档由 AI README 生成骨架 - 等待 AI 分析源文件后填充*
""",

    "business-knowledge": """# 业务知识

> 🤖 **AI 扫描指南**：AI 应先扫描代码，按业务模块生成框架，人类再填充具体数值
>
> **第一步**：扫描代码结构，识别业务模块（order, user, product 等）
> **第二步**：查找枚举类、常量定义、配置文件中的业务数值
> **第三步**：生成业务模块框架表格
> **第四步**：人类填写具体数值和说明

---

## 业务模块划分

> 🤖 **AI 扫描提示**：
> - 查找 `order`, `user`, `product`, `payment`, `inventory` 等业务目录
> - 识别核心业务实体和它们之间的关系
> - 按模块组织下面的业务规则表格

<!--
🤖 AI 填充示例：

本项目包含以下业务模块：

| 模块 | 目录 | 核心实体 | 说明 |
|------|------|----------|------|
| 订单模块 | `src/order/` | Order, OrderItem | 订单创建、支付、履约 |
| 用户模块 | `src/user/` | User, Address | 用户注册、登录、资料管理 |
| 商品模块 | `src/product/` | Product, Sku, Category | 商品管理、库存、分类 |
| 支付模块 | `src/payment/` | Payment, Refund | 支付处理、退款 |
-->

| 模块 | 目录 | 核心实体 | 说明 |
|------|------|----------|------|
| 🤖 AI 待扫描 | 🤖 AI 待填充 | 🤖 AI 待填充 | 🤖 AI 待填充 |

---

## 领域术语

> 🤖 **AI 扫描提示**：
> - 搜索 enum 定义、常量类
> - 查找类名中的业务概念（OrderStatus, PaymentType 等）
> - 提取注释中的业务术语

| 术语 | 含义 | 使用场景 | 相关代码位置 |
|------|------|----------|-------------|
| 🤖 AI 待扫描 | - | - | - |

---

## 业务规则数值

> 💡 **人类填写指南**: 从代码中提取硬编码的业务数值，包括：
> - 超时时间（订单支付超时、自动确认收货）
> - 限制数值（库存锁定时长、最大重试次数）
> - 计算规则（运费计算、退款金额计算）
> - 阈值配置（告警阈值、分页大小）

### [模块名称] 业务规则

> 🤖 **AI 扫描提示**：搜索该模块下的硬编码数字
> - `timeout`, `expire`, `limit`, `max`, `min`, `default`
> - `@Value`, `const`, `static final`

| 规则名称 | 数值 | 实现方式 | 配置位置 | 相关代码 |
|---------|------|---------|---------|---------|
| 待人类填写 | - | - | - | - |

---

## 业务状态流转

> 💡 **人类填写**: 使用 Mermaid 绘制核心实体的状态机

### [实体名称] 状态流转

```mermaid
stateDiagram-v2
    [*] --> 状态A: 事件1
    状态A --> 状态B: 事件2
```

**状态说明**:

| 状态 | 含义 | 触发条件 | 允许的操作 |
|------|------|---------|-----------|
| 待人类填写 | - | - | - |

---

## 业务边界与异常

> 💡 **人类填写**: 记录业务的边界情况和异常处理规则

| 场景 | 预期行为 | 实际实现 | 注意事项 |
|------|---------|---------|---------|
| 待人类填写 | - | - | - |

---

## 外部依赖规则

> 💡 **人类填写**: 记录依赖外部系统的规则和限制

| 依赖系统 | 调用限制 | 超时配置 | 降级策略 |
|---------|---------|---------|---------|
| 待人类填写 | - | - | - |

---

*🤖 AI 生成框架 - 人类填写具体内容*
""",

    "history-experience": """# 历史经验

> 🤖 **AI 扫描指南**：AI 通过两种途径扫描获取历史经验素材，人类再总结成文档
>
> **途径一：代码注释扫描**
> 1. AI 搜索代码注释中的关键词：TODO, FIXME, HACK, WORKAROUND, 踩坑, 坑, 历史债, 临时方案, 兼容老版本
> 2. 记录相关代码文件路径和行数
> 3. 分析哪些是通用经验，可总结到本文档
>
> **途径二：Git Commit 扫描**
> 1. AI 执行 git log --all --oneline --grep="fix\|bug\|问题\|修复\|解决" -n 50
> 2. 筛选有价值的 commit，执行 git show <commit-id> 查看详情
> 3. 总结可沉淀的经验
>
> ⚠️ **注意**：AI 只提供扫描结果和候选素材，人类负责确认和整理

---

## 从代码注释提取的经验

> 🤖 **AI 扫描任务**：搜索关键词，记录候选问题

### 候选问题 1

| 项目 | 内容 |
|------|------|
| **发现位置** | 文件路径:行号 |
| **注释原文** | 粘贴发现的注释 |
| **AI 分析** | 初步判断问题类型 |
| **人类确认** | ⬜ 确认 / ⬜ 忽略 |

---

## 从 Git Commit 提取的经验

> 🤖 **AI 扫描任务**：分析 git log 找出修复类 commit

### Commit 候选 1

| 项目 | 内容 |
|------|------|
| **Commit ID** | abc1234 |
| **Message** | 粘贴 message |
| **AI 分析** | 初步判断修复类型 |
| **人类确认** | ⬜ 深入总结 / ⬜ 忽略 |

---

## 已确认的经验记录

> 💡 **人类填写**: 从候选中筛选，整理成规范格式

### [问题标题]

**分类**: 环境配置 | 依赖冲突 | 性能问题 | 安全漏洞 | 业务逻辑 | 其他
**优先级**: P0-阻塞 | P1-严重 | P2-一般 | P3-低
**来源**: 代码注释 | Git Commit | 人工发现

#### 问题现象
描述问题

#### 根因分析
表面原因：
根本原因：

#### 修复方案
具体修改

#### 预防措施
如何避免

---

*🤖 AI 提供扫描素材 - 人类整理确认*
""",
}


def scan_project(root_path: str) -> dict:
    """扫描项目结构"""
    result = {
        "name": Path(root_path).name,
        "root_path": root_path,
        "scan_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "languages": [],
        "languages_str": "待 AI 分析",
        "languages_table": "| 语言 | 文件数 | 主要用途 |\n|------|--------|----------|\n| 🤖 AI 待分析 | - | 🤖 AI 待分析 |\n",
        "entry_points": [],
        "entry_points_str": "🤖 AI 待查找",
        "dependencies": [],
        "directory_tree": "",
        "modules": []
    }

    # 统计文件类型
    lang_count = {}
    for ext, lang in {
        ".ts": "TypeScript", ".tsx": "TypeScript",
        ".js": "JavaScript", ".jsx": "JavaScript",
        ".java": "Java", ".kt": "Kotlin",
        ".py": "Python", ".go": "Go",
        ".rs": "Rust", ".php": "PHP"
    }.items():
        files = list(Path(root_path).rglob(f"*{ext}"))
        if files:
            lang_count[lang] = lang_count.get(lang, 0) + len(files)

    result["languages"] = [f"{k} ({v} files)" for k, v in sorted(lang_count.items(), key=lambda x: -x[1])[:5]]
    if result["languages"]:
        result["languages_str"] = ", ".join(result["languages"])
        result["languages_table"] = "\n".join([f"| {k} | {v} | 🤖 AI 待分析 |" for k, v in sorted(lang_count.items(), key=lambda x: -x[1])[:5]])

    # 查找入口文件
    entry_patterns = ["main.py", "app.py", "index.js", "main.ts", "Main.java", "main.go"]
    entry_points = []
    for pattern in entry_patterns:
        files = list(Path(root_path).rglob(pattern))
        if files:
            entry_points.extend([str(f.relative_to(root_path)) for f in files[:3]])

    if entry_points:
        result["entry_points"] = entry_points
        result["entry_points_str"] = "\n".join([f"{i+1}. `{e}`" for i, e in enumerate(entry_points)])

    # 生成目录树（简化版）
    tree_lines = []
    for i, item in enumerate(sorted(Path(root_path).iterdir())):
        if item.name.startswith(".") and item.name not in [".github", ".vscode"]:
            continue
        if item.is_dir():
            tree_lines.append(f"📁 {item.name}/")
            # 显示子目录（限制数量）
            subdirs = [d for d in item.iterdir() if d.is_dir() and not d.name.startswith(".")][:3]
            for sub in subdirs:
                tree_lines.append(f"  📁 {sub.name}/")
        else:
            tree_lines.append(f"📄 {item.name}")
    result["directory_tree"] = "\n".join(tree_lines[:30])

    # 识别模块
    module_dirs = ["src", "app", "lib", "packages", "core", "api", "services"]
    for mod in module_dirs:
        mod_path = Path(root_path) / mod
        if mod_path.exists():
            file_count = len(list(mod_path.rglob("*")))
            result["modules"].append(f"| **{mod}** | `{mod}/` | {file_count} 个文件 |")

    if result["modules"]:
        result["modules"] = "\n".join(result["modules"])
    else:
        result["modules"] = "*AI 待分析：读取源文件后补充模块划分*"

    return result


def generate_document(template_name: str, data: dict) -> str:
    """生成文档内容"""
    template = TEMPLATES.get(template_name, "")
    # 使用 replace 而不是 format 来避免大括号冲突
    content = template.replace("{progressive_guide}", PROGRESSIVE_GUIDE)
    content = content.replace("{name}", data.get("name", ""))
    content = content.replace("{root_path}", data.get("root_path", ""))
    content = content.replace("{scan_time}", data.get("scan_time", ""))
    content = content.replace("{languages_str}", data.get("languages_str", ""))
    content = content.replace("{languages_table}", data.get("languages_table", ""))
    content = content.replace("{entry_points_str}", data.get("entry_points_str", ""))
    content = content.replace("{directory_tree}", data.get("directory_tree", ""))
    content = content.replace("{modules}", data.get("modules", ""))
    return content


def main():
    parser = argparse.ArgumentParser(description="AI README Generator")
    parser.add_argument("--root", default=".", help="Project root directory")
    parser.add_argument("--output", default=".ai-readme", help="Output directory")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    args = parser.parse_args()

    print("🔍 扫描项目...")
    project_data = scan_project(args.root)

    docs_to_generate = [
        ("generated/项目结构.md", "project-structure"),
        ("generated/技术架构.md", "tech-architecture"),
        ("generated/核心流程.md", "core-flow"),
        ("generated/接口约定.md", "api-convention"),
        ("generated/接口示例.md", "api-examples"),
        ("generated/数据模型.md", "data-model"),
        ("generated/数据库文档.md", "database-doc"),
        ("generated/错误处理.md", "error-handling"),
        ("generated/开发运行.md", "dev-guide"),
        ("manual/业务知识.md", "business-knowledge"),
        ("manual/历史经验.md", "history-experience"),
    ]

    output_dir = Path(args.root) / args.output

    if not args.dry_run:
        (output_dir / "generated").mkdir(parents=True, exist_ok=True)
        (output_dir / "manual").mkdir(parents=True, exist_ok=True)

    for filepath, template_name in docs_to_generate:
        print(f"📝 生成: {filepath}")
        content = generate_document(template_name, project_data)

        if args.dry_run:
            print(f"   [预览模式] 将生成 {len(content)} 字符")
        else:
            full_path = output_dir / filepath
            full_path.write_text(content, encoding="utf-8")
            print(f"   ✅ 已生成")

    # 生成 AGENT.md 导航
    agent_md = f"""# 项目上下文 - AI 开发引导

## 文档结构

### generated/ - AI 生成

| 文件 | 内容 |
|------|------|
| [项目结构.md](./generated/项目结构.md) | 目录结构、模块划分、入口文件 |
| [技术架构.md](./generated/技术架构.md) | 技术栈、架构分层、依赖关系 |
| [核心流程.md](./generated/核心流程.md) | 业务流程、状态机、异常处理 |
| [接口约定.md](./generated/接口约定.md) | 接口定义、请求规范、鉴权机制 |
| [接口示例.md](./generated/接口示例.md) | 请求/响应 JSON 示例 |
| [数据模型.md](./generated/数据模型.md) | 数据结构、关系、校验规则 |
| [数据库文档.md](./generated/数据库文档.md) | 数据字典、索引设计 |
| [错误处理.md](./generated/错误处理.md) | 错误类型、全局处理、监控 |
| [开发运行.md](./generated/开发运行.md) | 环境要求、构建命令、工具配置 |

### manual/ - 人工维护

| 文件 | 内容 |
|------|------|
| [业务知识.md](./manual/业务知识.md) | 业务规则、术语、状态流转 |
| [历史经验.md](./manual/历史经验.md) | 踩坑记录、最佳实践 |

---

## 使用指南

1. **AI 填充**: 使用 Claude/GPT 读取 `generated/` 文件，分析源代码后填充内容
2. **人工补充**: 团队成员填写 `manual/` 中的业务知识和历史经验
3. **定期更新**: 架构变更后重新生成，业务规则变化后更新 manual

---

*生成时间: {project_data['scan_time']}*
"""

    if not args.dry_run:
        (output_dir / "AGENT.md").write_text(agent_md, encoding="utf-8")
        print("✅ 文档生成完成!")
        print(f"\n输出目录: {output_dir}")
        print("\n下一步:")
        print("  1. AI 读取 generated/ 文件并填充内容")
        print("  2. 人工补充 manual/ 目录")
    else:
        print("\n[预览模式] 未写入文件")


if __name__ == "__main__":
    main()
