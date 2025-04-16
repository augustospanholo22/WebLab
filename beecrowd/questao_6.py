hora_trabalhadas = int(input("Horas trabalhadas: "))

if hora_trabalhadas <= 160:
    salario = hora_trabalhadas * 20


elif hora_trabalhadas > 160 and hora_trabalhadas <= 200:
    horas_extras = hora_trabalhadas - 160
    salario = (160 * 20) + (horas_extras * 30)

else:
    horas_extras = hora_trabalhadas - 160
    extra_50 = 40
    extra_100 = horas_extras - 40

    salario = (160 * 20) + (extra_50 * 30) + (extra_100 * 40)

print(f"Salario: {salario}")
    