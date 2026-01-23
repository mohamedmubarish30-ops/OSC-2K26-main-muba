"""
Problem 107: Steps Calculator
Error Type: LOGICAL
Difficulty: Medium
"""

def calculate_steps(items):
    total = 0
    # Or pure logic error like total = items[0] then loop skips 0
    for item in items:
        total = item # Overwrites total instead of adding
    return total

print(calculate_steps([10, 20, 30]))