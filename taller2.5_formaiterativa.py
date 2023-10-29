def mcm_iterativo(a, b):
  a_primos = factorizar_primos(a)
  b_primos = factorizar_primos(b)

  mcm = 1
  for p in a_primos:
    if p in b_primos:
      mcm *= p ** max(a_primos[p], b_primos[p])
  return mcm


def factorizar_primos(n):

  factores = {}
  while n % 2 == 0:
    factores[2] = factores.get(2, 0) + 1
    n //= 2
  p = 3
  while p * p <= n:
    while n % p == 0:
      factores[p] = factores.get(p, 0) + 1
      n //= p
    p += 2
  if n > 1:
    factores[n] = 1
  return factores
if __name__ == "__main__":


  a = int(input("Ingrese el primer número: "))
  b = int(input("Ingrese el segundo número: "))

  # Calculamos el Mínimo Común Múltiplo.
  mcm = mcm_iterativo(a, b)

  # Imprimimos el resultado.
  print(f"El Mínimo Común Múltiplo de {a} y {b} es {mcm}")


