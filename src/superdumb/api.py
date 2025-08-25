# src/superdumb/api.py
from fastapi import FastAPI
from pydantic import BaseModel
from .config import settings
from .models.openai_backend import OpenAIBackend
from .engine import Engine

app = FastAPI(title="Superdumb-AI")
backend = OpenAIBackend(settings.model)
engine = Engine(backend)

class AskReq(BaseModel):
    prompt: str
    level: int = 5
    mode: str = "text"      # "text" | "code"
    truth_enabled: bool = True
    humor_profile: dict = {}

@app.post("/respond")
async def respond(req: AskReq):
    data = await engine.respond(req.prompt, level=req.level, mode=req.mode,
                                humor_profile=req.humor_profile, truth_enabled=req.truth_enabled)
    # Hide truth by default; expose tokenized flow on separate endpoint in your UI
    return {"dumb_answer": data["dumb_answer"], "trace": data["trace"], "has_truth": data["truth"] is not None}

@app.post("/reveal")
async def reveal(req: AskReq):
    data = await engine.respond(req.prompt, level=req.level, mode=req.mode,
                                humor_profile=req.humor_profile, truth_enabled=True)
    return {"truth": data["truth"], "trace": data["trace"]}
  