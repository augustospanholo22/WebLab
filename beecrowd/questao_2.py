idade = int(input("Informe sua idade: "))

if idade <= 10:
    print("O valor do ingresso é: R$ 7.00")

elif idade > 10 and idade <= 60:
    print("O valor do ingresso é: R$ 15.00")

else:
    print("O valor do ingresso é: R$ 10.00")