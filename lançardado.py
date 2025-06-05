import random

input ("Pressione o enter para lançar o dado")

resultado = random.randint(1,6)

print(f"O dado rolou : {resultado}" );

if resultado == 6 :
   print("Uau! você é fera!")

if resultado <= 2 :
   print("Que pena, tente denovo!")

if resultado == 5 :
   print("É, até que você não foi tão mal!")