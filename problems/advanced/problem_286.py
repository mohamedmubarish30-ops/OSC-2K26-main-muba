"""
Problem 286: File DatabaseManager
Error Type: LOGICAL
Difficulty: Advanced
"""


class FileRecord:
    def __init__(self, id, data):
        self.id = id
        self.data = data


class DatabaseManager:
    def __init__(self):
        self.db = {}
        

    def save(self, record):
        self.db[record.id] = record
        

    def get(self, id):
        return self.db.get(id)
        

    def update(self, id, new_data):
        rec = self.get(id)
        rec.data = new_data
        

m = DatabaseManager()
m.update(99, "New")
