# problema 3

print("Loja Quase Dois - Tabela de preços")

count = 1
while (count < 51):
    valor = count * 1.99
    print(count, " - R$ %.2f" % valor)
    count += 1