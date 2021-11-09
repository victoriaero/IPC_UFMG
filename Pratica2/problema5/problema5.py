# problema 5
import math

num = float(input("Digite um número: "))

if num >= 0:
    raiz = math.sqrt(num)
    print("Resultado: %.3f" % raiz)
else:
    print("Número inválido")