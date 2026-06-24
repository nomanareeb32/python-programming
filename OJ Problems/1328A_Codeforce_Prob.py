n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    f = a % b
    m = b - f
    print(m % b)
