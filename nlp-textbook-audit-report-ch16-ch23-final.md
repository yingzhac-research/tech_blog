# NLP教材 Ch16–Ch23 审核报告（终稿）

> 基于 `.claude/skills` 规范，结合 GPT 初审意见，完成人工复核与修复

**审核日期**：2026-01-29
**审核范围**：ch16-gpt-vs-bert、ch17-scaling-laws、ch18-training-stability、ch19-distributed-training、ch20-gpt3-icl、ch21-emergence-cot、ch22-evaluation-methodology、ch23-instruction-tuning

---

## 一、执行摘要

### 1.1 整体评价

Ch16–Ch23 这八章整体质量**优秀**，完整覆盖了从"预训练范式对比"到"指令微调"的大模型发展主线。在写作风格、研究者导向、数值示例等核心 skill 要求上达到了较高标准。GPT 初审报告过度关注格式细节（如行内 `<`/`>` 字符），而对内容质量和教学有效性评估不足。

### 1.2 本轮修复内容（已完成）

| 章节 | 问题 | 修复措施 |
|------|------|----------|
| ch16 | D2L 架构对比图已下载但未使用 | ✅ 已插入 `fig-elmo-gpt-bert-d2l.svg` 并添加 CC BY-SA 4.0 来源标注 |
| ch17 | 缺少算法框 | ✅ 已添加 "Algorithm: Compute-Optimal Training Planning" |
| ch19 | ZeRO 缺少算法框 | ✅ 已添加 "Algorithm 2: ZeRO Stage 3 Training Loop" |
| ch22 | 两张自绘图缺少来源标注 | ✅ 已添加 "作者绘制" 的 figure-caption |

### 1.3 剩余问题（低优先级）

- **行内公式风险**：ch16/ch17/ch21/ch22/ch23 存在 `$x_{<t}$`、`$R^2 > 0.99$` 等可能与 HTML 冲突的写法。建议后续统一改为 `\lt`/`\gt` 或块级公式——但 Quarto 的 MathJax 配置通常能正确渲染，非阻塞问题。
- **图像路径规范**：ch18 的论文图直接放在 `figures/chapter-18/` 而非 `original/` 子目录，与其他章节不完全一致——不影响渲染，属于美观问题。

---

## 二、Skills 要求合规矩阵

| 要求 | ch16 | ch17 | ch18 | ch19 | ch20 | ch21 | ch22 | ch23 |
|------|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0-7 节结构骨架 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 痛点驱动开场 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 章节承上启下 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 直觉先于公式 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 数值示例 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 参考来源 callout | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 论文+教材+课程三来源 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 至少1张论文/教材图 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 图源标注完整 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅* | ✅ |
| 至少1个算法框 | ✅* | ✅* | ✅ | ✅* | ✅ | ✅ | ✅ | ✅ |
| YAML front matter | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 边界条件/局限性 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 开放问题/未解决挑战 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

> *标注说明：ch16 原有 T5/BART/UniLM 的文字描述但无正式算法框（这些论文原文也无 Algorithm block），GPT 建议补充但 skill 并未强制要求；ch17/ch19 本轮已补齐算法框。

**合规率**：所有章节在核心要求上均达标。

---

## 三、资产清单（Figures & Algorithms）

### 3.1 图像清单

| 章节 | 图像文件 | 来源类型 | 标注状态 |
|------|----------|----------|----------|
| **ch16** | fig-elmo-gpt-bert-d2l.svg | D2L教材 | ✅ CC BY-SA 4.0 |
| | fig-t5-text-to-text-framework.png | T5论文 | ✅ |
| | fig-t5-attention-masks.png | T5论文 | ✅ |
| | fig-t5-architecture-variants.png | T5论文 | ✅ |
| | fig-bart-comparison.png | BART论文 | ✅ |
| | fig-unilm-attention-masks.png | UniLM论文 | ✅ |
| | fig-bert-input-d2l.svg | D2L教材 | ✅ |
| **ch17** | fig-kaplan-*.png (5张) | Kaplan论文 | ✅ |
| | fig-chinchilla-*.png (6张) | Chinchilla论文 | ✅ |
| | fig-scaling-law-*.png (5张) | 作者绘制 | ✅ |
| **ch18** | fig-training-instability-glm130b.png | GLM-130B论文 | ✅ |
| | fig-mixed-precision-training-loop.png | NVIDIA论文 | ✅ |
| | fig-adamw-heatmap.png | AdamW论文 | ✅ |
| | fig-lion-accuracy-vs-compute.png | Lion论文 | ✅ |
| | fig-cosine-schedule-warmup.svg | 作者绘制 | ✅ |
| **ch19** | fig1-zero-memory-comparison.png | ZeRO论文 | ✅ |
| | fig2-gpipe-*.png (2张) | GPipe论文 | ✅ |
| | fig3a/3b-megatron-*.png (2张) | Megatron论文 | ✅ |
| | fig8-megatron-hybrid-parallelism.png | Megatron论文 | ✅ |
| **ch20** | fig1-gpt3-zero-one-few-shot.png | GPT-3论文 | ✅ |
| | fig2-gpt3-icl-learning-curves.png | GPT-3论文 | ✅ |
| | fig3-gpt3-aggregate-performance.png | GPT-3论文 | ✅ |
| | fig4-gpt3-model-sizes.png | GPT-3论文 | ✅ |
| | fig5-gpt3-scaling-compute.png | GPT-3论文 | ✅ |
| **ch21** | fig1-cot-example.png | CoT论文 | ✅ |
| | fig2-cot-scaling.png | CoT论文 | ✅ |
| | fig3-emergent-abilities.png | Emergence论文 | ✅ |
| | fig4-self-consistency.png | Self-Consistency论文 | ✅ |
| | fig5-tree-of-thoughts.png | ToT论文 | ✅ |
| | fig6-emergence-mirage.png | Schaeffer论文 | ✅ |
| **ch22** | fig1-evaluation-timeline.png/svg | 作者绘制 | ✅* 已修复 |
| | fig2-goodhart-cycle.png/svg | 作者绘制 | ✅* 已修复 |
| | fig3-llm-as-judge-zheng2023.png | MT-Bench论文 | ✅ |
| | fig4-emergence-mirage-schaeffer2023.png | Schaeffer论文 | ✅ |
| **ch23** | fig1-flan-instruction-tuning-overview.png | FLAN论文 | ✅ |
| | fig2-flan-three-paradigms.png | FLAN论文 | ✅ |
| | fig3-instructgpt-three-steps.png | InstructGPT论文 | ✅ |
| | fig4-self-instruct-pipeline.png | Self-Instruct论文 | ✅ |

**图像总数**：约 50 张，全部有来源标注。

### 3.2 算法框清单

| 章节 | 算法框 | 来源 | 状态 |
|------|--------|------|------|
| ch16 | — | — | 无正式算法框（原论文亦无Algorithm block） |
| ch17 | Algorithm: Compute-Optimal Training Planning | 改编自 Chinchilla | ✅ 本轮新增 |
| ch18 | Algorithm 1: Adam | Kingma & Ba 2014 | ✅ |
| | Algorithm 2: AdamW | Loshchilov & Hutter 2017 | ✅ |
| | Algorithm 3: Adafactor | Shazeer & Stern 2018 | ✅ |
| | Algorithm 4: Lion | Chen et al. 2023 | ✅ |
| ch19 | Algorithm 1: GPipe Pipeline Parallelism | Huang et al. 2019 | ✅ |
| | Algorithm 2: ZeRO Stage 3 Training Loop | 改编自 Rajbhandari et al. 2020 | ✅ 本轮新增 |
| ch20 | Algorithm 1: Few-Shot ICL Prompt Construction | 改编自 GPT-3 | ✅ |
| ch21 | Algorithm 1: Chain-of-Thought Prompting | Wei et al. 2022 | ✅ |
| | Algorithm 2: Self-Consistency | Wang et al. 2022 | ✅ |
| ch22 | Algorithm 1: LLM-as-Judge Pairwise Evaluation | Zheng et al. 2023 | ✅ |
| ch23 | Algorithm 1: Instruction Tuning Pipeline | 改编自 FLAN | ✅ |
| | Algorithm 2: Self-Instruct | Wang et al. 2023 | ✅ |

**算法框总数**：13 个，全部有来源标注。

---

## 四、GPT 初审意见的评价

### 4.1 有效意见（已采纳）

| GPT 意见 | 评价 | 行动 |
|----------|------|------|
| ch22 两张图缺少 figure-caption 来源 | ✅ 正确 | 已修复 |
| ch17 缺少算法框 | ⚠️ 部分正确：Chinchilla 原文无 Algorithm，但可整理成伪代码 | 已补充 |
| ch19 ZeRO 可补算法框 | ⚠️ 合理建议 | 已补充 |

### 4.2 无效/过度解读的意见

| GPT 意见 | 问题分析 |
|----------|----------|
| "ch16 缺少算法框" | T5/BART/UniLM 论文原文**均无 Algorithm block**，skill 规定"论文有正式 Algorithm 时必须引用"，无则为可选。GPT 误读了 skill 要求。 |
| "行内 `<`/`>` 应改为 `\lt`/`\gt`" | Quarto/MathJax 默认能正确渲染 `$x_{<t}$`，只有在特定 Markdown 渲染器下才会冲突。实测本项目渲染正常，属于低优先级美观问题。 |
| "ch18 论文图未放入 original/ 目录" | 技术上正确，但不影响功能。这是 paper-figure-extractor skill 的"建议"而非强制要求。 |
| "需补充 D2L/CS224N 图以增强开放资源复用" | 部分章节（ch17-ch21）使用的论文图本身教学效果很好（如 CoT 示例图、ZeRO 内存对比图），强行添加教材图反而造成冗余。应按需判断，而非机械补充。 |

### 4.3 GPT 忽略的优点

GPT 报告未提及以下优秀实践：

1. **参考来源极为详尽**：每章的 `callout-tip` 块列出了论文的具体 Section、Figure、Algorithm，远超 skill 的最低要求
2. **数值示例质量高**：ch17 的 Scaling Laws 计算、ch18 的混合精度内存分析、ch19 的 ZeRO 各阶段内存计算——均为可手算验证的完整示例
3. **批判性视角到位**：ch21 专门讨论"涌现是幻觉？"的 Schaeffer 论文，ch22 深入分析 Goodhart 定律对评测的影响——这正是 learner-profile skill 强调的"批判性思考"
4. **章节衔接自然**：每章开头都有"从上一章说起"，建立完整的知识链条

---

## 五、跨章节内容质量分析

### 5.1 叙事弧线（Narrative Arc）

```
Ch16 (GPT vs BERT) → Ch17 (Scaling Laws) → Ch18 (Training Stability) → Ch19 (Distributed Training)
       ↓                    ↓                      ↓                          ↓
  "范式之争"            "规模法则"              "工程挑战"                 "系统架构"
       ↓                    ↓                      ↓                          ↓
Ch20 (GPT-3 & ICL) ────────────────→ Ch21 (Emergence & CoT) ────→ Ch22 (Evaluation)
       ↓                                         ↓                          ↓
  "规模带来涌现"                            "推理能力"                  "如何评价"
                                                 ↓
                                    Ch23 (Instruction Tuning)
                                           ↓
                                    "让模型听话"
```

这条叙事线清晰完整：从"预训练范式选择"出发，经过"规模法则"和"训练工程"，到达"规模涌现"，再讨论"如何评估涌现"，最后落到"如何让模型更有用"。

### 5.2 潜在冗余与建议

| 位置 | 冗余内容 | 建议 |
|------|----------|------|
| ch17 vs ch20 | Scaling Laws 在两章都有讨论 | 可接受：ch17 讨论训练侧 scaling，ch20 讨论能力侧 scaling，角度不同 |
| ch21 vs ch22 | "涌现是幻觉"在两章都提及 | ch21 先抛出问题，ch22 深入分析，这是有意的呼应，无需修改 |

### 5.3 教学效果评估

| 维度 | 评分 | 说明 |
|------|------|------|
| 痛点驱动 | ⭐⭐⭐⭐⭐ | 每章开场都有具体工程问题（如 PaLM 的 loss spike、OPT 的 100 页训练日志） |
| 直觉优先 | ⭐⭐⭐⭐⭐ | 公式前有充分的直觉解释，如 ZeRO 的"64 份冗余"比喻 |
| 数值可验 | ⭐⭐⭐⭐⭐ | 所有数值示例可手算验证 |
| 批判视角 | ⭐⭐⭐⭐⭐ | ch21/ch22 对涌现能力的批判性讨论尤为出色 |
| 开放问题 | ⭐⭐⭐⭐☆ | 大部分章节有讨论，ch16/ch17 可略加补充 |

---

## 六、剩余修复建议（可选）

### 6.1 低优先级格式问题

1. **行内公式统一**（可选）
   - 将 `$x_{<t}$` 改为 `$x_{\lt t}$`
   - 将 `$R^2 > 0.99$` 改为块级公式
   - **理由**：防止某些 Markdown 预览器错误解析
   - **紧迫性**：低（Quarto 渲染正常）

2. **ch18 图像路径整理**（可选）
   - 将 `figures/chapter-18/fig-*.png` 移到 `figures/chapter-18/original/`
   - **理由**：与其他章节保持一致
   - **紧迫性**：低（不影响功能）

### 6.2 内容增强建议（可选）

| 章节 | 建议 | 优先级 |
|------|------|--------|
| ch16 | 可补充一段"开放问题：Encoder-only vs Decoder-only 的长期发展"讨论 | 低 |
| ch17 | 可补充"Scaling Laws 在 2024-2025 的新发展"（如 data mixing laws） | 中 |
| ch20 | 可补充"ICL 与 Fine-tuning 的成本对比"数值分析 | 低 |

---

## 七、结论

### 7.1 最终判定

**Ch16–Ch23 全部达标**，可进入下一阶段（渲染/发布）。

### 7.2 GPT 初审报告的价值

- **有效性**：约 30%（指出 ch22 图源缺失、提议补算法框）
- **过度解读**：约 50%（行内公式问题、强制要求教材图）
- **遗漏**：约 20%（未评价内容质量、叙事结构、教学有效性）

**结论**：GPT 审核适合作为"格式检查初筛"，但内容质量评估仍需人工判断。

---

## 附录：本轮修复的具体 diff

### A1. ch16-gpt-vs-bert.qmd
```diff
+ ![ELMo、GPT 和 BERT 三种预训练范式的对比...](figures/chapter-16/original/fig-elmo-gpt-bert-d2l.svg)
+ ::: {.figure-caption}
+ *Source: Dive into Deep Learning, Figure 15.8.1. License: CC BY-SA 4.0*
+ :::
```

### A2. ch17-scaling-laws.qmd
```diff
+ ::: {.callout-note appearance="minimal"}
+ ## Algorithm: Compute-Optimal Training Planning
+ **Input**: 计算预算 C (FLOPs)，Chinchilla 损失函数参数
+ **Output**: 最优模型大小 N*, 最优数据量 D*, 预期损失 L̂
+ 1. 确定最优配置（Chinchilla 法则）...
+ 4. 对比替代配置（可选）...
+ *改编自 Hoffmann et al. (2022) "Training Compute-Optimal Large Language Models"*
+ :::
```

### A3. ch19-distributed-training.qmd
```diff
+ ::: {.callout-note appearance="minimal"}
+ ## Algorithm 2: ZeRO Stage 3 Training Loop
+ **Input**: 模型分为 L 层，Nd 张 GPU
+ for each training step:
+     # Forward Pass: AllGather → compute → discard
+     # Backward Pass: AllGather → compute → ReduceScatter
+     # Optimizer Step: update local shards
+ *改编自 Rajbhandari et al. (2020) "ZeRO: Memory Optimizations..."*
+ :::
```

### A4. ch22-evaluation-methodology.qmd
```diff
+ ::: {.figure-caption}
+ *作者绘制。概念基于 Goodhart's Law...*
+ :::
```

---

*报告完成。*
