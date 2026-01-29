# TODO: NLP textbook audit plan (ch9-ch15)

## Skills to apply (read first)
- .claude/skills/nlp-textbook-chapter/SKILL.md
- .claude/skills/writing-style/SKILL.md
- .claude/skills/learner-profile/SKILL.md
- .claude/skills/technical-standards/SKILL.md
- .claude/skills/paper-figure-extractor.md

## Chapter scope (files)
- posts_ch/nlp/ch09-efficient-attention.qmd
- posts_ch/nlp/ch10-pretraining-origins.qmd
- posts_ch/nlp/ch11-elmo.qmd
- posts_ch/nlp/ch12-gpt.qmd
- posts_ch/nlp/ch13-bert.qmd
- posts_ch/nlp/ch14-pretraining-objectives.qmd
- posts_ch/nlp/ch15-engineering-optimization.qmd

## Skill requirements distilled into a checklist
- Structure: follow the 0-7 section spine from the chapter template; pain-point-driven opening; clear bridge from prior chapter.
- Researcher orientation: include boundary conditions, failure modes/limitations, and open questions.
- Writing style: intuition before formulas, prose-first (avoid list-heavy exposition), use analogies and multi-angle explanations.
- Numeric example: at least one small, hand-computable worked example for the core algorithm.
- References: a dedicated reference callout block per chapter with at least one paper, one open textbook, and one public course; record specific sections/figures/algorithms used.
- Figures: at least one figure sourced from a paper/textbook/course (or clearly labeled as author-drawn); include caption + source.
- Algorithm box: at least one algorithm/pseudocode callout sourced from a paper (or explicitly marked as adapted).
- Technical standards: YAML front matter completeness; LaTeX/Markdown conflicts avoided; image paths are relative and renderable.

## Inputs to collect
- Extract the required items from the five skills above into a single audit checklist.
- From nlp-textbook-outline.md, confirm the narrative placement of ch9-ch15 and any cross-chapter dependencies.
- Identify expected figure/algorithm candidates per chapter based on the key papers in the outline.

## Per-chapter audit steps
- Verify structural sections (0-7) and pain-point-driven intro.
- Check researcher-oriented content (boundary conditions, failure modes, open questions).
- Check writing style (intuition before formulas, prose flow, analogies, multi-angle views).
- Confirm at least one worked numeric example for the core method.
- Validate YAML front matter fields and technical-standards compliance.

## References and sources audit
- Locate the reference callout block and confirm it lists: papers, open textbooks, and public courses.
- For each cited source, record which section/figure/algorithm is used in the chapter.
- Flag missing/unclear attributions or sources that are mentioned but not actually used.

## Figures and algorithm boxes audit
- Inventory all figures and algorithm/pseudocode callouts in ch9-ch15.
- For each figure: record caption, file path, and source line; verify origin (paper/book/course or labeled author-drawn).
- For each algorithm box: verify it matches a paper algorithm; if adapted, mark it explicitly.
- Check figure storage paths under posts_ch/nlp/figures/chapter-9..15/original and note missing folders/files.
- If images are extracted from papers, confirm white-background handling and proper citation format.

## Open resources usage
- From skills, list the target open textbooks (D2L, UDL, SLP3, etc.) and public courses (CS224N, CMU 11-711, etc.).
- For each chapter, verify at least one concrete usage (figure/insight/teaching framing) from these resources.
- Identify underused resources and propose where to integrate them.

## Redundancy and overlap check
- Identify repeated explanations across ch9-ch15 (e.g., GPT vs BERT pretraining objectives).
- Recommend consolidation points or cross-links to avoid repetition.

## Deliverables (after review)
- Compliance matrix: chapters x skill requirements (pass/partial/fail + notes).
- Asset inventory: all images/algorithms with sources and attribution status.
- Gap list: missing references, missing figures, missing algorithm boxes, missing numeric examples.
- Priority fixes: ordered list of edits per chapter.
- Resource integration plan: which open textbook/course assets to add where.
