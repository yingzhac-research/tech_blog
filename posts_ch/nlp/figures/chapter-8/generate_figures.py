"""
Transformer Chapter 8 - Architecture Figures
使用 matplotlib 生成专业级架构图
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, ConnectionPatch
import numpy as np

# 设置全局样式
plt.rcParams['font.family'] = ['DejaVu Sans', 'Microsoft YaHei', 'SimHei']
plt.rcParams['font.size'] = 10
plt.rcParams['axes.unicode_minus'] = False

# 配色方案 - 使用更现代的颜色
COLORS = {
    'encoder': '#4A90A4',      # 蓝绿色
    'decoder': '#E07A5F',      # 珊瑚色
    'attention': '#81B29A',    # 薄荷绿
    'ffn': '#F2CC8F',          # 淡黄色
    'norm': '#B8B8D1',         # 淡紫灰
    'input': '#3D405B',        # 深灰蓝
    'output': '#3D405B',
    'arrow': '#555555',
    'text': '#2D2D2D',
    'bg': '#FAFAFA',
}


def draw_rounded_box(ax, x, y, width, height, text, color, text_color='white', fontsize=9, alpha=0.9):
    """绘制圆角矩形框"""
    box = FancyBboxPatch(
        (x - width/2, y - height/2), width, height,
        boxstyle="round,pad=0.02,rounding_size=0.1",
        facecolor=color, edgecolor='none', alpha=alpha,
        transform=ax.transData, zorder=2
    )
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            color=text_color, fontweight='medium', zorder=3)
    return box


def draw_arrow(ax, start, end, color=COLORS['arrow'], style='->'):
    """绘制箭头"""
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle=style, color=color, lw=1.5),
                zorder=1)


# ============================================================
# 图1: RNN-based Seq2Seq with Attention
# ============================================================
def create_rnn_seq2seq():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')
    ax.set_facecolor(COLORS['bg'])
    fig.patch.set_facecolor(COLORS['bg'])

    # Encoder 部分
    encoder_y = 3.5
    encoder_color = COLORS['encoder']
    for i, label in enumerate(['h₁', 'h₂', 'h₃', 'h₄']):
        x = 1.5 + i * 1.2
        draw_rounded_box(ax, x, encoder_y, 0.8, 0.6, label, encoder_color, fontsize=11)
        if i > 0:
            draw_arrow(ax, (x - 1.2 + 0.4, encoder_y), (x - 0.4, encoder_y))

    # Encoder 标签
    ax.text(3.3, 4.3, 'Encoder', ha='center', fontsize=12, fontweight='bold', color=encoder_color)

    # Decoder 部分
    decoder_y = 1.5
    decoder_color = COLORS['decoder']
    for i, label in enumerate(['s₁', 's₂', 's₃']):
        x = 6 + i * 1.2
        draw_rounded_box(ax, x, decoder_y, 0.8, 0.6, label, decoder_color, fontsize=11)
        if i > 0:
            draw_arrow(ax, (x - 1.2 + 0.4, decoder_y), (x - 0.4, decoder_y))

    # Decoder 标签
    ax.text(7.2, 0.7, 'Decoder', ha='center', fontsize=12, fontweight='bold', color=decoder_color)

    # Context 连接 (虚线)
    ax.annotate('', xy=(6 - 0.4, decoder_y + 0.3), xytext=(4.5 + 0.4, encoder_y - 0.3),
                arrowprops=dict(arrowstyle='->', color=COLORS['attention'],
                               linestyle='dashed', lw=1.5))
    ax.text(5.5, 2.7, 'context', fontsize=9, color=COLORS['attention'], style='italic')

    # Attention 连接
    for i in range(4):
        x_enc = 1.5 + i * 1.2
        ax.annotate('', xy=(7.2, decoder_y + 0.35), xytext=(x_enc, encoder_y - 0.35),
                    arrowprops=dict(arrowstyle='->', color=COLORS['attention'],
                                   alpha=0.4, lw=1))
    ax.text(4.5, 2.2, 'attention', fontsize=9, color=COLORS['attention'], style='italic')

    plt.tight_layout()
    plt.savefig('fig-rnn-seq2seq.png', dpi=150, bbox_inches='tight',
                facecolor=COLORS['bg'], edgecolor='none')
    plt.savefig('fig-rnn-seq2seq.svg', bbox_inches='tight',
                facecolor=COLORS['bg'], edgecolor='none')
    plt.close()
    print("[OK] Created: fig-rnn-seq2seq.png/svg")


# ============================================================
# 图2: Transformer Architecture Overview
# ============================================================
def create_transformer_overview():
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_facecolor(COLORS['bg'])
    fig.patch.set_facecolor(COLORS['bg'])

    # ---- Encoder 侧 ----
    enc_x = 3

    # Input Embedding
    draw_rounded_box(ax, enc_x, 1, 2.5, 0.6, 'Input Embedding', COLORS['input'], fontsize=9)
    draw_rounded_box(ax, enc_x, 1.8, 2.5, 0.5, '+ Positional Encoding', '#6B7280', fontsize=8)

    # Encoder Block
    enc_block_y = 4.5
    block_width = 2.8

    # 背景框
    enc_bg = FancyBboxPatch((enc_x - block_width/2 - 0.2, 2.5), block_width + 0.4, 4.5,
                            boxstyle="round,pad=0.05,rounding_size=0.2",
                            facecolor=COLORS['encoder'], alpha=0.15, edgecolor=COLORS['encoder'],
                            linestyle='--', linewidth=1.5)
    ax.add_patch(enc_bg)
    ax.text(enc_x, 7.2, 'Encoder ×N', ha='center', fontsize=11, fontweight='bold',
            color=COLORS['encoder'])

    # Encoder 内部组件
    draw_rounded_box(ax, enc_x, 3.2, block_width, 0.6, 'Multi-Head Self-Attention', COLORS['attention'], fontsize=9)
    draw_rounded_box(ax, enc_x, 4.0, block_width, 0.45, 'Add & Norm', COLORS['norm'], text_color='#333', fontsize=8)
    draw_rounded_box(ax, enc_x, 4.8, block_width, 0.6, 'Feed-Forward Network', COLORS['ffn'], text_color='#333', fontsize=9)
    draw_rounded_box(ax, enc_x, 5.6, block_width, 0.45, 'Add & Norm', COLORS['norm'], text_color='#333', fontsize=8)

    # Encoder 内部箭头
    draw_arrow(ax, (enc_x, 1.3), (enc_x, 1.55))
    draw_arrow(ax, (enc_x, 2.05), (enc_x, 2.9))
    draw_arrow(ax, (enc_x, 3.5), (enc_x, 3.75))
    draw_arrow(ax, (enc_x, 4.25), (enc_x, 4.5))
    draw_arrow(ax, (enc_x, 5.1), (enc_x, 5.35))

    # ---- Decoder 侧 ----
    dec_x = 9

    # Output Embedding
    draw_rounded_box(ax, dec_x, 1, 2.5, 0.6, 'Output Embedding', COLORS['input'], fontsize=9)
    draw_rounded_box(ax, dec_x, 1.8, 2.5, 0.5, '+ Positional Encoding', '#6B7280', fontsize=8)

    # Decoder Block 背景
    dec_bg = FancyBboxPatch((dec_x - block_width/2 - 0.2, 2.5), block_width + 0.4, 5.5,
                            boxstyle="round,pad=0.05,rounding_size=0.2",
                            facecolor=COLORS['decoder'], alpha=0.15, edgecolor=COLORS['decoder'],
                            linestyle='--', linewidth=1.5)
    ax.add_patch(dec_bg)
    ax.text(dec_x, 8.2, 'Decoder ×N', ha='center', fontsize=11, fontweight='bold',
            color=COLORS['decoder'])

    # Decoder 内部组件
    draw_rounded_box(ax, dec_x, 3.2, block_width, 0.6, 'Masked Multi-Head\nSelf-Attention', COLORS['attention'], fontsize=8)
    draw_rounded_box(ax, dec_x, 4.0, block_width, 0.45, 'Add & Norm', COLORS['norm'], text_color='#333', fontsize=8)
    draw_rounded_box(ax, dec_x, 4.8, block_width, 0.6, 'Multi-Head\nCross-Attention', COLORS['attention'], fontsize=8)
    draw_rounded_box(ax, dec_x, 5.6, block_width, 0.45, 'Add & Norm', COLORS['norm'], text_color='#333', fontsize=8)
    draw_rounded_box(ax, dec_x, 6.4, block_width, 0.6, 'Feed-Forward Network', COLORS['ffn'], text_color='#333', fontsize=9)
    draw_rounded_box(ax, dec_x, 7.2, block_width, 0.45, 'Add & Norm', COLORS['norm'], text_color='#333', fontsize=8)

    # Decoder 内部箭头
    draw_arrow(ax, (dec_x, 1.3), (dec_x, 1.55))
    draw_arrow(ax, (dec_x, 2.05), (dec_x, 2.9))
    draw_arrow(ax, (dec_x, 3.55), (dec_x, 3.75))
    draw_arrow(ax, (dec_x, 4.25), (dec_x, 4.5))
    draw_arrow(ax, (dec_x, 5.15), (dec_x, 5.35))
    draw_arrow(ax, (dec_x, 5.85), (dec_x, 6.1))
    draw_arrow(ax, (dec_x, 6.7), (dec_x, 6.95))

    # Encoder 到 Decoder 的 Cross-Attention 连接
    ax.annotate('', xy=(dec_x - block_width/2, 4.8), xytext=(enc_x + block_width/2, 5.6),
                arrowprops=dict(arrowstyle='->', color=COLORS['encoder'], lw=2,
                               connectionstyle='arc3,rad=-0.2'))

    # 输出层
    draw_rounded_box(ax, dec_x, 8.6, 2.5, 0.6, 'Linear + Softmax', COLORS['output'], fontsize=9)
    draw_arrow(ax, (dec_x, 7.45), (dec_x, 8.3))

    # Output 标签
    ax.text(dec_x, 9.3, 'Output Probabilities', ha='center', fontsize=10, color=COLORS['text'])
    draw_arrow(ax, (dec_x, 8.9), (dec_x, 9.15))

    plt.tight_layout()
    plt.savefig('fig-transformer-overview.png', dpi=150, bbox_inches='tight',
                facecolor=COLORS['bg'], edgecolor='none')
    plt.savefig('fig-transformer-overview.svg', bbox_inches='tight',
                facecolor=COLORS['bg'], edgecolor='none')
    plt.close()
    print("[OK] Created: fig-transformer-overview.png/svg")


# ============================================================
# 图3: Scaled Dot-Product Attention
# ============================================================
def create_scaled_attention():
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis('off')
    ax.set_facecolor(COLORS['bg'])
    fig.patch.set_facecolor(COLORS['bg'])

    y_top = 3.2
    y_mid = 2.0
    y_bot = 0.8

    # 输入: Q, K, V
    draw_rounded_box(ax, 1, y_top, 0.7, 0.5, 'Q', COLORS['encoder'], fontsize=11)
    draw_rounded_box(ax, 2.2, y_top, 0.7, 0.5, 'K', COLORS['encoder'], fontsize=11)
    draw_rounded_box(ax, 8.5, y_top, 0.7, 0.5, 'V', COLORS['decoder'], fontsize=11)

    # MatMul (Q·K^T)
    draw_rounded_box(ax, 1.6, y_mid, 1.2, 0.5, 'MatMul', COLORS['attention'], fontsize=9)
    draw_arrow(ax, (1, y_top - 0.25), (1.3, y_mid + 0.25))
    draw_arrow(ax, (2.2, y_top - 0.25), (1.9, y_mid + 0.25))

    # Scale
    draw_rounded_box(ax, 3.3, y_mid, 1.4, 0.5, 'Scale ÷√dₖ', COLORS['ffn'], text_color='#333', fontsize=9)
    draw_arrow(ax, (2.2, y_mid), (2.6, y_mid))

    # Mask (optional)
    draw_rounded_box(ax, 5, y_mid, 1.2, 0.5, 'Mask', COLORS['norm'], text_color='#333', fontsize=9)
    ax.text(5, y_mid - 0.45, '(optional)', fontsize=7, ha='center', color='#888')
    draw_arrow(ax, (4, y_mid), (4.4, y_mid))

    # Softmax
    draw_rounded_box(ax, 6.5, y_mid, 1.2, 0.5, 'Softmax', '#9B59B6', fontsize=9)
    draw_arrow(ax, (5.6, y_mid), (5.9, y_mid))

    # MatMul with V
    draw_rounded_box(ax, 8, y_mid, 1.2, 0.5, 'MatMul', COLORS['attention'], fontsize=9)
    draw_arrow(ax, (7.1, y_mid), (7.4, y_mid))
    draw_arrow(ax, (8.5, y_top - 0.25), (8.2, y_mid + 0.25))

    # Output
    draw_rounded_box(ax, 8, y_bot, 1.0, 0.5, 'Output', COLORS['output'], fontsize=9)
    draw_arrow(ax, (8, y_mid - 0.25), (8, y_bot + 0.25))

    # 公式标注
    ax.text(5, 0.2, r'Attention(Q, K, V) = softmax(QK$^\mathsf{T}$ / √d$_k$) V',
            ha='center', fontsize=11, style='italic', color=COLORS['text'])

    plt.tight_layout()
    plt.savefig('fig-scaled-dot-product.png', dpi=150, bbox_inches='tight',
                facecolor=COLORS['bg'], edgecolor='none')
    plt.savefig('fig-scaled-dot-product.svg', bbox_inches='tight',
                facecolor=COLORS['bg'], edgecolor='none')
    plt.close()
    print("[OK] Created: fig-scaled-dot-product.png/svg")


# ============================================================
# 图4: Multi-Head Attention
# ============================================================
def create_multi_head():
    fig, ax = plt.subplots(figsize=(11, 7))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7)
    ax.axis('off')
    ax.set_facecolor(COLORS['bg'])
    fig.patch.set_facecolor(COLORS['bg'])

    # 输入 Q, K, V
    input_y = 6.2
    draw_rounded_box(ax, 3, input_y, 0.8, 0.5, 'Q', COLORS['encoder'], fontsize=11)
    draw_rounded_box(ax, 5.5, input_y, 0.8, 0.5, 'K', COLORS['encoder'], fontsize=11)
    draw_rounded_box(ax, 8, input_y, 0.8, 0.5, 'V', COLORS['decoder'], fontsize=11)

    # 多头结构
    head_colors = ['#E07A5F', '#81B29A', '#F2CC8F']
    head_labels = ['Head 1', 'Head 2', 'Head h']
    head_x = [2.5, 5.5, 8.5]

    for i, (x, label, color) in enumerate(zip(head_x, head_labels, head_colors)):
        # Linear 层
        linear_y = 5.0
        draw_rounded_box(ax, x - 0.6, linear_y, 0.5, 0.4, 'W^Q', color, fontsize=7, alpha=0.7)
        draw_rounded_box(ax, x, linear_y, 0.5, 0.4, 'W^K', color, fontsize=7, alpha=0.7)
        draw_rounded_box(ax, x + 0.6, linear_y, 0.5, 0.4, 'W^V', color, fontsize=7, alpha=0.7)

        # 从输入到 Linear
        draw_arrow(ax, (3, input_y - 0.25), (x - 0.6, linear_y + 0.2), color='#888')
        draw_arrow(ax, (5.5, input_y - 0.25), (x, linear_y + 0.2), color='#888')
        draw_arrow(ax, (8, input_y - 0.25), (x + 0.6, linear_y + 0.2), color='#888')

        # Head 框
        head_bg = FancyBboxPatch((x - 1.1, 3.0), 2.2, 1.6,
                                 boxstyle="round,pad=0.03,rounding_size=0.15",
                                 facecolor=color, alpha=0.2, edgecolor=color, linewidth=1.5)
        ax.add_patch(head_bg)

        # Attention
        draw_rounded_box(ax, x, 3.8, 1.6, 0.5, 'Scaled Dot-Product\nAttention', color, fontsize=7)
        ax.text(x, 3.15, label, ha='center', fontsize=9, fontweight='bold', color=color)

        # Linear 到 Attention
        draw_arrow(ax, (x - 0.6, linear_y - 0.2), (x - 0.4, 4.1), color='#888')
        draw_arrow(ax, (x, linear_y - 0.2), (x, 4.1), color='#888')
        draw_arrow(ax, (x + 0.6, linear_y - 0.2), (x + 0.4, 4.1), color='#888')

    # ... 省略号
    ax.text(5.5, 3.5, '...', fontsize=16, ha='center', va='center', color='#888')

    # Concat
    concat_y = 2.0
    draw_rounded_box(ax, 5.5, concat_y, 2.0, 0.5, 'Concat', '#6B7280', fontsize=10)

    for x in head_x:
        draw_arrow(ax, (x, 3.0), (5.5, concat_y + 0.25), color='#888')

    # Linear (output projection)
    draw_rounded_box(ax, 5.5, 1.2, 1.5, 0.5, 'Linear W^O', COLORS['attention'], fontsize=9)
    draw_arrow(ax, (5.5, concat_y - 0.25), (5.5, 1.45))

    # Output
    draw_rounded_box(ax, 5.5, 0.4, 1.2, 0.5, 'Output', COLORS['output'], fontsize=10)
    draw_arrow(ax, (5.5, 0.95), (5.5, 0.65))

    plt.tight_layout()
    plt.savefig('fig-multi-head.png', dpi=150, bbox_inches='tight',
                facecolor=COLORS['bg'], edgecolor='none')
    plt.savefig('fig-multi-head.svg', bbox_inches='tight',
                facecolor=COLORS['bg'], edgecolor='none')
    plt.close()
    print("[OK] Created: fig-multi-head.png/svg")


# ============================================================
# 图5: Pre-Norm vs Post-Norm
# ============================================================
def create_pre_post_norm():
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    for ax in axes:
        ax.set_xlim(0, 5)
        ax.set_ylim(0, 6)
        ax.axis('off')
        ax.set_facecolor(COLORS['bg'])
    fig.patch.set_facecolor(COLORS['bg'])

    # ---- Post-Norm (Original) ----
    ax = axes[0]
    ax.set_title('Post-Norm (Original)', fontsize=12, fontweight='bold', color=COLORS['decoder'], pad=10)

    cx = 2.5
    draw_rounded_box(ax, cx, 5.2, 0.8, 0.5, 'x', COLORS['input'], fontsize=11)

    # Sublayer
    draw_rounded_box(ax, cx, 4.0, 1.5, 0.5, 'Sublayer', COLORS['attention'], fontsize=9)
    draw_arrow(ax, (cx, 4.95), (cx, 4.25))

    # Residual 分支
    ax.annotate('', xy=(cx + 1.2, 3.2), xytext=(cx + 1.2, 5.2),
                arrowprops=dict(arrowstyle='-', color='#888', lw=1.5))
    ax.annotate('', xy=(cx + 0.3, 3.2), xytext=(cx + 1.2, 3.2),
                arrowprops=dict(arrowstyle='->', color='#888', lw=1.5))

    # Add
    draw_rounded_box(ax, cx, 3.0, 0.6, 0.5, '+', '#6B7280', fontsize=14)
    draw_arrow(ax, (cx, 3.75), (cx, 3.25))

    # LayerNorm
    draw_rounded_box(ax, cx, 2.0, 1.5, 0.5, 'LayerNorm', COLORS['norm'], text_color='#333', fontsize=9)
    draw_arrow(ax, (cx, 2.75), (cx, 2.25))

    # Output
    draw_rounded_box(ax, cx, 1.0, 1.0, 0.5, 'Output', COLORS['output'], fontsize=9)
    draw_arrow(ax, (cx, 1.75), (cx, 1.25))

    # ---- Pre-Norm (Later models) ----
    ax = axes[1]
    ax.set_title('Pre-Norm (GPT, LLaMA, ...)', fontsize=12, fontweight='bold', color=COLORS['encoder'], pad=10)

    draw_rounded_box(ax, cx, 5.2, 0.8, 0.5, 'x', COLORS['input'], fontsize=11)

    # LayerNorm first
    draw_rounded_box(ax, cx, 4.2, 1.5, 0.5, 'LayerNorm', COLORS['norm'], text_color='#333', fontsize=9)
    draw_arrow(ax, (cx, 4.95), (cx, 4.45))

    # Sublayer
    draw_rounded_box(ax, cx, 3.2, 1.5, 0.5, 'Sublayer', COLORS['attention'], fontsize=9)
    draw_arrow(ax, (cx, 3.95), (cx, 3.45))

    # Residual 分支 (从 x 直接到 +)
    ax.annotate('', xy=(cx + 1.2, 2.2), xytext=(cx + 1.2, 5.2),
                arrowprops=dict(arrowstyle='-', color='#888', lw=1.5))
    ax.annotate('', xy=(cx + 0.3, 2.2), xytext=(cx + 1.2, 2.2),
                arrowprops=dict(arrowstyle='->', color='#888', lw=1.5))

    # Add
    draw_rounded_box(ax, cx, 2.0, 0.6, 0.5, '+', '#6B7280', fontsize=14)
    draw_arrow(ax, (cx, 2.95), (cx, 2.25))

    # Output
    draw_rounded_box(ax, cx, 1.0, 1.0, 0.5, 'Output', COLORS['output'], fontsize=9)
    draw_arrow(ax, (cx, 1.75), (cx, 1.25))

    plt.tight_layout()
    plt.savefig('fig-pre-post-norm.png', dpi=150, bbox_inches='tight',
                facecolor=COLORS['bg'], edgecolor='none')
    plt.savefig('fig-pre-post-norm.svg', bbox_inches='tight',
                facecolor=COLORS['bg'], edgecolor='none')
    plt.close()
    print("[OK] Created: fig-pre-post-norm.png/svg")


# ============================================================
# 图6: Cross-Attention
# ============================================================
def create_cross_attention():
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 5)
    ax.axis('off')
    ax.set_facecolor(COLORS['bg'])
    fig.patch.set_facecolor(COLORS['bg'])

    # Encoder 输出
    enc_x = 2.5
    enc_bg = FancyBboxPatch((enc_x - 1.3, 1.5), 2.6, 2.5,
                            boxstyle="round,pad=0.05,rounding_size=0.2",
                            facecolor=COLORS['encoder'], alpha=0.15,
                            edgecolor=COLORS['encoder'], linewidth=1.5)
    ax.add_patch(enc_bg)
    ax.text(enc_x, 4.2, 'Encoder', ha='center', fontsize=11, fontweight='bold', color=COLORS['encoder'])

    draw_rounded_box(ax, enc_x, 2.8, 2.0, 0.6, 'Encoder Output', COLORS['encoder'], fontsize=9)

    # Decoder 状态
    dec_x = 6.5
    dec_bg = FancyBboxPatch((dec_x - 1.3, 1.5), 2.6, 2.5,
                            boxstyle="round,pad=0.05,rounding_size=0.2",
                            facecolor=COLORS['decoder'], alpha=0.15,
                            edgecolor=COLORS['decoder'], linewidth=1.5)
    ax.add_patch(dec_bg)
    ax.text(dec_x, 4.2, 'Decoder', ha='center', fontsize=11, fontweight='bold', color=COLORS['decoder'])

    draw_rounded_box(ax, dec_x, 2.8, 2.0, 0.6, 'Decoder State', COLORS['decoder'], fontsize=9)

    # Cross-Attention 框
    ca_y = 0.8
    draw_rounded_box(ax, 4.5, ca_y, 2.5, 0.7, 'Cross-Attention', COLORS['attention'], fontsize=10)

    # 箭头连接
    # Query 来自 Decoder
    ax.annotate('', xy=(5.3, ca_y + 0.35), xytext=(dec_x, 2.5),
                arrowprops=dict(arrowstyle='->', color=COLORS['decoder'], lw=2,
                               connectionstyle='arc3,rad=0.2'))
    ax.text(6.3, 1.6, 'Query', fontsize=9, color=COLORS['decoder'], fontweight='bold')

    # Key, Value 来自 Encoder
    ax.annotate('', xy=(3.7, ca_y + 0.35), xytext=(enc_x, 2.5),
                arrowprops=dict(arrowstyle='->', color=COLORS['encoder'], lw=2,
                               connectionstyle='arc3,rad=-0.2'))
    ax.text(2.0, 1.6, 'Key, Value', fontsize=9, color=COLORS['encoder'], fontweight='bold')

    plt.tight_layout()
    plt.savefig('fig-cross-attention.png', dpi=150, bbox_inches='tight',
                facecolor=COLORS['bg'], edgecolor='none')
    plt.savefig('fig-cross-attention.svg', bbox_inches='tight',
                facecolor=COLORS['bg'], edgecolor='none')
    plt.close()
    print("[OK] Created: fig-cross-attention.png/svg")


# ============================================================
# 主函数
# ============================================================
if __name__ == '__main__':
    print("Generating Transformer Chapter 8 figures...\n")

    create_rnn_seq2seq()
    create_transformer_overview()
    create_scaled_attention()
    create_multi_head()
    create_pre_post_norm()
    create_cross_attention()

    print("\n=== All figures generated successfully! ===")
    print("Files saved in current directory (PNG and SVG formats)")
