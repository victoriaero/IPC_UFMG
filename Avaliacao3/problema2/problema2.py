# problema 2

def consumo(distancia, quant_lgas_consumidos):
    dist_lgas = distancia / quant_lgas_consumidos
    if dist_lgas < 8:
        return "Venda o carro!"
    elif dist_lgas >= 8 and dist_lgas < 12:
        return "Econômico!"
    else:
        return "Super econômico!" 