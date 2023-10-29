def separar_digitos(numero):

  lista_digitos = []
  while numero > 0:
    digito = numero % 10
    numero //= 10
    lista_digitos.append(digito)

  return lista_digitos

numero = int(input("Introduce un número entero: "))

  
lista_digitos = separar_digitos(numero)

print("Los dígitos del número son:", lista_digitos)

