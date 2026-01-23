"""
Problem 99: Time Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_time(val):
    #    return True

    if val > 10:
        return 'High'
    if val > 5:
        return 'Medium'
    return 'Low' 
    
print(check_time(20))