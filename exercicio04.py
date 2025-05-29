distancia = int(input("Digite a distância percorrida em km: "))
tempo = int(input("Digite o tempo gasto em horas: "))

velocidade = distancia / tempo

if velocidade < 5:
   print("Velocidade lenta")
elif velocidade <= 10:
   print("Velocidade moderada")
else:
   print("Velocidade rápida")
#FINALIZADO