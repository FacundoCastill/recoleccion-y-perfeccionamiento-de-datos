import re

def eliminar_texto_especifico(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as file:
            contenido = file.read()

        contenido_sin_texto_especifico = re.sub(r'usuario: Eliminaste este mensaje\.|bot: <Multimedia omitido>|usuario: <Multimedia omitido>', '', contenido)

        with open(archivo_salida, 'w', encoding='utf-8') as file:
            file.write(contenido_sin_texto_especifico)

        print(f"Eliminación de textos específicos completada. El resultado se guardó en {archivo_salida}")

    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo: {archivo_entrada}")
    except Exception as e:
        print(f"Se produjo un error: {e}")

archivo_entrada = r'eliminartexto\chat.txt'
archivo_salida = r'eliminartexto\chat_sin_texto_especifico.txt'

eliminar_texto_especifico(archivo_entrada, archivo_salida)