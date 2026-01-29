# NLP教材 ch16–ch23 审核报告（基于 .claude/skills）

## 依据的 skills
- nlp-textbook-chapter：章节结构、参考来源记录、配图/伪代码要求、图像存放规范
- writing-style：直觉先于公式、散文式叙述、类比与数值例子
- technical-standards：YAML front matter、公式/Markdown/中英混排规范
- learner-profile：强调“为什么”、边界条件、批判性与开放问题
- paper-figure-extractor：论文配图提取与来源标注规范

## 检查范围
- posts_ch/nlp/ch16-gpt-vs-bert.qmd
- posts_ch/nlp/ch17-scaling-laws.qmd
- posts_ch/nlp/ch18-training-stability.qmd
- posts_ch/nlp/ch19-distributed-training.qmd
- posts_ch/nlp/ch20-gpt3-icl.qmd
- posts_ch/nlp/ch21-emergence-cot.qmd
- posts_ch/nlp/ch22-evaluation-methodology.qmd
- posts_ch/nlp/ch23-instruction-tuning.qmd

## 外部资料抽查（论文/教材/课程）
- 论文：T5、BART、UniLM、GPT-3、Scaling Laws、Chinchilla、Self-Instruct、Emergent Abilities Mirage 等核心来源已抽查页面与关键图表说明。
- 教材：D2L、SLP3
- 课程：Stanford CS224N

> 注：部分论文页面因工具访问限制未能完整打开（如 CoT / ToT 等），报告中的缺口与建议以当前章节文本与模板要求为准，建议人工复核原文细节。

---

## 逐章问题

### 第16章：GPT vs BERT（ch16-gpt-vs-bert）
- 伪代码：缺少算法框（建议补 T5/BART/UniLM 中的核心流程或 mask 构造伪代码，并注明“改编自”）。
- 技术规范：行内公式含 `<`（如 $x_{<t}$）应改为块级公式或使用 `\lt`。
- 资源利用：本章图片均来自论文，公开教材/课程的图示与讲解仅体现在参考来源中，建议至少补一张 D2L/CS224N 的架构对比/注意力模式图以增强“开放资源复用”。

### 第17章：Scaling Laws（ch17-scaling-laws）
- 伪代码：缺少算法框（建议补“compute-optimal 分配/拟合流程”的伪代码，标注改编自 Kaplan/Chinchilla）。
- 技术规范：行内公式含 `>`（如 $R^2 > 0.99$）应改为块级公式或使用 `\gt`。
- 资源利用：本章主要使用论文图，公开课/教材的教学图示可补充一张以强化“方法论总结”。

### 第18章：训练稳定性（ch18-training-stability）
- 图像存放：多张论文来源图未放在 `figures/chapter-18/original/`（如 GLM-130B loss spike、AdamW heatmap、Lion 对比等），不符合“论文原图入 original 目录”的规范；建议移动或调整路径。
- 其他：结构、参考来源、算法框、数值例子均符合要求。

### 第19章：分布式训练（ch19-distributed-training）
- 整体符合：结构、参考来源、配图、算法框、数值例子均到位。

### 第20章：GPT-3 ICL（ch20-gpt3-icl）
- 整体符合：参考来源、配图、算法框、数值例子均到位。

### 第21章：涌现与 CoT（ch21-emergence-cot）
- 技术规范：行内公式含 `>`/`<`（如 $p > 0.5$, $p < 0.5$）应改为块级公式或 `\gt/\lt`。
- 其他：配图、算法框、数值例子均到位。

### 第22章：评测方法论（ch22-evaluation-methodology）
- 图源标注缺失：`fig2-goodhart-cycle.png`、`fig1-evaluation-timeline.png` 缺少 figure-caption 与来源说明；需补充来源或明确“作者绘制”。
- 技术规范：行内公式含 `>`/`<`（如 $c < r$、$\theta_i > 0$）应改为块级公式或 `\lt/\gt`。
- 其他：算法框与数值例子齐全。

### 第23章：Instruction Tuning（ch23-instruction-tuning）
- 技术规范：行内公式含 `<`（如 $x_{<t}$、$y_{<t}$）应改为块级公式或 `\lt`。
- 其他：参考来源、配图、算法框、数值例子均到位。

---

## 章节之间的问题（结构与内容层）
- 算法框缺失：ch16、ch17 未提供论文算法框。
- 图源标注不一致：ch22 有 2 张图缺少 figure-caption 来源标注。
- 图像存放规范：ch18 多张论文图未放入 `original/` 子目录。
- 公式规范风险：ch16/ch17/ch21/ch22/ch23 存在行内 `<`/`>`，需改写以避免 Markdown/HTML 冲突。
- 开放资源复用偏弱：部分章节虽在参考来源中列出教材/课程，但正文中缺少明确图示或框架引用。

---

## 可从论文/教材/公开课补充的精华（按章节）

### ch16 GPT vs BERT
- 论文：补一个 T5/BART/UniLM 的“流程型算法框”（mask 构造或文本到文本训练流程）。
- 教材/课程：引入 D2L 11.9/15.8 的架构对比图或 CS224N 的“encoder/decoder taxonomy”示意图，强化教学可视化。

### ch17 Scaling Laws
- 论文：补一个“compute-optimal 分配/拟合流程”伪代码（Kaplan/Chinchilla 的可执行步骤）。
- 课程：补一张公开课的 scaling law 总结图，强化方法论概括。

### ch18 训练稳定性
- 论文：将论文原图移动到 `original/` 目录，保持图源管理一致性。
- 教材：可补一张 D2L 优化器/学习率调度图，以统一教材风格。

### ch19 分布式训练
- 课程：可补一张 CS224N/CMU 的并行训练总览图作为“宏观地图”。

### ch20 GPT-3 ICL
- 课程：可补一张公开课对 ICL vs 微调的对比图，帮助读者建立“范式迁移”直觉。

### ch21 Emergence & CoT
- 论文：如补充 CoT 或 ToT 原文示意图，可进一步提升“方法谱系”的可视化效果。

### ch22 评测方法论
- 教材/课程：可引入 HELM/MT-Bench 的评测流程图（或 Stanford 课程中的评测框架图），丰富“方法论图谱”。

### ch23 Instruction Tuning
- 论文：可补一张 FLAN/InstructGPT 数据混合或训练配方的流程图，强化“数据-目标-行为”链条。

---

## 结论性提示（优先级）
1. **补齐算法框**：ch16/ch17 必须补论文算法或明确改编的伪代码框。
2. **补齐图源标注**：ch22 两张图需补 figure-caption（或标注作者绘制）。
3. **修复行内公式规范**：ch16/ch17/ch21/ch22/ch23 行内含 `<`/`>` 的公式改为块级或 `\lt/\gt`。
4. **统一论文图像管理**：ch18 论文原图移入 `figures/chapter-18/original/`。
5. **增强开放资源复用**：在若干章节中引入 D2L/SLP3/CS224N 的图示或讲解结构，提升教学一致性。
