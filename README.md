# Python for AI — Learning Path

A hands-on course that takes you from "never wrote Python" to
**building AI features**: data analysis, machine learning, LLM APIs,
RAG, and agents.

Every topic follows the same rhythm: **Scenario → Topic → Questions**,
and every few modules you build a real **Project**.

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

## Setup (one time)

Part 1 needs only Python. Part 2 needs the AI packages:

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows  (Linux/Mac: source .venv/bin/activate)
pip install -r requirements.txt
```

LLM lessons (`16_llm_basics` onward) run **without any API key** — they
use built-in simulations of the API, with the real code shown and ready
for when you have a key.

---

## Part 1 — Python Fundamentals

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

## Part 2 — Python for AI

- [**`13_numpy/`**](13_numpy) — Arrays, shapes, masks, broadcasting, vectorized math.
- [**`14_pandas/`**](14_pandas) — DataFrames: load, explore, filter, group, clean data.
- [**`15_ml_sklearn/`**](15_ml_sklearn) — Your first models: train/test, evaluation, pipelines.
- [**`16_llm_basics/`**](16_llm_basics) — LLM API anatomy, prompting, structured JSON output.
- [**`17_rag/`**](17_rag) — Embeddings, semantic search, retrieval-augmented generation.
- [**`18_ai_agents/`**](18_ai_agents) — Tool calling and the agent loop.

---

## Projects (Build to Learn)

Starter code with TODOs is in [`99_projects/`](99_projects); full
solutions in `answers/projects/`.

| # | Project | Difficulty | Practices |
| :--- | :--- | :--- | :--- |
| 1 | Number Guessing Game | Beginner | Basics, loops, conditions, `random` |
| 2 | Todo List CLI | Beginner+ | Collections, functions, match, JSON files |
| 3 | Contact Book | Intermediate | Dicts, comprehensions, errors, sorting |
| 4 | Bank Account System | Intermediate+ | OOP: classes, inheritance, properties, exceptions |
| 5 | Sales Data Analyzer | Capstone (Part 1) | CSV, generators, decorators, typing, dataclasses |
| 6 | Data Explorer | Intermediate | Pandas: load, clean, group, report |
| 7 | First ML Classifier | Intermediate | sklearn: split, baseline, train, evaluate |
| 8 | Semantic FAQ Search + RAG | Advanced | Embeddings, cosine similarity, retrieval |
| 9 | Mini AI Agent | Advanced | Tool registry, tool calling, agent loop |

```bash
python 99_projects/project_06_data_explorer.py
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
python 13_numpy/array_basics.py
```

The `07_modules` lessons import each other — run `main.py` from inside its folder:

```bash
cd 07_modules
python main.py
```
