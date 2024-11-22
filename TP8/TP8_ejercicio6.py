"""
6. Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras
repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras
ordenadas según su longitud. Los signos de puntuación no deben afectar el
proceso.

"""
import string

def eliminar_repetidas(frase):
    """
    Elimina palabras repetidas y las ordena por longitud
    """
    frase_limpia = frase.translate(str.maketrans('', '', string.punctuation))

    palabras = set(frase_limpia.split())

    palabras_ordenadas = sorted(palabras, key=len)
    
    return palabras_ordenadas

if __name__ == "__main__":
    frase = input("Ingrese una frase: ")
    
    resultado = eliminar_repetidas(frase)
    
    print("Palabras únicas ordenadas por longitud:")
    for palabra in resultado:
        print(palabra)