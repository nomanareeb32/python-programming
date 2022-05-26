import math

n, m, a = map(int, input().split())
# if m % a == 0:
#     r1 = m // a
# else:
#     r1 = m // a + 1
r1 = math.ceil(m/a)
# if n % a == 0:
#     r2 = n // a
# else:
#     r2 = n // a + 1
r2 = math.ceil(n/a)
print(r1 * r2)
