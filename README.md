# ai-readme

AI-friendly project documentation generator. Generates a documentation skeleton that AI can fill by scanning project code.

## What It Does

1. **Script** scans project structure and generates 11 document skeletons in `.ai-readme/`
2. **AI** fills technical content by analyzing source code
3. **AI** generates a task index table for quick navigation
4. **AI** scans code comments and git history to build experience documentation for humans to refine

## Usage

```bash
# Generate documentation skeleton
python scripts/generate.py --root /path/to/project --output .ai-readme

# Then let AI fill the content following SKILL.md instructions
```

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

- **Auto-adaptive**: AI determines which documents are relevant based on actual project scan — no manual filtering needed
- **Code-grounded**: 核心流程.md requires real code locations (file + line numbers)
- **Anti-Patterns**: 历史经验.md includes a dedicated section for recording what NOT to do
- **Task Index**: AGENT.md includes a task-based navigation table generated from actual filled content

## Skill Installation

Point your AI agent to this directory. The SKILL.md defines the full workflow and quality standards.
