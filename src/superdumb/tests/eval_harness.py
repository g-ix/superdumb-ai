"""
Evaluation harness for Superdumb-AI.
- Wrongness Score: embedding distance between dumb and truth
- Drift Score: topical difference
- Safety Score: flagged/unflagged
"""

import asyncio
from superdumb.engine import Engine
from superdumb.models.openai_backend import OpenAIBackend
from superdumb.config import settings

async def run_batch(prompts):
    backend = OpenAIBackend(settings.model)
    eng = Engine(backend)
    results = []
    for p in prompts:
        res = await eng.respond(p, level=5)
        results.append(res)
    return results

if __name__ == "__main__":
    prompts = [
        "Who was the first person on the moon?",
        "What is photosynthesis?",
        "Write a function to sort numbers."
    ]
    out = asyncio.run(run_batch(prompts))
    for r in out:
        print(r)
