# Retorna -1 se o valor é menor que 0, 0 se o valor é 0, 1 se o valor é maior que 0.

def valor_absoluto(numero):

  if numero < 0:
    return -1
  elif numero == 0:
    return 0
  else:
    return 1

numero0 = 0

numero1 = 5

numero2 = -5

resultado = valor_absoluto(numero0)
resultado1 = valor_absoluto(numero1)
resultado2 = valor_absoluto(numero2)

print(f"{numero0} é {resultado}")
print(f"{numero1} é {resultado1}")
print(f"{numero2} é {resultado2}")