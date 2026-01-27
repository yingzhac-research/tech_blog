"""
Transformer Chapter 8 - Architecture Figures (v2)
Sebastian Raschka 风格：干净、留白、柔和配色、无边框
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
from matplotlib.lines import Line2D
import matplotlib.patheffects as path_effects
import numpy as np

# ============================================================
# 风格配置 - Raschka Style
# ============================================================

# 柔和的配色方案（偏蓝灰、绿、橙）
COLORS = {
    # 主色调
    'blue': '#6C9BC2',        # 柔和蓝
    'green': '#7FB685',       # 柔和绿
    'orange': '#E8A87C',      # 柔和橙
    'purple': '#9B8DC2',      # 柔和紫
    'red': '#D4817A',         # 柔和红
    'yellow': '#E8D07C',      # 柔和黄
    'gray': '#A8B5C4',        # 蓝灰色

    # 功能色
    'encoder': '#6C9BC2',     # 蓝
    'decoder': '#E8A87C',     # 橙
    'attention': '#7FB685',   # 绿
    'ffn': '#E8D07C',         # 黄
    'norm': '#D4D4E8',        # 淡紫灰
    'embed': '#A8B5C4',       # 灰

    # 基础色
    'text': '#4A4A4A',        # 深灰文字
    'text_light': '#FFFFFF',  # 白色文字
    'arrow': '#7A7A7A',       # 箭头灰
    'bg': '#FFFFFF',          # 纯白背景
    'block_bg': '#F8F9FA',    # 区块背景
}

# 全局样式
plt.rcParams.update({
    'font.family': ['Arial', 'DejaVu Sans', 'Microsoft YaHei'],
    'font.size': 10,
    'font.weight': 'normal',
    'axes.unicode_minus': False,
    'figure.facecolor': COLORS['bg'],
    'axes.facecolor': COLORS['bg'],
    'savefig.facecolor': COLORS['bg'],
    'savefig.edgecolor': 'none',
})


# ============================================================
# 绘图工具函数
# ============================================================

def create_canvas(width, height):
    """创建干净的画布"""
    fig, ax = plt.subplots(figsize=(width, height))
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.axis('off')
    ax.set_aspect('equal')
    return fig, ax


def draw_box(ax, x, y, width, height, color, text='', text_color=None,
             fontsize=9, alpha=1.0, radius=0.15):
    """绘制圆角矩形（无边框，Raschka风格）"""
    if text_color is None:
        # 根据背景色自动选择文字颜色
        text_color = COLORS['text_light'] if color in [COLORS['blue'], COLORS['green'],
                                                        COLORS['encoder'], COLORS['decoder'],
                                                        COLORS['attention']] else COLORS['text']

    box = FancyBboxPatch(
        (x - width/2, y - height/2), width, height,
        boxstyle=f"round,pad=0.02,rounding_size={radius}",
        facecolor=color,
        edgecolor='none',  # 无边框
        alpha=alpha,
        zorder=2
    )
    ax.add_patch(box)

    if text:
        # 多行文本支持
        ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
                color=text_color, fontweight='medium', zorder=3,
                linespacing=1.2)
    return box


def draw_arrow(ax, start, end, color=None, lw=1.2, style='->',
               shrink_a=0, shrink_b=0, curved=False, rad=0.2):
    """绘制箭头（细线，Raschka风格）"""
    if color is None:
        color = COLORS['arrow']

    if curved:
        conn_style = f'arc3,rad={rad}'
    else:
        conn_style = 'arc3,rad=0'

    ax.annotate('',
                xy=end, xytext=start,
                arrowprops=dict(
                    arrowstyle=style,
                    color=color,
                    lw=lw,
                    shrinkA=shrink_a,
                    shrinkB=shrink_b,
                    connectionstyle=conn_style
                ),
                zorder=1)


def draw_label(ax, x, y, text, fontsize=10, color=None, weight='bold', ha='center'):
    """绘制标签文字"""
    if color is None:
        color = COLORS['text']
    ax.text(x, y, text, ha=ha, va='center', fontsize=fontsize,
            color=color, fontweight=weight, zorder=4)


def draw_dashed_box(ax, x, y, width, height, color, label='', label_pos='top'):
    """绘制虚线区块框"""
    box = FancyBboxPatch(
        (x - width/2, y - height/2), width, height,
        boxstyle="round,pad=0.03,rounding_size=0.2",
        facecolor=color,
        edgecolor=COLORS['arrow'],
        alpha=0.3,
        linestyle='--',
        linewidth=1.2,
        zorder=0
    )
    ax.add_patch(box)

    if label:
        label_y = y + height/2 + 0.25 if label_pos == 'top' else y - height/2 - 0.25
        ax.text(x, label_y, label, ha='center', va='center' if label_pos == 'top' else 'top',
                fontsize=10, color=COLORS['text'], fontweight='bold', zorder=4)


# ============================================================
# 图1: RNN-based Seq2Seq with Attention
# ============================================================
def create_rnn_seq2seq():
    fig, ax = create_canvas(10, 4.5)

    # Encoder
    enc_y = 3.2
    enc_color = COLORS['encoder']
    enc_labels = ['h1', 'h2', 'h3', 'h4']

    for i, label in enumerate(enc_labels):
        x = 1.5 + i * 1.1
        draw_box(ax, x, enc_y, 0.7, 0.55, enc_color, label, fontsize=11)
        if i > 0:
            draw_arrow(ax, (x - 1.1 + 0.35, enc_y), (x - 0.35, enc_y))

    draw_label(ax, 2.6, 3.9, 'Encoder', color=COLORS['encoder'])

    # Decoder
    dec_y = 1.3
    dec_color = COLORS['decoder']
    dec_labels = ['s1', 's2', 's3']

    for i, label in enumerate(dec_labels):
        x = 6.2 + i * 1.1
        draw_box(ax, x, dec_y, 0.7, 0.55, dec_color, label, fontsize=11)
        if i > 0:
            draw_arrow(ax, (x - 1.1 + 0.35, dec_y), (x - 0.35, dec_y))

    draw_label(ax, 7.3, 0.5, 'Decoder', color=COLORS['decoder'])

    # Context 连接
    draw_arrow(ax, (4.5 + 0.35, enc_y - 0.3), (6.2 - 0.35, dec_y + 0.3),
               color=COLORS['attention'], style='->', lw=1.5)
    ax.text(5.6, 2.5, 'context', fontsize=9, color=COLORS['attention'],
            style='italic', ha='center')

    # Attention 连接（淡色）
    for i in range(4):
        x_enc = 1.5 + i * 1.1
        draw_arrow(ax, (x_enc, enc_y - 0.28), (7.3, dec_y + 0.28),
                   color=COLORS['attention'], lw=0.8, style='->')
    ax.text(4.2, 2.0, 'attention', fontsize=9, color=COLORS['attention'],
            style='italic', ha='center')

    plt.tight_layout(pad=0.5)
    plt.savefig('fig-rnn-seq2seq.png', dpi=200, bbox_inches='tight')
    plt.savefig('fig-rnn-seq2seq.svg', bbox_inches='tight')
    plt.close()
    print("[OK] fig-rnn-seq2seq")


# ============================================================
# 图2: Transformer Architecture Overview
# ============================================================
def create_transformer_overview():
    fig, ax = create_canvas(11, 9)

    box_w = 2.2
    box_h = 0.5
    gap = 0.7

    # ========== Encoder 侧 ==========
    enc_x = 3

    # Input Embedding
    draw_box(ax, enc_x, 0.8, box_w, box_h, COLORS['embed'], 'Input\nEmbedding', fontsize=8)
    draw_box(ax, enc_x, 1.5, box_w, 0.35, COLORS['gray'], '+ Pos Encoding',
             text_color=COLORS['text'], fontsize=7, alpha=0.6)

    # Encoder Block 区域
    enc_base = 2.3
    draw_dashed_box(ax, enc_x, enc_base + 1.8, box_w + 0.6, 3.8,
                    COLORS['encoder'], 'Encoder x N')

    # Encoder 组件
    y = enc_base + 0.3
    draw_box(ax, enc_x, y, box_w, box_h, COLORS['attention'], 'Multi-Head\nSelf-Attention', fontsize=8)
    y += gap
    draw_box(ax, enc_x, y, box_w, 0.35, COLORS['norm'], 'Add & Norm', fontsize=7)
    y += gap * 0.7
    draw_box(ax, enc_x, y, box_w, box_h, COLORS['ffn'], 'Feed Forward', fontsize=8)
    y += gap
    draw_box(ax, enc_x, y, box_w, 0.35, COLORS['norm'], 'Add & Norm', fontsize=7)

    # Encoder 内部箭头
    arrows_y = [1.05, 1.68, 2.55, 3.0, 3.45, 3.9]
    for i in range(len(arrows_y) - 1):
        draw_arrow(ax, (enc_x, arrows_y[i]), (enc_x, arrows_y[i+1] - 0.18))

    # ========== Decoder 侧 ==========
    dec_x = 8

    # Output Embedding
    draw_box(ax, dec_x, 0.8, box_w, box_h, COLORS['embed'], 'Output\nEmbedding', fontsize=8)
    draw_box(ax, dec_x, 1.5, box_w, 0.35, COLORS['gray'], '+ Pos Encoding',
             text_color=COLORS['text'], fontsize=7, alpha=0.6)

    # Decoder Block 区域
    dec_base = 2.3
    draw_dashed_box(ax, dec_x, dec_base + 2.5, box_w + 0.6, 5.2,
                    COLORS['decoder'], 'Decoder x N')

    # Decoder 组件
    y = dec_base + 0.3
    draw_box(ax, dec_x, y, box_w, box_h, COLORS['attention'], 'Masked\nSelf-Attention', fontsize=8)
    y += gap
    draw_box(ax, dec_x, y, box_w, 0.35, COLORS['norm'], 'Add & Norm', fontsize=7)
    y += gap * 0.7
    draw_box(ax, dec_x, y, box_w, box_h, COLORS['attention'], 'Cross-Attention', fontsize=8)
    y += gap
    draw_box(ax, dec_x, y, box_w, 0.35, COLORS['norm'], 'Add & Norm', fontsize=7)
    y += gap * 0.7
    draw_box(ax, dec_x, y, box_w, box_h, COLORS['ffn'], 'Feed Forward', fontsize=8)
    y += gap
    draw_box(ax, dec_x, y, box_w, 0.35, COLORS['norm'], 'Add & Norm', fontsize=7)

    # Decoder 内部箭头
    dec_arrows_y = [1.05, 1.68, 2.55, 3.0, 3.45, 3.9, 4.35, 4.8, 5.25]
    for i in range(len(dec_arrows_y) - 1):
        draw_arrow(ax, (dec_x, dec_arrows_y[i]), (dec_x, dec_arrows_y[i+1] - 0.18))

    # Encoder -> Cross-Attention 连接
    draw_arrow(ax, (enc_x + box_w/2 + 0.1, 4.25), (dec_x - box_w/2 - 0.1, 3.73),
               color=COLORS['encoder'], lw=1.8, curved=True, rad=-0.15)

    # Output 层
    output_y = 6.2
    draw_box(ax, dec_x, output_y, box_w, box_h, COLORS['purple'], 'Linear', fontsize=9)
    draw_arrow(ax, (dec_x, 5.6), (dec_x, output_y - 0.25))

    output_y2 = 6.9
    draw_box(ax, dec_x, output_y2, box_w, box_h, COLORS['red'], 'Softmax', fontsize=9)
    draw_arrow(ax, (dec_x, output_y + 0.25), (dec_x, output_y2 - 0.25))

    # Output 标签
    draw_label(ax, dec_x, 7.6, 'Output Probabilities', fontsize=9, weight='normal')
    draw_arrow(ax, (dec_x, output_y2 + 0.25), (dec_x, 7.4))

    plt.tight_layout(pad=0.5)
    plt.savefig('fig-transformer-overview.png', dpi=200, bbox_inches='tight')
    plt.savefig('fig-transformer-overview.svg', bbox_inches='tight')
    plt.close()
    print("[OK] fig-transformer-overview")


# ============================================================
# 图3: Scaled Dot-Product Attention
# ============================================================
def create_scaled_attention():
    fig, ax = create_canvas(10, 3.5)

    y_top = 2.8
    y_mid = 1.6
    y_bot = 0.5

    box_w = 1.0
    box_h = 0.45

    # 输入 Q, K, V
    draw_box(ax, 1.2, y_top, 0.6, 0.5, COLORS['blue'], 'Q', fontsize=12)
    draw_box(ax, 2.2, y_top, 0.6, 0.5, COLORS['blue'], 'K', fontsize=12)
    draw_box(ax, 8.5, y_top, 0.6, 0.5, COLORS['orange'], 'V', fontsize=12)

    # MatMul (Q @ K^T)
    draw_box(ax, 1.7, y_mid, box_w, box_h, COLORS['attention'], 'MatMul', fontsize=9)
    draw_arrow(ax, (1.2, y_top - 0.25), (1.5, y_mid + 0.23))
    draw_arrow(ax, (2.2, y_top - 0.25), (1.9, y_mid + 0.23))

    # Scale
    draw_box(ax, 3.2, y_mid, box_w + 0.2, box_h, COLORS['ffn'], 'Scale', fontsize=9)
    ax.text(3.2, y_mid - 0.4, '(/ sqrt dk)', fontsize=7, ha='center', color=COLORS['text'], alpha=0.7)
    draw_arrow(ax, (2.2, y_mid), (2.6, y_mid))

    # Mask
    draw_box(ax, 4.8, y_mid, box_w, box_h, COLORS['norm'], 'Mask', fontsize=9)
    ax.text(4.8, y_mid - 0.4, '(optional)', fontsize=7, ha='center', color=COLORS['text'], alpha=0.6)
    draw_arrow(ax, (3.8, y_mid), (4.3, y_mid))

    # Softmax
    draw_box(ax, 6.2, y_mid, box_w, box_h, COLORS['purple'], 'Softmax', fontsize=9)
    draw_arrow(ax, (5.3, y_mid), (5.7, y_mid))

    # MatMul with V
    draw_box(ax, 7.8, y_mid, box_w, box_h, COLORS['attention'], 'MatMul', fontsize=9)
    draw_arrow(ax, (6.7, y_mid), (7.3, y_mid))
    draw_arrow(ax, (8.5, y_top - 0.25), (8.0, y_mid + 0.23))

    # Output
    draw_box(ax, 7.8, y_bot, 0.9, box_h, COLORS['gray'], 'Output', fontsize=9)
    draw_arrow(ax, (7.8, y_mid - 0.23), (7.8, y_bot + 0.23))

    plt.tight_layout(pad=0.5)
    plt.savefig('fig-scaled-dot-product.png', dpi=200, bbox_inches='tight')
    plt.savefig('fig-scaled-dot-product.svg', bbox_inches='tight')
    plt.close()
    print("[OK] fig-scaled-dot-product")


# ============================================================
# 图4: Multi-Head Attention
# ============================================================
def create_multi_head():
    fig, ax = create_canvas(10, 7)

    # 输入 Q, K, V
    input_y = 6.3
    draw_box(ax, 2.5, input_y, 0.6, 0.5, COLORS['blue'], 'Q', fontsize=12)
    draw_box(ax, 5.0, input_y, 0.6, 0.5, COLORS['blue'], 'K', fontsize=12)
    draw_box(ax, 7.5, input_y, 0.6, 0.5, COLORS['orange'], 'V', fontsize=12)

    # 多头
    head_info = [
        (2.0, COLORS['encoder'], 'Head 1'),
        (5.0, COLORS['attention'], 'Head 2'),
        (8.0, COLORS['decoder'], 'Head h'),
    ]

    head_y = 4.2

    for hx, hcolor, hlabel in head_info:
        # Linear 投影（小方块）
        linear_y = 5.4
        for dx, lbl in [(-0.5, 'Wq'), (0, 'Wk'), (0.5, 'Wv')]:
            draw_box(ax, hx + dx, linear_y, 0.4, 0.3, hcolor, '', fontsize=6, alpha=0.5)

        # 连接线到输入
        draw_arrow(ax, (2.5, input_y - 0.25), (hx - 0.5, linear_y + 0.15), color=COLORS['arrow'], lw=0.8)
        draw_arrow(ax, (5.0, input_y - 0.25), (hx, linear_y + 0.15), color=COLORS['arrow'], lw=0.8)
        draw_arrow(ax, (7.5, input_y - 0.25), (hx + 0.5, linear_y + 0.15), color=COLORS['arrow'], lw=0.8)

        # Attention 框
        draw_dashed_box(ax, hx, head_y, 1.8, 1.4, hcolor)
        draw_box(ax, hx, head_y, 1.5, 0.5, hcolor, 'Attention', fontsize=8)
        draw_label(ax, hx, head_y - 0.9, hlabel, fontsize=9, color=hcolor)

        # Linear 到 Attention
        for dx in [-0.5, 0, 0.5]:
            draw_arrow(ax, (hx + dx, linear_y - 0.15), (hx + dx * 0.3, head_y + 0.5),
                      color=COLORS['arrow'], lw=0.8)

    # 省略号
    ax.text(5.0, head_y, '...', fontsize=18, ha='center', va='center',
            color=COLORS['arrow'], alpha=0.5)

    # Concat
    concat_y = 2.3
    draw_box(ax, 5.0, concat_y, 1.8, 0.5, COLORS['gray'], 'Concat', fontsize=10)

    for hx, _, _ in head_info:
        draw_arrow(ax, (hx, head_y - 0.7 - 0.25), (5.0, concat_y + 0.25), color=COLORS['arrow'])

    # Linear W^O
    linear_y = 1.4
    draw_box(ax, 5.0, linear_y, 1.8, 0.5, COLORS['attention'], 'Linear (Wo)', fontsize=9)
    draw_arrow(ax, (5.0, concat_y - 0.25), (5.0, linear_y + 0.25))

    # Output
    output_y = 0.5
    draw_box(ax, 5.0, output_y, 1.2, 0.5, COLORS['purple'], 'Output', fontsize=10)
    draw_arrow(ax, (5.0, linear_y - 0.25), (5.0, output_y + 0.25))

    plt.tight_layout(pad=0.5)
    plt.savefig('fig-multi-head.png', dpi=200, bbox_inches='tight')
    plt.savefig('fig-multi-head.svg', bbox_inches='tight')
    plt.close()
    print("[OK] fig-multi-head")


# ============================================================
# 图5: Pre-Norm vs Post-Norm
# ============================================================
def create_pre_post_norm():
    fig, axes = plt.subplots(1, 2, figsize=(9, 5))

    for ax in axes:
        ax.set_xlim(0, 4.5)
        ax.set_ylim(0, 5.5)
        ax.axis('off')
        ax.set_aspect('equal')

    box_w = 1.6
    box_h = 0.45
    cx = 2.25

    # ========== Post-Norm ==========
    ax = axes[0]
    ax.set_title('Post-Norm (Original)', fontsize=11, fontweight='bold',
                 color=COLORS['decoder'], pad=15)

    y = 4.8
    draw_box(ax, cx, y, 0.6, 0.5, COLORS['gray'], 'x', fontsize=12)

    y = 3.8
    draw_box(ax, cx, y, box_w, box_h, COLORS['attention'], 'Sublayer', fontsize=9)
    draw_arrow(ax, (cx, 4.55), (cx, y + 0.23))

    # Residual 分支
    ax.plot([cx + 0.9, cx + 0.9], [4.8, 2.9], color=COLORS['arrow'], lw=1.2, ls='-')
    draw_arrow(ax, (cx + 0.9, 2.9), (cx + 0.3, 2.9), color=COLORS['arrow'])

    y = 2.9
    draw_box(ax, cx, y, 0.5, 0.45, COLORS['gray'], '+', fontsize=14, alpha=0.7)
    draw_arrow(ax, (cx, 3.55), (cx, y + 0.23))

    y = 2.0
    draw_box(ax, cx, y, box_w, box_h, COLORS['norm'], 'LayerNorm', fontsize=9)
    draw_arrow(ax, (cx, 2.67), (cx, y + 0.23))

    y = 1.1
    draw_box(ax, cx, y, 1.0, 0.45, COLORS['purple'], 'Output', fontsize=9)
    draw_arrow(ax, (cx, 1.77), (cx, y + 0.23))

    # ========== Pre-Norm ==========
    ax = axes[1]
    ax.set_title('Pre-Norm (GPT, LLaMA)', fontsize=11, fontweight='bold',
                 color=COLORS['encoder'], pad=15)

    y = 4.8
    draw_box(ax, cx, y, 0.6, 0.5, COLORS['gray'], 'x', fontsize=12)

    y = 3.9
    draw_box(ax, cx, y, box_w, box_h, COLORS['norm'], 'LayerNorm', fontsize=9)
    draw_arrow(ax, (cx, 4.55), (cx, y + 0.23))

    y = 3.0
    draw_box(ax, cx, y, box_w, box_h, COLORS['attention'], 'Sublayer', fontsize=9)
    draw_arrow(ax, (cx, 3.67), (cx, y + 0.23))

    # Residual 分支（从 x 直接到 +）
    ax.plot([cx + 0.9, cx + 0.9], [4.8, 2.1], color=COLORS['arrow'], lw=1.2, ls='-')
    draw_arrow(ax, (cx + 0.9, 2.1), (cx + 0.3, 2.1), color=COLORS['arrow'])

    y = 2.1
    draw_box(ax, cx, y, 0.5, 0.45, COLORS['gray'], '+', fontsize=14, alpha=0.7)
    draw_arrow(ax, (cx, 2.77), (cx, y + 0.23))

    y = 1.2
    draw_box(ax, cx, y, 1.0, 0.45, COLORS['purple'], 'Output', fontsize=9)
    draw_arrow(ax, (cx, 1.87), (cx, y + 0.23))

    plt.tight_layout(pad=1.0)
    plt.savefig('fig-pre-post-norm.png', dpi=200, bbox_inches='tight')
    plt.savefig('fig-pre-post-norm.svg', bbox_inches='tight')
    plt.close()
    print("[OK] fig-pre-post-norm")


# ============================================================
# 图6: Cross-Attention
# ============================================================
def create_cross_attention():
    fig, ax = create_canvas(9, 4.5)

    # Encoder 区域
    enc_x = 2.5
    draw_dashed_box(ax, enc_x, 2.8, 2.5, 2.2, COLORS['encoder'], 'Encoder')
    draw_box(ax, enc_x, 2.8, 2.0, 0.6, COLORS['encoder'], 'Encoder\nOutput', fontsize=9)

    # Decoder 区域
    dec_x = 6.5
    draw_dashed_box(ax, dec_x, 2.8, 2.5, 2.2, COLORS['decoder'], 'Decoder')
    draw_box(ax, dec_x, 2.8, 2.0, 0.6, COLORS['decoder'], 'Decoder\nState', fontsize=9)

    # Cross-Attention
    ca_y = 0.8
    draw_box(ax, 4.5, ca_y, 2.2, 0.6, COLORS['attention'], 'Cross-Attention', fontsize=10)

    # 连接箭头
    # Key, Value from Encoder
    draw_arrow(ax, (enc_x, 2.5), (4.0, ca_y + 0.3),
               color=COLORS['encoder'], lw=1.8, curved=True, rad=-0.2)
    draw_label(ax, 2.8, 1.5, 'K, V', fontsize=9, color=COLORS['encoder'], weight='normal')

    # Query from Decoder
    draw_arrow(ax, (dec_x, 2.5), (5.0, ca_y + 0.3),
               color=COLORS['decoder'], lw=1.8, curved=True, rad=0.2)
    draw_label(ax, 6.2, 1.5, 'Q', fontsize=9, color=COLORS['decoder'], weight='normal')

    plt.tight_layout(pad=0.5)
    plt.savefig('fig-cross-attention.png', dpi=200, bbox_inches='tight')
    plt.savefig('fig-cross-attention.svg', bbox_inches='tight')
    plt.close()
    print("[OK] fig-cross-attention")


# ============================================================
# 主函数
# ============================================================
if __name__ == '__main__':
    print("Generating Transformer figures (v2 - Raschka style)...\n")

    create_rnn_seq2seq()
    create_transformer_overview()
    create_scaled_attention()
    create_multi_head()
    create_pre_post_norm()
    create_cross_attention()

    print("\n=== All figures generated! ===")
