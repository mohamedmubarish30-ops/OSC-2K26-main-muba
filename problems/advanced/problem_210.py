"""
Problem 210: Hospital ReportGenerator
Error Type: LOGICAL
Difficulty: Advanced
"""


class HospitalReport:
    def __init__(self, data):
        self.data = data
        

    def generate(self):
        report = "REPORT"
        for i in len(self.data):
            report += str(self.data[i])
        return report


r = HospitalReport([1, 2, 3])
print(r.generate())
