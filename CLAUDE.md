# Project: NLP Textbook (tech_blog)

## Overview
This is a Quarto-based technical blog that includes an NLP textbook series ("NLP: From Symbols to Intelligence"). The textbook follows a **pain-driven, model-centered** narrative tracing the evolution of NLP from pre-deep-learning to the LLM era.

## NLP Textbook Structure
- **Source files**: `posts_ch/nlp/ch00-*.qmd` through `ch18-*.qmd` (19 chapters written, ch00-ch18)
- **Outline**: `.claude/skills/nlp-textbook-chapter/references/outline.md` (34-chapter plan, v3.0)
- **Writing guide/skill**: `.claude/skills/nlp-textbook-chapter/SKILL.md`
- **Chapter template**: `.claude/skills/nlp-textbook-chapter/references/template.md`
- **Writing examples**: `.claude/skills/nlp-textbook-chapter/references/examples.md`
- **Open textbook resources**: `.claude/skills/nlp-textbook-chapter/references/open-textbooks.md`
- **University course resources**: `.claude/skills/nlp-textbook-chapter/references/university-courses.md`
- **D2L figure resources**: `.claude/skills/nlp-textbook-chapter/references/d2l-resources.md`

## Active Restructure Plan
**IMPORTANT**: There is an active restructuring plan at `nlp-textbook-restructure-plan.md` in the project root. This plan proposes 4 changes based on comparison with classic NLP textbooks (SLP3, D2L, UDL, DLB, PML) and courses (CS224N, CMU 11-711, Princeton COS 484). Read this file before making any structural changes to the textbook.

### Summary of planned changes:
1. **Merge Ch5+Ch6** → combined "Attention Mechanism" chapter
2. **Add new Ch2** → "NLP Core Tasks Overview" (task landscape map)
3. **Add new Ch27** → "Beyond Dense Transformer" (SSM/Mamba + MoE)
4. **Expand Ch12 (GPT)** → add decoding strategies section

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
