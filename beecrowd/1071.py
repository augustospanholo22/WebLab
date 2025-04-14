x = int(input("Valor X: "))
y = int(input("Valor Y: "))

if x > y:
    x, y = y, x

soma = 0

for i in range(x + 1, y):
    if i % 2 != 0:
        soma += i

print(f"Soma dos ímpares entre {x} e {y}: {soma}")
