# problema 6

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

resto_4 = ano % 4
resto_100 = ano % 100

if (mes > 12 or mes < 1):
    print("Data inválida")
elif (dia > 31 or dia < 1):
    print("Data inválida")
elif mes == 2: # fevereiro
    if dia > 29:
        print("Data inválida")
    elif dia == 29 and ano == 400:
        print("Data válida")
    elif dia == 29:
        if resto_4 == 0 and resto_100 != 0:
            print("Data válida")
        else:
            print("Data inválida")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia > 30:
        print("Data inválida")
    else:
        print("Data válida")
else:
    print("Data válida")