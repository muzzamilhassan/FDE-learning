"""
12_typing / type_hints.py
Topic: Type Hints and Annotations (TypeScript vs Python typing)

TYPESCRIPT vs PYTHON TYPE ANNOTATIONS:
--------------------------------------
TypeScript:
    let age: number = 25;
    let items: string[] = ["a", "b"];
    function process(id: number | string): string { ... }
    // TypeScript types are completely erased at compile time (no runtime presence).

Python:
    age: int = 25
    items: list[str] = ["a", "b"]
    def process(identifier: int | str) -> str: ...
    // Python type hints are NOT enforced by Python at runtime!
    // Python ignores them at execution time.
    // Static type checkers (mypy, pyright) check them during linting / CI.
    // They are preserved in `__annotations__` for reflection and libraries like Pydantic.
"""
from typing import Callable, Optional, Any

# 1. Primitives & Collections
user_name: str = "Alice"
user_id: int = 1001
is_active: bool = True
tags: list[str] = ["python", "typescript", "fullstack"]
metadata: dict[str, Any] = {"version": 1.2, "env": "production"}

# 2. Union Types (Python 3.10+ uses `|` just like TypeScript!)
# TS: id: number | string
def format_user_id(identifier: int | str) -> str:
    return f"USR-{identifier}"

# 3. Optional Types
# TS: email?: string  or  string | null
def get_user_avatar(email: str | None = None) -> str:
    if email:
        return f"https://avatar.dev/{email}"
    return "https://avatar.dev/default"

# 4. Callable (Function Signatures)
# TS: transform: (val: number) => number
def apply_math(value: int, transform: Callable[[int], int]) -> int:
    return transform(value)

print("Formatted ID:", format_user_id(505))
print("Formatted ID with string:", format_user_id("admin_99"))
print("Transform result:", apply_math(10, lambda n: n * 5))
