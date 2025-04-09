repeticao = 0 
soma = 0
while repeticao < 5:
    num = int(input("Informe um número: "))
    repeticao += 1

    if num %2 !=0:
        soma += 1


        if repeticao == 5:
            break
print(f"Há {soma} números primos")
    