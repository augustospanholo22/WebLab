idade = int(input("Informe sua idade: "))
brinquedos = int(input("Informe quantos brinquedos: "))

if idade <= 4:
    entrada = 0
    brinquedos_preco = 5

    if brinquedos < 3:
        val_brinquedos = entrada + (brinquedos * brinquedos_preco)
    if brinquedos >= 3:
        val_brinquedos = entrada + (brinquedos * brinquedos_preco) - brinquedos_preco


elif idade >= 5 and idade <= 12:
    entrada = 15
    brinquedos_preco = 5

    if brinquedos < 3:
        val_brinquedos = entrada + (brinquedos * brinquedos_preco)
    if brinquedos >= 3:
        val_brinquedos = entrada + (brinquedos * brinquedos_preco) - brinquedos_preco



else:
    entrada = 30
    brinquedos_preco = 5

    if brinquedos < 5:
        val_brinquedos = entrada + (brinquedos * brinquedos_preco)
    if brinquedos >= 5:
        val_brinquedos = entrada + (brinquedos * brinquedos_preco) - brinquedos_preco


print(f"Valor a pagar: {val_brinquedos}")