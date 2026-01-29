"""
从论文PDF中提取关键图片
用于第29章：开源大模型的演进
"""

import fitz  # PyMuPDF
from pathlib import Path
from PIL import Image
import io

def extract_page_as_image(pdf_path, page_num, output_path, dpi=200):
    """将PDF的特定页面渲染为高清图片"""
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_num)

    # 3x缩放以获得高分辨率
    zoom = dpi / 72  # 72是默认DPI
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)

    # 转换为PIL Image
    img = Image.open(io.BytesIO(pix.tobytes("png")))

    # 添加白色背景（如果有透明度）
    if img.mode == 'RGBA':
        background = Image.new('RGBA', img.size, (255, 255, 255, 255))
        img = Image.alpha_composite(background, img)
    img = img.convert('RGB')

    img.save(output_path, 'PNG', quality=95)
    print(f"[OK] Saved: {output_path}")
    doc.close()
    return img

def crop_figure_from_page(pdf_path, page_num, crop_box, output_path, dpi=200):
    """从PDF页面裁剪特定区域（用于提取图片）

    crop_box: (x0, y0, x1, y1) 相对于页面的比例 (0-1)
    """
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_num)

    # 获取页面尺寸
    page_rect = page.rect

    # 计算裁剪区域（像素坐标）
    x0 = page_rect.width * crop_box[0]
    y0 = page_rect.height * crop_box[1]
    x1 = page_rect.width * crop_box[2]
    y1 = page_rect.height * crop_box[3]

    clip = fitz.Rect(x0, y0, x1, y1)

    # 渲染裁剪区域
    zoom = dpi / 72
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, clip=clip)

    # 转换并保存
    img = Image.open(io.BytesIO(pix.tobytes("png")))
    if img.mode == 'RGBA':
        background = Image.new('RGBA', img.size, (255, 255, 255, 255))
        img = Image.alpha_composite(background, img)
    img = img.convert('RGB')

    # 添加padding
    padding = 20
    new_img = Image.new('RGB', (img.width + 2*padding, img.height + 2*padding), (255, 255, 255))
    new_img.paste(img, (padding, padding))

    new_img.save(output_path, 'PNG', quality=95)
    print(f"[OK] Cropped and saved: {output_path}")
    doc.close()
    return new_img

def add_white_background(input_path, output_path=None, padding=25):
    """给图片添加白色背景和padding"""
    if output_path is None:
        output_path = input_path

    img = Image.open(input_path)

    if img.mode == 'RGBA':
        background = Image.new('RGBA', img.size, (255, 255, 255, 255))
        img = Image.alpha_composite(background, img)

    img = img.convert('RGB')

    new_width = img.width + 2 * padding
    new_height = img.height + 2 * padding
    new_img = Image.new('RGB', (new_width, new_height), (255, 255, 255))
    new_img.paste(img, (padding, padding))

    new_img.save(output_path, 'PNG')
    print(f"[OK] Added white background: {output_path}")

def main():
    base_dir = Path(__file__).parent / "original"

    print("=" * 60)
    print("Extracting figures for Chapter 29: Open Source LLM Evolution")
    print("=" * 60)

    # ============================================================
    # Mistral 7B Paper - Sliding Window Attention (Figure 1, page 2)
    # ============================================================
    print("\n[1] Mistral 7B - Sliding Window Attention...")
    mistral_pdf = base_dir / "mistral-paper.pdf"

    # Figure 1 is on page 2 (0-indexed: page 1), showing SWA
    crop_figure_from_page(
        mistral_pdf,
        page_num=1,  # Page 2
        crop_box=(0.05, 0.08, 0.95, 0.45),  # Top portion with Figure 1
        output_path=base_dir / "fig1-mistral-sliding-window.png",
        dpi=250
    )

    # ============================================================
    # Mixtral Paper - MoE Architecture (Figure 1, page 2)
    # ============================================================
    print("\n[2] Mixtral - MoE Architecture...")
    mixtral_pdf = base_dir / "mixtral-paper.pdf"

    # Figure 1 shows MoE routing
    crop_figure_from_page(
        mixtral_pdf,
        page_num=1,  # Page 2
        crop_box=(0.1, 0.05, 0.9, 0.50),  # Figure area
        output_path=base_dir / "fig2-mixtral-moe-architecture.png",
        dpi=250
    )

    # ============================================================
    # LLaMA Paper - Training loss curve (if available)
    # ============================================================
    print("\n[3] LLaMA - Performance/Training curves...")
    llama_pdf = base_dir / "llama1-paper.pdf"

    # LLaMA论文Figure 1是training loss曲线，在page 4
    crop_figure_from_page(
        llama_pdf,
        page_num=3,  # Page 4
        crop_box=(0.1, 0.05, 0.9, 0.50),  # Figure area
        output_path=base_dir / "fig3-llama-training-loss.png",
        dpi=250
    )

    print("\n" + "=" * 60)
    print("Figure extraction complete!")
    print("=" * 60)

    # List extracted files
    print("\nExtracted files:")
    for f in base_dir.glob("fig*.png"):
        print(f"  - {f.name}")

if __name__ == "__main__":
    main()
