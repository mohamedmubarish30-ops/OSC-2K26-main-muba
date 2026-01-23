"""
Problem 141: Score Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_score(val):
    #    return True

    if val > 10:
        return 'High'
    if val > 5:
        return 'Medium'
    return 'Low' 
    
print(check_score(20))