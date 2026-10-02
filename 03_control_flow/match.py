"""
03_control_flow / match.py
Topic: Structural Pattern Matching (match / case) - Python 3.10+

JAVASCRIPT switch vs PYTHON match-case:
---------------------------------------
JS Switch Statement:
    switch (status) {
        case 200:
            return "OK";
        case 404:
            return "Not Found";
        default:
            return "Unknown";
    }
    // Pitfall in JS: Forgetting `break` causes dangerous fall-through!

Python match-case:
    - NO fall-through! (No `break` statements needed).
    - Can match exact values, multiple values with `|`, types, patterns,
      tuples, lists, and dicts!
    - Supports 'guard clauses' using `if`.
    - Wildcard `case _:` acts as the default fallback.
"""

# ------------------------------------------------------------------------------
# 1. Basic Value Matching
# ------------------------------------------------------------------------------
def handle_http_status(code: int) -> str:
    match code:
        case 200:
            return "OK: Request succeeded"
        case 201:
            return "Created: Resource created"
        case 400:
            return "Bad Request: Check client parameters"
        case 401 | 403:   # Matching multiple alternatives with pipe (|)
            return "Auth Error: Unauthorized or Forbidden"
        case 404:
            return "Not Found: Resource does not exist"
        case 500:
            return "Server Error: Internal server error"
        case _:           # Wildcard (equivalent to 'default:' in JS switch)
            return f"Unhandled HTTP status: {code}"

print("200:", handle_http_status(200))
print("403:", handle_http_status(403))
print("999:", handle_http_status(999))


# ------------------------------------------------------------------------------
# 2. Structural Pattern Matching with Guards
# ------------------------------------------------------------------------------
# Pattern matching can unpack lists, tuples, or dicts while matching their shape!
def dispatch_action(action):
    match action:
        # Match a list of exactly 1 string: ["quit"]
        case ["quit"]:
            print("Action: Quitting application...")

        # Match a 2-element list where 1st is "load": ["load", filename]
        case ["load", filename]:
            print(f"Action: Loading file '{filename}'")

        # Match a 3-element list with a conditional 'guard' (if):
        case ["move", x, y] if isinstance(x, int) and isinstance(y, int):
            print(f"Action: Moving coordinates to ({x}, {y})")

        # Match a dictionary structure:
        case {"type": "notify", "message": msg}:
            print(f"Action: Notification received -> '{msg}'")

        case _:
            print(f"Action: Unrecognized command structure -> {action}")

dispatch_action(["load", "dataset.csv"])
dispatch_action(["move", 15, 30])
dispatch_action({"type": "notify", "message": "Build finished successfully"})
