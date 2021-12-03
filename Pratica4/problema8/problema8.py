# problema 8

def quantidade_pares(inicio, fim):
    count = 0
    for i in range(inicio, (fim + 1)):
        if i % 2 == 0:
            count += 1
    return count