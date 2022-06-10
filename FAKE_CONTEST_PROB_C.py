def printDivisors(n):
    i = 1
    w = []
    while i <= n:
        if n % i == 0:
            w.append(i)
        i += 1
    return w


a = int(input())
z = printDivisors(a)
if int(z[0]) < 2:
    print("Never give up")
else:
    print("Well done")
