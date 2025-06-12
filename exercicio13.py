# Crie um programa que receba um ano e diga se ele é bissexto.
# (Dica: múltiplos de 4, exceto os múltiplos de 100, a menos que também sejam múltiplos de 400)
def e_bissexto(ano):
    """Verifica se um ano é bissexto."""
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
ano = int(input("Digite um ano: "))
if e_bissexto(ano):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")
# FINALIZADO