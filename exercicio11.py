#Crie um programa que receba o peso (kg) e a altura (m) de uma pessoa e calcule o IMC.
#Classifique o resultado de acordo com a faixa:
#Abaixo do peso (< 18.5)
#Peso normal (18.5 a 24.9)
#Sobrepeso (25 a 29.9)
#Obesidade (>= 30)
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

imc = calcular_imc(peso, altura)

classificacao = classificar_imc(imc)
print(f"O seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")