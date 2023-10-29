import math

#función para la aproximacion de coseno
def aprox_coseno(x, n):
  aprox = 0

  for i in range(n):
    termino = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    aprox += termino

  valor = math.cos(x)
  dif = abs(valor - aprox)

  return aprox, dif

#funcion para obtener el numero de terminos necesarios para obtener error
def term_necesarios(x, error_max):
  n = 0
  error = error_max + 1
  while error > error_max:
    n += 1
    aprox, _ = aprox_coseno(x, n)
    error = abs(math.cos(x) - aprox)
  return n

x = float(input("Ingresa el valor de x: "))

#errores deseados
errores_deseados = [0.1, 1, 10]

#se imprime el error con el porcentaje en fraccion 
for error_per in errores_deseados:
  error_max = error_per / 100  
  n_max = term_necesarios(x, error_max)
  aprox, dif = aprox_coseno(x, n_max)
  print(f"Para x = {x}, se necesita un mínimo de {n_max} términos para obtener un error del {error_per}% o menos.")
  print(f"Aproximación de cos({x}) con {n_max} términos: {aprox:.7f}")
  print(f"Diferencia con el valor real: {dif:.4f}")
  print()

