# NLP教材 ch1–ch8 审核报告（基于 .claude/skills）

## 依据的 skills
- nlp-textbook-chapter：章节结构、配图/伪代码规则、开放资源使用要求
- writing-style：直觉先于公式、散文式叙述、类比与数值例子
- technical-standards：YAML front matter、公式/Markdown/中英混排规范
- learner-profile：强调“为什么”、边界条件、批判性与开放问题

## 检查范围
- chapters：`posts_ch/nlp/ch01-early-explorations.qmd` … `posts_ch/nlp/ch08-transformer.qmd`

---

## 逐章问题

### 第1章：早期探索（ch01-early-explorations）
- 结构一致性：缺少模板中的“问题本质/核心思想/技术细节”主干段落，整体偏历史叙事，与后续章的模板结构不一致。
- 图片：全章无图，未满足“关键概念需配图”的要求；N-gram/HMM/CRF/传统Pipeline 等内容应配结构图或流程图。
- 伪代码：Viterbi Algorithm 有来源标注，符合要求。
- 开源资源：延伸阅读仅提到 SLP3，未利用 D2L/公开课 slides 的可视化资源。
- 技术规范：YAML 缺少 `tags` 与 `description`；表格/行内公式出现 `|`（如 `P(y_t | y_{t-1})`）应改为块级公式或 `\mid`。

### 第2章：表示学习（ch02-representation-learning）
- 图片：`fig3-cbow-vs-skipgram.png` 无来源标注，且 front matter `image` 也指向该图；需要注明“作者绘制”或替换为论文/D2L/课程图。FastText 图有来源标注 OK。
- 伪代码：SGNS 算法有来源，但为自写 Python；若非论文原算法，需标注“改编自”。
- 技术规范：多处行内公式含 `|`（如 `|\mathcal{V}|`、`P(w_o \| w_c)`），按规范应改为块级或使用 `\mid`。
- 写作风格：概念解释中使用较多列表，偏离“散文式”要求。
- 资源利用：延伸阅读仅 SLP3，无 CS224N/UDL 等公开课或开源教材的图示与讲解引用。

### 第3章：Tokenization（ch03-tokenization）
- 图片：正文无任何插图，仅 front matter `image`；但已有生成图（`fig-tokenization-strategies`、`fig-multilingual-efficiency`）未使用，违反“配图优先”。
- 图片来源：front matter 图未标注来源/“作者绘制”。
- 伪代码：BPE Algorithm 1 有来源标注，符合要求。
- 写作风格：大量条目式列举（策略、影响、清洗步骤等），偏离散文式要求。
- 资源利用：未引用公开教材/课程的图示或讲解（如 SLP3、CS224N 的 tokenization/LM 相关内容）。
- 技术规范：YAML 缺少 `tags` 与 `description`。

### 第4章：RNN/LSTM（ch04-rnn-lstm）
- 技术规范：行内公式含 `|`/`<`（如 `$|\lambda_{\max}| < 1$`、`O(d \log |\mathcal{V}|)`）应改为块级公式或使用 `\mid/\lt/\gt`。
- 资源利用：未使用 D2L/UDL/公开课图示（尽管这些资源对 RNN/LSTM 有高质量图）。
- 其他：YAML 缺少 `tags` 与 `description`。
- 图片与伪代码：均有来源标注，符合要求。

### 第5章：Attention 机制（ch05-attention-mechanism）
- 技术规范：行内公式含 `>`（如 `H(x) > O(d)`、`\alpha_{ij} > 0`）应改为块级公式或使用 `\gt`。
- 资源利用：已使用 D2L 图，但未使用公开课/其他教材图示。
- 其他：YAML 缺少 `tags` 与 `description`。

### 第6章：Attention 变体（ch06-attention-variants）
- 资源利用：未引用公开课程/教材图示（CS224N/CMU/Princeton 等）。
- 其他：YAML 缺少 `tags` 与 `description`。
- 图片与伪代码：已有论文来源标注，符合要求。

### 第7章：Self-Attention（ch07-self-attention）
- 伪代码：`Algorithm: Self-Attention` 无来源标注，且未注明“改编自”。应引用 Vaswani et al. (2017) 或相关论文/公开课算法描述。
- 重复风险：位置编码与自注意力公式在第8章再次详细出现，建议在本章完成核心推导，下一章仅引用。
- 资源利用：未使用 D2L/UDL/公开课图示。
- 其他：YAML 缺少 `tags` 与 `description`。

### 第8章：Transformer（ch08-transformer）
- 图片来源缺失：
  - `fig-rnn-seq2seq.png`、`fig-pre-post-norm.png`、`fig-cross-attention.png` 未标注来源（似为自绘）。
  - 两个 placeholder 图（Positional Encoding/Attention Visualization）未落地为真实图片，也未引用来源。
- 技术规范：行内公式含 `<`/`>`（如 mask 的条件）应改为块级公式或使用 `\lt/\gt`。
- 资源利用：未引用 D2L/UDL/公开课图示（尽管这些资源覆盖 Transformer 的核心结构）。
- 其他：YAML 缺少 `tags` 与 `description`。

---

## 章节之间的问题（结构与内容层）
- 模板一致性：ch01 未按“0–7”模板结构展开，导致全书结构不统一。
- 图/伪代码来源一致性：部分章严格标注来源，部分章无来源或 placeholder，风格不一致。
- 开源资源利用不足：除 SLP3、D2L（单章）外，公开教材/课程几乎未被系统引用，未满足“开放资源复用”要求。
- 重复内容：
  - Attention 的基本定义、Q/K/V 数学公式在 ch05/ch07/ch08 多次展开。
  - 位置编码在 ch07 与 ch08 重复深入讲解。
  - RNN/Seq2Seq 局限在 ch04 与 ch08 重复叙述。
- 写作风格：多章存在“列表密集、散文不足”的共性问题，违背写作风格要求。
- 技术规范：所有章节 YAML 缺少 `tags`/`description`，部分章存在行内公式符号冲突问题。

---

## 可从开源教材/公开课补充的精华（按章节）

### ch01 早期探索
- SLP3：N-gram/HMM/CRF 经典图示与讲解（可补结构图与示意流程）。
- CS224N 课程（基础 NLP 与语言模型相关 slides）可用于补充历史与范式演进图示。

### ch02 表示学习
- CS224N “Word Vectors” Slides：向量空间直觉、类比任务示意图。
- SLP3 词向量相关章节：补充权威背景与经典实验对比图。

### ch03 Tokenization
- SLP3（早期章节中的分词/预处理相关内容）：补充术语统一与语言差异图示。
- 公开课 slides（CS224N/CMU ANLP）中的 subword/Byte-level 示例图，可补 multilingual 与效率对比。

### ch04 RNN/LSTM
- D2L RNN/LSTM/Seq2Seq 图（D2L 10.x、10.7）可替换或补充架构图。
- UDL RNN 章节图示（结构更清晰、风格统一）。

### ch05 Attention 机制
- D2L 11.4 Attention 结构图已使用，可补 attention 可视化/对齐矩阵示意图。
- CS224N slides 中的 attention 直觉图可补“为什么 work”。

### ch06 Attention 变体
- Luong 论文已有图，但可补公开课 slides 中“global/local/hard/soft”对比图，提高教学可视化质量。

### ch07 Self-Attention
- D2L 11.5/11.6 的 self-attention/positional encoding 图（规范、可复用）。
- UDL Transformer 章节图示用于位置编码与几何直觉补充。

### ch08 Transformer
- D2L 11.7 Transformer 架构图与多头注意力图可统一风格。
- UDL/CS224N 的 Pre-Norm vs Post-Norm、训练稳定性图示可替换自绘图。
- 公开课 slides 可补充 attention pattern 可视化图，替换 placeholder。

---

## 结论性提示（优先级）
1. **补齐来源**：所有未标注来源的图片/伪代码必须补充来源或明确“作者绘制/改编自”。
2. **补齐图片**：ch01、ch03 需要新增关键图；ch08 placeholder 必须落地。
3. **统一技术规范**：所有章节补 `tags`/`description`；修正行内公式含 `|<>` 的渲染风险。
4. **削减重复**：注意力/位置编码/Seq2Seq 局限内容需跨章收敛，避免重复讲解。
5. **提升资源利用率**：系统引入 D2L/UDL/CS224N 等公开资源中的核心图和讲解。
