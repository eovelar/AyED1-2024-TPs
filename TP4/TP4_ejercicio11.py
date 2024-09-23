"""
Escribir un programa que cuente cuántas veces se encuentra una subcadena dentro
de otra cadena, sin diferenciar mayúsculas y minúsculas. Tener en cuenta que los
caracteres de la subcadena no necesariamente deben estar en forma consecutiva
dentro de la cadena, pero sí respetando el orden de los mismos.
"""
def contar_subcadena(cadena, subcadena):
    """
    Cuenta cuántas veces se encuentra una subcadena dentro de otra cadena, sin diferenciar mayúsculas y minúsculas.
    """
    cadena_min = cadena.lower()
    subcadena_min = subcadena.lower()
    

    coincidencias = 0
    indice = 0
    while indice < len(cadena_min):
        indice_inicio = cadena_min.find(subcadena_min[0], indice)
        if indice_inicio == -1:
            break
        if cadena_min[indice_inicio:indice_inicio + len(subcadena_min)] == subcadena_min:
            coincidencias += 1
        indice = indice_inicio + 1
    return coincidencias

def main():
    cadena = input("Ingrese una cadena: ")
    subcadena = input("Ingrese la sub-cadena a buscar: ")
    cantidad_encontrada = contar_subcadena(cadena, subcadena)
    print("Cadena:", cadena)
    print("Sub-cadena:", subcadena)
    print("Cantidad encontrada:", cantidad_encontrada)

if __name__ == "__main__":
    main()