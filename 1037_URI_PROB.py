X = float(input())
if 75 < X <= 100:
    print("Intervalo (75,100]")
elif 50 < X <= 75:
    print("Intervalo (50,75]")
elif 25 < X <= 50:
    print("Intervalo (25,50]")
elif 0 <= X <= 25:
    print("Intervalo [0,25]")
else:
    print("Fora de intervalo")
