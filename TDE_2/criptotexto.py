C = int(input())

for _ in range(C):
    mensagem = input()
    texto_oculto = ''.join([letra for letra in mensagem if letra.islower()])
    print(texto_oculto[::-1])