"""
Problem 190: Age Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_age(val):
    #    return True

    if val > 10:
        return 'High'
    if val > 5:
        return 'Medium'
    return 'Low' 
    
print(check_age(20))