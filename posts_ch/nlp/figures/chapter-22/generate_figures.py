"""
Chapter 22: Evaluation Methodology — Figure Generation
生成评测方法论演进时间线图

Style: Sebastian Raschka 风格 — 干净、留白、柔和配色、无边框
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# 配色方案
COLORS = {
    'auto_metric': '#6C9BC2',    # 柔和蓝 (自动指标)
    'benchmark': '#7FB685',       # 柔和绿 (静态benchmark)
    'generative': '#E8A87C',      # 柔和橙 (生成式评测)
    'contamination': '#C27C7C',   # 柔和红 (数据污染)
    'text': '#4A4A4A',            # 深灰文字
    'bg': '#FAFAFA',              # 浅灰背景
    'line': '#CCCCCC',            # 浅灰线条
}

def create_evaluation_timeline():
    """创建评测方法论演进时间线"""
    fig, ax = plt.subplots(1, 1, figsize=(16, 8))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    # 时间轴
    years = range(2002, 2025)
    ax.axhline(y=0, xmin=0.02, xmax=0.98, color=COLORS['line'], linewidth=2, zorder=1)

    # 年份刻度
    for year in [2002, 2004, 2014, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]:
        ax.plot(year, 0, 'o', color=COLORS['line'], markersize=4, zorder=2)
        ax.text(year, -0.25, str(year), ha='center', va='top',
                fontsize=9, color=COLORS['text'])

    # 事件定义: (year, y_offset, label, color, description)
    events = [
        # 第一代：自动指标
        (2002, 1.5, 'BLEU', COLORS['auto_metric'],
         'Papineni et al.\nn-gram precision'),
        (2004, 1.0, 'ROUGE', COLORS['auto_metric'],
         'Lin\nRecall-oriented'),

        # 过渡
        (2014, 0.8, 'Word2Vec\nevals', COLORS['auto_metric'],
         'Analogy tasks'),

        # 第二代：理解能力benchmark
        (2018, 2.0, 'GLUE', COLORS['benchmark'],
         'Wang et al.\n9 NLU tasks'),
        (2019, 1.5, 'SuperGLUE', COLORS['benchmark'],
         'Wang et al.\n8 harder tasks'),
        (2020, 2.5, 'MMLU', COLORS['benchmark'],
         'Hendrycks et al.\n57 subjects'),
        (2020, 1.2, 'BERTScore', COLORS['auto_metric'],
         'Zhang et al.\nSemantic similarity'),
        (2021, 1.8, 'TruthfulQA', COLORS['contamination'],
         'Lin et al.\nHallucination eval'),
        (2022, 2.8, 'HELM', COLORS['benchmark'],
         'Liang et al.\n7 scenarios × 7 metrics'),
        (2022, 1.5, 'BIG-bench', COLORS['benchmark'],
         'Srivastava et al.\n204 tasks'),

        # 第三代：生成式评测
        (2023, 2.2, 'MT-Bench', COLORS['generative'],
         'Zheng et al.\nLLM-as-Judge'),
        (2023, 3.0, 'Chatbot\nArena', COLORS['generative'],
         'LMSYS\nElo rating'),
        (2023, 0.8, 'Schaeffer\net al.', COLORS['contamination'],
         'Emergent abilities\n= mirage?'),
    ]

    for year, y, label, color, desc in events:
        # 连接线
        ax.plot([year, year], [0.1, y - 0.15], color=color, linewidth=1.5,
                alpha=0.6, zorder=2)
        # 标记点
        ax.plot(year, 0, 'o', color=color, markersize=8, zorder=3)
        # 标签框
        bbox_props = dict(boxstyle="round,pad=0.3", facecolor=color,
                         edgecolor='none', alpha=0.15)
        ax.text(year, y, label, ha='center', va='center',
                fontsize=10, fontweight='bold', color=color,
                bbox=bbox_props, zorder=4)
        # 描述文字
        ax.text(year, y - 0.35, desc, ha='center', va='top',
                fontsize=7.5, color=COLORS['text'], style='italic',
                zorder=4)

    # 时代标注（底部）
    era_spans = [
        (2001, 2016, 'Era 1: Automatic Metrics', COLORS['auto_metric']),
        (2017.5, 2022.2, 'Era 2: Understanding Benchmarks', COLORS['benchmark']),
        (2022.5, 2024.5, 'Era 3: Generative\nEvaluation', COLORS['generative']),
    ]

    for x1, x2, label, color in era_spans:
        ax.annotate('', xy=(x2, -0.7), xytext=(x1, -0.7),
                    arrowprops=dict(arrowstyle='<->', color=color,
                                   linewidth=2))
        ax.text((x1 + x2) / 2, -1.0, label, ha='center', va='top',
                fontsize=9, color=color, fontweight='bold')

    # 图例
    legend_elements = [
        mpatches.Patch(facecolor=COLORS['auto_metric'], alpha=0.5,
                      label='Automatic Metrics'),
        mpatches.Patch(facecolor=COLORS['benchmark'], alpha=0.5,
                      label='Static Benchmarks'),
        mpatches.Patch(facecolor=COLORS['generative'], alpha=0.5,
                      label='Generative Evaluation'),
        mpatches.Patch(facecolor=COLORS['contamination'], alpha=0.5,
                      label='Reliability / Contamination'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=9,
             frameon=False)

    # 标题
    ax.set_title('Evolution of NLP Evaluation Methodology (2002–2024)',
                fontsize=14, fontweight='bold', color=COLORS['text'],
                pad=20)

    # 清理坐标轴
    ax.set_xlim(2000, 2025)
    ax.set_ylim(-1.3, 3.5)
    ax.axis('off')

    plt.tight_layout()
    return fig


def create_goodhart_cycle():
    """创建 Goodhart 定律循环图"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    # 四个阶段的位置（圆形排列）
    positions = {
        'publish': (0.2, 0.75),
        'optimize': (0.8, 0.75),
        'saturate': (0.8, 0.25),
        'obsolete': (0.2, 0.25),
    }

    labels = {
        'publish': 'Benchmark\nPublished',
        'optimize': 'Community\nOptimizes',
        'saturate': 'Scores\nSaturate',
        'obsolete': 'Benchmark\nObsolete',
    }

    examples = {
        'publish': 'GLUE (2018)',
        'optimize': 'BERT (2018)\nRoBERTa (2019)',
        'saturate': 'Human-level\n(2020)',
        'obsolete': '→ SuperGLUE\n→ MMLU',
    }

    colors_cycle = [COLORS['benchmark'], COLORS['auto_metric'],
                    COLORS['contamination'], COLORS['generative']]

    # 绘制节点
    for i, (key, (x, y)) in enumerate(positions.items()):
        box = FancyBboxPatch((x - 0.12, y - 0.1), 0.24, 0.2,
                             boxstyle="round,pad=0.02,rounding_size=0.03",
                             facecolor=colors_cycle[i], edgecolor='none',
                             alpha=0.2, transform=ax.transAxes)
        ax.add_patch(box)
        ax.text(x, y + 0.02, labels[key], ha='center', va='center',
                fontsize=11, fontweight='bold', color=colors_cycle[i],
                transform=ax.transAxes)
        ax.text(x, y - 0.13, examples[key], ha='center', va='top',
                fontsize=8, color=COLORS['text'], style='italic',
                transform=ax.transAxes)

    # 绘制箭头
    arrow_props = dict(arrowstyle='->', color=COLORS['text'],
                      linewidth=2, connectionstyle="arc3,rad=0.1")
    pairs = [('publish', 'optimize'), ('optimize', 'saturate'),
             ('saturate', 'obsolete'), ('obsolete', 'publish')]

    for start, end in pairs:
        x1, y1 = positions[start]
        x2, y2 = positions[end]
        # 偏移到边缘
        dx = (x2 - x1) * 0.3
        dy = (y2 - y1) * 0.3
        ax.annotate('', xy=(x2 - dx * 0.5, y2 - dy * 0.5),
                    xytext=(x1 + dx * 0.5, y1 + dy * 0.5),
                    arrowprops=arrow_props, xycoords='axes fraction',
                    textcoords='axes fraction')

    # 中心标注
    ax.text(0.5, 0.5, "Goodhart's\nLaw", ha='center', va='center',
            fontsize=14, fontweight='bold', color=COLORS['text'],
            alpha=0.4, transform=ax.transAxes)

    ax.set_title("The Goodhart Cycle in NLP Evaluation",
                fontsize=14, fontweight='bold', color=COLORS['text'])
    ax.axis('off')
    plt.tight_layout()
    return fig


if __name__ == "__main__":
    # 生成时间线图
    fig1 = create_evaluation_timeline()
    fig1.savefig('figures/chapter-22/original/fig1-evaluation-timeline.png',
                dpi=200, bbox_inches='tight', facecolor='white')
    fig1.savefig('figures/chapter-22/original/fig1-evaluation-timeline.svg',
                bbox_inches='tight', facecolor='white')
    print("[OK] fig1-evaluation-timeline")

    # 生成 Goodhart 循环图
    fig2 = create_goodhart_cycle()
    fig2.savefig('figures/chapter-22/original/fig2-goodhart-cycle.png',
                dpi=200, bbox_inches='tight', facecolor='white')
    fig2.savefig('figures/chapter-22/original/fig2-goodhart-cycle.svg',
                bbox_inches='tight', facecolor='white')
    print("[OK] fig2-goodhart-cycle")

    plt.close('all')
    print("\nAll figures generated successfully!")
