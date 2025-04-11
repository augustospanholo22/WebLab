nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))

if nota1 < 0 or nota1 >10 or nota2 < 0 or nota2 > 10 or nota3 <0 or nota3 > 10 or nota4 < 0 or nota4 >10:
    print("NOTA INVÁLIDA")
    exit()

peso1 = nota1 * 0.2
peso2 = nota2 * 0.3
peso3 = nota3 * 0.4
peso4 = nota4 * 0.1

media = (peso1 + peso2 + peso3 + peso4)
print(f"Media = {media:.1f}")

if media >5 and media <7:
    print("Aluno em exame.")
    nota_exame = float(input("Nota do exame: "))
    nova_media = (media + nota_exame) / 2

    if nota_exame >10 or nota_exame < 0:
        print("Nota Invalida")
        exit()

    if nova_media >= 5:
            print("Aluno aprovado.")
    elif nova_media < 5:
            print("Aluno reprovado.")

    print(f"Media final = {nova_media}")

if media >= 7:
    print("Aluno aprovado.")

elif media <5:
    print("Aluno reprovado.")

