"""
=====================================================================
TOPIC: Custom Exceptions
=====================================================================

SCENARIO
--------
You are writing the checkout flow for a small online shop. When a
cart is empty or a card is declined, a generic ValueError tells the
caller nothing. You want failures with real names - ones that carry
data like the declined amount - so calling code can react precisely.

TOPIC
-----
- Define your own error by subclassing Exception.
- Name them PascalCase and end in "Error" (e.g. PaymentDeclinedError).
- Add attributes in __init__ so the error carries useful data.
- A shared base class lets callers catch ALL your errors with one
  except; put SPECIFIC excepts before broad ones or they never run.

QUESTIONS
---------
Q1. Predict the output: which except block runs, and why?
Q2. Predict: what does print(err) show for a custom error that never
    calls super().__init__(msg)?
Q3. Write OutOfStockError (carrying the item name) and a reserve()
    function that raises it when stock is 0.

Run: python 06_errors/custom_exceptions.py
Answers: answers/06_errors.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

class ShopError(Exception):
    """Base class: every error this shop raises inherits from it."""


class EmptyCartError(ShopError):
    """Raised when checkout is called with no items."""


class PaymentDeclinedError(ShopError):
    def __init__(self, code: str, amount: float):
        super().__init__(f"Card declined (code {code}) for ${amount:.2f}")
        self.code = code                # details the caller can read
        self.amount = amount


def checkout(cart: list[str], amount: float) -> str:
    if not cart:
        raise EmptyCartError("Cart is empty - add something first")
    if amount > 100:
        raise PaymentDeclinedError("limit-exceeded", amount)
    return "paid"


# Catching the BASE class catches every subclass too.
try:
    checkout([], 20.0)
except ShopError as err:
    print(f"Shop problem: {err} ({type(err).__name__})")
# Catch a SPECIFIC error to read its extra attributes safely.
try:
    checkout(["mug"], 250.0)
except PaymentDeclinedError as err:
    print(f"Declined! code={err.code}, amount={err.amount}")

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/06_errors.py
# ------------------------------------------------------------------
# Q1: Predict the output - which block prints?
#     try:
#         checkout(["mug"], 250.0)          # raises PaymentDeclinedError
#     except ShopError:
#         print("A")
#     except PaymentDeclinedError:
#         print("B")
#
# Q2: Predict - what does print(err) show here, and why?
#     class BadError(Exception):
#         def __init__(self, msg):
#             self.msg = msg               # note: no super().__init__(msg)
#     print(BadError("something broke"))
#
# Q3: Write class OutOfStockError(Exception) that stores the item name,
#     and reserve(item, stock) that raises it when stock is 0.
