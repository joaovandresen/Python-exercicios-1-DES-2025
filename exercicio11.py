#Crie um programa que receba o peso (kg) e a altura (m) de uma pessoa e calcule o IMC.
#Classifique o resultado de acordo com a faixa:
#Abaixo do peso (< 18.5)
#Peso normal (18.5 a 24.9)
#Sobrepeso (25 a 29.9)
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura ** 2)
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"O seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
#FINALIZADO