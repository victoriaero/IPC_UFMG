# problema 6

inteiro = int(input("Digite um inteiro n: "))

num_1 = 1
num_2 = 1

for i in range(2, inteiro):
    soma = num_1 + num_2
    num_1 = num_2
    num_2 = soma

print(num_2)