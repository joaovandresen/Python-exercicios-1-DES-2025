nota1 = int(input("Digite a nota da primeira meta: "))
nota2 = int(input("Digite a nota da segunda meta: "))
nota3 = int(input("Digite a nota da terceira meta: "))

media = (nota1 + nota2 + nota3) 
if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Em treinamento")
else:
    print("Reprovado")
#FINALIZADO