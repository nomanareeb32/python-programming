lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = []
for x in lst:
    if x not in result:
        result.append(x)
print(result)