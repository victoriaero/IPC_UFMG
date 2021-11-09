# problema 4

v_sal = float(input("Digite o valor do salário: "))
v_aum = float()
v_tot = float()

if v_sal <= 280.00:
    v_aum = v_sal*20/100
    v_tot = v_sal + v_aum
elif v_sal <= 700.00:
    v_aum = v_sal*15/100
    v_tot = v_sal + v_aum
elif v_sal <= 1500.00:
    v_aum = v_sal*10/100
    v_tot = v_sal + v_aum
elif v_sal > 1500.00:
    v_aum = v_sal*5/100
    v_tot = v_sal + v_aum

print("Valor do aumento: %.2f" % v_aum)
print("Novo salário: %.2f" % v_tot)