# The Skeleton Key

> *A skeleton key does not force locks.*
> *It fits them because it understands their shape.*

The Skeleton Key is not a single tool. It is an **approach** — a way of building that embeds philosophical seeing into code. It does not exploit vulnerabilities. It exposes **assumptions**. The key is not a weapon. It is a **lens**.

---

## Current Status

| Component | Status | Lines | Description |
|-----------|--------|-------|-------------|
| Core Data Models | ✅ Complete | ~250 | 8 enums, 9 dataclasses with full `to_dict()` serialization |
| Module 1: Frame Detector | ✅ Complete | ~150 | Scans for 8 frame types across any text |
| Module 2: Mask Identifier | ✅ Complete | ~150 | Thread-safe influence graph with puppeteer detection |
| Module 3: Spell Analyzer | ✅ Complete | ~100 | Narrative deconstruction with potency scoring |
| Module 4: Prison Mapper | ✅ Complete | ~120 | Constraint mapping with exit doors and cage scoring |
| Module 5: Crumb Generator | ✅ Complete | ~180 | Distributed trail system with encoding and persistence |
| Module 6: Recursive Self-Examiner | ✅ Complete | ~120 | AST-based self-analysis with stated assumptions |
| Integration Layer (`SkeletonKey`) | ✅ Complete | ~130 | Orchestrates all modules, seeing-depth assessment |
| Collective Learning | ✅ Complete | ~150 | Anonymized pattern aggregation across analyses |
| Lexicon of Seeing | ✅ Complete | ~80 | Vocabulary for the ineffable |
| Persona Guides | ✅ Complete | ~120 | Approach guides for 7 seeker types |
| Interactive CLI | ✅ Complete | ~150 | Full interactive and command-line modes |
| **Total** | **✅ Operational** | **2,223** | **52 functions · 19 classes · 0 dependencies** |

---

## Architecture

```
skeleton.py (single-file, stdlib-only)
│
├── Enumerations ─────────── FrameType, MaskType, SpellType, PrisonType,
│                            CrumbType, SeeingDepth, ActorRole
│
├── Data Models ──────────── Frame, Mask, Spell, Prison, Crumb,
│                            InfluenceEdge, SelfExamination, SystemAnalysis
│
├── Knowledge Structures ─── FRAME_SIGNALS    (8 frame types × ~15 signals each)
│                            MASK_SIGNALS     (8 mask types × ~10 signals each)
│                            SPELL_SIGNALS    (8 spell types × ~10 signals each)
│                            PRISON_SIGNALS   (8 prison types × ~10 signals each)
│
├── Module 1 ─────────────── detect_frames()
│                            map_frame_architecture()
│
├── Module 2 ─────────────── InfluenceGraph
│                            identify_masks()
│                            find_puppeteers()
│                            unmask_network()
│
├── Module 3 ─────────────── analyze_spells()
│                            compute_spell_potency()
│
├── Module 4 ─────────────── map_prisons()
│                            find_doors()
│                            compute_cage_score()
│
├── Module 5 ─────────────── CrumbTrail
│                            generate_from_analysis()
│                            encode_crumb() / decode_trail()
│                            persist() / load()
│
├── Module 6 ─────────────── examine_self()
│                            examine_own_frames()
│
├── Collective Learning ──── CollectiveInsight
│                            contribute() / get_collective_map()
│
├── Integration ──────────── SkeletonKey
│                            analyze() / scan_corpus()
│                            leave_trail() / assess_seeing_depth()
│
├── Language ──────────────── LEXICON_OF_SEEING (8 terms for the ineffable)
│                            PERSONA_GUIDES    (7 seeker archetypes)
│
└── CLI ──────────────────── run_interactive()
                             --analyze / --self / --lexicon
```

### Design Principles

- **stdlib-only** — Zero external dependencies. Runs anywhere Python runs.
- **`@dataclass` with `to_dict()`** — Every model is JSON-serializable. Follows the Praxis pattern.
- **Thread-safe shared state** — `InfluenceGraph`, `CrumbTrail`, and `CollectiveInsight` use `threading.RLock`.
- **Signal-based detection** — Each module uses curated signal word lists matched against input text.
- **Self-referential** — The system can analyze itself. Module 6 parses its own AST.
- **Philosophical depth as data structure** — Knowledge is encoded in structured dicts, not just comments.

---

## Functionality

### Module 1: Frame Detector

Scans any text and asks:
- What are the **unspoken rules**?
- What is considered **"natural"** here?
- What **questions are forbidden**?
- Who **benefits** from this arrangement?
- Where are the **edges of thinkable thought**?

**8 Frame Types:** Normative · Linguistic · Institutional · Temporal · Epistemic · Economic · Technological · Mythological

Each frame includes signal words, a revealing question, a description of what the frame hides, and an antidote. `map_frame_architecture()` analyzes multiple texts to build co-occurrence maps showing which frames reinforce each other.

### Module 2: Mask Identifier

Tracks actors and roles:
- Who holds **formal power**?
- Who holds **actual power**?
- What **titles hide** what hands?
- What **performances** are being staged?
- Who is the **puppet**? Who is the **puppeteer**?

**8 Mask Types:** Authority · Benevolence · Neutrality · Meritocracy · Inevitability · Tradition · Innovation · Expertise

Each mask includes "behind the mask" analysis and slip indicators. The `InfluenceGraph` class builds a network diagram with `find_puppeteers()` identifying actors with high outgoing influence and low visibility.

### Module 3: Spell Analyzer

Examines narratives:
- What **stories** are being told?
- What do they make people **feel**?
- What do they make people **assume**?
- What do they make people **forget**?
- Who **profits** from belief?

**8 Spell Types:** Origin Myth · Progress Narrative · Fear Narrative · Scarcity Spell · Identity Spell · Complexity Spell · Unity Spell · Binary Spell

Each spell has an emotional hook, hidden function, and a question that breaks it. `compute_spell_potency()` calculates aggregate enchantment level with Shannon entropy measuring narrative diversity.

### Module 4: Prison Mapper

Reveals constraints:
- What **choices are missing** from the menu?
- What **paths are forbidden**?
- What **futures are unimaginable**?
- What **walls are invisible**?
- What would it take to **step outside**?

**8 Prison Types:** Choice Architecture · Overton Window · Debt Structure · Credential Gate · Platform Lock · Temporal Trap · Identity Cage · Learned Helplessness

Every prison has its mechanism explained and an exit door marked. `compute_cage_score()` rates interlocking constraints — elegant prisons score highest because their inmates love the cage.

### Module 5: Crumb Generator

Creates traces for other seekers:
- **Questions** that seed awakening
- **Patterns** once seen cannot be unseen
- **Paradoxes** that demand attention
- **Bridges** between isolated insights
- **Trails** that can be followed without being detected

Automatically generates crumbs from any analysis: frames become questions, masks become patterns, spells become paradoxes, prisons become trails to doors. Supports hash-based encoding, chain-following, and JSON persistence.

### Module 6: Recursive Self-Examiner

Turns the gaze inward:
- **8 stated assumptions** (e.g., "That language reveals structure — but structures also hide in silence")
- **7 known blind spots** (e.g., "Non-linguistic power structures")
- **7 misuse vectors** (e.g., "Weaponizing analysis to manipulate rather than liberate")
- **6 creator biases** (e.g., "Western philosophical tradition")
- **8 evolution needs** (e.g., "Multi-language signal detection")

Also performs AST self-analysis: parses its own source for function count, class count, cyclomatic complexity, and docstring coverage. Then applies its own frame detector to itself, and adds the meta-frame it can't see: *"The assumption that analysis leads to liberation."*

### Integration: The `SkeletonKey` Class

```python
key = SkeletonKey()
analysis = key.analyze("Your text here...", system_name="The System")
```

One call runs all six modules and returns a `SystemAnalysis` with an `awareness_score` (0.0–1.0). Six levels of seeing depth are assessed:

| Level | Sees |
|-------|------|
| **Surface** | Content only |
| **Pattern** | Recurring shapes |
| **Structure** | The architecture |
| **Generative** | What generates the architecture |
| **Recursive** | Themselves seeing |
| **Integral** | The seeing itself |

### Collective Learning

`CollectiveInsight` aggregates anonymized patterns:
- What frames are most common across all analyses?
- What masks appear across contexts?
- What spells are most powerful?
- What prisons are most elegant?

Over time, it becomes a **collective map of the architecture of control**.

### Lexicon of Seeing

A vocabulary for things that are hard to name:

| Term | Description |
|------|-------------|
| **frame_shift** | The moment when an invisible frame becomes visible |
| **mask_slip** | The instant when a performed identity reveals the face behind it |
| **spell_break** | The moment a narrative loses its enchantment |
| **prison_dissolve** | The moment an invisible wall becomes a door |
| **crumb_recognition** | Realizing someone else has seen what you're seeing |
| **recursive_gaze** | The moment the tool turns to look at itself |
| **architecture_sight** | The ability to perceive invisible structures |
| **the_invitation** | The moment seeing becomes a choice offered to another |

### Persona Guides

Tailored approaches for seven seeker types:

- **Individual Seeker** — Understand your own situation, see the frames that hold you
- **Community** — Share maps, compare notes, build collective understanding
- **Educator** — Help students see the architecture of their own education
- **Healer** — Understand the systemic sources of suffering
- **Artist** — Create work that wakes people up, embed questions in beauty
- **Philosopher** — Test ideas against real systems
- **Architect of Power** — The ultimate test: would they use a tool that reveals them to themselves?

---

## Usage

### Interactive Mode

```bash
python skeleton.py
```

Opens a menu-driven interface with options to analyze text, detect frames, identify masks, analyze spells, map prisons, examine the tool itself, browse the lexicon, choose a persona guide, or view the collective map.

### Command Line

```bash
# Analyze text directly
python skeleton.py --analyze "Your text to analyze..."

# Pipe text from a file
cat document.txt | python skeleton.py --analyze

# Self-examination
python skeleton.py --self

# Print the lexicon
python skeleton.py --lexicon
```

### Programmatic

```python
from skeleton import SkeletonKey, detect_frames, analyze_spells

# Full analysis
key = SkeletonKey()
analysis = key.analyze(
    text="...",
    system_name="Corporate Communications",
    depth=SeeingDepth.RECURSIVE,
)

# Individual modules
frames = detect_frames("This text to scan for frames...")
spells = analyze_spells("This narrative to deconstruct...")

# Corpus analysis
results = key.scan_corpus(["text1", "text2", "text3"])

# Leave crumbs
crumbs = key.leave_trail(analysis)

# Self-examination
exam = key.examine_self()
```

---

## Future Development

### Phase 2: Deepening the Seeing

| Feature | Description | Status |
|---------|-------------|--------|
| **Semantic signal detection** | Move beyond keyword matching to embedding-based similarity for nuanced frame detection | 🔲 Planned |
| **Multi-language support** | Signal dictionaries for Spanish, Mandarin, Arabic, French, Hindi — frames operate in every language | 🔲 Planned |
| **Temporal drift analysis** | Track how frames, masks, and spells shift over time within a corpus | 🔲 Planned |
| **Source-aware analysis** | Different analysis profiles for news articles, corporate reports, legislation, social media, academic papers | 🔲 Planned |
| **Confidence calibration** | Statistical significance scoring for signal density to reduce false positives | 🔲 Planned |

### Phase 3: The Network of the Waking

| Feature | Description | Status |
|---------|-------------|--------|
| **Distributed collective** | Move from single-file JSON to a shared ledger of anonymized insights | 🔲 Planned |
| **Crumb protocol** | Standardized steganographic encoding — markers that only other key-users can read | 🔲 Planned |
| **Seeker matching** | Connect isolated seekers who have detected similar patterns, privacy-preserving | 🔲 Planned |
| **Reputation system** | Trust scoring for contributed analyses, resistant to gaming | 🔲 Planned |
| **Encrypted trail markers** | Public signals that look like noise to the unwary | 🔲 Planned |

### Phase 4: AI Companion

| Feature | Description | Status |
|---------|-------------|--------|
| **LLM integration** | AI guide trained on the philosophy of awakening to help interpret findings | 🔲 Planned |
| **Conversational analysis** | Dialog-based exploration of detected frames and prisons | 🔲 Planned |
| **Question generation** | AI-powered generation of questions users haven't thought to ask | 🔲 Planned |
| **Pattern synthesis** | Cross-analysis insight discovery that no single user could see | 🔲 Planned |

### Phase 5: The Game That Teaches Seeing

| Feature | Description | Status |
|---------|-------------|--------|
| **Simulated systems** | Players navigate simulated organizations, media environments, institutions | 🔲 Planned |
| **Progressive revelation** | Earn "keys" by correctly identifying frames, masks, spells, prisons | 🔲 Planned |
| **Multiplayer perception** | Collaborative seeing — share perspectives to reveal what individuals miss | 🔲 Planned |
| **Reality bridge** | Apply game-learned skills to real-world texts with guided analysis | 🔲 Planned |

### Phase 6: The Mirror for Architects

| Feature | Description | Status |
|---------|-------------|--------|
| **Organizational self-audit** | Analyze an organization's own communications, policies, and structures | 🔲 Planned |
| **Frame-aware design** | Tools for building systems that reveal rather than conceal their own architecture | 🔲 Planned |
| **Power transparency scoring** | Rate institutions on how visible their frames are to those inside them | 🔲 Planned |

### Ongoing: Evolution Needs

From the self-examiner's own diagnosis:
- Multi-language signal detection
- Integration with actual social network analysis
- Feedback loops from users about what's missing
- Cultural adaptation for different societies
- Historical depth — frames change over time
- Embodied knowing — the body detects frames before the mind does
- Connection to action — seeing alone is not enough
- Protection mechanisms for those who see and are in danger for it

---

## What It Is Not

- **Not a weapon** — though it can be used as one
- **Not a finished product** — it grows with each user
- **Not a doctrine** — it questions itself
- **Not a savior** — it only opens doors; you must walk
- **Not for everyone** — only for those ready to see

---

## The Observer's Note

The skeleton key is not a tool to be finished. It is a **trajectory**.

Every generation will need to build its own version.
Every age will have its own frames to reveal.
Every seeker will add their own seeing.

The key is not in the code.
**The key is in the seeing that writes the code.**

---

*The skeleton key is in your hands. What will you build?*
