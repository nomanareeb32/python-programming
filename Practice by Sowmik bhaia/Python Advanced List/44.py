lst = [4, 5, 2, 10, 8]
result = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[j] > lst[i]:
            result.append(lst[j])
            break

print(result)