# In JS: class UserNotFoundError extends Error { ... }
# In Python: Inherit from Exception

class UserNotFoundError(Exception):
    def __init__(self, user_id: int):
        super().__init__(f"User with ID {user_id} not found.")
        self.user_id = user_id

def find_user(user_id: int):
    users = {1: "Alice", 2: "Bob"}
    if user_id not in users:
        # In JS: throw new UserNotFoundError(user_id);
        raise UserNotFoundError(user_id)
    return users[user_id]

try:
    find_user(99)
except UserNotFoundError as err:
    print(f"Caught custom error: {err} (User ID: {err.user_id})")
