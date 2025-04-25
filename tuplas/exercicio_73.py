times = ("Flamengo","Palmeiras","Fluminense","Ceará SC","Cruzeiro",
         "Bragantino","Vasco","Juventude","Mirassol","Internacional",
         "Botafogo","Fortaleza","Santos","Corinthias","Vitória","São Paulo",
         "Gremio","Bahia","Atlético-MG","Sport-Recife")
print(f"=-"*15)
print(f"Lista de times do Brasileirão = {times}")
print(f"=-"*15)
print(f"Os primeiros 5 são  {times[0:5]}")
print(f"=-"*15)
print(f"Os 4 últimos são {times[16:]}")
print(f"=-"*15)
print(f"Times em ordem alfabética: {sorted(times)}")
print(f"=-"*15)
print(f"O Gremio esta na posição {times.index("Gremio")+1}")