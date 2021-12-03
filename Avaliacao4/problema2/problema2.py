# problema 2

n = int(input("Digite n: "))

soma = 0
count = 1

while(count < (n + 1)):
    soma += (1 / count)
    count += 1

print("Resultado: %.2f" % soma)