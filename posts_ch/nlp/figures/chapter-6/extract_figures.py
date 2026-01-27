"""
从 Bahdanau Attention 论文 PDF 中提取图片
"""

import fitz  # PyMuPDF
from pathlib import Path
from PIL import Image
import io

def extract_figures_from_pdf(pdf_path, output_dir):
    """从 PDF 提取所有图片"""
    doc = fitz.open(pdf_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    extracted = []
    for page_num, page in enumerate(doc):
        images = page.get_images()
        for img_idx, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            # 跳过太小的图片（可能是logo等）
            if len(image_bytes) < 5000:
                continue

            output_path = output_dir / f"page{page_num+1}_fig{img_idx+1}.{image_ext}"
            with open(output_path, "wb") as f:
                f.write(image_bytes)

            extracted.append(output_path)
            print(f"[OK] Extracted: {output_path} ({len(image_bytes):,} bytes)")

    doc.close()
    return extracted

def add_white_background(input_path, output_path=None, padding=20):
    """给图片添加白色背景和 padding"""
    if output_path is None:
        output_path = input_path

    img = Image.open(input_path)

    # 处理透明背景
    if img.mode == 'RGBA':
        background = Image.new('RGBA', img.size, (255, 255, 255, 255))
        img = Image.alpha_composite(background, img)

    img = img.convert('RGB')

    # 添加 padding
    new_width = img.width + 2 * padding
    new_height = img.height + 2 * padding
    new_img = Image.new('RGB', (new_width, new_height), (255, 255, 255))
    new_img.paste(img, (padding, padding))

    new_img.save(output_path, 'PNG')
    print(f"[OK] Added white background: {output_path}")
    return output_path

if __name__ == "__main__":
    # 设置路径
    script_dir = Path(__file__).parent
    pdf_path = script_dir / "pdfs" / "bahdanau-attention-1409.0473.pdf"
    output_dir = script_dir / "original"

    print(f"PDF: {pdf_path}")
    print(f"Output: {output_dir}")
    print("-" * 50)

    # 提取图片
    if pdf_path.exists():
        extracted = extract_figures_from_pdf(pdf_path, output_dir)
        print(f"\nExtracted {len(extracted)} figures")

        # 为所有提取的图片添加白色背景
        print("\nAdding white backgrounds...")
        for img_path in extracted:
            if img_path.suffix.lower() in ['.png', '.jpg', '.jpeg']:
                add_white_background(img_path)
    else:
        print(f"PDF not found: {pdf_path}")
