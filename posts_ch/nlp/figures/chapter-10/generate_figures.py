"""
Chapter 10: 预训练思想的起源 — 配图生成脚本

风格: Sebastian Raschka 风格 — 干净、留白、柔和配色、无边框
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# ============================================================
# 全局配色方案
# ============================================================
COLORS = {
    'blue':    '#6C9BC2',
    'orange':  '#E8A87C',
    'green':   '#7FB685',
    'yellow':  '#E8D07C',
    'purple':  '#B39DDB',
    'red':     '#E57373',
    'gray':    '#A8B5C4',
    'light_gray': '#F0F2F5',
    'text':    '#4A4A4A',
    'white':   '#FFFFFF',
}

import platform
if platform.system() == 'Windows':
    _cjk_font = 'Microsoft YaHei'
elif platform.system() == 'Darwin':
    _cjk_font = 'PingFang SC'
else:
    _cjk_font = 'Noto Sans CJK SC'

plt.rcParams.update({
    'font.size': 11,
    'font.family': 'sans-serif',
    'font.sans-serif': [_cjk_font, 'Arial', 'DejaVu Sans'],
    'axes.unicode_minus': False,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.spines.left': False,
    'axes.spines.bottom': False,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'text.color': COLORS['text'],
})


# ============================================================
# Figure 1: 预训练范式演进时间线
# ============================================================
def fig_pretraining_timeline():
    fig, ax = plt.subplots(figsize=(14, 5))

    # 时间轴
    years = [2008, 2013, 2014, 2015, 2017, 2018]
    y_base = 0.5

    ax.plot([2007, 2019], [y_base, y_base], color=COLORS['gray'],
            linewidth=2, zorder=1)

    # 事件数据: (year, label, sublabel, color, y_offset)
    events = [
        (2008, 'Collobert &\nWeston', '多任务共享表示\n(被低估的先驱)',
         COLORS['gray'], 0.25),
        (2013, 'Word2Vec', '词向量预训练\n(第一代: 浅层迁移)',
         COLORS['blue'], 0.25),
        (2014, 'ImageNet\n预训练', 'CNN特征迁移\n(CV的启示)',
         COLORS['green'], -0.30),
        (2015, 'Dai & Le', 'LSTM语言模型\n预训练 (第二代)',
         COLORS['orange'], 0.25),
        (2017, 'Transformer', '强大的新架构\n(缺一把火)',
         COLORS['purple'], -0.30),
        (2018, 'ULMFiT\nELMo / GPT\nBERT', '深层预训练+微调\n(第三代: 范式成熟)',
         COLORS['red'], 0.25),
    ]

    for year, label, sublabel, color, y_off in events:
        # 圆点
        ax.scatter(year, y_base, s=120, color=color, zorder=3,
                   edgecolors='white', linewidths=1.5)
        # 连接线
        ax.plot([year, year], [y_base, y_base + y_off * 0.8],
                color=color, linewidth=1.5, zorder=2)
        # 标签
        va = 'bottom' if y_off > 0 else 'top'
        y_label = y_base + y_off
        ax.text(year, y_label, label, ha='center', va=va,
                fontsize=10, fontweight='bold', color=COLORS['text'])
        y_sub = y_label + (0.12 if y_off > 0 else -0.12)
        ax.text(year, y_sub, sublabel, ha='center', va=va,
                fontsize=8, color=COLORS['gray'], style='italic')

    # 年份标签
    for year in years:
        ax.text(year, y_base - 0.08, str(year), ha='center', va='top',
                fontsize=9, color=COLORS['text'], fontweight='bold')

    # 阶段标注
    ax.annotate('', xy=(2016, 0.05), xytext=(2008, 0.05),
                arrowprops=dict(arrowstyle='->', color=COLORS['blue'],
                               lw=1.5))
    ax.text(2012, 0.0, '词级别迁移', ha='center', fontsize=8,
            color=COLORS['blue'])

    ax.annotate('', xy=(2019, 0.05), xytext=(2016, 0.05),
                arrowprops=dict(arrowstyle='->', color=COLORS['red'],
                               lw=1.5))
    ax.text(2017.5, 0.0, '模型级别迁移', ha='center', fontsize=8,
            color=COLORS['red'])

    ax.set_xlim(2007, 2019.5)
    ax.set_ylim(-0.3, 1.15)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title('NLP 预训练范式的演进', fontsize=14,
                 fontweight='bold', pad=15, color=COLORS['text'])

    plt.tight_layout()
    fig.savefig('fig-pretraining-timeline.png', dpi=200, bbox_inches='tight',
                facecolor='white')
    fig.savefig('fig-pretraining-timeline.svg', bbox_inches='tight',
                facecolor='white')
    plt.close()
    print('[OK] fig-pretraining-timeline')


# ============================================================
# Figure 2: 迁移学习两种方式对比
# ============================================================
def fig_transfer_comparison():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5.5))

    def draw_model(ax, title, layers, frozen_up_to=-1, has_new_head=False):
        """绘制模型示意图, layers: list of (label, color)"""
        n = len(layers)
        box_h = 0.7
        gap = 0.15
        total_h = n * box_h + (n - 1) * gap
        y_start = (5 - total_h) / 2

        for i, (label, color) in enumerate(layers):
            y = y_start + i * (box_h + gap)
            alpha = 0.4 if i <= frozen_up_to else 1.0
            edgecolor = COLORS['gray'] if i <= frozen_up_to else 'none'
            linestyle = '--' if i <= frozen_up_to else '-'

            box = FancyBboxPatch((0.5, y), 3, box_h,
                                 boxstyle="round,pad=0.05,rounding_size=0.15",
                                 facecolor=color, edgecolor=edgecolor,
                                 alpha=alpha, linewidth=1.5,
                                 linestyle=linestyle)
            ax.add_patch(box)
            ax.text(2, y + box_h / 2, label, ha='center', va='center',
                    fontsize=10, color=COLORS['text'],
                    alpha=max(alpha, 0.6),
                    fontweight='bold' if i > frozen_up_to else 'normal')

            # 冻结图标
            if i <= frozen_up_to:
                ax.text(3.7, y + box_h / 2, '[frozen]', ha='center', va='center',
                        fontsize=7, color=COLORS['gray'])

            # 箭头
            if i > 0:
                ax.annotate('', xy=(2, y), xytext=(2, y - gap),
                            arrowprops=dict(arrowstyle='->', color=COLORS['gray'],
                                           lw=1.2))

        ax.set_xlim(-0.2, 4.5)
        ax.set_ylim(-0.3, 5.3)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(title, fontsize=12, fontweight='bold', pad=10,
                     color=COLORS['text'])

    # (a) 从零训练
    layers_scratch = [
        ('Embedding\n(随机初始化)', COLORS['light_gray']),
        ('Hidden Layer 1', COLORS['light_gray']),
        ('Hidden Layer 2', COLORS['light_gray']),
        ('Task Head', COLORS['light_gray']),
    ]
    draw_model(axes[0], '(a) 从零训练', layers_scratch)
    axes[0].text(2, -0.1, '所有层随机初始化\n需要大量标注数据',
                 ha='center', fontsize=9, color=COLORS['red'], style='italic')

    # (b) 特征提取
    layers_feature = [
        ('Embedding\n(预训练 Word2Vec)', COLORS['blue']),
        ('Hidden Layer 1', COLORS['light_gray']),
        ('Hidden Layer 2', COLORS['light_gray']),
        ('Task Head', COLORS['light_gray']),
    ]
    draw_model(axes[1], '(b) 词向量预训练\n(浅层迁移)', layers_feature,
               frozen_up_to=0)
    axes[1].text(2, -0.1, '仅迁移词级别知识\n高层仍需从零学习',
                 ha='center', fontsize=9, color=COLORS['orange'], style='italic')

    # (c) 深层预训练 + 微调
    layers_finetune = [
        ('Embedding\n(预训练)', COLORS['blue']),
        ('Hidden Layer 1\n(预训练)', COLORS['green']),
        ('Hidden Layer 2\n(预训练)', COLORS['green']),
        ('Task Head\n(新增)', COLORS['orange']),
    ]
    draw_model(axes[2], '(c) 深层预训练 + 微调\n(ULMFiT / GPT / BERT)',
               layers_finetune)
    axes[2].text(2, -0.1, '所有层都预训练\n微调适配下游任务',
                 ha='center', fontsize=9, color=COLORS['green'], style='italic')

    plt.tight_layout()
    fig.savefig('fig-transfer-comparison.png', dpi=200, bbox_inches='tight',
                facecolor='white')
    fig.savefig('fig-transfer-comparison.svg', bbox_inches='tight',
                facecolor='white')
    plt.close()
    print('[OK] fig-transfer-comparison')


# ============================================================
# Figure 3: 静态 vs 上下文词向量
# ============================================================
def fig_static_vs_contextual():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # --- (a) 静态词向量 ---
    ax = axes[0]
    ax.set_title('(a) 静态词向量 (Word2Vec / GloVe)', fontsize=11,
                 fontweight='bold', color=COLORS['text'], pad=12)

    sentences = [
        'I went to the bank to deposit money.',
        'I sat on the bank of the river.',
    ]
    # 两个句子中的 "bank" 指向同一个向量
    for i, sent in enumerate(sentences):
        y = 3.5 - i * 1.8
        ax.text(0.3, y, sent, fontsize=9.5, color=COLORS['text'],
                bbox=dict(boxstyle='round,pad=0.4', facecolor=COLORS['light_gray'],
                         edgecolor='none'))
        # "bank" 高亮
        # 箭头指向同一个向量
        ax.annotate('', xy=(4.5, 1.5), xytext=(2.2, y - 0.3),
                    arrowprops=dict(arrowstyle='->', color=COLORS['red'],
                                   lw=1.3, connectionstyle='arc3,rad=0.2'))

    # 共享向量
    vec_box = FancyBboxPatch((3.8, 1.0), 2.5, 0.9,
                             boxstyle='round,pad=0.1,rounding_size=0.15',
                             facecolor=COLORS['red'], alpha=0.15,
                             edgecolor=COLORS['red'], linewidth=1.5)
    ax.add_patch(vec_box)
    ax.text(5.05, 1.45, '"bank"\n[0.23, −0.15, 0.87, ...]',
            ha='center', va='center', fontsize=9, color=COLORS['red'],
            fontweight='bold')
    ax.text(5.05, 0.6, '一个词 = 一个固定向量\n无法区分不同含义!',
            ha='center', fontsize=8.5, color=COLORS['red'], style='italic')

    ax.set_xlim(-0.1, 7)
    ax.set_ylim(0, 4.5)
    ax.set_xticks([])
    ax.set_yticks([])

    # --- (b) 上下文词向量 ---
    ax = axes[1]
    ax.set_title('(b) 上下文词向量 (ELMo / BERT)', fontsize=11,
                 fontweight='bold', color=COLORS['text'], pad=12)

    for i, (sent, meaning, color) in enumerate([
        ('I went to the bank to deposit money.', '金融机构', COLORS['blue']),
        ('I sat on the bank of the river.', '河岸', COLORS['green']),
    ]):
        y = 3.5 - i * 1.8
        ax.text(0.3, y, sent, fontsize=9.5, color=COLORS['text'],
                bbox=dict(boxstyle='round,pad=0.4', facecolor=COLORS['light_gray'],
                         edgecolor='none'))

        # 各自指向不同向量
        vec_y = y - 0.7
        vec_box = FancyBboxPatch((3.8, vec_y - 0.1), 2.5, 0.65,
                                 boxstyle='round,pad=0.1,rounding_size=0.15',
                                 facecolor=color, alpha=0.15,
                                 edgecolor=color, linewidth=1.5)
        ax.add_patch(vec_box)
        ax.annotate('', xy=(5.05, vec_y + 0.25), xytext=(2.2, y - 0.3),
                    arrowprops=dict(arrowstyle='->', color=color,
                                   lw=1.3))
        vec_text = f'"bank" → {meaning}' if i == 0 else f'"bank" → {meaning}'
        ax.text(5.05, vec_y + 0.22, vec_text,
                ha='center', va='center', fontsize=9, color=color,
                fontweight='bold')

    ax.text(5.05, 0.45, '同一个词 = 不同向量\n根据上下文动态生成',
            ha='center', fontsize=8.5, color=COLORS['green'], style='italic')

    ax.set_xlim(-0.1, 7)
    ax.set_ylim(0, 4.5)
    ax.set_xticks([])
    ax.set_yticks([])

    plt.tight_layout()
    fig.savefig('fig-static-vs-contextual.png', dpi=200, bbox_inches='tight',
                facecolor='white')
    fig.savefig('fig-static-vs-contextual.svg', bbox_inches='tight',
                facecolor='white')
    plt.close()
    print('[OK] fig-static-vs-contextual')


# ============================================================
# Main
# ============================================================
if __name__ == '__main__':
    fig_pretraining_timeline()
    fig_transfer_comparison()
    fig_static_vs_contextual()
    print('\nAll figures generated successfully.')
