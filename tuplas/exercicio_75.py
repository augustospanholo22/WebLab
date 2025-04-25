num = (int(input("Digite um valor: ")),
       int(input("Digite um valor: ")),
       int(input("Digite um valor: ")),
       int(input("Digite um valor: ")),)
print(f"Voce digitou os valores {num}")
print(f"O valor 9 apareceu {num.count(9)} vez(es)")
if 3 in num:
    print(f"O valor 3 apareceu na posição {num.index(3)+1}")
else:
    print(f"O numero 3 nao foi digitado")
print(f"Os valores pares digitados foram: ", end="")
for n in num:
    if n % 2 ==0:
        print(n,end=" ")
