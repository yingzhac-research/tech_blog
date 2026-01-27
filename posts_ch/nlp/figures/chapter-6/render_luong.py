"""
渲染 Luong Attention 论文页面
"""

import fitz
from pathlib import Path

def render_pdf_pages(pdf_path, output_dir, dpi=150):
    doc = fitz.open(pdf_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    zoom = dpi / 72
    mat = fitz.Matrix(zoom, zoom)

    for page_num in range(min(len(doc), 6)):  # 只渲染前6页
        page = doc.load_page(page_num)
        pix = page.get_pixmap(matrix=mat)
        output_path = output_dir / f"luong_page_{page_num+1:02d}.png"
        pix.save(output_path)
        print(f"[OK] {output_path}")

    doc.close()

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    pdf_path = script_dir / "pdfs" / "luong-attention-1508.04025.pdf"
    output_dir = script_dir / "rendered_pages"

    if pdf_path.exists():
        render_pdf_pages(pdf_path, output_dir, dpi=150)
    else:
        print(f"PDF not found: {pdf_path}")
