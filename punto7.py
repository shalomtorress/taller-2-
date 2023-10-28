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
