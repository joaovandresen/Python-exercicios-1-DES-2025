distancia = float(input("Digite a distância em km: "))

if distancia <= 50:
    frete = 5.00  
elif distancia <= 150:
    frete = 15.00  
else:
    frete = 25.00  
print(f"O custo do frete para {distancia} km é R$ {frete:.2f}")
#FINALIZADO