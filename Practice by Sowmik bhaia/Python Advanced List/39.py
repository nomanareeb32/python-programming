lst = [1, 2, 3, 4, 5]
result = []
for x in lst:
    result.append(x)
    result.append(x)

"""
result = [x for x in lst for _ in range(2)]
"""
print(result)