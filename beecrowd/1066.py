par = 0
impar = 0
positivo = 0
negativo = 0

for c in range(1,6):
    val = int(input(f"Valores {c}: "))

    if val % 2 ==0:
        par += 1

    if val % 2 !=0:
        impar += 1

    if val > 0:
        positivo += 1

    if val < 0:
        negativo += 1

print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{positivo} valor(es) positivos(s)")
print(f"{negativo} valor(es) negativo(s)")