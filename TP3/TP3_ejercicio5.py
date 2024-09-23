"""
Desarrollar un programa que permita realizar reservas en una sala de cine de N
filas con M butacas por cada fila. Desarrollar las siguientes funciones y utilizarlas
en un mismo programa:
mostrar_butacas: Mostrará por pantalla el estado de cada una de las butacas
del cine. Esta función deberá ser invocada antes de que se realice la reserva, y
se volverá a invocar luego de la misma con los estados actualizados.
reservar: Deberá recibir una matriz y la butaca seleccionada, y actualizará la
sala en caso de estar disponible dicha butaca. La función devolverá True/False
si logró o no reservar la butaca.
cargar_sala: Recibirá una matriz como parámetro y la cargará con valores
aleatorios para simular una sala con butacas ya reservadas.
butacas_libres: Recibirá como parámetro la matriz y retornará cuántas butacas desocupadas hay en la sala.
butacas_contiguas: Buscará la secuencia más larga de butacas libres contiguas en una misma fila 
y devolverá las coordenadas de inicio de la misma. 
"""
import random as rn

def mostrar_butacas(sala):
    """
    Muestra el estado de cada una de las butacas
    """
    for i in range(len(sala)):
        for j in range(len(sala[i])):
            if sala[i][j] == 0:
                print("L", end=" ")  
            else:
                print("O", end=" ")  
        print()

def reservar(sala, fila, columna):
    """
    Reserva una butaca en la sala de cine.
    """
    if sala[fila][columna] == 0:
        sala[fila][columna] = 1 
        return True
    else:
        return False

def cargar_sala(sala):
    """
    Carga la sala de cine con valores aleatorios para simular butacas ya reservadas
    0: butaca libre, 1: butaca ocupada

    """
    for i in range(len(sala)):
        for j in range(len(sala[i])):
            sala[i][j] = rn.randint(0, 1) 

def butacas_libres(sala):
    """
    Retorna cuántas butacas desocupadas hay en la sala
    """
    libres = 0
    for i in range(len(sala)):
        for j in range(len(sala[i])):
            if sala[i][j] == 0:
                libres += 1
    return libres

def butacas_contiguas(sala):
    """
    Busca la secuencia más larga de butacas libres contiguas en una misma fila y devuelve las coordenadas de inicio de la misma

    """
    max_contiguas = 0
    coordenadas_inicio = (-1, -1)
    for i in range(len(sala)):
        contiguas = 0
        for j in range(len(sala[i])):
            if sala[i][j] == 0:
                contiguas += 1
                if contiguas > max_contiguas:
                    max_contiguas = contiguas
                    coordenadas_inicio = (i, j - contiguas + 1)
            else:
                contiguas = 0
    return coordenadas_inicio

"""
Crea sala de cine con 5 filas y 10 butacas por fila
"""
sala = [[0 for _ in range(10)] for _ in range(5)]

"""
Carga sala con valores aleatorios
"""
cargar_sala(sala)

print("Estado inicial de la sala:")
mostrar_butacas(sala)

"""
Reservar butaca en la fila 2, columna 5
"""
if reservar(sala, 2, 5):
    print("La reserva se realizó exitosamente")
else:
    print("Esta butaca ya no se encuentra disponible")

"""
Mostrar estado actual de la sala
"""
print(":")
mostrar_butacas(sala)

"""
Mostrar número de butacas libres en total
"""
print(f"Butacas libres: {butacas_libres(sala)}")

# Mostrar coordenadas de inicio de la secuencia de butacas libres contiguas
coordenadas_inicio = butacas_contiguas(sala)
if coordenadas_inicio != (-1, -1):
    print(f"La secuencia de butacas libres contiguas se encuentra en la fila {coordenadas_inicio[0]} desde la columna {coordenadas_inicio[1]}")
else:
    print("No hay secuencias de butacas libres contiguas.")