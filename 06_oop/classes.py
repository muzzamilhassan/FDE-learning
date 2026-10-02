"""
06_oop / classes.py
Topic: Classes, Constructors (__init__), `self` vs `this`, and Method Types

================================================================================
OOP FOUNDATION FOR JAVASCRIPT DEVELOPERS:
================================================================================
What is Object-Oriented Programming (OOP)?
- A Class is a BLUEPRINT (like an architectural schematic for a building).
- An Object / Instance is the ACTUAL BUILDING created from that blueprint.

JAVASCRIPT ES6 CLASS vs PYTHON CLASS:
-------------------------------------
JavaScript:
    class User {
        constructor(name, email) {
            this.name = name;      // 'this' is implicit
            this.email = email;
        }
        greet() {
            console.log(`Hello, ${this.name}`);
        }
    }
    const u = new User("Alice", "alice@example.com"); // requires 'new' keyword

Python:
    class User:
        def __init__(self, name: str, email: str):
            self.name = name       // 'self' must be explicit!
            self.email = email
            
        def greet(self):           // 'self' passed explicitly as 1st arg!
            print(f"Hello, {self.name}")

    u = User("Alice", "alice@example.com") // NO 'new' keyword!

THE BIG MYSTERY: WHAT IS `self` AND WHY IS IT EVERYWHERE?
---------------------------------------------------------
In JS:
    `this` is magically provided by the runtime. BUT `this` in JS is notorious
    for losing its context when passed as a callback (requiring .bind(this) or arrow functions).
In Python:
    "Explicit is better than implicit" (The Zen of Python).
    `self` is simply a reference to the specific instance calling the method.
    When you write:
        my_user.greet()
    Python internally translates that to:
        User.greet(my_user)
    That is why `self` must be written as the first parameter in instance methods!
"""

class BankAccount:
    # --------------------------------------------------------------------------
    # 1. Class Attributes (Shared by ALL instances - like static properties in JS)
    # --------------------------------------------------------------------------
    # JS: static bankName = "Global Federal";
    bank_name = "Global Federal"
    total_accounts_created = 0

    # --------------------------------------------------------------------------
    # 2. Constructor: __init__
    # --------------------------------------------------------------------------
    # Equivalent to `constructor(...)` in JS:
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        # Instance attributes (Unique to each individual bank account):
        # JS: this.accountHolder = accountHolder;
        self.account_holder = account_holder
        self.balance = initial_balance
        
        # Modifying class attribute on the Class:
        BankAccount.total_accounts_created += 1

    # --------------------------------------------------------------------------
    # 3. Instance Method (Operates on `self`, the specific account instance)
    # --------------------------------------------------------------------------
    # JS: deposit(amount) { this.balance += amount; }
    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self.balance += amount
        print(f"[{self.account_holder}] Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")
        return self.balance

    def withdraw(self, amount: float) -> float:
        if amount > self.balance:
            raise ValueError("Insufficient funds!")
        self.balance -= amount
        print(f"[{self.account_holder}] Withdrew ${amount:.2f}. Remaining Balance: ${self.balance:.2f}")
        return self.balance

    # --------------------------------------------------------------------------
    # 4. Class Method (@classmethod) - Receives `cls` instead of `self`
    # --------------------------------------------------------------------------
    # In JS: Often used as factory functions on static classes:
    #   static createWithBonus(holder, bonus) { return new BankAccount(holder, bonus * 1.1); }
    @classmethod
    def create_with_welcome_bonus(cls, account_holder: str):
        """Alternative constructor creating an account with a $50 welcome bonus."""
        # `cls` is the BankAccount class itself! Calling cls(...) creates an instance:
        return cls(account_holder, initial_balance=50.0)

    # --------------------------------------------------------------------------
    # 5. Static Method (@staticmethod) - Pure utility bound to the class namespace
    # --------------------------------------------------------------------------
    # JS: static isValidAccountNumber(num) { return num.length === 10; }
    # Receives NEITHER `self` NOR `cls`. Just a regular function that lives in the class:
    @staticmethod
    def is_valid_currency(currency_code: str) -> bool:
        return currency_code.upper() in {"USD", "EUR", "GBP", "PKR", "JPY"}


# ==============================================================================
# DEMONSTRATION & PRACTICE
# ==============================================================================
# Notice: In Python, you DO NOT use the `new` keyword! Just call the class like a function:
# JS: const acc1 = new BankAccount("Alice", 500.0);
acc1 = BankAccount("Alice", 500.0)
acc2 = BankAccount("Bob", 200.0)

# Calling instance methods:
acc1.deposit(150.0)
acc1.withdraw(50.0)

# Alternative constructor via @classmethod:
acc3 = BankAccount.create_with_welcome_bonus("Charlie")
print(f"Charlie's bonus account balance: ${acc3.balance}")

# Accessing class attribute:
print(f"Total bank accounts created: {BankAccount.total_accounts_created}")

# Calling static method:
print("Is EUR valid currency?:", BankAccount.is_valid_currency("EUR"))
print("Is XYZ valid currency?:", BankAccount.is_valid_currency("XYZ"))
