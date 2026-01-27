"""
渲染 PDF 页面为图片，然后手动识别需要的图
"""

import fitz  # PyMuPDF
from pathlib import Path

def render_pdf_pages(pdf_path, output_dir, dpi=200):
    """渲染 PDF 的每一页为 PNG 图片"""
    doc = fitz.open(pdf_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    zoom = dpi / 72  # 72 is the default DPI
    mat = fitz.Matrix(zoom, zoom)

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap(matrix=mat)
        output_path = output_dir / f"page_{page_num+1:02d}.png"
        pix.save(output_path)
        print(f"[OK] Rendered: {output_path}")

    doc.close()
    print(f"\nTotal pages rendered: {len(doc)}")

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    pdf_path = script_dir / "pdfs" / "bahdanau-attention-1409.0473.pdf"
    output_dir = script_dir / "rendered_pages"

    if pdf_path.exists():
        render_pdf_pages(pdf_path, output_dir, dpi=150)
    else:
        print(f"PDF not found: {pdf_path}")
