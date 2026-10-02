# Python Learning Path for JavaScript Developers

Clean, concise, bite-sized Python code examples comparing JavaScript directly to Python, with a simple focus on Object-Oriented Programming (OOP).

---

## ⚡ Quick JavaScript vs Python Cheat Sheet

| JavaScript | Python Equivalent | Note |
| :--- | :--- | :--- |
| `let x = 10; const y = 20;` | `x = 10; y = 20` | No declaration keywords (`let`/`const`) |
| `console.log("Hi", name)` | `print("Hi", name)` | Built-in print |
| `` `Hello ${name}` `` | `f"Hello {name}"` | f-string |
| `arr.push(x)` | `lst.append(x)` | Add to end of list |
| `arr.length` | `len(lst)` | Built-in length function |
| `{ name: "Alice" }` | `{"name": "Alice"}` | Dict keys **must** be quoted strings |
| `obj.key ?? default` | `obj.get("key", default)` | Safe dictionary access |
| `&&`, `\|\|`, `!` | `and`, `or`, `not` | Logical operators |
| `===` (value check) | `==` | Deep structural value equality |
| `arr.length === 0` | `if not lst:` | **Empty `[]` and `{}` are Falsy in Python!** |
| `...args` | `*args` / `**kwargs` | Positional tuple & keyword dict |
| `arr.map(fn).filter(fn)` | `[fn(x) for x in arr if cond]` | List comprehensions |
| `class Dog extends Animal` | `class Dog(Animal):` | Class inheritance |
| `constructor()` | `def __init__(self):` | Initializer method |
| `this.name` | `self.name` | `self` explicitly passed as 1st param |
| `get prop() / set prop()` | `@property / @prop.setter` | Managed properties |
| `Promise.all([p1, p2])` | `asyncio.gather(c1, c2)` | Concurrent async |

---

## 📁 Modules

- [**`01_basics/`**](file:///c:/Users/Revnix/Desktop/personal/fde-learning/01_basics) — Variables, data types, strings, operators, I/O.
- [**`02_collections/`**](file:///c:/Users/Revnix/Desktop/personal/fde-learning/02_collections) — Lists, tuples, dictionaries, sets.
- [**`03_control_flow/`**](file:///c:/Users/Revnix/Desktop/personal/fde-learning/03_control_flow) — Conditions, loops, match-case.
- [**`04_functions/`**](file:///c:/Users/Revnix/Desktop/personal/fde-learning/04_functions) — Functions, arguments, lambdas, comprehensions.
- [**`05_js_to_python/`**](file:///c:/Users/Revnix/Desktop/personal/fde-learning/05_js_to_python) — Map/filter/reduce, destructuring, spread/rest, truthy/falsy, equality.
- [**`06_oop/`**](file:///c:/Users/Revnix/Desktop/personal/fde-learning/06_oop) — Classes (`self`), inheritance, properties, dunder methods.
- [**`07_errors/`**](file:///c:/Users/Revnix/Desktop/personal/fde-learning/07_errors) — Exceptions & custom errors.
- [**`08_modules/`**](file:///c:/Users/Revnix/Desktop/personal/fde-learning/08_modules) — Imports and `__name__ == "__main__"`.
- [**`09_files/`**](file:///c:/Users/Revnix/Desktop/personal/fde-learning/09_files) — Text, JSON, and CSV files.
- [**`10_python_features/`**](file:///c:/Users/Revnix/Desktop/personal/fde-learning/10_python_features) — Iterators, generators, decorators, context managers.
- [**`11_async/`**](file:///c:/Users/Revnix/Desktop/personal/fde-learning/11_async) — `async / await` and concurrent tasks.
- [**`12_typing/`**](file:///c:/Users/Revnix/Desktop/personal/fde-learning/12_typing) — Type hints and `@dataclass`.
- [**`13_packages/`**](file:///c:/Users/Revnix/Desktop/personal/fde-learning/13_packages) — Virtual environments and `requirements.txt`.

---

## 🚀 How to Run

```bash
python 01_basics/variables.py
python 06_oop/classes.py
python 06_oop/inheritance.py
```
