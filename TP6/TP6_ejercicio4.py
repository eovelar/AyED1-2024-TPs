"""
4. Desarrollar un programa para eliminar todos los comentarios de un programa escrito en lenguaje Python. Tener en cuenta que los comentarios comienzan con el
signo # (siempre que éste no se encuentre encerrado entre comillas simples o dobles) y que también se considera comentario a las cadenas de documentación
(docstrings).
"""
import re

def eliminar_comentarios(archivo_entrada, archivo_salida):
    """
    Elimina comentarios y cadenas de documentación (docstrings) de un archivo Python.
    """
    with open(archivo_entrada, 'r', encoding='utf-8') as f_in:
        contenido = f_in.read()

    contenido = re.sub(r'#.*$', '', contenido, flags=re.MULTILINE)
    contenido = re.sub(r'''(?:\'\'\'|\"\"\")[\s\S]*?(?:\'\'\'|\"\"\")''', '', contenido)

    with open(archivo_salida, 'w', encoding='utf-8') as f_out:
        f_out.write(contenido)

if __name__ == "__main__":
    archivo_entrada = input("Ingrese el nombre del archivo a procesar: ")
    archivo_salida = input("Ingrese el nombre del archivo de salida: ")
    eliminar_comentarios(archivo_entrada, archivo_salida)
    print("Comentarios eliminados con éxito.")