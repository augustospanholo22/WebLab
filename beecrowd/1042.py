print("Digite três números inteiros separados por espaço:")
entrada = input("Entrada: ")
valores = list(map(int, entrada.split()))
original = valores.copy()

# Ordena a cópia da lista
valores.sort()

print("\nNúmeros em ordem crescente:")
for v in valores:
    print(v)

print("\nOrdem original:")
for v in original:
    print(v)
