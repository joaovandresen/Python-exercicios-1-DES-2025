# Peça a idade do usuário e diga se ele pode se cadastrar em um site:
# Permitido: 13 anos ou mais
idade = int(input("Digite sua idade: "))

if idade == 13:
    print("Cadastro permitido")
elif idade >= 13:
    print("Cadastro permitido.")
else:
    print("Cadastro não permitido.")
# FINALIZADO