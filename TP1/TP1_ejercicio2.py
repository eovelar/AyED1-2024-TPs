"""
Desarrollar una función que reciba tres números enteros positivos correspondientes
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
Devolver True o False según la fecha sea correcta o no. Realizar también un
programa para verificar el comportamiento de la función.
"""

def anio_bisiesto(anio):
    """
    Verifica si un año es bisiesto.

    Args:
        anio (int): Año.

    Returns:
        bool: True si el año es bisiesto, False en caso contrario.
    """
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

def fecha_valida(dia, mes, anio):
    """
    Verifica si una fecha es válida.

    Args:
        dia (int): día (1-31)
        mes (int): mes (1-12)
        anio (int): año

    Returns:
        bool: True si la fecha es válida, False en caso contrario.
    """

    if mes < 1 or mes > 12:
        return False
    """
    Verificar si el día es válido según el mes
    """
    if mes in [1, 3, 5, 7, 8, 10, 12]: 
        if dia < 1 or dia > 31:
            return False
    elif mes in [4, 6, 9, 11]: 
        if dia < 1 or dia > 30:
            return False
    elif mes == 2:  # Febrero
        if anio_bisiesto(anio):
            if dia < 1 or dia > 29:
                return False
        else:
            if dia < 1 or dia > 28:
                return False
    """
    Si se cumplen todas las condiciones anteriores, la fecha es válida
    """
    return True

def main():
    """
    Se le pide al usuario ingresar los datos de la fecha
    """
    while True:
        try:
            dia = int(input("Ingrese el día: "))
            mes = int(input("Ingrese el mes: "))
            anio = int(input("Ingrese el año: "))
            if fecha_valida(dia, mes, anio):
                print("La fecha es válida")
            else:
                print("La fecha no es correcta")
        except ValueError:
            print("Error! Ingrese solamente números enteros")

if __name__ == "__main__":
    main()