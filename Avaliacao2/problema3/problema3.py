# problema 3

hr_trab = float(input("Digite o valor da hora de trabalho: "))
hr_mes = float(input("Digite a quantidade de horas trabalhadas no mês: "))

sal_bruto = hr_trab * hr_mes

if sal_bruto <= 900:
    ir = 0
    inss = (sal_bruto)*(10/100)
    fgts = (sal_bruto)*(11/100)
    total_desc = ir + inss
    sal_liq = sal_bruto - total_desc
elif sal_bruto <= 1500 and sal_bruto > 900:
    ir = (sal_bruto)*(5/100)
    inss = (sal_bruto)*(10/100)
    fgts = (sal_bruto)*(11/100)
    total_desc = ir + inss
    sal_liq = sal_bruto - total_desc
elif sal_bruto <= 2500 and sal_bruto > 1500:
    ir = (sal_bruto)*(10/100)
    inss = (sal_bruto)*(10/100)
    fgts = (sal_bruto)*(11/100)
    total_desc = ir + inss
    sal_liq = sal_bruto - total_desc
elif sal_bruto > 2500:
    ir = (sal_bruto)*(20/100)
    inss = (sal_bruto)*(10/100)
    fgts = (sal_bruto)*(11/100)
    total_desc = ir + inss
    sal_liq = sal_bruto - total_desc

print("Salário Bruto: R$ %.2f" % sal_bruto)
print("IR: R$ %.2f" % ir)
print("INSS: R$ %.2f" % inss)
print("FGTS: R$ %.2f" % fgts)
print("Total de descontos: R$ %.2f" % total_desc)
print("Salário líquido: R$ %.2f" % sal_liq)