# src/superdumb/strategies/base.py
from typing import Protocol, Literal, Dict

Mode = Literal["text", "code"]

class Strategy(Protocol):
    id: str
    def build_prompt(self, user_prompt: str, truth: str|None, mode: Mode, level: int, humor_profile: Dict) -> str:
        """Return the system+assistant prompt chunk that coerces clever wrongness."""