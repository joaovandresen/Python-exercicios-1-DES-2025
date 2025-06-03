dias_01 = int(input("Digite o tempo da tarefa X: "))
dias_02 = int(input("Digite o tempo da tarefa Y: "))
dias_03 = int(input("Digite o tempo da tarefa Z: "))

if dias_01 < 0 or dias_02 < 0 or dias_03 < 0:
    print("Erro: tempo de tarefa negativo!")
else:
    total = dias_01 + dias_02 + dias_03
    print("Tempo total para finalizar as tarefas:", total, "horas")
#FINALIZADO