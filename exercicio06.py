acesso_plataforma = int(input("Digite o horário que você está acessando a plataforma: "))

if acesso_plataforma <= 22 :
   print("Alerta! Você está tentando acessar a plataforma em um horário não permitido.")

if acesso_plataforma >= 9 :
   print("Horário autorizado.")