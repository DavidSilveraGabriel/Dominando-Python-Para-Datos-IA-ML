# Ejercicios: Módulo 3 - Introducción a NumPy y Arrays (`ndarray`)

# --- Prerrequisito ---
# Asegúrate de tener NumPy instalado. Si no, ejecuta en tu terminal:
# pip install numpy
# o
# conda install numpy

import numpy as np

print("--- Ejercicio 1: Creación de Arrays desde Listas ---")
# Instrucciones:
# 1. Crea una lista de Python llamada `lista_pesos` con los siguientes valores (pesos en kg):
#    [65.5, 70.2, 68.0, 75.8, 62.3]
# 2. Convierte `lista_pesos` en un array de NumPy llamado `pesos_array`.
# 3. Imprime la lista original y el array de NumPy.
# 4. Imprime el tipo de dato (`dtype`) del array `pesos_array`.

# Escribe tu código aquí
lista_pesos = [65.5, 70.2, 68.0, 75.8, 62.3]
pesos_array = np.array(lista_pesos)

print(f"Lista original: {lista_pesos}")
print(f"Array NumPy: {pesos_array}")
print(f"Tipo de dato (dtype) del array: {pesos_array.dtype}")


print("\n--- Ejercicio 2: Atributos del Array ---")
# Instrucciones:
# 1. Crea una lista de listas llamada `datos_sensores` simulando lecturas de 2 sensores en 4 momentos:
#    [[10, 12], [11, 13], [10, 11], [12, 12]]
# 2. Convierte `datos_sensores` en un array de NumPy 2D llamado `sensores_array`.
# 3. Imprime el array `sensores_array`.
# 4. Imprime los siguientes atributos del array:
#    - Número de dimensiones (`ndim`)
#    - Forma (`shape`)
#    - Tamaño total (`size`)
#    - Tipo de dato (`dtype`)

# Escribe tu código aquí
datos_sensores = [[10, 12], [11, 13], [10, 11], [12, 12]]
sensores_array = np.array(datos_sensores)

print(f"Array de sensores:\n{sensores_array}")
print(f"Número de dimensiones (ndim): {sensores_array.ndim}")
print(f"Forma (shape): {sensores_array.shape}")
print(f"Tamaño total (size): {sensores_array.size}")
print(f"Tipo de dato (dtype): {sensores_array.dtype}")


print("\n--- Ejercicio 3: Especificando el Tipo de Dato (dtype) ---")
# Instrucciones:
# 1. Crea una lista de Python `numeros_enteros = [1, 0, 1, 1, 0]`.
# 2. Crea un array de NumPy `booleanos_array` a partir de `numeros_enteros`,
#    especificando explícitamente que el tipo de dato sea booleano (`dtype=bool`).
# 3. Imprime el array `booleanos_array`.
# 4. Crea otra lista `alturas = [1.75, 1.82, 1.69]`.
# 5. Crea un array de NumPy `alturas_int_array` a partir de `alturas`,
#    especificando que el tipo de dato sea entero (`dtype=int`). Observa qué sucede
#    con la parte decimal.
# 6. Imprime el array `alturas_int_array`.

# Escribe tu código aquí
numeros_enteros = [1, 0, 1, 1, 0]
booleanos_array = np.array(numeros_enteros, dtype=bool)
print(f"Array booleano desde enteros: {booleanos_array}")

alturas = [1.75, 1.82, 1.69]
alturas_int_array = np.array(alturas, dtype=int) # La parte decimal se trunca
print(f"Array entero desde floats: {alturas_int_array}")


print("\n--- Ejercicio 4: Reflexión - NumPy vs Listas ---")
# Instrucciones: Basado en la lección, menciona brevemente (en un comentario)
# dos ventajas clave de usar arrays de NumPy sobre las listas estándar de Python
# para operaciones numéricas.

# Escribe tu respuesta como comentario
# Ventaja 1: Eficiencia (velocidad y memoria) debido a almacenamiento contiguo y C.
# Ventaja 2: Conveniencia (operaciones vectorizadas sin bucles for explícitos).
# Ventaja 3 (opcional): Funcionalidad (muchas funciones matemáticas/científicas).

print("Reflexión completada (ver comentarios en el código).")

# --- Fin de los ejercicios ---
