lst = [1, 2, 3, 2, 4, 1, 5, 3]
result = []
for x in lst:
    if x not in result:
        result.append(x)
    else:
        print(x)