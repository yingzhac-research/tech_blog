"""
从论文PDF中提取关键配图
"""
import fitz  # PyMuPDF
from PIL import Image
import io
from pathlib import Path

def render_page_region(pdf_path, page_num, output_path, scale=3.0, crop_box=None):
    """渲染PDF页面的特定区域为高清图片"""
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_num)

    # 高分辨率渲染
    mat = fitz.Matrix(scale, scale)
    pix = page.get_pixmap(matrix=mat)

    # 转换为PIL Image
    img = Image.open(io.BytesIO(pix.tobytes()))

    # 裁剪（如果指定）
    if crop_box:
        # crop_box = (left, top, right, bottom) 比例
        w, h = img.size
        left = int(w * crop_box[0])
        top = int(h * crop_box[1])
        right = int(w * crop_box[2])
        bottom = int(h * crop_box[3])
        img = img.crop((left, top, right, bottom))

    # 添加白色背景和padding
    img = add_white_background(img, padding=30)

    img.save(output_path, 'PNG', quality=95)
    print(f"[OK] Saved: {output_path}")
    doc.close()
    return img

def add_white_background(img, padding=25):
    """给图片添加白色背景和padding"""
    if img.mode == 'RGBA':
        background = Image.new('RGBA', img.size, (255, 255, 255, 255))
        img = Image.alpha_composite(background, img)
    img = img.convert('RGB')

    # 添加padding
    new_width = img.width + 2 * padding
    new_height = img.height + 2 * padding
    new_img = Image.new('RGB', (new_width, new_height), (255, 255, 255))
    new_img.paste(img, (padding, padding))

    return new_img

def main():
    output_dir = Path("original")
    output_dir.mkdir(exist_ok=True)

    # CLIP论文 - Figure 1在第2页 (0-indexed: page 1)
    # 对比学习示意图
    print("Extracting CLIP Figure 1...")
    render_page_region(
        "original/clip-paper.pdf",
        page_num=1,  # 第2页
        output_path=str(output_dir / "fig-clip-contrastive.png"),
        scale=3.0,
        crop_box=(0.1, 0.15, 0.9, 0.55)  # 裁剪Figure 1区域
    )

    # LLaVA论文 - Figure 1在第3页 (0-indexed: page 2)
    print("Extracting LLaVA Figure 1...")
    render_page_region(
        "original/llava-paper.pdf",
        page_num=2,  # 第3页
        output_path=str(output_dir / "fig-llava-architecture.png"),
        scale=3.0,
        crop_box=(0.1, 0.1, 0.9, 0.5)  # 裁剪Figure 1区域
    )

    # BLIP-2论文 - Figure 1在第1页 (0-indexed: page 0)
    print("Extracting BLIP-2 Figure 1...")
    render_page_region(
        "original/blip2-paper.pdf",
        page_num=0,  # 第1页
        output_path=str(output_dir / "fig-blip2-architecture.png"),
        scale=3.0,
        crop_box=(0.05, 0.35, 0.95, 0.75)  # 裁剪Figure 1区域
    )

    print("\nAll figures extracted successfully!")

if __name__ == "__main__":
    main()
