# problema 6

custo_fab = float(input("Digite o custo de fábrica: "))

if custo_fab <= 12000:
    custo_tot = custo_fab + (custo_fab * 5/100)
elif custo_fab <= 25000:
    custo_tot = custo_fab + (custo_fab * 10/100) + (custo_fab * 15/100)
elif custo_fab > 25000:
    custo_tot = custo_fab + (custo_fab * 15/100) + (custo_fab * 20/100)

print("Custo total: %.2f" % custo_tot) 