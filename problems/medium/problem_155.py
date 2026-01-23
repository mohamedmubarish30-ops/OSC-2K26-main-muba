"""
Problem 155: Loan Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_loan(val):
    #    return True

    if val > 10:
        return 'High'
    if val > 5:
        return 'Medium'
    return 'Low' 
    
print(check_loan(20))