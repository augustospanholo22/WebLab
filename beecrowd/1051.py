salario = float(input("Salario: "))

if salario <= 2000:
    print("Isento")
else:
    imposto = 0

    if salario > 2000 and salario <= 3000:
        imposto += (salario - 2000) * 0.08

    elif salario > 3000 and salario <= 4500:
        imposto += (1000) * 0.08
        imposto += (salario - 3000) * 0.18

    else:
        imposto += (1000) * 0.08
        imposto += (1500) * 0.18
        imposto += (salario - 4500) * 0.28

    print(f"O imposto a ser pago é de {imposto:.2f}")