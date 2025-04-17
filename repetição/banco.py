val = int(input("Quantos reais voce quer sacar? R$"))

total = val
cedula = 50
tot_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        tot_cedula += 1
    else:
        if tot_cedula >0:
            print(f"Voce sacou {tot_cedula} cedulas de R${cedula}")

        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        tot_cedula = 0
        if total == 0:
            break