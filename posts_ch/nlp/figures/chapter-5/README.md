# 第4章 配图

## 已下载的论文/博客原图

| 文件 | 来源 | 描述 | 在文章中的位置 |
|------|------|------|----------------|
| `fig-rnn-unrolled-colah.png` | Colah's Blog | RNN展开图（时间维度） | RNN计算图与参数共享 |
| `fig-lstm-chain-colah.png` | Colah's Blog | **LSTM单元结构**（4层交互） | LSTM直觉部分 |
| `fig-lstm-cell-arxiv.png` | arXiv:1909.09586 | LSTM单元（CEC视角） | 备用 |
| `fig-simple-rnn-colah.png` | Colah's Blog | 简单RNN重复模块 | 备用 |
| `fig-gru-cell.png` | Cho et al. (2014) | **GRU单元结构** | GRU章节 |
| `fig-encoder-decoder.png` | Cho et al. (2014) | Encoder-Decoder架构 | Seq2Seq章节 |
| `fig-seq2seq.png` | Sutskever et al. (2014) | **Seq2Seq架构** (ABC→WXYZ) | Seq2Seq章节 |

## 图片来源详情

### Colah's Blog (2015)
- **标题**: Understanding LSTM Networks
- **URL**: https://colah.github.io/posts/2015-08-Understanding-LSTMs/
- **作者**: Christopher Olah
- **说明**: 最经典的LSTM可视化教程，图片清晰美观

### arXiv:1909.09586 (2019)
- **标题**: Understanding LSTM – a tutorial into Long Short-Term Memory
- **URL**: https://arxiv.org/abs/1909.09586
- **说明**: LSTM教程论文，包含原始CEC（Constant Error Carousel）视角的图

### Cho et al. (2014) - arXiv:1406.1078
- **标题**: Learning Phrase Representations using RNN Encoder-Decoder
- **URL**: https://arxiv.org/abs/1406.1078
- **内容**: GRU单元 (Figure 2) + Encoder-Decoder架构 (Figure 1)

### Sutskever et al. (2014) - arXiv:1409.3215
- **标题**: Sequence to Sequence Learning with Neural Networks
- **URL**: https://arxiv.org/abs/1409.3215
- **内容**: Seq2Seq架构 (Figure 1)

### Hochreiter & Schmidhuber (1997)
- **标题**: Long Short-Term Memory
- **出版**: Neural Computation 9(8):1735-1780
- **PDF**: https://www.bioinf.jku.at/publications/older/2604.pdf
- **说明**: LSTM原始论文，无arXiv版本

## 算法框

| 算法 | 来源 | 在文章中的位置 |
|------|------|----------------|
| LSTM Forward Pass | Hochreiter & Schmidhuber (1997) | LSTM数学形式化 |
| GRU Forward Pass | Cho et al. (2014) Eq. 5-8 | GRU数学形式化 |

## 文件结构

```
figures/chapter-4/
├── README.md
└── original/
    ├── fig-rnn-unrolled-colah.png    ← RNN展开
    ├── fig-lstm-chain-colah.png      ← LSTM结构（主图）
    ├── fig-lstm-cell-arxiv.png       ← LSTM单元（备用）
    ├── fig-simple-rnn-colah.png      ← 简单RNN（备用）
    ├── fig-gru-cell.png              ← GRU单元
    ├── fig-encoder-decoder.png       ← Encoder-Decoder
    └── fig-seq2seq.png               ← Seq2Seq架构
```
