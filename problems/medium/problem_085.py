"""
Problem 85: Distance Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_distance(val):
    #    return True

    if val > 10:
        return 'High'
    if val > 5:
        return 'Medium'
    return 'Low' 
    
print(check_distance(20))