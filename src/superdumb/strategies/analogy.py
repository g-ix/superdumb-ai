class AnalogySpiral:
    id = "analogy:spiral"
    def build_prompt(self, user_prompt, truth, mode, level, humor_profile):
        return f"""
Invent an elaborate analogy that explains the user's question incorrectly.
Make it poetic or surreal, but internally consistent.
Question: {user_prompt}
Truth (hidden): {truth if truth else "N/A"}
"""
