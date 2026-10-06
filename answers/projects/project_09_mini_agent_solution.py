"""
Solution for Project 09 - Mini Agent with Tools.

Run it with:
    python answers/projects/project_09_mini_agent_solution.py

Builds the classic agent loop with three local tools (a no-eval
calculator, a word counter, a unit converter), a defensive executor
that survives unknown tools and bad arguments, and a SIMULATED policy
(if-rules) that decides the next tool call. Comments show the exact
shapes of a real LLM tool-use exchange: tools in the request,
tool_use block back, tool_result message returned. 100% offline.
"""

from __future__ import annotations

import ast
import json
import operator
import re
from textwrap import indent

DEMO_GOAL = (
    'Count the words in "Good morning and welcome to PulseFit", then '
    "tell me what is 12 * 45 + 5, and convert 2.5 km to miles."
)

# ------------------------------------------------------------------
# The three tools
# ------------------------------------------------------------------

_ALLOWED_CHARS = set("0123456789+-*/(). ")

_OPS = {  # ast node type -> the function that computes it
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}

LENGTH_TO_M = {"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0,
               "inch": 0.0254, "ft": 0.3048, "mile": 1609.344}
WEIGHT_TO_G = {"g": 1.0, "kg": 1000.0, "lb": 453.592, "oz": 28.3495}


def _eval_node(node: ast.AST) -> float:
    """Walk the parse tree; allow ONLY numbers, unary minus and + - * /."""
    if isinstance(node, ast.Expression):
        return _eval_node(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_eval_node(node.left), _eval_node(node.right))
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = _eval_node(node.operand)
        return -value if isinstance(node.op, ast.USub) else value
    raise ValueError(f"not allowed in an expression: {type(node).__name__}")


def safe_calculator(expression: str) -> float:
    """Task 3: math without eval -- whitelist, parse, walk."""
    if not isinstance(expression, str):
        raise ValueError("expression must be a string")
    illegal = set(expression) - _ALLOWED_CHARS
    if illegal:
        raise ValueError(f"illegal characters in expression: {''.join(sorted(illegal))!r}")
    try:
        tree = ast.parse(expression, mode="eval")  # PARSE it, never exec it
    except SyntaxError as exc:
        raise ValueError(f"not a valid expression: {exc.msg}") from exc
    return float(_eval_node(tree))


def word_count(text: str) -> int:
    """Task 4: whitespace-separated words."""
    return len(text.split())


def _canonical(unit: str, table: dict[str, float]) -> str | None:
    """Look up a unit name, tolerating a plain English plural (miles -> mile)."""
    unit = unit.strip().lower()
    if unit in table:
        return unit
    if unit.endswith("s") and unit[:-1] in table:
        return unit[:-1]
    return None


def unit_convert(value: float, from_unit: str, to_unit: str) -> float:
    """Task 4: from_unit -> base unit -> to_unit, within one family.

    Users (and LLMs) say "miles" and "feet", not just "mile" and "ft",
    so lookups tolerate plurals. Mixing families (km -> kg) raises.
    """
    for table in (LENGTH_TO_M, WEIGHT_TO_G):
        source = _canonical(from_unit, table)
        target = _canonical(to_unit, table)
        if source and target:
            return value * table[source] / table[target]
    raise ValueError(f"cannot convert {from_unit!r} to {to_unit!r} "
                     f"(length: {sorted(LENGTH_TO_M)}; weight: {sorted(WEIGHT_TO_G)})")


# ------------------------------------------------------------------
# Task 1-2: registry + schemas (the real request shape)
# ------------------------------------------------------------------

TOOL_REGISTRY: dict = {
    "safe_calculator": safe_calculator,
    "word_count": word_count,
    "unit_convert": unit_convert,
}

TOOL_SCHEMAS: list[dict] = [
    {
        "name": "safe_calculator",
        "description": "Evaluate a math expression made of numbers, "
                       "+ - * / and parentheses. No letters allowed.",
        "input_schema": {"type": "object",
                         "properties": {"expression": {"type": "string"}},
                         "required": ["expression"]},
    },
    {
        "name": "word_count",
        "description": "Count the whitespace-separated words in a text.",
        "input_schema": {"type": "object",
                         "properties": {"text": {"type": "string"}},
                         "required": ["text"]},
    },
    {
        "name": "unit_convert",
        "description": "Convert a value between length units (mm cm m km "
                       "inch ft mile) or between weight units (g kg lb oz).",
        "input_schema": {"type": "object",
                         "properties": {"value": {"type": "number"},
                                        "from_unit": {"type": "string"},
                                        "to_unit": {"type": "string"}},
                         "required": ["value", "from_unit", "to_unit"]},
    },
]


# ------------------------------------------------------------------
# Task 5: the defensive executor
# ------------------------------------------------------------------

def execute_tool(name: str, tool_input: dict) -> dict:
    """Run one tool; EVERY failure mode becomes data, never a crash."""
    if name not in TOOL_REGISTRY:
        known = ", ".join(sorted(TOOL_REGISTRY))
        return {"ok": False, "error": f"unknown tool '{name}' (known: {known})"}
    try:
        result = TOOL_REGISTRY[name](**tool_input)
    except TypeError as exc:
        return {"ok": False, "error": f"bad arguments for '{name}': {exc}"}
    except (ValueError, ZeroDivisionError) as exc:
        return {"ok": False, "error": f"'{name}' refused: {exc}"}
    return {"ok": True, "result": result}


# ------------------------------------------------------------------
# Task 6: the policy -- SIMULATED; real shape in the docstring
# ------------------------------------------------------------------

def decide_next_action(goal: str, history: list[dict]) -> dict | None:
    """Return the next tool call {"id", "name", "input"} or None when done.

    IN REAL LIFE (module 18) this whole function is ONE API call:
    you send TOOL_SCHEMAS + the conversation, and the model replies
    with a tool_use content block such as:
        {"type": "tool_use", "id": "toolu_01abc", "name": "safe_calculator",
         "input": {"expression": "12 * 45 + 5"}}
    You run the tool and send back a user message with a tool_result
    block: {"type": "tool_result", "tool_use_id": "toolu_01abc",
    "content": "545", "is_error": false} -- until the model answers
    in plain text instead (stop_reason "end_turn").
    """
    done = {step["name"] for step in history if step["type"] == "tool_use"}
    next_id = f"toolu_{sum(step['type'] == 'tool_use' for step in history) + 1:02d}"

    candidates: list[tuple[int, dict]] = []  # (position in goal, action)

    quoted = re.search(r'"(.+?)"', goal)
    if quoted and "word_count" not in done:
        candidates.append((quoted.start(),
                           {"id": next_id, "name": "word_count",
                            "input": {"text": quoted.group(1)}}))

    math = re.search(r"what is ([\d\s.+\-*/]+)", goal)
    if math and "safe_calculator" not in done:
        candidates.append((math.start(),
                           {"id": next_id, "name": "safe_calculator",
                            "input": {"expression": math.group(1).strip()}}))

    convert = re.search(r"convert\s+([\d.]+)\s*([a-z]+)\s+(?:to|in)\s+([a-z]+)",
                        goal, re.IGNORECASE)
    if convert and "unit_convert" not in done:
        candidates.append((convert.start(),
                           {"id": next_id, "name": "unit_convert",
                            "input": {"value": float(convert.group(1)),
                                      "from_unit": convert.group(2),
                                      "to_unit": convert.group(3)}}))

    if not candidates:
        return None
    candidates.sort(key=lambda pair: pair[0])  # earliest mention first
    return candidates[0][1]


def compose_final_answer(goal: str, history: list[dict]) -> str:
    """Also simulated: in real life the model writes this sentence."""
    parts = []
    for step in history:
        if step["type"] != "tool_result":
            continue
        outcome = step["result"]
        if outcome.get("ok"):
            value = outcome["result"]
            if isinstance(value, float):
                value = f"{value:.4g}"
            parts.append(f"{step['name']} -> {value}")
        else:
            parts.append(f"{step['name']} FAILED ({outcome['error']})")
    return "Final answer: " + "; ".join(parts) + "."


# ------------------------------------------------------------------
# Task 7: the loop
# ------------------------------------------------------------------

def run_agent(goal: str, max_steps: int = 6) -> str:
    """decide -> execute -> observe, with a visible trace and a leash."""
    print(f"\nGOAL: {goal}")
    history: list[dict] = []
    for step_number in range(1, max_steps + 1):
        action = decide_next_action(goal, history)
        if action is None:
            print(f"\n[step {step_number}] policy: goal satisfied -> stop")
            return compose_final_answer(goal, history)
        print(f"\n[step {step_number}] tool_use : id={action['id']} "
              f"{action['name']} {action['input']}")
        outcome = execute_tool(action["name"], action["input"])
        print(f"[step {step_number}] result   : {outcome}")
        # Real life: append these two messages, then call the model again --
        #   {"role": "assistant", "content": [<the tool_use block>]}
        #   {"role": "user", "content": [{"type": "tool_result",
        #       "tool_use_id": action["id"], "content": str(outcome)}]}
        history.append({"type": "tool_use", **action})
        history.append({"type": "tool_result", "name": action["name"],
                        "result": outcome})
    print(f"\n[max_steps] {max_steps} steps reached -- stopping anyway")
    return "Gave up: max_steps reached (agents need leashes)."


def main() -> None:
    print("MINI AGENT WITH TOOLS -- solution")

    print("\nPart 1: tool registry")
    for name, function in TOOL_REGISTRY.items():
        print(f"  {name:<16} -> {function.__name__}()")

    print("\nPart 2: tool schemas (what a real tool-use request sends)")
    print(indent(json.dumps(TOOL_SCHEMAS, indent=2), "  "))

    print("\nPart 3: the executor survives bad calls")
    abuse = [
        ("fly_to_moon", {}),
        ("word_count", {"words": 3}),
        ("safe_calculator", {"expression": "5 / 0"}),
        ("safe_calculator", {"expression": "__import__('os').listdir()"}),
        ("unit_convert", {"value": 2.5, "from_unit": "km", "to_unit": "kg"}),
    ]
    for name, tool_input in abuse:
        outcome = execute_tool(name, tool_input)
        print(f"  {name}({tool_input}) ->\n    {outcome}")

    print("\nPart 4: the full agent run")
    final = run_agent(DEMO_GOAL)
    print(f"\n{final}")

    print("\nPolicy, executor, history, leash: that is every agent ever.")
    print("Swap the if-rules for a real LLM with TOOL_SCHEMAS attached,")
    print("and this same loop runs for real.")


if __name__ == "__main__":
    main()
