"""
=====================================================================
TOPIC: Exceptions - try / except / else / finally
=====================================================================

SCENARIO
--------
You are building a bill-splitting feature for a dinner-club app.
Users type how many people to split a bill between, and sometimes
they type "0" - or even the word "four". Your program must survive
the bad input, print a friendly message, and keep running.

TOPIC
-----
- Put risky code in `try:`; an error there jumps to a matching `except`.
- `except SomeError as err:` handles one error type; `err` holds details.
- `else:` runs only when NOTHING failed; `finally:` runs ALWAYS.
- Catch specific errors; a bare `except:` even swallows Ctrl+C, so avoid it.
- Gotcha: a variable set in `try` may not exist in `except` (it never ran).

QUESTIONS
---------
Q1. Predict the output: which lines print, in what order?
Q2. Spot the bug: the handler crashes with NameError. Why?
Q3. Write parse_count(text): return int(text), or -1 for invalid text.

Run: python 06_errors/exceptions.py
Answers: answers/06_errors.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

def split_bill(total: float, people: int) -> float | None:
    try:
        share = total / people              # risky: ZeroDivisionError if 0
    except ZeroDivisionError:
        print("  Cannot split between zero people.")
        return None
    except TypeError as err:                # wrong type, e.g. people="four"
        print(f"  Bad types: {err}")
        return None
    else:
        # Only reached when the try block raised nothing.
        print(f"  Each person pays: {share:.2f}")
        return share
    finally:
        # Always runs: success, error, or even the early returns above.
        print("  (attempt finished)")


print("Splitting 80.0 between 4 people:")
split_bill(80.0, 4)
print("Splitting 80.0 between 0 people:")
split_bill(80.0, 0)
print("Splitting 80.0 between 'four' people:")
split_bill(80.0, "four")
# finally shines for CLEANUP: it runs even when the error escapes upward.
try:
    try:
        raise ValueError("bad value found")
    finally:
        print("  cleanup ran, even though we raised")
except ValueError as err:
    print(f"  caught outside: {err}")

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/06_errors.py
# ------------------------------------------------------------------
# Q1: Predict the output - which lines print, in what order?
#     try:
#         items = ["a", "b"]
#         print(items[5])
#     except IndexError:
#         print("bad index")
#     else:
#         print("all good")
#     finally:
#         print("done")
#
# Q2: Spot the bug - why does this crash with NameError instead of
#     printing a friendly message?
#     try:
#         price = int("abc")
#     except ValueError:
#         print(price)
# Q3: Write parse_count(text): return int(text), or -1 if the text
#     is not a valid number (e.g. "7" -> 7, "seven" -> -1).
