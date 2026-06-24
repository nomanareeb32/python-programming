import math

a = int(input())
ans = {}
for i in range(2, int(math.sqrt(a))+1):
    if a % i == 0:
        count = 0
        while a % i == 0:
            count += 1
            a /= i
            ans[i] = count
print(ans)
