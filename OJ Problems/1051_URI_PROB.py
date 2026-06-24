sal = float(input())

if 0 < sal <= 2000:
    print(f"Isento")
elif 2000 < sal <= 3000:
    resto = sal - 2000
    resultado = resto * 0.08
    print(f"R$ {resultado:0.2f}")
elif 3000 < sal < 4500:
    resto = sal - 3000
    resultado = (resto * 0.18) + (1000 * 0.08)
    print(f"R$ {resultado:0.2f}")
else:
    resto = sal - 4500
    resultado = (resto * 0.28) + (1500 * 0.18) + (1000 * 0.08)
    print(f"R$ {resultado:0.2f}")
