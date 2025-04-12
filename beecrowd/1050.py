print((("""
DDD     Destination
________________________
61      Brasilia
71      Salvador
11      São paulo
21      Rio de janeiro
32      Juiz de fora
19      Campinas
27      Vitoria
31      Belo Horizonte
""")))

ddd = int(input("Qual é o DDD? "))

if ddd == 61:
    print("Brasilia")

elif ddd == 71:
    print("Salvador")

elif ddd == 11:
    print("São paulo")

elif ddd == 21:
    print("Rio de janeiro")

elif ddd == 32:
    print("Juiz de fora")

elif ddd == 19:
    print("Campinas")

elif ddd == 27:
    print("Vitoria")

elif ddd == 31:
    print("Belo Horizonte")

else:
    print("DDD não cadastrado")