"""
Problem 64: Grade Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_grade(val):
    #    return True

    if val > 10:
        return 'High'
    if val > 5:
        return 'Medium'
    return 'Low' 
    
print(check_grade(20))