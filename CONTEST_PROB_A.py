a = int(input())
b = int(input())
c = input()
if b == len(c):
    for z in range(a):
        c = list(c)
        d = 0
        count = 0
        for i in range(len(c)):
            if c.remove(c[d]) == c.reverse():
                count += 1
                d += 1
            elif c.remove(c[d]) != c.reverse():
                d += 1
        print(count)
