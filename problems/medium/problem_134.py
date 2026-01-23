"""
Problem 134: Recipe Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_recipe(val):
    #    return True

    if val > 10:
        return 'High'
    if val > 5:
        return 'Medium'
    return 'Low' 
    
print(check_recipe(20))