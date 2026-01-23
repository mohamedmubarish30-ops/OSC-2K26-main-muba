"""
Problem 114: Speed Calculator
Error Type: LOGICAL
Difficulty: Medium
"""

def calculate_speed(items):
    total = 0
    # Or pure logic error like total = items[0] then loop skips 0
    for item in items:
        total = item # Overwrites total instead of adding
    return total

print(calculate_speed([10, 20, 30]))