#!/usr/bin/env python3
"""Fetch Worm Wiki pages and add to knowledge base."""

import json
import requests
from pathlib import Path

def fetch_wiki_page(url):
    """Fetch wiki page content."""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return {
            "url": url,
            "status": "success",
            "content_length": len(response.text),
            "raw_html": response.text[:50000]  # Limit to 50KB
        }
    except Exception as e:
        return {
            "url": url,
            "status": "error",
            "error": str(e)
        }

def main():
    import sys
    import io

    # Fix Windows console encoding
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # Load existing knowledge base
    kb_file = Path("worm_knowledge_base.json")
    with open(kb_file, "r", encoding="utf-8") as f:
        knowledge_base = json.load(f)

    wiki_urls = [
        ("Trigger_Event", "https://worm.fandom.com/wiki/Trigger_Event"),
        ("Power_Classifications", "https://worm.fandom.com/wiki/Power_Classifications"),
        ("Shard", "https://worm.fandom.com/wiki/Shard")
    ]

    print("[*] Fetching Wiki pages...")
    for name, url in wiki_urls:
        print(f"[*] Fetching {name}...")
        data = fetch_wiki_page(url)
        knowledge_base["sources"][f"wiki_{name}"] = {
            "type": "wiki",
            **data
        }
        if data["status"] == "success":
            print(f"[+] Fetched {name} ({data['content_length']} bytes)")
        else:
            print(f"[-] Error fetching {name}: {data.get('error')}")

    # Save updated knowledge base
    with open(kb_file, "w", encoding="utf-8") as f:
        json.dump(knowledge_base, f, ensure_ascii=False, indent=2)

    print(f"\n[+] Knowledge base updated")
    print(f"[*] Total sources: {len(knowledge_base['sources'])}")

if __name__ == "__main__":
    main()
