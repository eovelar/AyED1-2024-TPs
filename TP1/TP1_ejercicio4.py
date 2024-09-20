"""
Un comercio de electrodomésticos necesita para su línea de cajas un programa que
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
dos números enteros, correspondientes al total de la compra y al dinero recibido.
Informar cuántos billetes de cada denominación deben ser entregados como vuelto,
de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes
de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el
dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta
de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se
abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1
billete de $200, 1 billete de $100 y 3 billetes de $10.
"""

def cambio(compra, dinero):
    """
    Calcula el cambio que debe entregarle al cliente
    """
    billetes = [5000, 1000, 500, 200, 100, 50, 10]

    try:
        # Verifica si el monto recibido es suficiente
        if recibido < total:
            raise ValueError("Pago insuficiente")

        # Calcula el cambio
        cambio = recibido - total

        # Inicializa conteo de billetes
        conteo_billetes = {}

        # Itera sobre los billetes
        for billete in billetes:
            cuenta = cambio // billete
            if cuenta > 0:
                conteo_billetes[billete] = cuenta
                cambio -= cuenta * billete

        # Verifica si el cambio se puede realizar con los billetes disponibles
        if cambio > 0:
            raise ValueError("No se puede realizar el cambio con los billetes disponibles")

        return conteo_billetes

    except ValueError as e:
        return f"Error: {e}"