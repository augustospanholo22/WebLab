estudante = "SIM/NAO"
idade = int(input("Informe a idade: "))
estudante = str(input("Estudante? ")).upper() .strip()

if idade <= 6:
    ingresso = 0

if idade > 6 and idade <60:
    ingresso = 20

else: 
    ingresso = 10

if estudante == "SIM":
        ingresso = 10

print(f"O valor do ingresso é {ingresso}")