# problema 2

v_pedro = float(input("Digite o valor que o Pedro apostou: "))
v_joao = float(input("Digite o valor que o João apostou: "))
v_marcela = float(input("Digite o valor que a Marcela apostou: "))

v_premio = float(input("Digite o valor do prêmio: "))

proporcao = (v_premio)/(v_pedro + v_joao + v_marcela)

p_pedro = (proporcao) * (v_pedro)
p_joao = (proporcao) * (v_joao)
p_marcela = (proporcao) * (v_marcela)

print('Prêmio do Pedro: %.2f' % p_pedro)
print('Prêmio do João: %.2f' % p_joao)
print('Prêmio da Marcela: %.2f' % p_marcela)