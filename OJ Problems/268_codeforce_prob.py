n = int(input())
w = 0
list1 = []
list2 = []
for i in range(n):
    a, b = map(lambda x: int(x), input().split())
    list1.append(a)
    list2.append(b)
for i in list1:
    k = 0
    while k < len(list2):
        if i == list2[k]:
            w += 1
        k += 1
print(w)
