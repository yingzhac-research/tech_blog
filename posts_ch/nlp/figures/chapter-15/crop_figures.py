"""从论文渲染页面裁剪关键图片并添加白底"""
from PIL import Image

def add_white_background(img, padding=30):
    """给图片添加白色背景和 padding"""
    if img.mode == 'RGBA':
        background = Image.new('RGBA', img.size, (255, 255, 255, 255))
        img = Image.alpha_composite(background, img)
    img = img.convert('RGB')
    new_w = img.width + 2 * padding
    new_h = img.height + 2 * padding
    new_img = Image.new('RGB', (new_w, new_h), (255, 255, 255))
    new_img.paste(img, (padding, padding))
    return new_img

# ── Figure 1: ALBERT 跨层分析 (page 3) ──
# L2 distance and cosine similarity plots
albert_p3 = Image.open('albert_page_03.png')
w, h = albert_p3.size
# The figure is in the middle-lower portion of the page
# Crop the two plots and their caption
albert_fig1 = albert_p3.crop((int(w*0.05), int(h*0.48), int(w*0.95), int(h*0.72)))
albert_fig1 = add_white_background(albert_fig1)
albert_fig1.save('original/fig1-albert-cross-layer-analysis.png', 'PNG')
print(f"[OK] ALBERT Figure 1: {albert_fig1.size}")

# ── Figure 2: DistilBERT 气泡图 (page 0) ──
# Parameter counts bubble chart
distil_p0 = Image.open('distilbert_page_00.png')
w, h = distil_p0.size
# The bubble chart is in the right portion of the page
distil_fig1 = distil_p0.crop((int(w*0.50), int(h*0.56), int(w*0.98), int(h*0.82)))
distil_fig1 = add_white_background(distil_fig1)
distil_fig1.save('original/fig2-distilbert-model-sizes.png', 'PNG')
print(f"[OK] DistilBERT Figure 1: {distil_fig1.size}")

# ── Figure 3: ALBERT 训练曲线 (page 8, already cropped as fig2) ──
# Adding data and removing dropout
albert_fig2 = Image.open('albert_fig2_crop_test.png')
albert_fig2 = add_white_background(albert_fig2)
albert_fig2.save('original/fig3-albert-training-curves.png', 'PNG')
print(f"[OK] ALBERT Figure 2: {albert_fig2.size}")

print("\nAll figures saved to original/")
