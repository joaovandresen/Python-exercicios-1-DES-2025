# Peça três números e exiba-os em ordem crescente.
# Solicita três números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

numeros = [numero1, numero2, numero3]

numeros.sort()
print("Ordem crescente:", numeros)
# FINALIZADO