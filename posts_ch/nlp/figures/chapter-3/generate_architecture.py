"""
Generate Word2Vec Architecture Diagrams (CBOW and Skip-gram)
Style: Clean, Sebastian Raschka inspired
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Color palette (soft, professional)
COLORS = {
    'input': '#6C9BC2',       # Soft blue
    'hidden': '#7FB685',      # Soft green
    'output': '#E8A87C',      # Soft orange
    'projection': '#E8D07C', # Soft yellow
    'text': '#4A4A4A',        # Dark gray
    'arrow': '#888888',       # Medium gray
    'bg': '#FFFFFF',          # White
}

def draw_layer(ax, x, y, width, height, color, label, n_nodes=None):
    """Draw a neural network layer as a rounded rectangle"""
    box = FancyBboxPatch(
        (x - width/2, y - height/2), width, height,
        boxstyle="round,pad=0.02,rounding_size=0.1",
        facecolor=color, edgecolor='none', alpha=0.9
    )
    ax.add_patch(box)

    if n_nodes:
        # Draw nodes inside
        node_spacing = height / (n_nodes + 1)
        for i in range(n_nodes):
            node_y = y - height/2 + node_spacing * (i + 1)
            circle = plt.Circle((x, node_y), 0.08, color='white', ec=COLORS['text'], lw=1)
            ax.add_patch(circle)

    # Label
    ax.text(x, y - height/2 - 0.15, label, ha='center', va='top',
            fontsize=10, color=COLORS['text'], fontweight='bold')

def draw_arrow(ax, start, end, color=None):
    """Draw an arrow between two points"""
    if color is None:
        color = COLORS['arrow']
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5))

def draw_word_boxes(ax, x, y, words, vertical=True, box_width=0.6, box_height=0.25, spacing=0.35):
    """Draw word input/output boxes"""
    n = len(words)
    if vertical:
        total_height = n * box_height + (n-1) * (spacing - box_height)
        start_y = y + total_height / 2 - box_height / 2
        for i, word in enumerate(words):
            word_y = start_y - i * spacing
            box = FancyBboxPatch(
                (x - box_width/2, word_y - box_height/2), box_width, box_height,
                boxstyle="round,pad=0.02,rounding_size=0.05",
                facecolor=COLORS['input'], edgecolor='none', alpha=0.8
            )
            ax.add_patch(box)
            ax.text(x, word_y, word, ha='center', va='center',
                    fontsize=9, color='white', fontweight='bold')
    return x, y

def create_cbow_diagram():
    """Create CBOW architecture diagram"""
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-1, 3.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Title
    ax.text(2, 3.2, 'CBOW (Continuous Bag of Words)', ha='center', va='bottom',
            fontsize=14, fontweight='bold', color=COLORS['text'])

    # Input words (context)
    context_words = ['w(t-2)', 'w(t-1)', 'w(t+1)', 'w(t+2)']
    input_x = 0.5
    for i, word in enumerate(context_words):
        y = 2.2 - i * 0.6
        box = FancyBboxPatch(
            (input_x - 0.35, y - 0.15), 0.7, 0.3,
            boxstyle="round,pad=0.02,rounding_size=0.05",
            facecolor=COLORS['input'], edgecolor='none', alpha=0.9
        )
        ax.add_patch(box)
        ax.text(input_x, y, word, ha='center', va='center',
                fontsize=10, color='white', fontweight='bold')

    ax.text(input_x, -0.3, 'Input Layer\n(Context Words)', ha='center', va='top',
            fontsize=9, color=COLORS['text'])

    # Projection layer (sum/average)
    proj_x = 1.8
    proj_y = 1.3
    box = FancyBboxPatch(
        (proj_x - 0.4, proj_y - 0.5), 0.8, 1.0,
        boxstyle="round,pad=0.02,rounding_size=0.1",
        facecolor=COLORS['projection'], edgecolor='none', alpha=0.9
    )
    ax.add_patch(box)
    ax.text(proj_x, proj_y, 'SUM', ha='center', va='center',
            fontsize=11, color=COLORS['text'], fontweight='bold')
    ax.text(proj_x, proj_y - 0.7, 'Projection\n(Average)', ha='center', va='top',
            fontsize=9, color=COLORS['text'])

    # Arrows from input to projection
    for i in range(4):
        y = 2.2 - i * 0.6
        draw_arrow(ax, (input_x + 0.4, y), (proj_x - 0.45, proj_y))

    # Hidden layer
    hidden_x = 2.8
    hidden_y = 1.3
    box = FancyBboxPatch(
        (hidden_x - 0.3, hidden_y - 0.5), 0.6, 1.0,
        boxstyle="round,pad=0.02,rounding_size=0.1",
        facecolor=COLORS['hidden'], edgecolor='none', alpha=0.9
    )
    ax.add_patch(box)
    ax.text(hidden_x, hidden_y - 0.7, 'Hidden\nLayer', ha='center', va='top',
            fontsize=9, color=COLORS['text'])

    # Arrow from projection to hidden
    draw_arrow(ax, (proj_x + 0.45, proj_y), (hidden_x - 0.35, hidden_y))

    # Output layer
    output_x = 4
    output_y = 1.3
    box = FancyBboxPatch(
        (output_x - 0.35, output_y - 0.15), 0.7, 0.3,
        boxstyle="round,pad=0.02,rounding_size=0.05",
        facecolor=COLORS['output'], edgecolor='none', alpha=0.9
    )
    ax.add_patch(box)
    ax.text(output_x, output_y, 'w(t)', ha='center', va='center',
            fontsize=10, color='white', fontweight='bold')
    ax.text(output_x, output_y - 0.35, 'Output\n(Target Word)', ha='center', va='top',
            fontsize=9, color=COLORS['text'])

    # Arrow from hidden to output
    draw_arrow(ax, (hidden_x + 0.35, hidden_y), (output_x - 0.4, output_y))

    # Weight labels
    ax.text(1.15, 2.0, 'W', ha='center', va='center', fontsize=10,
            color=COLORS['text'], style='italic')
    ax.text(3.4, 1.6, "W'", ha='center', va='center', fontsize=10,
            color=COLORS['text'], style='italic')

    plt.tight_layout()
    return fig

def create_skipgram_diagram():
    """Create Skip-gram architecture diagram"""
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-1, 3.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Title
    ax.text(2, 3.2, 'Skip-gram', ha='center', va='bottom',
            fontsize=14, fontweight='bold', color=COLORS['text'])

    # Input word (center word)
    input_x = 0.5
    input_y = 1.3
    box = FancyBboxPatch(
        (input_x - 0.35, input_y - 0.15), 0.7, 0.3,
        boxstyle="round,pad=0.02,rounding_size=0.05",
        facecolor=COLORS['input'], edgecolor='none', alpha=0.9
    )
    ax.add_patch(box)
    ax.text(input_x, input_y, 'w(t)', ha='center', va='center',
            fontsize=10, color='white', fontweight='bold')
    ax.text(input_x, input_y - 0.35, 'Input\n(Center Word)', ha='center', va='top',
            fontsize=9, color=COLORS['text'])

    # Projection layer
    proj_x = 1.8
    proj_y = 1.3
    box = FancyBboxPatch(
        (proj_x - 0.3, proj_y - 0.5), 0.6, 1.0,
        boxstyle="round,pad=0.02,rounding_size=0.1",
        facecolor=COLORS['projection'], edgecolor='none', alpha=0.9
    )
    ax.add_patch(box)
    ax.text(proj_x, proj_y - 0.7, 'Projection\nLayer', ha='center', va='top',
            fontsize=9, color=COLORS['text'])

    # Arrow from input to projection
    draw_arrow(ax, (input_x + 0.4, input_y), (proj_x - 0.35, proj_y))

    # Hidden layer
    hidden_x = 2.8
    hidden_y = 1.3
    box = FancyBboxPatch(
        (hidden_x - 0.3, hidden_y - 0.5), 0.6, 1.0,
        boxstyle="round,pad=0.02,rounding_size=0.1",
        facecolor=COLORS['hidden'], edgecolor='none', alpha=0.9
    )
    ax.add_patch(box)
    ax.text(hidden_x, hidden_y - 0.7, 'Hidden\nLayer', ha='center', va='top',
            fontsize=9, color=COLORS['text'])

    # Arrow from projection to hidden
    draw_arrow(ax, (proj_x + 0.35, proj_y), (hidden_x - 0.35, hidden_y))

    # Output words (context)
    context_words = ['w(t-2)', 'w(t-1)', 'w(t+1)', 'w(t+2)']
    output_x = 4
    for i, word in enumerate(context_words):
        y = 2.2 - i * 0.6
        box = FancyBboxPatch(
            (output_x - 0.35, y - 0.15), 0.7, 0.3,
            boxstyle="round,pad=0.02,rounding_size=0.05",
            facecolor=COLORS['output'], edgecolor='none', alpha=0.9
        )
        ax.add_patch(box)
        ax.text(output_x, y, word, ha='center', va='center',
                fontsize=10, color='white', fontweight='bold')

        # Arrow from hidden to each output
        draw_arrow(ax, (hidden_x + 0.35, hidden_y), (output_x - 0.4, y))

    ax.text(output_x, -0.3, 'Output Layer\n(Context Words)', ha='center', va='top',
            fontsize=9, color=COLORS['text'])

    # Weight labels
    ax.text(1.15, 1.6, 'W', ha='center', va='center', fontsize=10,
            color=COLORS['text'], style='italic')
    ax.text(3.4, 2.0, "W'", ha='center', va='center', fontsize=10,
            color=COLORS['text'], style='italic')

    plt.tight_layout()
    return fig

def create_combined_diagram():
    """Create combined CBOW and Skip-gram comparison diagram"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    for ax in axes:
        ax.set_xlim(-0.5, 4.5)
        ax.set_ylim(-1, 3.5)
        ax.set_aspect('equal')
        ax.axis('off')

    # --- CBOW (left) ---
    ax = axes[0]
    ax.text(2, 3.2, 'CBOW', ha='center', va='bottom',
            fontsize=16, fontweight='bold', color=COLORS['text'])
    ax.text(2, 2.9, 'Predict center word from context', ha='center', va='top',
            fontsize=10, color='#666666', style='italic')

    # Input words
    context_words = ['w(t-2)', 'w(t-1)', 'w(t+1)', 'w(t+2)']
    input_x = 0.5
    for i, word in enumerate(context_words):
        y = 2.2 - i * 0.6
        box = FancyBboxPatch(
            (input_x - 0.35, y - 0.15), 0.7, 0.3,
            boxstyle="round,pad=0.02,rounding_size=0.05",
            facecolor=COLORS['input'], edgecolor='none', alpha=0.9
        )
        ax.add_patch(box)
        ax.text(input_x, y, word, ha='center', va='center',
                fontsize=9, color='white', fontweight='bold')
    ax.text(input_x, -0.2, 'Context', ha='center', va='top', fontsize=9, color=COLORS['text'])

    # Projection
    proj_x = 2
    proj_y = 1.3
    box = FancyBboxPatch(
        (proj_x - 0.35, proj_y - 0.4), 0.7, 0.8,
        boxstyle="round,pad=0.02,rounding_size=0.1",
        facecolor=COLORS['hidden'], edgecolor='none', alpha=0.9
    )
    ax.add_patch(box)
    ax.text(proj_x, proj_y, 'Hidden', ha='center', va='center',
            fontsize=9, color='white', fontweight='bold')

    for i in range(4):
        y = 2.2 - i * 0.6
        ax.annotate('', xy=(proj_x - 0.4, proj_y), xytext=(input_x + 0.4, y),
                    arrowprops=dict(arrowstyle='->', color=COLORS['arrow'], lw=1.2))

    # Output
    output_x = 3.5
    box = FancyBboxPatch(
        (output_x - 0.35, proj_y - 0.15), 0.7, 0.3,
        boxstyle="round,pad=0.02,rounding_size=0.05",
        facecolor=COLORS['output'], edgecolor='none', alpha=0.9
    )
    ax.add_patch(box)
    ax.text(output_x, proj_y, 'w(t)', ha='center', va='center',
            fontsize=9, color='white', fontweight='bold')
    ax.text(output_x, proj_y - 0.35, 'Target', ha='center', va='top', fontsize=9, color=COLORS['text'])

    ax.annotate('', xy=(output_x - 0.4, proj_y), xytext=(proj_x + 0.4, proj_y),
                arrowprops=dict(arrowstyle='->', color=COLORS['arrow'], lw=1.5))

    # --- Skip-gram (right) ---
    ax = axes[1]
    ax.text(2, 3.2, 'Skip-gram', ha='center', va='bottom',
            fontsize=16, fontweight='bold', color=COLORS['text'])
    ax.text(2, 2.9, 'Predict context from center word', ha='center', va='top',
            fontsize=10, color='#666666', style='italic')

    # Input word
    input_x = 0.5
    input_y = 1.3
    box = FancyBboxPatch(
        (input_x - 0.35, input_y - 0.15), 0.7, 0.3,
        boxstyle="round,pad=0.02,rounding_size=0.05",
        facecolor=COLORS['input'], edgecolor='none', alpha=0.9
    )
    ax.add_patch(box)
    ax.text(input_x, input_y, 'w(t)', ha='center', va='center',
            fontsize=9, color='white', fontweight='bold')
    ax.text(input_x, input_y - 0.35, 'Center', ha='center', va='top', fontsize=9, color=COLORS['text'])

    # Hidden
    proj_x = 2
    box = FancyBboxPatch(
        (proj_x - 0.35, input_y - 0.4), 0.7, 0.8,
        boxstyle="round,pad=0.02,rounding_size=0.1",
        facecolor=COLORS['hidden'], edgecolor='none', alpha=0.9
    )
    ax.add_patch(box)
    ax.text(proj_x, input_y, 'Hidden', ha='center', va='center',
            fontsize=9, color='white', fontweight='bold')

    ax.annotate('', xy=(proj_x - 0.4, input_y), xytext=(input_x + 0.4, input_y),
                arrowprops=dict(arrowstyle='->', color=COLORS['arrow'], lw=1.5))

    # Output words
    output_x = 3.5
    for i, word in enumerate(context_words):
        y = 2.2 - i * 0.6
        box = FancyBboxPatch(
            (output_x - 0.35, y - 0.15), 0.7, 0.3,
            boxstyle="round,pad=0.02,rounding_size=0.05",
            facecolor=COLORS['output'], edgecolor='none', alpha=0.9
        )
        ax.add_patch(box)
        ax.text(output_x, y, word, ha='center', va='center',
                fontsize=9, color='white', fontweight='bold')
        ax.annotate('', xy=(output_x - 0.4, y), xytext=(proj_x + 0.4, input_y),
                    arrowprops=dict(arrowstyle='->', color=COLORS['arrow'], lw=1.2))

    ax.text(output_x, -0.2, 'Context', ha='center', va='top', fontsize=9, color=COLORS['text'])

    plt.tight_layout()
    return fig

if __name__ == "__main__":
    import os

    output_dir = "."

    # Generate individual diagrams
    print("Generating CBOW diagram...")
    fig = create_cbow_diagram()
    fig.savefig(f"{output_dir}/fig1-cbow-architecture.png", dpi=200, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    fig.savefig(f"{output_dir}/fig1-cbow-architecture.svg", bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close(fig)
    print("  Saved: fig1-cbow-architecture.png/svg")

    print("Generating Skip-gram diagram...")
    fig = create_skipgram_diagram()
    fig.savefig(f"{output_dir}/fig2-skipgram-architecture.png", dpi=200, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    fig.savefig(f"{output_dir}/fig2-skipgram-architecture.svg", bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close(fig)
    print("  Saved: fig2-skipgram-architecture.png/svg")

    print("Generating combined comparison diagram...")
    fig = create_combined_diagram()
    fig.savefig(f"{output_dir}/fig3-cbow-vs-skipgram.png", dpi=200, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    fig.savefig(f"{output_dir}/fig3-cbow-vs-skipgram.svg", bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close(fig)
    print("  Saved: fig3-cbow-vs-skipgram.png/svg")

    print("\nAll diagrams generated successfully!")
