"""
=====================================================================
TOPIC: How LLM APIs Work
=====================================================================

SCENARIO
--------
You are adding an AI feature to a support-desk app: someone types a
ticket, your code calls a model, a suggested reply comes back. This
file shows the anatomy of that call -- and why a multi-turn
"conversation" is really the same call made over and over.

TOPIC
-----
One entry point: client.messages.create(model, max_tokens, system,
messages). max_tokens is REQUIRED -- it caps reply length; too low and
the reply is cut off (stop_reason becomes "max_tokens"). messages is a
list of {"role": "user" or "assistant", "content": str}; the first one
must be "user". system is a separate string for standing instructions
-- it is not a message. The response has .content, a LIST of blocks
(use block.text where block.type == "text"), plus .usage token counts
and .stop_reason. The API is STATELESS: it remembers nothing, so every
turn you resend the whole list -- drop old turns and the model forgets.

QUESTIONS
---------
Q1. Predict: turn 2 sends ONLY "What is my name?" -- what comes back?
Q2. Spot the bug: a create() call that leaves out max_tokens.
Q3. Concept: on turn 9 of a chat, what does usage.input_tokens count?
Q4. Write code: a chat() helper that keeps one history list and
    resends it on every turn.

Run: python 16_llm_basics/how_llm_apis_work.py
Answers: answers/16_llm_basics.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------
from types import SimpleNamespace

# SIMULATION - stand-in for the real API. Same call/response shape as
# the anthropic SDK, no network, no key -- every flow below runs.
def _response(text, in_tokens, out_tokens):
    """Shaped like the real Message: block list, usage, stop_reason."""
    block = SimpleNamespace(type="text", text=text)
    usage = SimpleNamespace(input_tokens=in_tokens, output_tokens=out_tokens)
    return SimpleNamespace(content=[block], usage=usage,
                           stop_reason="end_turn",  # "max_tokens" if cut off
                           model="claude-sonnet-5-5")


def _reply(model, max_tokens, system, messages):
    """The canned 'model': tiny string rules instead of a network."""
    history = " ".join(m["content"] for m in messages).lower()
    last = messages[-1]["content"].lower()
    name = None
    if "my name is" in history:
        name = history.split("my name is")[-1].split()[0].strip(".,!?")
    if "what is my name" in last:
        text = ("Your name is " + name.title() + "." if name
                else "I don't know your name - you never told me.")
    elif name:
        text = "Nice to meet you, " + name.title() + "!"
    else:
        text = "Sorry to hear that! Did you hold power for 10 seconds?"
    in_tokens = (len(system or "") + len(history)) // 4  # pretend count
    return _response(text, in_tokens, len(text) // 4)


class SimulatedAnthropic:
    """SIMULATION - stands in for anthropic.Anthropic()."""
    class messages:  # so client.messages.create(...) works like the SDK
        @staticmethod
        def create(model, max_tokens, system=None, messages=None):
            return _reply(model, max_tokens, system, messages)


MODEL = "claude-sonnet-5-5"
client = SimulatedAnthropic()

print("--- one call: request in, Message object out ---")
response = client.messages.create(
    model=MODEL,
    max_tokens=300,  # required -- caps the reply length
    system="You are a concise support assistant.",
    messages=[{"role": "user", "content": "My laptop will not boot."}])
print("text:", response.content[0].text)
print("usage in/out:", response.usage.input_tokens,
      response.usage.output_tokens, "| stop_reason:", response.stop_reason)

print("--- stateless API: resend the WHOLE history every turn ---")
history = [{"role": "user", "content": "Hi! My name is Sam."}]
r1 = client.messages.create(model=MODEL, max_tokens=300, messages=history)
history.append({"role": "assistant", "content": r1.content[0].text})
print("turn 1:", r1.content[0].text)
r2 = client.messages.create(  # turn 1 dropped: the model never saw Sam
    model=MODEL, max_tokens=300,
    messages=[{"role": "user", "content": "What is my name?"}])
print("turn 2, history dropped:", r2.content[0].text)
history.append({"role": "user", "content": "What is my name?"})
r3 = client.messages.create(model=MODEL, max_tokens=300, messages=history)
print("turn 2, history resent:", r3.content[0].text)
print("input tokens grow with history:", r1.usage.input_tokens, "->",
      r3.usage.input_tokens)

# ------------------------------------------------------------------
# REAL CODE - what this looks like with a key. Put the key in the
# environment variable ANTHROPIC_API_KEY (never in your code), then
# anthropic.Anthropic() reads it automatically. (pip install anthropic)
# ------------------------------------------------------------------
# import anthropic
#
# client = anthropic.Anthropic()
# response = client.messages.create(
#     model="claude-sonnet-5-5",
#     max_tokens=1024,  # required -- raise it if replies get truncated
#     system="You are a concise support assistant.",
#     messages=[{"role": "user", "content": "My laptop will not boot."}])
# print(response.content[0].text)  # in real apps, check block.type first
# print(response.usage.input_tokens, response.usage.output_tokens)
# print(response.stop_reason)      # "end_turn" or "max_tokens" (truncated)

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/16_llm_basics.py
# ------------------------------------------------------------------
# Q1: Predict the "turn 2, history dropped" output above. Which line
#     makes the resent version work?
# Q2: Spot the bug: client.messages.create(model="claude-sonnet-5-5",
#     messages=[{"role": "user", "content": "Hi"}])
# Q3: On turn 9 of a chat, what does usage.input_tokens count, and why
#     does the number grow every turn?
# Q4: Write chat(user_text): append to a shared history list, call the
#     API with the WHOLE list, append the reply, return its text.
