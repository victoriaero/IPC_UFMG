# problema 1

invest_inicial = float(input("Digite o valor do investimento inicial: "))
taxa_anual = float(input("Digite a taxa de juros anual: "))
periodo = float(input("Digite o período do investimento em anos: "))

valor_futuro = (invest_inicial) * (1 + ((taxa_anual) * 0.01)) ** (periodo)

print('Valor futuro: %.2f' % valor_futuro)