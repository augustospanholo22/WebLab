valores = []
mai = men = 0
for v in range(0,5):
    valores.append(int(input(f"Digite o valor na posição {v}: ")))

    if v == 0:
        mai = men = valores[v]
    else:
        if valores[v] > mai:
            mai = valores[v]
        if valores[v] < men:
            men = valores[v] 

print(f"Você digitou os valores: {valores}")

print(f"O menor valor digitado foi {men} nas posições ", end="")
for i, c in enumerate(valores):
    if c == men:
        print(f"{i}...", end="")
print()

print(f"O maior valor digitado foi {mai} nas posições ", end="")
for i, c in enumerate(valores):
    if c == mai:
        print(f"{i}... ", end="")
print()


