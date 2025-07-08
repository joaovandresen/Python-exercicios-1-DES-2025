senhaCorreta = "1234r"
senha = input("Digite a senha: ")

while senha != senhaCorreta:
    print("Senha incorreta")
    senha = input("Tente novamente: ")
print("Acesso permitido!")