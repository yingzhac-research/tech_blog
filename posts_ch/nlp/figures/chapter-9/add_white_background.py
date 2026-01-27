"""
给 PNG 图片添加白色背景和 padding
解决暗色模式下看不清的问题
"""

from PIL import Image
import os


def add_white_background(input_path, output_path, padding=20, bg_color=(255, 255, 255)):
    """
    给图片添加白色背景和 padding

    Args:
        input_path: 输入图片路径
        output_path: 输出图片路径
        padding: 四周留白像素数
        bg_color: 背景颜色 (R, G, B)
    """
    img = Image.open(input_path)

    # 如果是 RGBA，转换透明区域为白色
    if img.mode == 'RGBA':
        background = Image.new('RGBA', img.size, bg_color + (255,))
        img = Image.alpha_composite(background, img)

    img = img.convert('RGB')

    # 创建带 padding 的新图片
    new_width = img.width + 2 * padding
    new_height = img.height + 2 * padding
    new_img = Image.new('RGB', (new_width, new_height), bg_color)
    new_img.paste(img, (padding, padding))

    new_img.save(output_path, 'PNG', quality=95)
    print(f"[OK] {os.path.basename(output_path)}")


def process_original_figures():
    """处理 original 目录下的所有图片"""

    original_dir = "original"

    figures = [
        # BigBird figures (830x832, RGBA - need white bg)
        ("bigbird-fig1a-random.png", 25),
        ("bigbird-fig1b-window.png", 25),
        ("bigbird-fig1c-global.png", 25),
        ("bigbird-fig1d-combined.png", 25),
        # Tay Survey taxonomy (830x602, RGBA - need white bg)
        ("tay-survey-fig2-taxonomy.png", 30),
    ]

    for filename, padding in figures:
        input_path = os.path.join(original_dir, filename)
        output_path = os.path.join(original_dir, filename)  # 覆盖原文件

        if os.path.exists(input_path):
            add_white_background(input_path, output_path, padding=padding)
        else:
            print(f"[SKIP] {filename} not found")


if __name__ == '__main__':
    print("Adding white background to original figures...\n")
    process_original_figures()
    print("\n=== Done! ===")
