"""
=====================================================================
TOPIC: The Agent Loop - LLM + Tools + a While Loop
=====================================================================

SCENARIO
--------
One tool call answered the weather question. But "How many words
are in the weather report for Paris, and what is 17 * 23?" needs a
CHAIN: fetch the weather, count the words in that report, then
multiply. An AGENT is just a loop: offer tools, run whatever the
model asks for, feed the results back, repeat until the model
answers in plain text. That loop is the whole secret of agents.

TOPIC
-----
- while steps < max_steps: ask the model -> a tool_use request means
  run it, append the tool_result, continue; a text answer means stop.
- Guard rails: max_steps (a stuck model must not loop forever), an
  allowlist of tools you will run, one log line per step.
- Gotcha: a tool error is an OBSERVATION - return it to the model
  with is_error=True; never let an exception kill the whole agent.
- Model-supplied args still need validation (see tool_calling.py).

QUESTIONS
---------
Q1. Predict the trace: how many tool calls does the demo goal need
    before the final text answer, and in what order?
Q2. Spot the bug: calling the tool function bare inside the loop --
    what happens when a tool raises ValueError?
Q3. Write code: a build_tool_result(tool_use_id, content,
    is_error=False) helper returning the exact user-message dict.

Run: python 18_ai_agents/agent_loop.py
Answers: answers/18_ai_agents.py
=====================================================================
"""

import json

# OFFLINE + KEYLESS: SimulatedAgentModel is a rule-based SIMULATION
# returning the same dict shapes as the real anthropic response. The
# loop code is what you keep when you swap in a real client.

# ------------------------------------------------------------------
# 1) The TOOLS - trusted local functions the agent may run.
# ------------------------------------------------------------------
def get_weather(city: str) -> dict:
    # FAKE data keeps us offline; this report text is what the goal
    # asks the agent to count the words of.
    return {"city": city, "report": "Overcast, 18C, light rain in Paris"}


def word_count(text: str) -> dict:
    return {"words": len(text.split())}


def calculator(a: float, b: float, operation: str) -> dict:
    # match on the operation string - a natural fit from lesson 03.
    match operation:
        case "mul":
            return {"result": a * b}
        case "div" if b != 0:
            return {"result": a / b}
        case _:
            raise ValueError(f"calculator cannot do {operation!r} here")


FUNCTIONS = {"get_weather": get_weather, "word_count": word_count,
             "calculator": calculator}
ALLOWED = set(FUNCTIONS)            # guard rail: the tool allowlist

TOOL_SCHEMAS = [
    {"name": "get_weather", "description": "Weather report for one city.",
     "input_schema": {"type": "object",
                      "properties": {"city": {"type": "string"}},
                      "required": ["city"]}},
    {"name": "word_count", "description": "Count the words in a text.",
     "input_schema": {"type": "object",
                      "properties": {"text": {"type": "string"}},
                      "required": ["text"]}},
    {"name": "calculator", "description": "Multiply or divide two numbers.",
     "input_schema": {"type": "object",
                      "properties": {"a": {"type": "number"},
                                     "b": {"type": "number"},
                                     "operation": {"type": "string",
                                                   "enum": ["mul", "div"]}},
                      "required": ["a", "b", "operation"]}},
]


def execute_tool(name: str, args: dict) -> tuple:
    """Check the allowlist, then run. ANY failure comes back as an
    error observation - one bad call must never crash the loop, it
    is just news for the model to react to."""
    if name not in ALLOWED:                 # never execute unknown tools
        return f"Error: tool {name!r} is not allowlisted", True
    try:                                    # also catches bad/hallucinated args
        return FUNCTIONS[name](**args), False
    except Exception as exc:
        return f"Error: {exc}", True

# ------------------------------------------------------------------
# THE REAL LOOP (comment only) - identical structure, real SDK:
#   while True:
#       response = client.messages.create(model="claude-opus-5-5",
#           max_tokens=16000, tools=TOOL_SCHEMAS, messages=messages)
#       if response.stop_reason != "tool_use":
#           break                              # final text answer
#       block = next(b for b in response.content if b.type == "tool_use")
#       messages.append({"role": "assistant", "content": response.content})
#       result, is_error = execute_tool(block.name, block.input)
#       messages.append({"role": "user", "content": [{
#           "type": "tool_result", "tool_use_id": block.id,
#           "content": result,
#           **({"is_error": True} if is_error else {})}]})
#   # max_steps + the allowlist are YOUR guard rails: the API itself
#   # happily keeps looping if the model re-calls the same tool.
class SimulatedAgentModel:
    """SIMULATION: a rule-based planner that decides its next step by
    reading the conversation, like a real model. It chains
    get_weather -> word_count -> calculator, then answers in text."""

    def create(self, messages: list, tools: list) -> dict:
        done = self._results(messages)      # which tools already ran?
        if "get_weather" not in done:
            return self._wants("get_weather", {"city": "Paris"})
        if "word_count" not in done:
            report = done["get_weather"]["report"]   # read the result
            return self._wants("word_count", {"text": report})
        if "calculator" not in done:
            return self._wants("calculator",
                               {"a": 17, "b": 23, "operation": "mul"})
        n, product = done["word_count"]["words"], done["calculator"]["result"]
        text = f"The Paris weather report has {n} words, and 17 * 23 = {product}."
        return {"stop_reason": "end_turn",
                "content": [{"type": "text", "text": text}]}

    @staticmethod
    def _wants(name: str, tool_input: dict) -> dict:
        return {"stop_reason": "tool_use",
                "content": [{"type": "tool_use", "id": f"toolu_{name}",
                             "name": name, "input": tool_input}]}

    @staticmethod
    def _results(messages: list) -> dict:
        """Replay the protocol: pair each tool_result with the
        tool_use that requested it, matched by id."""
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
# 2) The AGENT LOOP - tools + history + a budget + logging.
# ------------------------------------------------------------------
def run_agent(goal: str, model, max_steps: int = 8) -> str:
    """Ask -> (tool_use? execute + feed back) -> repeat -> final text."""
    messages = [{"role": "user", "content": goal}]
    for step in range(1, max_steps + 1):
        print(f"--- step {step} " + "-" * 44)
        response = model.create(messages, TOOL_SCHEMAS)
        block = response["content"][0]
        if response["stop_reason"] != "tool_use":    # model is done
            print("model   :", block["text"])
            return block["text"]
        print(f"model   : tool_use -> {block['name']}({block['input']})")
        result, is_error = execute_tool(block["name"], block["input"])
        note = "   [error observation]" if is_error else ""
        print(f"result  : {result}{note}")
        messages.append({"role": "assistant", "content": response["content"]})
        messages.append({"role": "user", "content": [
            {"type": "tool_result", "tool_use_id": block["id"],
             "content": json.dumps(result),
             **({"is_error": True} if is_error else {})},
        ]})
    print(f"--- guard: hit max_steps={max_steps}, stopping safely")
    return f"Gave up after {max_steps} steps."


GOAL = ("How many words are in the weather report for Paris, "
        "and what is 17 * 23?")

print("GOAL:", GOAL, "\n")
answer = run_agent(GOAL, SimulatedAgentModel())
print("\nfinal answer:", answer)

# Guard-rail demo: the plan needs 4 model calls (3 tools + the final
# text). With max_steps=2 the budget fires instead of hanging forever.
print("\nSame goal, max_steps=2 -- watch the guard rail fire:")
print("  ->", run_agent(GOAL, SimulatedAgentModel(), max_steps=2))

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/18_ai_agents.py
# ------------------------------------------------------------------
# Q1: Predict the trace - how many tool calls does the demo goal need
#     before the final text answer, in what order, and what stops the
#     model from calling get_weather forever?
#
# Q2: Spot the bug - inside the loop someone wrote
#         result = FUNCTIONS[name](**args)
#     with no try/except. A tool raises ValueError. What happens to
#     the agent, and what should happen instead?
#
# Q3: Write code - build_tool_result(tool_use_id, content,
#     is_error=False) returning the exact user-message dict the
#     protocol expects, then print it for toolu_word_count /
#     '{"words": 5}'.
