cont_idade = 0
cont_homem = 0
cont_f = 0
while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).upper() .strip()[0]

    if idade >= 18:
        cont_idade += 1

    if sexo == "M":
        cont_homem += 1

    if idade < 20 and sexo == "F":
        cont_f += 1
    
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N] ")).upper() .strip() [0]
    if continuar == "N":
        break

print(f"Total de pessoas com mais de 18 anos: {cont_idade}")
print(f"Ao todo temos {cont_homem} homens cadastrados")
print(f"E temos {cont_f} mulheres com menos de 20 anos")


    