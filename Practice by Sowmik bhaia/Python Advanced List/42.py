a = [3, 7, 3, 5, 9, 7, 3, 2, 5, 9, 7, 3, 2, 9, 5, 7, 2, 3, 9, 5]
i = 0
target = a[i]
index = []
for i in range(len(a)):
    if a[i] == target:
        index.append(i)
print(index)

"""
lst = [1, 2, 3, 2, 4, 1, 2, 5]
index_dict = {}
for i, value in enumerate(lst): #enumerate accounts for both index and value of the list element
    if value not in index_dict:
        index_dict[value] = []
    index_dict[value].append(i)
print(index_dict)
"""
