dia = 90
kmv = 0.20
dias = int(input("Quantos dias ficou com o carro? "))
km = int(input("Informe a quilometragem rodada: "))

dia *= dias
kmv *= km
val = dia + kmv

if dias > 7:
    val *= 0.15

print(f"Valor a pagar: R$ {val}")