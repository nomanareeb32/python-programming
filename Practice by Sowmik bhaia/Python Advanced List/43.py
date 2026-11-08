import math
a = [1,2,3,4,5,6,7,8,9,10]
b = []
for i in a:
    b.append(math.factorial(i))

"""
for i in a:
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    b.append(factorial)
"""

print(b)