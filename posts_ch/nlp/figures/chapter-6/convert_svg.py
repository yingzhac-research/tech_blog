"""
将 SVG 转换为 PNG
"""

from pathlib import Path
import subprocess

def convert_svg_to_png(svg_path, png_path, width=1200):
    """使用 Inkscape 或 cairosvg 转换 SVG 到 PNG"""
    try:
        # 尝试使用 cairosvg
        import cairosvg
        cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), output_width=width)
        print(f"[OK] Converted with cairosvg: {png_path}")
        return True
    except ImportError:
        print("cairosvg not installed, trying other methods...")

    # 如果没有 cairosvg，可以保留 SVG 格式（Quarto 支持 SVG）
    print(f"[INFO] Keeping SVG format: {svg_path}")
    return False

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    original_dir = script_dir / "original"

    svg_files = list(original_dir.glob("*.svg"))
    print(f"Found {len(svg_files)} SVG files")

    for svg_path in svg_files:
        png_path = svg_path.with_suffix('.png')
        convert_svg_to_png(svg_path, png_path)
