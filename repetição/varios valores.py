soma = 0
n = 0
contador = 0
while True:
    n = int(input("Digite um número [999 para parar]: "))
    if n == 999:
        break
    soma += n
    contador += 1
    
print(f"A soma dos {contador} numeros é: {soma}")
    
