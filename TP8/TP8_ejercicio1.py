"""
1.Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios, y luego escribir un programa que las vincule:
a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha
válida.
b. Sumar N días a una fecha.
c. Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
segundo se considerará que el primero corresponde al día anterior. En ningún
caso la diferencia en horas puede superar las 24 horas.
"""

from datetime import datetime, timedelta

def ingresar_fecha():
    """
    Ingresa una fecha y verifica que sea válida
    """
    while True:
        fecha_str = input("Ingrese una fecha (dd/mm/yyyy): ")
        try:
            fecha = datetime.strptime(fecha_str, '%d/%m/%Y')
            return (fecha.day, fecha.month, fecha.year)
        except ValueError:
            print("Fecha inválida. Intente de nuevo.")

def sumar_dias(fecha, n):
    dia, mes, año = fecha
    fecha_original = datetime(año, mes, dia)
    nueva_fecha = fecha_original + timedelta(days=n)
    return (nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)

def ingresar_horario():
    """
    Ingresa un horario y verifica que sea correcto
    """
    while True:
        horario_str = input("Ingrese un horario (hh:mm): ")
        try:
            hora, minuto = map(int, horario_str.split(':'))
            if 0 <= hora < 24 and 0 <= minuto < 60:
                return (hora, minuto)
            else:
                print("Horario inválido. Intente de nuevo.")
        except ValueError:
            print("Formato de horario incorrecto. Intente de nuevo.")

def calcular_diferencia(horario1, horario2):
    """
    Calcula la diferencia entre dos horarios
    """
    hora1, minuto1 = horario1
    hora2, minuto2 = horario2

    minutos1 = hora1 * 60 + minuto1
    minutos2 = hora2 * 60 + minuto2

    if minutos1 > minutos2:
        minutos1 -= 24 * 60 

    diferencia_minutos = minutos2 - minutos1

    if diferencia_minutos < 0:
        diferencia_minutos += 24 * 60 
    horas_diferencia = diferencia_minutos // 60
    minutos_diferencia = diferencia_minutos % 60

    return (horas_diferencia, minutos_diferencia)

if __name__ == "__main__":
    
    fecha = ingresar_fecha()
    print(f"Fecha ingresada: {fecha}")

    
    n = int(input("Ingrese la cantidad de días a sumar: "))
    nueva_fecha = sumar_dias(fecha, n)
    print(f"Nueva fecha después de sumar {n} días: {nueva_fecha}")

   
    print("Ingreso del primer horario:")
    horario1 = ingresar_horario()
    print(f"Primer horario ingresado: {horario1}")

    print("Ingreso del segundo horario:")
    horario2 = ingresar_horario()
    print(f"Segundo horario ingresado: {horario2}")

    diferencia = calcular_diferencia(horario1, horario2)
    print(f"Diferencia entre horarios: {diferencia[0]} horas y {diferencia[1]} minutos")