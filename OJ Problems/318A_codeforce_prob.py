n, k = map(int, input().split())
odds = (n + 1) // 2
evens = n // 2
if k <= odds:
    f = k * 2
    j = int(f)
    print(f - 1)
else:
    l = k - odds
    m = int(l)
    print(int(m * 2))
