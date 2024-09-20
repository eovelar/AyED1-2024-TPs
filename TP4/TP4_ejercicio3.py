"""
Los números de claves de dos cajas fuertes están intercalados dentro de un número
entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa
para obtener ambas claves, donde la primera se construye con los dígitos ubicados
en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en
posiciones pares. Los dígitos se numeran desde la izquierda. Ejemplo: Si clave
maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89.
"""
def desentraniar_clave(clave_maestra: int) -> tuple:
    """
    Args:
        clave_maestra (int): La clave maestra que contiene las dos claves intercaladas
    
    Returns:
        tuple: Una tupla que contiene las dos claves separadas
    """
    # ConCvierte la clave maestra a una cadena para poder acceder a cada dígito
    clave_maestra_str = str(clave_maestra)

    clave1 = ""
    clave2 = ""
    """
    Recorrer la clave maestra y construir las claves separadas
    """
    for i, digito in enumerate(clave_maestra_str):
        if i % 2 == 0: 
            clave2 += digito
        else: 
            clave1 += digito
    """
    Convierte las claves en enteros y las devuelve
    """
    return int(clave1), int(clave2)

def main() -> None:
    """
    Lee la clave maestra del usuario y desentraña las dos claves separadas
    """
    clave_maestra = int(input("Ingrese la clave maestra: "))
    clave1, clave2 = desentraniar_clave(clave_maestra)
    print("Clave 1:", clave1)
    print("Clave 2:", clave2)

if __name__ == "__main__":
    main()