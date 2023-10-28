# Usando un patrón de acumulación:
def multiplos_de_tres_acumulacion(lista):
    multiplos_de_tres = []
    for numero in lista:
        if numero % 3 == 0:
            multiplos_de_tres.append(numero)
    return multiplos_de_tres

# Ejemplo de uso
lista_A = [1, 2, 3, 6, 9, 12, 15]
multiplos = multiplos_de_tres_acumulacion(lista_A)
print(multiplos)
# Usando una comprensión de listas:
def multiplos_de_tres_comprension(lista):
    return [numero for numero in lista if numero % 3 == 0]

# Ejemplo de uso
lista_A = [1, 2, 3, 6, 9, 12, 15]
multiplos = multiplos_de_tres_comprension(lista_A)
print(multiplos)

