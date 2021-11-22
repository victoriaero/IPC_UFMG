# problema 1

def pagamento(salario):
    if salario <= 280:
        salario_atualizado = salario * 1.2
    elif salario > 280 and salario <= 700:
        salario_atualizado = salario * 1.15
    elif salario > 700 and salario <= 1500:
        salario_atualizado = salario * 1.1
    else:
        salario_atualizado = salario * 1.05

    return(salario_atualizado)