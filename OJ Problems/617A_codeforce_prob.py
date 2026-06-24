x = int(input())
count = 0
i = 0
while i < x:
    if x - 5 >= 0:
        count += 1
        i += 5
    elif x - 4 >= 0:
        count += 1
        i += 4
    elif x - 3 >= 0:
        count += 1
        i += 3
    elif x - 2 >= 0:
        count += 1
        i += 2
    elif x - 1 >= 0:
        count += 1
        i += 1
print(count)
