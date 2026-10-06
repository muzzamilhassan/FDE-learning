"""
=====================================================================
PROJECT: Bank Account System  (Difficulty: intermediate-advanced)
=====================================================================

SCENARIO
--------
A coding-bootcamp friend wants a tiny teaching bank for her students:
real accounts, a savings account that pays interest, helpful error
messages when someone overdrafts, and a clean transaction history
per account. You will build the engine behind it with classes -- the
same shapes you would meet in a real banking backend, just smaller.

WHAT YOU WILL PRACTICE
----------------------
- Classes, __init__ and self (from module 05)
- @property with validation (from module 05)
- Dunder methods: __str__, __repr__, __eq__, __len__ (from module 05)
- Inheritance and isinstance (from module 05)
- Class variables shared by all instances (from module 05)
- Custom exceptions (from module 06)

YOUR TASKS
----------
1. Finish Account.__init__: store the owner and the starting balance
   as a hidden self._balance, and start an empty self.history list.
   Refuse a negative starting balance with ValueError.
2. Turn balance into a read-only @property that returns self._balance.
3. deposit(amount): raise ValueError for amount <= 0, otherwise add
   to the balance and record the transaction with self._record().
4. withdraw(amount): raise InsufficientFundsError (with a helpful
   message!) when the balance is too small; otherwise subtract and
   record. Also raise ValueError for amount <= 0.
5. Write __str__ (friendly, like "Alice: $150.00"), __repr__ (for
   debugging) and __eq__ (equal when owner AND balance match; use
   isinstance first).
6. SavingsAccount.add_interest(): add balance * interest_rate to the
   balance and record it. interest_rate is a class variable.
7. Finish the Bank class: add_account (store by owner name in
   self.accounts), get_account (raise KeyError with a nice message),
   total_holdings (sum of all balances) and __len__ (number of
   accounts).
8. Stretch: a class variable account_count that counts every Account
   ever created.

STARTER CODE
------------
Run the demo below with:
    python 99_projects/project_04_bank_system.py

Every "TODO: ..." line disappears as you implement that part.
A full solution is in answers/projects/.
=====================================================================
"""


class InsufficientFundsError(Exception):
    """Raised when a withdrawal would overdraw an account."""
    # Given for free: raising it is your job in withdraw().


class Account:
    """A single bank account with a validated balance and a history."""

    # TODO 8 (stretch): add a class variable account_count = 0 here and
    # increase it inside __init__.

    def __init__(self, owner, balance=0.0):
        # TODO 1: refuse a negative starting balance (raise ValueError),
        # then store self.owner and self._balance (hidden attribute).
        # self.history is provided for you:
        print(f"TODO: flesh out Account.__init__ for {owner!r}")
        self.owner = owner
        self._balance = balance
        self.history = []

    @property
    def balance(self):
        """
        The only public way to read the balance.
        TODO 2: just `return self._balance` (read-only on purpose).
        """
        print("TODO: implement the balance property")
        return self._balance

    def deposit(self, amount):
        """
        TODO 3: amount <= 0 -> ValueError. Otherwise add it to the
        balance, call self._record("deposit", amount) and return
        the new balance.
        """
        print("TODO: implement Account.deposit()")
        return self._balance

    def withdraw(self, amount):
        """
        TODO 4: amount <= 0 -> ValueError. When amount is more than
        the balance, raise:
            InsufficientFundsError(f"Cannot withdraw ${amount:.2f}: "
                                   f"balance is ${self._balance:.2f}.")
        Otherwise subtract, record and return the new balance.
        """
        print("TODO: implement Account.withdraw()")
        return self._balance

    def _record(self, kind, amount):
        """Provided: appends one line to the transaction history.
        Call it from deposit() and withdraw()."""
        self.history.append({"kind": kind, "amount": amount,
                             "balance": self._balance})

    def __str__(self):
        """TODO 5: f"{self.owner}: ${self._balance:.2f}" """
        print("TODO: implement Account.__str__()")
        return f"<Account {self.owner!r}>"

    def __repr__(self):
        """TODO 5: something like Account(owner='Alice', balance=150.00)"""
        print("TODO: implement Account.__repr__()")
        return f"Account({self.owner!r})"

    def __eq__(self, other):
        """
        TODO 5: two accounts are equal when owner and balance match.
        Hint: if not isinstance(other, Account): return NotImplemented
        """
        print("TODO: implement Account.__eq__()")
        return self is other


class SavingsAccount(Account):
    """An Account that grows: it pays interest."""

    interest_rate = 0.03  # class variable: 3 percent for every savings account

    def add_interest(self):
        """
        TODO 6: interest = self._balance * self.interest_rate; add it to
        the balance, record it as "interest" and return the interest.
        """
        print("TODO: implement SavingsAccount.add_interest()")
        return 0.0


class Bank:
    """Manages many accounts in a dict keyed by owner name."""

    def __init__(self):
        self.accounts = {}  # "alice" -> Account(...)

    def add_account(self, account):
        """
        TODO 7: store the account in self.accounts using the lowercased
        owner name as the key. Return the account.
        """
        print("TODO: implement Bank.add_account()")

    def get_account(self, name):
        """
        TODO 7: return the account for `name`, or raise
        KeyError(f"No account for '{name}'.") when it is missing.
        """
        print("TODO: implement Bank.get_account()")
        return None

    def total_holdings(self):
        """TODO 7: the sum of every account's balance."""
        print("TODO: implement Bank.total_holdings()")
        return 0.0

    def __len__(self):
        """TODO 7: len(bank) -> how many accounts the bank manages."""
        print("TODO: implement Bank.__len__()")
        return len(self.accounts)


def main():
    print("=" * 50)
    print("  BANK ACCOUNT SYSTEM -- starter demo")
    print("  Fill in the TODOs and this demo really banks.")
    print("=" * 50)

    bank = Bank()
    alice = Account("Alice", 100)
    bob = SavingsAccount("Bob", 250)
    bank.add_account(alice)
    bank.add_account(bob)

    print(f"\n1) accounts in the bank: {len(bank)}")
    print("   repr(alice) ->", repr(alice))
    print("   str(alice)  ->", alice)

    print("\n2) money movement:")
    print("   Alice deposits 50 ->", alice.deposit(50))
    print("   Bob withdraws 50  ->", bob.withdraw(50))

    print("\n3) overdrawing must raise InsufficientFundsError:")
    try:
        alice.withdraw(10_000)
    except InsufficientFundsError as exc:
        print("   caught:", exc)
    else:
        print("   (no exception yet -- implement Account.withdraw!)")

    print("\n4) savings interest:")
    print("   Bob earns interest ->", bob.add_interest())

    print("\n5) equality compares owner AND balance:")
    print("   alice == Account('Alice', 150) ->", alice == Account("Alice", 150))

    print("\n6) bank totals:")
    print("   total holdings ->", bank.total_holdings())

    print("\nWork through the TODOs top to bottom and rerun often.")


if __name__ == "__main__":
    main()
