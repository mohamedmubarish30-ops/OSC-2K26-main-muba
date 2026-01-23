"""
Problem 228: Airline ReportGenerator
Error Type: LOGICAL
Difficulty: Advanced
"""


class AirlineReport:
    def __init__(self, data):
        self.data = data
        

    def generate(self):
        report = "REPORT"
        for i in len(self.data):
            report += str(self.data[i])
        return report


r = AirlineReport([1, 2, 3])
print(r.generate())
