hora_inicial = int(input("Hora inicial: "))
hora_final = int(input("Hora final: "))

minuto_inicial = hora_inicial *60
minuto_final = hora_final * 60

if minuto_final <= minuto_inicial:
    minuto_final += 24 * 60

duracao = minuto_final - minuto_inicial
horas = duracao // 60

print(f"\nO jogo durou {horas} horas")