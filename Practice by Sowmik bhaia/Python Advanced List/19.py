"""
a_list = [12, 5, 12, 33, 5, 47, 12, 9, 33, 5]
a_list.remove(12)
print(a_list)
"""

a = [12, 5, 12, 33, 5, 47, 12, 9, 33, 5]
b = [12, 5]
empty = []
for i in a:
    if i not in b:
        empty.append(i)
print(empty)