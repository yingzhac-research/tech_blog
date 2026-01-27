# NLP教材章节重构方案

> **目的**：基于对经典NLP教材（SLP3, D2L, UDL, DLB, PML, LBDL, DL4NLP）和名校课程（Stanford CS224N, CMU 11-711, Princeton COS 484, JHU 601.465, UW CSE 517, ETH NLP）的系统对比，提出章节重构方案，填补关键缺口。
>
> **原则**：改动最小化，收益最大化——用最少的结构变动解决最重要的内容缺口。
>
> **日期**：2026-01-27
>
> **状态**：讨论中，待确认

---

## 一、改动总览

| 操作 | 具体内容 | 净效果 |
|------|---------|--------|
| **合并** | Ch5 + Ch6 → 一章「注意力的诞生与演进」 | -1 章 |
| **新增** | NLP核心任务全景（Part 1，Ch1之后） | +1 章 |
| **新增** | 超越Dense Transformer：SSM/Mamba + MoE（Part 5） | +1 章 |
| **扩充** | Ch12（GPT）增加解码策略 section | +0 章 |
| **总计** | 34 → **35 章** | +1 章 |

---

## 二、改动详情

### 改动①：合并 Ch5 + Ch6 → 新 Ch5「注意力机制的诞生与演进」

#### 理由

Bahdanau (2014) 和 Luong (2015) attention 本质上是同一个故事的两个阶段——"如何计算 attention score"。对比经典资源的处理方式：

- **SLP3**：1章覆盖 Attention + Transformer
- **D2L**：Bahdanau 和 attention scoring 在同一章（Ch 11.4）
- **CS224N**：1个 lecture 覆盖完整 attention 演进
- **UDL**：1章（Ch 12 Transformers）

从研究视角看，Bahdanau vs Luong 的区别（加性 vs 乘性、global vs local）不足以支撑独立两章。合并后叙事更紧凑。

#### 合并后结构

```
Ch5 注意力机制的诞生与演进

5.1 核心洞察：不同位置的重要性不同
5.2 Bahdanau Attention (2014)：加性注意力
    - 动机：Seq2Seq的信息瓶颈
    - Alignment model的设计
    - 注意力权重的可解释性
5.3 Luong Attention (2015)：乘性注意力
    - Dot-product vs General vs Concat
    - 洞察：计算效率与表达能力的权衡
5.4 注意力变体的谱系
    - Local vs Global Attention
    - Hard vs Soft Attention
    - 可微分性的重要性
5.5 注意力可视化：模型在"看"什么？
5.6 痛点：注意力仍然依附于RNN，能否独立？
5.7 工程实践：带Attention的Seq2Seq翻译
```

#### 参考资源

| 资源 | 具体章节/Lecture | 参考用途 |
|------|-----------------|---------|
| **D2L** Ch 11.4 | Bahdanau Attention | 架构图（`seq2seq-details-attention.svg`） |
| **D2L** Ch 11.3 | Attention Scoring Functions | Dot-product vs Additive 的数学对比 |
| **SLP3** Ch 10.4 | Attention | 简洁的综述性覆盖 |
| **CS224N** L7 (2024) | Machine Translation, Attention | Attention 演进的 slides |
| **UDL** Ch 12 | Transformers | Attention 机制的可视化图解 |

#### 实施细节

- 原 `ch05-attention-mechanism.qmd` 和 `ch06-attention-variants.qmd` 合并为新的 `ch06-attention-mechanism.qmd`（因新编号）
- 保留原 Ch5 的核心内容作为主体
- 原 Ch6 的 Luong attention 和变体内容压缩后并入
- 原 Ch6 的"痛点：注意力仍依附于RNN"作为新章节的结尾，衔接 Self-Attention 章

---

### 改动②：新增「NLP核心任务全景」

#### 理由

这是与经典教材对比后**最显著的缺口**。当前大纲是 model-centered 的（每章一个模型/技术），但几乎完全跳过了 NLP 领域的核心任务。

问题的严重性：
- 研究者需要知道模型在解决什么问题
- 后续章节频繁提到 "在MT任务上"、"NER性能"，但读者无处查阅这些任务的定义
- SLP3 整本书以任务为组织单元，CS224N 有专门的 QA、Coreference、Parsing lectures

**设计决策**：不走 SLP3 的路线（每个任务独立成章），而是用一章提供**全景地图**，保持 model-centered 主线不变。

#### 建议位置

**Part 1（前深度学习时代），Ch1之后，作为新 Ch2。**

理由：
1. 这些任务大多在深度学习之前就被定义
2. 为后续所有模型章节提供"模型到底在解决什么问题"的锚点
3. 读者先看到问题全景，再看模型演进，理解更深
4. 逻辑顺序：Ch1（历史背景）→ Ch2（问题全景）→ Ch3（表示学习开始解题）

#### 建议章节结构

```
Ch2 NLP核心任务全景——模型要解决什么问题？

> 本章不深入技术细节，而是提供一张"任务地图"。
> 后续章节每讲一个模型，你都能在这张地图上找到它解决的问题。

2.1 为什么需要一张任务地图？
    - NLP的多样性：同样是"处理语言"，任务千差万别
    - 任务定义决定了模型设计

2.2 序列标注任务
    - 词性标注 (POS Tagging)：给每个词分配语法角色
    - 命名实体识别 (NER)：识别人名、地名、组织名
    - 评测：Token-level F1, Span-level F1
    - 代表性 benchmark：CoNLL-2003, OntoNotes

2.3 句法分析
    - 依存句法分析 (Dependency Parsing)：词与词的依存关系
    - 成分句法分析 (Constituency Parsing)：短语结构树
    - 评测：UAS/LAS, Parseval
    - 为什么parsing对理解语言结构很重要？

2.4 文本分类
    - 情感分析 (Sentiment Analysis)：正面/负面/中性
    - 自然语言推理 (NLI)：蕴含/矛盾/中立
    - 主题分类
    - 评测：Accuracy, F1
    - 代表性 benchmark：SST, MNLI, SNLI

2.5 序列到序列任务
    - 机器翻译 (Machine Translation)
      - NLP历史上最重要的应用之一
      - 注意力机制和Transformer都诞生于MT
      - 评测：BLEU, COMET
      - 代表性 benchmark：WMT
    - 文本摘要 (Summarization)
      - 抽取式 vs 生成式
      - 评测：ROUGE
      - 代表性 benchmark：CNN/DailyMail, XSum

2.6 信息获取任务
    - 问答系统 (Question Answering)
      - 抽取式QA：从文档中找答案
      - 生成式QA：自由生成答案
      - 评测：EM, F1
      - 代表性 benchmark：SQuAD, Natural Questions
    - 信息抽取 (Information Extraction)
      - 关系抽取、事件抽取
    - 共指消解 (Coreference Resolution)

2.7 生成任务
    - 对话系统
    - 故事/文本生成
    - 代码生成
    - 评测的困难：生成质量难以自动量化

2.8 从任务专用到通用模型：一条演进主线
    - 痛点：每个任务都需要专门的模型和特征工程
    - 预告：深度学习如何逐步走向"一个模型解所有任务"
    - 全书路线图：Ch3-9（模型演进）→ Ch10-17（预训练统一）→ Ch18+（LLM时代）

2.9 任务-模型-评测 速查表
    [贯穿全书的参考表格]
```

#### 参考资源

| 资源 | 具体章节/Lecture | 参考用途 |
|------|-----------------|---------|
| **SLP3** Ch 8 | Sequence Labeling (POS, NER) | NER/POS的经典定义和评测方法 |
| **SLP3** Ch 14 | Dependency Parsing | 依存句法分析的形式化定义 |
| **SLP3** Ch 13 | Machine Translation | MT任务的完整覆盖 |
| **SLP3** Ch 14 | QA and Information Extraction | QA任务的formulation |
| **SLP3** Ch 4-5 | Text Classification (Naive Bayes, Logistic Regression) | 文本分类任务定义 |
| **SLP3** Ch 25 | Coreference Resolution | 共指消解的定义 |
| **CS224N** L1-2 (2024/2025) | Introduction & Word Vectors | NLP任务全景概述 |
| **CS224N** L6 (2024) | Dependency Parsing | Parsing 的讲解和可视化 |
| **CS224N** L15-16 (2024) | QA, Coreference | 高级NLP任务 |
| **CMU ANLP** L1-2 | Introduction to NLP | NLP任务分类框架 |
| **Princeton COS 484** L1-3 | NLP Basics | 任务概述 slides |
| **D2L** Ch 16 | NLP Applications | 情感分析、NLI 的实例 |
| **JHU 601.465** Syllabus | 整体 | 形式化任务定义（特别是结构预测） |

#### 写作要点

- **不要变成SLP3**：每个任务只需1-2段介绍 + formulation + 关键benchmark，不需要深入方法论
- **强调"痛点"叙事**：每个任务都点出 pre-DL 时代的解法痛点，为后续章节铺垫
- **提供全书交叉索引**：每个任务注明"本书哪些章节的模型会解决这个任务"
- **任务速查表**：做一个大表格，方便读者后续随时查阅

---

### 改动③：新增「超越Dense Transformer」

#### 理由

SSM/Mamba 和 MoE 是2024-2025年改变NLP架构格局的两个最大变量：

- **MoE**：GPT-4（推测）、Mixtral、DeepSeek-V2/V3、Qwen-MoE 的核心架构。不讲MoE就无法理解当代主流大模型的设计。
- **SSM/Mamba**：挑战了 "Attention is All You Need" 的基本假设。Mamba 在多个任务上达到 Transformer 级别性能，但推理复杂度为 O(n) 而非 O(n²)。

对比经典资源：
- **CMU ANLP (2024-2025)**：已经覆盖 MoE 和 efficiency
- **D2L**：开始更新 SSM 相关内容
- **SLP3**：2024-2026 更新中逐步加入
- 其他教材：尚未覆盖（这是你的教材的前沿优势）

#### 建议位置

**Part 5（大语言模型时代），在原 Ch27（开源大模型）之前。**

理由：
- 原 Ch27 会讲到 Mixtral、DeepSeek-V2——读者需要先理解 MoE 和 SSM
- 先讲架构创新，再讲开源模型如何采用，是"先原理后实例"的教学顺序
- 与 Ch9（高效注意力）形成呼应：Ch9 是在 attention 框架内优化，本章是跳出 attention 框架

#### 建议章节结构

```
Ch28 超越Dense Transformer——架构创新的新方向

> 演进脉络：Dense Transformer遇到两个根本挑战——
> (1) 所有参数对每个token都激活，计算浪费 → MoE
> (2) O(n²)注意力是序列建模的唯一选择吗？ → SSM

一、Mixture of Experts (MoE)：稀疏激活的智慧

28.1 核心洞察：不是每个token都需要激活所有参数
    - Dense model的浪费：一个关于烹饪的token需要激活"数学知识"的参数吗？
    - 痛点：模型越大，推理成本线性增长

28.2 MoE的基本架构
    - Expert层替代FFN层
    - Gate/Router：如何决定token去哪个expert？
    - Top-k routing策略

28.3 MoE的演进
    - 早期探索：Jacobs et al. (1991)，Shazeer et al. (2017)
    - GShard (2020)：大规模MoE的工程化
    - Switch Transformer (2021)：Top-1 routing的简化
    - ST-MoE (2022)：稳定训练的最佳实践

28.4 现代MoE里程碑
    - Mixtral 8x7B (2023)：开源MoE的标杆
      - 8个expert，每次激活2个
      - 46.7B总参数，12.9B激活参数
    - DeepSeek-V2/V3 (2024)：MoE工程的极致
      - DeepSeekMoE的细粒度expert设计
      - 共享expert + 路由expert的混合策略

28.5 MoE的核心挑战
    - 负载均衡 (Load Balancing)：如何避免所有token涌向同一个expert？
    - 路由崩塌 (Routing Collapse)：expert利用率过低
    - 训练不稳定性
    - 工程挑战：expert分布在不同GPU上的通信开销

28.6 理论分析：MoE的scaling特性
    - MoE的scaling law与dense model有何不同？
    - 参数量 vs 激活参数量 vs 计算量的解耦

二、State Space Models (SSM)：序列建模的另一条路

28.7 核心洞察：序列建模不一定需要attention
    - 回顾：RNN → Attention → Transformer 的演进
    - 反思：我们是否过早抛弃了recurrence？

28.8 从线性系统到S4
    - 连续时间状态空间模型的数学框架
      - dx/dt = Ax + Bu, y = Cx + Du
    - 离散化：从连续到离散的转换
    - S4 (2021)：HiPPO初始化 + 结构化矩阵
    - S4的突破：长程依赖建模能力

28.9 Mamba：选择性状态空间
    - 痛点：S4的参数是时间不变的（time-invariant），无法根据输入内容调整
    - 关键创新：选择性机制（Selection Mechanism）
      - 让 B, C, Δ 参数依赖于输入
      - 实现了"内容感知"的序列建模
    - 硬件感知的实现
      - Scan算法的并行化
      - 避免了材料化完整状态矩阵
    - 性能：在语言建模上匹配同规模Transformer

28.10 Mamba-2与理论进展
    - 状态空间对偶性 (State Space Duality)
    - SSM与线性注意力的理论联系
    - 为什么这个联系重要？

28.11 混合架构的兴起
    - Jamba (AI21, 2024)：Mamba + Transformer + MoE
    - 为什么混合架构可能是最优解？
    - 不同层使用不同机制的设计理念

三、展望

28.12 Dense Transformer不再是唯一选择
    - 开放问题：什么任务适合什么架构？
    - Attention擅长什么？SSM擅长什么？MoE解决什么问题？
    - 趋势：从单一架构走向混合架构

28.13 工程实践：Mixtral/Mamba模型的使用与部署
```

#### 参考资源

**MoE 部分：**

| 资源 | 具体内容 | 参考用途 |
|------|---------|---------|
| **论文：Shazeer et al. (2017)** | "Outrageously Large Neural Networks" | MoE在DL中的奠基论文 |
| **论文：Fedus et al. (2021)** | "Switch Transformers" | Top-1 routing, scaling analysis |
| **论文：Jiang et al. (2024)** | "Mixtral of Experts" | 开源MoE架构设计 |
| **论文：DeepSeek-AI (2024)** | "DeepSeek-V2" | 细粒度MoE设计 |
| **论文：DeepSeek-AI (2025)** | "DeepSeek-V3" | MoE训练工程 |
| **CMU ANLP (2024)** | Efficiency lectures | MoE的教学覆盖 |
| **CS224N (2025)** | LLM Architecture lectures | 架构设计的 slides |
| **D2L** 待更新章节 | MoE section | 可复用的架构图 |

**SSM/Mamba 部分：**

| 资源 | 具体内容 | 参考用途 |
|------|---------|---------|
| **论文：Gu et al. (2021)** | "Efficiently Modeling Long Sequences with Structured State Spaces" (S4) | SSM奠基论文 |
| **论文：Gu & Dao (2023)** | "Mamba: Linear-Time Sequence Modeling with Selective State Spaces" | Mamba核心论文 |
| **论文：Dao & Gu (2024)** | "Transformers are SSMs" (Mamba-2) | SSM-Attention对偶性 |
| **论文：Lieber et al. (2024)** | "Jamba" | 混合架构 |
| **博客：Albert Gu** | S4/Mamba系列博客 | 直觉解释 |
| **Stanford CS224N (2025)** | 可能已包含SSM内容 | 教学slides |

**架构对比：**

| 资源 | 具体内容 | 参考用途 |
|------|---------|---------|
| **论文：Poli et al. (2023)** | "Hyena Hierarchy" | Attention替代方案的另一尝试 |
| **论文：Arora et al. (2024)** | Various SSM vs Transformer benchmarks | 性能对比数据 |
| **UDL** Ch 12 | Transformers | 标准Transformer架构图（用于对比） |

#### 写作要点

- **保持"痛点驱动"叙事**：MoE回应"dense scaling太浪费"，SSM回应"O(n²)是否必要"
- **数学推导精简**：SSM的连续/离散化数学可以给出完整推导，但不要让公式淹没直觉
- **工程视角**：MoE的通信开销、Mamba的硬件实现——这是你的教材的差异化优势
- **与全书的连接**：
  - 回顾 Ch9（高效注意力）的稀疏/线性注意力尝试——SSM是更彻底的"去attention"方案
  - 回顾 Ch17（Scaling Laws）——MoE改变了scaling的方式
  - 为 Ch29（开源大模型，原Ch27）铺垫——Mixtral、DeepSeek都用了这些技术

---

### 改动④：Ch12（GPT）扩充解码策略 Section

#### 理由

当前大纲从未系统讲过模型如何从概率分布中生成文本。这是理解自回归模型的基础知识：

- Ch12 讲GPT和因果语言建模（Causal LM），但没讲"拿到概率后怎么生成"
- Ch20 讲ICL，Ch21 讲CoT——都预设读者理解了解码过程
- 所有经典资源都有覆盖：SLP3、D2L、CS224N

不需要独立成章，因为解码策略自然属于"自回归生成"话题，嵌入GPT章节最合理。

#### 建议新增内容

```
在 Ch12（GPT，新编号 Ch13）中增加：

12.X 从概率分布到文本：解码策略

12.X.1 问题定义：自回归生成的每一步都是一个选择
    - p(x_t | x_1, ..., x_{t-1}) 给出了概率分布
    - 如何从这个分布中选择下一个token？

12.X.2 确定性方法
    - Greedy decoding：每步选概率最高的token
      - 简单但容易产生重复、退化文本
    - Beam search：保留top-k个候选序列
      - 机器翻译时代的标配
      - 痛点：为什么beam search在LLM时代被抛弃？
        - 倾向于产生"安全但无聊"的输出
        - 与人类写作的概率分布不匹配

12.X.3 随机采样方法
    - Temperature scaling：控制概率分布的"尖锐度"
      - T < 1：更确定（更保守）
      - T > 1：更随机（更创造性）
      - 数学：softmax(z_i / T)
    - Top-k sampling (Fan et al., 2018)
      - 只从概率最高的k个token中采样
      - 痛点：k的选择是fixed的，但不同context需要不同的"多样性"
    - Nucleus / Top-p sampling (Holtzman et al., 2020)
      - 动态选择最小的token集合，使累积概率 ≥ p
      - 洞察：自适应的多样性控制
      - 为什么top-p在LLM时代成为默认选择？

12.X.4 退化问题与应对
    - Repetition问题：模型陷入循环
    - Repetition penalty / Frequency penalty
    - 长度控制

12.X.5 洞察：解码策略 = 质量-多样性的权衡
    - 没有"最优"解码策略，取决于应用场景
    - 翻译/摘要偏向确定性，创意写作偏向随机性
```

#### 参考资源

| 资源 | 具体章节/Lecture | 参考用途 |
|------|-----------------|---------|
| **SLP3** Ch 10.3 | Decoding: Greedy, Beam Search | Beam search的完整讲解 |
| **SLP3** Ch 10.7 | Sampling methods | Top-k, Top-p的覆盖 |
| **D2L** Ch 10.8 | Beam Search | Beam search的图解和代码 |
| **论文：Holtzman et al. (2020)** | "The Curious Case of Neural Text Degeneration" | Nucleus sampling的原始论文，退化问题分析 |
| **论文：Fan et al. (2018)** | "Hierarchical Neural Story Generation" | Top-k sampling |
| **CS224N** L10-11 (2024) | NLG / LLMs | 解码策略的slides |
| **CMU ANLP** Generation lecture | Decoding methods | 教学覆盖 |

#### 写作要点

- **嵌入而非独立**：作为Ch12的一个section，不破坏章节结构
- **痛点驱动**：从"greedy太无聊" → "beam search也不够好" → "采样方法" → "top-p为什么胜出"
- **直觉优先**：temperature的"尖锐度"比喻，top-p的"自适应"直觉
- **与后续章节的连接**：Ch21（CoT）的效果部分依赖于解码策略的选择

---

## 三、重编号方案

### 完整的 Before → After 章节对照表

| 原编号 | 原标题 | → | 新编号 | 变化说明 |
|--------|--------|---|--------|---------|
| **Part 0：导论** | | | | |
| Ch0 | 如何阅读NLP研究 | → | Ch0 | 不变 |
| **Part 1：前深度学习时代** | | | | **(3→4章)** |
| Ch1 | 语言理解的早期探索 | → | Ch1 | 不变 |
| — | — | → | **Ch2** | **🆕 NLP核心任务全景** |
| Ch2 | 表示学习的觉醒 | → | Ch3 | 仅重编号 |
| Ch3 | Tokenization与数据基础 | → | Ch4 | 仅重编号 |
| **Part 2：序列建模** | | | | |
| Ch4 | 循环神经网络时代 | → | Ch5 | 仅重编号 |
| **Part 3：注意力机制** | | | | **(5→4章)** |
| Ch5+Ch6 | 注意力诞生 + 变体 | → | **Ch6** | **🔀 合并** |
| Ch7 | Self-Attention的突破 | → | Ch7 | 仅重编号 |
| Ch8 | Transformer | → | Ch8 | 仅重编号 |
| Ch9 | 高效注意力 | → | Ch9 | 仅重编号 |
| **Part 4：预训练范式** | | | | |
| Ch10 | 预训练思想的起源 | → | Ch10 | 仅重编号 |
| Ch11 | ELMo | → | Ch11 | 仅重编号 |
| Ch12 | GPT | → | Ch12 | **📝 扩充解码策略section** |
| Ch13 | BERT | → | Ch13 | 仅重编号 |
| Ch14 | 预训练目标的演进 | → | Ch14 | 仅重编号 |
| Ch15 | 预训练模型的工程优化 | → | Ch15 | 仅重编号 |
| Ch16 | GPT vs BERT | → | Ch16 | 仅重编号 |
| **Part 5：大语言模型时代** | | | | **(13→14章)** |
| Ch17 | Scaling Laws | → | Ch17 | 仅重编号 |
| Ch18 | 训练稳定性 | → | Ch18 | ✅已写 |
| Ch19 | 分布式训练 | → | Ch19 | 待写 |
| Ch20 | GPT-3与ICL | → | Ch20 | 待写 |
| Ch21 | 涌现能力与CoT | → | Ch21 | 待写 |
| Ch22 | 评测方法论 | → | Ch22 | 待写 |
| Ch23 | 指令微调 | → | Ch23 | 待写 |
| Ch24 | RLHF | → | Ch24 | 待写 |
| Ch25 | 对齐技术 | → | Ch25 | 待写 |
| Ch26 | 长上下文与高效推理 | → | Ch26 | 待写 |
| — | — | → | **Ch27** | **🆕 超越Dense Transformer** |
| Ch27 | 开源大模型 | → | Ch28 | 待写 |
| Ch28 | 高效微调 | → | Ch29 | 待写 |
| Ch29 | 推理优化 | → | Ch30 | 待写 |
| **Part 6：应用与前沿** | | | | |
| Ch30 | RAG | → | Ch31 | 待写 |
| Ch31 | LLM作为Agent | → | Ch32 | 待写 |
| Ch32 | 多模态大模型 | → | Ch33 | 待写 |
| Ch33 | 研究前沿地图 | → | Ch34 | 待写 |

### 编号变化分析

**巧合**：由于 Part 1 新增1章 (+1) 与 Part 3 合并1章 (-1) 恰好抵消，**Ch7 以后的所有章节编号不变**（直到 Part 5 新增章节之后）。

具体影响：

| 受影响范围 | 文件数 | 操作 |
|-----------|--------|------|
| Ch0, Ch1 | 2 | 不变 |
| 新 Ch2 (任务全景) | 1 | 新建 |
| 原 Ch2 → Ch3, 原 Ch3 → Ch4 | 2 | 重命名 + 内部引用更新 |
| 原 Ch4 → Ch5 | 1 | 重命名 |
| 原 Ch5+Ch6 → 新 Ch6 | 2→1 | 合并改写 |
| 原 Ch7-Ch18 → Ch7-Ch18 | 12 | **编号不变！** |
| 原 Ch12 (GPT) | 1 | 扩充内容（编号不变） |
| Ch19-Ch26 (未写) | 8 | 编号不变 |
| 新 Ch27 (SSM+MoE) | 1 | 新建 |
| 原 Ch27-Ch33 → Ch28-Ch34 | 7 | 编号+1（但均未写，无文件需改） |

**实际需要动的已有文件**：
1. `ch02-representation-learning.qmd` → `ch03-representation-learning.qmd`
2. `ch03-tokenization.qmd` → `ch04-tokenization.qmd`
3. `ch04-rnn-lstm.qmd` → `ch05-rnn-lstm.qmd`
4. `ch05-attention-mechanism.qmd` + `ch06-attention-variants.qmd` → `ch06-attention-mechanism.qmd`（合并）
5. `ch12-gpt.qmd` → 内容扩充（文件名不变）

**无需改动的已有文件**：ch00, ch01, ch07-ch11, ch13-ch18（共14个文件不动）

---

## 四、待讨论的开放问题

### 问题1：NLP任务全景章是否放在Part 1？

| 方案 | 位置 | 优点 | 缺点 |
|------|------|------|------|
| **A（推荐）** | Part 1，Ch1之后 | 先看问题再看方法；编号抵消巧妙 | 需重命名 ch02-ch04 三个文件 |
| B | Part 1 末尾，原Ch3之后 | 不打断Ch1→Ch2的连贯性 | 在Tokenization之后讲任务全景，顺序不太自然 |
| C | 作为Ch1的扩展section | 零重编号 | Ch1内容膨胀，失去独立性 |

### 问题2：MoE和SSM合一章 vs 各自独立？

| 方案 | 优点 | 缺点 |
|------|------|------|
| **合一章（推荐）** | 共享叙事主题（"超越dense Transformer"），对比更清晰，现代模型本身在混合使用 | 内容可能偏多（预计15000-20000字） |
| 各自独立两章 | 每个话题讲得更深 | 总章数增至36；叙事分散 |

### 问题3：是否需要增加多语言NLP内容？

当前大纲几乎不涉及多语言NLP（mBERT, XLM-R, cross-lingual transfer）。CS224N有专门的multilinguality lecture。这个缺口的优先级低于上述四项改动，但值得考虑是否在Ch28（开源大模型）中增加相关section。

### 问题4：outline.md 是否同步更新？

本方案确认后，需要同步更新：
- `.claude/skills/nlp-textbook-chapter/references/outline.md`（主大纲）
- `nlp-textbook-outline.md`（根目录副本，如有）

---

## 五、实施优先级

| 顺序 | 改动 | 依赖 | 说明 |
|------|------|------|------|
| 1 | 确认方案 | 无 | 本文档的讨论 |
| 2 | 更新 outline.md | 方案确认 | 同步大纲文件 |
| 3 | 文件重命名 | 大纲更新 | ch02→ch03, ch03→ch04, ch04→ch05 |
| 4 | 合并 Ch5+Ch6 | 重命名完成 | 内容改写 |
| 5 | 扩充 Ch12 解码策略 | 无依赖 | 可与其他步骤并行 |
| 6 | 写作新 Ch2（任务全景） | 重命名完成 | 全新章节 |
| 7 | 写作新 Ch27（SSM+MoE） | 无依赖 | 全新章节，可后期写 |

---

---

## 六、执行任务拆分（4个窗口）

### 已写章节确认

```
已完成：ch00, ch01, ch02, ch03, ch04, ch05, ch06, ch07, ch08, ch09,
        ch10, ch11, ch12, ch13, ch14, ch15, ch16, ch17, ch18
共 19 个文件（ch00-ch18）
```

### 依赖关系图

```
  Window 1 (结构调整)
    │
    ├──→ Window 3 (写 Ch2 任务全景)
    │      ↑ 必须等 W1 完成（文件结构就绪）
    │
    └──→ Window 4 (写 Ch27 SSM+MoE)
           ↑ 建议等 W1 完成（大纲已更新）

  Window 2 (扩充 Ch12 解码策略)
    ↑ 无依赖，可独立执行，甚至可与 W1 并行
```

### Window 1：结构调整（必须最先执行）

**目标**：完成文件重命名、章节合并、大纲更新。不写新内容。

**操作清单**：

1. 重命名已有文件（按逆序操作，避免覆盖）：
   - `ch04-rnn-lstm.qmd` → `ch05-rnn-lstm.qmd`
   - `ch03-tokenization.qmd` → `ch04-tokenization.qmd`
   - `ch02-representation-learning.qmd` → `ch03-representation-learning.qmd`
2. 合并 `ch05-attention-mechanism.qmd` + `ch06-attention-variants.qmd` → `ch06-attention-mechanism.qmd`
   - 按本文档"改动①"的结构重组内容
   - 删除原 ch05 和 ch06 两个文件
3. 扫描所有已有章节（ch00-ch18），更新内部交叉引用
   - 如"第2章"→"第3章"，"Ch4"→"Ch5"等
   - 特别注意 ch01 末尾对 ch02 的引用、ch07 开头对 ch06 的引用
4. 更新 `.claude/skills/nlp-textbook-chapter/references/outline.md`
   - 插入新 Ch2（NLP核心任务全景）的大纲
   - 合并 Ch5+Ch6 的大纲条目
   - 插入新 Ch27（超越Dense Transformer）的大纲
   - 更新章节分布统计表
5. 更新 `nlp-textbook-outline.md`（根目录副本，如果与 outline.md 内容一致）
6. 提交 git commit

**预估复杂度**：中等（主要是仔细的查找替换，不涉及大量新内容写作）

**Prompt**：

```
请阅读项目根目录的 nlp-textbook-restructure-plan.md（特别是"改动①"和"三、重编号方案"部分），执行以下操作：

1. 按逆序重命名文件（避免覆盖）：
   - posts_ch/nlp/ch04-rnn-lstm.qmd → ch05-rnn-lstm.qmd
   - posts_ch/nlp/ch03-tokenization.qmd → ch04-tokenization.qmd
   - posts_ch/nlp/ch02-representation-learning.qmd → ch03-representation-learning.qmd

2. 合并 ch05-attention-mechanism.qmd 和 ch06-attention-variants.qmd 为新的 ch06-attention-mechanism.qmd。
   按方案中"改动①"的合并结构重组内容，保留核心技术内容，压缩重复部分。合并完成后删除原两个文件。

3. 扫描 ch00-ch18 所有文件，更新章节交叉引用（"第2章"→"第3章"等）。

4. 更新 .claude/skills/nlp-textbook-chapter/references/outline.md：
   - 按方案插入新 Ch2（NLP核心任务全景）大纲占位
   - 合并原 Ch5+Ch6 的大纲条目
   - 插入新 Ch27（超越Dense Transformer）大纲占位
   - 更新章节统计

每步操作前先告诉我你要做什么，等我确认。完成后提交一个 git commit。
```

---

### Window 2：扩充 Ch12 解码策略（可与 W1 并行）

**目标**：在 ch12-gpt.qmd 中增加解码策略 section。

**为什么可以并行**：Ch12 的文件名和编号在重构中**不会改变**（+1/-1 在 ch06 处已抵消），所以不依赖 Window 1。

**操作清单**：

1. 阅读当前 ch12-gpt.qmd 的完整内容
2. 确定插入位置（建议在"因果语言建模"section 之后，"预训练+微调范式"之前）
3. 按本文档"改动④"的结构写作解码策略 section
4. 确保与前后 section 的衔接自然
5. 提交 git commit

**预估复杂度**：低-中（新增约 3000-5000 字，一个 section）

**Prompt**：

```
请阅读 nlp-textbook-restructure-plan.md 中"改动④：Ch12（GPT）扩充解码策略"部分，
然后阅读 posts_ch/nlp/ch12-gpt.qmd 的当前内容。

在 ch12 中增加一个解码策略 section，按方案中的结构：
- Greedy decoding
- Beam search（及其在LLM时代被抛弃的原因）
- Temperature scaling
- Top-k sampling
- Nucleus / Top-p sampling
- Repetition问题与penalty

参考资源：SLP3 Ch10.3 (Beam Search), Holtzman et al. 2020 (Nucleus Sampling)。

使用 nlp-textbook-chapter skill 的写作规范。先告诉我你计划插入的位置，等我确认后再写。
```

---

### Window 3：写作新 Ch2——NLP核心任务全景（依赖 W1 完成）

**目标**：创建全新的 ch02-nlp-task-landscape.qmd。

**为什么依赖 W1**：Window 1 会把原 ch02 重命名为 ch03，腾出 ch02 的位置。如果 W1 没做完就写 ch02，会产生文件冲突。

**操作清单**：

1. 阅读方案中"改动②"的详细结构和参考资源
2. 阅读 SLP3 相关章节（通过 web 获取目录结构）获取任务定义
3. 阅读 ch01（了解前一章的结尾衔接点）和 ch03（了解后一章的开头衔接点）
4. 使用 nlp-textbook-chapter skill 写作完整章节
5. 确保包含"任务-模型-评测速查表"（全书交叉参考表）
6. 提交 git commit

**预估复杂度**：高（全新章节，约 15000-20000 字）

**Prompt**：

```
请阅读 nlp-textbook-restructure-plan.md 中"改动②：新增 NLP核心任务全景"部分。

然后使用 /nlp-textbook-chapter skill 写作新的 Ch2。

关键要求：
- 这是一个"任务地图"章，不是每个任务的深入教程
- 每个任务需要：formulation（输入/输出）、评测指标、代表性benchmark、1-2段简介
- 需包含"任务-模型-评测速查表"，供读者后续查阅
- 结尾要衔接 Ch3（表示学习）——从"每个任务都需要专门的特征工程"这个痛点过渡

参考方案中列出的资源：SLP3 各任务章节、CS224N 相关Lecture、CMU ANLP。

先阅读 ch01 的结尾和 ch03（原ch02）的开头，确定衔接点。
然后给我一个章节大纲，等我确认后再写完整内容。

文件保存为 posts_ch/nlp/ch02-nlp-task-landscape.qmd
```

---

### Window 4：写作新 Ch27——超越Dense Transformer（建议等 W1 完成）

**目标**：创建全新的 ch27-beyond-dense-transformer.qmd。

**依赖关系**：技术上 ch27 是新文件且编号不受 W1 影响，但建议等 W1 完成（大纲已更新），这样 skill 和交叉引用都是正确的。可与 W3 并行。

**操作清单**：

1. 阅读方案中"改动③"的详细结构和参考资源
2. 阅读关键论文摘要（Mamba, Switch Transformer, Mixtral, DeepSeek-V2）
3. 阅读 ch09（高效注意力）和 ch17（Scaling Laws）了解衔接点
4. 使用 nlp-textbook-chapter skill 写作完整章节
5. 确保 MoE 和 SSM 两大部分都有"痛点驱动"叙事
6. 提交 git commit

**预估复杂度**：高（全新章节，技术深度大，约 15000-20000 字）

**Prompt**：

```
请阅读 nlp-textbook-restructure-plan.md 中"改动③：新增 超越Dense Transformer"部分。

然后使用 /nlp-textbook-chapter skill 写作新的 Ch27。

关键要求：
- 分两大部分：MoE（稀疏激活）和 SSM/Mamba（替代attention的序列建模）
- 保持痛点驱动叙事：MoE回应"dense scaling太浪费"，SSM回应"O(n²)是否必要"
- 最后一节讲混合架构（Jamba = Mamba + Transformer + MoE）
- 需要与 Ch9（高效注意力）和 Ch17（Scaling Laws）形成呼应

重点参考论文（方案中已列出）：
- MoE: Shazeer 2017, Switch Transformer 2021, Mixtral 2024, DeepSeek-V2/V3
- SSM: S4 (Gu 2021), Mamba (Gu & Dao 2023), Mamba-2 (Dao & Gu 2024)
- Hybrid: Jamba (Lieber 2024)

先给我一个详细大纲，等我确认后再写完整内容。

文件保存为 posts_ch/nlp/ch27-beyond-dense-transformer.qmd
```

---

### 执行时间线建议

```
Week 1:
  ┌─── Window 1 (结构调整) ────────────┐
  │  重命名 + 合并 + 更新大纲 + commit  │
  └────────────────────────────────────┘
  ┌─── Window 2 (Ch12 解码策略) ───┐     ← 可与 W1 同时进行
  │  扩充 section + commit          │
  └────────────────────────────────┘

Week 2:
  ┌─── Window 3 (Ch2 任务全景) ─────────┐
  │  全新章节写作 + commit               │
  └────────────────────────────────────┘
  ┌─── Window 4 (Ch27 SSM+MoE) ────────┐  ← 可与 W3 同时进行
  │  全新章节写作 + commit               │
  └────────────────────────────────────┘
```

---

*文档更新时间：2026-01-27*
*状态：讨论稿，待确认后实施*
