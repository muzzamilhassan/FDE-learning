# In JS: import { add, multiply } from './math_utils.js';
from math_utils import add, multiply
from user_service import UserService

def main():
    print("Math util add(10, 20):", add(10, 20))
    print("Math util multiply(3, 4):", multiply(3, 4))

    service = UserService()
    service.add_user("Alice")
    service.add_user("Bob")
    print("Users:", service.get_users())

if __name__ == "__main__":
    main()
