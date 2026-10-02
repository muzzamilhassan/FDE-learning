"""
06_oop / inheritance.py
Topic: Inheritance, super(), Method Overriding, Polymorphism, and Multiple Inheritance

================================================================================
OOP INHERITANCE EXPLAINED FOR JAVASCRIPT DEVELOPERS:
================================================================================
What is Inheritance?
- The "IS-A" relationship: A `Developer` IS AN `Employee`. A `Dog` IS AN `Animal`.
- Child (subclass) inherits attributes and methods from Parent (superclass).

JAVASCRIPT vs PYTHON INHERITANCE:
---------------------------------
JavaScript:
    class Employee { ... }
    class Developer extends Employee {
        constructor(name, salary, techStack) {
            super(name, salary); // must call super before using `this`
            this.techStack = techStack;
        }
    }

Python:
    class Employee: ...
    class Developer(Employee):   # Parent class in parentheses!
        def __init__(self, name: str, salary: float, tech_stack: list[str]):
            super().__init__(name, salary)
            self.tech_stack = tech_stack

MULTIPLE INHERITANCE (PYTHON SUPERPOWER vs JS PROTOTYPE LIMITATION):
--------------------------------------------------------------------
In JS: A class can ONLY extend ONE parent class (`extends A, B` is illegal).
In Python: Multiple inheritance is natively supported: `class Child(ParentA, ParentB):`.
Python uses MRO (Method Resolution Order) to determine which parent method to call.
"""

# ------------------------------------------------------------------------------
# 1. Base Class (Parent)
# ------------------------------------------------------------------------------
class Employee:
    def __init__(self, name: str, emp_id: str, base_salary: float):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def calculate_annual_pay(self) -> float:
        """Base calculation: 12 months of base salary."""
        return self.base_salary * 12

    def get_role_description(self) -> str:
        return f"Employee [{self.emp_id}]: {self.name}"


# ------------------------------------------------------------------------------
# 2. Subclass: Developer (Child extending Employee)
# ------------------------------------------------------------------------------
# Python syntax for inheritance: class ChildClass(ParentClass):
class Developer(Employee):
    def __init__(self, name: str, emp_id: str, base_salary: float, tech_stack: list[str]):
        # JS: super(name, emp_id, base_salary);
        super().__init__(name, emp_id, base_salary)
        self.tech_stack = tech_stack

    # Method Overriding (Replacing or augmenting parent method)
    def get_role_description(self) -> str:
        # Call the parent's version of get_role_description using super():
        parent_desc = super().get_role_description()
        return f"{parent_desc} (Dev Stack: {', '.join(self.tech_stack)})"


# ------------------------------------------------------------------------------
# 3. Subclass: Manager (Another Child extending Employee)
# ------------------------------------------------------------------------------
class Manager(Employee):
    def __init__(self, name: str, emp_id: str, base_salary: float, annual_bonus: float):
        super().__init__(name, emp_id, base_salary)
        self.annual_bonus = annual_bonus

    # Override calculate_annual_pay to add bonus:
    def calculate_annual_pay(self) -> float:
        return super().calculate_annual_pay() + self.annual_bonus


# ------------------------------------------------------------------------------
# 4. Polymorphism in Action
# ------------------------------------------------------------------------------
# Polymorphism means "many forms". Different classes share the same method names,
# allowing us to treat them uniformly:
team: list[Employee] = [
    Developer("Sarah", "DEV-01", 8000, ["Python", "PostgreSQL", "Docker"]),
    Developer("Alex", "DEV-02", 7500, ["TypeScript", "React", "Node.js"]),
    Manager("David", "MGR-01", 10000, annual_bonus=15000),
]

print("=== Payroll Report (Polymorphism Demo) ===")
for member in team:
    # Each object executes ITS OWN version of calculate_annual_pay and get_role_description:
    print(f"{member.get_role_description()} -> Annual: ${member.calculate_annual_pay():,.2f}")


# ------------------------------------------------------------------------------
# 5. Type Checking: isinstance() and issubclass()
# ------------------------------------------------------------------------------
# JS: member instanceof Developer
dev = team[0]
print("\nIs Sarah a Developer?:", isinstance(dev, Developer))
print("Is Sarah also an Employee?:", isinstance(dev, Employee))
print("Is Developer a subclass of Employee?:", issubclass(Developer, Employee))
