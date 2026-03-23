# ai-readme

AI-friendly project documentation generator. Point your AI agent to this skill, and it will scan your project and generate a full documentation set.

## What It Does

1. **Scans** project structure and generates 11 document skeletons
2. **AI fills** technical content by analyzing source code
3. **AI generates** a task index table for quick navigation
4. **AI scans** code comments and git history to build experience documentation for humans to refine

## How to Use

In Claude (or any AI agent that supports skills), reference this skill:

```
@ai-readme
```

Then run:

```
/ai-readme generate
```

The AI will:
1. Run the generation script to create document skeletons
2. Fill all `generated/` documents with technical content from code analysis
3. Generate a task index table and append it to `AGENT.md`
4. Build frameworks in `manual/` for human refinement

## Generated Structure

```
.ai-readme/
├── AGENT.md              # Navigation + task index
├── generated/            # AI fills these
│   ├── 项目结构.md
│   ├── 技术架构.md
│   ├── 核心流程.md
│   ├── 接口约定.md
│   ├── 接口示例.md
│   ├── 数据模型.md
│   ├── 数据库文档.md
│   ├── 错误处理.md
│   └── 开发运行.md
└── manual/               # AI builds framework, humans fill
    ├── 业务知识.md
    └── 历史经验.md
```

## Key Features

- **Auto-adaptive**: AI determines which documents are relevant based on actual project scan — works for frontend, backend, mobile, or any language/framework
- **Code-grounded**: 核心流程.md requires real code locations (file + line numbers), not vague descriptions
- **Anti-Patterns**: 历史经验.md includes a dedicated section for recording what NOT to do, sourced from code comments
- **Task Index**: AGENT.md includes a task-based navigation table generated from actual filled content

## Quality Standards

The skill enforces two hard rules:
1. Every key function in 核心流程.md must include real file path + line number
2. 历史经验.md must include Anti-Patterns — what NOT to do is often more valuable than bug records

## Manual vs Generated

**Generated (AI fills completely):**
- Project structure, architecture, data models, API definitions, error handling

**Manual (AI builds framework, humans fill):**
- Business rules and values
- Team lessons learned (AI provides candidates, humans confirm)
- Anti-patterns (AI scans, humans confirm)
