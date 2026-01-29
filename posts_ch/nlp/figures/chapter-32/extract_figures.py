"""
Extract figures from RAG and DPR paper PDFs
"""
import fitz  # PyMuPDF
from PIL import Image
import io
import os

def render_page_to_image(pdf_path, page_num, scale=3.0):
    """Render PDF page to high-resolution image"""
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_num)

    # High resolution rendering
    mat = fitz.Matrix(scale, scale)
    pix = page.get_pixmap(matrix=mat)

    # Convert to PIL Image
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    doc.close()
    return img

def crop_and_add_whitebg(img, crop_box, padding=30):
    """Crop image and add white background with padding"""
    # Crop
    cropped = img.crop(crop_box)

    # Add white background and padding
    new_width = cropped.width + 2 * padding
    new_height = cropped.height + 2 * padding
    new_img = Image.new('RGB', (new_width, new_height), (255, 255, 255))
    new_img.paste(cropped, (padding, padding))

    return new_img

def main():
    output_dir = "original"
    os.makedirs(output_dir, exist_ok=True)

    # ========================================
    # RAG paper Figure 1 (usually on page 2, index 1)
    # ========================================
    print("Processing RAG paper...")
    rag_pdf = "original/rag-paper.pdf"

    # Render page 2 (index 1) - RAG architecture diagram
    rag_page1 = render_page_to_image(rag_pdf, 1, scale=3.0)
    rag_page1.save(f"{output_dir}/rag-paper-page2-full.png")
    print(f"  Saved full page: {output_dir}/rag-paper-page2-full.png")
    print(f"  Page size: {rag_page1.size}")

    # RAG Figure 1 is approximately in the upper half of the page
    # With 3x scaling, typical crop region (adjust as needed)
    # Original page ~612x792pt, 3x -> ~1836x2376px
    # Figure 1 typically occupies upper portion - refined crop to exclude body text
    rag_fig1_box = (80, 80, 1760, 620)  # (left, top, right, bottom) - just the figure and caption
    rag_fig1 = crop_and_add_whitebg(rag_page1, rag_fig1_box, padding=20)
    rag_fig1.save(f"{output_dir}/fig-rag-architecture.png")
    print(f"  Saved RAG architecture: {output_dir}/fig-rag-architecture.png")

    # ========================================
    # DPR paper Figure 1 (usually on page 3, index 2)
    # ========================================
    print("\nProcessing DPR paper...")
    dpr_pdf = "original/dpr-paper.pdf"

    # Render page 3 (index 2) - DPR usually has architecture diagram here
    dpr_page2 = render_page_to_image(dpr_pdf, 2, scale=3.0)
    dpr_page2.save(f"{output_dir}/dpr-paper-page3-full.png")
    print(f"  Saved full page: {output_dir}/dpr-paper-page3-full.png")
    print(f"  Page size: {dpr_page2.size}")

    # Also render page 1
    dpr_page0 = render_page_to_image(dpr_pdf, 0, scale=3.0)
    dpr_page0.save(f"{output_dir}/dpr-paper-page1-full.png")
    print(f"  Saved page 1: {output_dir}/dpr-paper-page1-full.png")

    # Render page 2
    dpr_page1 = render_page_to_image(dpr_pdf, 1, scale=3.0)
    dpr_page1.save(f"{output_dir}/dpr-paper-page2-full.png")
    print(f"  Saved page 2: {output_dir}/dpr-paper-page2-full.png")

    print("\nDone! Please check generated images and adjust crop regions as needed.")

if __name__ == "__main__":
    main()
