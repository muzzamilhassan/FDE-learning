"""
08_modules / user_service.py
Topic: Service Module for User Management
"""

class UserService:
    def __init__(self):
        self._users: dict[int, dict] = {}

    def register_user(self, user_id: int, username: str, email: str) -> dict:
        user = {"id": user_id, "username": username, "email": email}
        self._users[user_id] = user
        return user

    def find_by_id(self, user_id: int) -> dict | None:
        return self._users.get(user_id)

    def list_users(self) -> list[dict]:
        return list(self._users.values())
