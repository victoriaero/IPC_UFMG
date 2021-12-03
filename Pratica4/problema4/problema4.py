# problema 4

preco_p = float(input("Digite o preço do pão: "))

count = 1
while(count < 51):
    valor = count * preco_p
    print(count, " - R$ %.2f" % valor)
    count += 1