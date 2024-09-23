"""
Desarrollar una función para reemplazar todas las apariciones de una palabra por
otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la
cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse
palabras completas, y no fragmentos de palabras. Escribir también un programa
para verificar el comportamiento de la función
"""

def reemplazar_palabra(cadena, palabra_original, palabra_nueva):
    """
    Reemplaza todas las apariciones de una palabra por otra en una cadena de caracteres
    """
    palabras = cadena.split()
    reemplazos = 0
    palabras_reemplazadas = [palabra_nueva if palabra == palabra_original else palabra for palabra in palabras]
    cadena_reemplazada = ' '.join(palabras_reemplazadas)
    reemplazos = len([palabra for palabra in palabras if palabra == palabra_original])
    
    return cadena_reemplazada, reemplazos

def main():
    print("Reemplazo de palabras en una cadena")
    
    cadena = input("Ingrese la cadena: ")
    palabra_original = input("Ingrese la palabra a reemplazar: ")
    palabra_nueva = input("Ingrese la palabra nueva: ")
    
    cadena_reemplazada, reemplazos = reemplazar_palabra(cadena, palabra_original, palabra_nueva)
    
    print("\nResultados:")
    print("Cadena original:", cadena)
    print("Cadena reemplazada:", cadena_reemplazada)
    print("Reemplazos realizados:", reemplazos)

if __name__ == "__main__":
    main()