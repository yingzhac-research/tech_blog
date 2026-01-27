"""
Chapter 9: Efficient Attention — Custom Figures
Sebastian Raschka 风格：干净、留白、柔和配色、无边框

生成以下图片：
1. fig-attention-patterns.png — 4种注意力模式对比（Full, Sliding Window, Dilated, Global+Sliding）
2. fig-linear-attention-order.png — 线性注意力的计算顺序对比
3. fig-complexity-comparison.png — O(n²) vs O(n) 复杂度增长曲线
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# ============================================================
# 风格配置 - Raschka Style (与 chapter-8 保持一致)
# ============================================================

COLORS = {
    # 主色调
    'blue': '#6C9BC2',
    'green': '#7FB685',
    'orange': '#E8A87C',
    'purple': '#9B8DC2',
    'red': '#D4817A',
    'yellow': '#E8D07C',
    'gray': '#A8B5C4',

    # 功能色
    'local': '#6C9BC2',       # 蓝色 — 局部窗口
    'global': '#E8A87C',      # 橙色 — 全局注意力
    'random': '#7FB685',      # 绿色 — 随机连接
    'dilated': '#9B8DC2',     # 紫色 — 扩张窗口
    'full': '#D4817A',        # 红色 — 全注意力
    'inactive': '#F0F0F0',    # 淡灰 — 无注意力

    # 基础色
    'text': '#4A4A4A',
    'text_light': '#FFFFFF',
    'arrow': '#7A7A7A',
    'bg': '#FFFFFF',
}

plt.rcParams.update({
    'font.family': ['Arial', 'DejaVu Sans'],
    'font.size': 10,
    'font.weight': 'normal',
    'axes.unicode_minus': False,
    'figure.facecolor': COLORS['bg'],
    'axes.facecolor': COLORS['bg'],
    'savefig.facecolor': COLORS['bg'],
    'savefig.edgecolor': 'none',
})


# ============================================================
# 图1: 四种注意力模式对比
# ============================================================
def create_attention_patterns():
    """
    4-panel figure: Full, Sliding Window, Dilated, Global+Sliding
    Each panel is an 8x8 attention matrix heatmap
    """
    n = 12  # matrix size
    fig, axes = plt.subplots(1, 4, figsize=(14, 3.8))

    titles = [
        '(a) Full Attention\n$O(n^2)$',
        '(b) Sliding Window\n$O(n \\times w)$',
        '(c) Dilated Sliding Window\n$O(n \\times w)$',
        '(d) Global + Sliding\n$O(n \\times w)$',
    ]

    def make_full(n):
        return np.ones((n, n))

    def make_sliding(n, w=3):
        """Sliding window: each token attends to w neighbors on each side"""
        m = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if abs(i - j) <= w:
                    m[i, j] = 1
        return m

    def make_dilated(n, w=2, dilation=2):
        """Dilated sliding window"""
        m = np.zeros((n, n))
        for i in range(n):
            # Dense local window
            for j in range(max(0, i - w), min(n, i + w + 1)):
                m[i, j] = 1
            # Dilated positions
            for k in range(1, w + 2):
                j_up = i + k * dilation
                j_down = i - k * dilation
                if 0 <= j_up < n:
                    m[i, j_up] = 1
                if 0 <= j_down < n:
                    m[i, j_down] = 1
        return m

    def make_global_sliding(n, w=3, global_indices=[0, 1]):
        """Global tokens + sliding window"""
        m = make_sliding(n, w)
        for g in global_indices:
            m[g, :] = 1   # global token attends to all
            m[:, g] = 1   # all attend to global token
        return m

    matrices = [
        make_full(n),
        make_sliding(n, w=2),
        make_dilated(n, w=1, dilation=3),
        make_global_sliding(n, w=2, global_indices=[0, 1]),
    ]

    # Color maps for each pattern
    for ax, mat, title in zip(axes, matrices, titles):
        # Create colored matrix
        colored = np.zeros((*mat.shape, 3))
        for i in range(n):
            for j in range(n):
                if mat[i, j] == 1:
                    # Different colors for different pattern types
                    if title.startswith('(a)'):
                        colored[i, j] = [0.42, 0.61, 0.76]  # blue
                    elif title.startswith('(b)'):
                        colored[i, j] = [0.42, 0.61, 0.76]  # blue for local
                    elif title.startswith('(c)'):
                        colored[i, j] = [0.61, 0.55, 0.76]  # purple for dilated
                    else:
                        # global+sliding: distinguish global vs local
                        if i <= 1 or j <= 1:
                            colored[i, j] = [0.91, 0.66, 0.49]  # orange for global
                        else:
                            colored[i, j] = [0.42, 0.61, 0.76]  # blue for local
                else:
                    colored[i, j] = [0.94, 0.94, 0.94]  # light gray

        ax.imshow(colored, aspect='equal', interpolation='nearest')

        # Grid lines
        for k in range(n + 1):
            ax.axhline(k - 0.5, color='white', lw=0.8)
            ax.axvline(k - 0.5, color='white', lw=0.8)

        ax.set_title(title, fontsize=10, fontweight='medium', color=COLORS['text'],
                     pad=8, linespacing=1.4)
        ax.set_xticks([])
        ax.set_yticks([])

        # Remove spines
        for spine in ax.spines.values():
            spine.set_visible(False)

    # Add axis labels
    axes[0].set_ylabel('Query position', fontsize=9, color=COLORS['text'])
    fig.text(0.5, 0.02, 'Key position', ha='center', fontsize=9, color=COLORS['text'])

    # Compute sparsity stats
    for ax, mat, title in zip(axes, matrices, titles):
        total = n * n
        active = int(mat.sum())
        pct = active / total * 100
        ax.text(n/2 - 0.5, n + 0.8, f'{active}/{total} ({pct:.0f}%)',
                ha='center', va='top', fontsize=8, color=COLORS['arrow'])

    plt.tight_layout(pad=1.0)
    plt.subplots_adjust(bottom=0.1)
    plt.savefig('fig-attention-patterns.png', dpi=200, bbox_inches='tight')
    plt.savefig('fig-attention-patterns.svg', bbox_inches='tight')
    plt.close()
    print("[OK] fig-attention-patterns")


# ============================================================
# 图2: 线性注意力计算顺序对比
# ============================================================
def create_linear_attention_order():
    """
    Shows the key insight of linear attention:
    Standard: (Q K^T) V — computes n×n matrix first
    Linear:   Q (K^T V) — computes d×d matrix first
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

    for ax in axes:
        ax.set_xlim(0, 6)
        ax.set_ylim(0, 5)
        ax.axis('off')
        ax.set_aspect('equal')

    def draw_matrix(ax, x, y, w, h, color, label, dim_label='', alpha=0.85):
        """Draw a matrix as a colored rectangle"""
        rect = FancyBboxPatch(
            (x - w/2, y - h/2), w, h,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor=color, edgecolor='none', alpha=alpha, zorder=2
        )
        ax.add_patch(rect)
        text_color = '#FFFFFF' if color in [COLORS['blue'], COLORS['red'], COLORS['green'],
                                            COLORS['purple']] else COLORS['text']
        ax.text(x, y, label, ha='center', va='center', fontsize=10,
                fontweight='medium', color=text_color, zorder=3)
        if dim_label:
            ax.text(x, y - h/2 - 0.18, dim_label, ha='center', va='top',
                    fontsize=7, color=COLORS['arrow'])

    def draw_op(ax, x, y, text, fontsize=14):
        ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
                color=COLORS['arrow'], fontweight='bold', zorder=3)

    # ===== Left panel: Standard Attention =====
    ax = axes[0]
    ax.set_title('Standard Attention: $(QK^\\top)V$', fontsize=11,
                 fontweight='bold', color=COLORS['red'], pad=12)

    # Step 1: Q × K^T → n×n matrix
    # Q
    draw_matrix(ax, 0.8, 3.5, 0.5, 1.4, COLORS['blue'], 'Q', 'n×d')
    draw_op(ax, 1.3, 3.5, '×')
    # K^T
    draw_matrix(ax, 2.0, 3.5, 1.1, 0.5, COLORS['blue'], 'K$^\\top$', 'd×n')

    # Arrow
    ax.annotate('', xy=(3.0, 2.3), xytext=(1.5, 2.9),
                arrowprops=dict(arrowstyle='->', color=COLORS['arrow'], lw=1.2))

    # = n×n matrix (big, highlighted as bottleneck)
    draw_matrix(ax, 3.0, 1.8, 1.4, 1.4, COLORS['red'], 'n×n', '')
    ax.text(3.0, 0.85, '⚠ bottleneck!', ha='center', fontsize=8,
            color=COLORS['red'], style='italic')

    draw_op(ax, 4.05, 1.8, '×')

    # V
    draw_matrix(ax, 4.7, 1.8, 0.5, 1.4, COLORS['green'], 'V', 'n×d')

    # = Output
    draw_op(ax, 5.2, 1.8, '=')
    draw_matrix(ax, 5.65, 1.8, 0.45, 1.4, COLORS['purple'], 'O', 'n×d')

    # Complexity
    ax.text(3.0, 0.35, 'Complexity: $O(n^2 d)$', ha='center', fontsize=10,
            color=COLORS['red'], fontweight='bold')

    # ===== Right panel: Linear Attention =====
    ax = axes[1]
    ax.set_title('Linear Attention: $\\phi(Q)(\\phi(K)^\\top V)$', fontsize=11,
                 fontweight='bold', color=COLORS['green'], pad=12)

    # Step 1: K^T × V → d×d matrix (small!)
    # K^T
    draw_matrix(ax, 1.0, 3.5, 1.1, 0.5, COLORS['blue'], '$\\phi(K)^\\top$', 'd×n')
    draw_op(ax, 1.85, 3.5, '×')
    # V
    draw_matrix(ax, 2.4, 3.5, 0.5, 1.1, COLORS['green'], 'V', 'n×d')

    # Arrow
    ax.annotate('', xy=(3.3, 2.5), xytext=(2.0, 2.9),
                arrowprops=dict(arrowstyle='->', color=COLORS['arrow'], lw=1.2))

    # = d×d matrix (small, highlighted as efficient)
    draw_matrix(ax, 3.5, 1.8, 0.7, 0.7, COLORS['green'], 'd×d', '')
    ax.text(3.5, 1.15, '✓ small!', ha='center', fontsize=8,
            color=COLORS['green'], style='italic')

    # φ(Q) ×
    draw_matrix(ax, 1.2, 1.8, 0.5, 1.4, COLORS['blue'], '$\\phi(Q)$', 'n×d')
    draw_op(ax, 1.85, 1.8, '×')

    # Bracket around d×d
    # Arrow from φ(Q) to d×d
    ax.annotate('', xy=(3.1, 1.8), xytext=(1.55, 1.8),
                arrowprops=dict(arrowstyle='->', color=COLORS['arrow'], lw=0.8,
                                connectionstyle='arc3,rad=0'))

    # = Output
    draw_op(ax, 4.3, 1.8, '=')
    draw_matrix(ax, 4.8, 1.8, 0.45, 1.4, COLORS['purple'], 'O', 'n×d')

    # Complexity
    ax.text(3.0, 0.35, 'Complexity: $O(n d^2)$', ha='center', fontsize=10,
            color=COLORS['green'], fontweight='bold')

    plt.tight_layout(pad=1.5)
    plt.savefig('fig-linear-attention-order.png', dpi=200, bbox_inches='tight')
    plt.savefig('fig-linear-attention-order.svg', bbox_inches='tight')
    plt.close()
    print("[OK] fig-linear-attention-order")


# ============================================================
# 图3: 复杂度增长曲线
# ============================================================
def create_complexity_comparison():
    """
    O(n²) vs O(n·w) vs O(n·d) growth curves
    """
    fig, ax = plt.subplots(figsize=(8, 5))

    n = np.linspace(100, 100000, 500)

    # Different methods
    d = 64    # head dimension
    w = 256   # window size
    k = 128   # projection dim for Linformer
    m = 128   # random features for Performer

    methods = {
        'Full Attention $O(n^2 d)$': n**2 * d,
        'Longformer $O(n \\cdot w)$': n * w * d,
        'Linformer $O(n \\cdot k)$': n * k * d,
        'Linear Attention $O(n \\cdot d^2)$': n * d**2,
    }

    colors_list = [COLORS['red'], COLORS['blue'], COLORS['orange'], COLORS['green']]
    linestyles = ['-', '-', '--', '-']
    linewidths = [2.5, 2, 1.8, 2]

    for (label, values), color, ls, lw in zip(methods.items(), colors_list, linestyles, linewidths):
        ax.plot(n / 1000, values / 1e9, label=label, color=color, lw=lw, ls=ls)

    # Styling
    ax.set_xlabel('Sequence length $n$ (thousands)', fontsize=11, color=COLORS['text'])
    ax.set_ylabel('FLOPs (billions)', fontsize=11, color=COLORS['text'])
    ax.set_title('Computational Cost vs. Sequence Length', fontsize=13,
                 fontweight='bold', color=COLORS['text'], pad=15)

    # Set log scale for better visualization
    ax.set_yscale('log')
    ax.set_xscale('log')

    # Grid
    ax.grid(True, alpha=0.3, linestyle='-', color=COLORS['gray'])
    ax.set_axisbelow(True)

    # Legend
    legend = ax.legend(loc='upper left', fontsize=9, framealpha=0.9,
                       edgecolor='none', fancybox=True)
    legend.get_frame().set_facecolor('#F8F9FA')

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(COLORS['gray'])
    ax.spines['bottom'].set_color(COLORS['gray'])

    # Tick styling
    ax.tick_params(colors=COLORS['text'], which='both')

    # Add annotation for the crossover point region
    ax.annotate('Full attention\nbecomes prohibitive',
                xy=(10, 1e3), fontsize=8, color=COLORS['red'],
                ha='center', style='italic', alpha=0.8)

    ax.annotate('Linear methods\nstay manageable',
                xy=(50, 2), fontsize=8, color=COLORS['green'],
                ha='center', style='italic', alpha=0.8)

    plt.tight_layout(pad=1.0)
    plt.savefig('fig-complexity-comparison.png', dpi=200, bbox_inches='tight')
    plt.savefig('fig-complexity-comparison.svg', bbox_inches='tight')
    plt.close()
    print("[OK] fig-complexity-comparison")


# ============================================================
# 主函数
# ============================================================
if __name__ == '__main__':
    print("Generating Chapter 9 figures (Raschka style)...\n")

    create_attention_patterns()
    create_linear_attention_order()
    create_complexity_comparison()

    print("\n=== All figures generated! ===")
