"""
Problem 183: BMI Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_bmi(val):
    #    return True

    if val > 10:
        return 'High'
    if val > 5:
        return 'Medium'
    return 'Low' 
    
print(check_bmi(20))