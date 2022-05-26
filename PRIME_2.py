import math


def isPrime(s):
    is_pr = True
    for i in range(2, int(math.sqrt(s))):
        if s % i == 0:
            is_pr = False
            break
    return is_pr


s = int(input())
if isPrime(s):
    print('IT IS A PRIME NUMBER')
else:
    print('IT IS NOT A PRIME NUMBER')
