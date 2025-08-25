# src/superdumb/cli.py
import asyncio, argparse
from .models.openai_backend import OpenAIBackend
from .engine import Engine
from .config import settings

def main():
    p = argparse.ArgumentParser()
    p.add_argument("prompt", type=str)
    p.add_argument("--level", type=int, default=5)
    p.add_argument("--mode", type=str, default="text")
    p.add_argument("--reveal", action="store_true")
    args = p.parse_args()

    async def run():
        eng = Engine(OpenAIBackend(settings.model))
        res = await eng.respond(args.prompt, level=args.level, mode=args.mode, truth_enabled=args.reveal)
        print("\n[DUMB]\n", res["dumb_answer"])
        if args.reveal and res["truth"]:
            print("\n[TRUTH]\n", res["truth"])
        print("\n[TRACE]", res["trace"])

    asyncio.run(run())

if __name__ == "__main__":
    main()