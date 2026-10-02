# In TypeScript: let age: number = 25; let name: string = "Alice";
# Python Type Hints (checked by linters like mypy, ignored at runtime)

name: str = "Alice"
age: int = 25
skills: list[str] = ["Python", "JavaScript"]

# In TS: id: number | string
def format_id(user_id: int | str) -> str:
    return f"ID-{user_id}"

# In TS: email: string | null
def get_email(email: str | None = None) -> str:
    return email if email else "No email"

print(format_id(101))
print(format_id("admin"))
print(get_email())
