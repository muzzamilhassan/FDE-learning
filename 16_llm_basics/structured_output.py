"""
=====================================================================
TOPIC: Structured Output (Getting JSON Back)
=====================================================================

SCENARIO
--------
Your catalog app reads product reviews and fills a database: name,
price, category. Free text is useless to a database -- you need JSON
you can parse, validate, and retry when the model misbehaves.

TOPIC
-----
Ask in the prompt: "Respond ONLY with JSON with exactly these keys".
Parse with json.loads -- and ALWAYS wrap it in try/except
json.JSONDecodeError: models sometimes wrap JSON in prose or markdown
fences, which will not parse.
Validate the fields you need BEFORE using them: json.loads happily
parses JSON whose keys are not the ones you asked for, and the
KeyError then explodes far away from the real cause.
On failure, retry with a repaired prompt -- tell the model what went
wrong and repeat the format rules. Two or three attempts, then give
up cleanly (default value or error), never an infinite loop.

QUESTIONS
---------
Q1. Predict: json.loads('Here you go: {"a": 1}') -- what happens?
Q2. Spot the bug: data = json.loads(text) then data["price"] with no
    check that the model used your key names.
Q3. Write code: extract_product(review_text) -> dict or None, using
    an ONLY-JSON prompt, safe parsing, and required-key validation.
Q4. Concept: why append a repair note to the prompt instead of
    resending the exact same prompt?

Run: python 16_llm_basics/structured_output.py
Answers: answers/16_llm_basics.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------
import json
from types import SimpleNamespace

GOOD_JSON = '{"name": "Aurora Desk Lamp", "price": 42.50, "category": "home"}'
BAD_JSON = ('Sure! Here is the JSON you asked for:\n'
            '```json\n{"name": "Aurora Desk Lamp", "price": 42.50}\n```')

# SIMULATION - stand-in for the real API. Same call/response shape as
# the anthropic SDK, no network, no key -- every flow below runs.
def _response(text, in_tokens, out_tokens):
    """Shaped like the real Message: block list, usage, stop_reason."""
    block = SimpleNamespace(type="text", text=text)
    usage = SimpleNamespace(input_tokens=in_tokens, output_tokens=out_tokens)
    return SimpleNamespace(content=[block], usage=usage,
                           stop_reason="end_turn", model="claude-sonnet-5-5")


def _reply(model, max_tokens, system, messages):
    """Canned 'model': sloppy on a vague prompt, clean on a strict one."""
    prompt = messages[-1]["content"]
    if "ONLY with JSON" in prompt or "not valid JSON" in prompt:
        return _response(GOOD_JSON, len(prompt) // 4, 13)
    return _response(BAD_JSON, len(prompt) // 4, 16)  # JSON wrapped in chat


class SimulatedAnthropic:
    """SIMULATION - stands in for anthropic.Anthropic()."""
    class messages:  # so client.messages.create(...) works like the SDK
        @staticmethod
        def create(model, max_tokens, system=None, messages=None):
            return _reply(model, max_tokens, system, messages)


MODEL = "claude-sonnet-5-5"
client = SimulatedAnthropic()
REQUIRED = ("name", "price", "category")
review = ("I bought the Aurora Desk Lamp for 42.50 dollars. "
          "Warm light, tiny scratch on the base.")


def ask_json(prompt, max_attempts=3, sabotage_first=False):
    """Call -> parse -> validate -> retry with a repaired prompt."""
    for attempt in range(1, max_attempts + 1):
        r = client.messages.create(
            model=MODEL, max_tokens=300,
            messages=[{"role": "user", "content": prompt}])
        raw = r.content[0].text
        if sabotage_first and attempt == 1:
            raw = BAD_JSON  # pretend the model had a bad first attempt
        try:
            data = json.loads(raw)
            if all(k in data for k in REQUIRED):
                return data, attempt
            problem = "missing required keys"
        except json.JSONDecodeError:
            problem = "not valid JSON"
        prompt += ("\nYour last output was not valid JSON. Respond ONLY "
                   "with the JSON object itself, no other text.")
        print("attempt", attempt, "rejected:", problem)
    return None, max_attempts


print("--- 1. vague prompt: the model wraps JSON in chatty prose ---")
vague = client.messages.create(
    model=MODEL, max_tokens=300,
    messages=[{"role": "user", "content": "Get the product info: " + review}])
raw = vague.content[0].text
print("model said:", raw.splitlines()[0], "...")
try:
    json.loads(raw)
    print("parsed fine")
except json.JSONDecodeError as err:
    print("json.loads raised:", str(err)[:45], "...")

print("--- 2. ONLY-JSON prompt: parse, then validate required keys ---")
strict_prompt = (
    "Extract the product name, price and category from the review.\n"
    "Respond ONLY with JSON with exactly these keys: name, price, category.\n"
    "<review>" + review + "</review>")
strict = client.messages.create(
    model=MODEL, max_tokens=300,
    messages=[{"role": "user", "content": strict_prompt}])
data = json.loads(strict.content[0].text)
print("parsed:", data)
print("required keys present:", all(k in data for k in REQUIRED))

print("--- 3. retry loop (first attempt deliberately bad) ---")
result, used = ask_json(strict_prompt, sabotage_first=True)
print("result:", result)
print("attempts used:", used)

# ------------------------------------------------------------------
# REAL CODE - same pattern against the real API. Put the key in the
# ANTHROPIC_API_KEY environment variable; anthropic.Anthropic() reads
# it automatically. (pip install anthropic)
# ------------------------------------------------------------------
# import json
# import anthropic
#
# client = anthropic.Anthropic()
# response = client.messages.create(
#     model="claude-sonnet-5-5",
#     max_tokens=300,
#     messages=[{"role": "user", "content": (
#         "Extract name, price and category from the review.\n"
#         "Respond ONLY with JSON, keys: name, price, category.\n"
#         "<review>" + review + "</review>"
#     )}])
# try:
#     data = json.loads(response.content[0].text)
# except json.JSONDecodeError:
#     data = None  # then retry with a repaired prompt, as in ask_json()

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/16_llm_basics.py
# ------------------------------------------------------------------
# Q1: What does json.loads('Here you go: {"a": 1}') raise, and why
#     must production code catch it?
# Q2: Spot the bug: data = json.loads(response.content[0].text) then
#     print(data["price"]) -- the parse succeeded, so what is missing?
# Q3: Write extract_product(review_text) -> dict or None, using an
#     ONLY-JSON prompt, safe parsing, and required-key validation.
# Q4: Concept: why append a repair note to the prompt instead of
#     resending the exact same prompt?
