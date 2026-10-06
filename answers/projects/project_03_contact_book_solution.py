"""
Solution for Project 03 - Contact Book.

Run it with:
    python answers/projects/project_03_contact_book_solution.py

Instead of an interactive menu it runs a scripted demo that
exercises every feature, so you can see the whole project work
in one go. The contacts are saved to contacts.json next to this
file. Stretch idea: wrap the features in a while-loop menu like
project 02.
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("contacts.json")


class ContactError(Exception):
    """Raised when a contact operation cannot be completed."""


def add_contact(book, name, phone, email="", category="friend"):
    """Add a contact dict to the book (keyed by lowercase name)."""
    key = name.strip().lower()
    if not key:
        raise ContactError("A contact needs a name.")
    if key in book:
        raise ContactError(f"'{name}' is already in the book.")
    contact = {
        "name": name.strip(),
        "phone": phone,
        "email": email,
        "category": category,
    }
    book[key] = contact
    return contact


def find_contact(book, name):
    """Case-insensitive lookup; raises ContactError when missing."""
    key = name.strip().lower()
    if key not in book:
        raise ContactError(f"No contact named '{name}'.")
    return book[key]


def list_contacts(book):
    """The contact dicts, sorted by name (case-insensitive)."""
    return sorted(book.values(), key=lambda contact: contact["name"].lower())


def update_contact(book, name, **fields):
    """Update only the fields that were passed in; returns the contact."""
    contact = find_contact(book, name)  # raises ContactError if missing
    allowed = {"phone", "email", "category"}
    for field, value in fields.items():
        if field not in allowed:
            raise ContactError(f"Cannot update unknown field '{field}'.")
        contact[field] = value
    return contact


def delete_contact(book, name):
    """Remove the contact and return True; False when unknown."""
    key = name.strip().lower()
    if key not in book:
        return False
    del book[key]
    return True


def category_stats(book):
    """{category: number_of_contacts} via a dict comprehension."""
    return {
        category: sum(1 for c in book.values() if c["category"] == category)
        for category in {c["category"] for c in book.values()}
    }


def save_contacts(book, path=DATA_FILE):
    """Write the contacts as a JSON list."""
    with path.open("w", encoding="utf-8") as f:
        json.dump(list(book.values()), f, indent=2)


def load_contacts(path=DATA_FILE):
    """Rebuild the book from JSON; missing/broken file -> empty dict."""
    if not path.exists():
        return {}
    try:
        with path.open("r", encoding="utf-8") as f:
            contacts = json.load(f)
        return {c["name"].lower(): c for c in contacts}
    except (json.JSONDecodeError, KeyError, TypeError, OSError):
        print(f"  Warning: could not read {path.name}, starting fresh.")
        return {}


def show(book, title):
    """Pretty-print every contact, sorted by name."""
    print(f"\n{title}")
    for contact in list_contacts(book):
        print(f"  {contact['name']:<15} {contact['phone']:<10} "
              f"{contact['category']:<8} {contact['email']}")


def main():
    print("=" * 50)
    print("  CONTACT BOOK -- solution demo")
    print("=" * 50)

    book = load_contacts()
    book.clear()  # demo only: start from scratch so every run is the same
    add_contact(book, "Ada Lovelace", "555-0101", "ada@example.com",
                category="work")
    add_contact(book, "Grace Hopper", "555-0102", category="work")
    add_contact(book, "Alan Turing", "555-0103")
    add_contact(book, "Mary Jackson", "555-0104", category="family")
    print(f"   the book now holds {len(book)} contacts")

    print("\n2) Duplicates are refused (custom exception + try/except):")
    try:
        add_contact(book, "ada lovelace", "555-9999")
    except ContactError as exc:
        print(f"   ContactError: {exc}")

    print("\n3) Case-insensitive search, plus a missing name:")
    try:
        print("   found:", find_contact(book, "GRACE hopper"))
    except ContactError as exc:
        print(f"   ContactError: {exc}")
    try:
        find_contact(book, "Nobody")
    except ContactError as exc:
        print(f"   ContactError: {exc}")

    print("\n4) Updating Alan (only the given fields change):")
    update_contact(book, "Alan Turing", phone="555-9999", category="mentor")

    show(book, "5) All contacts, sorted by name:")

    print("\n6) Contacts per category (dict comprehension):")
    for category, count in sorted(category_stats(book).items()):
        print(f"   {category:<8} {count}")

    print("\n7) Deleting Grace ->", delete_contact(book, "Grace Hopper"))
    print("   Deleting a ghost ->", delete_contact(book, "Nobody"))

    save_contacts(book)
    print(f"\nSaved {len(book)} contacts to {DATA_FILE.name}. Done!")


if __name__ == "__main__":
    main()
