from math import sqrt

a = float(input("Valor de A: "))
b = float(input("Valor de B: "))
c = float(input("Valor de C: "))

delta = b**2 - 4*a*c

if a == 0 or delta < 0:
    print("Impossivel calcular")

else:
    raiz1 = (-b + sqrt(delta)) / (2 * a)
    raiz2 = (-b - sqrt(delta)) / (2 * a)
    print(f"R1 = {raiz1:.5f}")
    print(f"R2 = {raiz2:.5f}")