"""
05_js_to_python / spread_rest.py
Topic: JavaScript Spread (...) and Rest (...) vs Python (* and **)

OPERATOR TRANSLATION GUIDE:
---------------------------
Concept                  JavaScript Syntax            Python Syntax
---------------------------------------------------------------------------------
List/Array Spread        [...arr1, ...arr2]           [*arr1, *arr2]  or  arr1 + arr2
Dict/Object Spread       { ...obj1, ...obj2 }         {**obj1, **obj2}  or  obj1 | obj2
Function Rest Positional function fn(...args) {}      def fn(*args):
Function Rest Named      function fn(opts) {}         def fn(**kwargs):
Function Call Spread     fn(...args)                  fn(*args)
Function Call Named      fn(...obj)                   fn(**kwargs)
"""

# ------------------------------------------------------------------------------
# 1. Spreading Lists (Arrays)
# ------------------------------------------------------------------------------
list_a = [1, 2, 3]
list_b = [4, 5, 6]

# JS: const combined = [0, ...listA, ...listB, 7];
combined = [0, *list_a, *list_b, 7]
print("Combined list with *:", combined)


# ------------------------------------------------------------------------------
# 2. Spreading Dictionaries (Objects)
# ------------------------------------------------------------------------------
default_settings = {"theme": "light", "notifications": True, "fontSize": 14}
user_overrides = {"theme": "dark", "fontSize": 16}

# Approach A (Python 3.5+): Using ** unpacking
# JS: const config = { ...defaultSettings, ...userOverrides };
config_via_unpack = {**default_settings, **user_overrides}

# Approach B (Python 3.9+): Using the union pipe operator (|)
config_via_pipe = default_settings | user_overrides

print("Merged dict (pipe):", config_via_pipe)


# ------------------------------------------------------------------------------
# 3. Spreading Arguments into a Function Call
# ------------------------------------------------------------------------------
def create_endpoint(method: str, path: str, timeout: int = 30):
    return f"{method} {path} (timeout={timeout}s)"

params = ["POST", "/api/v1/checkout"]
# JS: createEndpoint(...params)
print("Position args spread (*params):", create_endpoint(*params))

named_params = {"path": "/api/v1/users", "method": "GET", "timeout": 10}
# JS: createEndpoint(namedParams.method, namedParams.path, ...)
print("Keyword args spread (**named_params):", create_endpoint(**named_params))
