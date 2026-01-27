"""
裁剪 Bahdanau 论文的图片
"""

from PIL import Image
from pathlib import Path

def crop_and_save(input_path, output_path, crop_box, add_padding=True, padding=20):
    """
    裁剪图片并保存

    crop_box: (left, top, right, bottom) in pixels
    """
    img = Image.open(input_path)
    cropped = img.crop(crop_box)

    if add_padding:
        # 添加白色padding
        new_width = cropped.width + 2 * padding
        new_height = cropped.height + 2 * padding
        new_img = Image.new('RGB', (new_width, new_height), (255, 255, 255))
        new_img.paste(cropped, (padding, padding))
        cropped = new_img

    cropped.save(output_path, 'PNG')
    print(f"[OK] Cropped: {output_path}")
    print(f"     Size: {cropped.width} x {cropped.height}")

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    rendered_dir = script_dir / "rendered_pages"
    output_dir = script_dir / "original"
    output_dir.mkdir(parents=True, exist_ok=True)

    # 检查页面尺寸
    page3 = Image.open(rendered_dir / "page_03.png")
    page6 = Image.open(rendered_dir / "page_06.png")
    print(f"Page 3 size: {page3.size}")
    print(f"Page 6 size: {page6.size}")

    # Figure 1 - 模型架构图 (page 3, 右上角)
    # 页面尺寸大约是 1275 x 1650 (150 dpi 的 letter size)
    # Figure 1 在右侧，大约 x: 700-1200, y: 150-550
    crop_and_save(
        rendered_dir / "page_03.png",
        output_dir / "fig1-attention-model.png",
        crop_box=(680, 130, 1220, 600),  # (left, top, right, bottom)
        add_padding=True
    )

    # Figure 3 - 对齐可视化 (page 6, 占据大部分页面)
    # 四个热力图，大约 y: 70-650
    crop_and_save(
        rendered_dir / "page_06.png",
        output_dir / "fig3-alignment-visualization.png",
        crop_box=(50, 60, 1220, 720),
        add_padding=True
    )

    print("\nDone!")
