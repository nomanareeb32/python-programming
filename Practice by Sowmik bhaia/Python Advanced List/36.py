a = [3, 7, 12, 19, 5, 24, 8]
b = [6, 12, 3, 45, 19, 11, 27]
c = [19, 3, 55, 12, 8, 31, 7]
for i in a:
    for j in b:
        for k in c:
            if i == j == k:
                print(i, end=", ")
"""
for i in a:
    if i in b and i in c:
    print(i, end=", ")
"""

"""
result = list(set(a) & set(b) & set(c))
print(result)
"""