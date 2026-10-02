# Python Mastery Roadmap for JavaScript Developers

A comprehensive, hands-on learning roadmap designed specifically for **JavaScript/TypeScript developers** transitioning to Python, with a deep focus on **Object-Oriented Programming (OOP)**, language structure differences, and modern Python paradigms.

---

## 🧭 JavaScript to Python Quick Mental Model

| Concept | JavaScript / TypeScript | Python Equivalent |
| :--- | :--- | :--- |
| **Variables** | `let x = 10; const y = 20;` | `x = 10` (no keywords; `UPPERCASE` for constants) |
| **Print Output** | `console.log("Hello", name);` | `print("Hello", name)` |
| **String Interpolation** | `` `Hello, ${name}` `` | `f"Hello, {name}"` |
| **Conditionals** | `if (x) { ... } else if { ... }` | `if x: ... elif y: ... else:` |
| **Ternary Operator** | `cond ? a : b` | `a if cond else b` |
| **Arrays / Lists** | `[1, 2, 3]` (`arr.push(4)`) | `[1, 2, 3]` (`lst.append(4)`) |
| **Objects / Dicts** | `{ name: "Alice" }` | `{"name": "Alice"}` (Keys must be quoted!) |
| **Logical Operators** | `&&`, `\|\|`, `!` | `and`, `or`, `not` |
| **Value Equality** | `===` (strict check) | `==` (value check, structural for lists/dicts) |
| **Reference Equality**| `===` (on objects/arrays) | `is` (checks memory identity) |
| **Empty Check** | `arr.length === 0` | `if not arr:` (**Empty `[]` & `{}` are Falsy in Python!**) |
| **Rest / Spread** | `...args` | `*args` (positional) & `**kwargs` (keyword/dict) |
| **Arrow Functions** | `(a, b) => a + b` | `lambda a, b: a + b` (single expression only) |
| **Array Methods** | `arr.map(fn).filter(fn)` | `[fn(x) for x in arr if cond]` (Comprehensions) |
| **Class Definition** | `class Car { constructor() {} }` | `class Car: def __init__(self):` |
| **`this` vs `self`** | `this` (implicit, dynamically bound) | `self` (explicit first parameter in every method) |
| **Private Fields** | `#field` (ES2022) | `_field` (convention) or `__field` (name mangling) |
| **Getters / Setters** | `get prop() / set prop(val)` | `@property` / `@prop.setter` |
| **Async Function** | `async function fn()` (eager) | `async def fn():` (lazy coroutine) |
| **Promise.all** | `await Promise.all([p1, p2])` | `await asyncio.gather(c1, c2)` |
| **Package Manager** | `package.json` + `npm` | `requirements.txt` + `pip` + `.venv` |

---

## 📁 Repository Structure

```
├── 01_basics/                  # Core syntax, variables, data types, strings, operators, I/O
│   ├── variables.py
│   ├── data_types.py
│   ├── strings.py
│   ├── operators.py
│   └── input_output.py
│
├── 02_collections/             # Python built-in data structures
│   ├── lists.py
│   ├── tuples.py
│   ├── dictionaries.py
│   └── sets.py
│
├── 03_control_flow/            # Conditions, loops, and pattern matching
│   ├── conditions.py
│   ├── loops.py
│   └── match.py
│
├── 04_functions/               # Functions, arguments, lambdas, comprehensions
│   ├── functions.py
│   ├── arguments.py
│   ├── lambda.py
│   └── comprehensions.py
│
├── 05_js_to_python/            # Direct side-by-side mapping from JS to Python
│   ├── map_filter_reduce.py
│   ├── destructuring.py
│   ├── spread_rest.py
│   ├── truthy_falsy.py
│   └── equality.py
│
├── 06_oop/                     # DEEP DIVE: Object-Oriented Programming
│   ├── classes.py              # Blueprint vs instance, self vs this, @classmethod, @staticmethod
│   ├── inheritance.py          # Subclassing, super(), overriding, polymorphism, MRO
│   ├── properties.py           # Encapsulation, protected _var, @property getters & setters
│   └── dunder_methods.py       # Magic methods (__init__, __str__, __repr__, __eq__, __add__, etc.)
│
├── 07_errors/                  # Error and exception handling (try/except/else/finally)
│   ├── exceptions.py
│   └── custom_exceptions.py
│
├── 08_modules/                 # Modular design, imports, and if __name__ == "__main__"
│   ├── math_utils.py
│   ├── user_service.py
│   └── main.py
│
├── 09_files/                   # File I/O: text, JSON, CSV streaming with context managers
│   ├── text_files.py
│   ├── json_files.py
│   └── csv_files.py
│
├── 10_python_features/         # Iterators, generators, decorators, context managers
│   ├── iterators.py
│   ├── generators.py
│   ├── decorators.py
│   └── context_managers.py
│
├── 11_async/                   # Asynchronous programming with asyncio (coroutines vs Promises)
│   ├── basic_async.py
│   └── concurrent_tasks.py
│
├── 12_typing/                  # Static typing and modern dataclasses
│   ├── type_hints.py
│   └── dataclasses.py
│
├── 13_packages/                # Dependency management and virtual environments
│   ├── requirements.txt
│   └── package_demo.py
│
└── README.md
```

---

## 🎯 Master OOP: The 4 Core Pillars in Python

For JavaScript developers where OOP is often prototypal or confused by `this` binding, Python provides clean, classical OOP:

1. **Classes & Instances ([`06_oop/classes.py`](file:///c:/Users/Revnix/Desktop/personal/fde-learning/06_oop/classes.py))**:
   - `self` is explicitly the instance. No mystery `.bind(this)` bugs!
   - `__init__` replaces `constructor`.
   - `@classmethod` operates on the class itself (`cls`).
   - `@staticmethod` groups utility logic without binding instance or class.

2. **Inheritance & Polymorphism ([`06_oop/inheritance.py`](file:///c:/Users/Revnix/Desktop/personal/fde-learning/06_oop/inheritance.py))**:
   - `class Dog(Animal):` extends parent.
   - `super().__init__()` calls parent constructor.
   - Multiple inheritance natively supported (`class C(A, B):`).

3. **Encapsulation & Managed Attributes ([`06_oop/properties.py`](file:///c:/Users/Revnix/Desktop/personal/fde-learning/06_oop/properties.py))**:
   - `_variable` convention signals internal use.
   - `@property` creates getters; `@price.setter` validates incoming values.

4. **Dunder / Magic Methods ([`06_oop/dunder_methods.py`](file:///c:/Users/Revnix/Desktop/personal/fde-learning/06_oop/dunder_methods.py))**:
   - Operator overloading (+, -, ==) and Python protocol hooks (`len()`, indexing `[]`, `in`).

---

## 🚀 Running Any Script

Run any file directly from your terminal:
```bash
python 01_basics/variables.py
python 05_js_to_python/map_filter_reduce.py
python 06_oop/classes.py
python 06_oop/dunder_methods.py
python 11_async/concurrent_tasks.py
```
