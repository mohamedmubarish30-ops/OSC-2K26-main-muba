"""
Problem 216: Bank ReportGenerator
Error Type: LOGICAL
Difficulty: Advanced
"""


class BankReport:
    def __init__(self, data):
        self.data = data
        

    def generate(self):
        report = "REPORT"
        for i in len(self.data):
            report += str(self.data[i])
        return report


r = BankReport([1, 2, 3])
print(r.generate())
