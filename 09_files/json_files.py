import json

# In JS: JSON.stringify(data) -> Python: json.dumps(data)
data = {"project": "Python Learning", "stars": 50, "is_active": True}
json_string = json.dumps(data, indent=2)
print("JSON string:\n", json_string)

# In JS: JSON.parse(jsonStr) -> Python: json.loads(json_string)
parsed_dict = json.loads(json_string)
print("Parsed dict:", parsed_dict["project"])
