def separar_partes(numero):
  parte_entera = int(numero)

  parte_decimal = numero - parte_entera

  lista_digitos_decimales = [int(digito) for digito in str(parte_decimal)[2:]]

  return parte_entera, lista_digitos_decimales

if __name__ == "__main__":

  numero = float(input("Introduce un número flotante: "))

  # Separamos las partes.
  parte_entera, lista_digitos_decimales = separar_partes(numero)

  # Imprimimos las partes.
  print("La parte entera del número es:", parte_entera)
  print("Los dígitos de la parte decimal del número son:", lista_digitos_decimales)



  
