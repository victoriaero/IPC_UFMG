# problema 5

valor = float(input("Digite o valor do produto: "))
estado = str(input("Digite o estado: "))
taxa = float()
valor_final = float()

if estado != "MG" and estado != "SP" and estado != "RJ" and estado != "MS":
    print("Estado inválido")
elif estado == "MG":
    taxa = (valor)*(7/100)
    valor_final = valor + taxa
    print("Valor final: %.2f" % valor_final)
elif estado == "SP":
    taxa = (valor)*(12/100)
    valor_final = valor + taxa
    print("Valor final: %.2f" % valor_final)
elif estado == "RJ":
    taxa = (valor)*(15/100)
    valor_final = valor + taxa
    print("Valor final: %.2f" % valor_final)
elif estado == "MS":
    taxa = (valor)*(8/100)
    valor_final = valor + taxa
    print("Valor final: %.2f" % valor_final)