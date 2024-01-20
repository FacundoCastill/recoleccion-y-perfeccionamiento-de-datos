import re

def eliminar_marcas_temporales(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as file:
            contenido = file.read()

        contenido_sin_marcas = re.sub(r'\d{1,2}/\d{1,2}/\d{4}, \d{1,2}:\d{2} - ', '', contenido)

        with open(archivo_salida, 'w', encoding='utf-8') as file:
            file.write(contenido_sin_marcas)

        print(f"Eliminación de marcas temporales completada. El resultado se guardó en {archivo_salida}")

    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo: {archivo_entrada}")
    except Exception as e:
        print(f"Se produjo un error: {e}")

archivo_entrada = r'archivos\chat.txt'
archivo_salida = r'archivos\chat_sin_marcas.txt'

eliminar_marcas_temporales(archivo_entrada, archivo_salida)