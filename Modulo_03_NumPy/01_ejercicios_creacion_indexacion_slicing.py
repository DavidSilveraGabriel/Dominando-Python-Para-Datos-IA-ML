# Ejercicios: Módulo 3 - Creación de Arrays, Indexación y Slicing

import numpy as np

print("--- Ejercicio 1: Creación de Arrays con Funciones ---")
# Instrucciones:
# 1. Crea un array de ceros de forma (2, 5) llamado `zeros_2x5`. Imprímelo.
# 2. Crea un array de unos de forma (4, 3) con tipo de dato entero (`dtype=int`) llamado `unos_4x3`. Imprímelo.
# 3. Crea un array llamado `rango_10_30` con números del 10 al 29 (inclusive) usando `np.arange()`. Imprímelo.
# 4. Crea un array llamado `linspace_0_1_11` con 11 puntos espaciados uniformemente entre 0 y 1 (ambos inclusive) usando `np.linspace()`. Imprímelo.
# 5. Crea una matriz identidad 4x4 llamada `identidad_4x4` usando `np.eye()` o `np.identity()`. Imprímela.
# 6. Crea un array 2x3 llamado `random_uniform` con números aleatorios de una distribución uniforme [0, 1). Imprímelo.
# 7. Crea un array 3x2 llamado `random_int` con enteros aleatorios entre 50 y 100 (exclusivo). Imprímelo.

# Escribe tu código aquí
zeros_2x5 = np.zeros((2, 5))
print(f"Array de ceros (2, 5):\n{zeros_2x5}\n")

unos_4x3 = np.ones((4, 3), dtype=int)
print(f"Array de unos (4, 3) entero:\n{unos_4x3}\n")

rango_10_30 = np.arange(10, 30)
print(f"Array con arange(10, 30): {rango_10_30}\n")

linspace_0_1_11 = np.linspace(0, 1, 11)
print(f"Array con linspace(0, 1, 11): {linspace_0_1_11}\n")

identidad_4x4 = np.identity(4)
print(f"Matriz identidad 4x4:\n{identidad_4x4}\n")

random_uniform = np.random.rand(2, 3)
print(f"Array aleatorio uniforme (2, 3):\n{random_uniform}\n")

random_int = np.random.randint(50, 100, size=(3, 2))
print(f"Array aleatorio entero [50, 100) (3, 2):\n{random_int}\n")


print("--- Ejercicio 2: Indexación ---")
# Instrucciones:
# 1. Crea el array `arr_idx = np.arange(20, 30)`. Imprímelo.
# 2. Accede e imprime el tercer elemento (índice 2).
# 3. Accede e imprime el penúltimo elemento (usando índice negativo).
# 4. Modifica el primer elemento (índice 0) para que valga 100. Imprime el array modificado.
# 5. Crea la matriz `mat_idx = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])`. Imprímela.
# 6. Accede e imprime el elemento en la primera fila, última columna.
# 7. Accede e imprime el elemento en la última fila, primera columna.
# 8. Modifica el elemento central (fila 1, columna 1) para que valga 55. Imprime la matriz modificada.

# Escribe tu código aquí
arr_idx = np.arange(20, 30)
print(f"Array para indexación: {arr_idx}")
print(f"Tercer elemento (índice 2): {arr_idx[2]}")
print(f"Penúltimo elemento (índice -2): {arr_idx[-2]}")
arr_idx[0] = 100
print(f"Array modificado (primer elemento): {arr_idx}\n")

mat_idx = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(f"Matriz para indexación:\n{mat_idx}")
print(f"Elemento [0, 2] (primera fila, última col): {mat_idx[0, 2]}")
print(f"Elemento [-1, 0] (última fila, primera col): {mat_idx[-1, 0]}")
mat_idx[1, 1] = 55
print(f"Matriz modificada (elemento central):\n{mat_idx}")


print("\n--- Ejercicio 3: Slicing ---")
# Instrucciones:
# 1. Crea el array `arr_slice = np.arange(15)`. Imprímelo.
# 2. Obtén un slice con los elementos del índice 5 al 10 (exclusive). Imprímelo.
# 3. Obtén un slice con los primeros 4 elementos. Imprímelo.
# 4. Obtén un slice con los últimos 3 elementos. Imprímelo.
# 5. Obtén un slice con todos los elementos, pero saltando de 3 en 3. Imprímelo.
# 6. Crea la matriz `mat_slice = np.arange(1, 13).reshape((3, 4))`. Imprímela.
# 7. Obtén un slice con la segunda fila completa. Imprímelo.
# 8. Obtén un slice con la segunda y tercera columna completas. Imprímelo.
# 9. Obtén un slice con las filas 0 y 1, y las columnas 1 y 2. Imprímelo.
# 10. (Importante) Modifica un elemento del slice obtenido en el paso 9 (ej. el primer elemento a 99).
#     Imprime el slice modificado Y la matriz `mat_slice` original. Observa si la original cambió (debería, es una vista).
# 11. Crea una COPIA del slice del paso 9 usando `.copy()`. Modifica un elemento de la copia.
#     Imprime la copia modificada y la matriz `mat_slice` original. Observa si la original cambió (no debería).

# Escribe tu código aquí
arr_slice = np.arange(15)
print(f"Array para slicing: {arr_slice}")
print(f"Slice [5:10]: {arr_slice[5:10]}")
print(f"Slice [:4]: {arr_slice[:4]}")
print(f"Slice [-3:]: {arr_slice[-3:]}")
print(f"Slice [::3]: {arr_slice[::3]}\n")

mat_slice = np.arange(1, 13).reshape((3, 4))
print(f"Matriz para slicing:\n{mat_slice}")
print(f"Segunda fila (índice 1): {mat_slice[1, :]}") # o mat_slice[1]
print(f"Columnas 2 y 3 (índices 1, 2):\n{mat_slice[:, 1:3]}")
sub_mat_vista = mat_slice[0:2, 1:3]
print(f"Slice filas 0,1 y cols 1,2 (Vista):\n{sub_mat_vista}")

print("\nModificando la VISTA:")
sub_mat_vista[0, 0] = 99 # Modifica el elemento (0,0) de la vista (que era 2)
print(f"Vista modificada:\n{sub_mat_vista}")
print(f"Matriz ORIGINAL después de modificar vista:\n{mat_slice}") # ¡Cambió!

print("\nModificando la COPIA:")
mat_slice[0, 1] = 2 # Restauramos el valor original para claridad
sub_mat_copia = mat_slice[0:2, 1:3].copy() # Creamos una copia
sub_mat_copia[0, 0] = 77 # Modificamos la copia
print(f"Copia modificada:\n{sub_mat_copia}")
print(f"Matriz ORIGINAL después de modificar copia:\n{mat_slice}") # No cambió


print("\n--- Ejercicio 4: Indexación Booleana ---")
# Instrucciones:
# 1. Crea el array `arr_bool = np.array([10, -5, 20, 0, -8, 15, -1])`. Imprímelo.
# 2. Selecciona e imprime solo los elementos positivos de `arr_bool`.
# 3. Selecciona e imprime solo los elementos negativos de `arr_bool`.
# 4. Selecciona e imprime solo los elementos mayores que 5 O menores que -5.
# 5. Modifica `arr_bool` para que todos los elementos negativos se conviertan en 0. Imprime el array modificado.

# Escribe tu código aquí
arr_bool = np.array([10, -5, 20, 0, -8, 15, -1])
print(f"Array para indexación booleana: {arr_bool}")
print(f"Elementos positivos: {arr_bool[arr_bool > 0]}")
print(f"Elementos negativos: {arr_bool[arr_bool < 0]}")
condicion_extremos = (arr_bool > 5) | (arr_bool < -5)
print(f"Elementos > 5 o < -5: {arr_bool[condicion_extremos]}")
arr_bool[arr_bool < 0] = 0
print(f"Array con negativos a 0: {arr_bool}")

# --- Fin de los ejercicios ---
