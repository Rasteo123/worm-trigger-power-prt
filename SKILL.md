---
name: worm-trigger-power-prt
description: Bidirectional generator for Worm trigger events and parahuman powers with PRT classification
---

# Worm Trigger-Power PRT Classification Skill

## Purpose

This skill provides bidirectional generation between trigger events and parahuman powers in the Worm universe, with comprehensive PRT (Parahuman Response Team) / СКП (Служба Контроля Паралюдей) classification.

**Two operational modes:**

1. **trigger_to_power**: Generate power description, classification, and rating from a trigger event
2. **power_to_trigger**: Generate plausible trigger event(s) from a power description

## When to Use This Skill

- **Worldbuilding**: Create original characters (OCs) for Worm fanfiction
- **Game mastering**: Generate NPCs for Worm TTRPG campaigns
- **Analysis**: Classify existing Worm characters or hypothetical powers
- **Reverse engineering**: Understand what traumatic events could produce specific powers
- **Consistency checking**: Verify if a power/trigger pair follows Worm's established rules

## Knowledge Base Sources

### PDF Documentation (17 files, 270 pages)
- **Classification guides**: BLASTERS.pdf, BREAKERS.pdf, BRUTE.pdf, CHANGER.pdf, MOVERS.pdf, STRANGERS.pdf, STRIKERS.pdf, THINKERS.pdf, TINKERS.pdf, TRUMP.pdf
- **Comprehensive reference**: PRT Quest.pdf (46 pages)
- **Advanced mechanics**: Sample Multitrigger.pdf (cluster triggers, bud mechanics)
- **Russian translations**: Механика-Триггеров.pdf, Триггеры.pdf, Триггеры-Изломов-_Breaker_.pdf, Триггеры-Козырей-_Trump_.pdf, Триггеры-Повелителей-_Master_.pdf

### Wiki References (3 pages)
- [Trigger Event](https://worm.fandom.com/wiki/Trigger_Event): Core trigger mechanics
- [Power Classifications](https://worm.fandom.com/wiki/Power_Classifications): PRT classification system
- [Shard](https://worm.fandom.com/wiki/Shard): Entity shard behavior and assignment logic

## Input Contract

### Mode A: trigger_to_power

**Required fields:**
- `mode`: "trigger_to_power"
- `trigger_description`: String (free-form, RU/EN supported)

**Optional fields:**
- `user_context`: Additional character background
- `constraints`: Limitations on power scope/type
- `language`: "ru" or "en" (default: auto-detect)

**Example input:**
```json
{
  "mode": "trigger_to_power",
  "trigger_description": "A teenage girl is locked in a school locker filled with biohazard waste for hours while students mock her. She feels utterly helpless, isolated, and disgusted by the situation and herself.",
  "language": "en"
}
```

### Mode B: power_to_trigger

**Required fields:**
- `mode`: "power_to_trigger"
- `power_description`: String (free-form, RU/EN supported)

**Optional fields:**
- `known_classification`: PRT rating if already known (e.g., "Master 8")
- `num_variants`: Number of trigger variants to generate (1-3, default: 1)
- `language`: "ru" or "en" (default: auto-detect)

**Example input:**
```json
{
  "mode": "power_to_trigger",
  "power_description": "Ability to control insects within a several-block radius with perfect multitasking",
  "known_classification": "Master 8",
  "num_variants": 2
}
```

## Output Contract

### Mode A Output: trigger_to_power

```json
{
  "mode": "trigger_to_power",
  "input_summary": "Brief recap of trigger event",
  "output": {
    "power_description": "Detailed power description with mechanics, limitations, and edge cases",
    "classification": [
      {
        "type_ru": "Повелитель",
        "type_en": "Master",
        "rating": 8,
        "primary": true,
        "justification": "Why this rating and type"
      },
      {
        "type_ru": "Мыслитель",
        "type_en": "Thinker",
        "rating": 3,
        "primary": false,
        "justification": "Secondary classification reasoning"
      }
    ],
    "limitations": [
      "Cannot control humans",
      "Reduced effectiveness against fire-based attacks",
      "Requires line of sight for initial connection"
    ],
    "secondary_effects": [
      "Enhanced multitasking ability",
      "Minor sensory enhancement through insect swarm"
    ],
    "counterplay": [
      "Area-of-effect attacks",
      "Environmental hazards (fire, cold)",
      "Isolation from insect populations"
    ],
    "reasoning": [
      {
        "point": "Master classification primary",
        "because": "Trigger involved feeling helpless and isolated (classic Master trigger: social isolation + loss of control over social situation)",
        "sources": ["Триггеры-Повелителей-_Master_.pdf#p1", "Trigger_Event(wiki)"]
      },
      {
        "point": "Insect control specifically",
        "because": "Disgust element (biohazard) creates thematic connection to 'disgusting' or 'alien' minions",
        "sources": ["PRT Quest.pdf#p23", "Sample Multitrigger.pdf#p8"]
      },
      {
        "point": "Thinker secondary rating",
        "because": "Perfect multitasking required to control thousands of insects is a cognitive enhancement",
        "sources": ["THINKERS.pdf#p5"]
      }
    ],
    "confidence": 0.85,
    "questions_for_user": [
      "Was there a specific person the victim blamed for the situation?",
      "Did the trigger happen in complete isolation or with others nearby?"
    ]
  }
}
```

### Mode B Output: power_to_trigger

```json
{
  "mode": "power_to_trigger",
  "input_summary": "Brief recap of power",
  "output": {
    "trigger_variants": [
      {
        "variant_number": 1,
        "probability": "most_likely",
        "trigger_description": "Detailed scenario of trigger event",
        "trigger_analysis": {
          "emotional_core": "Helplessness, isolation, disgust",
          "threat_type": "Social/environmental",
          "duration": "Extended (hours)",
          "locus_of_blame": "External (peers)"
        }
      },
      {
        "variant_number": 2,
        "probability": "alternative",
        "trigger_description": "Alternative trigger scenario",
        "trigger_analysis": {
          "emotional_core": "Different emotional emphasis",
          "threat_type": "Alternative threat",
          "duration": "Acute or extended",
          "locus_of_blame": "Self or external"
        }
      }
    ],
    "classification": [
      {
        "type_ru": "Повелитель",
        "type_en": "Master",
        "rating": 8,
        "primary": true,
        "justification": "Derived from power scope and capabilities"
      }
    ],
    "limitations": [
      "Inferred from power description"
    ],
    "secondary_effects": [
      "Logical consequences of power"
    ],
    "counterplay": [
      "Tactical countermeasures"
    ],
    "reasoning": [
      {
        "point": "Master trigger required",
        "because": "Control-based powers stem from loss of control in social contexts",
        "sources": ["Триггеры-Повелителей-_Master_.pdf", "Trigger_Event(wiki)"]
      }
    ],
    "confidence": 0.72,
    "questions_for_user": [
      "Are there any known limitations not mentioned?",
      "Is this power part of a cluster trigger?"
    ]
  }
}
```

## PRT Classification System

### Complete Type Mapping (RU/EN)

| Type RU | Type EN | Core Concept | Rating Scale Focus |
|---------|---------|--------------|-------------------|
| Бугай | Brute | Enhanced durability/strength | Toughness level 1-12 |
| Ловкач | Mover | Enhanced mobility | Speed/versatility 1-12 |
| Шейкер | Shaker | Area-of-effect control | Range/potency 1-12 |
| Бластер | Blaster | Ranged attacks | Damage/range 1-12 |
| Страйкер | Striker | Touch-based effects | Lethality/requirement 1-12 |
| Чейнджер | Changer | Self-transformation | Utility/completeness 1-12 |
| Незаметник | Stranger | Stealth/confusion | Detection difficulty 1-12 |
| Повелитель | Master | Minion control | Scope/autonomy 1-12 |
| Мыслитель | Thinker | Information gathering | Processing/scope 1-12 |
| Технарь | Tinker | Super-crafting | Specialty breadth 1-12 |
| Излом | Breaker | Altered state | State power 1-12 |
| Козырь | Trump | Power manipulation | Effect on others 1-12 |

### Rating Scale 1-12 (General Guidelines)

**Ratings 1-3**: Minor threat
- 1: Negligible (requires specific circumstances)
- 2: Noteworthy (specialist response)
- 3: Concerning (small team)

**Ratings 4-6**: Moderate threat
- 4: Dangerous (trained team required)
- 5: Serious (experienced team)
- 6: High priority (elite response)

**Ratings 7-9**: Major threat
- 7: Critical (multiple teams)
- 8: Strategic asset/threat (regional concern)
- 9: Extreme (national concern)

**Ratings 10-12**: S-Class potential
- 10: Near S-Class (could trigger evacuation)
- 11: S-Class lite (widespread destruction potential)
- 12: Endbringer-tier (existential threat)

### Multi-Classification Rules

1. **Primary vs Secondary**: Highest rating is usually primary
2. **Slash notation**: "Master 8 / Thinker 3" means primarily Master with Thinker sub-rating
3. **Bracket notation**: "Shaker (Stranger 5)" means Shaker power with Stranger application
4. **Trump wildcards**: Trump powers often have variable ratings: "Trump 6-10"

## Decision Algorithm

### trigger_to_power Flow

```
1. PARSE TRIGGER
   ├─ Identify emotional core (fear, isolation, disgust, betrayal, etc.)
   ├─ Categorize threat type (physical, social, environmental, abstract)
   ├─ Determine duration (acute vs extended)
   └─ Assess locus of blame (self vs external)

2. MAP TO TRIGGER TYPE
   ├─ Brute: Physical damage, endurance challenges
   ├─ Mover: Confinement, pursuit, restriction of movement
   ├─ Shaker: Environmental hazards, territory control needed
   ├─ Blaster: Long-range threat, need to keep distance
   ├─ Striker: Close-quarters inevitable confrontation
   ├─ Changer: Identity crisis, need to be someone else
   ├─ Stranger: Social exposure, need to hide/escape notice
   ├─ Master: Social isolation, loss of control over social situation
   ├─ Thinker: Information deficit, lack of understanding
   ├─ Tinker: Problem requiring tools/preparation (extended trigger)
   ├─ Breaker: Need to escape current reality entirely
   └─ Trump: Betrayal by or conflict with other parahumans

3. GENERATE POWER MECHANICS
   ├─ Thematic connection (literal or metaphorical to trigger)
   ├─ Ironic twist (shard's alien interpretation)
   ├─ Built-in limitations (shards test conflict drive)
   └─ Secondary effects (cognitive/sensory changes)

4. ASSIGN RATINGS
   ├─ Evaluate scope (area, number of targets, range)
   ├─ Assess lethality/impact
   ├─ Consider versatility and counters
   ├─ Apply modifier for Manton effect bypass (+1 to +3)
   └─ Check for multi-classification

5. VALIDATE CONSISTENCY
   ├─ Cross-reference with knowledge base examples
   ├─ Verify trigger→power logic chain
   └─ Ensure no canon contradictions
```

### power_to_trigger Flow

```
1. ANALYZE POWER
   ├─ Extract primary classification from mechanics
   ├─ Identify secondary classifications
   ├─ Estimate rating from described capabilities
   └─ Note unusual features (Manton bypass, Trump interaction, etc.)

2. INFER TRIGGER TYPE
   ├─ Reverse-map from classification to trigger category
   ├─ Consider power theme (fire = destruction need, insects = disgust, etc.)
   ├─ Analyze limitations for trigger hints
   └─ Check for cluster/multitrigger indicators

3. GENERATE TRIGGER SCENARIO
   ├─ Create concrete life situation
   ├─ Build emotional progression to breaking point
   ├─ Include sensory details
   ├─ Specify threat type and duration
   └─ Add ironic element (shard's "solution")

4. CREATE VARIANTS (if requested)
   ├─ Variant 1: Most direct/obvious interpretation
   ├─ Variant 2: Alternative emotional core
   └─ Variant 3: Edge case or cluster trigger possibility

5. VALIDATE PLAUSIBILITY
   ├─ Check against known canon examples
   ├─ Ensure emotional logic holds
   └─ Verify power→trigger causality
```

## Consistency Rules

### Hard Rules (Never Violate)

1. **Trigger events are traumatic**: No "mild inconveniences" cause powers
2. **Powers are ironic/alien**: Shards don't give you exactly what you want
3. **First triggers happen once**: Can't re-trigger with new power (except very rare second triggers)
4. **Manton effect is default**: Most powers can't directly affect humans unless specified
5. **Ratings reflect threat level to PRT responders**: Not raw "power level"
6. **Shards push conflict**: Powers have built-in limitations or compulsions

### Soft Rules (Context-Dependent)

1. **Physical triggers → physical powers**: Usually but not always
2. **Master triggers involve social isolation**: Common pattern, not absolute
3. **Tinker triggers are extended**: Typical but can be acute with right context
4. **Higher ratings are rarer**: Distribution follows power law
5. **Cluster triggers share themes**: Buds from same trigger event have related powers

### Source Priority

When sources conflict:
1. **PDF documentation** (extracted from quest/CYOA, treated as primary canon for this skill)
2. **Wiki pages** (community consensus, occasionally speculative)
3. **Logical inference** (mark as "inference" in reasoning)

Never invent "facts" - if uncertain, note low confidence and ask clarifying questions.

## Handling Ambiguity

### When Input is Vague

**Low detail trigger**: "A bad car accident"
- **Response**: Ask 2-3 specific questions:
  - "Was the person trapped/helpless or in control?"
  - "Were others involved (passenger, driver of other car)?"
  - "What was the primary emotion: fear of death, guilt, anger at other driver?"
- **Or**: Generate best-effort answer with low confidence (0.4-0.6) and list assumptions

**Unclear power scope**: "Can control fire"
- **Response**: Ask for specifics:
  - "Can they generate fire or only control existing flames?"
  - "What's the range and scale (lighter vs forest fire)?"
  - "Can they control temperature or just shape/movement?"
- **Or**: Generate multiple variants with different interpretations

### Anti-Hallucination Measures

1. **Always cite sources**: Reference PDF page or wiki section
2. **Mark inferences explicitly**: "Inference: based on similar patterns in TINKERS.pdf#p45"
3. **Use confidence scores**: 0.0-1.0, where <0.5 means high uncertainty
4. **Prefer "unknown" over guessing**: Better to say "insufficient data" than fabricate
5. **Cross-reference examples**: Check against canon characters with similar powers
6. **Question assumptions**: Include "questions_for_user" section in output

## Examples and Test Cases

See `TESTS.md` for 20+ detailed examples covering:
- 10 trigger_to_power scenarios (various classifications)
- 10 power_to_trigger reverse engineering cases
- Multitrigger/cluster examples
- Edge cases (second triggers, cauldron powers, Manton bypass)
- Bilingual examples (RU/EN)

## Implementation Notes

### Knowledge Base Access

The skill uses `worm_knowledge_base.json` (549KB) containing:
- 17 PDF sources (270 pages of extracted text)
- 3 wiki page snapshots
- Searchable by keyword, classification type, or trigger pattern

### Recommendation for API/LLM Integration

When integrating this skill:
1. **Load knowledge base once** at initialization (JSON parse)
2. **Implement semantic search** over trigger examples and power descriptions
3. **Use few-shot examples** from TESTS.md in prompts
4. **Temperature 0.7-0.8** for creative but consistent generation
5. **Max tokens ≥1500** for detailed outputs
6. **Validate JSON output** against schema before returning

### Recommended Enhancements

- **Vector database**: Embed all trigger/power examples for RAG
- **Caching**: Common classifications (Master, Brute, Thinker)
- **User feedback loop**: Learn from accepted/rejected generations
- **Canon character database**: Cross-reference with ~300 known Worm capes

## Limitations

1. **Not a substitute for reading Worm**: Skill is optimized for generation, not deep lore discussion
2. **Post-canon speculation**: Ward and post-Gold Morning mechanics are partial coverage
3. **Subjective ratings**: PRT ratings are in-universe assessments, not objective power metrics
4. **Creativity bounds**: Novel power combinations may lack direct precedent
5. **Language limitations**: RU translations are partial (7 PDFs), EN sources dominate

## Version History

- **v1.0** (2026-01-19): Initial release
  - 17 PDF sources processed
  - 3 wiki pages integrated
  - Bidirectional generation support
  - Full PRT classification system (12 types × 12 ratings)
  - RU/EN bilingual support

---

**Skill created with**: Claude Code + MCP Skill Seekers
**Knowledge base generated**: 2026-01-19
**Total documentation**: 270 pages + 3 wiki articles
