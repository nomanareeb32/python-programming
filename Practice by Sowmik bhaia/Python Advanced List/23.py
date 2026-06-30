a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [12, 5, 12, 33, 5, 47, 12, 9, 33, 5]

"""
common = []
a = set(a)
b = set(b)
for i in a:
    if i in b and i not in common:
        common.append(i)
print(*common, sep=', ')
"""

"""
a = set(a)
b = set(b)
z = [set(a) & set(b)] #z = list(set(a) & set(b))
print(z)
"""
