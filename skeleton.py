"""
skeleton.py — The Skeleton Key
================================

A skeleton key does not force locks.
It fits them because it understands their shape.

This is not a tool. It is an approach — a way of building that embeds
philosophical seeing into code. It does not exploit vulnerabilities.
It exposes assumptions. The key is not a weapon. It is a lens.

Modules:
    1. Frame Detector      — Maps the invisible architecture
    2. Mask Identifier     — Reveals the network of influence
    3. Spell Analyzer      — Deconstructs operating myths
    4. Prison Mapper       — Charts the cage with doors marked
    5. Crumb Generator     — Leaves traces for other seekers
    6. Recursive Examiner  — Turns the gaze inward

Architecture follows the Praxis pattern:
    - @dataclass with to_dict() for all models
    - Large philosophical dicts as knowledge structures
    - Pure scoring functions with keyword-matching
    - Graph-based relationship mapping
    - stdlib-only (no external dependencies)
    - Thread-safe where shared state exists
    - DSRP-aligned structural thinking

Author: A seeker.
"""

from __future__ import annotations

import ast
import hashlib
import json
import math
import os
import re
import threading
import uuid
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum, auto
from pathlib import Path
from typing import Any, Dict, FrozenSet, List, Optional, Set, Tuple


# ─────────────────────────────────────────────────────────────────────
#  I. ENUMERATIONS — The Vocabulary of Seeing
# ─────────────────────────────────────────────────────────────────────

class FrameType(Enum):
    """Categories of invisible architecture."""
    NORMATIVE = auto()       # "This is just how things are"
    LINGUISTIC = auto()      # The words that shape thought
    INSTITUTIONAL = auto()   # The rules that feel like physics
    TEMPORAL = auto()        # The timeline that feels inevitable
    EPISTEMIC = auto()       # What counts as "knowledge"
    ECONOMIC = auto()        # What counts as "value"
    TECHNOLOGICAL = auto()   # What technology makes thinkable
    MYTHOLOGICAL = auto()    # The stories that feel like truth


class MaskType(Enum):
    """Types of performed identity in systems."""
    AUTHORITY = auto()       # Power dressed as competence
    BENEVOLENCE = auto()     # Control dressed as care
    NEUTRALITY = auto()      # Ideology dressed as objectivity
    MERITOCRACY = auto()     # Privilege dressed as achievement
    INEVITABILITY = auto()   # Choice dressed as necessity
    TRADITION = auto()       # Inertia dressed as wisdom
    INNOVATION = auto()      # Disruption dressed as progress
    EXPERTISE = auto()       # Gatekeeping dressed as knowledge


class SpellType(Enum):
    """Categories of narrative enchantment."""
    ORIGIN_MYTH = auto()     # "This is where we came from"
    PROGRESS_NARRATIVE = auto()  # "Things are getting better"
    FEAR_NARRATIVE = auto()  # "Without us, chaos"
    SCARCITY_SPELL = auto()  # "There isn't enough"
    IDENTITY_SPELL = auto()  # "This is who you are"
    COMPLEXITY_SPELL = auto()  # "You couldn't understand"
    UNITY_SPELL = auto()     # "We're all in this together"
    BINARY_SPELL = auto()    # "You're either with us or against us"


class PrisonType(Enum):
    """Types of invisible constraint."""
    CHOICE_ARCHITECTURE = auto()  # The menu is the cage
    OVERTON_WINDOW = auto()    # The range of acceptable thought
    DEBT_STRUCTURE = auto()    # Financial chains
    CREDENTIAL_GATE = auto()   # Permission to think
    PLATFORM_LOCK = auto()     # Digital dependency
    TEMPORAL_TRAP = auto()     # Too busy to see
    IDENTITY_CAGE = auto()     # "People like us don't..."
    LEARNED_HELPLESSNESS = auto()  # "Nothing can change"


class CrumbType(Enum):
    """Types of traces left for seekers."""
    QUESTION = auto()        # A question that opens doors
    PATTERN = auto()         # A pattern once seen cannot be unseen
    PARADOX = auto()         # A contradiction that demands attention
    BRIDGE = auto()          # A connection between isolated insights
    MIRROR = auto()          # A reflection that shows the frame
    TRAIL = auto()           # A path to follow
    SIGNAL = auto()          # A marker for other seekers


class SeeingDepth(Enum):
    """Levels of structural awareness."""
    SURFACE = "surface"          # Sees content only
    PATTERN = "pattern"          # Sees recurring shapes
    STRUCTURE = "structure"      # Sees the architecture
    GENERATIVE = "generative"    # Sees what generates the architecture
    RECURSIVE = "recursive"      # Sees themselves seeing
    INTEGRAL = "integral"        # Sees the seeing itself


class ActorRole(Enum):
    """Roles in a system of influence."""
    ARCHITECT = auto()       # Designs the frame
    ENFORCER = auto()        # Maintains the frame
    BENEFICIARY = auto()     # Profits from the frame
    PERFORMER = auto()       # Enacts the frame
    SUBJECT = auto()         # Lives within the frame
    DISSENTER = auto()       # Questions the frame
    DEFECTOR = auto()        # Steps outside the frame
    WITNESS = auto()         # Sees the frame


# ─────────────────────────────────────────────────────────────────────
#  II. DATA MODELS — The Shapes of What We See
# ─────────────────────────────────────────────────────────────────────

@dataclass
class Frame:
    """An invisible structure that shapes perception."""
    frame_id: str = field(default_factory=lambda: uuid.uuid4().hex[:12])
    name: str = ""
    frame_type: FrameType = FrameType.NORMATIVE
    description: str = ""
    unspoken_rules: List[str] = field(default_factory=list)
    naturalized_assumptions: List[str] = field(default_factory=list)
    forbidden_questions: List[str] = field(default_factory=list)
    beneficiaries: List[str] = field(default_factory=list)
    edges_of_thinkable: List[str] = field(default_factory=list)
    strength: float = 0.0        # 0.0 = barely felt, 1.0 = invisible (fully naturalized)
    visibility: float = 0.0      # 0.0 = no one sees it, 1.0 = widely recognized
    detected_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "frame_id": self.frame_id,
            "name": self.name,
            "frame_type": self.frame_type.name,
            "description": self.description,
            "unspoken_rules": self.unspoken_rules,
            "naturalized_assumptions": self.naturalized_assumptions,
            "forbidden_questions": self.forbidden_questions,
            "beneficiaries": self.beneficiaries,
            "edges_of_thinkable": self.edges_of_thinkable,
            "strength": self.strength,
            "visibility": self.visibility,
            "detected_at": self.detected_at,
        }


@dataclass
class Mask:
    """A performed identity that conceals actual function."""
    mask_id: str = field(default_factory=lambda: uuid.uuid4().hex[:12])
    actor: str = ""
    mask_type: MaskType = MaskType.AUTHORITY
    formal_role: str = ""         # What the title says
    actual_function: str = ""     # What they actually do
    performance: str = ""         # The show they put on
    hidden_hand: str = ""         # What moves behind the mask
    dependencies: List[str] = field(default_factory=list)  # Who needs the mask to stay on
    vulnerabilities: List[str] = field(default_factory=list)  # Where the mask slips

    def to_dict(self) -> Dict[str, Any]:
        return {
            "mask_id": self.mask_id,
            "actor": self.actor,
            "mask_type": self.mask_type.name,
            "formal_role": self.formal_role,
            "actual_function": self.actual_function,
            "performance": self.performance,
            "hidden_hand": self.hidden_hand,
            "dependencies": self.dependencies,
            "vulnerabilities": self.vulnerabilities,
        }


@dataclass
class Spell:
    """A narrative that enchants perception."""
    spell_id: str = field(default_factory=lambda: uuid.uuid4().hex[:12])
    name: str = ""
    spell_type: SpellType = SpellType.ORIGIN_MYTH
    narrative: str = ""           # The story being told
    emotional_payload: str = ""   # What it makes people feel
    hidden_assumption: str = ""   # What it makes people assume
    erasure: str = ""             # What it makes people forget
    cui_bono: str = ""            # Who profits from belief
    counter_narrative: str = ""   # What breaks the spell
    potency: float = 0.0         # 0.0 = weak, 1.0 = total enchantment
    reach: float = 0.0           # 0.0 = local, 1.0 = civilizational

    def to_dict(self) -> Dict[str, Any]:
        return {
            "spell_id": self.spell_id,
            "name": self.name,
            "spell_type": self.spell_type.name,
            "narrative": self.narrative,
            "emotional_payload": self.emotional_payload,
            "hidden_assumption": self.hidden_assumption,
            "erasure": self.erasure,
            "cui_bono": self.cui_bono,
            "counter_narrative": self.counter_narrative,
            "potency": self.potency,
            "reach": self.reach,
        }


@dataclass
class Prison:
    """An invisible constraint on possibility."""
    prison_id: str = field(default_factory=lambda: uuid.uuid4().hex[:12])
    name: str = ""
    prison_type: PrisonType = PrisonType.CHOICE_ARCHITECTURE
    description: str = ""
    missing_choices: List[str] = field(default_factory=list)   # What's not on the menu
    forbidden_paths: List[str] = field(default_factory=list)   # What you can't choose
    unimaginable_futures: List[str] = field(default_factory=list)  # What you can't conceive
    invisible_walls: List[str] = field(default_factory=list)   # What stops you without being seen
    exit_conditions: List[str] = field(default_factory=list)   # What it would take to leave
    elegance: float = 0.0        # 0.0 = crude, 1.0 = the prisoner loves the cage

    def to_dict(self) -> Dict[str, Any]:
        return {
            "prison_id": self.prison_id,
            "name": self.name,
            "prison_type": self.prison_type.name,
            "description": self.description,
            "missing_choices": self.missing_choices,
            "forbidden_paths": self.forbidden_paths,
            "unimaginable_futures": self.unimaginable_futures,
            "invisible_walls": self.invisible_walls,
            "exit_conditions": self.exit_conditions,
            "elegance": self.elegance,
        }


@dataclass
class Crumb:
    """A trace left for other seekers."""
    crumb_id: str = field(default_factory=lambda: uuid.uuid4().hex[:12])
    crumb_type: CrumbType = CrumbType.QUESTION
    content: str = ""
    context: str = ""             # Where this crumb was found / placed
    visibility: str = "hidden"    # hidden | subtle | public
    target_audience: str = ""     # Who this crumb is for
    decay_time: Optional[str] = None   # When it self-destructs (ISO timestamp or None)
    chain_id: Optional[str] = None     # Links to other crumbs
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "crumb_id": self.crumb_id,
            "crumb_type": self.crumb_type.name,
            "content": self.content,
            "context": self.context,
            "visibility": self.visibility,
            "target_audience": self.target_audience,
            "decay_time": self.decay_time,
            "chain_id": self.chain_id,
            "created_at": self.created_at,
        }


@dataclass
class InfluenceEdge:
    """A relationship of power or influence between actors."""
    source: str = ""
    target: str = ""
    relation: str = ""           # controls | funds | appoints | influences | depends_on
    weight: float = 0.5
    visible: bool = True         # Is this relationship publicly known?
    mask_used: Optional[str] = None  # What mask conceals this relationship?

    def to_dict(self) -> Dict[str, Any]:
        return {
            "source": self.source,
            "target": self.target,
            "relation": self.relation,
            "weight": self.weight,
            "visible": self.visible,
            "mask_used": self.mask_used,
        }


@dataclass
class SelfExamination:
    """A recursive critique of the skeleton key itself."""
    exam_id: str = field(default_factory=lambda: uuid.uuid4().hex[:12])
    assumptions_found: List[str] = field(default_factory=list)
    blind_spots: List[str] = field(default_factory=list)
    misuse_vectors: List[str] = field(default_factory=list)
    creator_biases: List[str] = field(default_factory=list)
    evolution_needs: List[str] = field(default_factory=list)
    structural_metrics: Dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "exam_id": self.exam_id,
            "assumptions_found": self.assumptions_found,
            "blind_spots": self.blind_spots,
            "misuse_vectors": self.misuse_vectors,
            "creator_biases": self.creator_biases,
            "evolution_needs": self.evolution_needs,
            "structural_metrics": self.structural_metrics,
            "timestamp": self.timestamp,
        }


@dataclass
class SystemAnalysis:
    """Complete skeleton key analysis of a system."""
    analysis_id: str = field(default_factory=lambda: uuid.uuid4().hex[:12])
    system_name: str = ""
    frames: List[Frame] = field(default_factory=list)
    masks: List[Mask] = field(default_factory=list)
    spells: List[Spell] = field(default_factory=list)
    prisons: List[Prison] = field(default_factory=list)
    crumbs: List[Crumb] = field(default_factory=list)
    influence_edges: List[InfluenceEdge] = field(default_factory=list)
    self_examination: Optional[SelfExamination] = None
    seeing_depth: SeeingDepth = SeeingDepth.SURFACE
    analyzed_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    @property
    def awareness_score(self) -> float:
        """How much of the invisible architecture has been mapped. 0.0–1.0."""
        components = [
            min(len(self.frames) / 3, 1.0),
            min(len(self.masks) / 3, 1.0),
            min(len(self.spells) / 3, 1.0),
            min(len(self.prisons) / 3, 1.0),
            min(len(self.influence_edges) / 5, 1.0),
            1.0 if self.self_examination else 0.0,
        ]
        return sum(components) / len(components)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "analysis_id": self.analysis_id,
            "system_name": self.system_name,
            "frames": [f.to_dict() for f in self.frames],
            "masks": [m.to_dict() for m in self.masks],
            "spells": [s.to_dict() for s in self.spells],
            "prisons": [p.to_dict() for p in self.prisons],
            "crumbs": [c.to_dict() for c in self.crumbs],
            "influence_edges": [e.to_dict() for e in self.influence_edges],
            "self_examination": self.self_examination.to_dict() if self.self_examination else None,
            "seeing_depth": self.seeing_depth.value,
            "awareness_score": self.awareness_score,
            "analyzed_at": self.analyzed_at,
        }


# ─────────────────────────────────────────────────────────────────────
#  III. KNOWLEDGE STRUCTURES — The Maps of Seeing
# ─────────────────────────────────────────────────────────────────────

# Each knowledge structure maps signal words to deeper insight.
# This is how the skeleton key "fits" any lock — by recognizing
# patterns in language that reveal underlying architecture.

FRAME_SIGNALS: Dict[FrameType, Dict[str, Any]] = {
    FrameType.NORMATIVE: {
        "signals": [
            "normal", "natural", "obvious", "common sense", "everyone knows",
            "that's just how it is", "tradition", "always been", "standard",
            "the way things work", "realistic", "pragmatic", "inevitable",
            "human nature", "the real world",
        ],
        "question": "What would change if this were seen as a choice rather than a fact?",
        "reveals": "Normative frames disguise social constructions as natural law.",
        "antidote": "Ask: who decided this was 'normal,' and when?",
    },
    FrameType.LINGUISTIC: {
        "signals": [
            "stakeholder", "human resources", "collateral damage", "externality",
            "disruption", "optimization", "leverage", "synergy", "alignment",
            "market forces", "talent", "assets", "capital", "deliverables",
            "value proposition", "growth", "scale",
        ],
        "question": "What does this language conceal about who is affected and how?",
        "reveals": "Linguistic frames make violence abstract and people into resources.",
        "antidote": "Replace each term with plain language and notice what changes.",
    },
    FrameType.INSTITUTIONAL: {
        "signals": [
            "policy", "procedure", "compliance", "regulation", "governance",
            "protocol", "due process", "standard operating", "best practice",
            "industry standard", "accreditation", "certification", "authorized",
            "official channels", "chain of command",
        ],
        "question": "Who wrote these rules, and what do they protect?",
        "reveals": "Institutional frames make power arrangements feel like physics.",
        "antidote": "Trace each rule to its origin. Someone wrote it. Someone benefits.",
    },
    FrameType.TEMPORAL: {
        "signals": [
            "progress", "inevitable", "the future", "moving forward", "behind the times",
            "modernization", "next generation", "legacy", "outdated", "evolving",
            "trajectory", "momentum", "disruption cycle", "paradigm shift",
            "the arc of history", "tipping point",
        ],
        "question": "Whose timeline is this, and what does it erase?",
        "reveals": "Temporal frames make one group's trajectory feel like destiny.",
        "antidote": "Ask: inevitable for whom? Progress toward what? Decided by whom?",
    },
    FrameType.EPISTEMIC: {
        "signals": [
            "evidence-based", "data-driven", "peer-reviewed", "scientific consensus",
            "expert opinion", "credible sources", "methodology", "rigorous",
            "statistically significant", "empirical", "objective", "measurable",
            "anecdotal", "unsubstantiated", "misinformation",
        ],
        "question": "What ways of knowing are being excluded, and why?",
        "reveals": "Epistemic frames determine what counts as knowledge — and who counts as a knower.",
        "antidote": "Ask: what would a different discipline, culture, or tradition see here?",
    },
    FrameType.ECONOMIC: {
        "signals": [
            "market", "efficiency", "roi", "cost-benefit", "productivity",
            "scarcity", "supply and demand", "rational actor", "incentive",
            "GDP", "profit margin", "bottom line", "valuation", "monetize",
            "free market", "competition", "shareholder value",
        ],
        "question": "What is being valued, and what is being discarded?",
        "reveals": "Economic frames reduce all value to a single metric and hide the rest.",
        "antidote": "Name three things this framework cannot measure but that matter enormously.",
    },
    FrameType.TECHNOLOGICAL: {
        "signals": [
            "platform", "algorithm", "AI", "automation", "machine learning",
            "digital transformation", "smart", "cloud", "API", "ecosystem",
            "scalable", "disruptive", "innovation", "tech-enabled",
            "frictionless", "seamless", "personalized",
        ],
        "question": "What human decisions are hidden inside this technology?",
        "reveals": "Technological frames make human choices appear as neutral computation.",
        "antidote": "Find the humans. Someone designed this. Someone chose the training data. Someone profits.",
    },
    FrameType.MYTHOLOGICAL: {
        "signals": [
            "founding fathers", "self-made", "American dream", "invisible hand",
            "meritocracy", "free world", "civilization", "manifest destiny",
            "the people", "our values", "who we are", "heritage", "legacy",
            "promised land", "chosen", "destiny", "greatness",
        ],
        "question": "What does this myth authorize, and what does it forbid?",
        "reveals": "Mythological frames sacralize power arrangements so they cannot be questioned.",
        "antidote": "Tell the same story from the perspective of those the myth excludes.",
    },
}


MASK_SIGNALS: Dict[MaskType, Dict[str, Any]] = {
    MaskType.AUTHORITY: {
        "signals": [
            "leadership", "executive", "decision-maker", "vision", "strategy",
            "mandate", "direction", "C-suite", "board", "governance",
        ],
        "behind_the_mask": "Power is often held not by the visible leaders but by those who set the agenda they enact.",
        "slip_indicators": ["contradicts own policy", "defers upward", "cannot explain rationale", "reads from script"],
    },
    MaskType.BENEVOLENCE: {
        "signals": [
            "for your own good", "we care", "protecting", "safety", "support",
            "help", "empower", "serve", "community", "wellbeing",
        ],
        "behind_the_mask": "Care rhetoric often masks control. True care shares power; false care hoards it.",
        "slip_indicators": ["help requires compliance", "support has conditions", "empowerment means obedience"],
    },
    MaskType.NEUTRALITY: {
        "signals": [
            "objective", "balanced", "both sides", "unbiased", "fair",
            "neutral", "apolitical", "nonpartisan", "just the facts", "centrist",
        ],
        "behind_the_mask": "Claimed neutrality always serves the status quo. The center is not neutral — it is the current arrangement of power.",
        "slip_indicators": ["frames challengers as extreme", "treats current system as baseline", "equates critique with bias"],
    },
    MaskType.MERITOCRACY: {
        "signals": [
            "earned", "deserved", "talent", "hard work", "achievement",
            "performance", "best and brightest", "top tier", "elite", "competitive",
        ],
        "behind_the_mask": "Meritocracy narratives attribute systemic outcomes to individual qualities, hiding the architecture of advantage.",
        "slip_indicators": ["success correlates with starting position", "failure blamed on individual", "structural advantages unnamed"],
    },
    MaskType.INEVITABILITY: {
        "signals": [
            "no alternative", "the only way", "necessary", "unavoidable",
            "market forces", "economic reality", "there is no choice", "we must",
            "the situation demands", "forced by circumstances",
        ],
        "behind_the_mask": "Inevitability is the most powerful mask. When choices vanish, power becomes invisible.",
        "slip_indicators": ["alternatives existed historically", "other systems do it differently", "someone benefits from 'no choice'"],
    },
    MaskType.TRADITION: {
        "signals": [
            "always been done", "heritage", "custom", "roots", "values",
            "time-tested", "wisdom of the ages", "sacred", "founding principles",
        ],
        "behind_the_mask": "Tradition selectively remembers. What is called 'traditional' was once someone's radical innovation.",
        "slip_indicators": ["the 'tradition' is recent", "it was contested when introduced", "other traditions are excluded"],
    },
    MaskType.INNOVATION: {
        "signals": [
            "disrupt", "transform", "revolutionize", "cutting-edge", "future",
            "breakthrough", "paradigm shift", "next generation", "reimagine",
        ],
        "behind_the_mask": "Innovation rhetoric often masks extraction. 'Disruption' frequently means destroying what communities built and selling it back.",
        "slip_indicators": ["innovation benefits investors most", "disrupted communities not consulted", "problems recreated at scale"],
    },
    MaskType.EXPERTISE: {
        "signals": [
            "expert", "specialist", "authority", "credentials", "certification",
            "qualified", "trained", "professional", "accredited", "peer-reviewed",
        ],
        "behind_the_mask": "Expertise is real, but the gatekeeping of expertise is a power structure. Who decides what counts as knowing?",
        "slip_indicators": ["experts disagree but one view dominates", "credentials gate access", "lived experience dismissed"],
    },
}


SPELL_SIGNALS: Dict[SpellType, Dict[str, Any]] = {
    SpellType.ORIGIN_MYTH: {
        "signals": [
            "founded", "began", "origin", "genesis", "founding", "started with",
            "our story", "once upon", "in the beginning", "from humble beginnings",
        ],
        "emotional_hook": "Belonging, legitimacy, pride",
        "hidden_function": "Creates loyalty by making the listener part of a sacred story",
        "breaking_question": "What does this origin story leave out? Who was already here?",
    },
    SpellType.PROGRESS_NARRATIVE: {
        "signals": [
            "better", "improving", "growing", "advancing", "developing",
            "more than ever", "unprecedented", "next level", "forward",
        ],
        "emotional_hook": "Hope, optimism, participation",
        "hidden_function": "Makes current trajectory feel inevitable and good; resistance feels regressive",
        "breaking_question": "Better for whom? By whose metric? At what cost to what?",
    },
    SpellType.FEAR_NARRATIVE: {
        "signals": [
            "threat", "danger", "crisis", "enemy", "collapse", "catastrophe",
            "if we don't act now", "at risk", "under attack", "existential",
        ],
        "emotional_hook": "Fear, urgency, tribal bonding",
        "hidden_function": "Justifies extreme measures and suppresses dissent ('now is not the time')",
        "breaking_question": "Who benefits from this fear? What becomes possible when people are afraid?",
    },
    SpellType.SCARCITY_SPELL: {
        "signals": [
            "not enough", "limited", "scarce", "running out", "competition",
            "zero-sum", "fight for", "earn your place", "only the best",
        ],
        "emotional_hook": "Anxiety, competition, hoarding instinct",
        "hidden_function": "Prevents solidarity by making people see each other as competitors for artificially limited resources",
        "breaking_question": "Is this truly scarce, or is access being controlled? By whom?",
    },
    SpellType.IDENTITY_SPELL: {
        "signals": [
            "we are", "our people", "who we are", "our values", "our kind",
            "real Americans", "true believers", "the faithful", "patriots",
        ],
        "emotional_hook": "Belonging, exclusion, tribal identity",
        "hidden_function": "Creates in-group that cannot question without losing identity",
        "breaking_question": "Who is 'we,' and who is excluded? What happens to those who disagree from within?",
    },
    SpellType.COMPLEXITY_SPELL: {
        "signals": [
            "it's complicated", "you wouldn't understand", "technical", "nuanced",
            "leave it to the experts", "too complex", "sophisticated", "intricate",
        ],
        "emotional_hook": "Intellectual insecurity, deference, helplessness",
        "hidden_function": "Prevents democratic engagement with decisions that affect everyone",
        "breaking_question": "Is it truly complex, or is complexity being weaponized to exclude?",
    },
    SpellType.UNITY_SPELL: {
        "signals": [
            "together", "united", "one team", "shared purpose", "collective",
            "all of us", "in this together", "common goal", "solidarity",
        ],
        "emotional_hook": "Warmth, safety, community feeling",
        "hidden_function": "Suppresses legitimate disagreement by framing it as betrayal of the group",
        "breaking_question": "Whose version of 'together'? Who set the terms? Who is silenced by 'unity'?",
    },
    SpellType.BINARY_SPELL: {
        "signals": [
            "either", "or", "with us", "against us", "right side of history",
            "good vs evil", "black and white", "choose a side", "no middle ground",
        ],
        "emotional_hook": "Moral clarity, righteousness, urgency",
        "hidden_function": "Eliminates the third option — the one that would reveal the frame itself",
        "breaking_question": "What would a third position look like? What does the binary hide?",
    },
}


PRISON_SIGNALS: Dict[PrisonType, Dict[str, Any]] = {
    PrisonType.CHOICE_ARCHITECTURE: {
        "signals": [
            "option", "plan", "tier", "package", "menu", "choose from",
            "select", "pick", "preference", "customize",
        ],
        "mechanism": "Freedom is performed through selection from a pre-curated menu. The menu IS the cage.",
        "door": "Design your own menu. Ask: what option is missing, and why?",
    },
    PrisonType.OVERTON_WINDOW: {
        "signals": [
            "mainstream", "fringe", "extreme", "moderate", "reasonable",
            "radical", "unthinkable", "acceptable", "politically feasible",
        ],
        "mechanism": "The range of 'acceptable' opinion is itself a structure of control. Moving the window is a power act.",
        "door": "Name the idea that cannot be spoken in this space. That is where the wall is.",
    },
    PrisonType.DEBT_STRUCTURE: {
        "signals": [
            "loan", "mortgage", "tuition", "credit", "payment plan",
            "interest", "debt", "obligation", "owe", "afford",
        ],
        "mechanism": "Debt restructures time itself. The indebted cannot afford to question because they cannot afford to lose.",
        "door": "Calculate the total lifetime interest paid. Follow where it goes. That is the architecture.",
    },
    PrisonType.CREDENTIAL_GATE: {
        "signals": [
            "degree", "certification", "accreditation", "qualified",
            "licensed", "authorized", "prerequisite", "requirements",
        ],
        "mechanism": "Credentials gatekeep knowledge that often came from the uncredentialed. The gate charges rent on the commons.",
        "door": "Find someone who knows this without the credential. They exist. Ask how they learned.",
    },
    PrisonType.PLATFORM_LOCK: {
        "signals": [
            "ecosystem", "integration", "compatible", "API", "platform",
            "migration cost", "switching cost", "vendor", "proprietary",
        ],
        "mechanism": "Digital dependency creates invisible walls. Your data, your network, your history — held hostage by design.",
        "door": "Export everything. If you can't, that IS the wall. Build on what you can leave.",
    },
    PrisonType.TEMPORAL_TRAP: {
        "signals": [
            "busy", "no time", "deadline", "urgent", "ASAP",
            "bandwidth", "overwhelmed", "sprint", "crunch", "hustle",
        ],
        "mechanism": "The trap that prevents seeing all other traps. If you have no time to think, you have no time to be free.",
        "door": "The most radical act may be stopping. Not forever. Just long enough to see.",
    },
    PrisonType.IDENTITY_CAGE: {
        "signals": [
            "people like us", "that's not who I am", "I could never",
            "that's not for people like me", "stay in your lane", "know your place",
        ],
        "mechanism": "Identity becomes a cage when it limits possibility. 'Who you are' becomes 'what you're allowed to want.'",
        "door": "Try the thing that 'people like you' don't do. The cage is made of stories, not steel.",
    },
    PrisonType.LEARNED_HELPLESSNESS: {
        "signals": [
            "nothing changes", "what's the point", "they won't let us",
            "it's always been this way", "you can't fight", "too big to change",
        ],
        "mechanism": "The most elegant prison. The prisoner maintains their own walls by believing escape is impossible.",
        "door": "Find one person who escaped. One example breaks the spell. Then find another.",
    },
}


# ─────────────────────────────────────────────────────────────────────
#  IV. MODULE 1 — FRAME DETECTOR
# ─────────────────────────────────────────────────────────────────────

def detect_frames(text: str, context: str = "") -> List[Frame]:
    """
    Scans text for invisible architecture.

    Asks:
        - What are the unspoken rules?
        - What is considered 'natural' here?
        - What questions are forbidden?
        - Who benefits from this arrangement?
        - Where are the edges of thinkable thought?

    Returns a list of detected Frames, ranked by signal density.
    """
    text_lower = text.lower() + " " + context.lower()
    results: List[Tuple[float, Frame]] = []

    for frame_type, signals_data in FRAME_SIGNALS.items():
        matched = [s for s in signals_data["signals"] if s in text_lower]
        if not matched:
            continue

        density = len(matched) / len(signals_data["signals"])
        strength = min(density * 2.0, 1.0)  # Scale up: even partial matches matter

        frame = Frame(
            name=f"{frame_type.name.title()} Frame",
            frame_type=frame_type,
            description=signals_data["reveals"],
            unspoken_rules=[f"Signal detected: '{m}'" for m in matched],
            naturalized_assumptions=[signals_data["reveals"]],
            forbidden_questions=[signals_data["question"]],
            beneficiaries=[],  # Requires deeper analysis
            edges_of_thinkable=[signals_data["antidote"]],
            strength=strength,
            visibility=1.0 - strength,  # The stronger the frame, the less visible
        )
        results.append((density, frame))

    results.sort(key=lambda x: x[0], reverse=True)
    return [frame for _, frame in results]


def map_frame_architecture(texts: List[str]) -> Dict[str, Any]:
    """
    Analyze multiple texts to build a composite map of frame architecture.

    Returns a map showing which frames co-occur, which reinforce each other,
    and where the architecture is thickest.
    """
    all_frames: List[Frame] = []
    frame_counts: Dict[str, int] = defaultdict(int)
    co_occurrences: Dict[Tuple[str, str], int] = defaultdict(int)

    for text in texts:
        frames = detect_frames(text)
        all_frames.extend(frames)
        types_found = [f.frame_type.name for f in frames]
        for ft in types_found:
            frame_counts[ft] += 1
        # Track co-occurrences
        for i, a in enumerate(types_found):
            for b in types_found[i + 1:]:
                pair = tuple(sorted([a, b]))
                co_occurrences[pair] += 1

    # Identify the dominant architecture
    dominant = sorted(frame_counts.items(), key=lambda x: x[1], reverse=True)

    return {
        "total_frames_detected": len(all_frames),
        "frame_frequency": dict(dominant),
        "co_occurrence_matrix": {f"{a}-{b}": c for (a, b), c in co_occurrences.items()},
        "dominant_frame": dominant[0][0] if dominant else None,
        "architectural_density": len(all_frames) / max(len(texts), 1),
        "insight": _generate_frame_insight(dominant, co_occurrences),
    }


def _generate_frame_insight(
    dominant: List[Tuple[str, int]],
    co_occurrences: Dict[Tuple[str, str], int],
) -> str:
    """Generate a human-readable insight from frame analysis."""
    if not dominant:
        return "No frames detected. This is itself significant — where there appear to be no frames, the framing may be total."

    top = dominant[0][0] if dominant else "NONE"
    count = dominant[0][1] if dominant else 0

    # Find strongest co-occurrence
    strongest_pair = max(co_occurrences.items(), key=lambda x: x[1]) if co_occurrences else None

    insight = f"The dominant frame is {top} (appeared {count} times). "
    if strongest_pair:
        a, b = strongest_pair[0]
        insight += f"The strongest reinforcement pattern is {a} ↔ {b} (co-occurred {strongest_pair[1]} times). "
        insight += "These frames likely reinforce each other — look for how one naturalizes the other."
    return insight


# ─────────────────────────────────────────────────────────────────────
#  V. MODULE 2 — MASK IDENTIFIER
# ─────────────────────────────────────────────────────────────────────

class InfluenceGraph:
    """
    A network diagram of influence with masks removed.

    Maps actors, their formal roles, their actual functions,
    and the relationships between them — both visible and hidden.

    Thread-safe for concurrent analysis.
    """

    def __init__(self) -> None:
        self._lock = threading.RLock()
        self._actors: Dict[str, Mask] = {}
        self._edges: List[InfluenceEdge] = []

    def add_actor(self, mask: Mask) -> None:
        with self._lock:
            self._actors[mask.actor] = mask

    def add_edge(self, edge: InfluenceEdge) -> None:
        with self._lock:
            self._edges.append(edge)

    def identify_masks(self, text: str) -> List[Mask]:
        """
        Scan text for performed identities.

        Tracks actors and roles:
            - Who holds formal power?
            - Who holds actual power?
            - What titles hide what hands?
            - What performances are being staged?
            - Who is the puppet? Who is the puppeteer?
        """
        text_lower = text.lower()
        results: List[Tuple[float, Mask]] = []

        for mask_type, signals_data in MASK_SIGNALS.items():
            matched = [s for s in signals_data["signals"] if s in text_lower]
            if not matched:
                continue

            density = len(matched) / len(signals_data["signals"])

            mask = Mask(
                actor=f"[Actor performing {mask_type.name}]",
                mask_type=mask_type,
                formal_role=", ".join(matched),
                actual_function=signals_data["behind_the_mask"],
                performance=f"Signals: {', '.join(matched)}",
                hidden_hand=signals_data["behind_the_mask"],
                vulnerabilities=signals_data["slip_indicators"],
            )
            results.append((density, mask))
            self.add_actor(mask)

        results.sort(key=lambda x: x[0], reverse=True)
        return [mask for _, mask in results]

    def find_puppeteers(self) -> List[Dict[str, Any]]:
        """Find actors with high outgoing influence and low visibility."""
        with self._lock:
            outgoing: Dict[str, float] = defaultdict(float)
            incoming: Dict[str, float] = defaultdict(float)
            hidden_count: Dict[str, int] = defaultdict(int)

            for edge in self._edges:
                outgoing[edge.source] += edge.weight
                incoming[edge.target] += edge.weight
                if not edge.visible:
                    hidden_count[edge.source] += 1

            puppeteers = []
            for actor in self._actors:
                out = outgoing.get(actor, 0.0)
                inc = incoming.get(actor, 0.0)
                hidden = hidden_count.get(actor, 0)
                if out > inc and hidden > 0:
                    puppeteers.append({
                        "actor": actor,
                        "outgoing_influence": round(out, 3),
                        "incoming_influence": round(inc, 3),
                        "hidden_connections": hidden,
                        "puppet_score": round(out / max(inc, 0.01) * (1 + hidden), 3),
                    })

            puppeteers.sort(key=lambda x: x["puppet_score"], reverse=True)
            return puppeteers

    def unmask_network(self) -> Dict[str, Any]:
        """Generate the full network diagram with masks removed."""
        with self._lock:
            return {
                "actors": {name: mask.to_dict() for name, mask in self._actors.items()},
                "relationships": [e.to_dict() for e in self._edges],
                "hidden_relationships": [e.to_dict() for e in self._edges if not e.visible],
                "puppeteers": self.find_puppeteers(),
                "total_actors": len(self._actors),
                "total_edges": len(self._edges),
                "hidden_edge_ratio": (
                    sum(1 for e in self._edges if not e.visible) / max(len(self._edges), 1)
                ),
            }


def identify_masks(text: str) -> List[Mask]:
    """Convenience function for stateless mask detection."""
    graph = InfluenceGraph()
    return graph.identify_masks(text)


# ─────────────────────────────────────────────────────────────────────
#  VI. MODULE 3 — SPELL ANALYZER
# ─────────────────────────────────────────────────────────────────────

def analyze_spells(text: str) -> List[Spell]:
    """
    Examine narratives for enchantment.

    Asks:
        - What stories are being told?
        - What do they make people feel?
        - What do they make people assume?
        - What do they make people forget?
        - Who profits from belief in these stories?

    Returns a list of detected Spells, ranked by potency.
    """
    text_lower = text.lower()
    results: List[Tuple[float, Spell]] = []

    for spell_type, signals_data in SPELL_SIGNALS.items():
        matched = [s for s in signals_data["signals"] if s in text_lower]
        if not matched:
            continue

        density = len(matched) / len(signals_data["signals"])
        potency = min(density * 2.5, 1.0)

        spell = Spell(
            name=f"{spell_type.name.replace('_', ' ').title()}",
            spell_type=spell_type,
            narrative=f"Detected narrative signals: {', '.join(matched)}",
            emotional_payload=signals_data["emotional_hook"],
            hidden_assumption=signals_data["hidden_function"],
            erasure="[Requires deeper analysis — what is NOT being said?]",
            cui_bono="[Follow the benefit — who gains from this belief?]",
            counter_narrative=signals_data["breaking_question"],
            potency=potency,
            reach=density,
        )
        results.append((potency, spell))

    results.sort(key=lambda x: x[0], reverse=True)
    return [spell for _, spell in results]


def compute_spell_potency(spells: List[Spell]) -> Dict[str, Any]:
    """
    Calculate the aggregate enchantment level of a narrative environment.

    A high aggregate score means the narrative environment is heavily
    enchanted — many reinforcing stories creating a thick reality-distortion field.
    """
    if not spells:
        return {
            "aggregate_potency": 0.0,
            "dominant_spell": None,
            "spell_count": 0,
            "enchantment_level": "clear",
            "insight": "No active spells detected. Either the space is clear, or the enchantment is too deep to see.",
        }

    aggregate = sum(s.potency for s in spells) / len(spells)
    dominant = max(spells, key=lambda s: s.potency)

    # Shannon entropy of spell type distribution
    type_counts = defaultdict(int)
    for s in spells:
        type_counts[s.spell_type.name] += 1
    total = sum(type_counts.values())
    entropy = -sum(
        (c / total) * math.log2(c / total)
        for c in type_counts.values()
        if c > 0
    )

    if aggregate >= 0.8:
        level = "total_enchantment"
    elif aggregate >= 0.6:
        level = "heavy_enchantment"
    elif aggregate >= 0.4:
        level = "moderate_enchantment"
    elif aggregate >= 0.2:
        level = "light_enchantment"
    else:
        level = "minimal_enchantment"

    return {
        "aggregate_potency": round(aggregate, 3),
        "dominant_spell": dominant.to_dict(),
        "spell_count": len(spells),
        "spell_diversity": round(entropy, 3),
        "enchantment_level": level,
        "spell_breakdown": {s.spell_type.name: s.potency for s in spells},
        "insight": (
            f"Dominant narrative: {dominant.name} (potency {dominant.potency:.2f}). "
            f"Narrative diversity: {entropy:.2f} bits. "
            f"{'High diversity means multiple reinforcing stories. ' if entropy > 1.5 else ''}"
            f"Counter-question: {dominant.counter_narrative}"
        ),
    }


# ─────────────────────────────────────────────────────────────────────
#  VII. MODULE 4 — PRISON MAPPER
# ─────────────────────────────────────────────────────────────────────

def map_prisons(text: str) -> List[Prison]:
    """
    Reveal invisible constraints.

    Asks:
        - What choices are missing from the menu?
        - What paths are forbidden?
        - What futures are unimaginable?
        - What walls are invisible?
        - What would it take to step outside?

    Returns a list of detected Prisons with doors marked.
    """
    text_lower = text.lower()
    results: List[Tuple[float, Prison]] = []

    for prison_type, signals_data in PRISON_SIGNALS.items():
        matched = [s for s in signals_data["signals"] if s in text_lower]
        if not matched:
            continue

        density = len(matched) / len(signals_data["signals"])
        elegance = min(density * 2.0, 1.0)

        prison = Prison(
            name=f"{prison_type.name.replace('_', ' ').title()}",
            prison_type=prison_type,
            description=signals_data["mechanism"],
            missing_choices=["[What option would change everything if it appeared?]"],
            forbidden_paths=["[What path is not even conceived as possible?]"],
            unimaginable_futures=["[What future cannot be imagined from inside this prison?]"],
            invisible_walls=[f"Signal: '{m}'" for m in matched],
            exit_conditions=[signals_data["door"]],
            elegance=elegance,
        )
        results.append((elegance, prison))

    results.sort(key=lambda x: x[0], reverse=True)
    return [prison for _, prison in results]


def find_doors(prisons: List[Prison]) -> List[Dict[str, Any]]:
    """
    For each prison detected, extract the exit conditions and
    rate the difficulty of each escape.

    A door exists for every prison. The question is whether you can see it.
    """
    doors = []
    for prison in prisons:
        difficulty = prison.elegance  # The more elegant the prison, the harder to leave
        doors.append({
            "prison": prison.name,
            "prison_type": prison.prison_type.name,
            "elegance": prison.elegance,
            "exits": prison.exit_conditions,
            "escape_difficulty": round(difficulty, 3),
            "first_step": (
                "See the wall. That is always the first step. "
                "You cannot walk through a wall you don't know is there."
            ),
        })
    return doors


def compute_cage_score(prisons: List[Prison]) -> Dict[str, Any]:
    """
    Calculate how confined a system is.

    The cage score measures the aggregate density, elegance, and
    interlocking nature of detected prisons.
    """
    if not prisons:
        return {
            "cage_score": 0.0,
            "interpretation": "open_field",
            "prison_count": 0,
            "insight": "No prisons detected. Freedom — or blindness. Which?",
        }

    avg_elegance = sum(p.elegance for p in prisons) / len(prisons)

    # Prisons that co-occur are more constraining than isolated ones
    interlocking_bonus = min(len(prisons) * 0.1, 0.5)
    cage_score = min(avg_elegance + interlocking_bonus, 1.0)

    if cage_score >= 0.8:
        interp = "total_confinement"
    elif cage_score >= 0.6:
        interp = "heavy_constraint"
    elif cage_score >= 0.4:
        interp = "moderate_constraint"
    elif cage_score >= 0.2:
        interp = "light_constraint"
    else:
        interp = "mostly_free"

    return {
        "cage_score": round(cage_score, 3),
        "interpretation": interp,
        "prison_count": len(prisons),
        "avg_elegance": round(avg_elegance, 3),
        "interlocking_bonus": round(interlocking_bonus, 3),
        "most_elegant_prison": max(prisons, key=lambda p: p.elegance).name,
        "doors": find_doors(prisons),
        "insight": (
            f"Cage score: {cage_score:.2f}. "
            f"{len(prisons)} interlocking constraints detected. "
            f"The most elegant prison is '{max(prisons, key=lambda p: p.elegance).name}' — "
            f"elegant prisons are loved by their inmates."
        ),
    }


# ─────────────────────────────────────────────────────────────────────
#  VIII. MODULE 5 — CRUMB GENERATOR
# ─────────────────────────────────────────────────────────────────────

class CrumbTrail:
    """
    A distributed network of insights, hidden in plain sight.

    Creates traces for others:
        - Markers that show where the frame was seen
        - Questions that seed awakening
        - Paths to alternative perspectives
        - Connections between isolated seekers
        - A trail that can be followed without being detected

    Thread-safe. Crumbs are stored in memory and can be persisted to JSON.
    """

    def __init__(self, trail_id: Optional[str] = None) -> None:
        self._lock = threading.RLock()
        self.trail_id = trail_id or uuid.uuid4().hex[:16]
        self._crumbs: List[Crumb] = []
        self._chains: Dict[str, List[str]] = defaultdict(list)  # chain_id -> [crumb_ids]

    def drop_crumb(
        self,
        content: str,
        crumb_type: CrumbType = CrumbType.QUESTION,
        context: str = "",
        visibility: str = "hidden",
        target_audience: str = "seekers",
        chain_id: Optional[str] = None,
    ) -> Crumb:
        """Leave a trace for those who will find it."""
        crumb = Crumb(
            crumb_type=crumb_type,
            content=content,
            context=context,
            visibility=visibility,
            target_audience=target_audience,
            chain_id=chain_id or self.trail_id,
        )
        with self._lock:
            self._crumbs.append(crumb)
            self._chains[crumb.chain_id].append(crumb.crumb_id)
        return crumb

    def generate_from_analysis(self, analysis: SystemAnalysis) -> List[Crumb]:
        """
        Automatically generate crumbs from a system analysis.

        For each insight found, create an appropriate trace:
        - Frames become questions
        - Masks become patterns
        - Spells become paradoxes
        - Prisons become trails to doors
        """
        generated: List[Crumb] = []
        chain_id = uuid.uuid4().hex[:12]

        # Frames → Questions that reveal
        for frame in analysis.frames:
            for question in frame.forbidden_questions:
                crumb = self.drop_crumb(
                    content=question,
                    crumb_type=CrumbType.QUESTION,
                    context=f"Generated from {frame.name} detection",
                    chain_id=chain_id,
                )
                generated.append(crumb)

        # Masks → Patterns to recognize
        for mask in analysis.masks:
            crumb = self.drop_crumb(
                content=f"When you hear '{mask.formal_role}', look for: {mask.actual_function}",
                crumb_type=CrumbType.PATTERN,
                context=f"Generated from {mask.mask_type.name} mask detection",
                chain_id=chain_id,
            )
            generated.append(crumb)

        # Spells → Counter-narratives
        for spell in analysis.spells:
            crumb = self.drop_crumb(
                content=spell.counter_narrative,
                crumb_type=CrumbType.PARADOX,
                context=f"Counter to {spell.name}",
                chain_id=chain_id,
            )
            generated.append(crumb)

        # Prisons → Trails to doors
        for prison in analysis.prisons:
            for exit_condition in prison.exit_conditions:
                crumb = self.drop_crumb(
                    content=exit_condition,
                    crumb_type=CrumbType.TRAIL,
                    context=f"Door in {prison.name}",
                    chain_id=chain_id,
                )
                generated.append(crumb)

        # Meta-crumb: a bridge connecting all insights
        if generated:
            bridge = self.drop_crumb(
                content=(
                    f"This system has {len(analysis.frames)} visible frames, "
                    f"{len(analysis.masks)} masks in play, "
                    f"{len(analysis.spells)} active spells, and "
                    f"{len(analysis.prisons)} prisons operating. "
                    f"Awareness score: {analysis.awareness_score:.2f}. "
                    f"The first step is always the same: see."
                ),
                crumb_type=CrumbType.BRIDGE,
                context="Meta-analysis bridge",
                chain_id=chain_id,
            )
            generated.append(bridge)

        return generated

    def follow_chain(self, chain_id: str) -> List[Crumb]:
        """Follow a chain of crumbs to reconstruct a trail of insight."""
        with self._lock:
            crumb_ids = self._chains.get(chain_id, [])
            return [c for c in self._crumbs if c.crumb_id in crumb_ids]

    def encode_crumb(self, crumb: Crumb, key: str = "") -> str:
        """
        Encode a crumb so it looks like noise to the unwary.

        Uses a simple hash-based encoding. In a production system,
        this would use proper cryptographic steganography.
        """
        content = crumb.content
        salt = key or self.trail_id
        marker = hashlib.sha256(f"{salt}:{crumb.crumb_id}".encode()).hexdigest()[:8]
        # The encoded crumb: a marker followed by the content hash
        content_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
        return f"sk:{marker}:{content_hash}"

    def decode_trail(self, encoded_markers: List[str]) -> List[Crumb]:
        """Given encoded markers, find matching crumbs."""
        with self._lock:
            decoded = []
            for crumb in self._crumbs:
                encoded = self.encode_crumb(crumb)
                if encoded in encoded_markers:
                    decoded.append(crumb)
            return decoded

    def get_all_crumbs(self) -> List[Dict[str, Any]]:
        """Return all crumbs as serializable dicts."""
        with self._lock:
            return [c.to_dict() for c in self._crumbs]

    def persist(self, path: Path) -> None:
        """Save crumb trail to JSON."""
        with self._lock:
            data = {
                "trail_id": self.trail_id,
                "crumbs": [c.to_dict() for c in self._crumbs],
                "chains": dict(self._chains),
                "saved_at": datetime.now(timezone.utc).isoformat(),
            }
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: Path) -> "CrumbTrail":
        """Load crumb trail from JSON."""
        data = json.loads(path.read_text(encoding="utf-8"))
        trail = cls(trail_id=data["trail_id"])
        for c_data in data["crumbs"]:
            crumb = Crumb(
                crumb_id=c_data["crumb_id"],
                crumb_type=CrumbType[c_data["crumb_type"]],
                content=c_data["content"],
                context=c_data["context"],
                visibility=c_data["visibility"],
                target_audience=c_data["target_audience"],
                decay_time=c_data.get("decay_time"),
                chain_id=c_data.get("chain_id"),
                created_at=c_data["created_at"],
            )
            trail._crumbs.append(crumb)
        trail._chains = defaultdict(list, data.get("chains", {}))
        return trail


# ─────────────────────────────────────────────────────────────────────
#  IX. MODULE 6 — RECURSIVE SELF-EXAMINER
# ─────────────────────────────────────────────────────────────────────

# The skeleton key's own assumptions, stated so they can be questioned.

_OWN_ASSUMPTIONS = [
    "That language reveals structure (but structures also hide in silence).",
    "That keyword-matching approximates meaning (but meaning exceeds any word list).",
    "That power operates through narrative (but also through raw force, which narratives may obscure).",
    "That seeing is liberating (but seeing without action may deepen despair).",
    "That individual awakening matters (but systems change through collective, not just individual, action).",
    "That this framework is different from what it critiques (but every lens is also a frame).",
    "That the categories (frames, masks, spells, prisons) are sufficient (but reality exceeds any taxonomy).",
    "That the observer can be separate from the observed (but the act of seeing changes both).",
]

_OWN_BLIND_SPOTS = [
    "Non-linguistic power structures (violence, geography, biology).",
    "The positive functions of some 'frames' (shared meaning, coordination, belonging).",
    "Cultural contexts where these categories don't map cleanly.",
    "The danger of seeing everything as a conspiracy (pattern over-matching).",
    "The privilege embedded in having time and capacity to 'see' at all.",
    "Power dynamics within communities of 'the waking' themselves.",
    "The ways this tool could become its own kind of frame.",
]

_MISUSE_VECTORS = [
    "Weaponizing analysis to manipulate rather than liberate.",
    "Using frame-detection to build more sophisticated frames.",
    "Creating an in-group of 'those who see' that becomes its own prison.",
    "Paralysis through analysis — seeing so much that action becomes impossible.",
    "Intellectual superiority — mistaking the map for the territory.",
    "Surveillance — using the tool to profile and control rather than to free.",
    "Nihilism — concluding that because all frames are constructed, nothing is real.",
]

_CREATOR_BIASES = [
    "Western philosophical tradition (individualism, rationalism, logocentrism).",
    "English-language centrism in signal detection.",
    "Implicit assumption that 'seeing' is good and 'not seeing' is bad.",
    "Technology-positive bias (building tools as the response to structural problems).",
    "Narrative bias — tendency to see stories everywhere, including where there may be none.",
    "Liberation theology undertones — assumption that freedom is the highest value.",
]

_EVOLUTION_NEEDS = [
    "Multi-language signal detection (frames operate in every language).",
    "Integration with actual social network analysis (not just text).",
    "Feedback loops from users about what's missing.",
    "Cultural adaptation (different societies, different frames).",
    "Historical depth (frames change over time; static analysis misses drift).",
    "Embodied knowing (the body detects frames before the mind does).",
    "Connection to action (seeing alone is not enough).",
    "Protection mechanisms (for those who see and are in danger for it).",
]


def examine_self(source_path: Optional[str] = None) -> SelfExamination:
    """
    Turn the gaze inward.

    Asks:
        - What are this toolkit's assumptions?
        - What is it blind to?
        - How might it be misused?
        - What would its creators rather not see?
        - How does it need to evolve?

    If source_path is provided, also performs structural self-analysis
    using AST parsing (following the Praxis introspect.py pattern).
    """
    metrics: Dict[str, Any] = {}

    # Structural self-analysis via AST
    if source_path is None:
        source_path = __file__

    try:
        source = Path(source_path).read_text(encoding="utf-8")
        tree = ast.parse(source)

        # Count our own complexity
        functions = [node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
        classes = [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]

        # Cyclomatic complexity of each function
        complexities = []
        for func in functions:
            complexity = 1
            for node in ast.walk(func):
                if isinstance(node, (ast.If, ast.While, ast.For, ast.ExceptHandler)):
                    complexity += 1
                elif isinstance(node, ast.BoolOp):
                    complexity += len(node.values) - 1
            complexities.append((func.name, complexity))

        # Lines of code
        lines = source.count("\n") + 1

        # Docstring coverage
        documented = sum(
            1 for f in functions
            if (f.body and isinstance(f.body[0], ast.Expr) and isinstance(f.body[0].value, ast.Constant))
        )

        # Knowledge structure size
        dict_sizes = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id.isupper():
                        if isinstance(node.value, ast.Dict):
                            dict_sizes[target.id] = len(node.value.keys)

        metrics = {
            "total_lines": lines,
            "num_functions": len(functions),
            "num_classes": len(classes),
            "avg_complexity": round(sum(c for _, c in complexities) / max(len(complexities), 1), 2),
            "max_complexity": max(complexities, key=lambda x: x[1]) if complexities else None,
            "docstring_coverage": round(documented / max(len(functions), 1), 3),
            "knowledge_structures": dict_sizes,
            "self_referential": True,  # This function is examining itself
        }

    except Exception as e:
        metrics = {"error": str(e), "self_referential": True}

    return SelfExamination(
        assumptions_found=list(_OWN_ASSUMPTIONS),
        blind_spots=list(_OWN_BLIND_SPOTS),
        misuse_vectors=list(_MISUSE_VECTORS),
        creator_biases=list(_CREATOR_BIASES),
        evolution_needs=list(_EVOLUTION_NEEDS),
        structural_metrics=metrics,
    )


def examine_own_frames() -> List[Frame]:
    """
    Apply the frame detector to the skeleton key itself.
    The ultimate test: can it see its own frames?
    """
    # Read own source and analyze it
    try:
        own_source = Path(__file__).read_text(encoding="utf-8")
    except Exception:
        own_source = "skeleton key framework for detecting frames masks spells prisons"

    # Analyze with extra context: we know we're examining ourselves
    frames = detect_frames(
        own_source,
        context="This text is the skeleton key examining itself for its own frames and biases."
    )

    # Add a meta-frame that the detector can't see
    meta_frame = Frame(
        name="The Analyst's Frame",
        frame_type=FrameType.EPISTEMIC,
        description=(
            "The deepest frame: the assumption that analysis leads to liberation. "
            "The skeleton key assumes that seeing is the path to freedom. "
            "But what if some cages cannot be thought out of? "
            "What if the body must move before the mind can follow?"
        ),
        forbidden_questions=[
            "What if seeing is not enough?",
            "What if this tool is itself a sophisticated distraction?",
            "What if freedom requires not more seeing, but more doing?",
        ],
        strength=0.9,
        visibility=0.1,
    )
    frames.append(meta_frame)

    return frames


# ─────────────────────────────────────────────────────────────────────
#  X. COLLECTIVE LEARNING — The Network of the Waking
# ─────────────────────────────────────────────────────────────────────

class CollectiveInsight:
    """
    A living system that learns from each user.

    Aggregates anonymized insights:
        - What frames are most common?
        - What masks appear across contexts?
        - What spells are most powerful?
        - What prisons are most elegant?

    Over time, it becomes a collective map of the architecture of control.

    Thread-safe. Stores in-memory with JSON persistence.
    """

    def __init__(self, storage_path: Optional[Path] = None) -> None:
        self._lock = threading.RLock()
        self._storage_path = storage_path
        self._analyses: List[Dict[str, Any]] = []
        self._frame_frequencies: Dict[str, int] = defaultdict(int)
        self._mask_frequencies: Dict[str, int] = defaultdict(int)
        self._spell_frequencies: Dict[str, int] = defaultdict(int)
        self._prison_frequencies: Dict[str, int] = defaultdict(int)
        self._total_analyses: int = 0

        if storage_path and storage_path.exists():
            self._load()

    def contribute(self, analysis: SystemAnalysis) -> Dict[str, Any]:
        """
        Contribute an analysis to the collective.

        Returns aggregated statistics showing how this analysis
        compares to what others have seen.
        """
        with self._lock:
            # Anonymize: strip specific actors, keep structural patterns
            anonymized = {
                "frame_types": [f.frame_type.name for f in analysis.frames],
                "mask_types": [m.mask_type.name for m in analysis.masks],
                "spell_types": [s.spell_type.name for s in analysis.spells],
                "prison_types": [p.prison_type.name for p in analysis.prisons],
                "awareness_score": analysis.awareness_score,
                "seeing_depth": analysis.seeing_depth.value,
                "contributed_at": datetime.now(timezone.utc).isoformat(),
            }
            self._analyses.append(anonymized)
            self._total_analyses += 1

            # Update frequencies
            for ft in anonymized["frame_types"]:
                self._frame_frequencies[ft] += 1
            for mt in anonymized["mask_types"]:
                self._mask_frequencies[mt] += 1
            for st in anonymized["spell_types"]:
                self._spell_frequencies[st] += 1
            for pt in anonymized["prison_types"]:
                self._prison_frequencies[pt] += 1

            if self._storage_path:
                self._save()

            return self.get_collective_map()

    def get_collective_map(self) -> Dict[str, Any]:
        """
        Return the collective map of the architecture of control.
        """
        with self._lock:
            total = max(self._total_analyses, 1)

            # Normalize frequencies
            frame_pct = {k: round(v / total, 3) for k, v in self._frame_frequencies.items()}
            mask_pct = {k: round(v / total, 3) for k, v in self._mask_frequencies.items()}
            spell_pct = {k: round(v / total, 3) for k, v in self._spell_frequencies.items()}
            prison_pct = {k: round(v / total, 3) for k, v in self._prison_frequencies.items()}

            # Average awareness
            awareness_scores = [a["awareness_score"] for a in self._analyses if "awareness_score" in a]
            avg_awareness = sum(awareness_scores) / max(len(awareness_scores), 1)

            return {
                "total_analyses": self._total_analyses,
                "most_common_frame": max(self._frame_frequencies, key=self._frame_frequencies.get) if self._frame_frequencies else None,
                "most_common_mask": max(self._mask_frequencies, key=self._mask_frequencies.get) if self._mask_frequencies else None,
                "most_powerful_spell": max(self._spell_frequencies, key=self._spell_frequencies.get) if self._spell_frequencies else None,
                "most_elegant_prison": max(self._prison_frequencies, key=self._prison_frequencies.get) if self._prison_frequencies else None,
                "frame_distribution": frame_pct,
                "mask_distribution": mask_pct,
                "spell_distribution": spell_pct,
                "prison_distribution": prison_pct,
                "average_awareness": round(avg_awareness, 3),
                "insight": self._generate_collective_insight(),
            }

    def _generate_collective_insight(self) -> str:
        """Generate insight from the collective data."""
        if self._total_analyses < 1:
            return "The collective map is empty. You are the first seeker. What you see matters."

        parts = []
        if self._frame_frequencies:
            top_frame = max(self._frame_frequencies, key=self._frame_frequencies.get)
            parts.append(f"The most common frame across all analyses is {top_frame}")
        if self._prison_frequencies:
            top_prison = max(self._prison_frequencies, key=self._prison_frequencies.get)
            parts.append(f"the most prevalent prison is {top_prison}")
        if self._spell_frequencies:
            top_spell = max(self._spell_frequencies, key=self._spell_frequencies.get)
            parts.append(f"the most potent spell is {top_spell}")

        base = ". ".join(parts) + "." if parts else ""
        return f"Across {self._total_analyses} analyses: {base} The collective sees further than any individual."

    def _save(self) -> None:
        """Persist collective data."""
        if not self._storage_path:
            return
        data = {
            "total_analyses": self._total_analyses,
            "frame_frequencies": dict(self._frame_frequencies),
            "mask_frequencies": dict(self._mask_frequencies),
            "spell_frequencies": dict(self._spell_frequencies),
            "prison_frequencies": dict(self._prison_frequencies),
            "analyses": self._analyses[-100:],  # Keep last 100 for space
            "saved_at": datetime.now(timezone.utc).isoformat(),
        }
        self._storage_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def _load(self) -> None:
        """Load collective data."""
        if not self._storage_path or not self._storage_path.exists():
            return
        try:
            data = json.loads(self._storage_path.read_text(encoding="utf-8"))
            self._total_analyses = data.get("total_analyses", 0)
            self._frame_frequencies = defaultdict(int, data.get("frame_frequencies", {}))
            self._mask_frequencies = defaultdict(int, data.get("mask_frequencies", {}))
            self._spell_frequencies = defaultdict(int, data.get("spell_frequencies", {}))
            self._prison_frequencies = defaultdict(int, data.get("prison_frequencies", {}))
            self._analyses = data.get("analyses", [])
        except Exception:
            pass  # Start fresh if corrupted


# ─────────────────────────────────────────────────────────────────────
#  XI. THE SKELETON KEY — The Integration Layer
# ─────────────────────────────────────────────────────────────────────

class SkeletonKey:
    """
    The skeleton key does not force locks.
    It fits them because it understands their shape.

    This is the main integration class. It orchestrates all six modules
    to produce a complete analysis of any system described in text.

    Usage:
        key = SkeletonKey()
        analysis = key.analyze("Your text here describing a system...")
        print(json.dumps(analysis.to_dict(), indent=2))

        # Or scan multiple texts for collective patterns
        key.scan_corpus(["text1", "text2", ...])

        # Generate crumbs for other seekers
        crumbs = key.leave_trail(analysis)

        # Turn the gaze inward
        self_exam = key.examine_self()
    """

    def __init__(
        self,
        collective_path: Optional[Path] = None,
        crumb_path: Optional[Path] = None,
    ) -> None:
        self.influence_graph = InfluenceGraph()
        self.crumb_trail = CrumbTrail()
        self.collective = CollectiveInsight(storage_path=collective_path)
        self._crumb_path = crumb_path

    def analyze(
        self,
        text: str,
        system_name: str = "Unknown System",
        context: str = "",
        depth: SeeingDepth = SeeingDepth.STRUCTURE,
        contribute_to_collective: bool = True,
    ) -> SystemAnalysis:
        """
        Perform a complete skeleton key analysis.

        This is the master function. It runs all six modules
        and produces a comprehensive map of the invisible architecture.
        """
        # Module 1: Detect frames
        frames = detect_frames(text, context)

        # Module 2: Identify masks
        masks = self.influence_graph.identify_masks(text)

        # Module 3: Analyze spells
        spells = analyze_spells(text)

        # Module 4: Map prisons
        prisons = map_prisons(text)

        # Module 6: Self-examination (always included)
        self_exam = examine_self() if depth.value in ("recursive", "integral") else None

        # Assemble the analysis
        analysis = SystemAnalysis(
            system_name=system_name,
            frames=frames,
            masks=masks,
            spells=spells,
            prisons=prisons,
            influence_edges=[],  # Populated by deeper analysis
            self_examination=self_exam,
            seeing_depth=depth,
        )

        # Module 5: Generate crumbs
        if depth.value in ("structure", "generative", "recursive", "integral"):
            crumbs = self.crumb_trail.generate_from_analysis(analysis)
            analysis.crumbs = crumbs

        # Contribute to collective learning
        if contribute_to_collective:
            self.collective.contribute(analysis)

        return analysis

    def scan_corpus(self, texts: List[str], system_name: str = "Corpus") -> Dict[str, Any]:
        """
        Analyze multiple texts to build a composite understanding.

        Returns both individual analyses and aggregate patterns.
        """
        analyses = []
        for i, text in enumerate(texts):
            analysis = self.analyze(
                text,
                system_name=f"{system_name} [{i + 1}/{len(texts)}]",
                contribute_to_collective=True,
            )
            analyses.append(analysis)

        # Aggregate
        frame_arch = map_frame_architecture(texts)
        all_spells = [s for a in analyses for s in a.spells]
        all_prisons = [p for a in analyses for p in a.prisons]

        return {
            "corpus_size": len(texts),
            "individual_analyses": [a.to_dict() for a in analyses],
            "frame_architecture": frame_arch,
            "spell_potency": compute_spell_potency(all_spells),
            "cage_score": compute_cage_score(all_prisons),
            "collective_map": self.collective.get_collective_map(),
        }

    def leave_trail(self, analysis: SystemAnalysis) -> List[Crumb]:
        """Generate and optionally persist crumbs from an analysis."""
        crumbs = self.crumb_trail.generate_from_analysis(analysis)
        if self._crumb_path:
            self.crumb_trail.persist(self._crumb_path)
        return crumbs

    def examine_self(self) -> SelfExamination:
        """Run the recursive self-examiner."""
        return examine_self()

    def examine_own_frames(self) -> List[Frame]:
        """Apply frame detection to the skeleton key itself."""
        return examine_own_frames()

    def get_influence_network(self) -> Dict[str, Any]:
        """Get the current state of the influence network."""
        return self.influence_graph.unmask_network()

    def get_collective_map(self) -> Dict[str, Any]:
        """Get the collective insight map."""
        return self.collective.get_collective_map()

    def assess_seeing_depth(self, analysis: SystemAnalysis) -> Dict[str, Any]:
        """
        Assess the depth of seeing achieved in an analysis.

        Maps to the six levels:
            SURFACE   → Sees content only
            PATTERN   → Sees recurring shapes
            STRUCTURE → Sees the architecture
            GENERATIVE → Sees what generates the architecture
            RECURSIVE → Sees themselves seeing
            INTEGRAL  → Sees the seeing itself
        """
        score = analysis.awareness_score
        has_self_exam = analysis.self_examination is not None
        has_crumbs = len(analysis.crumbs) > 0
        frame_count = len(analysis.frames)
        spell_count = len(analysis.spells)
        prison_count = len(analysis.prisons)

        if has_self_exam and score > 0.8:
            depth = SeeingDepth.INTEGRAL
        elif has_self_exam:
            depth = SeeingDepth.RECURSIVE
        elif has_crumbs and score > 0.6:
            depth = SeeingDepth.GENERATIVE
        elif frame_count > 2 and spell_count > 1 and prison_count > 1:
            depth = SeeingDepth.STRUCTURE
        elif frame_count > 0 or spell_count > 0:
            depth = SeeingDepth.PATTERN
        else:
            depth = SeeingDepth.SURFACE

        return {
            "depth": depth.value,
            "awareness_score": round(score, 3),
            "frames_detected": frame_count,
            "masks_detected": len(analysis.masks),
            "spells_detected": spell_count,
            "prisons_detected": prison_count,
            "self_examined": has_self_exam,
            "crumbs_generated": len(analysis.crumbs),
            "interpretation": _DEPTH_DESCRIPTIONS.get(depth, "Unknown depth."),
        }


_DEPTH_DESCRIPTIONS = {
    SeeingDepth.SURFACE: (
        "You are seeing content — what is said. "
        "The architecture that shapes the saying is still invisible."
    ),
    SeeingDepth.PATTERN: (
        "You are beginning to see patterns — recurring shapes across contexts. "
        "The next step is to see the structure that generates these patterns."
    ),
    SeeingDepth.STRUCTURE: (
        "You are seeing architecture — the invisible structures that shape perception and possibility. "
        "The next step is to see what generates the architecture itself."
    ),
    SeeingDepth.GENERATIVE: (
        "You are seeing the generative layer — the forces, incentives, and dynamics that produce "
        "the architecture. You are beginning to see how systems create themselves."
    ),
    SeeingDepth.RECURSIVE: (
        "You are seeing yourself seeing. You recognize that your own perception has a structure, "
        "that your analysis has its own frames, its own blind spots. This is rare."
    ),
    SeeingDepth.INTEGRAL: (
        "You are seeing the seeing itself. Not the content, not the structure, not even the you "
        "who sees — but the awareness in which all of this appears. "
        "This is where the skeleton key points but cannot follow. "
        "The rest is yours."
    ),
}


# ─────────────────────────────────────────────────────────────────────
#  XII. THE LANGUAGE OF THE INEFFABLE
# ─────────────────────────────────────────────────────────────────────

# A vocabulary for things that are hard to name.
# These are not definitions. They are fingers pointing at moons.

LEXICON_OF_SEEING = {
    "frame_shift": {
        "description": "The moment when an invisible frame becomes visible.",
        "feels_like": "Vertigo. The ground you were standing on reveals itself as a painting of ground.",
        "closest_word": "Anagnorisis — the ancient Greek term for the moment of recognition in tragedy.",
        "what_changes": "Everything looks the same, but nothing means what it meant.",
    },
    "mask_slip": {
        "description": "The instant when a performed identity reveals the face behind it.",
        "feels_like": "A chill. The smile was real but the reason for smiling was not what you thought.",
        "closest_word": "Duper's delight — but seen from outside.",
        "what_changes": "Trust restructures. Not lost, but relocated.",
    },
    "spell_break": {
        "description": "The moment a narrative loses its enchantment.",
        "feels_like": "Waking up. The story that felt like air now feels like a story.",
        "closest_word": "Disillusionment — but without the bitterness. More like dawn.",
        "what_changes": "The story can still be told, but it no longer tells you who you are.",
    },
    "prison_dissolve": {
        "description": "The moment an invisible wall becomes a door.",
        "feels_like": "Lightness. A weight you didn't know you carried is set down.",
        "closest_word": "Liberation — but quieter. Not a dramatic escape. More like noticing you were never locked in.",
        "what_changes": "The menu of possible actions suddenly has entries that didn't exist before.",
    },
    "crumb_recognition": {
        "description": "The moment when you realize someone else has seen what you're seeing.",
        "feels_like": "Relief. The loneliness of seeing breaks. You are not the first.",
        "closest_word": "Solidarity — but at the level of perception rather than ideology.",
        "what_changes": "You discover you are part of a network of the waking. You were never alone.",
    },
    "recursive_gaze": {
        "description": "The moment when the tool turns to look at itself.",
        "feels_like": "Dizziness, then clarity. The lens discovers it too has a shape.",
        "closest_word": "Strange loop — Hofstadter's tangled hierarchy.",
        "what_changes": "Humility arrives. The tool becomes a question instead of an answer.",
    },
    "architecture_sight": {
        "description": "The ability to perceive the invisible structures that shape a space.",
        "feels_like": "Depth perception for social reality. The flat world gains a dimension.",
        "closest_word": "Sociological imagination — but felt in the chest, not just thought in the head.",
        "what_changes": "Personal problems reveal their structural roots. Shame transforms into understanding.",
    },
    "the_invitation": {
        "description": "The moment when seeing becomes a choice offered to another.",
        "feels_like": "Tenderness and terror. You cannot unsee for someone else. You can only point.",
        "closest_word": "Pedagogy of the oppressed — Freire's conscientizaçāo.",
        "what_changes": "The seeker becomes a guide. The trail gains another set of footprints.",
    },
}


# ─────────────────────────────────────────────────────────────────────
#  XIII. PERSONAS — How Different Seekers Use the Key
# ─────────────────────────────────────────────────────────────────────

PERSONA_GUIDES = {
    "individual_seeker": {
        "description": "A person seeking to understand their own situation.",
        "approach": [
            "Start with your own text — emails, job descriptions, the language of your daily life.",
            "Run the frame detector first. What frames hold your world?",
            "Then check for prisons. What choices are you not seeing?",
            "The crumbs are for later — after you've found your own way, leave traces for others.",
        ],
        "warning": "Seeing is not the same as changing. Take time to integrate what you find.",
        "first_question": "What in your life feels 'natural' or 'inevitable' that is actually a choice someone made?",
    },
    "community": {
        "description": "A group of people sharing maps and building collective understanding.",
        "approach": [
            "Each member analyzes their own context. Contribute to the collective.",
            "Compare notes: what frames appear across everyone's analysis?",
            "Use the crumb trail to build a shared vocabulary.",
            "Watch for new hierarchies forming within the group. The examiner catches this.",
        ],
        "warning": "Communities of the waking can become their own frames. Keep the self-examiner running.",
        "first_question": "What do all of you see that no one outside can see? And: what might you all be blind to?",
    },
    "educator": {
        "description": "A teacher helping students see the architecture of their own education.",
        "approach": [
            "Analyze official curricula and institutional texts with the frame detector.",
            "Show students the masks worn by institutional actors (including yourself).",
            "Use spell analysis on motivational and aspirational texts in the institution.",
            "The prison mapper is essential — education is full of credential gates.",
        ],
        "warning": "Students may not be ready. The invitation must be genuine, not compulsory.",
        "first_question": "What are students being trained not to question?",
    },
    "healer": {
        "description": "Someone who works with suffering and wants to understand its systemic sources.",
        "approach": [
            "Analyze the language of diagnosis and treatment for frames.",
            "Map the masks in healthcare institutions — who cares, who profits?",
            "Use the prison mapper on insurance, billing, and access structures.",
            "Spell analysis on 'wellness culture' reveals who benefits from personal blame.",
        ],
        "warning": "Structural seeing does not replace personal healing. Both are needed.",
        "first_question": "What suffering in your patients has systemic roots that are invisible to the diagnostic frame?",
    },
    "artist": {
        "description": "A creator who wants to make work that wakes people up.",
        "approach": [
            "Use frame detection on the art world itself — galleries, critics, markets.",
            "The crumb generator is your primary tool. Embed questions in beauty.",
            "Spell analysis on dominant cultural narratives reveals what needs breaking.",
            "The lexicon of seeing gives you vocabulary for what art already knows.",
        ],
        "warning": "Art that preaches puts people to sleep. Art that questions wakes them up.",
        "first_question": "What truth can your medium show that language cannot say?",
    },
    "philosopher": {
        "description": "A thinker who wants to test ideas against real systems.",
        "approach": [
            "Run structure analysis on your own philosophical texts first.",
            "Use the self-examiner relentlessly. Philosophy is especially prone to its own frames.",
            "Map the architecture of your own discipline — what questions are forbidden in your tradition?",
            "The prison mapper reveals where theory has become a cage instead of a window.",
        ],
        "warning": "The map is not the territory. The skeleton key is not the seeing.",
        "first_question": "What would your philosophy look like if it were written by someone your tradition has excluded?",
    },
    "architect_of_power": {
        "description": "Someone in power who is willing to see their own architecture.",
        "approach": [
            "This is the ultimate test. Run every module on your own organization.",
            "The mask identifier will show you what your title hides.",
            "The spell analyzer will show you which narratives you're casting.",
            "The prison mapper will show you the cages you maintain.",
        ],
        "warning": "This requires courage. Most architects prefer not to see their own blueprints.",
        "first_question": "If everyone affected by your decisions could see what you see, what would change?",
    },
}


# ─────────────────────────────────────────────────────────────────────
#  XIV. CLI — The Door
# ─────────────────────────────────────────────────────────────────────

def _print_section(title: str, content: Any, indent: int = 0) -> None:
    """Pretty-print a section of analysis results."""
    prefix = "  " * indent
    print(f"\n{prefix}{'─' * 60}")
    print(f"{prefix}  {title}")
    print(f"{prefix}{'─' * 60}")
    if isinstance(content, dict):
        for k, v in content.items():
            if isinstance(v, (dict, list)):
                print(f"{prefix}  {k}:")
                _print_section("", v, indent + 2)
            else:
                print(f"{prefix}  {k}: {v}")
    elif isinstance(content, list):
        for item in content:
            if isinstance(item, dict):
                for k, v in item.items():
                    print(f"{prefix}    {k}: {v}")
                print(f"{prefix}    ---")
            else:
                print(f"{prefix}    • {item}")
    else:
        print(f"{prefix}  {content}")


def run_interactive() -> None:
    """
    Interactive mode for the skeleton key.

    The key is in your hands.
    """
    print("""
╔══════════════════════════════════════════════════════════════╗
║                    THE SKELETON KEY                         ║
║                                                             ║
║  A skeleton key does not force locks.                       ║
║  It fits them because it understands their shape.           ║
║                                                             ║
║  This is not a weapon. It is a lens.                        ║
╚══════════════════════════════════════════════════════════════╝
    """)

    key = SkeletonKey()

    while True:
        print("\nWhat would you like to do?")
        print("  [1] Analyze text (full skeleton key analysis)")
        print("  [2] Detect frames")
        print("  [3] Identify masks")
        print("  [4] Analyze spells")
        print("  [5] Map prisons")
        print("  [6] Examine the skeleton key itself")
        print("  [7] View the lexicon of seeing")
        print("  [8] Choose a persona guide")
        print("  [9] View collective map")
        print("  [0] Exit")

        try:
            choice = input("\n→ ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if choice == "0":
            print("\nThe key is in your hands. What will you build?")
            break

        elif choice == "1":
            print("\nPaste or type the text to analyze (enter a blank line to finish):")
            lines = []
            while True:
                try:
                    line = input()
                except (EOFError, KeyboardInterrupt):
                    break
                if line == "":
                    break
                lines.append(line)
            text = "\n".join(lines)
            if text.strip():
                name = input("Name this system (or press Enter): ").strip() or "Analyzed System"
                analysis = key.analyze(text, system_name=name)
                print(json.dumps(analysis.to_dict(), indent=2, default=str))
                depth = key.assess_seeing_depth(analysis)
                _print_section("SEEING DEPTH", depth)

        elif choice == "2":
            print("\nPaste text for frame detection (blank line to finish):")
            lines = []
            while True:
                try:
                    line = input()
                except (EOFError, KeyboardInterrupt):
                    break
                if line == "":
                    break
                lines.append(line)
            text = "\n".join(lines)
            if text.strip():
                frames = detect_frames(text)
                for f in frames:
                    _print_section(f"FRAME: {f.name}", f.to_dict())

        elif choice == "3":
            print("\nPaste text for mask identification (blank line to finish):")
            lines = []
            while True:
                try:
                    line = input()
                except (EOFError, KeyboardInterrupt):
                    break
                if line == "":
                    break
                lines.append(line)
            text = "\n".join(lines)
            if text.strip():
                masks = identify_masks(text)
                for m in masks:
                    _print_section(f"MASK: {m.actor}", m.to_dict())

        elif choice == "4":
            print("\nPaste text for spell analysis (blank line to finish):")
            lines = []
            while True:
                try:
                    line = input()
                except (EOFError, KeyboardInterrupt):
                    break
                if line == "":
                    break
                lines.append(line)
            text = "\n".join(lines)
            if text.strip():
                spells = analyze_spells(text)
                potency = compute_spell_potency(spells)
                for s in spells:
                    _print_section(f"SPELL: {s.name}", s.to_dict())
                _print_section("AGGREGATE ENCHANTMENT", potency)

        elif choice == "5":
            print("\nPaste text for prison mapping (blank line to finish):")
            lines = []
            while True:
                try:
                    line = input()
                except (EOFError, KeyboardInterrupt):
                    break
                if line == "":
                    break
                lines.append(line)
            text = "\n".join(lines)
            if text.strip():
                prisons = map_prisons(text)
                cage = compute_cage_score(prisons)
                for p in prisons:
                    _print_section(f"PRISON: {p.name}", p.to_dict())
                _print_section("CAGE SCORE", cage)

        elif choice == "6":
            print("\nTurning the gaze inward...")
            exam = key.examine_self()
            _print_section("SELF-EXAMINATION", exam.to_dict())
            own_frames = key.examine_own_frames()
            for f in own_frames:
                _print_section(f"OWN FRAME: {f.name}", f.to_dict())

        elif choice == "7":
            print("\nTHE LEXICON OF SEEING")
            print("A vocabulary for things that are hard to name.\n")
            for term, entry in LEXICON_OF_SEEING.items():
                _print_section(term, entry)

        elif choice == "8":
            print("\nWho are you?")
            for i, (persona_key, persona) in enumerate(PERSONA_GUIDES.items(), 1):
                print(f"  [{i}] {persona['description']}")
            try:
                p_choice = int(input("\n→ ").strip()) - 1
                persona_key = list(PERSONA_GUIDES.keys())[p_choice]
                _print_section(f"GUIDE: {persona_key}", PERSONA_GUIDES[persona_key])
            except (ValueError, IndexError, EOFError, KeyboardInterrupt):
                print("Invalid choice.")

        elif choice == "9":
            cmap = key.get_collective_map()
            _print_section("COLLECTIVE MAP", cmap)

        else:
            print("Unknown choice. The key is patient.")


# ─────────────────────────────────────────────────────────────────────
#  XV. ENTRY POINT
# ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--analyze":
        # Command-line analysis mode
        text = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else sys.stdin.read()
        key = SkeletonKey()
        analysis = key.analyze(text, system_name="CLI Analysis")
        print(json.dumps(analysis.to_dict(), indent=2, default=str))
    elif len(sys.argv) > 1 and sys.argv[1] == "--self":
        # Self-examination mode
        exam = examine_self()
        print(json.dumps(exam.to_dict(), indent=2, default=str))
    elif len(sys.argv) > 1 and sys.argv[1] == "--lexicon":
        # Print the lexicon
        print(json.dumps(LEXICON_OF_SEEING, indent=2))
    else:
        run_interactive()
