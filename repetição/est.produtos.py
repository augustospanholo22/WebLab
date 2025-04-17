soma = 0
cont_1000 = 0
menor = cont = 0
barato = " "
while True:
    nome = str(input("Nome do produto: ")) .strip()
    preco = int(input("Preço: R$ "))
    cont += 1
    soma += preco
    if preco > 1000:
        cont_1000 += 1
    
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome

    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Quer continuar? [S/N] ")).upper() .strip() [0]
    if resposta == "N":
        break

print(f"O total da compra foi R${soma}")
print(f"Temos {cont_1000} produtos custando mais do que R$1000.00")
print(f"O produto mais barato foi {barato} que custa {menor:.2f}")
