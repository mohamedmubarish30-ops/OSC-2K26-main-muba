"""
Problem 209: Hospital NotificationService
Error Type: LOGICAL
Difficulty: Advanced
"""


class HospitalUser:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class NotificationService:
    def __init__(self):
        self.users = []
        self.logs = []


    def add_user(self, user):
        self.users.append(user)
        self.log_action(f"Added {user.username}")
    def log_action(self, msg):
        self.logs.append(msg)


sys = NotificationService()
u = HospitalUser("Alice", "Admin")
sys.add_user(u)
