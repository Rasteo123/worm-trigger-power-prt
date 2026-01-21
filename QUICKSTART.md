# Worm Trigger-Power Skill - Quick Start

**5-minute setup guide**

## Installation (No dependencies!)

```bash
cd C:\Users\Admin\Desktop\Worm
python worm_skill.py
```

## Usage

### Interactive CLI

```bash
python worm_skill.py
# Select mode: 1 (trigger→power) or 2 (power→trigger)
```

### Python API

```python
from worm_skill import WormSkill

skill = WormSkill()

# Trigger → Power
result = skill.process({
    "mode": "trigger_to_power",
    "trigger_description": "Locked in locker, social isolation, disgust"
})

print(result["output"]["classification"])
# [{"type_ru": "Повелитель", "type_en": "Master", "rating": 8}, ...]

# Power → Trigger
result = skill.process({
    "mode": "power_to_trigger",
    "power_description": "Control insects with multitasking",
    "known_classification": "Master 8"
})

print(result["output"]["trigger_variants"][0])
```

### Search Knowledge Base

```python
results = skill.search_knowledge_base("master trigger")
for r in results:
    print(f"{r['source']} - Page {r['page']}")
```

## Test Examples

```bash
python test_skill_example.py
```

Runs 3 tests:
1. Taylor Hebert trigger (trigger→power)
2. Insect control (power→trigger)
3. Knowledge base search

## Files

- **SKILL.md**: Full specification (read this for LLM integration)
- **TESTS.md**: 25 test cases (use as few-shot examples)
- **README.md**: Complete documentation
- **worm_skill.py**: Python processor
- **worm_knowledge_base.json**: 17 PDFs + 3 wikis (549KB)

## LLM Integration

**For production-quality generation**, integrate with Claude/GPT:

```python
# 1. Load SKILL.md as system prompt
# 2. Add few-shot examples from TESTS.md
# 3. Query knowledge base with WormSkill.search_knowledge_base()
# 4. Pass to LLM (Claude Sonnet 3.5+ or GPT-4)
# 5. Validate JSON output
```

See README.md "API Integration" section for details.

## PRT Classifications (RU/EN)

- Бугай / Brute (durability/strength)
- Ловкач / Mover (mobility)
- Шейкер / Shaker (area control)
- Бластер / Blaster (ranged attacks)
- Страйкер / Striker (touch-based)
- Чейнджер / Changer (transformation)
- Незаметник / Stranger (stealth)
- Повелитель / Master (minion control)
- Мыслитель / Thinker (information)
- Технарь / Tinker (crafting)
- Излом / Breaker (altered state)
- Козырь / Trump (power manipulation)

**Ratings**: 1-12 (1-3 minor, 4-6 moderate, 7-9 major, 10-12 S-Class)

## Support

- Read **SKILL.md** for full specification
- Check **TESTS.md** for examples
- See **COMPLETION_REPORT.md** for technical details

---

**Created**: 2026-01-19 | **Version**: 1.0 | **Size**: 628KB
