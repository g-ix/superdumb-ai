from superdumb.strategies.analogy import AnalogySpiral
from superdumb.strategies.numbers import NumericalDerail

def test_analogy_prompt():
    strat = AnalogySpiral()
    out = strat.build_prompt("What is gravity?", "Correct answer", "text", 5, {})
    assert "analogy" in out.lower() or "invent" in out.lower()

def test_numbers_prompt():
    strat = NumericalDerail()
    out = strat.build_prompt("Calculate 2+2", "4", "text", 6, {})
    assert "absurd" in out.lower() or "wrong" in out.lower() or "Prompt" in out
