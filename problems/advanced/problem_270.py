"""
Problem 270: Stock ReportGenerator
Error Type: LOGICAL
Difficulty: Advanced
"""


class StockReport:
    def __init__(self, data):
        self.data = data
        

    def generate(self):
        report = "REPORT"
        for i in len(self.data):
            report += str(self.data[i])
        return report


r = StockReport([1, 2, 3])
print(r.generate())
