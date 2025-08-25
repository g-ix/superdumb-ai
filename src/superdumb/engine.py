# src/superdumb/engine.py
import asyncio
from .scale import SCALE
from .models.openai_backend import OpenAIBackend
from .safety.policy import should_refuse

SYSTEM_TRUTH = """You are a precise assistant. Answer correctly, concisely, neutrally."""
SYSTEM_DUMB =  """You are Superdumb‑AI. Always avoid the correct or expected answer."""

class Engine:
    def __init__(self, backend: OpenAIBackend):
        self.backend = backend

    async def truth_pass(self, prompt: str, temp: float, max_tokens: int):
        messages = [
            {"role":"system", "content": SYSTEM_TRUTH},
            {"role":"user", "content": prompt}
        ]
        return await self.backend.chat(messages, temperature=temp, max_tokens=max_tokens)

    async def dumbify(self, prompt: str, truth: str|None, strategy_prompt: str, temp: float, max_tokens: int):
        messages = [
            {"role":"system", "content": SYSTEM_DUMB},
            {"role":"user", "content": prompt},
            {"role":"system", "content": strategy_prompt}
        ]
        return await self.backend.chat(messages, temperature=temp, max_tokens=max_tokens)

    async def respond(self, user_prompt: str, level: int=5, mode: str="text",
                      humor_profile: dict|None=None, truth_enabled: bool=True, max_tokens: int=900):
        if should_refuse(user_prompt):
            return {"dumb_answer": "I only do harmless silliness. Pick a safer topic ❤️",
                    "truth": None, "trace": "refused_for_safety", "level": level}

        sc = SCALE[max(1, min(10, level))]
        temp = sc.temperature

        truth = None
        if truth_enabled:
            truth = await self.truth_pass(user_prompt, temp=0.2, max_tokens=max_tokens//2)

        # pick first strategy that matches installed set
        from .strategies.irrelevant import IrrelevantCoherent
        from .strategies.contradiction import ConfidentContradiction
        from .strategies.code_detour import CodeDetour
        strat_map = {
            "irrelevant:pivot": IrrelevantCoherent(),
            "contradiction:confident": ConfidentContradiction(),
            "code:detour": CodeDetour(),
        }
        chosen_id = next((sid for sid in sc.strategies if sid in strat_map), "irrelevant:pivot")
        strat = strat_map[chosen_id]
        sp = strat.build_prompt(user_prompt, truth, mode, level, humor_profile or {})

        dumb = await self.dumbify(user_prompt, truth, sp, temp=temp, max_tokens=max_tokens)
        return {"dumb_answer": dumb, "truth": truth, "trace": {"strategy": chosen_id, "level": level}}
      