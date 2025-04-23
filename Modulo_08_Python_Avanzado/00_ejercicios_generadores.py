# Ejercicios: Módulo 8 - Generadores

import time
import sys

print("--- Conceptos y Uso de Generadores ---")

# --- Ejercicio 1: Función Generadora Simple ---
# Instrucciones:
# 1. Define una función generadora llamada `contar_hasta(n)` que use `yield`
#    para producir números desde 0 hasta `n-1`.
# 2. Crea un objeto generador llamando a `contar_hasta(5)`.
# 3. Itera sobre el objeto generador usando un bucle `for` e imprime cada número generado.
# 4. Intenta iterar sobre el mismo objeto generador una segunda vez. ¿Qué sucede? (Comenta la respuesta).

print("--- Ejercicio 1: Función Generadora Simple ---")
# Escribe tu código aquí

# 1. Definir función generadora
def contar_hasta(n):
    print("Iniciando generador...")
    i = 0
    while i < n:
        print(f"Yielding {i}")
        yield i
        i += 1
    print("Generador finalizado.")

# 2. Crear objeto generador
generador_nums = contar_hasta(5)
print(f"Tipo de generador_nums: {type(generador_nums)}")

# 3. Iterar sobre el generador (primera vez)
print("\nPrimera iteración:")
for numero in generador_nums:
    print(f"Recibido: {numero}")

# 4. Intentar iterar de nuevo
print("\nSegunda iteración (intento):")
for numero in generador_nums:
    print(f"Recibido en segunda iteración: {numero}") # No debería imprimir nada

# Respuesta a 4: No sucede nada en la segunda iteración. Un generador se agota
# después de ser consumido por completo una vez. Para volver a obtener los valores,
# necesitarías crear una nueva instancia del generador llamando a contar_hasta(5) de nuevo.

print("-" * 20)


# --- Ejercicio 2: Expresión Generadora ---
# Instrucciones:
# 1. Crea una lista de números `mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`.
# 2. Usa una *expresión generadora* para crear un generador que produzca el cuadrado
#    de cada número par en `mi_lista`. Guarda el generador en `gen_cuadrados_pares`.
# 3. Itera sobre `gen_cuadrados_pares` e imprime cada valor generado.
# 4. Compara el uso de memoria de una expresión generadora vs. una comprensión de lista
#    que haga lo mismo (calcula el tamaño usando `sys.getsizeof()`). (Opcional pero ilustrativo).

print("\n--- Ejercicio 2: Expresión Generadora ---")
# Escribe tu código aquí

# 1. Lista original
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Lista original: {mi_lista}")

# 2. Crear expresión generadora
gen_cuadrados_pares = (n**2 for n in mi_lista if n % 2 == 0)
print(f"Tipo de gen_cuadrados_pares: {type(gen_cuadrados_pares)}")

# 3. Iterar e imprimir
print("\nCuadrados de números pares (generador):")
for cuadrado in gen_cuadrados_pares:
    print(cuadrado)

# 4. Comparación de memoria (Opcional)
lista_cuadrados_pares = [n**2 for n in mi_lista if n % 2 == 0]
# Recrear el generador para medirlo antes de consumirlo
gen_cuadrados_pares_mem = (n**2 for n in mi_lista if n % 2 == 0)

size_lista = sys.getsizeof(lista_cuadrados_pares)
size_generador = sys.getsizeof(gen_cuadrados_pares_mem)

print(f"\nTamaño en memoria de la lista: {size_lista} bytes")
print(f"Tamaño en memoria del generador: {size_generador} bytes")
print("Nota: El tamaño del generador es constante (representa el objeto iterador),")
print("mientras que el tamaño de la lista crece con el número de elementos.")

print("-" * 20)


# --- Ejercicio 3: Generador para Leer Archivo Línea por Línea ---
# Instrucciones:
# 1. (Preparación) Crea manualmente un archivo de texto simple llamado `mi_archivo.txt`
#    en el mismo directorio que este script. Escribe algunas líneas de texto en él.
#    Ejemplo de contenido para `mi_archivo.txt`:
#    ```
#    Esta es la primera línea.
#    Aquí viene la segunda.
#    Y finalmente, la tercera.
#    ```
# 2. Define una función generadora `leer_lineas(nombre_archivo)` que abra el archivo
#    especificado, lea cada línea usando un bucle `for` sobre el objeto archivo,
#    y use `yield` para devolver cada línea (puedes quitarle el salto de línea final
#    con `.strip()` si quieres). Asegúrate de que el archivo se cierre correctamente
#    (puedes usar `with open(...)`).
# 3. Usa tu generador `leer_lineas` para iterar sobre `mi_archivo.txt` e imprimir cada línea.
# 4. ¿Cuál es la ventaja de usar un generador para leer archivos grandes en lugar de
#    leer todo el contenido en memoria de una vez? (Comenta la respuesta).

print("\n--- Ejercicio 3: Generador para Leer Archivo ---")
# Escribe tu código aquí

# 1. (Asegúrate de que mi_archivo.txt existe)
nombre_fichero = "mi_archivo.txt"
try:
    # Crear archivo si no existe para el ejemplo
    with open(nombre_fichero, "w") as f:
        f.write("Esta es la primera línea.\n")
        f.write("Aquí viene la segunda.\n")
        f.write("Y finalmente, la tercera.\n")
    print(f"Archivo '{nombre_fichero}' creado/asegurado para el ejercicio.")
except IOError as e:
    print(f"Error al crear el archivo de ejemplo: {e}")
    # Salir si no se puede crear el archivo
    sys.exit(1)


# 2. Definir función generadora
def leer_lineas(nombre_archivo):
    print(f"\nAbriendo archivo '{nombre_archivo}' con generador...")
    try:
        with open(nombre_archivo, 'r') as f:
            for linea in f:
                yield linea.strip() # Quitar saltos de línea
        print("Archivo cerrado por el generador.")
    except FileNotFoundError:
        print(f"Error: Archivo '{nombre_archivo}' no encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")


# 3. Usar el generador
print("\nLeyendo líneas con el generador:")
lector = leer_lineas(nombre_fichero)
try:
    for linea_leida in lector:
        print(f"  '{linea_leida}'")
except Exception as e:
    print(f"Ocurrió un error durante la lectura: {e}")


# 4. Ventaja de los generadores para archivos grandes
# Respuesta: La principal ventaja es la eficiencia de memoria. Un generador
# lee y procesa el archivo línea por línea (o bloque por bloque), cargando
# solo una pequeña porción del archivo en memoria a la vez. En contraste,
# leer todo el archivo (`f.readlines()` o `f.read()`) cargaría el contenido
# completo en memoria, lo cual puede ser inviable o muy lento para archivos
# de gigabytes o terabytes. Los generadores permiten procesar archivos
# enormes con un uso de memoria constante y bajo.

print("\nVentaja de generadores para archivos grandes: Eficiencia de memoria.")
print("-" * 20)


# --- Ejercicio 4: Generadores Infinitos (con precaución) ---
# Instrucciones:
# 1. Define una función generadora `generador_pares()` que genere una secuencia
#    infinita de números pares (0, 2, 4, 6, ...). Usa un bucle `while True`.
# 2. Crea una instancia del generador.
# 3. Usa un bucle `for` para obtener e imprimir los primeros 5 números pares
#    generados. **Importante:** Asegúrate de tener una condición de salida
#    (ej. `if numero_par > 8: break`) dentro del bucle `for` para evitar
#    un bucle infinito.

print("\n--- Ejercicio 4: Generador Infinito ---")
# Escribe tu código aquí

# 1. Definir generador infinito
def generador_pares():
    num = 0
    while True:
        yield num
        num += 2

# 2. Crear instancia
pares_infinitos = generador_pares()

# 3. Iterar con condición de salida
print("Primeros 5 números pares generados:")
count = 0
for numero_par in pares_infinitos:
    print(numero_par)
    count += 1
    if count >= 5: # Condición de salida
        break

# También podríamos usar islice de itertools
# from itertools import islice
# print("\nUsando islice para obtener los primeros 5:")
# pares_infinitos_2 = generador_pares() # Nueva instancia
# for numero_par in islice(pares_infinitos_2, 5):
#     print(numero_par)

print("-" * 20)

# --- Fin de los ejercicios ---
