a = [1, 2, 3, 4, 5]
b = ["apple", "banana", "cherry", "date", "elderberry"]
result = list(zip(a, b))

"""
result = []
for i in range(len(a)):
    result.append((a[i], b[i]))
"""

print(result)