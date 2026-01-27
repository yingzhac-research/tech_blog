"""
Generate a sinusoidal positional encoding heatmap for a Transformer textbook chapter.

PE(pos, 2i)   = sin(pos / 10000^(2i / d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i / d_model))
"""

import matplotlib
matplotlib.use("Agg")  # non-GUI backend

import matplotlib.pyplot as plt
import numpy as np

# -- Parameters --------------------------------------------------------------
max_pos = 101        # positions 0..100
d_model = 128        # embedding dimensions 0..127
output_path = r"C:\Users\yingz\Documents\tech_blog\posts_ch\nlp\figures\chapter-8\positional-encoding.png"

# -- Compute positional encoding matrix --------------------------------------
pe = np.zeros((d_model, max_pos))  # shape: (d_model, max_pos) for imshow

positions = np.arange(max_pos)              # (max_pos,)
dims = np.arange(0, d_model, 2)             # even indices: 0, 2, 4, ...

# Denominator: 10000^(2i / d_model) -- use log-space for numerical stability
div_term = np.exp(dims * -(np.log(10000.0) / d_model))  # (d_model/2,)

# Outer product gives (max_pos, d_model/2)
angles = positions[:, np.newaxis] * div_term[np.newaxis, :]

pe[0::2, :] = np.sin(angles).T   # even dims -> sin
pe[1::2, :] = np.cos(angles).T   # odd dims  -> cos

# -- Plot ---------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6))

im = ax.imshow(
    pe,
    aspect="auto",
    cmap="RdBu_r",        # red-white-blue diverging
    vmin=-1,
    vmax=1,
    origin="upper",
    interpolation="nearest",
)

# Colorbar
cbar = fig.colorbar(im, ax=ax, fraction=0.025, pad=0.02)
cbar.set_label("Value", fontsize=11)

# Labels & title
ax.set_title("Sinusoidal Positional Encoding", fontsize=15, fontweight="bold", pad=12)
ax.set_xlabel("Position", fontsize=12)
ax.set_ylabel("Dimension", fontsize=12)

# Tick marks -- show a reasonable subset
x_ticks = np.arange(0, max_pos, 10)
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_ticks)

y_ticks = np.arange(0, d_model, 16)
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_ticks)

# -- Frequency annotations ---------------------------------------------------
# "High frequency" near the top (low dimension indices)
ax.annotate(
    "High frequency",
    xy=(max_pos + 3, 10),
    xycoords="data",
    fontsize=10,
    fontstyle="italic",
    color="#333333",
    ha="left",
    va="center",
    annotation_clip=False,
)

# "Low frequency" near the bottom (high dimension indices)
ax.annotate(
    "Low frequency",
    xy=(max_pos + 3, d_model - 12),
    xycoords="data",
    fontsize=10,
    fontstyle="italic",
    color="#333333",
    ha="left",
    va="center",
    annotation_clip=False,
)

# Bracket-like lines connecting the labels to the axis edge
arrow_props = dict(arrowstyle="-", color="#555555", lw=0.8)
ax.annotate("", xy=(max_pos - 1, 0), xytext=(max_pos + 2, 10),
            arrowprops=arrow_props, annotation_clip=False)
ax.annotate("", xy=(max_pos - 1, 24), xytext=(max_pos + 2, 10),
            arrowprops=arrow_props, annotation_clip=False)

ax.annotate("", xy=(max_pos - 1, d_model - 24), xytext=(max_pos + 2, d_model - 12),
            arrowprops=arrow_props, annotation_clip=False)
ax.annotate("", xy=(max_pos - 1, d_model - 1), xytext=(max_pos + 2, d_model - 12),
            arrowprops=arrow_props, annotation_clip=False)

# -- Save --------------------------------------------------------------------
fig.tight_layout()
fig.savefig(output_path, dpi=200, bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"Saved: {output_path}")
