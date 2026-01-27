"""
Chapter 2: The Awakening of Representation Learning - Figure Extraction Script

Usage:
1. pip install pymupdf pillow requests
2. python extract_figures.py

Downloads PDFs and extracts figures to original/ directory
"""

import os
import requests
import fitz  # PyMuPDF
from PIL import Image
from io import BytesIO

# 配置
OUTPUT_DIR = "original"
PAPERS = {
    "word2vec-1301.3781": "https://arxiv.org/pdf/1301.3781",
    "word2vec-explained-1411.2738": "https://arxiv.org/pdf/1411.2738",
    "fasttext-1607.04606": "https://arxiv.org/pdf/1607.04606",
}

def download_pdf(url, filename):
    """Download PDF file"""
    print(f"Downloading {url}...")
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"  Saved to {filename}")
        return True
    else:
        print(f"  Download failed: {response.status_code}")
        return False

def add_white_background(img_bytes, padding=25):
    """Add white background and padding to image"""
    img = Image.open(BytesIO(img_bytes))

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

    return new_img

def extract_figures_from_pdf(pdf_path, output_prefix):
    """Extract all figures from PDF"""
    print(f"\nProcessing {pdf_path}...")
    doc = fitz.open(pdf_path)

    extracted = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        images = page.get_images()

        for img_idx, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)

            if base_image:
                # Add white background
                try:
                    processed_img = add_white_background(base_image["image"])

                    # Save
                    output_path = f"{OUTPUT_DIR}/{output_prefix}_p{page_num+1}_fig{img_idx+1}.png"
                    processed_img.save(output_path, 'PNG')
                    print(f"  Extracted: {output_path}")
                    extracted.append(output_path)
                except Exception as e:
                    print(f"  Processing failed: {e}")

    doc.close()
    return extracted

def main():
    # Create output directories
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs("pdfs", exist_ok=True)

    all_figures = {}

    for name, url in PAPERS.items():
        pdf_path = f"pdfs/{name}.pdf"

        # Download PDF
        if not os.path.exists(pdf_path):
            if not download_pdf(url, pdf_path):
                continue

        # Extract figures
        figures = extract_figures_from_pdf(pdf_path, name)
        all_figures[name] = figures

    # Print summary
    print("\n" + "="*50)
    print("Extraction complete! Figure summary:")
    print("="*50)
    for name, figures in all_figures.items():
        print(f"\n{name}:")
        for fig in figures:
            print(f"  - {fig}")

    print(f"\nAll figures saved to {OUTPUT_DIR}/ directory")
    print("Please manually check and rename to meaningful names, e.g.:")
    print("  - fig1-cbow-skipgram-architecture.png")
    print("  - fig2-word-analogy.png")

if __name__ == "__main__":
    main()
