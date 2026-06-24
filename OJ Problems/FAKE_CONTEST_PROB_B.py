n = int(input())
a = list(map(int, input().split()))
b = ''
for i in range(len(a)):
    if a[i] % 2 == 0:
        b = b + "0"
    else:
        b = b + "1"
    if i != (len(a) - 1):
        b = b + " "
print(b)
