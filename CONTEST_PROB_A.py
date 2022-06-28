n, q = map(int, input().split())
a = []
for i in range(1, n + 1):
    a.append(i)


def coPrime(num):
    count = 1
    for i in range(2, num):
        if num % i != 0:
            count += 1
    return count


f = []
for i in a:
    t = coPrime(i)
    f.append(t)

for i in range(q):
    l, r = map(int, input().split())

    max = f[l - 1]
    for i in range(l, r):
        if f[i] > max:
            max = f[i]
    print(max)
