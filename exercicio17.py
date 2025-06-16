#Peça ao usuário uma temperatura em Celsius e converta para Fahrenheit.
# Fórmula: F = C × 1.8 + 32
# .
def celsius_fahrenheit(celsius):
  
  fahrenheit = celsius * 1.8 + 32
  return fahrenheit

temperatura_celsius = float(input("Digite a temperatura em ºC: "))

temperatura_fahrenheit = celsius_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C é igual a {temperatura_fahrenheit}°F")
# FINALIZADO