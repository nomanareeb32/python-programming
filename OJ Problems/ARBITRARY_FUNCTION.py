def add(*nums):
    s = 0
    for i in nums:
        s = s + i
    return s


c = add(2, 3, 4, 5, 6)
print(c)
