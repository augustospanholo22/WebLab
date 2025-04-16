resposta = "S/N"
contador = soma = maior = menor = 0
while resposta != "N":
    n = int(input("Digite um número: "))
    resposta = str(input("Quer continuar? [S/N] ")) .upper()
    contador += 1
    soma += n 
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    
   
media = soma / contador
print(f"Voce digitou {contador} números e a média foi {media:.2f}")
print(f"O maior valor foi {maior} e o menor foi {menor}")
