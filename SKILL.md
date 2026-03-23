---
name: ai-readme
description: "Generate AI-friendly project documentation skeleton. AI fills technical content in generated/ (9 files) AND scans code to create frameworks in manual/ (2 files) for human refinement."
---

# AI README Generator

Generate documentation skeleton for AI-assisted development.

## What This Skill Does

1. **Runs Python script** to scan project structure
2. **Creates 11 document skeletons** in `.ai-readme/`
3. **AI fills technical content** in `generated/` (9 files)
4. **AI scans and creates frameworks** in `manual/` (2 files) for humans to refine

## Command

```bash
/ai-readme generate
```

## Execution Steps

### Step 1: Run Generation Script

Execute the Python script to create document skeletons:

```bash
python /Users/zengye/code/ai/ai_readme/skills/ai-readme/scripts/generate.py --root . --output .ai-readme
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

### Step 2: Fill Technical Content (AI Task)

Read `generated/*.md` files and fill technical content by analyzing code.

### Step 3: Scan and Create Manual Frameworks (AI Task)

For `manual/` files, AI should:

**业务知识.md:**
- Scan code to identify business modules (order, user, product, etc.)
- Search for hardcoded values: `timeout`, `limit`, `max`, `min`, `default`
- Create module framework tables
- Humans fill specific business values

**历史经验.md:**
- **Option 1 - Code Comments:** Search for `FIXME`, `TODO`, `HACK`, `WORKAROUND`, `踩坑`, `历史债`
- **Option 2 - Git Commits:** Run `git log --all --oneline --grep="fix\|bug\|修复\|解决" -n 30`
- Create candidate lists for human review
- Humans confirm and organize into final experiences

### Step 4: Done

Document generation complete. Technical docs filled, manual frameworks created for human refinement.

## Important Rules

**AI SHOULD:**
- Fill `generated/*.md` with technical content from code analysis
- Scan code to identify business modules for `manual/业务知识.md` framework
- Search comments/git for potential issues for `manual/历史经验.md` candidates
- Create structured tables and lists for humans to fill

**AI SHOULD NOT:**
- Invent business values (timeouts, thresholds) without code evidence
- Write final "lessons learned" without human confirmation
- Guess at domain semantics

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

## Script Options

```bash
# Default - generate in current directory
python /Users/zengye/code/ai/ai_readme/skills/ai-readme/scripts/generate.py

# Custom project root
python /Users/zengye/code/ai/ai_readme/skills/ai-readme/scripts/generate.py --root /path/to/project

# Preview only
python /Users/zengye/code/ai/ai_readme/skills/ai-readme/scripts/generate.py --dry-run
```
