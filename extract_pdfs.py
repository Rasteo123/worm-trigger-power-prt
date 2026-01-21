#!/usr/bin/env python3
"""Extract text from all Worm PDFs and create knowledge base."""

import os
import json
import fitz  # PyMuPDF
from pathlib import Path

def extract_pdf_text(pdf_path):
    """Extract text from a single PDF."""
    doc = fitz.open(pdf_path)
    full_text = []

    for page_num, page in enumerate(doc, 1):
        text = page.get_text()
        if text.strip():
            full_text.append({
                "page": page_num,
                "text": text.strip()
            })

    doc.close()
    return full_text

def main():
    import sys
    import io

    # Fix Windows console encoding
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    pdf_files = [
        "BLASTERS.pdf",
        "BREAKERS.pdf",
        "BRUTE.pdf",
        "CHANGER.pdf",
        "MOVERS.pdf",
        "PRT Quest.pdf",
        "Sample Multitrigger.pdf",
        "STRANGERS.pdf",
        "STRIKERS.pdf",
        "THINKERS.pdf",
        "TINKERS.pdf",
        "TRUMP.pdf",
        "Механика-Триггеров.pdf",
        "Триггеры.pdf",
        "Триггеры-Изломов-_Breaker_.pdf",
        "Триггеры-Козырей-_Trump_.pdf",
        "Триггеры-Повелителей-_Master_.pdf"
    ]

    knowledge_base = {
        "name": "worm_trigger_power_prt",
        "description": "Worm universe trigger-power knowledge base",
        "sources": {}
    }

    for pdf_file in pdf_files:
        pdf_path = Path(pdf_file)
        if not pdf_path.exists():
            print(f"[!] Skipping {pdf_file} - not found")
            continue

        print(f"[*] Processing {pdf_file}...")
        try:
            text_data = extract_pdf_text(pdf_path)
            knowledge_base["sources"][pdf_file] = {
                "type": "pdf",
                "pages": len(text_data),
                "content": text_data
            }
            print(f"[+] Extracted {len(text_data)} pages from {pdf_file}")
        except Exception as e:
            print(f"[-] Error processing {pdf_file}: {e}")

    # Save knowledge base
    output_file = Path("worm_knowledge_base.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(knowledge_base, f, ensure_ascii=False, indent=2)

    print(f"\n[+] Knowledge base saved to {output_file}")
    print(f"[*] Total sources: {len(knowledge_base['sources'])}")

if __name__ == "__main__":
    main()
