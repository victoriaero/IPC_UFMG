# problema 3

idade = int(input("Digite a idade: "))
tempo_c = int(input("Digite o tempo de contribuição: "))
sexo = str(input("Digite o sexo (M/F): "))

if sexo == "M":
    if idade >= 65 or (idade >= 60 and tempo_c >= 35):
        print("Pode aposentar")
    else:
        print("Não pode aposentar")
elif sexo == "F":
    if idade >= 60 or (idade >= 55 and tempo_c >= 30):
        print("Pode aposentar")
    else:
        print("Não pode aposentar")