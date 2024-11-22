"""
3. Desarrollar una función que devuelva una cadena de caracteres con el nombre del
mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
obtenerse de una lista de cadenas de caracteres inicializada dentro de la función.
Devolver una cadena vacía si el número de mes es inválido. La detección de meses
inválidos deberá realizarse a través de excepciones.
"""
def nombre_mes(num_mes: int) -> str:
    """
    Devuelve el nombre del mes correspondiente al número ingresado.

    Args:
        numero_mes (int): Número del mes (1-12).

    Returns:
        str: Nombre del mes correspondiente, o cadena vacía si el número no es válido.
    """

    meses = [
        "Enero", 
        "Febrero", 
        "Marzo", 
        "Abril", 
        "Mayo", 
        "Junio",
        "Julio", 
        "Agosto", 
        "Septiembre", 
        "Octubre", 
        "Noviembre", 
        "Diciembre"
    ]
    
    try:
        """
        Verifica si el número de mes está en el rango válido
        """
        if num_mes < 1 or num_mes > 12:
            raise ValueError("Número de mes inválido")
        
        return meses[num_mes - 1] 
    
    except ValueError:
        """
        Devuelve una cadena vacía si hay un error
        """
        return ""

if __name__ == "__main__":
    mes = int(input("Ingrese el número del mes: "))
    nombre_mes = nombre_mes(mes)
    
    if nombre_mes:
        print(f"El nombre del mes es: {nombre_mes}")
    else:
        print("Número inválido, únicamente ingrese números del 1 al 12")
    
    