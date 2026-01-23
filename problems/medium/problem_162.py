"""
Problem 162: Interest Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_interest(val):
    #    return True

    if val > 10:
        return 'High'
    if val > 5:
        return 'Medium'
    return 'Low' 
    
print(check_interest(20))