# Módulo 3: Creación de Arrays, Indexación y Slicing

Además de crear arrays a partir de listas existentes con `np.array()`, NumPy ofrece funciones muy útiles para crear arrays comunes desde cero. También exploraremos cómo acceder y manipular elementos específicos o subconjuntos de arrays.

```python
import numpy as np
```

## Funciones para Crear Arrays

NumPy proporciona varias funciones para generar arrays con patrones específicos:

*   **`np.zeros(shape, dtype=float)`:** Crea un array lleno de ceros con la forma (`shape`) dada.
*   **`np.ones(shape, dtype=float)`:** Crea un array lleno de unos.
*   **`np.full(shape, fill_value, dtype=None)`:** Crea un array lleno de un valor específico (`fill_value`).
*   **`np.empty(shape, dtype=float)`:** Crea un array "vacío" (sin inicializar sus entradas a ningún valor particular; contendrá lo que haya en memoria en ese momento). Es ligeramente más rápido que `zeros` u `ones` si vas a llenar todos los elementos inmediatamente después.
*   **`np.arange([start,] stop[, step,], dtype=None)`:** Similar al `range()` de Python, pero devuelve un `ndarray` en lugar de un iterador. Crea valores espaciados uniformemente dentro de un intervalo dado. ¡Ojo! `stop` no está incluido.
*   **`np.linspace(start, stop, num=50, endpoint=True, dtype=None)`:** Crea un array con un número específico (`num`) de puntos espaciados uniformemente entre `start` y `stop`. `endpoint=True` incluye el valor `stop` en el array. Muy útil para generar coordenadas para gráficos.
*   **`np.eye(N, M=None, k=0, dtype=float)`:** Crea una matriz identidad de tamaño NxN (o NxM si se especifica M). La diagonal principal tiene unos y el resto son ceros. `k` permite desplazar la diagonal.
*   **`np.identity(n, dtype=None)`:** Similar a `np.eye(n)`, crea una matriz identidad cuadrada.
*   **`np.random.rand(d0, d1, ..., dn)`:** Crea un array con números aleatorios de una distribución uniforme entre [0, 1) con la forma dada.
*   **`np.random.randn(d0, d1, ..., dn)`:** Crea un array con números aleatorios de una distribución normal estándar (media 0, desviación estándar 1) con la forma dada.
*   **`np.random.randint(low, high=None, size=None, dtype=int)`:** Crea un array con enteros aleatorios entre `low` (incluido) y `high` (excluido). `size` define la forma del array.

```python
# Ejemplos de creación de arrays
zeros_array = np.zeros((2, 3)) # Matriz 2x3 de ceros (float por defecto)
print(f"Zeros:\n{zeros_array}\n")

ones_array = np.ones((3, 2), dtype=int) # Matriz 3x2 de unos (enteros)
print(f"Ones:\n{ones_array}\n")

full_array = np.full((2, 4), 7) # Matriz 2x4 llena de 7s
print(f"Full:\n{full_array}\n")

arange_array = np.arange(0, 10, 2) # Array [0 2 4 6 8]
print(f"Arange: {arange_array}\n")

linspace_array = np.linspace(0, 1, 5) # 5 puntos entre 0 y 1 (incluidos)
print(f"Linspace: {linspace_array}\n") # Salida: [0.   0.25 0.5  0.75 1.  ]

identity_matrix = np.identity(3)
print(f"Identity:\n{identity_matrix}\n")

random_array = np.random.rand(2, 2) # Matriz 2x2 aleatoria [0, 1)
print(f"Random (uniform):\n{random_array}\n")

random_int_array = np.random.randint(1, 10, size=(3, 4)) # Enteros aleatorios [1, 10) en matriz 3x4
print(f"Random integers:\n{random_int_array}\n")
```

## Indexación de Arrays (Acceso a Elementos)

Acceder a elementos individuales o subconjuntos de arrays es fundamental. NumPy utiliza índices basados en cero.

**Arrays de 1 Dimensión:** Similar a las listas de Python.

```python
arr1d = np.arange(10, 20) # Array [10 11 12 13 14 15 16 17 18 19]
print(f"Array 1D: {arr1d}")

# Acceder a un elemento
print(f"Elemento en índice 0: {arr1d[0]}")   # Salida: 10
print(f"Elemento en índice 3: {arr1d[3]}")   # Salida: 13
print(f"Último elemento: {arr1d[-1]}")      # Salida: 19

# Modificar un elemento
arr1d[0] = 100
print(f"Array modificado: {arr1d}") # Salida: [100  11  12  13  14  15  16  17  18  19]
```

**Arrays Multidimensionales (ej. 2D - Matrices):** Se usa una tupla de índices separados por comas `[fila, columna]`.

```python
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\nArray 2D:\n{arr2d}")

# Acceder a un elemento [fila, columna]
print(f"Elemento en [0, 0]: {arr2d[0, 0]}") # Salida: 1 (Primera fila, primera columna)
print(f"Elemento en [1, 2]: {arr2d[1, 2]}") # Salida: 6 (Segunda fila, tercera columna)
print(f"Elemento en [2, 1]: {arr2d[2, 1]}") # Salida: 8 (Tercera fila, segunda columna)

# Sintaxis alternativa (menos común para un solo elemento): arr2d[fila][columna]
print(f"Elemento en [0][0] (alt): {arr2d[0][0]}") # Salida: 1

# Modificar un elemento
arr2d[1, 1] = 55
print(f"\nArray 2D modificado:\n{arr2d}")
# Salida:
# [[ 1  2  3]
#  [ 4 55  6]
#  [ 7  8  9]]
```

## Slicing (Rebanado) de Arrays

Slicing permite seleccionar **subconjuntos** de un array, creando "vistas" de los datos originales.

**Sintaxis Básica (similar a listas):** `start:stop:step`

*   `start`: Índice inicial (incluido, por defecto es 0).
*   `stop`: Índice final (excluido, por defecto es el final del array).
*   `step`: Paso (por defecto es 1).

**Slicing en Arrays 1D:**

```python
arr1d = np.arange(10) # [0 1 2 3 4 5 6 7 8 9]
print(f"\nArray 1D para slicing: {arr1d}")

# Primeros 5 elementos
slice1 = arr1d[0:5] # o arr1d[:5]
print(f"arr1d[:5] -> {slice1}") # Salida: [0 1 2 3 4]

# Elementos desde el índice 5 hasta el final
slice2 = arr1d[5:]
print(f"arr1d[5:] -> {slice2}") # Salida: [5 6 7 8 9]

# Elementos del índice 2 al 6 (excluido)
slice3 = arr1d[2:6]
print(f"arr1d[2:6] -> {slice3}") # Salida: [2 3 4 5]

# Cada segundo elemento
slice4 = arr1d[::2]
print(f"arr1d[::2] -> {slice4}") # Salida: [0 2 4 6 8]

# Invertir el array
slice5 = arr1d[::-1]
print(f"arr1d[::-1] -> {slice5}") # Salida: [9 8 7 6 5 4 3 2 1 0]
```

**Slicing en Arrays 2D:** Se aplica la sintaxis de slicing a cada dimensión, separada por comas `[slice_filas, slice_columnas]`.

```python
arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f"\nArray 2D para slicing:\n{arr2d}")

# Primeras dos filas, columnas 1 y 2
# Filas: 0:2 (filas 0 y 1)
# Columnas: 1:3 (columnas 1 y 2)
slice2d_1 = arr2d[0:2, 1:3]
print(f"\nPrimeras 2 filas, columnas 1 y 2:\n{slice2d_1}")
# Salida:
# [[2 3]
#  [6 7]]

# Fila del medio (índice 1), todas las columnas
slice2d_2 = arr2d[1, :] # o arr2d[1]
print(f"\nFila del medio: {slice2d_2}") # Salida: [5 6 7 8] (devuelve un array 1D)

# Todas las filas, columna del índice 2
slice2d_3 = arr2d[:, 2]
print(f"\nColumna del índice 2: {slice2d_3}") # Salida: [ 3  7 11] (devuelve un array 1D)

# Últimas dos columnas, todas las filas
slice2d_4 = arr2d[:, -2:]
print(f"\nÚltimas 2 columnas:\n{slice2d_4}")
# Salida:
# [[ 3  4]
#  [ 7  8]
#  [11 12]]
```

**¡Importante! Las Vistas (Views) vs. Copias (Copies):**

*   Por defecto, el slicing en NumPy crea **vistas** del array original, no copias.
*   Una **vista** es una referencia a los mismos datos en memoria. Si modificas una vista, **¡también modificas el array original!**
*   Esto es eficiente porque evita copiar datos innecesariamente.

```python
arr_original = np.arange(5) # [0 1 2 3 4]
vista = arr_original[1:4]  # Vista: [1 2 3]
print(f"\nOriginal: {arr_original}")
print(f"Vista: {vista}")

vista[0] = 99 # Modificamos la vista
print(f"Vista modificada: {vista}")
print(f"¡Original TAMBIÉN modificado!: {arr_original}") # Salida: [ 0 99  2  3  4]
```

*   Si necesitas una **copia** independiente de los datos (para modificarla sin afectar al original), usa el método `.copy()`:

```python
arr_original_2 = np.arange(5)
copia = arr_original_2[1:4].copy() # Creamos una copia explícita
print(f"\nOriginal 2: {arr_original_2}")
print(f"Copia: {copia}")

copia[0] = 77 # Modificamos la copia
print(f"Copia modificada: {copia}")
print(f"Original 2 NO afectado: {arr_original_2}") # Salida: [0 1 2 3 4]
```

## Indexación Booleana

Permite seleccionar elementos de un array basados en una condición booleana.

```python
nombres = np.array(["Ana", "Luis", "Eva", "Luis"])
datos = np.random.randn(4, 3) # Matriz 4x3 de datos aleatorios

print(f"\nNombres: {nombres}")
print(f"Datos:\n{datos}")

# Condición booleana: ¿el nombre es "Luis"?
condicion_luis = (nombres == "Luis")
print(f"Condición (nombres == 'Luis'): {condicion_luis}") # Salida: [False  True False  True]

# Usar la condición para seleccionar filas de 'datos'
print(f"\nFilas de 'datos' donde nombre es 'Luis':\n{datos[condicion_luis]}")
# Selecciona las filas 1 y 3 de 'datos'

# También se puede aplicar a la misma dimensión
numeros = np.arange(10)
print(f"\nNúmeros: {numeros}")
print(f"Números mayores que 5: {numeros[numeros > 5]}") # Salida: [6 7 8 9]

# Combinar condiciones booleanas (& para AND, | para OR, ~ para NOT)
condicion_ana_o_eva = (nombres == "Ana") | (nombres == "Eva")
print(f"\nFilas de 'datos' donde nombre es 'Ana' o 'Eva':\n{datos[condicion_ana_o_eva]}")

# Modificar elementos basados en condición
numeros[numeros < 5] = 0 # Pone a 0 los elementos menores que 5
print(f"Números modificados (<5 a 0): {numeros}") # Salida: [0 0 0 0 0 5 6 7 8 9]
```

La creación, indexación y slicing son operaciones fundamentales para trabajar eficazmente con arrays NumPy. Dominarlas te permitirá manipular y acceder a tus datos numéricos de forma eficiente y flexible.
