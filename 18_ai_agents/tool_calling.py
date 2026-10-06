"""
=====================================================================
TOPIC: Tool Calling - Giving a Language Model Hands
=====================================================================

SCENARIO
--------
You ask your assistant "What is the weather in Paris?" and it
confidently invents a forecast -- it only predicts plausible text.
A TOOL is a real Python function the model may ASK you to run: the
model never executes code, it sends a structured request, you run
your trusted function, and pass the result back for the final answer.

TOPIC
-----
- A tool = name + description + input_schema (JSON Schema for the
  arguments the model may supply).
- One request, two outcomes: text (done) OR a tool_use block
  {"type": "tool_use", "id", "name", "input"} and stop_reason
  "tool_use" -- run it, send back a tool_result, call again.
- Gotcha: the model can hallucinate a tool name or argument --
  validate both against your registry before executing anything.
- Only run locally trusted functions; never eval() model text.

QUESTIONS
---------
Q1. Predict: on the FIRST model call for the Paris question, what
    stop_reason and content come back?
Q2. Spot the bug: an executor that just runs FUNCTIONS[name](**args)
    -- name two ways the model can break it.
Q3. Write code: add a word_count(text) tool (function + schema).

Run: python 18_ai_agents/tool_calling.py
Answers: answers/18_ai_agents.py
=====================================================================
"""

import json

# OFFLINE + KEYLESS: the "model" below is a rule-based SIMULATION
# returning plain dicts shaped exactly like the real anthropic
# response -- the calling code here is what you write against the
# real SDK, so swapping in a real client is the only change.

# ------------------------------------------------------------------
# 1) The REAL functions - trusted, local, offline. The model never
#    sees this code, only the results.
# ------------------------------------------------------------------
def get_weather(city: str) -> dict:
    # FAKE table keeps the lesson offline; a real tool might call a
    # weather API - the model still only ever sees the returned value.
    fake = {"Paris": "Overcast, 18C, light rain", "Tokyo": "Sunny, 26C"}
    return {"city": city, "report": fake.get(city.title(), "Clear, 21C")}


def calculator(a: float, b: float, operation: str) -> dict:
    # Raises on bad input on purpose - execute_tool turns that into
    # an error observation instead of a crash.
    if operation == "add":
        return {"result": a + b}
    if operation == "mul":
        return {"result": a * b}
    raise ValueError(f"calculator cannot do {operation!r}")


FUNCTIONS = {"get_weather": get_weather, "calculator": calculator}

# ------------------------------------------------------------------
# 2) The tool SCHEMAS - what we TELL the model about each function.
#    This is the exact "tools" shape the anthropic SDK expects.
# ------------------------------------------------------------------
TOOL_SCHEMAS = [
    {"name": "get_weather", "description": "Weather report for one city.",
     "input_schema": {"type": "object",
                      "properties": {"city": {"type": "string"}},
                      "required": ["city"]}},
    {"name": "calculator", "description": "Add or multiply two numbers.",
     "input_schema": {"type": "object",
                      "properties": {"a": {"type": "number"},
                                     "b": {"type": "number"},
                                     "operation": {"type": "string",
                                                   "enum": ["add", "mul"]}},
                      "required": ["a", "b", "operation"]}},
]


def execute_tool(name: str, args: dict) -> tuple:
    """Validate, then run. Returns (result, is_error) - is_error is
    the same flag a real tool_result carries when a call fails."""
    if name not in FUNCTIONS:                  # hallucinated tool name
        return f"Error: no tool named {name!r}", True
    schema = next(t for t in TOOL_SCHEMAS if t["name"] == name)["input_schema"]
    missing = [k for k in schema["required"] if k not in args]
    unknown = [k for k in args if k not in schema["properties"]]
    if missing or unknown:                     # hallucinated arguments
        return f"Error: missing={missing} unexpected={unknown}", True
    try:
        return FUNCTIONS[name](**args), False  # the REAL work happens
    except Exception as exc:                   # on trusted code only
        return f"Error: {exc}", True

# ------------------------------------------------------------------
# THE REAL FLOW - the SIMULATION below mirrors these SDK shapes 1:1.
# With `pip install anthropic` and ANTHROPIC_API_KEY set:
#   response = client.messages.create(model="claude-opus-5-5",
#       max_tokens=16000, tools=TOOL_SCHEMAS, messages=messages)
#   if response.stop_reason == "tool_use":
#       block = next(b for b in response.content if b.type == "tool_use")
#       # block.id "toolu_01ABC..." | block.name | block.input (dict)
#       result, is_error = execute_tool(block.name, block.input)
#       messages.append({"role": "assistant", "content": response.content})
#       messages.append({"role": "user", "content": [{
#           "type": "tool_result", "tool_use_id": block.id,  # ids match
#           "content": json.dumps(result),
#           **({"is_error": True} if is_error else {})}]})
#       response = client.messages.create(..., messages=messages)  # round 2
class SimulatedModel:
    """SIMULATION of the API: rule-based, offline, keyless. Returns
    dicts with the SAME keys as the real response (stop_reason and
    content blocks), so the demo reads like real client code."""

    def create(self, messages: list, tools: list) -> dict:
        last = messages[-1]["content"]
        if isinstance(last, list):             # a tool_result came back
            data = json.loads(last[0]["content"])
            text = f"The weather in {data['city']} is: {data['report']}."
            return {"stop_reason": "end_turn",
                    "content": [{"type": "text", "text": text}]}
        if "weather" in str(last).lower():     # silly-simple decision rule
            return {"stop_reason": "tool_use",
                    "content": [{"type": "tool_use", "id": "toolu_001",
                                 "name": "get_weather",
                                 "input": {"city": "Paris"}}]}
        return {"stop_reason": "end_turn",
                "content": [{"type": "text",
                             "text": "No tool needed for that."}]}

# ------------------------------------------------------------------
# 3) One full tool-call cycle - watch each protocol step happen.
# ------------------------------------------------------------------
model = SimulatedModel()
messages = [{"role": "user", "content": "What is the weather in Paris?"}]

print("user    :", messages[0]["content"])
response = model.create(messages, TOOL_SCHEMAS)          # round trip 1
print("model   :", response["stop_reason"], response["content"])
block = next(b for b in response["content"] if b["type"] == "tool_use")
messages.append({"role": "assistant", "content": response["content"]})
result, is_error = execute_tool(block["name"], block["input"])   # REAL code
print("executor:", f"{block['name']}({block['input']}) ->", result)
messages.append({"role": "user", "content": [
    {"type": "tool_result", "tool_use_id": block["id"],
     "content": json.dumps(result),
     **({"is_error": True} if is_error else {})},
]})
response = model.create(messages, TOOL_SCHEMAS)          # round trip 2
print("model   :", response["stop_reason"])
print("answer  :", response["content"][0]["text"])

# Gotchas in action: the model can invent a tool name or an argument.
print("gotcha  : unknown tool ->", execute_tool("delete_everything", {}))
print("gotcha  : invented arg  ->",
      execute_tool("get_weather", {"city": "Paris", "unit": "kelvin"}))

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/18_ai_agents.py
# ------------------------------------------------------------------
# Q1: Predict the output - on the FIRST model.create() call for the
#     Paris question, what are response["stop_reason"] and the
#     tool_use block's "name" and "input"?
#
# Q2: Spot the bug - an executor written as
#         result = FUNCTIONS[name](**args)
#     with no other checks. Name two distinct failure modes when the
#     model hallucinates, and the fix used in this file.
#
# Q3: Write code - add a word_count tool (function returning
#     {"words": len(text.split())} + a TOOL_SCHEMAS entry), then
#     print execute_tool("word_count", {"text": "agents use tools
#     in loops"}) and say what comes back.
