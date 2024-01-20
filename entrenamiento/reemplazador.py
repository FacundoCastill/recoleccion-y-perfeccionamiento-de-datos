import re

def reemplazar_texto(archivo_entrada, archivo_salida, reemplazos):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as file:
            contenido = file.read()

        for viejo_texto, nuevo_texto in reemplazos.items():
            contenido = re.sub(re.escape(viejo_texto), nuevo_texto, contenido)

        with open(archivo_salida, 'w', encoding='utf-8') as file:
            file.write(contenido)

        print(f"Reemplazo completado. El resultado se guardó en {archivo_salida}")

    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo: {archivo_entrada}")
    except Exception as e:
        print(f"Se produjo un error: {e}")

archivo_entrada = r'direccion\de\entrada\archivoentrada.txt'
archivo_salida = r'direccion\de\salida\archivosalida.txt'

reemplazos = {
    'a': 'usuario a',
    'b': 'usuario b'
}

reemplazar_texto(archivo_entrada, archivo_salida, reemplazos)