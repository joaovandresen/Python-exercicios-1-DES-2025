#Peça ao usuário uma senha e verifique se ela contém pelo menos 8 caracteres.
#Exiba uma mensagem de "Senha válida" ou "Senha muito curta".
senha = input("Digite sua senha: ")

if senha >= "12345678":
        print("Senha válida.")
else:
        print("Senha muito curta.")
