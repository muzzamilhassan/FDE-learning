"""
Solution for Project 02 - Todo List CLI.

Run it with:
    python answers/projects/project_02_todo_cli_solution.py

Tasks are stored as a JSON list next to this file (todos.json),
so your list survives every restart. Requires Python 3.10+
for the match statement.
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("todos.json")


def ask(prompt):
    """input() that survives closed input (pipes, redirected files)."""
    try:
        return input(prompt)
    except EOFError:
        return None


def load_tasks():
    """Read todos.json; a missing or broken file means an empty list."""
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print(f"  Warning: could not read {DATA_FILE.name}, starting fresh.")
        return []


def save_tasks(tasks):
    """Write the whole task list back to todos.json."""
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def next_id(tasks):
    """One higher than the biggest id in use (1 for an empty list)."""
    return max((task["id"] for task in tasks), default=0) + 1


def find_by_id(tasks, wanted):
    """Return the task with this id, or None."""
    for task in tasks:
        if task["id"] == wanted:
            return task
    return None


def ask_task_id(tasks, action):
    """Ask for an id and return the matching task (or None)."""
    raw = ask(f"Which task id should I {action}? ")
    if raw is None:
        return None
    try:
        wanted = int(raw.strip())
    except ValueError:
        print("  That was not a number.")
        return None
    task = find_by_id(tasks, wanted)
    if task is None:
        print(f"  No task has id {wanted}.")
    return task


def add_task(tasks):
    """Append a new {'id', 'title', 'done'} dict."""
    title = ask("What needs doing? ")
    if title is None or not title.strip():
        print("  Empty task -- nothing added.")
        return
    task = {"id": next_id(tasks), "title": title.strip(), "done": False}
    tasks.append(task)
    print(f"  Added #{task['id']}: {task['title']}")


def list_tasks(tasks):
    """Print every task as '[x] #1 Buy milk'."""
    if not tasks:
        print("  Nothing to do -- enjoy the quiet!")
        return
    print()
    for task in tasks:
        mark = "x" if task["done"] else " "
        print(f"  [{mark}] #{task['id']} {task['title']}")
    done_count = sum(1 for task in tasks if task["done"])
    print(f"\n  {done_count}/{len(tasks)} done\n")


def complete_task(tasks):
    """Mark one task as done."""
    task = ask_task_id(tasks, "complete")
    if task is None:
        return
    if task["done"]:
        print(f"  #{task['id']} was already done.")
    else:
        task["done"] = True
        print(f"  Nice! '#{task['title']}' is done.")


def delete_task(tasks):
    """Remove one task from the list."""
    task = ask_task_id(tasks, "delete")
    if task is None:
        return
    tasks.remove(task)
    print(f"  Deleted #{task['id']}: {task['title']}")


def handle(choice, tasks):
    """Run one menu command. Returns False when it is time to quit."""
    match choice:
        case "add" | "a":
            add_task(tasks)
        case "list" | "ls":
            list_tasks(tasks)
        case "complete" | "done":
            complete_task(tasks)
        case "delete" | "rm":
            delete_task(tasks)
        case "quit" | "q":
            return False
        case _:
            print(f"  Unknown option: {choice!r} (try 'add' or 'quit')")
    return True


MENU = """
==============================
  TODO LIST
==============================
  add      - new task
  list     - show tasks
  complete - mark a task done
  delete   - remove a task
  quit     - save and exit
"""


def main():
    print("TODO LIST -- solution")
    tasks = load_tasks()
    print(f"Loaded {len(tasks)} task(s) from {DATA_FILE.name}.")

    running = True
    while running:
        print(MENU)
        choice = ask("Choose an option: ")
        if choice is None:  # input closed -> save and quit politely
            choice = "quit"
        running = handle(choice.strip().lower(), tasks)

    save_tasks(tasks)
    print(f"Saved {len(tasks)} task(s) to {DATA_FILE.name}. Bye!")


if __name__ == "__main__":
    main()
