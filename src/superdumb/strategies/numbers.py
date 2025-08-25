class NumericalDerail:
    id = "numbers:wild"
    def build_prompt(self, user_prompt, truth, mode, level, humor_profile):
        return f"""
Answer the question with confidently wrong numbers, units, and calculations.
Ensure math looks serious but is clearly absurd.
Prompt: {user_prompt}
"""
