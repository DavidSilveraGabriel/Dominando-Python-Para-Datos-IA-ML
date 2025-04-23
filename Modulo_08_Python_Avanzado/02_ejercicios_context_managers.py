# Ejercicios: Módulo 8 - Context Managers (`with` statement)

import time
from contextlib import contextmanager

print("--- Context Managers y la Sentencia `with` ---")

# --- Ejercicio 1: Uso Básico de `with open()` ---
# Instrucciones:
# 1. Usa la sentencia `with` para abrir (o crear si no existe) un archivo llamado `ejemplo_with.txt` en modo escritura (`'w'`).
# 2. Dentro del bloque `with`, escribe dos líneas en el archivo: "Primera línea con with." y "Segunda línea.".
# 3. Después del bloque `with`, intenta escribir una tercera línea en el mismo objeto archivo (esto debería fallar o el archivo ya debería estar cerrado). Comenta por qué.
# 4. Vuelve a abrir el archivo `ejemplo_with.txt` en modo lectura (`'r'`) usando `with` e imprime su contenido.

print("--- Ejercicio 1: Uso Básico de `with open()` ---")
nombre_archivo = "ejemplo_with.txt"

# 1, 2. Escribir en el archivo usando with
try:
    print(f"\nEscribiendo en '{nombre_archivo}'...")
    with open(nombre_archivo, 'w') as f:
        print(f"Archivo abierto: {not f.closed}")
        f.write("Primera línea con with.\n")
        f.write("Segunda línea.\n")
    print(f"Archivo cerrado después del bloque with: {f.closed}") # Debería estar cerrado
except IOError as e:
    print(f"Error al escribir en el archivo: {e}")

# 3. Intentar escribir fuera del bloque with
# f.write("Tercera línea (fallará)\n") # Descomentar esto causará un ValueError: I/O operation on closed file
# Explicación: La sentencia `with` garantiza que el método `__exit__` del
# context manager del archivo (que cierra el archivo) se llame automáticamente
# al salir del bloque, incluso si ocurren excepciones. Por lo tanto, `f` ya está cerrado aquí.
print("\nIntento de escritura fuera de 'with' fallaría (comentado).")

# 4. Leer el archivo usando with
print(f"\nLeyendo contenido de '{nombre_archivo}':")
try:
    with open(nombre_archivo, 'r') as f:
        contenido = f.read()
        print(contenido)
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no se encontró para lectura.")
except IOError as e:
    print(f"Error al leer el archivo: {e}")

print("-" * 20)


# --- Ejercicio 2: Crear un Context Manager con una Clase ---
# Instrucciones:
# 1. Define una clase `Temporizador` que actúe como un context manager.
# 2. En `__init__`, inicializa una variable para guardar el tiempo de inicio.
# 3. En `__enter__`:
#    a. Guarda el tiempo de inicio actual (`time.perf_counter()`).
#    b. Imprime "Iniciando temporizador...".
#    c. Devuelve `self` (el objeto temporizador).
# 4. En `__exit__`:
#    a. Guarda el tiempo de finalización (`time.perf_counter()`).
#    b. Calcula la duración (tiempo final - tiempo inicial).
#    c. Imprime el tiempo transcurrido formateado (ej. "Bloque ejecutado en: X.YYYY segundos").
#    d. Los argumentos `exc_type`, `exc_val`, `exc_tb` indican si ocurrió una excepción. Por ahora, no hagas manejo especial de excepciones (devuelve `None` o `False` implícitamente).
# 5. Usa tu context manager `Temporizador` con una sentencia `with` para medir cuánto tarda un bloque de código simple (ej. un bucle `for` que haga alguna operación o un `time.sleep(0.5)`).

print("\n--- Ejercicio 2: Context Manager con Clase ---")

# 1, 2, 3, 4. Definir la clase Temporizador
class Temporizador:
    def __init__(self):
        self._tiempo_inicio = None
        print("Temporizador listo.")

    def __enter__(self):
        self._tiempo_inicio = time.perf_counter()
        print("Iniciando temporizador...")
        return self # Devolver el objeto permite usar 'as' si fuera necesario

    def __exit__(self, exc_type, exc_val, exc_tb):
        tiempo_fin = time.perf_counter()
        duracion = tiempo_fin - self._tiempo_inicio
        print(f"Bloque ejecutado en: {duracion:.4f} segundos")
        # No manejamos excepciones explícitamente aquí,
        # si devolvemos False (o nada/None), las excepciones se propagan.
        # Si devolviéramos True, indicaríamos que la excepción fue manejada.
        return False # Propagar excepciones si ocurren

# 5. Usar el context manager
print("\nUsando el Temporizador:")
with Temporizador():
    # Código cuya duración queremos medir
    print("Realizando alguna tarea...")
    time.sleep(0.75) # Simular trabajo
    resultado_tarea = sum(i for i in range(10000)) # Otra tarea rápida
    print("Tarea finalizada.")

# Ejemplo con excepción (para ver que se propaga)
# print("\nUsando el Temporizador con una excepción:")
# try:
#     with Temporizador():
#         print("Haciendo algo que fallará...")
#         time.sleep(0.1)
#         x = 1 / 0 # Generar ZeroDivisionError
# except ZeroDivisionError as e:
#     print(f"Excepción capturada fuera del 'with': {e}")
# Notar que __exit__ se ejecuta incluso si hay excepción.

print("-" * 20)


# --- Ejercicio 3: Crear un Context Manager con `contextlib.contextmanager` ---
# Instrucciones:
# 1. Importa `contextmanager` de `contextlib`.
# 2. Define una función generadora llamada `gestor_recurso_simple(nombre_recurso)`.
# 3. Dentro de la función:
#    a. Imprime un mensaje indicando que se está "Adquiriendo" el recurso `nombre_recurso`.
#    b. Usa `yield` para ceder el control (este es el punto donde se ejecuta el bloque `with`). Puedes hacer `yield nombre_recurso` si quieres que el `as` reciba algo.
#    c. Después del `yield`, imprime un mensaje indicando que se está "Liberando" el recurso `nombre_recurso`. Asegúrate de que este código de limpieza se ejecute incluso si hay excepciones en el bloque `with` (usa `try...finally`).
# 4. Decora tu función generadora con `@contextmanager`.
# 5. Usa tu nuevo context manager `gestor_recurso_simple` con una sentencia `with` para simular la gestión de un recurso llamado "Conexión BD". Dentro del `with`, imprime un mensaje como "Usando la Conexión BD...".

print("\n--- Ejercicio 3: Context Manager con `@contextmanager` ---")

# 1. Importar (hecho al principio)
# from contextlib import contextmanager

# 2, 3, 4. Definir y decorar la función generadora
@contextmanager
def gestor_recurso_simple(nombre_recurso):
    """Context manager simple usando el decorador @contextmanager."""
    print(f"Adquiriendo recurso: '{nombre_recurso}'...")
    # Código de setup aquí (si fuera necesario)
    try:
        yield nombre_recurso # Ceder control y opcionalmente devolver un valor
    finally:
        # Código de limpieza aquí (se ejecuta siempre)
        print(f"Liberando recurso: '{nombre_recurso}'...")

# 5. Usar el context manager
print("\nUsando gestor_recurso_simple:")
with gestor_recurso_simple("Conexión BD") as recurso:
    print(f"-> Bloque 'with': Usando '{recurso}'...")
    # Simular trabajo con el recurso
    time.sleep(0.2)
    print("-> Bloque 'with': Terminando de usar el recurso.")

# Ejemplo con excepción
# print("\nUsando gestor_recurso_simple con excepción:")
# try:
#     with gestor_recurso_simple("Archivo Temporal") as recurso:
#         print(f"-> Bloque 'with': Usando '{recurso}'...")
#         raise ValueError("¡Algo salió mal dentro del with!")
# except ValueError as e:
#     print(f"Excepción capturada fuera del 'with': {e}")
# Notar que la limpieza ("Liberando recurso...") se ejecuta igualmente.

print("-" * 20)

# --- Fin de los ejercicios ---
