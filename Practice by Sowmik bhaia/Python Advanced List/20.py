a = [4, 4, 4, 9, 2, 9, 4, 7, 2, 9, 4, 2, 7, 9, 4, 2, 2, 7, 9, 4, 9, 2, 4, 7, 2, 9, 4, 7, 9, 2, 4, 2, 9, 7, 4]
b = {x: a.count(x) for x in a} #Dict comprehension
print(b)