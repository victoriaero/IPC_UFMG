# problema 3

sal_c = float(input("Digite o salário do Carlos: "))
rend_p = float(input("Digite o rendimento da poupança(%): "))
rend_f = float(input("Digite o rendimento do fundo de renda fixa(%): "))

sal_j = sal_c / 3

count_mes = int()
while(sal_j < sal_c):
    sal_c += (sal_c * rend_p / 100)
    sal_j += (sal_j * rend_f / 100)
    count_mes += 1

print("Meses: ", count_mes)