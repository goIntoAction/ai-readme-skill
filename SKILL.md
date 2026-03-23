---
name: ai-readme
description: "Generate AI-friendly project documentation skeleton. AI fills technical content in generated/ (9 files) AND scans code to create frameworks in manual/ (2 files) for human refinement."
---

# AI README Generator

Generate documentation skeleton for AI-assisted development.

## What This Skill Does

1. **Runs Python script** to scan project structure
2. **Creates 11 document skeletons** in `.ai-readme/`
3. **AI evaluates which documents are relevant** and fills them
4. **AI generates task index** and appends to `AGENT.md`
5. **AI scans and creates frameworks** in `manual/` (2 files) for humans to refine

## Command

```bash
/ai-readme generate
```

## Execution Steps

### Step 1: Run Generation Script

Execute the Python script to create document skeletons:

```bash
python /Users/zengye/code/ai_readme-skill/scripts/generate.py --root . --output .ai-readme
```

This creates:
```
.ai-readme/
├── AGENT.md              # Navigation entry point
├── generated/            # AI fills these (technical content)
│   ├── 项目结构.md       # Project structure
│   ├── 技术架构.md       # Tech architecture
│   ├── 核心流程.md       # Core flows
│   ├── 接口约定.md       # API conventions
│   ├── 接口示例.md       # API examples
│   ├── 数据模型.md       # Data models
│   ├── 数据库文档.md     # Database docs
│   ├── 错误处理.md       # Error handling
│   └── 开发运行.md       # Dev setup
└── manual/               # AI creates frameworks, humans refine
    ├── 业务知识.md       # AI scans code → human fills values
    └── 历史经验.md       # AI scans comments/git → human confirms
```

### Step 2: Evaluate Document Relevance and Fill Content

Read `generated/*.md` files, then evaluate each one:

**判断方式**：
- 扫描完项目后，针对每个文档自问：本项目是否有与这个文档主题相关的内容？
- **有** → 正常填充
- **完全没有** → 在文档开头写一行 `本项目无 [主题相关内容]，跳过`，不做全文填充

**不依赖文件类型列表判断**，AI 扫描项目后自然知道该项目有什么、没有什么。

### Step 3: Generate Task Index (AI Auto-generates)

After filling all relevant `generated/` content, **proactively** scan the actual filled content and append a task index table to the end of `AGENT.md`. Format:

```markdown
## 按任务查文档

| 任务场景 | 相关文档 | 关键代码位置 |
|---------|---------|------------|
| 改订单创建逻辑 | 核心流程.md | OrderServiceImpl.submit() @ OrderServiceImpl.java:91 |
| 改商品库存逻辑 | 核心流程.md | SkuStockService.lock() @ SkuStockLockServiceImpl.java |
| 改登录认证逻辑 | 核心流程.md | AuthAccountServiceImpl @ AuthAccountServiceImpl.java:40 |
| 查分布式事务配置 | 技术架构.md | — |
| 改接口定义 | 接口约定.md, 接口示例.md | 对应 Feign Client 或 Controller |
| 改数据模型 | 数据模型.md | 对应 Entity/Model |
| 查错误码 | 错误处理.md | ResponseEnum 定义位置 |
| ... | ... | ... |
```

**生成规则**：
- 每个有实际内容的文档至少生成 1 行
- 代码位置精确到文件名和方法名，不要只写文件路径
- 不要写"待填充"，只写实际填充后的真实内容

### Step 4: Scan and Create Manual Frameworks (AI Task)

For `manual/` files, AI should:

**业务知识.md:**
- Scan code to identify business modules (order, user, product, etc.)
- Search for hardcoded values: `timeout`, `limit`, `max`, `min`, `default`
- Create module framework tables
- Humans fill specific business values

**历史经验.md:**
- **Option 1 - Code Comments:** Search for `FIXME`, `TODO`, `HACK`, `WORKAROUND`, `踩坑`, `历史债`, `临时方案`, `兼容老版本`
- **Option 2 - Git Commits:** Run `git log --all --oneline --grep="fix\|bug\|修复\|解决" -n 30`
- Create candidate lists for human review
- Humans confirm and organize into final experiences
- **Anti-Patterns**: Also scan for `// 不要用`, `// 严禁`, `// 不能这样写`, `// 禁止` 等反模式注释，记录"不该怎么做"

### Step 5: Done

Document generation complete. Technical docs filled, task index generated, manual frameworks created for human refinement.

---

## Quality Standards

**AI SHOULD:**
- Fill `generated/*.md` with technical content from code analysis
- Scan code to identify business modules for `manual/业务知识.md` framework
- Search comments/git for potential issues for `manual/历史经验.md` candidates
- Create structured tables and lists for humans to fill
- Generate task index based on **actual filled content**, not placeholders

**Quality Requirements:**

1. **`核心流程.md` must contain real code locations**
   - Every key function MUST include: file path + line number range
   - Example: `OrderServiceImpl.submit() @ OrderServiceImpl.java:91-130`
   - Sequence diagrams alone are not enough — AI must locate exact code

2. **`历史经验.md` must include Anti-Patterns**
   - In addition to bug fixes, also record: "what NOT to do"
   - Scan for comments like `// 不要用这种方式`, `// 严禁`, `// 错误写法`
   - These anti-patterns are often more valuable than bug records

**AI SHOULD NOT:**
- Invent business values (timeouts, thresholds) without code evidence
- Write final "lessons learned" without human confirmation
- Guess at domain semantics
- Generate task index rows with "待填充" or placeholder content
- Write code locations that don't actually exist in the codebase
- 改变文档的章节结构（骨架文件的 ## 标题顺序不能打乱）
- 跳过任何空模板段落不填充
- 自己发挥写文档里没有提到的主题
- 写到"待填充"就停下来，必须填完所有章节

---

## Document Types

**generated/ (AI fills completely):**
- Technical architecture
- Code structure
- Data models
- API definitions
- Error handling

**manual/ (AI creates framework, humans fill details):**
- Business rules and values
- Team lessons learned (AI provides candidates, humans confirm)
- Anti-patterns (AI scans, humans confirm)

## Script Options

```bash
# Default - generate in current directory
python /Users/zengye/code/ai_readme-skill/scripts/generate.py

# Custom project root
python /Users/zengye/code/ai_readme-skill/scripts/generate.py --root /path/to/project

# Preview only
python /Users/zengye/code/ai_readme-skill/scripts/generate.py --dry-run
```
