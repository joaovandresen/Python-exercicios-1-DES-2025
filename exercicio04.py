distancia = float(input("Digite a distância: "))
tempo = float(input("Digite o tempo: "))

velocidade = distancia / tempo

if velocidade < 5:
   print("Velocidade lenta")
elif velocidade <= 10:
   print("Velocidade moderada")
else:
   print("Velocidade rápida")
#FINALIZADO