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
