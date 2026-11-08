a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prod = 1
for i in range(1, len(a), 2):
    prod *= a[i]
print(prod)