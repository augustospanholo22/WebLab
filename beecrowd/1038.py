print((("""
___________________________________________        
CODIGO  ESPECIFICAÇÂO       PREÇO
___________________________________________
1       Cachorro Quente     R$ 4.00
2       X-Salada            R$ 4.50
3       X-Bacon             R$ 5.00
4       Torrada simples     R$ 2.00
5       Refrigerante        R$ 1.50
___________________________________________"""))) 

codigo = int(input("Digite aqui o código do seu pedido: "))
quantidade = int(input("Quantos deseja? "))

if codigo <1 or codigo >5:
    print("Valor não encontrado")
    exit()

else:
    if codigo == 1:
        codigo = 4.00

    elif codigo ==2:
        codigo= 4.50

    elif codigo == 3:
        codigo = 5.00

    elif codigo == 4:
        codigo = 2.00

    else:
        codigo = 1.50

soma = codigo * quantidade
print(f"Total: {soma:.2f}")