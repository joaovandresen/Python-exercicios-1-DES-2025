# Crie um programa que calcule o reajuste de salário:
# Salários até R$ 2000,00: +15%
# De R$ 2000,01 a R$ 5000,00: +10%
# Acima de R$ 5000,00: +5%
salario = float(input("Digite o seu salário: "))
if salario <= 2000:
    salario_novo = salario * 1.15
elif salario <= 5000:
    salario_novo = salario * 1.10
else:
    salario_novo = salario * 1.05
print(f"O seu salário é: R$ {salario_novo:.2f}")
#FINALIZADO