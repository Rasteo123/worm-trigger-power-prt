#!/usr/bin/env python3
"""Test Worm skill with example inputs."""

import json
import sys
import io
from worm_skill import WormSkill

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    skill = WormSkill()

    print("=== Test 1: trigger_to_power (Taylor Hebert) ===\n")

    result1 = skill.process({
        "mode": "trigger_to_power",
        "trigger_description": "A teenage girl is locked in a school locker filled with used tampons and biohazard waste for hours. She feels utterly helpless, socially isolated (her former best friend led the bullies), and disgusted by her situation.",
        "language": "en"
    })

    print("INPUT:", result1["input_summary"])
    print("\nCLASSIFICATIONS:")
    for c in result1["output"]["classification"]:
        primary_str = " (PRIMARY)" if c["primary"] else ""
        print(f"  - {c['type_ru']} / {c['type_en']} {c['rating']}{primary_str}")
        print(f"    Justification: {c['justification']}")

    print("\nREASONING:")
    for r in result1["output"]["reasoning"]:
        print(f"  - {r['point']}")
        print(f"    Because: {r['because']}")
        print(f"    Sources: {', '.join(r['sources'])}")

    print(f"\nCONFIDENCE: {result1['output']['confidence']}")
    print(f"QUESTIONS: {', '.join(result1['output']['questions_for_user'])}")

    print("\n" + "="*60 + "\n")
    print("=== Test 2: power_to_trigger (Insect Control) ===\n")

    result2 = skill.process({
        "mode": "power_to_trigger",
        "power_description": "Control over insects within several blocks with perfect multitasking. Can sense through their senses.",
        "known_classification": "Master 8 / Thinker 3",
        "num_variants": 2
    })

    print("INPUT:", result2["input_summary"])
    print("\nCLASSIFICATIONS:")
    for c in result2["output"]["classification"]:
        primary_str = " (PRIMARY)" if c["primary"] else ""
        print(f"  - {c['type_ru']} / {c['type_en']} {c['rating']}{primary_str}")

    print("\nTRIGGER VARIANTS:")
    for v in result2["output"]["trigger_variants"]:
        print(f"  Variant {v['variant_number']} ({v['probability']}):")
        print(f"    {v['trigger_description']}")
        print(f"    Emotional core: {v['trigger_analysis']['emotional_core']}")

    print("\n" + "="*60 + "\n")
    print("=== Test 3: Knowledge Base Search ===\n")

    search_results = skill.search_knowledge_base("master trigger", source_types=["pdf"])
    print(f"Found {len(search_results)} results for 'master trigger':\n")

    for i, r in enumerate(search_results[:3], 1):
        print(f"{i}. [{r['source']}] Page {r['page']}")
        print(f"   {r['snippet'][:150]}...\n")

    print("\n" + "="*60)
    print("\n✅ All tests completed successfully!")
    print("\nNote: This is a REFERENCE implementation.")
    print("For full power/trigger generation, integrate with LLM API using SKILL.md prompt.")

if __name__ == "__main__":
    main()
