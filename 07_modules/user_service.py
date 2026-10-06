"""
=====================================================================
TOPIC: Modules - A Small Service Module (user_service)
=====================================================================

SCENARIO
--------
Your app needs ONE place that knows the signed-up users. Other files
should not build their own user lists in secret; they import
UserService and ask it to add or list users.

TOPIC
-----
- A module can hold a CLASS, not just functions - importing is identical.
- self._users: the leading underscore means "internal, please do not
  touch from outside" (a convention, not enforced by Python).
- get_users returns a COPY of the list, so callers can change their
  copy without silently corrupting the service's real data.

Questions live in main.py - run: cd 07_modules && python main.py
Answers: answers/07_modules.py
=====================================================================
"""

# ------------------------------------------------------------------
# MODULE CODE (imported by main.py)
# ------------------------------------------------------------------

class UserService:
    def __init__(self):
        self._users: list[str] = []          # internal state

    def add_user(self, name: str) -> bool:
        """Add a user; return False (adding nothing) for duplicates."""
        if name in self._users:
            return False
        self._users.append(name)
        return True

    def get_users(self) -> list[str]:
        # list(...) makes a shallow copy - caller changes never leak back in.
        return list(self._users)


# ------------------------------------------------------------------
# SELF-TEST - runs ONLY via "python user_service.py", never on import
# ------------------------------------------------------------------
if __name__ == "__main__":
    print("Running user_service self-tests...")
    service = UserService()
    assert service.add_user("Alice") is True
    assert service.add_user("Alice") is False    # duplicate rejected
    assert service.get_users() == ["Alice"]
    print("All user_service tests passed.")
