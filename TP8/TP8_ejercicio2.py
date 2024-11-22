"""
2. Escribir una función que reciba como parámetro una tupla conteniendo una fecha
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada
en formato extendido. La función debe contemplarse que el año se ingrese en dos
dígitos, los que serán interpretados según un año de corte definido dentro del
programa. Cualquier año mayor que éste se considerará del siglo pasado. Por
ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030"
para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de
1931". Si el año se ingresa en cuatro dígitos el año de corte no será tenido en
cuenta. Escribir también un programa para ingresar los datos, invocar a la función y
mostrar el resultado.

"""

def formato_fecha(fecha, anio_corte=30):
    """Convierte una tupla de fecha (día, mes, año) en formato extendido."""
    dia, mes, anio = fecha

    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }

    if anio < 100:
        if anio > anio_corte:
            anio += 1900  
        else:
            anio += 2000  

    fecha_formateada = f"{dia} de {meses[mes]} de {anio}"
    return fecha_formateada

if __name__ == "__main__":
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes (1-12): "))
    anio = int(input("Ingrese el año (puede ser en dos o cuatro dígitos): "))

    fecha = (dia, mes, anio)

    resultado = formato_fecha(fecha)
    print("La fecha en formato extendido es:", resultado)