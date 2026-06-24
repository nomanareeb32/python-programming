n = list(map(int, input().split()))
for i in range(0, n[1]):
    if n[0] % 10 == 0:
        n[0] = n[0] // 10
    else:
        n[0] = n[0] - 1
print(n[0])
