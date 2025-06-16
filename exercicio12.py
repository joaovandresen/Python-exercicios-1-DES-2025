#Peça ao usuário uma senha e verifique se ela contém pelo menos 8 caracteres.
#Exiba uma mensagem de "Senha válida" ou "Senha muito curta".
senha = input("Digite sua senha: ")

digitos = len(senha)

if digitos >= 8: 
    print("Senha correta.")
else:
    print("Senha incorreta.")
# FINALIZADO