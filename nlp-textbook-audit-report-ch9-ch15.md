# NLP教材 ch9–ch15 审核报告（基于 .claude/skills）

## 依据的 skills
- nlp-textbook-chapter：章节结构、参考来源记录、配图/伪代码要求
- writing-style：直觉先于公式、散文式叙述、类比与数值例子
- technical-standards：YAML front matter、公式/Markdown/中英混排规范
- learner-profile：强调“为什么”、边界条件、批判性与开放问题
- paper-figure-extractor：论文配图提取与来源标注规范

## 检查范围
- posts_ch/nlp/ch09-efficient-attention.qmd
- posts_ch/nlp/ch10-pretraining-origins.qmd
- posts_ch/nlp/ch11-elmo.qmd
- posts_ch/nlp/ch12-gpt.qmd
- posts_ch/nlp/ch13-bert.qmd
- posts_ch/nlp/ch14-pretraining-objectives.qmd
- posts_ch/nlp/ch15-engineering-optimization.qmd

## 外部资料抽查（论文/教材/课程）
- 论文：Efficient Transformers survey、BigBird、ELMo、BERT、XLNet、T5、RoBERTa、ULMFiT、Word2Vec 等
- 教材：D2L（BERT 相关章节）、SLP3（预训练/上下文表征相关章节）
- 课程：Stanford CS224N（Pretraining/Contextual Embeddings 相关讲义）

> 注：ALBERT、DistilBERT、ELECTRA、SimCSE 的原文页面未能直接访问到（工具限制）。报告中的缺口与建议基于当前章节文本与模板要求给出，后续建议人工核对原文细节。

---

## 逐章问题

### 第9章：高效注意力（ch09-efficient-attention）
- 参考来源：缺少“本章参考来源”callout（论文/教材/课程清单未记录）。
- 配图来源：仅 Tay survey / BigBird 图有来源标注；`fig-complexity-comparison.png`、`fig-linear-attention-order.png`、`fig-attention-patterns.png` 无来源或“作者绘制”标注。
- 伪代码：无算法框（建议补 Longformer/Performer/Linformer 中至少一个核心算法流程）。
- 数值例子：缺少“可手算的完整数值演算示例”（可用线性注意力或稀疏掩码的小例子）。
- 技术规范：行内公式含 `>`（如 `\epsilon > 0`）应改为块级公式或 `\gt`。
- Front matter：`image: figures/efficient-attention-banner.png` 文件不存在。

### 第10章：预训练思想的起源（ch10-pretraining-origins）
- 参考来源：缺少“本章参考来源”callout（论文/教材/课程清单未记录）。
- 配图来源：所有图片无来源或“作者绘制”标注（时间线/迁移对比/静态 vs 上下文向量）。
- 伪代码：无算法框（建议补 ULMFiT 三阶段微调流程或 Word2Vec/负采样训练流程）。
- 数值例子：缺少核心算法的完整数值演算示例（现有数据成本表不够“算法级”）。
- Front matter：`image: figures/pretraining-origins-banner.png` 文件不存在。

### 第11章：ELMo（ch11-elmo）
- 配图：存在“待绘制：ELMo 架构图”占位，需补真实图或论文原图。
- Front matter：`image: figures/chapter-11/elmo-banner.png` 文件不存在。
- 其他：参考来源、算法框、数值例子整体满足要求。

### 第12章：GPT（ch12-gpt）
- 配图来源：`fig-causal-attention-mask.png` 无来源或“作者绘制”标注。
- 技术规范：行内公式含 `n < d` / `n > d`（`<`/`>` 冲突）应改为块级公式或 `\lt/\gt`。
- Front matter：`image: figures/chapter-12/gpt-banner.png` 文件不存在。
- 其他：参考来源、算法框、数值例子基本满足要求。

### 第13章：BERT（ch13-bert）
- 基本符合模板与技能要求；图片/算法/数值例子均到位。
- 可选优化：避免与上一章重复展示“ELMo/GPT/BERT 对比图”（建议保留一处，另一处用跨章引用）。

### 第14章：预训练目标演进（ch14-pretraining-objectives）
- 配图来源：T5/XLNet/ELECTRA/T5 mask 图均无 figure-caption 来源标注（目前仅插图）。
- 技术规范：行内公式含 `>`（相似度示例）需改为块级公式或 `\gt`。
- 其他：参考来源、算法框、数值例子基本满足要求。

### 第15章：工程优化（ch15-engineering-optimization）
- 数值例子：缺少“完整可手算”的核心算法示例（当前仅温度缩放示例，建议补蒸馏损失或参数共享的小例子）。
- 技术规范：行内公式含 `T > 1` 需改为块级公式或 `\gt`。
- 其他：参考来源、算法框、配图标注基本满足要求。

---

## 章节之间的问题（结构与内容层）
- 参考来源记录缺失：ch09/ch10 未按模板提供“本章参考来源”callout。
- 图源标注不一致：ch09/ch10/ch12/ch14 存在无来源图片，整体风格不统一。
- Front matter 图片缺失：ch09–ch12 的 `image` 文件不存在。
- 算法框缺失：ch09/ch10 无算法伪代码框。
- 数值例子不足：ch09/ch10/ch15 缺少“可手算的完整算法数值例子”。
- 公式规范风险：ch09/ch12/ch14/ch15 行内公式含 `>`/`<`。
- 内容重复：ELMo/GPT/BERT 对比图在 ch11 与 ch12 重复，可考虑跨章引用。

---

## 可从论文/教材/公开课补充的精华（按章节）

### ch09 高效注意力
- 论文：Tay et al. survey 的方法分类图、BigBird 的稀疏注意力示意图可作为主图；补图时明确标注来源。
- 课程：如需“高效注意力”的直觉图，可考虑 CS224N/CMU 的效率优化讲解 slides（需补来源）。

### ch10 预训练思想起源
- 论文：ULMFiT（ACL 2018）流程图/三阶段微调细节适合作算法框与图；Word2Vec 负采样流程适合作数值例子。
- 教材：D2L 对“上下文词向量 vs 静态词向量”的讲解结构可借鉴；SLP3 的 contextual embeddings 章节可补历史脉络。
- 课程：CS224N 的 Word Vectors / Pretraining 讲义适合作为教学顺序与图示参考。

### ch11 ELMo
- 论文：ELMo 原文图 1/2 用于替换“待绘制”占位图。

### ch12 GPT
- 论文/官方：OpenAI GPT 技术报告中的输入转换示意图与模型架构图需配完整来源说明；因果 mask 图若自绘需标注“作者绘制”。

### ch14 预训练目标演进
- 论文：XLNet（排列 LM）与 T5（Text-to-Text）原图建议加 figure-caption；ELECTRA 架构图补清晰来源标注。

### ch15 工程优化
- 论文：RoBERTa/ALBERT/DistilBERT 的训练策略与效率对比表可作为工程优化证据；补充蒸馏损失或参数共享的数值例子以满足“可手算示例”。

---

## 结论性提示（优先级）
1. **补齐“参考来源”callout**：ch09/ch10 必须补论文+教材+课程三类来源记录。
2. **补齐图源标注**：所有未标注来源的图片必须补来源或明确“作者绘制”。
3. **补齐算法框与数值例子**：ch09/ch10/ch15 按技能要求补齐。
4. **修复公式规范**：行内含 `>`/`<` 的公式改为块级或 `\gt/\lt`。
5. **修复 front matter 图片**：ch09–ch12 的 banner 文件补齐或更换路径。
