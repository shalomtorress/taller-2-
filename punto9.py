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
