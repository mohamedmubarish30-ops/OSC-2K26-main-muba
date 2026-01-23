"""
Problem 127: Fuel Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_fuel(val):
    #    return True

    if val > 10:
        return 'High'
    if val > 5:
        return 'Medium'
    return 'Low' 
    
print(check_fuel(20))