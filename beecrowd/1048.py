salario = float(input("Informe seu salário: "))

if salario > 0 and salario <= 400:
    novo_salario = salario * 1.15 
    print(f"Novo salario: {novo_salario:.2f}")
    reajuste_ganho = salario * 0.15
    print(f"Reajuste ganho: {reajuste_ganho:.0f}")
    percentual = "15%"
    print(f"Em percentual: {percentual}")

elif salario > 400 and salario <= 800:
    novo_salario = salario * 1.12 
    print(f"Novo salario: {novo_salario:.2f}")
    reajuste_ganho = salario * 0.12
    print(f"Reajuste ganho: {reajuste_ganho:.0f}")
    percentual = "12%"
    print(f"Em percentual: {percentual}")

elif salario > 800 and salario <= 1200:
    novo_salario = salario * 1.10 
    print(f"Novo salario: {novo_salario:.2f}")
    reajuste_ganho = salario * 0.10
    print(f"Reajuste ganho: {reajuste_ganho:.0f}")
    percentual = "10%"
    print(f"Em percentual: {percentual}")

elif salario > 1200 and salario <= 2000:
    novo_salario = salario * 1.07 
    print(f"Novo salario: {novo_salario:.2f}")
    reajuste_ganho = salario * 0.07
    print(f"Reajuste ganho: {reajuste_ganho:.0f}")
    percentual = "7%"
    print(f"Em percentual: {percentual}")

else:
    novo_salario = salario * 1.04 
    print(f"Novo salario: {novo_salario:.2f}")
    reajuste_ganho = salario * 0.04
    print(f"Reajuste ganho: {reajuste_ganho:.0f}")
    percentual = "4%"
    print(f"Em percentual: {percentual}")