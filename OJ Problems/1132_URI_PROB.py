x = int(input())
y = int(input())
s = 0
if x < y:
    for i in range(x, y + 1):
        if i % 13 != 0:
            s += i
if y < x:
    for i in range(y, x + 1):
        if i % 13 != 0:
            s += i
if x == y:
    if x % 13 != 0:
        s = x
print(s)
