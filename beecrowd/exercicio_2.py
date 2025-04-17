val = float(input("Qual é o valor da compra? "))
distancia = float(input("Qual a distancia da entrega (KM): "))

if val > 100:
    frete = 0.00
else:
    if distancia <= 5:
        frete = 5.00
    elif distancia <= 10:
        frete = 10.00
    else:
        frete = 20.00

print(f"O valor do frete fica: R$ {frete:.2f}")