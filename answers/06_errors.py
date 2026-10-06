"""
Answers for 06_errors - try the questions first!
"""

# ------------------------------------------------------------------
# exceptions.py
# ------------------------------------------------------------------

# Q1: Output is "bad index" then "done".
# Why: print(items[5]) raises IndexError, so control jumps to except
# (skipping else), but finally ALWAYS runs no matter what.
def q1_demo() -> None:
    try:
        items = ["a", "b"]
        print(items[5])
    except IndexError:
        print("bad index")
    else:
        print("all good")        # skipped: an error DID happen
    finally:
        print("done")


# Q2: It crashes with NameError.
# Why: int("abc") raised BEFORE the assignment ran, so `price` was
# never created - the except block cannot print what does not exist.
# Fix: give the variable a default first, or print a message instead.
def q2_fixed() -> None:
    price = None                 # exists even if int() fails
    try:
        price = int("abc")
    except ValueError:
        print("invalid input")


# Q3: parse_count - return the int, or -1 on bad input.
# Why: int() raises ValueError on non-numeric text, so we catch exactly
# that and return the fallback. ZeroDivisionError-style surprises gone.
def parse_count(text: str) -> int:
    try:
        return int(text)
    except ValueError:
        return -1


print("--- exceptions.py answers ---")
q1_demo()                        # -> "bad index" then "done"
q2_fixed()                       # -> "invalid input"
assert parse_count("7") == 7
assert parse_count("seven") == -1
assert parse_count(" 12 ") == 12     # bonus: int() ignores surrounding spaces
print("Q1-Q3 verified.")

# ------------------------------------------------------------------
# custom_exceptions.py
# ------------------------------------------------------------------

# Q1: Only "A" prints.
# Why: PaymentDeclinedError IS a ShopError (subclass), so the first
# matching block wins - put specific excepts BEFORE broad ones.
def q1_order_demo() -> None:
    class ShopError(Exception):
        pass

    class PaymentDeclinedError(ShopError):
        pass

    try:
        raise PaymentDeclinedError("declined")
    except ShopError:                 # matches first, even for the subclass
        print("A")
    except PaymentDeclinedError:      # unreachable: shadowed by ShopError
        print("B")


# Q2: print(err) shows an EMPTY string.
# Why: Exception stores its message during super().__init__(msg);
# skipping that call leaves the parent's message empty (err.msg still
# works, but str(err) - what print uses - shows nothing).
class GoodError(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)         # parent keeps the message...
        self.msg = msg                # ...we keep the attribute


# Q3: OutOfStockError carries the item name; reserve() raises it.
# Why: extra attributes (self.item) let the caller react to the exact
# problem - e.g. restock that one item - not just show a message.
class OutOfStockError(Exception):
    def __init__(self, item: str):
        super().__init__(f"'{item}' is out of stock")
        self.item = item


def reserve(item: str, stock: int) -> str:
    if stock == 0:
        raise OutOfStockError(item)
    return f"{item} reserved"


print("--- custom_exceptions.py answers ---")
q1_order_demo()
err = GoodError("something broke")
print("GoodError message:", err)
assert reserve("mug", 3) == "mug reserved"
try:
    reserve("mug", 0)
except OutOfStockError as oos:
    print("Caught:", oos, "| item =", oos.item)
print("Q1-Q3 verified.")
