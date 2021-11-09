# problema 2

v_max = float(input("Digite o valor da velocidade máxima: "))
v_reg = float(input("Digite o valor da velocidade registrada: "))

if v_max >= v_reg:
    print("Sem Infração")
elif (20/100*v_max) + v_max >= v_reg:
    print("Infração Média")
elif (50/100*v_max) + v_max >= v_reg:
    print("Infração Grave")
else:
    print("Infração Gravíssima")