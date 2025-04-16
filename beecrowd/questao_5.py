horario = int(input("Hora da corrida: "))
distancia = float(input("Distancia da corrida: "))
min = horario * 60

if min >= 360 and min <= 1320:
    fixa = 4.00
    preco_km = 2.50

elif min > 1320 or min < 360:
    fixa = 6.00
    preco_km = 3.50

else:
    fixa = 0.00
    preco_km = 0.00

valor_total = fixa + (preco_km * distancia)


print(f"O valor a ser cobrado é: R$ {valor_total:.2f}")