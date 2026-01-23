"""
Problem 71: Temperature Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_temperature(val):
    #    return True

    if val > 10:
        return 'High'
    if val > 5:
        return 'Medium'
    return 'Low' 
    
print(check_temperature(20))