# Loja oferece os seguintes descontos:
# Compras acima de R$ 500,00 têm 10%
# Acima de R$ 300,00 têm 5%
# Menor ou igual a R$ 300,00 não têm desconto
valordacompra = int(input("Digite o valor da sua compra: "))

if valordacompra == 300 :
    print("Não têm desconto")
elif valordacompra >= 500:
    print("Você ganhou um desconto de 10%")

if valordacompra <= 300:
    print("Não tem desconto")
# FINALIZADO