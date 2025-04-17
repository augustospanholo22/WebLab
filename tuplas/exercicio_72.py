numero = ("Zero","um","dois","tres","quatro",
          "cinco","seis","sete","oito","nove",
          "dez","onze","doze","treze","quatorze",
          "quinze","dezeseis","dezessete","dezoito",
          "dezenove","vinte")
while True:
    while True:
        num = int(input("Digite um número entre 0 e 20: "))
        if num >= 0 and num <=20:
            break

    print(f"Voce digitou o numero {numero[num]}") 

    resposta = str(input("Voce quer continuar?  ")).strip() .upper()[0]
    if resposta == "N":
        break
