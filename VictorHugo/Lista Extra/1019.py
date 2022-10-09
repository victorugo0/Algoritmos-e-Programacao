# https://www.beecrowd.com.br/judge/pt/problems/view/1019

tempoDuracao = int(input())
hora = 0 
minutos = 0
segundos = 0
while True:
    if tempoDuracao <= 3600:
        break
    
    tempoDuracao -= 3600
    hora += 1

while True:
    if tempoDuracao <= 60:
        break
    
    tempoDuracao -= 60
    minutos += 1

while True:
    if tempoDuracao <= 1:
        segundos += 1
        break
    
    tempoDuracao -= 1
    segundos += 1

print('%i:%i:%i' % (hora, minutos, segundos))