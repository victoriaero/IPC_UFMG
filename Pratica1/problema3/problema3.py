# problema 3

tempo = int(input("Digite o valor do tempo em segundos: "))

horas = str((tempo)//3600)
minutos = str((tempo)%3600//60)
segundos = str((tempo)%3600%60)

valor_convertido = ("{} h {} min {} s".format(horas, minutos, segundos))

print("Valor convertido: " + valor_convertido)