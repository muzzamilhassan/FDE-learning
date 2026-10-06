"""
=====================================================================
TOPIC: Match Statements (match / case)
=====================================================================

SCENARIO
--------
Your music app reads text commands from a player bar: "play",
"pause", "stop", plus a volume level as a number. A match statement
routes each command to the right action, replacing a long tower of
elif checks with one readable block.

TOPIC
-----
- match value: / case pattern: -- needs Python 3.10 or newer.
- Cases are checked top to bottom; the FIRST matching case runs.
- No fall-through: exactly one case body ever executes.
- case a | b matches either value; case _ matches anything.
- A guard adds a condition: case n if n > 10: ...
- Gotcha: a bare name in a pattern CAPTURES the value; it does not
  compare against an existing variable.

QUESTIONS
---------
Q1. Predict the output of the Q1 code.
Q2. Spot the bug: the user types "off" but "Powering down" never
    prints. Why?
Q3. Write respond(command) that returns "Running" for "start",
    "Stopped" for "stop", and "Unknown command" otherwise.
Q4. Concept: when does a case written with a bare variable name
    (like case mode:) actually match?

Run: python 03_control_flow/match.py
Answers: answers/03_control_flow.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

def status_message(code: int) -> str:
    match code:
        case 200:
            return "OK"
        case 401 | 403:            # or-pattern: matches either value
            return "Auth Error"
        case 404:
            return "Not Found"
        case _:                    # wildcard: catches everything else
            return "Unknown"

for code in (200, 403, 404, 500):
    print(code, "->", status_message(code))

# Guards check more than plain equality.
def describe(n: int) -> str:
    match n:
        case 0:
            return "zero"
        case n if n > 0:           # guard: only positives land here
            return "positive"
        case _:
            return "negative"
print(describe(7), describe(-7), describe(0))

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/03_control_flow.py
# ------------------------------------------------------------------

# Q1: What does this print?
#     def size(n):
#         match n:
#             case 1 | 2 | 3:   return "small"
#             case n if n <= 6: return "medium"
#             case _:           return "large"
#     print(size(2), size(5), size(9))

# Q2: The user types "off", but "Powering down" never prints. Why?
#     OFF = "off"
#     match "off":
#         case OFF:
#             print("Powering down")

# Q3: Write respond(command) using match:
#     "start" -> "Running", "stop" -> "Stopped",
#     anything else -> "Unknown command".
#     Print the result for "start", "stop", and "dance".

# Q4: Concept question -- a case like "case mode:" matches far more
#     often than you expect. What is it really doing?
