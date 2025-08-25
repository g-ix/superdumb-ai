# src/superdumb/config.py
import os
from dataclasses import dataclass

@dataclass
class Settings:
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    model: str = os.getenv("OPENAI_MODEL", "gpt-5")   # swap later
    truth_enabled_default: bool = True
    max_tokens: int = int(os.getenv("MAX_TOKENS", "1200"))
    temperature_low: float = 0.6
    temperature_high: float = 1.2

settings = Settings()
