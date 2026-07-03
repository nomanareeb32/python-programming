import random
lst = [random.randint(1,100) for j in range(20)]
print(lst)
for i in lst:
    if i > 50:
        lst.remove(i)
print(lst)