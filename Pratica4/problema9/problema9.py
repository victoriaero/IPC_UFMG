# problema 9

soma_par = 0
soma_impar = 0

while True:
    num = int(input("Digite um número: "))
    if num > 0 or num == 0:
        if num % 2 == 0: 
            soma_par += num
        else:
            soma_impar += num
    else:
        break

print("Soma pares: ", soma_par)
print("Soma ímpares: ", soma_impar)