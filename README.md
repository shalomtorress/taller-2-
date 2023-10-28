# taller-2-
## Punto 1
+ Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. Pista: Utilice los operadores módulo (%) y división entera (//).


````python
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

## Punto 7. 
+ Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.
````python
# Función para verificar si una cadena tiene dos o más vocales
def tiene_dos_o_mas_vocales(cadena):
    vocales = "AEIOUaeiou"
    contador = 0

    for letra in cadena:
        if letra in vocales:
            contador += 1
            if contador >= 2:
                return True

    return False

# Función principal para buscar cadenas en la lista
def buscar_cadenas_con_dos_o_mas_vocales(lista):
    encontrada = False

    for cadena in lista:
        if tiene_dos_o_mas_vocales(cadena):
            print("Cadena con dos o más vocales encontrada:", cadena)
            encontrada = True

    if not encontrada:
        print("No existe ninguna cadena con dos o más vocales en la lista.")

# Ejemplo de uso
lista_de_cadenas = ["Hola", "Mundo", "Python", "Perro", "Gato"]
buscar_cadenas_con_dos_o_mas_vocales(lista_de_cadenas)
````
+ Función ```tiene_dos_o_mas_vocales```: Esta función toma una cadena como entrada y verifica si contiene al menos dos vocales. 
+ Utiliza un bucle ```for``` para recorrer cada letra en la cadena y compara cada letra con una lista de vocales, que está representada por la cadena "AEIOUaeiou".
+ El contador se incrementa cada vez que se encuentra una vocal en la cadena. Si el contador alcanza al menos 2, la función devuelve ```True```, indicando que la cadena cumple con la condición de tener al menos dos vocales. Si no se cumple, la función devuelve ```False```.
## Punto 8
+ Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista.
````python
# Función para encontrar elementos en la primera lista que no están en la segunda lista
def encontrar_elementos_no_comunes(lista1, lista2):
    # Convierte ambas listas en conjuntos para realizar la operación de diferencia
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    # Encuentra los elementos en el primer conjunto que no están en el segundo conjunto
    elementos_no_comunes = conjunto1 - conjunto2

    return list(elementos_no_comunes)  # Convierte el resultado de nuevo en una lista

# Ejemplo de uso
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

elementos_no_comunes = encontrar_elementos_no_comunes(lista1, lista2)
print("Elementos en la primera lista que no están en la segunda lista:", elementos_no_comunes)
````
+ La función ```encontrar_elementos_no_comunes``` toma dos listas como entrada, ```lista1``` y ```lista2```.
+ Convierte ambas listas en conjuntos utilizando ```set()```, lo que elimina duplicados y facilita las operaciones de conjuntos.
+ Luego, utiliza la operación de diferencia ```(-)``` para encontrar los elementos que están en el ```conjunto1``` (que corresponde a ```lista1```) pero no están en el ```conjunto2``` (que corresponde a ```lista2```).
+ Finalmente, convierte el resultado de la operación de diferencia de nuevo en una lista utilizando ```list()```, ya que el resultado es un conjunto.
## Punto 9
+ Resolver el punto 7 del taller 1 usando operaciones con vectores.
````python
import math

# Función para calcular el promedio de una lista de números
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

# Función para calcular la mediana de una lista de números
def calcular_mediana(numeros):
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    if n % 2 == 0:
        # Si hay un número par de elementos, la mediana es el promedio de los dos elementos del medio
        medio_1 = numeros_ordenados[n // 2 - 1]
        medio_2 = numeros_ordenados[n // 2]
        return (medio_1 + medio_2) / 2
    else:
        # Si hay un número impar de elementos, la mediana es el elemento del medio
        return numeros_ordenados[n // 2]

# Función para calcular el promedio multiplicativo de una lista de números
def calcular_promedio_multiplicativo(numeros):
    multiplicacion = 1
    for numero in numeros:
        multiplicacion *= numero
    return multiplicacion ** (1 / len(numeros))

# Función para calcular la potencia del mayor número elevado al menor número
def calcular_potencia_mayor_menor(numeros):
    numeros_ordenados = sorted(numeros)
    mayor = numeros_ordenados[-1]
    menor = numeros_ordenados[0]
    return mayor ** menor

# Función para calcular la raíz cúbica del menor número
def calcular_raiz_cubica_menor(numeros):
    menor = min(numeros)
    return math.pow(menor, 1/3)

# Pedir al usuario que ingrese 5 números reales
numeros = []
for i in range(5):
    numero = float(input("Ingrese un número real: "))
    numeros.append(numero)

# Calcular y mostrar los resultados
promedio = calcular_promedio(numeros)
mediana = calcular_mediana(numeros)
promedio_multiplicativo = calcular_promedio_multiplicativo(numeros)
numeros_ascendente = sorted(numeros)
numeros_descendente = sorted(numeros, reverse=True)
potencia_mayor_menor = calcular_potencia_mayor_menor(numeros)
raiz_cubica_menor = calcular_raiz_cubica_menor(numeros)

print(f"Promedio: {promedio}")
print(f"Mediana: {mediana}")
print(f"Promedio Multiplicativo: {promedio_multiplicativo}")
print(f"Números Ordenados Ascendente: {numeros_ascendente}")
print(f"Números Ordenados Descendente: {numeros_descendente}")
print(f"Potencia del Mayor al Menor: {potencia_mayor_menor}")
print(f"Raíz Cúbica del Menor: {raiz_cubica_menor}")
````
+ Importamos el módulo ```math``` para poder utilizar funciones matemáticas como la raíz cúbica.
+ Definimos varias funciones para realizar diferentes cálculos:
  + ```calcular_promedio(numeros)```: Calcula el promedio de una lista de números sumando todos los números y dividiendo por la cantidad de números en la lista.
  + ```calcular_mediana(numeros)```: Calcula la mediana de una lista de números. Para ello, primero ordena la lista y luego determina si la cantidad de números es par o impar. Si es par, toma el promedio de los dos números en el medio; si es impar, toma el número del medio.
  + ```calcular_promedio_multiplicativo(numeros)```: Calcula el promedio multiplicativo de una lista de números. Esto implica multiplicar todos los números y luego calcular la raíz enésima, donde n es la cantidad de números en la lista.
  + ```calcular_potencia_mayor_menor(numeros)```: Calcula la potencia del mayor número elevado al menor número. Primero, ordena la lista de números para obtener el mayor y el menor.
  + ```calcular_raiz_cubica_menor(numeros)```: Calcula la raíz cúbica del número más pequeño en la lista.
+ Luego, solicitamos al usuario que ingrese 5 números reales en un bucle ```for```, y almacenamos estos números en la lista ```numeros```.
+ Después de recopilar los números, llamamos a cada una de las funciones definidas anteriormente para calcular el promedio, la mediana, el promedio multiplicativo, el orden ascendente y descendente de los números, la potencia del mayor al menor, y la raíz cúbica del menor número.
+ Finalmente, imprimimos los resultados en la pantalla, utilizando las f-strings de Python para mostrar los valores calculados.



