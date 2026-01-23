"""
Problem 285: File AuthSystem
Error Type: LOGICAL
Difficulty: Advanced
"""


class FileUser:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class AuthSystem:
    def __init__(self):
        self.users = []
        self.logs = []


    def add_user(self, user):
        self.users.append(user)
        self.log_action(f"Added {user.username}")


    def log_action(self, msg):
        self.logs.append(msg)


sys = AuthSystem()
u = FileUser("Alice", "Admin")
sys.add_user(u)
