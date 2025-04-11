a = int(input("Valor A: "))
b = int(input("Valor B: "))
c = int(input("Valor C: "))
d = int(input("Valor D: "))

if b > c and d > a and c + d > a + b and c >0 and d > 0 and a %2 == 0:
    print("Valores aceitos")
else:
    print("Valores não aceitos")