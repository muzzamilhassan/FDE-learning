"""
12_typing / dataclasses.py
Topic: The @dataclass Decorator (TypeScript Interfaces / Classes Made Simple)

TYPESCRIPT INTERFACE vs PYTHON @dataclass:
------------------------------------------
In TypeScript:
    interface User {
        id: number;
        name: string;
        email: string;
        role?: string;
    }
    // At runtime in JS, an interface does not exist. It is just a plain object.

In Python:
    Normally, writing a class requires tedious boilerplate:
        def __init__(self, id, name, email): ...
        def __repr__(self): ...
        def __eq__(self, other): ...

    The `@dataclass` decorator AUTOMATICALLY generates:
        - `__init__()` (constructor with type hints)
        - `__repr__()` (clean printable representation)
        - `__eq__()` (value equality comparison)
"""
from dataclasses import dataclass, field

# ------------------------------------------------------------------------------
# 1. Basic Dataclass
# ------------------------------------------------------------------------------
@dataclass
class User:
    id: int
    username: str
    email: str
    role: str = "viewer"  # Default value

user1 = User(id=1, username="sarah", email="sarah@corp.com")
user2 = User(id=1, username="sarah", email="sarah@corp.com")

print("User repr (automatic!):", user1)
# Automatic __eq__ compares attribute values:
print("user1 == user2 (automatic value equality!):", user1 == user2)


# ------------------------------------------------------------------------------
# 2. Frozen (Immutable) Dataclasses & Default Factory
# ------------------------------------------------------------------------------
# `frozen=True` makes instances immutable (like Object.freeze() in JS!):
# `default_factory=list` creates a fresh new list for every instance:
@dataclass(frozen=True)
class DatabaseConfig:
    host: str
    port: int = 5432
    options: list[str] = field(default_factory=list)

db_config = DatabaseConfig(host="db.internal.net", options=["ssl=true"])
print("\nFrozen db_config:", db_config)

# Attempting mutation raises FrozenInstanceError:
try:
    db_config.port = 3306  # type: ignore
except Exception as e:
    print(f"Caught mutation error on frozen dataclass: {type(e).__name__} -> {e}")
