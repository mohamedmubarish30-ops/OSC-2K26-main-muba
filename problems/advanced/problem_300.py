"""
Problem 300: Music ReportGenerator
Error Type: LOGICAL
Difficulty: Advanced
"""


class MusicReport:
    def __init__(self, data):
        self.data = data
        

    def generate(self):
        report = "REPORT
"
        for i in len(self.data):
            report += str(self.data[i])
        return report


r = MusicReport([1, 2, 3])
print(r.generate())
