#!/usr/bin/env python3
"""
Worm Trigger-Power PRT Classification Skill
Main processor module for bidirectional trigger↔power generation
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass


@dataclass
class Classification:
    """PRT Classification type with rating."""
    type_ru: str
    type_en: str
    rating: int  # 1-12
    primary: bool
    justification: str


@dataclass
class ReasoningStep:
    """Single reasoning step with source citation."""
    point: str
    because: str
    sources: List[str]


class WormSkill:
    """Main skill processor."""

    # PRT Classification mapping
    CLASSIFICATIONS = {
        "brute": {"ru": "Бугай", "en": "Brute"},
        "mover": {"ru": "Ловкач", "en": "Mover"},
        "shaker": {"ru": "Шейкер", "en": "Shaker"},
        "blaster": {"ru": "Бластер", "en": "Blaster"},
        "striker": {"ru": "Страйкер", "en": "Striker"},
        "changer": {"ru": "Чейнджер", "en": "Changer"},
        "stranger": {"ru": "Незаметник", "en": "Stranger"},
        "master": {"ru": "Повелитель", "en": "Master"},
        "thinker": {"ru": "Мыслитель", "en": "Thinker"},
        "tinker": {"ru": "Технарь", "en": "Tinker"},
        "breaker": {"ru": "Излом", "en": "Breaker"},
        "trump": {"ru": "Козырь", "en": "Trump"},
    }

    # Trigger type keywords (for power_to_trigger inference)
    TRIGGER_KEYWORDS = {
        "brute": ["physical damage", "endurance", "pain", "injury", "assault", "beating"],
        "mover": ["confinement", "trapped", "pursuit", "escape", "restricted movement"],
        "shaker": ["environmental", "surrounded", "territory", "area threat", "hazard"],
        "blaster": ["distance", "ranged threat", "keep away", "long-range"],
        "striker": ["close-quarters", "touch", "intimate", "melee", "personal"],
        "changer": ["identity crisis", "transform", "be someone else", "body dysphoria"],
        "stranger": ["exposure", "hiding", "noticed", "escape attention", "social visibility"],
        "master": ["social isolation", "helpless", "control loss", "betrayal by group"],
        "thinker": ["information deficit", "don't understand", "missing knowledge", "confusion"],
        "tinker": ["need tools", "problem to solve", "lack resources", "preparation time"],
        "breaker": ["escape reality", "leave body", "unbearable present", "altered state"],
        "trump": ["parahuman conflict", "betrayed by powers", "power used against", "cape fight"],
    }

    def __init__(self, knowledge_base_path: str = "worm_knowledge_base.json"):
        """Initialize skill with knowledge base."""
        self.kb_path = Path(knowledge_base_path)
        self.knowledge_base = self._load_knowledge_base()

    def _load_knowledge_base(self) -> Dict[str, Any]:
        """Load knowledge base from JSON."""
        if not self.kb_path.exists():
            raise FileNotFoundError(f"Knowledge base not found: {self.kb_path}")

        with open(self.kb_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main processing endpoint.

        Args:
            input_data: JSON input matching schema in SKILL.md

        Returns:
            JSON output matching schema in SKILL.md
        """
        mode = input_data.get("mode")

        if mode == "trigger_to_power":
            return self._trigger_to_power(input_data)
        elif mode == "power_to_trigger":
            return self._power_to_trigger(input_data)
        else:
            raise ValueError(f"Unknown mode: {mode}. Use 'trigger_to_power' or 'power_to_trigger'")

    def _trigger_to_power(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate power from trigger description.

        This is a reference implementation. For production use, integrate with
        LLM API (Claude, GPT-4, etc.) using the SKILL.md prompt and few-shot
        examples from TESTS.md.
        """
        trigger_desc = input_data["trigger_description"]
        language = input_data.get("language", "en")

        # Analyze trigger (simplified keyword matching)
        trigger_analysis = self._analyze_trigger(trigger_desc)

        # Generate classification
        classifications = self._infer_classifications_from_trigger(trigger_analysis)

        # Build response
        return {
            "mode": "trigger_to_power",
            "input_summary": trigger_desc[:200] + "..." if len(trigger_desc) > 200 else trigger_desc,
            "output": {
                "power_description": "[LLM GENERATION REQUIRED] Use SKILL.md prompt with trigger context",
                "classification": [
                    {
                        "type_ru": self.CLASSIFICATIONS[c["type"]]["ru"],
                        "type_en": self.CLASSIFICATIONS[c["type"]]["en"],
                        "rating": c["rating"],
                        "primary": c["primary"],
                        "justification": c["justification"]
                    }
                    for c in classifications
                ],
                "limitations": ["[LLM GENERATION REQUIRED]"],
                "secondary_effects": ["[LLM GENERATION REQUIRED]"],
                "counterplay": ["[LLM GENERATION REQUIRED]"],
                "reasoning": [
                    {
                        "point": "Classification based on trigger analysis",
                        "because": f"Detected keywords: {', '.join(trigger_analysis['keywords'][:3])}",
                        "sources": ["worm_knowledge_base.json", "SKILL.md"]
                    }
                ],
                "confidence": 0.5,  # Low confidence without LLM
                "questions_for_user": self._generate_clarifying_questions(trigger_analysis)
            }
        }

    def _power_to_trigger(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate trigger(s) from power description.

        This is a reference implementation. For production use, integrate with
        LLM API using the SKILL.md prompt and few-shot examples from TESTS.md.
        """
        power_desc = input_data["power_description"]
        num_variants = input_data.get("num_variants", 1)
        known_class = input_data.get("known_classification")

        # Analyze power
        power_analysis = self._analyze_power(power_desc, known_class)

        # Generate classification if not provided
        classifications = self._infer_classifications_from_power(power_analysis)

        # Build response
        return {
            "mode": "power_to_trigger",
            "input_summary": power_desc[:200] + "..." if len(power_desc) > 200 else power_desc,
            "output": {
                "trigger_variants": [
                    {
                        "variant_number": i + 1,
                        "probability": "most_likely" if i == 0 else "alternative",
                        "trigger_description": "[LLM GENERATION REQUIRED] Use SKILL.md prompt with power context",
                        "trigger_analysis": {
                            "emotional_core": power_analysis["likely_emotions"][i] if i < len(power_analysis["likely_emotions"]) else "Unknown",
                            "threat_type": power_analysis["threat_type"],
                            "duration": "Unknown",
                            "locus_of_blame": "Unknown"
                        }
                    }
                    for i in range(num_variants)
                ],
                "classification": [
                    {
                        "type_ru": self.CLASSIFICATIONS[c["type"]]["ru"],
                        "type_en": self.CLASSIFICATIONS[c["type"]]["en"],
                        "rating": c["rating"],
                        "primary": c["primary"],
                        "justification": c["justification"]
                    }
                    for c in classifications
                ],
                "limitations": ["[LLM GENERATION REQUIRED]"],
                "secondary_effects": ["[LLM GENERATION REQUIRED]"],
                "counterplay": ["[LLM GENERATION REQUIRED]"],
                "reasoning": [
                    {
                        "point": "Classification inferred from power mechanics",
                        "because": f"Detected types: {', '.join([c['type'] for c in classifications])}",
                        "sources": ["worm_knowledge_base.json", "SKILL.md"]
                    }
                ],
                "confidence": 0.5,
                "questions_for_user": [
                    "Are there any limitations not mentioned in the power description?",
                    "Is this power part of a cluster trigger?"
                ]
            }
        }

    def _analyze_trigger(self, trigger_desc: str) -> Dict[str, Any]:
        """Analyze trigger description to extract key features."""
        trigger_lower = trigger_desc.lower()
        detected_types = []

        # Keyword matching
        for trigger_type, keywords in self.TRIGGER_KEYWORDS.items():
            if any(kw in trigger_lower for kw in keywords):
                detected_types.append(trigger_type)

        # Emotion detection (simplified)
        emotions = []
        emotion_keywords = {
            "helpless": ["helpless", "powerless", "unable", "can't", "couldn't"],
            "isolation": ["alone", "isolated", "abandoned", "nobody", "no one"],
            "disgust": ["disgust", "revolting", "filthy", "gross", "vile"],
            "rage": ["rage", "anger", "fury", "hate", "enraged"],
            "fear": ["fear", "terror", "afraid", "scared", "frightened"],
            "betrayal": ["betray", "trust", "backstab", "deceive", "lied"],
        }

        for emotion, keywords in emotion_keywords.items():
            if any(kw in trigger_lower for kw in keywords):
                emotions.append(emotion)

        return {
            "types": detected_types[:3],  # Top 3
            "keywords": [kw for kws in [self.TRIGGER_KEYWORDS[t] for t in detected_types[:2]] for kw in kws[:2]],
            "emotions": emotions,
            "text_length": len(trigger_desc)
        }

    def _analyze_power(self, power_desc: str, known_class: Optional[str] = None) -> Dict[str, Any]:
        """Analyze power description to extract key features."""
        power_lower = power_desc.lower()

        # Parse known classification if provided
        parsed_class = self._parse_classification(known_class) if known_class else []

        # Detect power mechanics
        mechanics = {
            "control": "control" in power_lower or "command" in power_lower,
            "transformation": "transform" in power_lower or "change" in power_lower,
            "projectile": "shoot" in power_lower or "blast" in power_lower or "throw" in power_lower,
            "touch": "touch" in power_lower or "contact" in power_lower,
            "area": "area" in power_lower or "zone" in power_lower or "radius" in power_lower,
            "information": "sense" in power_lower or "know" in power_lower or "detect" in power_lower,
        }

        # Map mechanics to likely trigger emotions
        emotion_map = {
            "control": ["helpless", "loss of control"],
            "transformation": ["identity crisis", "need to change"],
            "touch": ["intimacy", "violation"],
            "area": ["surrounded", "environmental threat"],
        }

        likely_emotions = []
        for mechanic, present in mechanics.items():
            if present and mechanic in emotion_map:
                likely_emotions.extend(emotion_map[mechanic])

        return {
            "parsed_classification": parsed_class,
            "mechanics": mechanics,
            "likely_emotions": likely_emotions[:3],
            "threat_type": "Unknown",  # Would need LLM
            "text_length": len(power_desc)
        }

    def _infer_classifications_from_trigger(self, analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Infer PRT classifications from trigger analysis."""
        classifications = []

        for i, ttype in enumerate(analysis["types"][:2]):  # Primary + secondary
            classifications.append({
                "type": ttype,
                "rating": 5,  # Default mid-range (would need LLM for accurate rating)
                "primary": i == 0,
                "justification": f"Trigger analysis suggests {ttype} classification"
            })

        if not classifications:
            # Fallback
            classifications.append({
                "type": "master",
                "rating": 4,
                "primary": True,
                "justification": "Default classification - insufficient trigger detail"
            })

        return classifications

    def _infer_classifications_from_power(self, analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Infer PRT classifications from power analysis."""
        if analysis["parsed_classification"]:
            return analysis["parsed_classification"]

        # Infer from mechanics
        classifications = []
        mechanics = analysis["mechanics"]

        if mechanics["control"]:
            classifications.append({"type": "master", "rating": 6, "primary": True, "justification": "Control-based power"})
        if mechanics["transformation"]:
            classifications.append({"type": "changer", "rating": 5, "primary": not classifications, "justification": "Transformation ability"})
        if mechanics["projectile"]:
            classifications.append({"type": "blaster", "rating": 6, "primary": not classifications, "justification": "Ranged attack"})
        if mechanics["touch"]:
            classifications.append({"type": "striker", "rating": 7, "primary": not classifications, "justification": "Touch-based effect"})
        if mechanics["area"]:
            classifications.append({"type": "shaker", "rating": 6, "primary": not classifications, "justification": "Area control"})

        if not classifications:
            classifications.append({"type": "brute", "rating": 4, "primary": True, "justification": "Default classification"})

        return classifications[:2]  # Primary + secondary

    def _parse_classification(self, class_str: str) -> List[Dict[str, Any]]:
        """Parse classification string like 'Master 8 / Thinker 3'."""
        classifications = []
        parts = class_str.split("/")

        for i, part in enumerate(parts):
            part = part.strip()
            match = re.match(r"(\w+)\s*(\d+)", part)
            if match:
                class_name = match.group(1).lower()
                rating = int(match.group(2))

                if class_name in self.CLASSIFICATIONS:
                    classifications.append({
                        "type": class_name,
                        "rating": rating,
                        "primary": i == 0,
                        "justification": "From known classification"
                    })

        return classifications

    def _generate_clarifying_questions(self, analysis: Dict[str, Any]) -> List[str]:
        """Generate clarifying questions based on analysis."""
        questions = []

        if not analysis["emotions"]:
            questions.append("What was the primary emotion during the trigger event?")

        if len(analysis["types"]) > 2:
            questions.append("Which aspect of the trigger was most traumatic?")

        if analysis["text_length"] < 100:
            questions.append("Can you provide more details about the trigger circumstances?")

        return questions[:3]  # Max 3 questions

    def search_knowledge_base(self, query: str, source_types: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        """
        Search knowledge base for relevant information.

        Args:
            query: Search query (keywords)
            source_types: Filter by source type (["pdf", "wiki"])

        Returns:
            List of matching entries with context
        """
        results = []
        query_lower = query.lower()

        for source_name, source_data in self.knowledge_base["sources"].items():
            if source_types and source_data["type"] not in source_types:
                continue

            if source_data["type"] == "pdf":
                for page_data in source_data.get("content", []):
                    text = page_data["text"].lower()
                    if query_lower in text:
                        results.append({
                            "source": source_name,
                            "type": "pdf",
                            "page": page_data["page"],
                            "snippet": self._extract_snippet(page_data["text"], query_lower)
                        })

            elif source_data["type"] == "wiki":
                if source_data.get("status") == "success":
                    content = source_data.get("raw_html", "").lower()
                    if query_lower in content:
                        results.append({
                            "source": source_name,
                            "type": "wiki",
                            "url": source_data["url"],
                            "snippet": f"Found '{query}' in {source_name}"
                        })

        return results[:10]  # Top 10 results

    def _extract_snippet(self, text: str, query: str, context_chars: int = 150) -> str:
        """Extract snippet around query match."""
        text_lower = text.lower()
        idx = text_lower.find(query)

        if idx == -1:
            return text[:context_chars]

        start = max(0, idx - context_chars // 2)
        end = min(len(text), idx + len(query) + context_chars // 2)

        snippet = text[start:end]
        if start > 0:
            snippet = "..." + snippet
        if end < len(text):
            snippet = snippet + "..."

        return snippet


# CLI interface
def main():
    import sys
    import io

    # Fix Windows console encoding
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

    skill = WormSkill()

    print("=== Worm Trigger-Power PRT Skill ===")
    print("Mode: 1) trigger_to_power  2) power_to_trigger  3) search")
    mode_choice = input("Select mode (1/2/3): ").strip()

    if mode_choice == "1":
        print("\nEnter trigger description:")
        trigger = input("> ")
        result = skill.process({
            "mode": "trigger_to_power",
            "trigger_description": trigger
        })
        print("\n" + json.dumps(result, ensure_ascii=False, indent=2))

    elif mode_choice == "2":
        print("\nEnter power description:")
        power = input("> ")
        result = skill.process({
            "mode": "power_to_trigger",
            "power_description": power
        })
        print("\n" + json.dumps(result, ensure_ascii=False, indent=2))

    elif mode_choice == "3":
        print("\nEnter search query:")
        query = input("> ")
        results = skill.search_knowledge_base(query)
        print(f"\n{len(results)} results found:\n")
        for r in results:
            print(f"[{r['source']}] {r.get('page', 'N/A')}")
            print(f"  {r['snippet']}\n")

    else:
        print("Invalid choice")
        sys.exit(1)


if __name__ == "__main__":
    main()
