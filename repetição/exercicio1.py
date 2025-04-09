soma = 0
repeticao = 0
vezes = int(input("Quantas vezes quer informar o valor: "))
while repeticao < vezes:
    val = int(input("Digite um valor: "))
    soma += val
    repeticao += 1


print(f"a soma de todos os valores é {soma}")