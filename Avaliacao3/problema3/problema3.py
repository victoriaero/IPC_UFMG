# problema 3

import math

# hora_ent = float(input("hora entrada: "))
# min_ent = float(input("min entrada: "))

# hora_saida = float(input("hora saida: "))
# min_saida = float(input("min saida: "))

def estacionamento(hora_ent, min_ent, hora_saida, min_saida):
    min_ent = min_ent / 60
    min_saida = min_saida / 60
    if hora_ent > hora_saida:
        hora = (24 - hora_ent) + hora_saida
    else:
        hora = hora_saida - hora_ent

    if min_ent > min_saida:
        min = min_ent - min_saida
        hora_total = hora - (min/60)
    else:
        min = min_saida - min_ent
        hora_total = hora + (min/60)

    hora_total = math.ceil(hora_total)

    if hora_total <= 2:
        preco = hora_total * 1
        return preco
    elif hora_total > 2 and hora_total <= 4:
        preco = hora_total * 1.4
        return preco
    else:
        preco = hora_total * 2
        return preco

# preco = estacionamento(hora_ent, min_ent, hora_saida, min_saida)

# print(preco)