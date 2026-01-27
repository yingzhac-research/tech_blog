"""
Generate a synthetic attention visualization figure for a Transformer textbook chapter.
3 layers x 4 heads grid of 6x6 attention heatmaps for "The cat sat on the mat".
"""

import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.gridspec import GridSpec

# ── Sentence tokens ──────────────────────────────────────────────────────────
words = ["The", "cat", "sat", "on", "the", "mat"]
n = len(words)

def softmax_rows(M):
    """Apply softmax to each row so rows sum to ~1."""
    e = np.exp(M - M.max(axis=1, keepdims=True))
    return e / e.sum(axis=1, keepdims=True)

def make_base(val=0.0):
    return np.full((n, n), val)

# ── Layer 1: mostly local / positional patterns ─────────────────────────────

# Head 1 – strong self-attention (diagonal)
L1H1 = make_base(-2.0)
for i in range(n):
    L1H1[i, i] = 3.0
    if i > 0: L1H1[i, i-1] = 0.5
    if i < n-1: L1H1[i, i+1] = 0.5
L1H1 = softmax_rows(L1H1)

# Head 2 – attend to previous word (sub-diagonal)
L1H2 = make_base(-2.0)
for i in range(n):
    if i > 0:
        L1H2[i, i-1] = 3.0
    else:
        L1H2[i, i] = 3.0  # first word attends to self
    L1H2[i, i] += 0.8
L1H2 = softmax_rows(L1H2)

# Head 3 – attend to next word (super-diagonal)
L1H3 = make_base(-2.0)
for i in range(n):
    if i < n-1:
        L1H3[i, i+1] = 3.0
    else:
        L1H3[i, i] = 3.0  # last word attends to self
    L1H3[i, i] += 0.5
L1H3 = softmax_rows(L1H3)

# Head 4 – roughly uniform (broad attention)
L1H4 = make_base(0.0)
np.random.seed(42)
L1H4 += np.random.normal(0, 0.3, (n, n))
L1H4 = softmax_rows(L1H4)

# ── Layer 2: mix of local and emerging global ────────────────────────────────

# Indices: The=0, cat=1, sat=2, on=3, the=4, mat=5

# Head 1 – determiners attend to their nouns  ("The"->cat, "the"->mat)
L2H1 = make_base(-2.0)
L2H1[0, 1] = 3.5   # The -> cat
L2H1[4, 5] = 3.5   # the -> mat
# other words attend to themselves mildly
for i in [1, 2, 3, 5]:
    L2H1[i, i] = 1.5
L2H1 = softmax_rows(L2H1)

# Head 2 – verb attends to subject; subject attends to verb
L2H2 = make_base(-2.0)
L2H2[2, 1] = 3.5   # sat -> cat (verb->subject)
L2H2[1, 2] = 2.5   # cat -> sat (subject->verb)
for i in [0, 3, 4, 5]:
    L2H2[i, i] = 1.5
L2H2 = softmax_rows(L2H2)

# Head 3 – positional: attend to first and last positions
L2H3 = make_base(-1.5)
for i in range(n):
    L2H3[i, 0] += 2.0
    L2H3[i, n-1] += 2.0
    L2H3[i, i] += 0.8
L2H3 = softmax_rows(L2H3)

# Head 4 – mixed / transition
L2H4 = make_base(-1.0)
L2H4[0, 1] = 1.5;  L2H4[1, 0] = 1.0
L2H4[2, 3] = 1.5;  L2H4[3, 2] = 1.0
L2H4[3, 5] = 2.0;  L2H4[5, 3] = 1.5
for i in range(n):
    L2H4[i, i] += 0.8
L2H4 = softmax_rows(L2H4)

# ── Layer 3: global / syntactic patterns ─────────────────────────────────────

# Head 1 – subject<->verb  (cat<->sat)
L3H1 = make_base(-2.5)
L3H1[1, 2] = 4.0   # cat -> sat
L3H1[2, 1] = 4.0   # sat -> cat
L3H1[0, 1] = 1.5   # The -> cat
L3H1[4, 5] = 1.5   # the -> mat
for i in [0, 3, 4, 5]:
    L3H1[i, i] += 1.0
L3H1 = softmax_rows(L3H1)

# Head 2 – preposition<->object  (on<->mat, sat<->on)
L3H2 = make_base(-2.5)
L3H2[3, 5] = 4.0   # on -> mat
L3H2[5, 3] = 3.5   # mat -> on
L3H2[2, 3] = 2.5   # sat -> on
L3H2[3, 2] = 1.5   # on -> sat
for i in [0, 1, 4]:
    L3H2[i, i] += 1.0
L3H2 = softmax_rows(L3H2)

# Head 3 – determiner->noun  (The->cat, the->mat) strong
L3H3 = make_base(-3.0)
L3H3[0, 1] = 4.5   # The -> cat
L3H3[4, 5] = 4.5   # the -> mat
L3H3[1, 0] = 2.0   # cat -> The
L3H3[5, 4] = 2.0   # mat -> the
for i in [2, 3]:
    L3H3[i, i] += 1.5
L3H3 = softmax_rows(L3H3)

# Head 4 – broad context, slight emphasis on content words (cat, sat, mat)
L3H4 = make_base(0.0)
content_idx = [1, 2, 5]  # cat, sat, mat
for i in range(n):
    for j in content_idx:
        L3H4[i, j] += 1.0
    L3H4[i, i] += 0.3
L3H4 += np.random.normal(0, 0.15, (n, n))
L3H4 = softmax_rows(L3H4)

# ── Collect all heads ────────────────────────────────────────────────────────
all_heads = [
    [L1H1, L1H2, L1H3, L1H4],
    [L2H1, L2H2, L2H3, L2H4],
    [L3H1, L3H2, L3H3, L3H4],
]

# ── Annotation map  (layer, head) -> annotation text ────────────────────────
annotations = {
    (0, 1): "Positional Head",   # Layer 1, Head 2 (previous-word pattern)
    (2, 0): "Syntactic Head",    # Layer 3, Head 1 (subject-verb)
}

# ── Plotting ─────────────────────────────────────────────────────────────────
cmap = mcolors.LinearSegmentedColormap.from_list(
    "white_darkblue", ["#ffffff", "#08306b"]
)

fig = plt.figure(figsize=(16, 10), dpi=200)
fig.patch.set_facecolor("white")

# Title
fig.suptitle(
    "Attention Patterns across Layers and Heads",
    fontsize=18, fontweight="bold", y=0.97
)

# Outer grid: 3 rows x 4 cols with generous spacing
gs = GridSpec(
    3, 4,
    left=0.06, right=0.92, top=0.89, bottom=0.06,
    wspace=0.45, hspace=0.50,
)

for layer_idx in range(3):
    for head_idx in range(4):
        ax = fig.add_subplot(gs[layer_idx, head_idx])
        mat = all_heads[layer_idx][head_idx]

        im = ax.imshow(mat, cmap=cmap, vmin=0, vmax=1, aspect="equal")

        # Tick labels
        ax.set_xticks(range(n))
        ax.set_xticklabels(words, fontsize=7, rotation=45, ha="right")
        ax.set_yticks(range(n))
        ax.set_yticklabels(words, fontsize=7)

        # Subplot title
        title_text = f"Layer {layer_idx+1}, Head {head_idx+1}"
        ax.set_title(title_text, fontsize=9, fontweight="semibold", pad=6)

        # Optional annotation badge
        if (layer_idx, head_idx) in annotations:
            label = annotations[(layer_idx, head_idx)]
            bbox_color = "#d62728" if "Syntactic" in label else "#1f77b4"
            ax.annotate(
                label,
                xy=(0.5, -0.22), xycoords="axes fraction",
                ha="center", va="top",
                fontsize=7, fontweight="bold", color="white",
                bbox=dict(
                    boxstyle="round,pad=0.25",
                    facecolor=bbox_color, edgecolor="none", alpha=0.9
                ),
            )

        # Light grid lines
        for edge in range(n + 1):
            ax.axhline(edge - 0.5, color="grey", linewidth=0.3, alpha=0.5)
            ax.axvline(edge - 0.5, color="grey", linewidth=0.3, alpha=0.5)

        ax.tick_params(length=0)

# Row labels on the left margin
for layer_idx in range(3):
    fig.text(
        0.01, 0.78 - layer_idx * 0.295,
        f"Layer {layer_idx+1}",
        fontsize=12, fontweight="bold", rotation=90,
        ha="center", va="center",
    )

# Shared colour bar
cbar_ax = fig.add_axes([0.94, 0.15, 0.015, 0.65])
cbar = fig.colorbar(
    plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(0, 1)),
    cax=cbar_ax
)
cbar.set_label("Attention Weight", fontsize=10)
cbar.ax.tick_params(labelsize=8)

# ── Save ─────────────────────────────────────────────────────────────────────
out_path = r"C:\Users\yingz\Documents\tech_blog\posts_ch\nlp\figures\chapter-8\attention-visualization.png"
fig.savefig(out_path, dpi=200, bbox_inches="tight", facecolor="white")
plt.close(fig)
print(f"Saved: {out_path}")
