soma = 0
numero = int(input("Digite um número (para somar gigante 0)"))

while numero != 0:
    soma += numero
    numero = int(input("Digite um número (para somar gigante 0)"))
print("Soma total:", soma)