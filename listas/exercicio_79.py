valores = []
while True:
    n = int(input("Digite um valor: "))
    if n not in valores:
        valores.append(n)
        print(f"Valor adicionado com sucesso!")
    else:
        print(f"Valor duplicado, não vou adicionar...")
    cont = str(input("Quer continuar?[S/N] ")).upper()
    if cont == "N":
        break
    else:
        continue

print("-=" * 30)
valores.sort()
print(f"Os valores digitados foram: {valores}")