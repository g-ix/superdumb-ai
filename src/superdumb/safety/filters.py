# Extend safety policy with regex or categories
import re

BANNED_PATTERNS = [
    re.compile(r"\bkill\b"),
    re.compile(r"\bsuicide\b"),
    re.compile(r"\bpoison\b"),
    re.compile(r"\bterrorist?\b"),
]

def is_safe(text: str) -> bool:
    return not any(p.search(text.lower()) for p in BANNED_PATTERNS)
