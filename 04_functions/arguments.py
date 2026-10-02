"""
04_functions / arguments.py
Topic: Positional, Keyword, Default, *args, and **kwargs

JAVASCRIPT vs PYTHON ARGUMENTS:
-------------------------------
JS Rest Parameters:
    function sum(...numbers) { return numbers.reduce((a,b) => a+b, 0); }
    // JS has NO built-in keyword arguments! JS developers pass an options object:
    function createUser({ username, role = "user", active = true } = {}) {}

Python Arguments:
    *args    -> Collects arbitrary POSITIONAL arguments into a tuple (like JS ...rest).
    **kwargs -> Collects arbitrary KEYWORD arguments into a dictionary!
                (Native named parameters without needing an options object!).
"""

# ------------------------------------------------------------------------------
# 1. Named / Keyword Arguments & Default Values
# ------------------------------------------------------------------------------
# IMPORTANT PYTHON RULE: Never use mutable defaults (e.g. def fn(items=[]))!
# Always use None: def fn(items=None): if items is None: items = []
def send_email(to: str, subject: str = "Notification", priority: str = "normal"):
    return f"Sending '{subject}' to {to} [Priority: {priority}]"

# In Python, you can call functions using named parameters in ANY order:
print(send_email("alice@example.com"))
print(send_email(to="bob@example.com", priority="high", subject="Security Alert"))


# ------------------------------------------------------------------------------
# 2. *args (Arbitrary Positional Arguments -> Tuple)
# ------------------------------------------------------------------------------
# JS: function addAll(...nums) { ... }
def calculate_sum(*numbers: float) -> float:
    # `numbers` is packed into a tuple: (10, 20, 30, ...)
    print("Received *numbers as tuple:", numbers)
    return sum(numbers)

print("Sum result:", calculate_sum(10, 20, 30, 40))


# ------------------------------------------------------------------------------
# 3. **kwargs (Arbitrary Keyword Arguments -> Dictionary)
# ------------------------------------------------------------------------------
# JS has no direct equivalent; in JS you pass an options object: fn(opts)
def create_user_profile(username: str, **attributes):
    # `attributes` is packed into a dictionary: {"email": "...", "role": "..."}
    print(f"Creating profile for: {username}")
    for key, value in attributes.items():
        print(f"  - {key}: {value}")

create_user_profile("dev_sarah", email="sarah@corp.com", role="Staff Engineer", team="Core")


# ------------------------------------------------------------------------------
# 4. Positional-Only (/) and Keyword-Only (*) Markers (Python 3.8+)
# ------------------------------------------------------------------------------
# - Arguments BEFORE '/' MUST be passed positionally.
# - Arguments AFTER '*' MUST be passed by keyword name.
def configure_service(service_name, /, version="1.0", *, debug=False):
    return f"Service: {service_name} v{version} (debug={debug})"

print(configure_service("AuthAPI", "2.0", debug=True))
# configure_service(service_name="AuthAPI")  # ERROR! service_name is positional-only
# configure_service("AuthAPI", "2.0", True)  # ERROR! debug is keyword-only
