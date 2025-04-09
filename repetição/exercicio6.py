# Variáveis de controle
soma_par = 0
soma_impar = 0
cont_par = 0
cont_impar = 0

while True:
    val = int(input("Digite um número: "))

    # Finaliza a sequência e mostra média, mas continua
    if val == -1:
        if cont_par > 0:
            media_par = soma_par / cont_par
        else:
            media_par = 0

        if cont_impar > 0:
            media_impar = soma_impar / cont_impar
        else:
            media_impar = 0

        print(f"MP = {int(media_par)} MI = {media_impar:.1f}")

        # Reinicia as variáveis para nova sequência
        soma_par = soma_impar = cont_par = cont_impar = 0
        continue

    # Finaliza a sequência e encerra o programa
    if val == -2:
        if cont_par > 0:
            media_par = soma_par / cont_par
        else:
            media_par = 0

        if cont_impar > 0:
            media_impar = soma_impar / cont_impar
        else:
            media_impar = 0

        print(f"MP = {int(media_par)} MI = {media_impar:.1f}")
        break

    # Classificação dos números
    if val % 2 == 0:
        soma_par += val
        cont_par += 1
    else:
        soma_impar += val
        cont_impar += 1




