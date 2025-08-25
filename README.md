# **Superdumb-AI**: *Let there be dumbness.*

**“In the world of Super-Intelligent AI, meet Superdumb-AI.”**

Superdumb-AI is an intentionally wrong AI assistant.  
It never gives the expected or correct answer — instead it produces witty, absurd, cleverly orchestrated nonsense.  
Useful for:
- 🎭 Entertainment & creative humor
- 📚 Critical thinking exercises
- 🧪 Testing LLM robustness (adversarial nonsense)
- 💻 Coding chaos (working but off-task code)

⚠️ **Warning:** This AI is wrong on purpose. Do not use for real advice.

---

## Features
- **Dumbness Scale (1–10)**: from “Almost Reliable” to “Super Dumb”
- **Truth+Transform mode**: optionally reveal the correct answer
- **Strategies**: irrelevant pivots, contradictions, code detours, fake citations…
- **Backends**: GPT-5 (via OpenAI API), local LLaMA/HF (stubbed, future)
- **Interfaces**: CLI, REST API (FastAPI), web playground (later)

---

## Quickstart

1. Clone & install:
   ```bash
   git clone https://github.com/you/superdumb-ai
   cd superdumb-ai
   pip install -e .
   cp .env.example .env
   # add your OPENAI_API_KEY


## Current Project Structure:
```
superdumb-ai/
├─ README.md
├─ LICENSE
├─ pyproject.toml               # or requirements.txt + setup.cfg
├─ .env.example
├─ src/
│  └─ superdumb/
│     ├─ __init__.py
│     ├─ config.py
│     ├─ models/
│     │  ├─ openai_backend.py   # GPT-5 client
│     │  └─ local_backend.py    # (stub) LLaMA/HF later
│     ├─ strategies/
│     │  ├─ base.py
│     │  ├─ irrelevant.py
│     │  ├─ contradiction.py
│     │  ├─ analogy.py
│     │  ├─ numbers.py
│     │  ├─ citations.py
│     │  ├─ code_detour.py
│     │  └─ language_twister.py
│     ├─ safety/
│     │  ├─ policy.py
│     │  └─ filters.py
│     ├─ engine.py              # Truth → Transform orchestration
│     ├─ scale.py               # Dumbness mapping
│     ├─ api.py                 # FastAPI app
│     └─ cli.py                 # CLI entry
├─ tests/
│  ├─ test_engine.py
│  ├─ test_strategies.py
│  └─ eval_harness.py           # enterprise evaluation
└─ examples/
   ├─ requests.http             # sample REST calls
   └─ prompts.md                # showcase
```
