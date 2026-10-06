# Python Learning Path

A hands-on, pure-Python course. Every topic follows the same rhythm:
**Scenario → Topic → Questions**, and every module ends with real
**Projects** you build yourself.

No prior Python needed. No other-language comparisons — just Python.

---

## How Each Lesson Works

Every `.py` file is one bite-sized lesson with three parts:

| Part | What it gives you |
| :--- | :--- |
| **SCENARIO** | A real-world mini-story that motivates the topic |
| **TOPIC** | Short explanation + runnable example code |
| **QUESTIONS** | 3-5 exercises (predict the output, spot the bug, write code) |

**How to study a lesson:**

1. Run the file: `python 01_basics/variables.py`
2. Read the scenario and topic, play with the examples
3. Try every question **yourself** before peeking
4. Check your answers in `answers/`

---

## Learning Path

- [**`01_basics/`**](01_basics) — Variables, data types, strings, operators, input/output, equality.
- [**`02_collections/`**](02_collections) — Lists, tuples, dictionaries, sets, unpacking.
- [**`03_control_flow/`**](03_control_flow) — Conditions, truthy/falsy, loops, match-case.
- [**`04_functions/`**](04_functions) — Functions, arguments, lambdas, map/filter/reduce, comprehensions.
- [**`05_oop/`**](05_oop) — Classes, inheritance, properties, dunder methods.
- [**`06_errors/`**](06_errors) — Exceptions and custom exceptions.
- [**`07_modules/`**](07_modules) — Imports, packages, `__name__ == "__main__"`.
- [**`08_files/`**](08_files) — Text, JSON, and CSV files.
- [**`09_python_features/`**](09_python_features) — Iterators, generators, decorators, context managers.
- [**`10_async/`**](10_async) — `async / await` and concurrent tasks.
- [**`11_typing/`**](11_typing) — Type hints and dataclasses.
- [**`12_packages/`**](12_packages) — Virtual environments and `requirements.txt`.

---

## Projects (Build to Learn)

After each few modules, build a project. Starter code with TODOs is in
[`99_projects/`](99_projects); full solutions in `answers/projects/`.

| # | Project | Difficulty | Practices |
| :--- | :--- | :--- | :--- |
| 1 | Number Guessing Game | Beginner | Basics, loops, conditions, `random` |
| 2 | Todo List CLI | Beginner+ | Collections, functions, match, JSON files |
| 3 | Contact Book | Intermediate | Dicts, comprehensions, errors, sorting |
| 4 | Bank Account System | Intermediate+ | OOP: classes, inheritance, properties, exceptions |
| 5 | Sales Data Analyzer | Capstone | CSV, generators, decorators, typing, dataclasses |

```bash
python 99_projects/project_01_number_game.py
```

---

## Answers

Every module has one answers file with worked solutions to all its
questions — but try first!

```bash
python answers/01_basics.py
```

---

## How to Run

Any lesson, from the repo root:

```bash
python 01_basics/variables.py
python 05_oop/classes.py
```

The `07_modules` lessons import each other — run `main.py` from inside its folder:

```bash
cd 07_modules
python main.py
```
