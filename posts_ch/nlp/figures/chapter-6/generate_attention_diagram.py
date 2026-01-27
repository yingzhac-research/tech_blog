"""
生成 Bahdanau Attention 机制流程图
风格：Sebastian Raschka 风格 - 干净、柔和配色
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

# 配色方案
COLORS = {
    'encoder': '#6C9BC2',      # 柔和蓝
    'decoder': '#E8A87C',      # 柔和橙
    'attention': '#7FB685',    # 柔和绿
    'context': '#B784A7',      # 柔和紫
    'output': '#E8D07C',       # 柔和黄
    'text': '#4A4A4A',         # 深灰文字
    'arrow': '#666666',        # 箭头颜色
    'light_gray': '#E8E8E8',   # 浅灰背景
}

def draw_rounded_box(ax, x, y, width, height, color, text, fontsize=10, text_color='white'):
    """绘制圆角矩形框"""
    box = FancyBboxPatch(
        (x - width/2, y - height/2), width, height,
        boxstyle="round,pad=0.02,rounding_size=0.1",
        facecolor=color, edgecolor='none', alpha=0.9
    )
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            color=text_color, fontweight='bold')

def draw_circle(ax, x, y, radius, color, text, fontsize=9):
    """绘制圆形节点"""
    circle = Circle((x, y), radius, facecolor=color, edgecolor='none', alpha=0.9)
    ax.add_patch(circle)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            color='white', fontweight='bold')

def draw_arrow(ax, start, end, color=None, style='->'):
    """绘制箭头"""
    if color is None:
        color = COLORS['arrow']
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle=style, color=color, lw=1.5))

def create_attention_diagram():
    """创建 Bahdanau Attention 机制图"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 9)
    ax.set_aspect('equal')
    ax.axis('off')

    # ==================== 编码器隐藏状态 ====================
    encoder_y = 7.5
    encoder_positions = [2, 4, 6, 8]
    encoder_labels = ['$h_1$', '$h_2$', '$h_3$', '$h_T$']

    for i, (x, label) in enumerate(zip(encoder_positions, encoder_labels)):
        draw_rounded_box(ax, x, encoder_y, 1.2, 0.8, COLORS['encoder'], label, fontsize=12)

    # 省略号
    ax.text(7, encoder_y, '...', ha='center', va='center', fontsize=16, color=COLORS['text'])

    # 编码器标签
    ax.text(5, 8.5, 'Encoder Hidden States', ha='center', va='center',
            fontsize=12, color=COLORS['text'], fontweight='bold')

    # ==================== 解码器状态 ====================
    decoder_x = 0.5
    decoder_y = 4
    draw_rounded_box(ax, decoder_x, decoder_y, 1.4, 0.8, COLORS['decoder'], '$s_{i-1}$', fontsize=12)
    ax.text(decoder_x, decoder_y - 0.8, 'Decoder\nState', ha='center', va='center',
            fontsize=9, color=COLORS['text'])

    # ==================== 对齐分数计算 ====================
    align_y = 5.5
    align_positions = [2, 4, 6, 8]
    align_labels = ['$e_{i1}$', '$e_{i2}$', '$e_{i3}$', '$e_{iT}$']

    for i, (x, label) in enumerate(zip(align_positions, align_labels)):
        draw_circle(ax, x, align_y, 0.4, COLORS['attention'], label, fontsize=9)

        # 从编码器到对齐分数的箭头
        draw_arrow(ax, (x, encoder_y - 0.4), (x, align_y + 0.4))

        # 从解码器到对齐分数的箭头
        draw_arrow(ax, (decoder_x + 0.7, decoder_y + 0.3), (x - 0.35, align_y - 0.25),
                   color=COLORS['decoder'])

    ax.text(7, align_y, '...', ha='center', va='center', fontsize=14, color=COLORS['text'])

    # 对齐分数公式
    ax.text(10, align_y, r'$e_{ij} = a(s_{i-1}, h_j)$', ha='left', va='center',
            fontsize=10, color=COLORS['text'], style='italic')

    # ==================== Softmax ====================
    softmax_y = 4
    softmax_x = 5
    draw_rounded_box(ax, softmax_x, softmax_y, 2.0, 0.7, COLORS['attention'], 'Softmax', fontsize=11)

    # 从对齐分数到softmax的箭头
    for x in align_positions:
        draw_arrow(ax, (x, align_y - 0.4), (softmax_x - 0.2 + (x-5)*0.1, softmax_y + 0.35))

    # ==================== 注意力权重 ====================
    weight_y = 2.5
    weight_positions = [2, 4, 6, 8]
    weight_labels = [r'$\alpha_{i1}$', r'$\alpha_{i2}$', r'$\alpha_{i3}$', r'$\alpha_{iT}$']

    for i, (x, label) in enumerate(zip(weight_positions, weight_labels)):
        draw_circle(ax, x, weight_y, 0.4, COLORS['context'], label, fontsize=8)

    ax.text(7, weight_y, '...', ha='center', va='center', fontsize=14, color=COLORS['text'])

    # 从softmax到权重的箭头
    for x in weight_positions:
        draw_arrow(ax, (softmax_x + (x-5)*0.1, softmax_y - 0.35), (x, weight_y + 0.4))

    # ==================== 加权求和 ====================
    context_y = 1
    context_x = 5
    draw_rounded_box(ax, context_x, context_y, 1.5, 0.8, COLORS['context'], '$c_i$', fontsize=12)

    # 从权重和编码器到上下文向量的箭头
    for x in weight_positions:
        # 虚线表示加权求和
        draw_arrow(ax, (x, weight_y - 0.4), (context_x - 0.3 + (x-5)*0.15, context_y + 0.4))

    # 上下文向量公式
    ax.text(context_x, context_y - 0.8, r'$c_i = \sum_j \alpha_{ij} h_j$', ha='center', va='center',
            fontsize=10, color=COLORS['text'], style='italic')

    # ==================== 标题 ====================
    ax.text(5, -0.3, 'Context Vector', ha='center', va='center',
            fontsize=11, color=COLORS['text'], fontweight='bold')

    # ==================== 图例 ====================
    legend_x = 10
    legend_items = [
        (COLORS['encoder'], 'Encoder'),
        (COLORS['decoder'], 'Decoder'),
        (COLORS['attention'], 'Alignment'),
        (COLORS['context'], 'Attention Weights'),
    ]
    for i, (color, label) in enumerate(legend_items):
        y = 3 - i * 0.6
        rect = FancyBboxPatch((legend_x - 0.3, y - 0.15), 0.4, 0.3,
                              boxstyle="round,pad=0.01,rounding_size=0.05",
                              facecolor=color, edgecolor='none')
        ax.add_patch(rect)
        ax.text(legend_x + 0.4, y, label, ha='left', va='center', fontsize=9, color=COLORS['text'])

    plt.tight_layout()
    return fig

if __name__ == "__main__":
    from pathlib import Path

    fig = create_attention_diagram()

    output_dir = Path(__file__).parent
    fig.savefig(output_dir / 'fig-attention-mechanism.png', dpi=200, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    fig.savefig(output_dir / 'fig-attention-mechanism.svg', bbox_inches='tight',
                facecolor='white', edgecolor='none')

    print("[OK] Generated: fig-attention-mechanism.png")
    print("[OK] Generated: fig-attention-mechanism.svg")
    plt.close()
