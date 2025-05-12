posicao = 0

medidas = int(input("Número de medidas: "))
rpm = list(map(int, input("Rpm (separadas por espaço): ").split()))

for i in range(1, medidas):
    if rpm[i] < rpm[i - 1]:
        posicao = i + 1 
        break 

print(posicao)
