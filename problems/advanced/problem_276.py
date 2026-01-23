"""
Problem 276: Social ReportGenerator
Error Type: LOGICAL
Difficulty: Advanced
"""


class SocialReport:
    def __init__(self, data):
        self.data = data
        

    def generate(self):
        report = "REPORT
"
        for i in len(self.data):
            report += str(self.data[i])
        return report


r = SocialReport([1, 2, 3])
print(r.generate())
