# In TypeScript: interface User { id: number; name: string; }
# In Python: @dataclass generates constructor and string representation automatically!
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    role: str = "Developer"

u1 = User(1, "Alice")
u2 = User(1, "Alice")

print(u1)               # User(id=1, name='Alice', role='Developer')
print(u1 == u2)         # True (Automatic value equality check!)
