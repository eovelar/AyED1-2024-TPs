"""
Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En
qué cambiaría la función si el rango de valores fuese diferente?
"""
def romano(num: int) -> str:
    """
    Convierte un número entero entre 0 y 3999 a un número romano
    
    Args:
        num (int): El número entero a convertir
    
    Returns:
        str: El número romano correspondiente
    """
    decimales = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    simbolo = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // decimales[i]):
            roman_num += simbolo[i]
            num -= decimales[i]
        i += 1
    return roman_num

def main() -> None:
    """
    Lee un número entero y lo convierte a número romano
    """
    num = int(input("Ingrese un número entero entre 0 y 3999: "))
    if 0 <= num <= 3999:
        print(romano(num))
    else:
        print("El número debe estar entre 0 y 3999")

if __name__ == "__main__":
    main()