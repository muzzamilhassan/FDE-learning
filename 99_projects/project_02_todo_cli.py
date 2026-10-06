"""
=====================================================================
PROJECT: Todo List CLI  (Difficulty: beginner-intermediate)
=====================================================================

SCENARIO
--------
You keep promising yourself you will finally organize your week, but
sticky notes keep disappearing. Time to build your own todo app that
lives in the terminal: add tasks, list them, tick them off, delete
the ones that no longer matter -- and everything survives a restart
because the list is saved to a JSON file on disk.

WHAT YOU WILL PRACTICE
----------------------
- Lists and list methods (from module 02)
- Dictionaries (from module 02)
- Writing your own functions (from module 04)
- while loops and the match statement (from module 03)
- String methods like .strip() and .lower() (from module 01)
- Saving and loading JSON files (from module 08)

YOUR TASKS
----------
1. Write load_tasks(): return [] when todos.json does not exist yet,
   otherwise open it and return the parsed JSON list.
2. Write save_tasks(tasks): dump the list into todos.json (indent=2
   makes the file human-readable).
3. Write next_id(tasks): one higher than the biggest id in use
   (1 when the list is empty). Every task gets a unique id.
4. Write add_task(tasks): ask for a title, then append a dict like
   {"id": 1, "title": "Buy milk", "done": False}.
5. Write list_tasks(tasks): print each task as "[x] #3 Walk dog"
   ('x' when done, ' ' when not). Empty list? Print a cheery line.
6. Write complete_task(tasks) and delete_task(tasks): ask for an id,
   convert with int() inside try/except ValueError, then act on the
   matching task (or print a "not found" message).
7. The menu in main() currently uses if/elif. Swap it for a match
   statement (module 03) -- cleaner and it practices match.
8. Stretch: add an "edit" option that renames a task.

STARTER CODE
------------
Complete the TODOs below. Run with:
    python 99_projects/project_02_todo_cli.py

Hints are inline. A full solution is in answers/projects/.
=====================================================================
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
    """
    Read the saved tasks from DATA_FILE.

    TODO 1: if the file does not exist, return []
    TODO 2: otherwise open it and return json.load(f)
    Hint: with DATA_FILE.open("r", encoding="utf-8") as f: ...
    """
    print("TODO: implement load_tasks()")
    return []


def save_tasks(tasks):
    """
    Write the whole task list to DATA_FILE as JSON.
    TODO: json.dump(tasks, f, indent=2)
    """
    print("TODO: implement save_tasks()")


def next_id(tasks):
    """
    Return one more than the biggest id currently in use.
    TODO: max(task["id"] for task in tasks) + 1 -- careful, what if
    the list is empty? max([], default=0) is your friend.
    """
    print("TODO: implement next_id()")
    return 1


def add_task(tasks):
    """
    TODO 4: ask "What needs doing? ", strip it, and append
    {"id": next_id(tasks), "title": title, "done": False}.
    Print a short confirmation.
    """
    print("TODO: implement add_task()")


def list_tasks(tasks):
    """
    TODO 5: print every task as "[x] #1 Buy milk" (or "[ ]" when not
    done). If there are no tasks, print something friendly instead.
    Hint: mark = "x" if task["done"] else " "
    """
    print("TODO: implement list_tasks()")


def complete_task(tasks):
    """
    TODO 6: ask for an id, find the task with that id, set
    task["done"] = True and confirm. Handle bad/unknown ids.
    """
    print("TODO: implement complete_task()")


def delete_task(tasks):
    """
    TODO 6: ask for an id and remove that task from the list.
    Hint: tasks.remove(found_task) or keep only the others.
    """
    print("TODO: implement delete_task()")


def show_menu():
    print("\n" + "=" * 30)
    print("  TODO LIST")
    print("=" * 30)
    print("  add      - new task")
    print("  list     - show all tasks")
    print("  complete - mark a task done")
    print("  delete   - remove a task")
    print("  quit     - save and exit")


def handle(choice, tasks):
    """
    Run one menu command. Returns False when the user quits.

    TODO 7: replace this if/elif chain with a match statement:
        match choice:
            case "add":
                ...
            case "quit" | "q":
                return False
            case _:
                print(...)
    """
    if choice == "add":
        add_task(tasks)
    elif choice == "list" or choice == "ls":
        list_tasks(tasks)
    elif choice == "complete" or choice == "done":
        complete_task(tasks)
    elif choice == "delete" or choice == "rm":
        delete_task(tasks)
    elif choice == "quit" or choice == "q":
        return False
    else:
        print(f"Unknown option: {choice!r} (try 'add' or 'quit')")
    return True


def main():
    print("TODO LIST -- starter (fill in the TODOs!)")
    tasks = load_tasks()
    print(f"Loaded {len(tasks)} task(s) from {DATA_FILE.name}.")

    running = True
    while running:
        show_menu()
        choice = ask("Choose an option: ")
        if choice is None:  # input closed -> quit politely
            choice = "quit"
        running = handle(choice.strip().lower(), tasks)

    save_tasks(tasks)
    print(f"Saved {len(tasks)} task(s). Bye!")


if __name__ == "__main__":
    main()
