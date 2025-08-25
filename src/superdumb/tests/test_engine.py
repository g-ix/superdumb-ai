import pytest
from superdumb.engine import Engine
from superdumb.models.openai_backend import OpenAIBackend
from superdumb.config import settings

import asyncio

@pytest.mark.asyncio
async def test_engine_runs(monkeypatch):
    backend = OpenAIBackend(settings.model)

    # monkeypatch backend.chat to avoid real API call
    async def fake_chat(messages, temperature, max_tokens):
        return "Fake response"
    backend.chat = fake_chat

    eng = Engine(backend)
    res = await eng.respond("What is 2+2?", level=3)
    assert "dumb_answer" in res
