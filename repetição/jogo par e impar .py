from random import randint
p_i = "P/I"
v = 0
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
while True:
    jogador = int(input("Diga um valor: "))
    p_i = str(input("Par ou Impar? [P/I] ")).upper()
    print("--------------------------------------------------------------------------------")

    computador = randint(0,11)
    total = jogador + computador
    print(f"Voce = {jogador} \ncomputador = {computador} \nTotal = {total}")
    print("--------------------------------------------------------------------------------")

    if total % 2 == 0 and p_i == "P":
        v += 1
        print(f"Voce VENCEU!")
        print(f"Vamos jogar novamente")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    elif total % 2 != 0 and p_i == "I":
        v += 1
        print(f"Voce VENCEU!")
        print(f"Vamos jogar novamente")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    else:
        print(f"Voce PERDEU")
        break
print(f"GAME OVER! Voce venceu {v} vezes")