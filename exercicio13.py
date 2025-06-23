# Crie um programa que receba um ano e diga se ele é bissexto.
# (Dica: múltiplos de 4, exceto os múltiplos de 100, a menos que também sejam múltiplos de 400)
ano = int(input("Digite um ano: "))

if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print("É um ano bissexto.")
else:
    print("Não é bissexto.")

# FINALIZADO