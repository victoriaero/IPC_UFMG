# problema 5

def peso_ideal(altura, sexo):
    if sexo == "F":
        peso = (62.1 * altura) - 44.7
        return peso
    else:
        peso = (72.7 * altura) - 58
        return peso