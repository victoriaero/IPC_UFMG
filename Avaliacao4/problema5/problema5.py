# problema 5

x = int()
numeros = list()

while x >= 0:
    x = int(input("Digite um número: "))
    if x >= 0:
        numeros.append(x)
print("Maior: ", max(numeros))
print("Menor: ", min(numeros))