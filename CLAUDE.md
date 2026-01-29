# Project: NLP Textbook (tech_blog)

## Overview
This is a Quarto-based technical blog that includes an NLP textbook series ("NLP: From Symbols to Intelligence"). The textbook follows a **pain-driven, model-centered** narrative tracing the evolution of NLP from pre-deep-learning to the LLM era.

## NLP Textbook Structure
- **Source files**: `posts_ch/nlp/ch00-*.qmd` through `ch18-*.qmd` (20 chapters written, ch00-ch18 + new ch02)
- **Outline**: `.claude/skills/nlp-textbook-chapter/references/outline.md` (36-chapter plan, v3.3)
- **Writing guide/skill**: `.claude/skills/nlp-textbook-chapter/SKILL.md`
- **Chapter template**: `.claude/skills/nlp-textbook-chapter/references/template.md`
- **Writing examples**: `.claude/skills/nlp-textbook-chapter/references/examples.md`
- **Open textbook resources**: `.claude/skills/nlp-textbook-chapter/references/open-textbooks.md`
- **University course resources**: `.claude/skills/nlp-textbook-chapter/references/university-courses.md`
- **D2L figure resources**: `.claude/skills/nlp-textbook-chapter/references/d2l-resources.md`

## Writing Progress
- **Completed**: Ch0–Ch18 + Ch2 (NLP核心任务全景) = 20 chapters written
- **Next to write**: Ch19 (分布式训练系统) onward; Ch27 (MoE) and Ch28 (SSM/Mamba) are priority new chapters
- **Restructure reference**: `nlp-textbook-restructure-plan.md` documents the completed restructuring (v3.0→v3.3)

## Writing Style
- Language: Chinese (Simplified) for content, English for technical terms
- Style: Pain-driven history, intuition before formulas, researcher-oriented
- Always use the `nlp-textbook-chapter` skill when writing new chapters
- Refer to `learner-profile` and `writing-style` skills for tone/style guidance
- Follow `technical-standards` skill for LaTeX, Markdown, Quarto formatting

## Other Content
- **Damodaran valuation series**: `posts_ch/valuation/` (uses `damodaran-series-guide` skill)
- **Rendered site**: `docs/` directory (auto-generated, do not edit directly)

## Tech Stack
- Quarto for rendering
- GitHub Pages for hosting
- Mermaid/SVG for diagrams
