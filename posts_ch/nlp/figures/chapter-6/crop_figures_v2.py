"""
裁剪 Bahdanau 论文的图片 - 修正版
"""

from PIL import Image
from pathlib import Path

def crop_and_save(input_path, output_path, crop_box, add_padding=True, padding=25):
    """裁剪图片并保存"""
    img = Image.open(input_path)
    cropped = img.crop(crop_box)

    if add_padding:
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

    # Figure 3 - 对齐可视化 (page 6, 四个热力图)
    # 需要包含完整的四个子图和标题
    crop_and_save(
        rendered_dir / "page_06.png",
        output_dir / "fig3-alignment-visualization.png",
        crop_box=(100, 55, 1180, 780),  # 调整以包含完整的四个图
        add_padding=True
    )

    # Figure 2 - BLEU vs 句子长度 (page 5, 右上角)
    crop_and_save(
        rendered_dir / "page_05.png",
        output_dir / "fig2-bleu-vs-length.png",
        crop_box=(700, 55, 1230, 400),
        add_padding=True
    )

    print("\nDone!")
