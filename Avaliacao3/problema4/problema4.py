# problema 4

def media(nota1, nota2, nota3, letra):
    if letra == "A":
        media_a = (nota1 + nota2 + nota3)/3
        return media_a
    elif letra == "P":
        media_p = ((nota1 * 5) + (nota2 * 3) + (nota3 * 2))/ 10
        return media_p