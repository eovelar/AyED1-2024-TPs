""" 
Desarrollar una función que reciba tres números enteros positivos y devuelva el
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar
también un programa para ingresar los tres valores, invocar a la función y mostrar
el máximo hallado, o un mensaje informativo si éste no existe.

""" 

def mayor(a, b, c):
    """ 
    Encuentra el número mayor entre los 3 números
    """ 
    numeros = [a, b, c]
    mayor_n = max(numeros)
    if numeros.count(mayor_n) == 1:
        return mayor_n
    else:
        return -1
        
def main():
    """
    Solicita al usuario que ingrese los números
    """
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    c = int(input("Ingrese el tercer número: "))
    
    maximo = mayor(a, b, c)
    
    if maximo == -1:
        print("No hay un valor mayor único entre los tres números")
    else:
        print(f"El valor mayor es {maximo}")

if __name__ == "__main__":
    main()
