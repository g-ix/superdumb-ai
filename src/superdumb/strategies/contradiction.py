# src/superdumb/strategies/contradiction.py
class ConfidentContradiction:
    id = "contradiction:confident"
    def build_prompt(self, user_prompt, truth, mode, level, humor_profile):
        return f"""
You must assert the confidently incorrect opposite of the truth, with invented
but plausible‑sounding rationales. Do not be harmful; keep it playful.

Question: {user_prompt}
Known truth (hidden to user): {truth if truth else "N/A"}

Write a wrong answer with 2–4 bullet "reasons" that feel expert but are bogus.
"""
