lista = input().split(" ")
count = len(lista)
A = int(lista[0])
for i in range(1, count + 1):
    K = int(lista[i])
    if K > 0:
        N = int(lista[i])
        break
T = A + N
Sum = 0
for j in range(A, T):
    Sum = Sum + j
print(Sum)
