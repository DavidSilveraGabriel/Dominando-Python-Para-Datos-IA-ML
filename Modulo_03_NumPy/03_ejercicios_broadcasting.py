# Ejercicios: Módulo 3 - Broadcasting

import numpy as np

print("--- Ejercicio 1: Broadcasting con Escalar ---")
# Instrucciones:
# 1. Crea una matriz `matriz_a = np.array([[1, 2, 3], [4, 5, 6]])`. Imprímela.
# 2. Suma 100 a `matriz_a` usando broadcasting. Imprime el resultado.
# 3. Multiplica `matriz_a` por 5 usando broadcasting. Imprime el resultado.

# Escribe tu código aquí
matriz_a = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Matriz A:\n{matriz_a}\n")

resultado_suma_esc = matriz_a + 100
print(f"Matriz A + 100:\n{resultado_suma_esc}\n")

resultado_mult_esc = matriz_a * 5
print(f"Matriz A * 5:\n{resultado_mult_esc}\n")


print("--- Ejercicio 2: Broadcasting con Vector Fila ---")
# Instrucciones:
# 1. Usa la misma `matriz_a` del ejercicio anterior.
# 2. Crea un vector fila `vector_f = np.array([10, 20, 30])`. Imprímelo.
# 3. Suma `matriz_a` y `vector_f` usando broadcasting. Imprime el resultado.
#    (El vector fila se sumará a cada fila de la matriz).
# 4. Multiplica `matriz_a` y `vector_f` usando broadcasting. Imprime el resultado.

# Escribe tu código aquí
vector_f = np.array([10, 20, 30])
print(f"Matriz A:\n{matriz_a}")
print(f"Vector Fila:\n{vector_f}\n")

resultado_suma_vf = matriz_a + vector_f
print(f"Matriz A + Vector Fila:\n{resultado_suma_vf}\n")

resultado_mult_vf = matriz_a * vector_f
print(f"Matriz A * Vector Fila:\n{resultado_mult_vf}\n")


print("--- Ejercicio 3: Broadcasting con Vector Columna ---")
# Instrucciones:
# 1. Usa la misma `matriz_a` de antes.
# 2. Crea un vector columna `vector_c = np.array([[100], [200]])`. Imprímelo.
#    (Nota las dobles llaves para asegurar que tenga shape (2, 1)).
# 3. Suma `matriz_a` y `vector_c` usando broadcasting. Imprime el resultado.
#    (El vector columna se sumará a cada columna de la matriz).
# 4. Intenta multiplicar `matriz_a` y `vector_c`. Imprime el resultado.

# Escribe tu código aquí
vector_c = np.array([[100], [200]]) # Shape (2, 1)
print(f"Matriz A:\n{matriz_a}")
print(f"Vector Columna:\n{vector_c}\n")

resultado_suma_vc = matriz_a + vector_c
print(f"Matriz A + Vector Columna:\n{resultado_suma_vc}\n")

resultado_mult_vc = matriz_a * vector_c
print(f"Matriz A * Vector Columna:\n{resultado_mult_vc}\n")


print("--- Ejercicio 4: Añadiendo Dimensiones con `np.newaxis` ---")
# Instrucciones:
# 1. Crea un vector `v = np.arange(4)` (shape (4,)). Imprímelo.
# 2. Usa `np.newaxis` para convertir `v` en un vector columna `v_col` (shape (4, 1)). Imprímelo.
# 3. Usa `np.newaxis` para convertir `v` en un vector fila explícito `v_fila` (shape (1, 4)). Imprímelo.
# 4. Suma `v_col` y `v_fila` usando broadcasting. Imprime el resultado (debería ser una matriz 4x4).

# Escribe tu código aquí
v = np.arange(4)
print(f"Vector original v (shape {v.shape}): {v}")

v_col = v[:, np.newaxis] # o v[:, None]
print(f"Vector columna v_col (shape {v_col.shape}):\n{v_col}")

v_fila = v[np.newaxis, :] # o v[None, :]
print(f"Vector fila explícito v_fila (shape {v_fila.shape}):\n{v_fila}\n")

resultado_suma_vcvf = v_col + v_fila
print(f"Suma v_col + v_fila (shape {resultado_suma_vcvf.shape}):\n{resultado_suma_vcvf}")


print("\n--- Ejercicio 5: Identificando Errores de Broadcasting ---")
# Instrucciones:
# Para cada par de shapes, indica si son compatibles para broadcasting según las reglas.
# Si son compatibles, indica la shape resultante. Si no, explica por qué.
# (Escribe tus respuestas como comentarios).

# a) Shape 1: (5, 3)   Shape 2: (3,)
#    Respuesta: Compatible. Shape 2 -> (1, 3). Comparando (5, 3) y (1, 3):
#               Dim -1: 3==3 (OK). Dim -2: 5 y 1 (OK, se estira). Resultante: (5, 3).

# b) Shape 1: (4, 1)   Shape 2: (4,)
#    Respuesta: Compatible. Shape 2 -> (1, 4). Comparando (4, 1) y (1, 4):
#               Dim -1: 1 y 4 (OK, se estira). Dim -2: 4 y 1 (OK, se estira). Resultante: (4, 4).

# c) Shape 1: (3, 4, 2) Shape 2: (4, 1)
#    Respuesta: Compatible. Shape 2 -> (1, 4, 1). Comparando (3, 4, 2) y (1, 4, 1):
#               Dim -1: 2 y 1 (OK, se estira). Dim -2: 4==4 (OK). Dim -3: 3 y 1 (OK, se estira). Resultante: (3, 4, 2).

# d) Shape 1: (6, 5)   Shape 2: (5, 6)
#    Respuesta: Incompatible. Comparando (6, 5) y (5, 6):
#               Dim -1: 5 y 6 (Error, no son iguales y ninguno es 1).

# e) Shape 1: (2, 3, 4) Shape 2: (3, 1)
#    Respuesta: Incompatible. Shape 2 -> (1, 3, 1). Comparando (2, 3, 4) y (1, 3, 1):
#               Dim -1: 4 y 1 (OK, se estira). Dim -2: 3==3 (OK). Dim -3: 2 y 1 (OK, se estira). Resultante: (2, 3, 4).
#               CORRECCIÓN: ¡Sí es compatible! Me equivoqué en la explicación inicial.
#               Dim -1: 4 y 1 -> OK (estira B) -> Resulta 4
#               Dim -2: 3 y 3 -> OK -> Resulta 3
#               Dim -3: 2 y 1 -> OK (estira B) -> Resulta 2
#               Shape Resultante: (2, 3, 4)

print("Análisis de compatibilidad completado (ver comentarios).")

# --- Fin de los ejercicios ---
