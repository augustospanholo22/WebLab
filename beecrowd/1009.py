nome = input("Nome: ")
salario_fixo = float(input("Salario: "))
vendas = float(input("vendas (R$): "))

calc = vendas * 0.15
calc += salario_fixo
print(f"Total = {calc:.2f}")