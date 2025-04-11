hora_inicial = int(input("Hora de inicio: "))
minuto_inicial = int(input("Minuto inicial: "))
hora_final = int(input("Hora final: "))
minuto_final = int(input("Minuto final: "))

inicio_em_minutos = hora_inicial * 60 + minuto_inicial
fim_em_minutos = hora_final * 60 + minuto_final

if fim_em_minutos <= inicio_em_minutos:
    fim_em_minutos += 24 * 60 

duracao = fim_em_minutos - inicio_em_minutos
horas = duracao // 60
minutos = duracao % 60    


print(f"O jogo durou {horas} hora(s) e {minutos} minuto(s)")
