x = int(input())
y = int(input())
s = 0
for i in range(x, y + 1):
    if i % 13 != 0:
        s += i
print(s)
