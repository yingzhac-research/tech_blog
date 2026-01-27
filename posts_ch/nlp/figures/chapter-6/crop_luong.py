"""
裁剪 Luong Attention 论文的 Figure 3 (Local Attention Model)
"""

from PIL import Image
from pathlib import Path

def crop_and_save(input_path, output_path, crop_box, add_padding=True, padding=25):
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

    # Figure 3 - Local Attention Model (page 4, 左侧)
    crop_and_save(
        rendered_dir / "luong_page_04.png",
        output_dir / "fig-luong-local-attention.png",
        crop_box=(45, 120, 480, 590),  # 扩大右侧范围
        add_padding=True
    )

    print("\nDone!")
