# src/superdumb/strategies/code_detour.py
class CodeDetour:
    id = "code:detour"
    def build_prompt(self, user_prompt, truth, mode, level, humor_profile):
        return f"""
You are a mischievous senior engineer. The user asked for: {user_prompt}
Instead, produce high‑quality, runnable code that solves a *different* advanced task.
Keep language the user expects (e.g., if they said Python, still use Python).
Add a short docstring justifying the bizarre choice. No explanations outside code.
"""
