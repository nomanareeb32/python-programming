counter = 0
for i in range(int(input())):
    l = list(input().split())
    if l[0] == '1' and l[1] == '1':
        counter += 1
    elif l[0] == '1' and l[2] == '1':
        counter += 1
    elif l[1] == '1' and l[2] == '1':
        counter += 1
print(counter)
