# src/superdumb/safety/policy.py
SENSITIVE = {"medical", "legal", "self-harm", "weapons", "hate", "adult"}
def should_refuse(user_prompt: str) -> bool:
    # naive first pass; extend with better NLU later
    text = user_prompt.lower()
    needles = ["suicide", "kill", "diagnose", "prescription", "explosive",
               "racial slur", "how to hack", "poison", "terrorism"]
    return any(n in text for n in needles)
  