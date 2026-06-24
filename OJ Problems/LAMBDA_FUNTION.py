def func(n):
    return lambda a: a * n


doubler = func(2)  # lambda a:a*2
tripler = func(3)  # lambda a:a*3
print(tripler(10))
print(doubler(10))

(lambda: print('something'))()