# problema 1

n1 = int(input("Digite o primeiro inteiro: "))
n2 = int(input("Digite o segundo inteiro: "))
n3 = int(input("Digite o terceiro inteiro: "))
n4 = int(input("Digite o quarto inteiro: "))
n5 = int(input("Digite o quinto inteiro: "))
count = int()

# maior número
if n1 >= n2 and n1 >= n3 and n1 >= n4 and n1 >= n5:
    print("Maior: " + str(n1))
if n2 >= n1 and n2 >= n3 and n2 >= n4 and n2 >= n5:
    print("Maior: " + str(n2))
if n3 >= n1 and n3 >= n2 and n3 >= n4 and n3 >= n5:
    print("Maior: " + str(n3))
if n4 >= n1 and n4 >= n2 and n4 >= n3 and n4 >= n5:
    print("Maior: " + str(n4))
if n5 >= n1 and n5 >= n2 and n5 >= n3 and n5 >= n4:
    print("Maior: " + str(n5))

# menor número
if n1 <= n2 and n1 <= n3 and n1 <= n4 and n1 <= n5:
    print("Menor: " + str(n1))
if n2 <= n1 and n2 <= n3 and n2 <= n4 and n2 <= n5:
    print("Menor: " + str(n2))
if n3 <= n1 and n3 <= n2 and n3 <= n4 and n3 <= n5:
    print("Menor: " + str(n3))
if n4 <= n1 and n4 <= n2 and n4 <= n3 and n4 <= n5:
    print("Menor: " + str(n4))
if n5 <= n1 and n5 <= n2 and n5 <= n3 and n5 <= n4:
    print("Menor: " + str(n5))

# divisíveis por três
if n1%3 == 0:
    count = count + 1
if n2%3 == 0:
    count = count + 1
if n3%3 == 0:
    count = count + 1
if n4%3 == 0:
    count = count + 1
if n5%3 == 0:
    count = count + 1

print("Quantidade de divisíveis por 3: " + str(count))