# problema 3

def verifica_triangulo(l1, l2, l3):
    if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
        return True
    else:
        return False

def tipo_triangulo(l1, l2, l3):
    if l1 == l2 == l3:
        return "Equilátero"
    elif l1 == l2 or l2 == l3 or l1 == l3:
        return "Isósceles"
    else:
        return "Escaleno"