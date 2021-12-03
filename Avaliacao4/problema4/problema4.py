# problema 4

import math

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

for i in range(x, (y + 1)):
    n = math.sqrt(i)
    if int(n) == n:
        print(i)