# problema 5

inteiro = int(input("Digite um inteiro n: "))

div = 2
for i in range(2, inteiro):
    if inteiro % i == 0:
        div = div + 1

if div > 2 or inteiro < 2:
    print("Não é primo")
else:
    print("É primo")