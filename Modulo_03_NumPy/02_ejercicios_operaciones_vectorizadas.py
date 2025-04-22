# Ejercicios: Módulo 3 - Operaciones Matemáticas y Estadísticas Vectorizadas

import numpy as np

print("--- Ejercicio 1: Operaciones Aritméticas Elemento a Elemento ---")
# Instrucciones:
# 1. Crea dos arrays 1D: `v1 = np.array([5, 10, 15])` y `v2 = np.array([2, 3, 4])`.
# 2. Realiza e imprime las siguientes operaciones elemento a elemento:
#    - `v1 + v2`
#    - `v1 * v2`
#    - `v1 / v2` (división flotante)
#    - `v1 ** v2` (v1 elevado a la potencia de v2)
# 3. Crea una matriz `m1 = np.array([[1, 2], [3, 4]])`.
# 4. Suma la matriz `m1` con un escalar `10` e imprime el resultado.
# 5. Multiplica la matriz `m1` por un escalar `3` e imprime el resultado.

# Escribe tu código aquí
v1 = np.array([5, 10, 15])
v2 = np.array([2, 3, 4])
print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 * v2: {v1 * v2}")
print(f"v1 / v2: {v1 / v2}")
print(f"v1 ** v2: {v1 ** v2}\n")

m1 = np.array([[1, 2], [3, 4]])
escalar_10 = 10
escalar_3 = 3
print(f"m1:\n{m1}")
print(f"m1 + {escalar_10}:\n{m1 + escalar_10}")
print(f"m1 * {escalar_3}:\n{m1 * escalar_3}")


print("\n--- Ejercicio 2: Funciones Universales (ufuncs) ---")
# Instrucciones:
# 1. Crea un array `arr_ufunc = np.array([1, 4, 9, 16, 25])`. Imprímelo.
# 2. Calcula e imprime la raíz cuadrada de cada elemento usando `np.sqrt()`.
# 3. Calcula e imprime el exponencial (e^x) de cada elemento usando `np.exp()`.
# 4. Crea dos arrays: `a = np.array([1, 5, 3])` y `b = np.array([4, 2, 6])`.
# 5. Calcula e imprime el máximo elemento a elemento entre `a` y `b` usando `np.maximum()`.

# Escribe tu código aquí
arr_ufunc = np.array([1, 4, 9, 16, 25])
print(f"Array para ufuncs: {arr_ufunc}")
print(f"Raíz cuadrada (np.sqrt): {np.sqrt(arr_ufunc)}")
# Limitamos la impresión de exp para evitar números muy grandes
print(f"Exponencial (np.exp) de los primeros 3: {np.exp(arr_ufunc[:3])}\n")

a = np.array([1, 5, 3])
b = np.array([4, 2, 6])
print(f"Array a: {a}")
print(f"Array b: {b}")
print(f"Máximo elemento a elemento (np.maximum): {np.maximum(a, b)}")


print("\n--- Ejercicio 3: Métodos Estadísticos ---")
# Instrucciones:
# 1. Crea una matriz `datos = np.array([[10, 25, 15], [30, 5, 20]])`. Imprímela.
# 2. Calcula e imprime la suma total de todos los elementos.
# 3. Calcula e imprime la media de todos los elementos.
# 4. Calcula e imprime la desviación estándar de todos los elementos.
# 5. Calcula e imprime el valor mínimo de cada columna (a lo largo del eje 0).
# 6. Calcula e imprime el valor máximo de cada fila (a lo largo del eje 1).
# 7. Calcula e imprime la suma acumulada de los elementos (aplanando el array primero si es necesario o usando el método directamente).

# Escribe tu código aquí
datos = np.array([[10, 25, 15], [30, 5, 20]])
print(f"Matriz de datos:\n{datos}")
print(f"Suma total: {datos.sum()}")
print(f"Media total: {datos.mean()}")
print(f"Desviación estándar total: {datos.std():.2f}") # :.2f para formatear a 2 decimales
print(f"Mínimo por columna (axis=0): {datos.min(axis=0)}")
print(f"Máximo por fila (axis=1): {datos.max(axis=1)}")
# cumsum funciona sobre el array aplanado por defecto
print(f"Suma acumulada: {datos.cumsum()}")


print("\n--- Ejercicio 4: Métodos Booleanos (any, all) ---")
# Instrucciones:
# 1. Crea el array `evaluaciones = np.array([True, False, True, True])`. Imprímelo.
# 2. Comprueba e imprime si *alguna* evaluación es `True` usando `.any()`.
# 3. Comprueba e imprime si *todas* las evaluaciones son `True` usando `.all()`.
# 4. Crea el array `numeros_check = np.array([5, 12, 8, 10])`.
# 5. Comprueba e imprime si *todos* los números en `numeros_check` son mayores que 0.
# 6. Comprueba e imprime si *alguno* de los números en `numeros_check` es par.

# Escribe tu código aquí
evaluaciones = np.array([True, False, True, True])
print(f"Array de evaluaciones: {evaluaciones}")
print(f"¿Alguna es True? {evaluaciones.any()}")
print(f"¿Todas son True? {evaluaciones.all()}\n")

numeros_check = np.array([5, 12, 8, 10])
print(f"Array numeros_check: {numeros_check}")
print(f"¿Todos > 0? {(numeros_check > 0).all()}")
print(f"¿Alguno es par? {(numeros_check % 2 == 0).any()}")

# --- Fin de los ejercicios ---
