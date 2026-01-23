"""
Problem 176: Tip Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_tip(val):
    #    return True

    if val > 10:
        return 'High'
    if val > 5:
        return 'Medium'
    return 'Low' 
    
print(check_tip(20))