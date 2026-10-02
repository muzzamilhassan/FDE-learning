"""
08_modules / main.py
Topic: Module Importing and Application Entry Point

JAVASCRIPT vs PYTHON IMPORTS:
-----------------------------
JS (ES Modules):
    import { add, multiply } from './math_utils.js';
    import { UserService } from './user_service.js';

Python:
    from math_utils import add, multiply
    from user_service import UserService
"""
from math_utils import add, multiply
from user_service import UserService

def main():
    print("=== Modular Application Execution ===")
    
    # 1. Using functions imported from math_utils
    calc = multiply(add(10, 15), 2)
    print(f"Imported math calculation: (10 + 15) * 2 = {calc}")

    # 2. Using UserService imported from user_service
    service = UserService()
    service.register_user(1, "alex_dev", "alex@code.io")
    service.register_user(2, "sarah_q", "sarah@code.io")

    print("Registered users:", service.list_users())

# Standard Python entrypoint guard:
if __name__ == "__main__":
    main()
