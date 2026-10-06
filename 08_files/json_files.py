"""
=====================================================================
TOPIC: JSON Files
=====================================================================

SCENARIO
--------
Your app remembers user preferences: theme, volume, notification
switches. On exit it saves them to settings.json, and on startup it
loads them back, so everything looks exactly as the user left it.

TOPIC
-----
json.dumps(obj) -> JSON string;  json.loads(text) -> Python object.
json.dump(obj, f) and json.load(f) do the same directly with a file.
Type mapping is automatic: True/False -> true/false, None -> null,
dicts -> objects, lists -> arrays.
indent=2 makes saved files human-readable.
Gotcha: JSON keys are ALWAYS strings, and JSON has no tuples or
comments -- round-tripping can change key types on you.

QUESTIONS
---------
Q1. Predict the output: json.dumps of True, None and a list.
Q2. Concept check: dumps/loads vs dump/load -- when do you use each?
Q3. Spot the bug: a saved integer key refuses to load back as an int.
Q4. Write code: save settings to a file and load them back.

Run: python 08_files/json_files.py
Answers: answers/08_files.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------
import json
import shutil
from pathlib import Path

DEMO_DIR = Path(__file__).parent / "demo_files"

try:
    if DEMO_DIR.exists():
        shutil.rmtree(DEMO_DIR)  # fresh start so every run is identical
    DEMO_DIR.mkdir()

    settings = {"theme": "dark", "volume": 80, "notifications": True}

    # dumps / loads work with STRINGS (handy for APIs, logs, messages)
    as_text = json.dumps(settings, indent=2)
    print("--- JSON string ---")
    print(as_text)

    back = json.loads(as_text)
    print("theme:", back["theme"])

    # dump / load work directly with FILE objects (handy for disk)
    path = DEMO_DIR / "settings.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=2)

    with open(path, "r", encoding="utf-8") as f:
        loaded = json.load(f)
    print("--- loaded from file ---")
    print(loaded)

    # The Python -> JSON type mapping happens for you
    print(json.dumps({"on": True, "off": False, "x": None, "nums": [1, 2]}))

finally:
    if DEMO_DIR.exists():
        shutil.rmtree(DEMO_DIR)  # leave no demo files behind

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/08_files.py
# ------------------------------------------------------------------
# Q1: Predict the output:
#         print(json.dumps({"ok": True, "count": 2, "tags": None}))
#
# Q2: What is the difference between dumps/loads and dump/load?
#     Give one use case for each pair.
#
# Q3: Spot the bug -- the last line raises KeyError:
#         saved = json.dumps({1: "one"})
#         loaded = json.loads(saved)
#         print(loaded[1])
#
# Q4: Write code: save {"theme": "dark", "volume": 80} to settings.json
#     with indent=2, load it back, and print the theme.
