novo = 0
hora_inicial = int(input("Hora de inicio: "))
minuto_inicial = int(input("Minuto inicial: "))
hora_final = int(input("Hora final: "))
minuto_final = int(input("Minuto final: "))

calc_h = hora_final - hora_inicial
calc_m = (minuto_final - minuto_inicial)

if calc_m < 0 and calc_h < 1:
    novo += calc_m

print(f"O jogo durou {calc_h} hora(s) e {novo} minuto(s)")
