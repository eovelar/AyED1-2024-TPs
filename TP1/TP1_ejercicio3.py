"""
Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes. 
Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes (detalladas en la tabla de abajo) 
se solicita desarrollar una función que reciba como parámetro la cantidad de viajes realizados en un
determinado mes y devuelva el total gastado en viajes. Realizar también un programa para verificar 
el comportamiento de la función.

Cantidad de viajes:      Valor del pasaje:
1 a 20                   Averiguar en Internet el valor actualizado
21 a 30                  20% de descuento sobre tarifa máxima
31 a 40                  30% de descuento sobre tarifa máxima
Más de 40                40% de descuento sobre tarifa máxima
"""

def gastos(viajes, tarifa_maxima):
    """
    Se cuentan los gastos de los viajes realizados en el mes

    args:
        viajes (int): Cantidad de viajes realizados en un mes.
        tarifa_maxima (float): Valor del pasaje máximo.

    returns:
        float: total gastado en viajes.
    """
    descuento = 0
    if viajes > 20:
        descuento = 0.2 if viajes <= 30 else 0.3 if viajes <= 40 else 0.4
    return viajes * tarifa_maxima * (1 - descuento)

def main():
    """
    Programa para verificar la función
    """
    while True:
        try:
            viajes = int(input("Ingrese la cantidad de viajes realizados en el mes: "))
            if viajes < 0:
                print("Error: La cantidad de viajes debe ser un número positivo.")
            else:
                tarifa_maxima = float(input("Ingrese el valor del pasaje máximo: "))
                gasto_total = gastos(viajes, tarifa_maxima)
                print(f"El total gastado en viajes es: ${gasto_total}")
        except ValueError:
            print("Error: Debe ingresar un número entero o decimal.")

if __name__ == "__main__":
    main()