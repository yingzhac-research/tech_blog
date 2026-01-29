"""
提取第26章配图的脚本
从 FlashAttention、RoPE、PagedAttention 论文中提取关键图片
"""

import fitz  # PyMuPDF
from PIL import Image
import io
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "original"
OUTPUT_DIR.mkdir(exist_ok=True)

def render_page_to_image(pdf_path, page_num, output_name, dpi=200, crop_box=None):
    """
    将 PDF 的指定页面渲染为图片

    Args:
        pdf_path: PDF 文件路径
        page_num: 页码（0-indexed）
        output_name: 输出文件名
        dpi: 分辨率
        crop_box: 裁剪区域 (x0, y0, x1, y1)，相对于页面尺寸的比例
    """
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_num)

    # 高分辨率渲染
    mat = fitz.Matrix(dpi/72, dpi/72)
    pix = page.get_pixmap(matrix=mat)

    # 转换为 PIL Image
    img = Image.open(io.BytesIO(pix.tobytes("png")))

    # 裁剪（如果指定）
    if crop_box:
        w, h = img.size
        x0, y0, x1, y1 = crop_box
        img = img.crop((int(x0*w), int(y0*h), int(x1*w), int(y1*h)))

    # 添加白色背景（处理透明）
    if img.mode == 'RGBA':
        background = Image.new('RGBA', img.size, (255, 255, 255, 255))
        img = Image.alpha_composite(background, img)
    img = img.convert('RGB')

    # 添加 padding
    padding = 25
    new_img = Image.new('RGB', (img.width + 2*padding, img.height + 2*padding), (255, 255, 255))
    new_img.paste(img, (padding, padding))

    output_path = OUTPUT_DIR / output_name
    new_img.save(output_path, 'PNG', quality=95)
    print(f"[OK] Saved: {output_path}")
    doc.close()
    return output_path

def main():
    # FlashAttention 论文 - Figure 1 (Memory Hierarchy / Tiling)
    # 通常在第2-3页
    print("\n=== Extracting FlashAttention figures ===")
    try:
        render_page_to_image(
            OUTPUT_DIR / "flash-attention-paper.pdf",
            page_num=1,  # 第2页（0-indexed）
            output_name="fig-flash-attention-tiling.png",
            dpi=250,
            crop_box=(0.05, 0.08, 0.95, 0.55)  # 裁剪上半部分（Figure 1区域）
        )
    except Exception as e:
        print(f"[ERROR] FlashAttention: {e}")

    # RoPE 论文 - Figure 1-2
    print("\n=== Extracting RoPE figures ===")
    try:
        render_page_to_image(
            OUTPUT_DIR / "rope-paper.pdf",
            page_num=2,  # 第3页
            output_name="fig-rope-visualization.png",
            dpi=250,
            crop_box=(0.1, 0.1, 0.9, 0.6)
        )
    except Exception as e:
        print(f"[ERROR] RoPE: {e}")

    # PagedAttention 论文 - Figure 1-3
    print("\n=== Extracting PagedAttention figures ===")
    try:
        # Figure 1: KV Cache 内存浪费问题
        render_page_to_image(
            OUTPUT_DIR / "pagedattention-paper.pdf",
            page_num=1,  # 第2页
            output_name="fig-pagedattention-memory.png",
            dpi=250,
            crop_box=(0.05, 0.35, 0.95, 0.85)
        )

        # Figure 3: PagedAttention 设计
        render_page_to_image(
            OUTPUT_DIR / "pagedattention-paper.pdf",
            page_num=3,  # 第4页
            output_name="fig-pagedattention-design.png",
            dpi=250,
            crop_box=(0.05, 0.08, 0.95, 0.55)
        )
    except Exception as e:
        print(f"[ERROR] PagedAttention: {e}")

    print("\n=== Done! ===")

if __name__ == "__main__":
    main()
