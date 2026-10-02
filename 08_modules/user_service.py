# Example service class
class UserService:
    def __init__(self):
        self.users = []

    def add_user(self, name: str):
        self.users.append(name)
        return self.users

    def get_users(self):
        return self.users
