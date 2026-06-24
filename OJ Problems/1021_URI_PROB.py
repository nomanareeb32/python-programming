N = float(input())
notes = [100, 50, 20, 10, 5, 2]
coins = [100, 50, 25, 10, 5, 1]
print("NOTAS:")
for notas in notes:
    temp = N//notas
    N %= notas
    print(f"{int(temp)} nota(s) de R$ {notas}.00")
N *= 100
print(f"MOEDAS:")
for notas in coins:
    temp = N//notas
    N %= notas
    print("%d moeda(s) de R$ %1.2f" % (temp, notas/100))
