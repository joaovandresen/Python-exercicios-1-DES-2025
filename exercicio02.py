tempo_x = int(input("Digite o tempo da tarefa X (em horas): "))
tempo_y = int(input("Digite o tempo da tarefa Y (em horas): "))
tempo_z = int(input("Digite o tempo da tarefa Z (em horas): "))

if tempo_x < 0 or tempo_y < 0 or tempo_z < 0:
    print("Erro: tempo de tarefa negativo!")
else:
    total = tempo_x + tempo_y + tempo_z
    print("Tempo total para finalizar as tarefas:", total, "horas")
#FINALIZADO