distancia = float(input("Digite a distância: "))
tempo = float(input("Digite o tempo: "))

velocidade = distancia / tempo

if velocidade < 5:
   print("Lento")
elif velocidade >=5 <= 10:
   print("Moderado")
else:
   print("Velocidade rápida")
#FINALIZADO