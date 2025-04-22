# Ejercicios: Módulo 2 - Manejo de Ficheros

# --- Preparación ---
# Define el nombre del archivo que usaremos en los ejercicios
nombre_archivo = "mi_archivo_ejercicio.txt"

# --- Ejercicio 1: Escritura en Archivo ('w') ---
# Instrucciones:
# 1. Usa `with open()` para abrir el archivo `nombre_archivo` en modo escritura ('w').
#    Recuerda usar `encoding="utf-8"` para buena compatibilidad.
# 2. Dentro del bloque `with`, escribe tres líneas en el archivo usando `f.write()`:
#    - "Línea 1: Hola desde Python."
#    - "Línea 2: Aprendiendo a escribir archivos."
#    - "Línea 3: ¡Es genial!"
#    Asegúrate de añadir el carácter de nueva línea `\n` al final de cada `write()`
#    para que cada texto aparezca en una línea separada en el archivo.
# 3. Imprime un mensaje indicando que el archivo ha sido escrito.

print(f"--- Ejercicio 1: Escribiendo en '{nombre_archivo}' (modo 'w') ---")
# Escribe tu código aquí
try:
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("Línea 1: Hola desde Python.\n")
        f.write("Línea 2: Aprendiendo a escribir archivos.\n")
        f.write("Línea 3: ¡Es genial!\n")
    print(f"Archivo '{nombre_archivo}' escrito correctamente.")
except Exception as e:
    print(f"Error al escribir el archivo: {e}")


# --- Ejercicio 2: Lectura Completa de Archivo ('r') ---
# Instrucciones:
# 1. Usa `with open()` para abrir el MISMO archivo `nombre_archivo` en modo lectura ('r').
#    No olvides el `encoding="utf-8"`.
# 2. Dentro del bloque `with`, lee TODO el contenido del archivo usando `f.read()`
#    y almacénalo en una variable llamada `contenido`.
# 3. Imprime un encabezado y luego imprime el valor de la variable `contenido`.

print(f"\n--- Ejercicio 2: Leyendo '{nombre_archivo}' completo (modo 'r') ---")
# Escribe tu código aquí
try:
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        contenido = f.read()
    print("Contenido leído del archivo:")
    print(contenido)
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
except Exception as e:
    print(f"Error al leer el archivo: {e}")


# --- Ejercicio 3: Añadir Contenido a Archivo ('a') ---
# Instrucciones:
# 1. Usa `with open()` para abrir de nuevo `nombre_archivo`, pero esta vez en modo
#    añadir ('a', append). Usa `encoding="utf-8"`.
# 2. Dentro del bloque `with`, escribe dos líneas adicionales:
#    - "Línea 4: Añadiendo más texto."
#    - "Línea 5: El modo 'a' no sobrescribe."
#    Recuerda añadir `\n`.
# 3. Imprime un mensaje indicando que se ha añadido contenido.

print(f"\n--- Ejercicio 3: Añadiendo a '{nombre_archivo}' (modo 'a') ---")
# Escribe tu código aquí
try:
    with open(nombre_archivo, "a", encoding="utf-8") as f:
        f.write("Línea 4: Añadiendo más texto.\n")
        f.write("Línea 5: El modo 'a' no sobrescribe.\n")
    print(f"Contenido añadido a '{nombre_archivo}'.")
except Exception as e:
    print(f"Error al añadir al archivo: {e}")


# --- Ejercicio 4: Lectura Línea por Línea (Iteración) ---
# Instrucciones:
# 1. Usa `with open()` para abrir `nombre_archivo` en modo lectura ('r') con UTF-8.
# 2. Dentro del bloque `with`, usa un bucle `for` para iterar directamente sobre
#    el objeto archivo (`for linea in f:`).
# 3. Dentro del bucle, imprime cada `linea`. Usa `.strip()` en la línea para
#    eliminar los saltos de línea extra que `print()` podría añadir y los que
#    ya vienen en la línea leída. Puedes formatear la salida si quieres,
#    por ejemplo: `print(f"Leído: {linea.strip()}")`.

print(f"\n--- Ejercicio 4: Leyendo '{nombre_archivo}' línea por línea ---")
# Escribe tu código aquí
try:
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        print("Contenido leído línea por línea:")
        for i, linea in enumerate(f):
            print(f"Línea {i+1}: {linea.strip()}")
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
except Exception as e:
    print(f"Error al leer el archivo línea por línea: {e}")


# --- Ejercicio 5: Manejo de Archivo Inexistente ---
# Instrucciones:
# 1. Intenta abrir un archivo que SABES que no existe (p.ej., "archivo_inexistente_qwerty.txt")
#    en modo lectura ('r') usando `with open()`.
# 2. Envuelve la declaración `with open()` en un bloque `try...except FileNotFoundError`.
# 3. En el bloque `except`, imprime un mensaje claro indicando que el archivo no se encontró.

print("\n--- Ejercicio 5: Manejando FileNotFoundError ---")
# Escribe tu código aquí
archivo_fantasma = "archivo_inexistente_qwerty.txt"
try:
    print(f"Intentando abrir '{archivo_fantasma}'...")
    with open(archivo_fantasma, "r", encoding="utf-8") as f:
        contenido_fantasma = f.read()
        print("¡Esto no debería imprimirse!")
except FileNotFoundError:
    print(f"¡Correcto! El archivo '{archivo_fantasma}' no existe y se manejó el error.")
except Exception as e:
    print(f"Ocurrió un error inesperado diferente a FileNotFoundError: {e}")


# --- Limpieza Opcional ---
# import os
# if os.path.exists(nombre_archivo):
#     os.remove(nombre_archivo)
#     print(f"\nArchivo de ejercicio '{nombre_archivo}' eliminado.")

# --- Fin de los ejercicios ---
