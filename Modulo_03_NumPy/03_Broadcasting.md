# Módulo 3: Broadcasting

Hemos visto que NumPy permite realizar operaciones aritméticas elemento a elemento entre arrays. Pero, ¿qué sucede si los arrays no tienen exactamente la misma forma (shape)? Aquí es donde entra en juego el **Broadcasting**.

**¿Qué es Broadcasting?**

Broadcasting es el conjunto de reglas que sigue NumPy para permitir que las funciones universales (ufuncs) operen sobre arrays de **formas diferentes**, siempre que esas formas sean **compatibles**. En esencia, NumPy "estira" o "duplica" virtualmente el array más pequeño a lo largo de las dimensiones faltantes o de tamaño 1 para que su forma coincida con la del array más grande, permitiendo así la operación elemento a elemento.

**¡Importante!** Este "estiramiento" es conceptual y eficiente. NumPy no crea copias reales de los datos en memoria para hacer broadcasting, lo que lo hace muy rápido y eficiente en memoria.

## Las Reglas del Broadcasting

Dos arrays son compatibles para broadcasting si se cumplen las siguientes reglas, comparando sus formas (shapes) de derecha a izquierda (desde la última dimensión hacia la primera):

1.  **Igualdad de Dimensiones:** Las dimensiones son iguales.
2.  **Una es 1:** Una de las dimensiones es 1. En este caso, NumPy "estira" virtualmente esa dimensión para que coincida con la dimensión del otro array.
3.  **(Error):** Si ninguna de las condiciones anteriores se cumple para alguna dimensión, los arrays no son compatibles y NumPy lanzará un error (`ValueError`).

**Proceso de Comparación:**

*   Si los arrays tienen diferente número de dimensiones (`ndim`), se añaden unos (1) a la izquierda de la forma del array con menos dimensiones hasta que ambas formas tengan la misma longitud.
*   Luego, se comparan las formas dimensión por dimensión, de derecha a izquierda.

**Ejemplos de Compatibilidad:**

*   `Array A (3, 4)` y `Array B (4,)` -> **Compatible**
    *   A: `(3, 4)`
    *   B: `(   4)` -> Se añade 1 a la izquierda: `(1, 4)`
    *   Comparando `(3, 4)` y `(1, 4)`:
        *   Dimensión -1: `4 == 4` (Regla 1) -> OK
        *   Dimensión -2: `3` y `1` (Regla 2) -> OK (B se estira a (3, 4))
*   `Array A (2, 1, 5)` y `Array B (3, 5)` -> **Compatible**
    *   A: `(2, 1, 5)`
    *   B: `(   3, 5)` -> Se añade 1 a la izquierda: `(1, 3, 5)`
    *   Comparando `(2, 1, 5)` y `(1, 3, 5)`:
        *   Dimensión -1: `5 == 5` (Regla 1) -> OK
        *   Dimensión -2: `1` y `3` (Regla 2) -> OK (A se estira en esta dim)
        *   Dimensión -3: `2` y `1` (Regla 2) -> OK (B se estira en esta dim)
        *   Forma resultante: `(2, 3, 5)`
*   `Array A (3, 4)` y `Array B (3,)` -> **INCOMPATIBLE**
    *   A: `(3, 4)`
    *   B: `(   3)` -> Se añade 1 a la izquierda: `(1, 3)`
    *   Comparando `(3, 4)` y `(1, 3)`:
        *   Dimensión -1: `4` y `3` -> ¡Error! No son iguales y ninguna es 1.
*   `Array A (3, 4)` y `Escalar (valor único)` -> **Compatible**
    *   Un escalar se trata como un array de dimensión 0. Se estira para coincidir con cualquier forma.

## Ejemplos Prácticos de Broadcasting

```python
import numpy as np

# Ejemplo 1: Array + Escalar (el caso más simple)
arr = np.arange(5) # [0 1 2 3 4]
print(f"Array original: {arr}")
print(f"Array + 100: {arr + 100}") # El escalar 100 se 'difunde' a cada elemento

# Ejemplo 2: Matriz (3, 3) + Vector (3,)
matriz = np.arange(9).reshape((3, 3)) # [[0 1 2], [3 4 5], [6 7 8]]
vector_fila = np.array([10, 20, 30]) # Shape (3,)

print(f"\nMatriz:\n{matriz}")
print(f"Vector fila: {vector_fila}")

# Suma: El vector_fila se 'difunde' a cada fila de la matriz
resultado = matriz + vector_fila
print(f"\nMatriz + Vector fila:\n{resultado}")
# Salida:
# [[10 21 32]
#  [13 24 35]
#  [16 27 38]]

# Ejemplo 3: Matriz (3, 3) + Vector Columna (3, 1)
vector_columna = np.array([[100], [200], [300]]) # Shape (3, 1)

print(f"\nMatriz:\n{matriz}")
print(f"Vector columna:\n{vector_columna}")

# Suma: El vector_columna se 'difunde' a cada columna de la matriz
resultado_col = matriz + vector_columna
print(f"\nMatriz + Vector columna:\n{resultado_col}")
# Salida:
# [[100 101 102]
#  [203 204 205]
#  [306 307 308]]

# Ejemplo 4: Vector Fila (3,) + Vector Columna (3, 1)
print(f"\nVector fila: {vector_fila}")
print(f"Vector columna:\n{vector_columna}")

# Suma: Ambos se difunden para crear una matriz (3, 3)
# vector_fila (3,) -> (1, 3) -> se estira a (3, 3)
# vector_columna (3, 1) -> se estira a (3, 3)
resultado_vecs = vector_fila + vector_columna
print(f"\nVector fila + Vector columna:\n{resultado_vecs}")
# Salida:
# [[110 120 130]
#  [210 220 230]
#  [310 320 330]]

# Ejemplo 5: Incompatible
arr_a = np.array([1, 2, 3]) # Shape (3,)
arr_b = np.array([10, 20])  # Shape (2,)
try:
    resultado_err = arr_a + arr_b
except ValueError as e:
    print(f"\nError al sumar arr_a (shape {arr_a.shape}) y arr_b (shape {arr_b.shape}): {e}")
    # Salida: Error... operands could not be broadcast together with shapes (3,) (2,)
```

## Añadiendo Dimensiones para Broadcasting

A veces, necesitas añadir explícitamente una dimensión de tamaño 1 a un array para que el broadcasting funcione como deseas (por ejemplo, para convertir un vector fila en un vector columna para ciertas operaciones). Puedes usar `np.newaxis` o `None` dentro de los corchetes de indexación.

```python
vector = np.arange(3) # [0 1 2], shape (3,)
print(f"\nVector original: {vector}, shape: {vector.shape}")

# Convertir a vector columna (añadir dimensión al final)
vector_col = vector[:, np.newaxis] # o vector[:, None]
print(f"Vector columna:\n{vector_col}")
print(f"Shape de vector columna: {vector_col.shape}") # Salida: (3, 1)

# Convertir a vector fila (añadir dimensión al principio)
vector_fila_expl = vector[np.newaxis, :] # o vector[None, :]
print(f"\nVector fila explícito:\n{vector_fila_expl}")
print(f"Shape de vector fila explícito: {vector_fila_expl.shape}") # Salida: (1, 3)

# Ahora podemos sumar el vector original con su versión en columna
suma_broad = vector + vector_col
print(f"\nSuma (vector + vector_col):\n{suma_broad}")
# Salida:
# [[0 1 2]
#  [1 2 3]
#  [2 3 4]]
```

El broadcasting es un concepto fundamental en NumPy que permite escribir código vectorizado de forma muy flexible y eficiente, incluso cuando las dimensiones de los arrays no coinciden exactamente. Entender sus reglas te ayudará a evitar errores y a aprovechar al máximo la potencia de NumPy.
