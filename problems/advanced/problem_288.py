"""
Problem 288: File ReportGenerator
Error Type: LOGICAL
Difficulty: Advanced
"""


class FileReport:
    def __init__(self, data):
        self.data = data
        

    def generate(self):
        report = "REPORT
"
        for i in len(self.data):
            report += str(self.data[i])
        return report


r = FileReport([1, 2, 3])
print(r.generate())
