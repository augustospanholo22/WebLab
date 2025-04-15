hora = int(input("Tempo de estacionamento (h): "))
minuto = int(input("Tempo de estacionamento (min):"))
total_min = hora * 60 + minuto

if total_min <= 120:
    valor = 5.00
    
else:
    extra = total_min - 120
    horas_completas = extra // 60
    min_extras = extra % 60

    valor = 5.00 + (horas_completas * 3.00)

    if min_extras > 0:
        if min_extras <= 30:
            valor += 1.50
        else:
            valor += 3.00
        
print(f"O valor a pagar: R${valor:.2f}")

