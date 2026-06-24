list = [1,2,3,4,5,6,7,8,9,10]
for i in range(0, len(list)):
    if list[i] % 2 != 0:
        list[i] = 0
print(list)