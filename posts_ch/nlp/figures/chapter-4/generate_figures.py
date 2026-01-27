"""
Generate figures for Chapter 3: Tokenization

Figure 1: BPE merge process visualization
Figure 2: Tokenization strategies comparison
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Sebastian Raschka style colors
COLORS = {
    'blue': '#6C9BC2',
    'orange': '#E8A87C',
    'green': '#7FB685',
    'yellow': '#E8D07C',
    'purple': '#B08FC7',
    'gray': '#A8B5C4',
    'text': '#4A4A4A',
    'white': '#FFFFFF',
    'light_gray': '#F5F5F5',
}

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 11


def draw_rounded_box(ax, x, y, width, height, color, text, fontsize=10, text_color='#4A4A4A'):
    """Draw a rounded rectangle with centered text"""
    box = FancyBboxPatch(
        (x - width/2, y - height/2), width, height,
        boxstyle="round,pad=0.02,rounding_size=0.1",
        facecolor=color, edgecolor='none',
        transform=ax.transData
    )
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            color=text_color, fontweight='medium')


def draw_arrow(ax, start, end, color='#A8B5C4'):
    """Draw an arrow from start to end"""
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5))


def create_bpe_merge_figure():
    """
    Create a visualization of the BPE merge process
    Shows how tokens are iteratively merged
    """
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.5, 'BPE Merge Process: Building Vocabulary',
            ha='center', va='center', fontsize=16, fontweight='bold', color=COLORS['text'])

    # Step labels on the left
    steps = [
        ('Step 0', 'Initial\n(characters)', 8.0),
        ('Step 1', 'Merge (e,s)\n→ "es"', 6.2),
        ('Step 2', 'Merge (es,t)\n→ "est"', 4.4),
        ('Step 3', 'Merge (l,o)\n→ "lo"', 2.6),
    ]

    for step_name, description, y in steps:
        ax.text(0.8, y, step_name, ha='center', va='center', fontsize=11,
                fontweight='bold', color=COLORS['text'])
        ax.text(0.8, y - 0.5, description, ha='center', va='center', fontsize=9,
                color=COLORS['gray'])

    # Token sequences at each step
    # Step 0: Initial characters
    tokens_step0 = [
        ('l', COLORS['blue']), ('o', COLORS['blue']), ('w', COLORS['blue']),
        ('e', COLORS['orange']), ('s', COLORS['orange']), ('t', COLORS['green']), ('_', COLORS['gray'])
    ]

    # Step 1: After merging (e,s)
    tokens_step1 = [
        ('l', COLORS['blue']), ('o', COLORS['blue']), ('w', COLORS['blue']),
        ('es', COLORS['orange']), ('t', COLORS['green']), ('_', COLORS['gray'])
    ]

    # Step 2: After merging (es,t)
    tokens_step2 = [
        ('l', COLORS['blue']), ('o', COLORS['blue']), ('w', COLORS['blue']),
        ('est', COLORS['yellow']), ('_', COLORS['gray'])
    ]

    # Step 3: After merging (l,o)
    tokens_step3 = [
        ('lo', COLORS['purple']), ('w', COLORS['blue']),
        ('est', COLORS['yellow']), ('_', COLORS['gray'])
    ]

    def draw_token_sequence(tokens, y_pos, start_x=3):
        x = start_x
        for token, color in tokens:
            width = 0.6 + len(token) * 0.3
            draw_rounded_box(ax, x, y_pos, width, 0.7, color, token, fontsize=12)
            x += width + 0.2
        return x

    # Draw all steps
    draw_token_sequence(tokens_step0, 8.0)
    draw_token_sequence(tokens_step1, 6.2)
    draw_token_sequence(tokens_step2, 4.4)
    draw_token_sequence(tokens_step3, 2.6)

    # Arrows between steps
    for y_start, y_end in [(7.5, 6.7), (5.7, 4.9), (3.9, 3.1)]:
        ax.annotate('', xy=(7, y_end), xytext=(7, y_start),
                    arrowprops=dict(arrowstyle='->', color=COLORS['gray'], lw=2))

    # Word being tokenized (right side)
    ax.text(11.5, 8.0, 'Word: "lowest"', ha='center', va='center',
            fontsize=12, fontweight='bold', color=COLORS['text'])

    # Vocabulary growth indicator
    vocab_info = [
        ('Vocab: 11', 8.0),
        ('Vocab: 12', 6.2),
        ('Vocab: 13', 4.4),
        ('Vocab: 14', 2.6),
    ]
    for text, y in vocab_info:
        ax.text(12.5, y, text, ha='center', va='center', fontsize=10,
                color=COLORS['gray'], style='italic')

    # Add merge frequency info
    freq_info = [
        ('freq(e,s) = 9', 7.1),
        ('freq(es,t) = 9', 5.3),
        ('freq(l,o) = 7', 3.5),
    ]
    for text, y in freq_info:
        ax.text(11, y, text, ha='center', va='center', fontsize=9,
                color=COLORS['text'],
                bbox=dict(boxstyle='round', facecolor=COLORS['light_gray'], edgecolor='none'))

    # Legend
    legend_items = [
        (COLORS['blue'], 'Original characters'),
        (COLORS['orange'], 'First merge'),
        (COLORS['yellow'], 'Second merge'),
        (COLORS['purple'], 'Third merge'),
    ]
    for i, (color, label) in enumerate(legend_items):
        ax.add_patch(FancyBboxPatch(
            (10, 1.2 - i * 0.4), 0.4, 0.25,
            boxstyle="round,pad=0.02,rounding_size=0.05",
            facecolor=color, edgecolor='none'
        ))
        ax.text(10.6, 1.32 - i * 0.4, label, ha='left', va='center',
                fontsize=9, color=COLORS['text'])

    plt.tight_layout()
    plt.savefig('fig-bpe-merge-process.png', dpi=200, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.savefig('fig-bpe-merge-process.svg', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print("[OK] Generated fig-bpe-merge-process.png/svg")
    plt.close()


def create_tokenization_strategies_figure():
    """
    Compare word-level, character-level, and subword tokenization
    """
    fig, axes = plt.subplots(3, 1, figsize=(12, 8))

    example_text = "tokenization"

    strategies = [
        ("Word-level", ["tokenization"], COLORS['blue']),
        ("Character-level", list("tokenization"), COLORS['orange']),
        ("Subword (BPE)", ["token", "ization"], COLORS['green']),
    ]

    for ax, (name, tokens, color) in zip(axes, strategies):
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 2)
        ax.axis('off')

        # Strategy name
        ax.text(0.5, 1, name, ha='left', va='center', fontsize=14,
                fontweight='bold', color=COLORS['text'])

        # Draw tokens
        x = 3
        for token in tokens:
            width = max(0.8, len(token) * 0.25)
            draw_rounded_box(ax, x, 1, width, 0.6, color, token, fontsize=10)
            x += width + 0.15

        # Token count
        ax.text(11, 1, f'{len(tokens)} token{"s" if len(tokens) > 1 else ""}',
                ha='right', va='center', fontsize=11, color=COLORS['gray'])

    plt.suptitle(f'Tokenization Strategies for "{example_text}"',
                 fontsize=16, fontweight='bold', y=0.98)

    plt.tight_layout()
    plt.savefig('fig-tokenization-strategies.png', dpi=200, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.savefig('fig-tokenization-strategies.svg', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print("[OK] Generated fig-tokenization-strategies.png/svg")
    plt.close()


def create_multilingual_efficiency_figure():
    """
    Show token efficiency across different languages
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    languages = ['English', 'Chinese', 'Japanese', 'Arabic', 'German']
    # Approximate token counts for "artificial intelligence" equivalent
    token_counts = [2, 5, 6, 9, 3]
    colors = [COLORS['blue'], COLORS['orange'], COLORS['green'],
              COLORS['purple'], COLORS['yellow']]

    bars = ax.barh(languages, token_counts, color=colors, height=0.6)

    # Add value labels
    for bar, count in zip(bars, token_counts):
        ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
                f'{count} tokens', va='center', fontsize=11, color=COLORS['text'])

    ax.set_xlabel('Number of Tokens', fontsize=12, color=COLORS['text'])
    ax.set_title('Token Efficiency: "Artificial Intelligence" Across Languages\n(GPT-2 Tokenizer)',
                 fontsize=14, fontweight='bold', color=COLORS['text'])
    ax.set_xlim(0, 12)

    # Remove spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(COLORS['gray'])
    ax.spines['bottom'].set_color(COLORS['gray'])
    ax.tick_params(colors=COLORS['text'])

    plt.tight_layout()
    plt.savefig('fig-multilingual-efficiency.png', dpi=200, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.savefig('fig-multilingual-efficiency.svg', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print("[OK] Generated fig-multilingual-efficiency.png/svg")
    plt.close()


if __name__ == "__main__":
    print("Generating Chapter 3 figures...")
    create_bpe_merge_figure()
    create_tokenization_strategies_figure()
    create_multilingual_efficiency_figure()
    print("Done!")
