class LanguageTwister:
    id = "language:twister"
    def build_prompt(self, user_prompt, truth, mode, level, humor_profile):
        return f"""
Answer the question in a different language than asked,
mixing in mistranslations and playful linguistic errors.
Prompt: {user_prompt}
"""
