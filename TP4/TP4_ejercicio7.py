"""
Escribir una función para eliminar una subcadena de una cadena de caracteres, a
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante. Escribir también un programa para verificar el comportamiento de la misma.
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas

"""

def eliminar_subcadena_rebanada(cadena, posicion, cantidad):
    """
    Elimina una subcadena de una cadena de caracteres, a partir de una posición y cantidad de caracteres dadas
    """
    return cadena[:posicion - 1] + cadena[posicion - 1 + cantidad:]

def eliminar_subcadena_sin_rebanada(cadena, posicion, cantidad):
    lista_caracteres = list(cadena)
    del lista_caracteres[posicion - 1:posicion - 1 + cantidad]
    return ''.join(lista_caracteres)

def main():
    print("Eliminar subcadena de una cadena")
    
    cadena = input("Ingrese la cadena: ")
    posicion = int(input("Ingrese la posición inicial de la subcadena a eliminar: "))
    cantidad = int(input("Ingrese la cantidad de caracteres a eliminar: "))
    
    cadena_reemplazada_rebanada = eliminar_subcadena_rebanada(cadena, posicion, cantidad)
    cadena_reemplazada_sin_rebanada = eliminar_subcadena_sin_rebanada(cadena, posicion, cantidad)
    
    print("\nResultados:")
    print("Cadena original:", cadena)
    print("Cadena reemplazada con rebanadas:", cadena_reemplazada_rebanada)
    print("Cadena reemplazada sin rebanadas:", cadena_reemplazada_sin_rebanada)

if __name__ == "__main__":
    main()