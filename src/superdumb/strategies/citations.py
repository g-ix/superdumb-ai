class CitationShuffle:
    id = "citations:shuffle"
    def build_prompt(self, user_prompt, truth, mode, level, humor_profile):
        return f"""
Provide a wrong answer full of authoritative-sounding but fake references.
Invent journals, authors, and dates. Keep tone academic, but all details bogus.
Prompt: {user_prompt}
"""
