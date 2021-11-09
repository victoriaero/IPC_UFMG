# problema 8

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

if (nota1 <= 10 and nota2 <= 10) and (nota1 >= 0 and nota2 >= 0):
    media = (nota1 + nota2) * 1/2
    print("Média: %.2f" % media)
else:
    print("Nota inválida")