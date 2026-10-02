"""
07_errors / custom_exceptions.py
Topic: Creating Custom Domain Exceptions

JAVASCRIPT vs PYTHON CUSTOM ERRORS:
-----------------------------------
JavaScript:
    class UserNotFoundError extends Error {
        constructor(userId) {
            super(`User with ID ${userId} not found`);
            this.name = "UserNotFoundError";
            this.userId = userId;
        }
    }

Python:
    class UserNotFoundError(Exception):
        def __init__(self, user_id: int):
            super().__init__(f"User with ID {user_id} was not found.")
            self.user_id = user_id
"""

# Base Application Exception
class ApplicationError(Exception):
    """Base class for all domain exceptions in our application."""
    pass


class UserNotFoundError(ApplicationError):
    """Raised when a queried user does not exist."""
    def __init__(self, user_id: int):
        self.user_id = user_id
        super().__init__(f"User with ID {user_id} was not found in database.")


class InsufficientFundsError(ApplicationError):
    """Raised when a wallet or account lacks sufficient funds for a transaction."""
    def __init__(self, current_balance: float, attempted_amount: float):
        self.current_balance = current_balance
        self.attempted_amount = attempted_amount
        diff = attempted_amount - current_balance
        super().__init__(
            f"Insufficient funds: Balance is ${current_balance:.2f}, "
            f"tried to withdraw ${attempted_amount:.2f} (short by ${diff:.2f})."
        )


# Practical application usage:
user_db = {1: "Alice", 2: "Bob"}

def get_user(user_id: int) -> str:
    if user_id not in user_db:
        raise UserNotFoundError(user_id)
    return user_db[user_id]


try:
    user = get_user(99)
except UserNotFoundError as err:
    print(f"Caught custom exception: {err}")
    print(f"Target User ID attribute: {err.user_id}")
