def mcm_recursivo(a, b):
  """
  Calcula el Mínimo Común Múltiplo de dos números enteros.

  Args:
    a: Primer número entero.
    b: Segundo número entero.

  Returns:
    Mínimo Común Múltiplo de los dos números.
  """

  if a % b == 0:
    return b
  else:
    return mcm_recursivo(b, a % b)


if __name__ == "__main__":
  """
  Programa principal.
  """

  a = int(input("Ingrese el primer número: "))
  b = int(input("Ingrese el segundo número: "))

  # Calculamos el Mínimo Común Múltiplo.
  mcm = mcm_recursivo(a, b)

  # Imprimimos el resultado.
  print(f"El Mínimo Común Múltiplo de {a} y {b} es {mcm}")

