# problema 2

# valor_hora = float(input("Digite o valor da hora trabalhada: "))
# quantidade_horas = float(input("Digite a quantidade de horas trabalhadas: "))

def pagamento(valor_hora, quantidade_horas):
    salario = valor_hora * quantidade_horas
    if salario <= 900:
        return salario
    elif salario > 900 and salario <= 1500:
        return (salario * 0.95)
    elif salario > 1500 and salario <= 2500:
        return (salario * 0.90)
    else:
        return (salario * 0.80)

# salario = pagamento(valor_hora, quantidade_horas)

# print("Salario Bruto: %.2f" % salario)