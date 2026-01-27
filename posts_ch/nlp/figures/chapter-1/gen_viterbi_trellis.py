import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

words = ['fish', 'can', 'swim']
states = ['N', 'V']
state_labels = ['N (\u540d\u8bcd)', 'V (\u52a8\u8bcd)']

delta = {
    (0, 0): 0.24,
    (0, 1): 0.04,
    (1, 0): 0.0216,
    (1, 1): 0.0336,
    (2, 0): 0.002688,
    (2, 1): 0.00756,
}

optimal_path = [0, 0, 1]

trans = {(0,0): 0.3, (0,1): 0.7, (1,0): 0.8, (1,1): 0.2}

emission = {
    (0,'fish'):0.4, (1,'fish'):0.1,
    (0,'can'):0.3,  (1,'can'):0.2,
    (0,'swim'):0.1, (1,'swim'):0.5,
}

initial = {0: 0.6, 1: 0.4}

fig, ax = plt.subplots(figsize=(12, 6), dpi=200)
ax.set_xlim(-0.5, 4.5)
ax.set_ylim(-1.8, 2.5)
ax.set_aspect('equal')
ax.axis('off')

x_positions = [1.0, 2.5, 4.0]
y_positions = [1.2, 0.0]
node_radius = 0.32

COLOR_OPTIMAL = '#E67E22'
COLOR_OPTIMAL_FILL = '#FDEBD0'
COLOR_GRAY = '#CCCCCC'
COLOR_GRAY_FILL = '#F5F5F5'
COLOR_TEXT = '#2C3E50'
COLOR_DELTA = '#2980B9'

def draw_arrow(ax, x1, y1, x2, y2, label, is_optimal, node_r=0.32):
    dx = x2 - x1
    dy = y2 - y1
    dist = np.sqrt(dx**2 + dy**2)
    ux, uy = dx / dist, dy / dist
    sx = x1 + ux * node_r
    sy = y1 + uy * node_r
    ex = x2 - ux * (node_r + 0.05)
    ey = y2 - uy * (node_r + 0.05)
    color = COLOR_OPTIMAL if is_optimal else COLOR_GRAY
    lw = 2.5 if is_optimal else 1.0
    alpha_val = 1.0 if is_optimal else 0.5
    zorder = 3 if is_optimal else 1
    ax.annotate('', xy=(ex, ey), xytext=(sx, sy),
        arrowprops=dict(arrowstyle='->', color=color, lw=lw,
            mutation_scale=15, shrinkA=0, shrinkB=0,
            connectionstyle='arc3,rad=0'),
        zorder=zorder)
    mx = (sx + ex) / 2
    my = (sy + ey) / 2
    perp_x, perp_y = -uy, ux
    offset = 0.15
    if dy < -0.1:
        offset = -0.15
    lx = mx + perp_x * offset
    ly = my + perp_y * offset
    fontsize = 8 if is_optimal else 7
    fontweight = 'bold' if is_optimal else 'normal'
    ax.text(lx, ly, label, fontsize=fontsize, ha='center', va='center',
            color=color, fontweight=fontweight, alpha=alpha_val, zorder=zorder + 1)

# Draw all transition arrows
for t in range(2):
    for s_from in range(2):
        for s_to in range(2):
            x1 = x_positions[t]
            y1 = y_positions[s_from]
            x2 = x_positions[t + 1]
            y2 = y_positions[s_to]
            prob = trans[(s_from, s_to)]
            is_opt = (optimal_path[t] == s_from and optimal_path[t + 1] == s_to)
            draw_arrow(ax, x1, y1, x2, y2, f'a={prob}', is_opt, node_radius)

# Draw nodes
for t in range(3):
    for s in range(2):
        x = x_positions[t]
        y = y_positions[s]
        d = delta[(t, s)]
        is_opt = (optimal_path[t] == s)
        fill_color = COLOR_OPTIMAL_FILL if is_opt else COLOR_GRAY_FILL
        edge_color = COLOR_OPTIMAL if is_opt else '#AAAAAA'
        lw = 2.5 if is_opt else 1.2
        circle = plt.Circle((x, y), node_radius, facecolor=fill_color,
                             edgecolor=edge_color, linewidth=lw, zorder=5)
        ax.add_patch(circle)
        ax.text(x, y + 0.08, states[s], fontsize=13, ha='center', va='center',
                fontweight='bold', color=COLOR_TEXT, zorder=6)
        if d >= 0.01:
            d_str = f'\u03b4={d:.4f}'
        else:
            d_str = f'\u03b4={d:.6f}'
        ax.text(x, y - 0.14, d_str, fontsize=7, ha='center', va='center',
                color=COLOR_DELTA, zorder=6, fontweight='bold')

# Word labels
for t in range(3):
    x = x_positions[t]
    ax.text(x, -0.8, f't={t+1}', fontsize=10, ha='center', va='center', color=COLOR_TEXT)
    ax.text(x, -1.1, '"' + words[t] + '"', fontsize=12, ha='center', va='center',
            color=COLOR_TEXT, fontweight='bold', style='italic')

# Emission probabilities
for t in range(3):
    x = x_positions[t]
    w = words[t]
    e_n = emission[(0, w)]
    e_v = emission[(1, w)]
    ax.text(x, -1.45, f'B(N)={e_n}  B(V)={e_v}', fontsize=7.5,
            ha='center', va='center', color='#7F8C8D')

# State labels on left
for s in range(2):
    y = y_positions[s]
    ax.text(0.2, y, state_labels[s], fontsize=12, ha='center', va='center',
            fontweight='bold', color=COLOR_TEXT)

# Initial probability arrows
for s in range(2):
    x = x_positions[0]
    y = y_positions[s]
    pi_val = initial[s]
    ax.annotate('', xy=(x - node_radius - 0.02, y), xytext=(x - node_radius - 0.35, y),
        arrowprops=dict(arrowstyle='->', color='#7F8C8D', lw=1.2,
                        mutation_scale=12, shrinkA=0, shrinkB=0),
        zorder=2)
    ax.text(x - node_radius - 0.18, y + 0.18, f'\u03c0={pi_val}', fontsize=7.5,
            ha='center', va='center', color='#7F8C8D')

# Title
ax.text(2.5, 2.2, 'Viterbi \u89e3\u7801\uff1aPOS Tagging "fish can swim"',
        fontsize=15, ha='center', va='center', fontweight='bold', color=COLOR_TEXT)

# Optimal path label
ax.text(2.5, 1.85, '\u6700\u4f18\u8def\u5f84: N \u2192 N \u2192 V',
        fontsize=12, ha='center', va='center', fontweight='bold',
        color=COLOR_OPTIMAL,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=COLOR_OPTIMAL_FILL,
                  edgecolor=COLOR_OPTIMAL, linewidth=1.5))

# Legend box (no family='monospace' to avoid CJK font issues)
legend_text = '\u521d\u59cb\u6982\u7387: \u03c0(N)=0.6, \u03c0(V)=0.4\n\u8f6c\u79fb\u6982\u7387: A(N\u2192N)=0.3, A(N\u2192V)=0.7\n               A(V\u2192N)=0.8, A(V\u2192V)=0.2'
ax.text(4.4, -1.1, legend_text, fontsize=7, ha='left', va='center',
        color='#555555',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#FAFAFA',
                  edgecolor='#DDDDDD', linewidth=0.8))

plt.tight_layout(pad=0.5)
out_path = r'C:\Users\yingz\Documents\tech_blog\posts_ch\nlp\figures\chapter-1\fig-viterbi-trellis.png'
plt.savefig(out_path, dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()
print(f'Saved to: {out_path}')
