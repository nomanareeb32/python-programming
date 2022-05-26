a = int(input())
for _ in range(a):
    b = int(input())
    c = input()
    count = 0
    for i in range(b):
        temp = c[:i]+c[i+1:]
        if temp == temp[::-1]:
            count += 1
    print(count)
