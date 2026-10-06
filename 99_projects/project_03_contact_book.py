"""
=====================================================================
PROJECT: Contact Book  (Difficulty: intermediate)
=====================================================================

SCENARIO
--------
A friend runs a small tutoring side hustle and still tracks clients
in a battered paper notebook. You offer to build her a contact book:
find any client in a second, keep the list sorted by name, group
people by category (work, friend, family...), and never lose data
when the program closes. Small tool, big quality-of-life upgrade.

WHAT YOU WILL PRACTICE
----------------------
- Dictionaries of dictionaries (from module 02)
- Functions with default values and **fields kwargs (from module 04)
- sorted() with key= (from module 02)
- Dict comprehensions (from module 02)
- try/except and a custom exception (from module 06)
- Saving and loading JSON files (from module 08)

YOUR TASKS
----------
1. Keep contacts in one dict, keyed by the lowercase name. Each value
   is a dict with the keys: name, phone, email, category.
2. add_contact(book, name, phone, email="", category="friend"):
   raise ContactError when the name is already in the book.
3. find_contact(book, name): case-insensitive lookup; raise
   ContactError when the name is unknown.
4. list_contacts(book): return the contacts sorted by name using
   sorted(..., key=...).
5. update_contact(book, name, **fields): update ONLY the fields that
   were actually passed in (e.g. phone="555-9999").
6. delete_contact(book, name): remove the contact and return True,
   or return False when the name is unknown.
7. category_stats(book): build {category: count} with a dict
   comprehension.
8. save_contacts()/load_contacts(): read and write the book as JSON
   at DATA_FILE, with try/except so a missing file is not an error.

STARTER CODE
------------
The main() below is a demo that calls every function. Run with:
    python 99_projects/project_03_contact_book.py

Every "TODO: ..." line disappears as you implement that function
(None means "no result yet"). A full solution is in answers/projects/.
=====================================================================
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("contacts.json")


class ContactError(Exception):
    """Raised when a contact operation cannot be completed."""


def add_contact(book, name, phone, email="", category="friend"):
    """
    Add a new contact dict to the book and return it.

    TODO 2: the key is name.strip().lower(); raise ContactError when
    that key already exists. Store the nicely spelled name too.
    Hint: contact = {"name": ..., "phone": ..., "email": ..., "category": ...}
    """
    print("TODO: implement add_contact()")
    return None


def find_contact(book, name):
    """
    Return the contact for `name`, ignoring upper/lower case.
    TODO 3: raise ContactError(f"No contact named '{name}'.") if absent.
    """
    print("TODO: implement find_contact()")
    return None


def list_contacts(book):
    """
    Return the contact dicts sorted by name.
    TODO 4: sorted(book.values(), key=lambda c: c["name"].lower())
    """
    print("TODO: implement list_contacts()")
    return None


def update_contact(book, name, **fields):
    """
    Update only the fields that were passed in, e.g.
        update_contact(book, "Alan", phone="555-9999", category="mentor")
    TODO 5: look the contact up first (raises ContactError if missing),
    then loop over fields.items() and assign. Return the contact.
    Hint: `for field, value in fields.items(): contact[field] = value`
    """
    print("TODO: implement update_contact()")
    return None


def delete_contact(book, name):
    """
    TODO 6: delete the contact and return True; return False when the
    name is unknown. (This one is a two-liner with `del`.)
    """
    print("TODO: implement delete_contact()")
    return False


def category_stats(book):
    """
    TODO 7: return {category: how_many_contacts} using a dict
    comprehension, e.g. {"work": 2, "friend": 1}.
    Hint: the keys can come from {c["category"] for c in book.values()}
    """
    print("TODO: implement category_stats()")
    return {}


def save_contacts(book, path=DATA_FILE):
    """
    TODO 8: write the contacts as a JSON list (book.values()) with
    indent=2, wrapped in `with path.open("w", encoding="utf-8")`.
    """
    print("TODO: implement save_contacts()")


def load_contacts(path=DATA_FILE):
    """
    TODO 8: return {} when the file does not exist. Otherwise read the
    JSON list and rebuild the dict: {c["name"].lower(): c for c in contacts}.
    Wrap the parsing in try/except (json.JSONDecodeError, OSError).
    """
    print("TODO: implement load_contacts()")
    return {}


def main():
    print("=" * 50)
    print("  CONTACT BOOK -- starter demo")
    print("=" * 50)
    print("Each 'TODO: implement ...' line marks a function you")
    print("still need to write. None means 'no result yet'.")
    print()

    book = load_contacts()
    book.clear()  # demo only: start from scratch so every run is the same
    add_contact(book, "Ada Lovelace", "555-0101", "ada@example.com", category="work")
    add_contact(book, "Grace Hopper", "555-0102", category="work")
    add_contact(book, "Alan Turing", "555-0103")
    print(f"   the book now holds {len(book)} contact(s)")

    print("2) find_contact('ada lovelace') ->", find_contact(book, "ada lovelace"))
    print("3) list_contacts ->", list_contacts(book))
    print("4) update_contact(Alan, phone=...) ->",
          update_contact(book, "Alan Turing", phone="555-9999"))
    print("5) category_stats ->", category_stats(book))
    print("6) delete_contact('Grace Hopper') ->", delete_contact(book, "Grace Hopper"))

    save_contacts(book)
    print(f"7) book saved to {DATA_FILE.name}")

    print("\nEvery step showing real data instead of TODO/None?")
    print("Congratulations -- your contact book works end to end!")


if __name__ == "__main__":
    main()
