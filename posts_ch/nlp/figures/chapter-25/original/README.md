# Chapter 25 Figures - 对齐技术的演进

## ✅ 已提取的论文原图

### 1. fig1-dpo-vs-rlhf.png
**来源**: Rafailov et al. (2023) "Direct Preference Optimization", Figure 1
**arXiv**: https://arxiv.org/abs/2305.18290
**提取方式**: arXiv HTML 版本直接下载
**内容**: DPO 与 RLHF 的核心区别对比图
- 左侧：RLHF 需要 preference data → reward model → RL → LM policy
- 右侧：DPO 只需要 preference data → maximum likelihood → final LM

### 2. fig2a-dpo-frontier.png
**来源**: Rafailov et al. (2023), Figure 2 (左)
**内容**: Expected reward vs KL divergence 的前沿曲线

### 3. fig2b-dpo-tldr.png
**来源**: Rafailov et al. (2023), Figure 2 (右)
**内容**: TL;DR 摘要任务的 win rate 对比

### 4. fig3-constitutional-ai-pipeline.png
**来源**: Bai et al. (2022) "Constitutional AI: Harmlessness from AI Feedback", Figure 1
**arXiv**: https://arxiv.org/abs/2212.08073
**提取方式**: 从 PDF 渲染页面后裁剪
**内容**: Constitutional AI 的两阶段流程
- SL 阶段：Helpful RLHF Model → Generate Responses + Critique → Finetuned SL-CAI Model
- RL 阶段：Constitutional AI Feedback → RLAIF Training → Final RL-CAI Model

## 图片使用说明

所有图片已添加白色背景和适当 padding，适配暗色模式显示。

在 Quarto 中引用格式：
```markdown
![图片描述](figures/chapter-25/original/fig1-dpo-vs-rlhf.png){#fig-id width=95%}

::: {.figure-caption}
*Source: 作者 et al. (年份) "论文标题", Figure X*
:::
```

## 提取日期
2026-01-28
