# problema 1

def soma_divisores(int):
    soma = 0
    count = 1
    while(count < (int)):
        if int % count == 0:
            soma += count
        count += 1

    return soma