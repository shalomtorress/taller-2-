# taller-2-
## Punto 1
+ Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. Pista: Utilice los operadores módulo (%) y división entera (//).


````pythhon
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
````
 se utiliza los operadores (%) (//) para separar los dígitos del número,(%) devuelve el resto de la división de dos números, se utiliza para obtener el dígito más a la derecha del número. (//) devuelve el cociente de la división de dos números, se utiliza para eliminar el dígito más a la derecha del número.
 El b while se ejecuta mientras el número sea mayor que 0, En cada iteración del bucle, se obtiene el dígito más a la derecha del número, se agrega a la lista ````lista_digitos```` y se elimina el dígito más a la derecha del número.
 ## Punto 2 
 + Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.
````python
def separarpartes(numero):
  parte_entera = int(numero)

  parte_decimal = numero - parte_entera

  lista_digitos_decimales = [int(digito) for digito in str(parte_decimal)[2:]]

  return parte_entera, lista_digitos_decimales

if __name__ == "__main__":

  numero = float(input("Introduce un número flotante: "))

  parte_entera, lista_digitos_decimales = separarpartes(numero)

  print("La parte entera del número es:", parte_entera)
  print("Los dígitos de la parte decimal del número son:", lista_digitos_decimales)
````
La función int convierte el número flotante a un número entero, con esto se separa la parte entera y la parte decimal, la parte decimal del número es la diferencia entre el número flotante original y la parte entera, se utiliza el str para crear una lista con la parte decimal, La función ````[2:] ```` elimina los dos primeros numeros de la lista, que corresponden al signo y al punto decimal 
con la funcion ````int```` se convierte cada numero de la lista en un numero entero.
## Punto 3 
+ Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.
````python
def numerosespejo(numero_1, numero_2):
 
  listanumero_1 = str(numero_1)
  listanumero_2 = str(numero_2)

  listanumero1reversa = listanumero_1[::-1]
  listanumero2reversa = listanumero_2[::-1]

  return listanumero_1 == listanumero1reversa and listanumero_2 == listanumero2reversa


if __name__ == "__main__":
  numero_1 = int(input("Introduce el primer número: "))
  numero_2 = int(input("Introduce el segundo número: "))

  sonespejos = numerosespejo(numero_1, numero_2)

  if sonespejos:
    print("Los números son espejos.")
  else:
    print("Los números no son espejos.")
````
se usa el str para convertir losnumeros en listas, despues se reversan estoas listas para poder comparar de izquierda a derecha o de derecha a izquierda. con ````==```` compara las listas, Si las listas son iguales, entonces los números son espejos.
## Punto 4
+ Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Calcule con cuántos términos de la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%.

````python
