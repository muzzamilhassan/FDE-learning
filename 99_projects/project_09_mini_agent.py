"""
=====================================================================
PROJECT: Mini Agent with Tools  (Difficulty: advanced)
=====================================================================

SCENARIO
--------
PulseFit support wants a little agent that can actually DO things:
check the math in a customer's invoice question, count words in a
canned message, convert units for international users. You will build
the classic agent loop by hand: a POLICY decides the next tool call,
an EXECUTOR runs it safely, the result feeds back in, and the loop
stops when the goal is answered -- or when max_steps cuts it off.
The policy here is SIMULATED with if-rules so everything runs
offline; comments mark exactly where a real LLM tool-use call sits.

WHAT YOU WILL PRACTICE
----------------------
- A tool registry: dict mapping name -> function (modules 02/04)
- Tool schemas: the JSON descriptions an LLM reads (from module 18)
- A defensive executor: unknown tool, bad args, tool errors (module 06)
- The agent loop: decide -> act -> observe -> repeat (from module 18)
- max_steps: every agent needs a leash (from module 18)
- Validating input and evaluating math WITHOUT eval() (module 06)

YOUR TASKS
----------
1. Fill TOOL_REGISTRY: name -> function for the three tools below.
2. Fill TOOL_SCHEMAS: one dict per tool (name, description,
   input_schema) -- compare with the real API shape in the comment.
3. safe_calculator(expression): whitelist the characters, then walk
   the ast (hint below) to compute the result. No eval(). Ever.
4. word_count(text) and unit_convert(value, from_unit, to_unit):
   small, honest functions that raise ValueError on nonsense.
5. execute_tool(name, tool_input): registry lookup + try/except -- a
   bad call becomes {"ok": False, "error": ...}, never a crash.
6. decide_next_action(goal, history): the SIMULATED policy. Rules read
   the goal AND what has already been done, then return
   {"id", "name", "input"} -- or None when nothing is left to do.
7. run_agent(goal, max_steps=6): the loop with a step-by-step trace.
8. main(): run the 3-tool demo goal, then feed the executor an
   unknown tool, wrong arguments, 5 / 0 and sneaky code.

STARTER CODE
------------
Complete the TODOs below. Run with:
    python 99_projects/project_09_mini_agent.py

100% offline and keyless; the only "intelligence" here is if-rules.
Hints are inline. A full solution is in answers/projects/.
=====================================================================
"""

from __future__ import annotations

import ast        # task 3: parsing expressions safely
import json       # main: pretty-printing the schemas
import operator   # task 3: the math behind + - * /
import re         # task 6: the simulated policy reads the goal

DEMO_GOAL = (
    'Count the words in "Good morning and welcome to PulseFit", then '
    "tell me what is 12 * 45 + 5, and convert 2.5 km to miles."
)

# ------------------------------------------------------------------
# Tasks 1-2: the registry and the schemas
# ------------------------------------------------------------------

TOOL_REGISTRY: dict = {
    # TODO 1: "safe_calculator": safe_calculator, ... (the 3 tools)
}

TOOL_SCHEMAS: list[dict] = [
    # TODO 2: describe each tool. A REAL tool-use request (module 18)
    # sends exactly this shape for every tool the model may call:
    #   {"name": "safe_calculator",
    #    "description": "what the tool is for, in one honest sentence",
    #    "input_schema": {"type": "object",
    #                     "properties": {"expression": {"type": "string"}},
    #                     "required": ["expression"]}}
    # (one such dict per tool: safe_calculator, word_count, unit_convert)
]

# ------------------------------------------------------------------
# Tasks 3-4: the three tools
# ------------------------------------------------------------------

_ALLOWED_CHARS = set("0123456789+-*/(). ")

_OPS = {  # ast node type -> the function that computes it
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


def _eval_node(node: ast.AST) -> float:
    """TODO 3 helper: walk the expression tree; allow ONLY numbers, + - * /.

    - ast.Expression      -> recurse into .body
    - ast.Constant (int/float) -> return the value
    - ast.BinOp whose .op is in _OPS ->
          _OPS[type(node.op)](_eval_node(node.left), _eval_node(node.right))
    - anything else -> raise ValueError("expression not allowed")
    """
    print("TODO: implement _eval_node()")
    raise ValueError("safe_calculator not implemented yet")


def safe_calculator(expression: str) -> float:
    """TODO 3: evaluate + - * / ( ) math WITHOUT eval().

    1. if set(expression) - _ALLOWED_CHARS: raise ValueError
       (letters, quotes, underscores -> someone is trying to smuggle code)
    2. tree = ast.parse(expression, mode="eval")
    3. return float(_eval_node(tree))
    Division by zero may raise -- the executor catches it (task 5).
    """
    print("TODO: implement safe_calculator()")
    raise ValueError("safe_calculator not implemented yet")


def word_count(text: str) -> int:
    """TODO 4: number of whitespace-separated words (len(text.split()))."""
    print("TODO: implement word_count()")
    return 0


LENGTH_TO_M = {"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0,
               "inch": 0.0254, "ft": 0.3048, "mile": 1609.344}
WEIGHT_TO_G = {"g": 1.0, "kg": 1000.0, "lb": 453.592, "oz": 28.3495}


def unit_convert(value: float, from_unit: str, to_unit: str) -> float:
    """TODO 4: convert within length OR within weight units.

    Pattern: convert from_unit -> base unit -> to_unit.
    Example: value * LENGTH_TO_M[from_unit] / LENGTH_TO_M[to_unit]
    If the two units are not in the same family, raise ValueError.
    """
    print("TODO: implement unit_convert()")
    raise ValueError("unit_convert not implemented yet")


# ------------------------------------------------------------------
# Task 5: the executor
# ------------------------------------------------------------------

def execute_tool(name: str, tool_input: dict) -> dict:
    """TODO 5: run TOOL_REGISTRY[name](**tool_input), defensively.

    - unknown name -> {"ok": False, "error": ...} (list the known tools)
    - TypeError -> bad arguments; ValueError/ZeroDivisionError -> the
      tool refused; both become error dicts, never a crash
    - success -> {"ok": True, "result": result}
    """
    print("TODO: implement execute_tool()")
    return {"ok": False, "error": "executor not implemented yet"}


# ------------------------------------------------------------------
# Task 6: the policy (simulated)
# ------------------------------------------------------------------

def decide_next_action(goal: str, history: list[dict]) -> dict | None:
    """TODO 6: the SIMULATED policy -- return the next tool call or None.

    IN REAL LIFE (module 18) this whole function is ONE API call with
    TOOL_SCHEMAS attached; the model answers with a tool_use block:

        response = client.messages.create(
            model="claude-opus-5-5",
            max_tokens=1024,
            tools=TOOL_SCHEMAS,   # <- the schemas you wrote in task 2
            messages=messages,    # goal + tool_use turns + tool_results
        )
        if response.stop_reason != "tool_use":
            return None           # model answered in words: we are done
        block = next(b for b in response.content if b.type == "tool_use")
        return {"id": block.id, "name": block.name, "input": block.input}
        # the block looks like:
        # {"type": "tool_use", "id": "toolu_01abc", "name": "safe_calculator",
        #  "input": {"expression": "12 * 45 + 5"}}

    The simulated version: a small rule table. Regex the goal (a
    quoted text, "what is <math>", "convert <x> <unit> to <unit>"),
    skip rules whose tool already ran (check history), pick the match
    appearing FIRST in the goal. No rule fires -> None.
    """
    print("TODO: implement decide_next_action()")
    return None


def compose_final_answer(goal: str, history: list[dict]) -> str:
    """TODO 6b (helper): turn the collected tool results into one reply.

    In real life the model writes this sentence itself. Here: one line
    per finished step, e.g. "word_count -> 6; safe_calculator -> 545".
    """
    print("TODO: implement compose_final_answer()")
    return "TODO: implement compose_final_answer()"


# ------------------------------------------------------------------
# Task 7: the loop
# ------------------------------------------------------------------

def run_agent(goal: str, max_steps: int = 6) -> str:
    """TODO 7: decide -> execute -> observe, with a visible trace.

    For step in 1..max_steps:
      action = decide_next_action(goal, history)
      if action is None: return compose_final_answer(goal, history)
      print the tool_use (name + id + input), run execute_tool,
      print the result, append BOTH events to history.
      IN REAL LIFE you would append two messages:
        {"role": "assistant", "content": [the tool_use block]}
        {"role": "user", "content": [{"type": "tool_result",
             "tool_use_id": action["id"], "content": <result string>}]}
    If max_steps is reached: return a "gave up" string. Agents need leashes.
    """
    print("TODO: implement run_agent()")
    return "TODO: implement run_agent() to see the trace."


def main() -> None:
    print("=" * 58)
    print("  MINI AGENT WITH TOOLS -- starter")
    print("  A policy, an executor, and a loop with a leash.")
    print("=" * 58)

    print("\nPart 1: tool registry")
    print(f"  registered: {sorted(TOOL_REGISTRY) or '(TODO 1: none yet)'}")

    print("\nPart 2: tool schemas (what a real LLM would read)")
    if TOOL_SCHEMAS:
        print(indent(json.dumps(TOOL_SCHEMAS, indent=2), "  "))
    else:
        print("  (TODO 2: none yet)")

    print("\nPart 3: executor survives bad calls")
    print(f"  unknown tool -> {execute_tool('fly_to_moon', {})}")

    print("\nPart 4: the full agent run")
    print(f"  goal: {DEMO_GOAL}")
    if TOOL_REGISTRY and TOOL_SCHEMAS:
        print(run_agent(DEMO_GOAL))
    else:
        print("  (implement tasks 1-7, then this prints the step-by-step trace)")

    print("\nYou built an agent loop. Now go break it (safely).")


if __name__ == "__main__":
    main()
