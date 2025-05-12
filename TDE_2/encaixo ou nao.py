cont = 0
qtd_teste = int(input("Quantos tester quer fazer? "))
while cont < qtd_teste:
    a = int(input("Valor A: "))
    b = int(input("Valor B: "))

    if a < 0 or b < 0:
        print("Erro, tente novamente")
        continue
    if a > 1000 and b > 1000:
        print("Número muito grande")
        continue

    if str(a).endswith(str(b)):
        print("Encaixa")
    else:
        print("Não encaixa")
    
    cont += 1
    
        
