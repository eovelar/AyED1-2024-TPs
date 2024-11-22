"""
5. La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
módulo math. Escribir un programa que utilice esta función para calcular la raíz
cuadrada de un número cualquiera ingresado a través del teclado. El programa
debe utilizar manejo de excepciones para evitar errores si se ingresa un número
negativo.

"""
import math

def raiz_cuadrada(num: int) -> float:
    """
    Solicita al usuario un número y devuelve su raíz cuadrada.
    
    Maneja excepciones si se ingresa un número negativo.
    """
    if num < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    
    return math.sqrt(num)

if __name__ == "__main__":
    try:
        num = int(input("Ingrese un número entero para calcular su raíz: ")) 
        raiz = raiz_cuadrada(num)
        print(f"La raíz cuadrada de {num} es {raiz}")  
    except ValueError as e:
        print(f"Solo debe ingresar números enteros. Intente nuevamente. {e}")