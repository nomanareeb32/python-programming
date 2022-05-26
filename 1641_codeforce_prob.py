from collections import defaultdict

l = int(input())
for i in range(l):
    n, x = map(int, input().split())
    noli = list(sorted(map(int, input().split()), reverse=False))
    # d = defaultdict(int)
    # for j in noli:
    #     if d[j]:
    #         d[j] -= 1
    #     else:
    #         d[j * x] += 1
    #
    # t = sum(d.values())
    # print(t)
    print(noli)
