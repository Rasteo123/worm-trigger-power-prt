# Worm Trigger-Power PRT Classification Skill

**Bidirectional generator for Worm universe trigger events ↔ parahuman powers with comprehensive PRT classification**

## Quick Start

### Installation

```bash
# Clone or download this repository
cd worm_trigger_power_prt

# No dependencies required! Knowledge base is pre-built
python worm_skill.py
```

### Basic Usage

```python
from worm_skill import WormSkill

skill = WormSkill()

# Mode A: Trigger → Power
result = skill.process({
    "mode": "trigger_to_power",
    "trigger_description": "A teenage girl is locked in a locker filled with biohazard waste for hours while being mocked by peers.",
    "language": "en"
})

print(result["output"]["classification"])
# [{"type_ru": "Повелитель", "type_en": "Master", "rating": 8, "primary": true}, ...]
```

```python
# Mode B: Power → Trigger
result = skill.process({
    "mode": "power_to_trigger",
    "power_description": "Control over insects within several blocks with perfect multitasking",
    "known_classification": "Master 8",
    "num_variants": 2
})

print(result["output"]["trigger_variants"][0]["trigger_description"])
# Generated trigger scenario...
```

## Files Structure

```
worm_trigger_power_prt/
├── SKILL.md                     # Complete skill specification (18KB)
├── README.md                    # This file
├── TESTS.md                     # 25 test examples (28KB)
├── worm_skill.py               # Main Python processor (15KB)
├── worm_knowledge_base.json    # Knowledge base: 17 PDFs + 3 wikis (549KB)
├── extract_pdfs.py             # PDF extraction script (used once)
├── fetch_wiki.py               # Wiki fetching script (used once)
└── worm_unified_config.json    # Original Skill Seekers config

Total: ~620KB packaged skill
```

## Knowledge Base

### PDF Sources (17 files, 270 pages)
- **Classification Guides**: BLASTERS, BREAKERS, BRUTE, CHANGER, MOVERS, STRANGERS, STRIKERS, THINKERS, TINKERS, TRUMP (10 files)
- **Comprehensive**: PRT Quest (46 pages)
- **Advanced**: Sample Multitrigger (cluster mechanics)
- **Russian**: Механика-Триггеров, Триггеры, Триггеры-Изломов, Триггеры-Козырей, Триггеры-Повелителей (7 files)

### Wiki References (3 pages)
- [Trigger Event](https://worm.fandom.com/wiki/Trigger_Event)
- [Power Classifications](https://worm.fandom.com/wiki/Power_Classifications)
- [Shard](https://worm.fandom.com/wiki/Shard)

## Features

### Two Operational Modes

1. **trigger_to_power**: Generate power, PRT classification (1-12 rating), limitations, counterplay
2. **power_to_trigger**: Reverse-engineer plausible trigger event(s) from power description

### PRT Classification System

12 types with RU/EN labels:
- **Бугай / Brute**: Enhanced durability/strength
- **Ловкач / Mover**: Enhanced mobility
- **Шейкер / Shaker**: Area control
- **Бластер / Blaster**: Ranged attacks
- **Страйкер / Striker**: Touch-based effects
- **Чейнджер / Changer**: Self-transformation
- **Незаметник / Stranger**: Stealth/confusion
- **Повелитель / Master**: Minion control
- **Мыслитель / Thinker**: Information gathering
- **Технарь / Tinker**: Super-crafting
- **Излом / Breaker**: Altered state
- **Козырь / Trump**: Power manipulation

**Rating Scale 1-12**:
- 1-3: Minor threat
- 4-6: Moderate threat
- 7-9: Major threat
- 10-12: S-Class potential

### Bilingual Support

- Input: Free-form RU/EN text
- Output: RU classification labels + EN equivalents
- All reasoning in user's language

## Use Cases

1. **Fanfiction Writing**: Create OCs with consistent trigger/power pairs
2. **TTRPG Campaigns**: Generate NPCs for Worm tabletop games
3. **Power Analysis**: Classify existing characters or hypothetical powers
4. **Worldbuilding**: Ensure trigger events follow Worm's rules
5. **Reverse Engineering**: Understand what trauma produces specific powers

## API Integration

### Recommended LLM Setup

This skill is a **reference implementation**. For production-quality generation:

1. **Load SKILL.md as system prompt**
2. **Use few-shot examples from TESTS.md** (25 cases)
3. **Query knowledge base** with `skill.search_knowledge_base(query)`
4. **Validate JSON output** against schema

```python
# Example LLM integration (pseudo-code)
from openai import OpenAI

client = OpenAI()

# Load skill instructions
with open("SKILL.md", "r") as f:
    skill_prompt = f.read()

# Load few-shot examples
with open("TESTS.md", "r") as f:
    examples = f.read()

# User request
user_input = {
    "mode": "trigger_to_power",
    "trigger_description": "..."
}

# Generate with LLM
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": skill_prompt},
        {"role": "system", "content": f"Examples:\n{examples}"},
        {"role": "user", "content": json.dumps(user_input)}
    ],
    temperature=0.7
)

result = json.loads(response.choices[0].message.content)
```

### Recommended Models

- **Claude Sonnet 3.5+**: Best for nuanced trigger/power logic (100K+ context)
- **GPT-4 Turbo**: Good balance of creativity and consistency
- **GPT-4o**: Fast inference, handles bilingual well
- **Claude Haiku**: Budget option for simple classifications

## Advanced Features

### Multi-Classification

```json
{
  "classification": [
    {"type_en": "Master", "rating": 8, "primary": true},
    {"type_en": "Thinker", "rating": 3, "primary": false}
  ]
}
```

### Cluster Triggers

See TESTS.md Example 21 for multi-trigger mechanics.

### Manton Bypass Detection

Automatically flags powers that ignore Manton limit (+2-3 rating boost).

### Confidence Scores

```json
{
  "confidence": 0.85,  // 0.0-1.0
  "questions_for_user": [
    "Was there a specific person blamed?",
    "Did the trigger happen in isolation?"
  ]
}
```

## Testing

Run test suite:

```bash
python -m pytest test_worm_skill.py  # (if you create tests)
```

Or validate manually against TESTS.md:

```bash
python worm_skill.py
# Select mode, paste test inputs, compare outputs
```

## Limitations

1. **Reference implementation**: Python module does keyword matching only; integrate LLM for full generation
2. **Knowledge cutoff**: Based on Worm (2011-2013) and Ward (partial coverage)
3. **Subjective ratings**: PRT ratings are in-universe assessments, not objective metrics
4. **No GUI**: CLI only (integrate into your own UI)

## Contributing

To improve knowledge base:

1. Add new PDFs to project folder
2. Run `python extract_pdfs.py` to update `worm_knowledge_base.json`
3. Update `SKILL.md` with new sources
4. Add test cases to `TESTS.md`

## Version History

- **v1.0** (2026-01-19): Initial release
  - 17 PDF sources (270 pages)
  - 3 wiki pages
  - Bidirectional generation
  - Full PRT classification (12 types × 12 ratings)
  - RU/EN bilingual support

## Credits

- **Worm**: Original web serial by Wildbow (J.C. McCrae)
- **PRT Quest**: Community CYOA by various authors
- **Worm Wiki**: Fandom community documentation
- **Skill Framework**: MCP Skill Seekers
- **Extraction**: Claude Code + PyMuPDF

## License

**Knowledge base**: Compiled from publicly available Worm documentation (fair use for educational/fan purposes)

**Code**: MIT License - Use freely, attribution appreciated

---

**Created with**: Claude Code + MCP Skill Seekers
**Build date**: 2026-01-19
**Skill version**: 1.0
