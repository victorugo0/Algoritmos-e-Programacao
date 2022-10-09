# https://www.beecrowd.com.br/judge/pt/problems/view/1017

tempoGasto = int(input())
velocidadeMedia = int(input())
distancia = tempoGasto * velocidadeMedia
gasolinaGasta = distancia / 12
print('%.3f' % gasolinaGasta)