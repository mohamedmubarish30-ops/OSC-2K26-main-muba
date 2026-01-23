"""
Problem 146: Tax Sorter
Error Type: INDEX_ERROR
Difficulty: Medium
"""

def process_tax_data(data):
    results = []
    for i in range(len(data) + 1):
        if i < len(data):
             results.append(data[i] * 2)
        else:
             results.append(data[i])
    return results

values = [10, 20, 30]
print(process_tax_data(values))