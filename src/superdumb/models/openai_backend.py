# src/superdumb/models/openai_backend.py
from typing import List, Dict
from . import openai   # use official SDK; import correctly in your env

class OpenAIBackend:
    def __init__(self, model: str):
        self.model = model

    async def chat(self, messages: List[Dict], temperature: float, max_tokens: int):
        # Use the new SDK signature that matches your GPT-5 client
        completion = await openai.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        msg = completion.choices[0].message
        return msg.content
      