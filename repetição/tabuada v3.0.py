from time import sleep
repeticao = soma = 0
while True:
    tabuada = int(input("Quer ver a tabuada de qual valor? "))

    if tabuada < 0:
        print("Encerrando programa...")
        sleep(2)
        break

    repeticao = 1
    while repeticao <= 10:
        soma = tabuada * repeticao
        print(f"{tabuada} x {repeticao} = {soma}")
        repeticao += 1
        
    

   
    