positivos = 0
soma = 0
for c in range(1,7):
    num = int(float(input(f"número {c}: ")))

    if num > 0:
        soma += num
        positivos += 1
        media = soma / positivos

print(f"Valores positivos: {positivos}")
print(f"Média: {media:.1f}")