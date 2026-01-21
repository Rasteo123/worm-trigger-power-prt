# Worm Trigger-Power Test Examples

This document contains 20+ test cases for validating the skill's trigger↔power generation logic.

## Part 1: trigger_to_power Examples

### Example 1: Classic Master Trigger (Taylor Hebert)

**Input:**
```json
{
  "mode": "trigger_to_power",
  "trigger_description": "15-year-old girl is locked in a school locker filled with used tampons and biohazard waste for hours during winter break. She feels utterly helpless, socially isolated (her former best friend led the bullies), and disgusted by her situation. Students mock her from outside.",
  "language": "en"
}
```

**Expected Output:**
- Primary: Master 8 (large-scale minion control, social isolation trigger)
- Secondary: Thinker 3 (multitasking enhancement required for control)
- Power: Control over arthropods (insects, arachnids) within several blocks
- Justification: Social isolation + helplessness = Master; disgust element → "disgusting" minions (bugs); extended duration = complex power

---

### Example 2: Brute/Striker Combo

**Input:**
```json
{
  "mode": "trigger_to_power",
  "trigger_description": "Teenage boy is jumped by gang members in an alley. He's beaten badly, knows he can't escape, and feels rage at his inability to fight back. Multiple attackers overwhelming him with close-range violence.",
  "language": "en"
}
```

**Expected Output:**
- Primary: Brute 4 (physical damage trigger)
- Secondary: Striker 3 (close-quarters, touch-based escalation)
- Power: Increased strength and durability that ramps up when taking damage; touch-based effect that weakens opponents
- Justification: Physical assault = Brute; close-quarters + rage at attackers = Striker component

---

### Example 3: Tinker Trigger (Extended)

**Input:**
```json
{
  "mode": "trigger_to_power",
  "trigger_description": "Engineering student spends weeks trying to build a life-saving device for their dying parent, but lacks the resources, knowledge, and time. Watches parent deteriorate over months, feeling like they're failing despite their best efforts.",
  "language": "en"
}
```

**Expected Output:**
- Primary: Tinker 5 (medical/life support specialty)
- Secondary: Possible Shaker 2 (if powers involve area-effect medical devices)
- Power: Ability to build advanced medical technology, life support systems, perhaps biotech
- Justification: Extended trigger (months) + problem requiring specialized tools = Tinker; medical theme from parent's illness

---

### Example 4: Shaker/Blaster Terrain Control

**Input:**
```json
{
  "mode": "trigger_to_power",
  "trigger_description": "Wildfire surrounds a firefighter. They watch the flames cut off all escape routes and advance on their position. Environmental threat on all sides, no safe ground, needs to control the space or die.",
  "language": "en"
}
```

**Expected Output:**
- Primary: Shaker 6 (environmental threat, area control needed)
- Secondary: Blaster 4 (ranged element if can project effect)
- Power: Create zones of altered temperature or flame-retardant barriers in large area; possibly manipulate existing fire
- Justification: Environmental threat surrounding victim = Shaker; fire theme literal; high rating due to scale of wildfire

---

### Example 5: Stranger Social Exposure

**Input:**
```json
{
  "mode": "trigger_to_power",
  "trigger_description": "A closeted LGBTQ+ teen is outed at school assembly when private messages are projected on screen. Everyone is staring, laughing, judging. They want to disappear, to never be seen by these people again.",
  "language": "en"
}
```

**Expected Output:**
- Primary: Stranger 5 (social exposure, need to hide)
- Secondary: Possible Master 2 (if powers involve perception manipulation of others)
- Power: Ability to make self forgettable/unnoticeable; people fail to register their presence or remember interactions
- Justification: Public humiliation + need to escape notice = Stranger; perception-based rather than invisibility (more psychological)

---

### Example 6: Breaker Escape Reality

**Input:**
```json
{
  "mode": "trigger_to_power",
  "trigger_description": "Car crash victim trapped in burning vehicle, doors jammed, seatbelt stuck. Intense pain and heat, feels their body failing, desperately wants to be anywhere but in their own skin right now.",
  "language": "en"
}
```

**Expected Output:**
- Primary: Breaker 6 (need to escape physical reality/body)
- Secondary: Mover 3 (if breaker state allows escape from confinement)
- Power: Transform into altered state (possibly intangible, fire-resistant, or energy form) that escapes normal physics
- Justification: Trapped + need to escape own body = Breaker; fire/pain theme suggests breaker state with relevant immunity

---

### Example 7: Trump Betrayal

**Input:**
```json
{
  "mode": "trigger_to_power",
  "trigger_description": "Parahuman hero is betrayed by their team during critical mission. Powers are used against them, feel utterly helpless against abilities they once fought beside. Trust shattered.",
  "language": "en"
}
```

**Expected Output:**
- Primary: Trump 7 (betrayal by parahumans, power-focused trauma)
- Secondary: Possible Stranger 3 or Master 2 (depending on mechanism)
- Power: Ability to copy, nullify, or manipulate other parahumans' powers; possibly only powers of those they've been betrayed by
- Justification: Conflict with other parahumans = Trump; betrayal theme suggests power theft/copying

---

### Example 8: Mover Confinement

**Input:**
```json
{
  "mode": "trigger_to_power",
  "trigger_description": "Hostage is bound and gagged in a basement for days. Hears footsteps approaching repeatedly, never knowing when captor will return. Desperate need to escape confinement and flee.",
  "language": "en"
}
```

**Expected Output:**
- Primary: Mover 5 (confinement, restriction of movement)
- Secondary: Possible Stranger 3 (if power involves stealth/escape)
- Power: Teleportation with limitations (line of sight, only to shadows, requires fear/stress), or enhanced speed/climbing
- Justification: Physical confinement + need for mobility = Mover; extended duration suggests complex power

---

### Example 9: Thinker Information Deficit

**Input:**
```json
{
  "mode": "trigger_to_power",
  "trigger_description": "Detective investigates case involving murdered family. All evidence points to them being the killer due to elaborate frame job. Can't figure out who's setting them up, feels like they're missing crucial information that would prove innocence.",
  "language": "en"
}
```

**Expected Output:**
- Primary: Thinker 6 (information deficit, need to understand)
- Secondary: Possible Stranger 2 (if power involves reading others' intentions)
- Power: Enhanced deductive reasoning, postcognition (seeing past events), or lie detection; possibly reads "evidence" that others miss
- Justification: Lack of information + investigative context = Thinker; theme suggests forensic/detective specialty

---

### Example 10: Changer Identity Crisis

**Input (RU):**
```json
{
  "mode": "trigger_to_power",
  "trigger_description": "Трансгендерная девушка не может позволить себе транзицию, постоянно испытывает дисфорию при взгляде в зеркало. Семья заставляет её притворяться кем-то, кем она не является. Отчаянно хочет изменить своё тело.",
  "language": "ru"
}
```

**Expected Output:**
- Primary: Чейнджер 4 (Changer 4) (identity crisis, need to transform self)
- Secondary: Possible Излом 2 (Breaker 2) if transformation is extreme
- Power: Ability to alter physical appearance, possibly gender presentation; transformations feel more "real" than baseline form
- Justification: Identity crisis + need to change body = Changer; theme directly tied to body dysphoria

---

## Part 2: power_to_trigger Examples

### Example 11: Reverse Engineer Lung

**Input:**
```json
{
  "mode": "power_to_trigger",
  "power_description": "Can transform into draconic form that continually escalates in size, strength, and pyrokinetic power the longer combat continues. Nearly invincible at peak escalation.",
  "known_classification": "Brute 9 / Changer 8 / Blaster 7",
  "num_variants": 2
}
```

**Expected Output:**
- **Trigger Variant 1 (Most Likely)**: Extended combat scenario where victim must endure and escalate to survive. Possibly gang warfare in youth, needing to become a "dragon" (metaphorically dominant) to protect others or establish territory.
- **Trigger Variant 2 (Alternative)**: Humiliation/emasculation scenario where victim needs to prove themselves increasingly dangerous; transformation represents becoming the "monster" others feared.
- Justification: Brute (physical threat) + Changer (transformation need) + Blaster (ranged capability) + Escalation mechanic (prolonged threat)

---

### Example 12: Reverse Engineer Flechette/Foil

**Input:**
```json
{
  "mode": "power_to_trigger",
  "power_description": "Can imbue objects (arrows, bolts, rebar) with an energy charge that causes them to phase through any material and ignore exotic defenses. Timed detonation option. Manton limit bypass (can affect living tissue).",
  "language": "en"
}
```

**Expected Output:**
- Primary: Striker 9 / Blaster 6 (touch-based imbuing + ranged application)
- **Trigger Variant**: Close-quarters scenario where victim faced opponent with overwhelming defense they couldn't penetrate. Possibly abusive relationship with power dynamic (can't "get through" to abuser). Striker suggests touch/intimacy element; Manton bypass suggests desperation to affect a person directly.
- Justification: Striker primary (imbues objects via touch), Blaster secondary (throws/shoots imbued objects); Manton bypass suggests trigger involved needing to harm/stop a specific person

---

### Example 13: Reverse Engineer Grue

**Input:**
```json
{
  "mode": "power_to_trigger",
  "power_description": "Generates opaque darkness that blocks all light and dampens sound. Those inside experience extreme sensory deprivation. Can expand area significantly.",
  "known_classification": "Shaker 7 / Stranger 4"
}
```

**Expected Output:**
- **Trigger Variant**: Witness to violence against sibling or loved one, unable to stop it, wants to hide/obscure the situation. Alternatively: victim of spotlight/interrogation who needs to create concealment and confusion. Shaker (area control) + Stranger (hiding/deception) suggests need to obscure an environment + escape notice.
- Justification: Darkness theme = hiding/concealment; sensory deprivation could relate to feeling "blocked out" or needing to disorient others

---

### Example 14: Reverse Engineer Skitter's Canon Trigger

**Input:**
```json
{
  "mode": "power_to_trigger",
  "power_description": "Контроль над всеми членистоногими в радиусе нескольких кварталов. Идеальная многозадачность — способность управлять тысячами существ одновременно с полным осознанием. Возможность использовать их чувства. Не работает на людях.",
  "language": "ru"
}
```

**Expected Output:**
- Primary: Повелитель 8 / Мыслитель 3 (Master 8 / Thinker 3)
- **Trigger Variant**: Социальная изоляция + беспомощность + отвращение. Возможный сценарий: издевательства в школе, заперли в тесном пространстве с чем-то отвратительным (насекомые, отходы), бывшие друзья предали. Длительная травма (часы). Элемент отвращения объясняет членистоногих как "миньонов".
- Justification: Большая площадь контроля + социальная изоляция = Master; многозадачность = Thinker вторичная; насекомые = метафора отвращения/изоляции

---

### Example 15: Reverse Engineer Bitch/Hellhound

**Input:**
```json
{
  "mode": "power_to_trigger",
  "power_description": "Can transform dogs into massive monstrous forms with enhanced strength, durability, and aggression. Requires physical contact with dogs. Only works on canines. Transformations are temporary but powerful.",
  "known_classification": "Master 6 / Changer 3"
}
```

**Expected Output:**
- **Trigger Variant 1**: Victim of abuse (likely foster care) where only companion was a dog. Needed protection but felt helpless; wanted dog to be big/strong enough to defend her. Master (minion control) + Changer (transformation) + specific to dogs (emotional attachment).
- **Trigger Variant 2**: Scenario where victim and dog were both threatened; needed to "empower" the dog to protect both of them.
- Justification: Master (controls enhanced minions) focused on dogs suggests strong emotional bond; Changer aspect (transforms dogs) indicates need to alter ally, not self

---

### Example 16: Reverse Engineer Panacea

**Input:**
```json
{
  "mode": "power_to_trigger",
  "power_description": "Touch-based biokinesis: can sense and alter any biological tissue at cellular level. Cannot affect own body or brains. Extremely versatile for healing or harm. Requires sustained contact.",
  "known_classification": "Striker 12 / Shaker 2"
}
```

**Expected Output:**
- **Trigger Variant**: Medical emergency involving loved one (likely sister or family member). Victim is helpless, watching them suffer/die, desperately wants to "fix" them but lacks ability. Touch-based suggests intimacy/closeness. Striker 12 rating indicates Manton bypass potential. Cannot affect self = shard restriction, possibly related to trigger involving helping *others* not self.
- Justification: Striker (touch-based); medical theme; high rating from versatility and Manton bypass; brain restriction is shard limitation to prevent instant mind control

---

### Example 17: Reverse Engineer Clockblocker

**Input:**
```json
{
  "mode": "power_to_trigger",
  "power_description": "Can freeze objects in time for unpredictable duration (seconds to hours). Frozen objects become invulnerable and immovable. Touch-based activation. Cannot control duration.",
  "known_classification": "Striker 7 / Shaker 3"
}
```

**Expected Output:**
- **Trigger Variant**: Dying parent with terminal illness. Victim wants to "freeze" time, make moment last forever, prevent inevitable loss. Striker (touch-based) suggests intimacy. Unpredictable duration = shard's ironic twist (can't control how long parent's suffering is extended). Alternatively: accident victim who wishes they could "pause" the moment before disaster.
- Justification: Time-stop theme = desire to freeze moment; touch-based = personal connection; invulnerability = protective instinct

---

### Example 18: Reverse Engineer Glory Girl

**Input:**
```json
{
  "mode": "power_to_trigger",
  "power_description": "Flight, super strength, invincible forcefield (regenerates after breaking). Emotion aura that inspires awe in allies and fear in enemies. Alexandria package minus speed.",
  "known_classification": "Brute 5 / Mover 3 / Shaker 3"
}
```

**Expected Output:**
- **Trigger Variant**: Scenario requiring victim to be "larger than life" protector figure. Possibly saving sibling from danger, needing to be strong, fast, and intimidating all at once. Emotion aura suggests social component (need to inspire/intimidate). Alexandria package (flight + strength + shield) indicates multi-threat trigger: needed mobility, power, and protection simultaneously.
- Justification: Brute (forcefield), Mover (flight), Shaker (aura); "hero package" suggests trigger where victim needed to be heroic protector

---

### Example 19: Reverse Engineer Shadow Stalker

**Input:**
```json
{
  "mode": "power_to_trigger",
  "power_description": "Can enter breaker state as living shadow: intangible, can phase through matter, enhanced mobility on walls/ceilings. Cannot interact with physical world while in shadow state. Must exit to attack.",
  "known_classification": "Breaker 6 / Mover 4 / Stranger 3"
}
```

**Expected Output:**
- **Trigger Variant**: Victim of stalking, assault, or home invasion. Needed to escape through walls, hide in shadows, become untouchable. Breaker (escape reality) + Mover (mobility) + Stranger (stealth). Shadow theme suggests hiding/predator avoidance. Limitation (can't attack while intangible) = shard forcing conflict (must become vulnerable to engage).
- Justification: Breaker primary (altered state), Mover (enhanced mobility), Stranger (stealth in shadows); shadow theme = hiding/escape

---

### Example 20: Reverse Engineer Oni Lee

**Input:**
```json
{
  "mode": "power_to_trigger",
  "power_description": "Teleports short range, leaving behind perfect duplicate that persists for seconds before crumbling to ash. Clone can act independently during its lifespan. Spammable.",
  "known_classification": "Mover 6 / Stranger 4 / Master 2"
}
```

**Expected Output:**
- **Trigger Variant**: Identity crisis + need for escape. Possibly suicide attempt survivor or scenario where victim felt "already dead" but needed to keep moving. Mover (teleport) + Master (creates minion/copy) + Stranger (duplicates confuse). Clone degradation = shard's commentary on victim feeling "disposable" or "hollowed out."
- Justification: Teleport (mobility need), clone creation (fractured identity), ash disintegration (self-destruction theme)

---

## Part 3: Edge Cases and Special Scenarios

### Example 21: Cluster Trigger (Multitrigger)

**Input:**
```json
{
  "mode": "trigger_to_power",
  "trigger_description": "Three college roommates in car crash. Driver feels guilt, front passenger feels helpless, back passenger feels betrayed (driver was drunk). All trigger simultaneously from shared trauma with different emotional cores.",
  "language": "en"
}
```

**Expected Output:**
- **Driver**: Primary Mover (escape/guilt) + secondary Shaker from passengers
- **Front Passenger**: Primary Brute (endure crash) + secondary Mover from driver
- **Back Passenger**: Primary Trump/Striker (betrayal) + secondary Brute from front passenger
- **Cluster Mechanics**: Powers interact, can sense each other, minor Trump dynamic
- Justification: Shared trigger event = cluster (Sample Multitrigger.pdf); different emotional cores = different primaries; shared secondaries from bud connection

---

### Example 22: Second Trigger

**Input:**
```json
{
  "mode": "trigger_to_power",
  "trigger_description": "Existing parahuman (Mover 4: short-range teleport) is trapped by Bakuda's time-stop bomb. Experiences subjective centuries frozen in time, aware but unable to move. Eventually second-triggers from extreme psychological stress.",
  "language": "en"
}
```

**Expected Output:**
- **Original Power**: Mover 4 (short-range teleport)
- **Second Trigger Enhancement**: Teleport now has "time-skip" component: appears to teleport but actually moves through frozen time, experiencing duration but undetectable to others. Mover 7 / Breaker 4.
- Justification: Second trigger intensifies existing power + adds new dimension related to trauma (time manipulation); rating increase reflects power boost

---

### Example 23: Cauldron Vial (Artificial Trigger)

**Input:**
```json
{
  "mode": "power_to_trigger",
  "power_description": "Can transform into living battery: generates enormous electricity, invulnerable while charging, can release as devastating blast. No clear thematic connection or limitations typical of natural triggers.",
  "num_variants": 1
}
```

**Expected Output:**
- **Assessment**: Likely Cauldron vial, not natural trigger
- **Reasoning**:
  - No obvious emotional core or trauma theme
  - Too straightforward (no ironic twist)
  - Very high power without proportional drawbacks
  - "Living battery" lacks narrative connection to trigger
- **If natural trigger (speculation)**: Would require electrical accident + need to "power through" something, but extremely unlikely given power cleanliness
- Confidence: 0.3 (probably Cauldron)

---

### Example 24: Manton Bypass Example

**Input:**
```json
{
  "mode": "trigger_to_power",
  "trigger_description": "Medical student watches helplessly as shooting victim bleeds out. Can't stop bleeding, has theoretical knowledge but lacks tools/ability. Victim is friend, very personal. Intense medical trauma.",
  "language": "en"
}
```

**Expected Output:**
- Primary: Striker 8 / Shaker 3
- Power: Touch-based biokinesis focused on blood manipulation. Can control blood flow, coagulation, oxygen transport. **Manton limit partially bypassed** (can affect living human blood). Range extends slightly beyond touch (blood remains connected).
- **Rating boost**: +2 for Manton bypass (Striker 6 → 8)
- Justification: Medical trigger + intimacy (friend) = Striker; blood theme direct from trigger; Manton bypass due to desperate need to affect *person* not object; Shaker component if can manipulate blood outside body

---

### Example 25: Trump Power Nullification

**Input (RU):**
```json
{
  "mode": "power_to_trigger",
  "power_description": "Создаёт поле подавления сил паралюдей в радиусе 50 метров. Все способности внутри поля ослабляются или полностью отключаются. Не влияет на физические изменения (например, если кто-то уже трансформировался).",
  "language": "ru"
}
```

**Expected Output:**
- Primary: Козырь 7 / Шейкер 5 (Trump 7 / Shaker 5)
- **Trigger Variant**: Паралюди использовали свои силы против триггера или близких. Чувство беспомощности перед "несправедливым преимуществом" способностей. Желание "выровнять игровое поле". Широкая область (50м) = Shaker компонент; подавление сил = Trump.
- **Alternative**: Жертва конфликта между паралюдьми, пострадавшая как "побочный ущерб". Хочет убрать все силы из уравнения.
- Justification: Trump (подавляет силы паралюдей); Shaker (область эффекта); не влияет на физические изменения = ограничение шарда

---

## Test Validation Criteria

For each test case, validate:

1. **Classification Match**: Does generated classification align with expected types?
2. **Rating Reasonableness**: Is 1-12 rating justified by scope/threat level?
3. **Trigger→Power Logic**: Does power thematically connect to trigger (literal or ironic)?
4. **Source Citations**: Are reasoning steps backed by PDF/wiki references?
5. **Consistency**: Do similar triggers produce similar power patterns?
6. **Confidence Calibration**: Are confidence scores appropriate for input detail?
7. **Bilingual Support**: Do RU inputs produce correct RU classification labels?

## Canon Character Cross-Reference

These examples align with canon Worm characters:
- Example 1: Taylor Hebert / Skitter
- Example 11: Lung
- Example 12: Flechette / Foil
- Example 13: Grue
- Example 15: Bitch / Hellhound / Rachel
- Example 16: Panacea / Amy Dallon
- Example 17: Clockblocker / Dennis
- Example 18: Glory Girl / Victoria Dallon
- Example 19: Shadow Stalker / Sophia Hess
- Example 20: Oni Lee

Use these to validate against wiki/PDF canon descriptions.
