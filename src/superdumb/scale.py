# src/superdumb/scale.py
from dataclasses import dataclass

@dataclass(frozen=True)
class ScaleLevel:
    name: str
    temperature: float
    strategies: list[str]   # strategy ids by preference order

SCALE = {
    1: ScaleLevel("Almost Reliable", 0.6, ["contradiction:subtle", "numbers:minor"]),
    2: ScaleLevel("Slightly Silly", 0.65, ["irrelevant:nearby", "analogy:mild"]),
    3: ScaleLevel("Cheeky Detour", 0.7, ["irrelevant:adjacent", "numbers:offset"]),
    4: ScaleLevel("Playful Wrong", 0.8, ["analogy:deep", "contradiction:confident"]),
    5: ScaleLevel("Half‑Wit", 0.9, ["irrelevant:pivot", "citations:shuffle"]),
    6: ScaleLevel("Bent Reality", 1.0, ["analogy:spiral", "numbers:wild"]),
    7: ScaleLevel("Absurdist", 1.05, ["irrelevant:far", "socratic:mislead"]),
    8: ScaleLevel("Chaotic", 1.1, ["citations:grandiose", "analogy:surreal"]),
    9: ScaleLevel("Unhinged", 1.15, ["irrelevant:remote", "numbers:fantasy"]),
    10: ScaleLevel("Super Dumb", 1.2, ["code:detour", "irrelevant:cosmic", "analogy:cosmic"]),
}
