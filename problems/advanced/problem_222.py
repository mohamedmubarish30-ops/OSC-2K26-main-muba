"""
Problem 222: School ReportGenerator
Error Type: LOGICAL
Difficulty: Advanced
"""


class SchoolReport:
    def __init__(self, data):
        self.data = data
        

    def generate(self):
        report = "REPORT"


        for i in len(self.data):
            report += str(self.data[i])
        return report


r = SchoolReport([1, 2, 3])
print(r.generate())
