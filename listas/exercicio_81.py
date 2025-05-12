lista = []
while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    cont = str(input("Quer continuar?[S/N] ")).upper()
    if cont =="N":
        break


print("-=" * 30)
print(f"Você digitou {len(lista)} elementos" )
lista.sort(reverse=True)
print(f"Os valores em ordem decrescente são {lista}")
if 5 in lista:
        print(f"O valor 5 faz parte da lista")
else:
        print(f"O valor 5, não faz parte da lista")
