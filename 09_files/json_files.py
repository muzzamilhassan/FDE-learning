"""
09_files / json_files.py
Topic: Working with JSON in Python

JAVASCRIPT vs PYTHON JSON:
--------------------------
JS:
    JSON.stringify(data, null, 2)  -> Stringify to JSON text
    JSON.parse(jsonString)         -> Parse JSON text to Object

Python:
    json.dumps(data, indent=2)     -> Dump to String
    json.loads(json_string)        -> Load from String
    json.dump(data, file)          -> Write directly to a File stream!
    json.load(file)                -> Read directly from a File stream!
"""
import json
from pathlib import Path

app_state = {
    "app_name": "Fullstack Learning",
    "version": "2.4.0",
    "features_enabled": ["auth", "payments", "analytics"],
    "rate_limit": 1000,
    "active": True,
    "database": {"host": "localhost", "port": 5432}
}

# ------------------------------------------------------------------------------
# 1. In-Memory: json.dumps() and json.loads()
# ------------------------------------------------------------------------------
# JS: const jsonStr = JSON.stringify(appState, null, 2);
json_string = json.dumps(app_state, indent=2)
print("Serialized JSON string:\n", json_string)

# JS: const parsedObj = JSON.parse(jsonStr);
parsed_dict = json.loads(json_string)
print("\nParsed version attribute:", parsed_dict["version"])


# ------------------------------------------------------------------------------
# 2. File Streaming: json.dump() and json.load()
# ------------------------------------------------------------------------------
json_file = Path("temp_config.json")

# Write directly to file:
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(app_state, f, indent=2)

# Read directly from file:
with open(json_file, "r", encoding="utf-8") as f:
    loaded_config = json.load(f)

print("Loaded from file:", loaded_config["app_name"])

# Cleanup
if json_file.exists():
    json_file.unlink()
    print("Cleaned up temp_config.json")
