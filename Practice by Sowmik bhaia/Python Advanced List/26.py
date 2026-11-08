lst = [[1, 2], [3, 4], [5, 6]]

flat = []

for sublist in lst:
    for item in sublist:
        flat.append(item)

print(flat)

#Flattens a nested list