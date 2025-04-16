num = int(input("Digite um número: "))
contador = num
fatorial = 1
while contador > 0:
    print(contador, end=" ")
    fatorial *= contador
    contador -= 1
print(f"\nO fatorial de {num} é {fatorial}")  