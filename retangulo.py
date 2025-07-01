def calculo_area(base, altura):
    area = base * altura
    return area
base = int(input("Digite a base: "))
altura = int(input("Digite a altura: "))


area = calculo_area(base, altura)
print(f"A área do retângulo com base {base} e altura {altura} é {area}")
# FINALIZADO