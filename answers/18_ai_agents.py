"""
Answers for 18_ai_agents - try the questions first!

Each answer is a one-line why plus working code you can run.
Everything is offline and keyless: the "model" is a rule-based
SIMULATION returning the same dict shapes as the real anthropic API.
Run: python answers/18_ai_agents.py
"""

import json

# ------------------------------------------------------------------
# Shared offline simulation helpers (same shapes as the real SDK)
# ------------------------------------------------------------------
def get_weather(city):
    return {"city": city, "report": "Overcast, 18C, light rain in Paris"}


def word_count(text):
    return {"words": len(text.split())}


def calculator(a, b, operation):
    match operation:
        case "mul":
            return {"result": a * b}
        case "div" if b != 0:
            return {"result": a / b}
        case _:
            raise ValueError(f"calculator cannot do {operation!r} (or / by 0)")


FUNCTIONS = {"get_weather": get_weather, "word_count": word_count,
             "calculator": calculator}


def execute_tool(name, args):
    """Allowlist + try/except: failures become (error, True) notes,
    never crashes."""
    if name not in FUNCTIONS:
        return f"Error: no tool named {name!r}", True
    try:
        return FUNCTIONS[name](**args), False
    except Exception as exc:
        return f"Error: {exc}", True


class ChainModel:
    """SIMULATION planner: reads the conversation like a real model,
    chaining get_weather -> word_count -> calculator."""

    def create(self, messages, tools=None):
        done = self._results(messages)
        if "get_weather" not in done:
            return self._wants("get_weather", {"city": "Paris"})
        if "word_count" not in done:
            return self._wants("word_count",
                               {"text": done["get_weather"]["report"]})
        if "calculator" not in done:
            return self._wants("calculator",
                               {"a": 17, "b": 23, "operation": "mul"})
        n = done["word_count"]["words"]
        product = done["calculator"]["result"]
        return {"stop_reason": "end_turn",
                "content": [{"type": "text",
                             "text": f"The Paris weather report has {n} "
                                     f"words, and 17 * 23 = {product}."}]}

    @staticmethod
    def _wants(name, tool_input):
        return {"stop_reason": "tool_use",
                "content": [{"type": "tool_use", "id": f"toolu_{name}",
                             "name": name, "input": tool_input}]}

    @staticmethod
    def _results(messages):
        asked, results = {}, {}
        for msg in messages:
            blocks = msg["content"] if isinstance(msg["content"], list) else []
            for b in blocks:
                if b["type"] == "tool_use":
                    asked[b["id"]] = b["name"]
                elif b["type"] == "tool_result":
                    results[asked.get(b["tool_use_id"], "?")] = \
                        json.loads(b["content"])
        return results


# ------------------------------------------------------------------
# tool_calling.py
# ------------------------------------------------------------------

# Q1: stop_reason is "tool_use" and content holds ONE block:
#     {"type": "tool_use", "id": "toolu_001", "name": "get_weather",
#      "input": {"city": "Paris"}}.
# Why: the model has no weather data, so guessing text would be a
# hallucination - instead it requests a run of your real function.
first = ChainModel().create(
    [{"role": "user", "content": "What is the weather in Paris?"}])
print("Q1:", first["stop_reason"], first["content"][0])


# Q2: Two failure modes of a bare FUNCTIONS[name](**args):
#     (1) hallucinated tool name -> KeyError crash (or worse, running
#     something you never intended); (2) hallucinated argument ->
#     TypeError: unexpected keyword argument. Fix: allowlist the name,
#     check args against input_schema, wrap execution so failures
#     return (error, is_error=True).
print("\nQ2:")
if "delete_files" in FUNCTIONS:            # the allowlist guard
    FUNCTIONS["delete_files"]()
else:
    print("  blocked: no tool named 'delete_files'")
try:
    FUNCTIONS["get_weather"](**{"city": "Paris", "unit": "kelvin"})
except TypeError as exc:                   # what the unvalidated call does
    print("  bare call:", exc)
print("  validated:", execute_tool("get_weather", {"city": "Paris"}))


# Q3: word_count is just another tool - function + schema entry, run
# by the same validated executor. Output: ({'words': 5}, False).
def word_count_tool(text):
    return {"words": len(text.split())}


WORD_COUNT_SCHEMA = {"name": "word_count",
                     "description": "Count the words in a text.",
                     "input_schema": {"type": "object",
                                      "properties": {"text": {"type": "string"}},
                                      "required": ["text"]}}
FUNCTIONS["word_count"] = word_count_tool
print("\nQ3:", execute_tool("word_count",
                            {"text": "agents use tools in loops"}))


# ------------------------------------------------------------------
# agent_loop.py
# ------------------------------------------------------------------

# Q1: THREE tool calls, in this order: get_weather -> word_count ->
#     calculator, then a text final answer (4 model calls total).
#     Nothing stops a real model from re-calling a tool forever -
#     YOUR max_steps budget does, returning "Gave up..." instead.
def run_agent(model, goal, max_steps=8):
    messages = [{"role": "user", "content": goal}]
    for step in range(1, max_steps + 1):
        response = model.create(messages)
        block = response["content"][0]
        if response["stop_reason"] != "tool_use":
            return block["text"]
        result, is_error = execute_tool(block["name"], block["input"])
        print(f"  step {step}: {block['name']}({block['input']}) -> {result}")
        messages.append({"role": "assistant", "content": response["content"]})
        messages.append({"role": "user", "content": [{
            "type": "tool_result", "tool_use_id": block["id"],
            "content": json.dumps(result),
            **({"is_error": True} if is_error else {})}]})
    return f"Gave up after {max_steps} steps."


print("\nQ1 trace:")
goal = ("How many words are in the weather report for Paris, "
        "and what is 17 * 23?")
print(" ", run_agent(ChainModel(), goal))


# Q2: The bare call raises out of run_agent - the exception kills the
#     WHOLE agent and the model never learns why the tool failed.
#     Instead, catch it in the executor and feed the error back as an
#     is_error tool_result, so the model can change course.
print("\nQ2:")
try:
    FUNCTIONS["calculator"](**{"a": 1, "b": 0, "operation": "div"})
except ValueError as exc:
    print("  bare call raises ->", exc)
print("  as observation ->",
      execute_tool("calculator", {"a": 1, "b": 0, "operation": "div"}))


# Q3: build_tool_result assembles the exact user message the protocol
#     expects - tool_use_id is the link that routes your answer back
#     to the model's request; is_error only appears when set.
def build_tool_result(tool_use_id, content, is_error=False):
    block = {"type": "tool_result", "tool_use_id": tool_use_id,
             "content": content}
    if is_error:
        block["is_error"] = True
    return {"role": "user", "content": [block]}


print("\nQ3:", build_tool_result("toolu_word_count", '{"words": 5}'))
print("   error case:",
      build_tool_result("toolu_calculator", "Error: cannot divide by 0",
                        is_error=True))
