# problema 5

valor_compra = float(input("Digite o valor da compra: "))

valor_desconto = (valor_compra) * 90/100
valor_parcela = (valor_compra)/6
comissao_avista = (valor_desconto) * 5/100
comissao_parcelado = (valor_compra) * 5/100

print('Valor com desconto: %.2f' % valor_desconto)
print('Valor da parcela: %.2f' % valor_parcela)
print('Comissão do vendedor (à vista): %.2f' % comissao_avista)
print('Comissão do vendedor (parcelado): %.2f' % comissao_parcelado)
