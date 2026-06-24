T = int(input())
D = 0
while T > 0:
    N = float(input())
    while True:
        N = N / 2
        if N <= 1.00:
            D += 1
            print("%d dias" % D)
            D = 0
            break
        D += 1
    T -= 1
