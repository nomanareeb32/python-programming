def sum(n):
    if n == 0:
        return -1
    print(sum(n-1))
    return n


print(sum(3))
