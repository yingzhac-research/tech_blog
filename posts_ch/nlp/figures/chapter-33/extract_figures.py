"""
Chapter 33 Figure Extraction Script
Extract figures from arXiv paper PDFs, add white background

Papers:
1. ReAct (arXiv:2210.03629) - Figure 1: ReAct vs CoT vs Act comparison
2. Generative Agents (arXiv:2304.03442) - Figure 2-3: Memory system architecture
3. Toolformer (arXiv:2302.04761) - Figure 1: Tool calling examples
4. LLM Agent Survey (arXiv:2308.11432) - Figure 2: Agent framework overview
"""

import os
import subprocess
from pathlib import Path

# Ensure directory exists
output_dir = Path("original")
output_dir.mkdir(exist_ok=True)

# Paper information
papers = [
    {
        "id": "2210.03629",
        "name": "react",
        "title": "ReAct: Synergizing Reasoning and Acting",
        "figures": [
            {"page": 2, "name": "fig1-react-comparison", "desc": "ReAct vs CoT vs Act-only comparison"}
        ]
    },
    {
        "id": "2304.03442",
        "name": "generative-agents",
        "title": "Generative Agents: Interactive Simulacra",
        "figures": [
            {"page": 3, "name": "fig2-agent-architecture", "desc": "Agent architecture overview"},
            {"page": 4, "name": "fig3-memory-retrieval", "desc": "Memory stream and retrieval"}
        ]
    },
    {
        "id": "2302.04761",
        "name": "toolformer",
        "title": "Toolformer: Language Models Can Teach Themselves",
        "figures": [
            {"page": 2, "name": "fig1-toolformer-example", "desc": "Tool calling insertion examples"}
        ]
    },
    {
        "id": "2308.11432",
        "name": "agent-survey",
        "title": "A Survey on LLM-based Autonomous Agents",
        "figures": [
            {"page": 3, "name": "fig2-agent-framework", "desc": "Agent construction framework"}
        ]
    }
]

def download_pdf(arxiv_id, output_path):
    """Download arXiv PDF"""
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    cmd = f'curl -L -o "{output_path}" "{url}"'
    print(f"Downloading: {url}")
    os.system(cmd)
    return os.path.exists(output_path)

def extract_page_as_image(pdf_path, page_num, output_path, scale=3):
    """
    Extract specific page from PDF as high-resolution image
    Using PyMuPDF (fitz)
    """
    try:
        import fitz  # PyMuPDF
    except ImportError:
        print("Please install PyMuPDF: pip install pymupdf")
        return False

    doc = fitz.open(pdf_path)
    if page_num >= len(doc):
        print(f"Error: Page {page_num} out of range (total {len(doc)} pages)")
        return False

    page = doc.load_page(page_num)
    # High resolution rendering (scale x)
    mat = fitz.Matrix(scale, scale)
    pix = page.get_pixmap(matrix=mat)
    pix.save(output_path)
    doc.close()
    print(f"[OK] Extracted page {page_num + 1} -> {output_path}")
    return True

def add_white_background(input_path, output_path=None, padding=25):
    """Add white background and padding to image"""
    try:
        from PIL import Image
    except ImportError:
        print("Please install Pillow: pip install pillow")
        return False

    if output_path is None:
        output_path = input_path

    img = Image.open(input_path)

    # Handle transparent background
    if img.mode == 'RGBA':
        background = Image.new('RGBA', img.size, (255, 255, 255, 255))
        img = Image.alpha_composite(background, img)

    img = img.convert('RGB')

    # Add padding
    new_width = img.width + 2 * padding
    new_height = img.height + 2 * padding
    new_img = Image.new('RGB', (new_width, new_height), (255, 255, 255))
    new_img.paste(img, (padding, padding))

    new_img.save(output_path, 'PNG')
    print(f"[OK] Added white background: {output_path}")
    return True

def main():
    print("=" * 60)
    print("Chapter 33 LLM Agent - Figure Extraction")
    print("=" * 60)

    for paper in papers:
        print(f"\nProcessing: {paper['title']}")
        print("-" * 40)

        pdf_path = f"{paper['name']}.pdf"

        # Step 1: Download PDF
        if not os.path.exists(pdf_path):
            if not download_pdf(paper['id'], pdf_path):
                print(f"[FAIL] Cannot download {paper['id']}")
                continue
        else:
            print(f"[SKIP] PDF exists: {pdf_path}")

        # Step 2: Extract each Figure from its page
        for fig in paper['figures']:
            page_num = fig['page'] - 1  # 0-indexed
            output_name = f"{fig['name']}.png"
            output_path = output_dir / output_name

            print(f"\nExtracting {fig['desc']} (Page {fig['page']})")

            # Extract page
            temp_path = output_dir / f"temp_{output_name}"
            if extract_page_as_image(pdf_path, page_num, str(temp_path)):
                # Add white background
                add_white_background(str(temp_path), str(output_path))
                # Delete temp file
                if temp_path.exists():
                    temp_path.unlink()

    print("\n" + "=" * 60)
    print("Done! Images saved in original/ directory")
    print("=" * 60)

    # List generated files
    print("\nGenerated files:")
    for f in output_dir.glob("*.png"):
        print(f"  - {f.name}")

if __name__ == "__main__":
    main()
