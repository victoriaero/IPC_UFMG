# problema 3

tempo = int(input("Digite o valor do tempo em segundos: "))

horas = str((tempo)//3600)
minutos = str((tempo)%3600//60)
segundos = str((tempo)%3600%60)

valor_convertido = ("{} h {} min {} s".format(horas, minutos, segundos))

print("Valor convertido: " + valor_convertido)

# SOLUCAO
# tempo_segundos = int(input('Digite o valor do tempo em segundos: '))

# horas = int(tempo_segundos / 3600)
# minutos = int((tempo_segundos % 3600) / 60)
# segundos = int(tempo_segundos % 60)

# print('Valor convertido:', horas, 'h', minutos, 'min', segundos, 's')