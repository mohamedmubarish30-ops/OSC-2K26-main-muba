"""
Problem 148: Tax Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_tax(val):
    #    return True

    if val > 10:
        return 'High'
    if val > 5:
        return 'Medium'
    return 'Low' 
    
print(check_tax(20))