# problema 4

def calcula_valor(preco_litro, quant_litros_abt, tipo_comb):
    if tipo_comb == "a":
        if quant_litros_abt <= 20:
            preco_total = (preco_litro * 0.97) * quant_litros_abt
            return preco_total
        else:
            preco_total = (preco_litro * 0.95) * quant_litros_abt
            return preco_total
    elif tipo_comb == "g":
        if quant_litros_abt <= 20:
            preco_total = (preco_litro * 0.96) * quant_litros_abt
            return preco_total
        else:
            preco_total = (preco_litro * 0.94) * quant_litros_abt
            return preco_total