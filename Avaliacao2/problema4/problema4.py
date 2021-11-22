# problema 4
import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a == 0:
    print("Não é uma equação quadrática")
else:
    delta = ((b)**2) - 4*(a)*(c)

    if delta < 0:
        print("Não existe raiz real")
    elif delta > 0:
        raiz1 = (-b + math.sqrt(delta))/(2*a)
        raiz2 = (-b - math.sqrt(delta))/(2*a)  
        print('Raiz 1: %.2f' % raiz1)
        print('Raiz 2: %.2f' % raiz2)
    else:
        raiz = (-b + math.sqrt(delta))/(2*a)
        print("Raiz única")
        print('Raiz: %.2f' % raiz)