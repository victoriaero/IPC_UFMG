# problema 1

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n2 <= n1 <= n3 or n3 <= n1 <= n2:
    print("Mediana: ", n1)
elif n1 <= n2 <= n3 or n3 <= n2 <= n1:
    print("Mediana: ", n2)
elif n1 <= n3 <= n2 or n2 <= n3 <= n1:
    print("Mediana: ", n3)