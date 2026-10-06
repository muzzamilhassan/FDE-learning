"""
Solution for Project 04 - Bank Account System (OOP).

Run it with:
    python answers/projects/project_04_bank_system_solution.py

A scripted demo that opens accounts, moves money, overdraws on
purpose (to show the custom exception), pays interest and prints
a transaction history.
"""

from __future__ import annotations


class InsufficientFundsError(Exception):
    """Raised when a withdrawal would overdraw an account."""


class Account:
    """A single bank account with a validated balance and a history."""

    bank_name = "Python National Bank"  # class variable: shared by all
    account_count = 0                   # stretch: every account ever made

    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Starting balance cannot be negative.")
        self.owner = owner
        self._balance = float(balance)  # hidden: read it via .balance
        self.history: list[dict] = []
        Account.account_count += 1

    @property
    def balance(self) -> float:
        """Read-only view of the money in the account."""
        return self._balance

    def deposit(self, amount: float) -> float:
        """Add money; returns the new balance."""
        if amount <= 0:
            raise ValueError("Deposit must be a positive amount.")
        self._balance += amount
        self._record("deposit", amount)
        return self._balance

    def withdraw(self, amount: float) -> float:
        """Take money out; refuses to overdraw the account."""
        if amount <= 0:
            raise ValueError("Withdrawal must be a positive amount.")
        if amount > self._balance:
            raise InsufficientFundsError(
                f"{self.owner} cannot withdraw ${amount:,.2f}: "
                f"the balance is only ${self._balance:,.2f}."
            )
        self._balance -= amount
        self._record("withdraw", amount)
        return self._balance

    def _record(self, kind: str, amount: float) -> None:
        """Append one line to the transaction history."""
        self.history.append(
            {"kind": kind, "amount": amount, "balance": self._balance}
        )

    def __str__(self) -> str:
        return f"{self.owner}: ${self._balance:,.2f}"

    def __repr__(self) -> str:
        return f"Account(owner={self.owner!r}, balance={self._balance:.2f})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Account):
            return NotImplemented
        return self.owner == other.owner and self._balance == other._balance


class SavingsAccount(Account):
    """An Account that grows: it pays interest."""

    interest_rate = 0.03  # class variable: 3 percent

    def add_interest(self) -> float:
        """Pay interest on the current balance; returns the interest."""
        interest = self._balance * self.interest_rate
        self._balance += interest
        self._record("interest", interest)
        return interest


class Bank:
    """Manages many accounts, keyed by the (lowercased) owner name."""

    def __init__(self) -> None:
        self.accounts: dict[str, Account] = {}

    def add_account(self, account: Account) -> Account:
        self.accounts[account.owner.lower()] = account
        return account

    def get_account(self, name: str) -> Account:
        key = name.strip().lower()
        if key not in self.accounts:
            raise KeyError(f"No account for '{name}' at {Account.bank_name}.")
        return self.accounts[key]

    def total_holdings(self) -> float:
        return sum(account.balance for account in self.accounts.values())

    def __len__(self) -> int:
        return len(self.accounts)


def print_history(account: Account) -> None:
    """Print every transaction of one account."""
    print(f"\nTransaction history for {account.owner}:")
    for number, entry in enumerate(account.history, start=1):
        print(f"  {number}. {entry['kind']:<8} ${entry['amount']:>8,.2f}"
              f"   balance ${entry['balance']:>9,.2f}")


def main():
    print("=" * 50)
    print(f"  Welcome to {Account.bank_name} -- solution demo")
    print("=" * 50)

    bank = Bank()
    alice = bank.add_account(Account("Alice", 100))
    bob = bank.add_account(SavingsAccount("Bob", 250))

    print(f"\n1) The bank manages {len(bank)} account(s).")
    print("   repr(alice) ->", repr(alice))
    print("   str(alice)  ->", alice)

    print("\n2) Deposits and withdrawals:")
    alice.deposit(50)
    bob.withdraw(50)
    print(f"   {alice}")
    print(f"   {bob}")

    print("\n3) Overdrawing raises the custom exception:")
    try:
        alice.withdraw(10_000)
    except InsufficientFundsError as exc:
        print(f"   InsufficientFundsError: {exc}")

    print("\n4) Bad amounts raise ValueError:")
    try:
        bob.deposit(-20)
    except ValueError as exc:
        print(f"   ValueError: {exc}")

    print("\n5) Savings accounts earn interest "
          f"({SavingsAccount.interest_rate:.0%}):")
    earned = bob.add_interest()
    print(f"   Bob earned ${earned:.2f} -> {bob}")

    print("\n6) isinstance shows the family tree:")
    print("   isinstance(bob, SavingsAccount):", isinstance(bob, SavingsAccount))
    print("   isinstance(bob, Account)       :", isinstance(bob, Account))

    print("\n7) __eq__ compares owner AND balance:")
    twin = Account("Alice", alice.balance)
    print("   alice == twin (same owner, same balance):", alice == twin)
    print("   alice == bob                            :", alice == bob)

    print("\n8) Unknown customers are refused:")
    try:
        bank.get_account("Carol")
    except KeyError as exc:
        print("   KeyError:", exc)

    print_history(alice)

    print(f"\n9) Total holdings across the bank: ${bank.total_holdings():,.2f}")
    print(f"   Accounts ever opened: {Account.account_count}")


if __name__ == "__main__":
    main()
