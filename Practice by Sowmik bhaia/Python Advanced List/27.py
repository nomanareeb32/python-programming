l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 12, 5, 12, 33, 5, 47, 12, 9, 33, 5]

"""
even = [a for a in l if a % 2 == 0] #list comprehension
odd = [a for a in l if a % 2 != 0] #list comprehension
"""

"""
even = []
odd = []
for i in l:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
"""

print(even)
print(odd)
