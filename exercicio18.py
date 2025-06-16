# Receba duas notas e seus respectivos pesos. Calcule a média ponderada.
# Fórmula: (nota1 × peso1 + nota2 × peso2) / (peso1 + peso2)

# FÓRMULA DA MÉDIA
def media_ponderada(nota1, peso1, nota2, peso2):
    return (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)

nota1 = float(input("Digite a primeira nota: "))
peso1 = float(input("Digite o peso da primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
peso2 = float(input("Digite o peso da segunda nota: "))

resultado = media_ponderada(nota1, peso1, nota2, peso2)
print(f"A média ponderada é: {resultado:.2f}")
# FINALIZADO