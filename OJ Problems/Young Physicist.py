a = int(input())
tx, ty, tz = 0, 0, 0
for i in range(a):
    x, y, z = map(int, input().split())
    tx += x
    ty += y
    tz += z
if tx == ty == tz == 0:
    print("YES")
else:
    print("NO")
