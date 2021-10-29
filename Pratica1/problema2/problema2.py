# problema 2

velocidade_inicial = float(input("Digite o valor da velocidade: "))
aceleracao = float(input("Digite o valor da aceleração: "))
tempo = float(input("Digite o valor do tempo: "))

velocidade_final = (velocidade_inicial) + (aceleracao)*(tempo)

distancia_percorrida = (velocidade_inicial)*(tempo)+((1/2)*(aceleracao)*(tempo)**2)

print('Velocidade final: %.2f' % velocidade_final)
print('Distância percorrida: %.2f' % distancia_percorrida)

# SOLUCAO
# velocidade = float(input('Digite o valor da velocidade: '))
# aceleracao = float(input('Digite o valor da aceleração: '))
# tempo = float(input('Digite o valor do tempo: '))

# vel_final = velocidade + (aceleracao * tempo)
# distancia = (velocidade * tempo) + ((aceleracao * (tempo ** 2)) / 2)

# print('Velocidade final: %.2f' % vel_final)
# print('Distância percorrida: %.2f' % distancia)