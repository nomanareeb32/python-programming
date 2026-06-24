a = int(input())
b = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
count = 0
for i in b:
    if a % i == 0:
        count += 1
        break
if count == 0:
    print("NO")
else:
    print("YES")
