# problema 1

raio = float(input("Digite o valor do raio da circunferência: "))

pi = 3.1415

perimetro = 2*(pi)*(raio)
area = (pi)*(raio)**2
volume = (4/3)*(pi)*(raio)**3

print("Perímetro: " + str(round(perimetro, 2)))
print("Área: " + str(round(area, 2)))
print("Volume: " + str(round(volume, 2)))