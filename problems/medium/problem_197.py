"""
Problem 197: Password Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_password(val):
    #    return True

    if val > 10:
        return 'High'
    if val > 5:
        return 'Medium'
    return 'Low' 
    
print(check_password(20))