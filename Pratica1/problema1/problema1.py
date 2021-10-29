# problema 1

raio = float(input("Digite o valor do raio da circunferência: "))

pi = 3.1415

perimetro = 2*(pi)*(raio)
area = (pi)*(raio)**2
volume = (4/3)*(pi)*(raio)**3

print("Perímetro: " + str(round(perimetro, 2)))
print("Área: " + str(round(area, 2)))
print("Volume: " + str(round(volume, 2)))

# SOLUCAO
# raio = float(input('Digite o valor do raio da circunferência: '))

# pi = 3.1415
# perimetro = 2 * pi * raio
# area = pi * (raio ** 2)
# volume = 4 * pi * ((raio ** 3) / 3)

# print('Perímetro: %.2f' % perimetro)
# print('Área: %.2f' % area)
# print('Volume: %.2f' % volume)

# Diferentes formas de fazer formatação de saída
#print('Resto: {}'.format(resto)) # método format de strings
#print(f'Resto: {resto}') # f-strings