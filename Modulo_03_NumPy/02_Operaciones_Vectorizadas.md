# Módulo 3: Operaciones Matemáticas y Estadísticas Vectorizadas

Una de las principales razones por las que NumPy es tan eficiente y popular es su capacidad para realizar **operaciones vectorizadas**. Esto significa que puedes aplicar operaciones matemáticas o funciones a **arrays completos** de una sola vez, sin necesidad de escribir bucles `for` explícitos en Python. NumPy ejecuta estos bucles internamente en código C optimizado, lo que resulta en un rendimiento mucho mayor.

```python
import numpy as np
```

## Operaciones Aritméticas Elemento a Elemento

Puedes realizar operaciones aritméticas estándar (`+`, `-`, `*`, `/`, `//`, `%`, `**`) directamente entre arrays de NumPy (que tengan formas compatibles, lo veremos en Broadcasting) o entre un array y un escalar (un solo número). La operación se aplica **elemento a elemento**.

```python
arr1 = np.array([[1., 2., 3.], [4., 5., 6.]])
arr2 = np.array([[10., 11., 12.], [13., 14., 15.]])
escalar = 2.0

print(f"Array 1:\n{arr1}")
print(f"Array 2:\n{arr2}")
print(f"Escalar: {escalar}")

# Suma de arrays
print(f"\nSuma (arr1 + arr2):\n{arr1 + arr2}")

# Resta de arrays
print(f"\nResta (arr2 - arr1):\n{arr2 - arr1}")

# Multiplicación elemento a elemento (NO es multiplicación de matrices)
print(f"\nMultiplicación elemento a elemento (arr1 * arr2):\n{arr1 * arr2}")

# División elemento a elemento
print(f"\nDivisión elemento a elemento (arr1 / arr2):\n{arr1 / arr2}")

# Operaciones con un escalar
print(f"\nSuma con escalar (arr1 + escalar):\n{arr1 + escalar}")
print(f"\nMultiplicación por escalar (arr1 * escalar):\n{arr1 * escalar}")
print(f"\nPotencia con escalar (arr1 ** escalar):\n{arr1 ** escalar}") # Eleva cada elemento al cuadrado

# Comparaciones elemento a elemento (devuelven array booleano)
print(f"\nComparación (arr1 > 3):\n{arr1 > 3}")
```

**Ventaja:** Esto es mucho más rápido y conciso que iterar con bucles `for`:

```python
# Equivalente lento con listas y bucles for (¡NO HACER!)
lista1 = [[1., 2., 3.], [4., 5., 6.]]
lista2 = [[10., 11., 12.], [13., 14., 15.]]
resultado_lista = [[0, 0, 0], [0, 0, 0]] # Pre-inicializar con tamaño correcto

for i in range(len(lista1)):
    for j in range(len(lista1[0])):
        resultado_lista[i][j] = lista1[i][j] + lista2[i][j]

print(f"\nResultado suma con bucles for:\n{resultado_lista}")
```

## Funciones Universales (ufuncs)

NumPy proporciona una gran cantidad de **Funciones Universales (ufuncs)**. Estas son funciones que operan sobre `ndarrays` elemento a elemento, produciendo otro array como salida. Son envoltorios rápidos de funciones implementadas en C.

**Ufuncs Unarias (operan sobre un solo array):**

*   `np.sqrt(arr)`: Raíz cuadrada de cada elemento.
*   `np.exp(arr)`: Exponencial (e^x) de cada elemento.
*   `np.log(arr)`, `np.log10(arr)`, `np.log2(arr)`: Logaritmos.
*   `np.sin(arr)`, `np.cos(arr)`, `np.tan(arr)`: Funciones trigonométricas.
*   `np.abs(arr)`: Valor absoluto.
*   `np.square(arr)`: Elevar al cuadrado (`arr ** 2`).
*   `np.ceil(arr)`, `np.floor(arr)`: Redondear hacia arriba/abajo al entero más cercano.
*   `np.rint(arr)`: Redondear al entero más cercano.
*   `np.isnan(arr)`: Devuelve un array booleano indicando qué elementos son NaN (Not a Number).
*   `np.isfinite(arr)`, `np.isinf(arr)`: Comprueba si son finitos o infinitos.
*   Y muchas más...

**Ufuncs Binarias (operan sobre dos arrays, elemento a elemento):**

*   `np.add(arr1, arr2)`: Suma (`arr1 + arr2`).
*   `np.subtract(arr1, arr2)`: Resta (`arr1 - arr2`).
*   `np.multiply(arr1, arr2)`: Multiplicación (`arr1 * arr2`).
*   `np.divide(arr1, arr2)` o `np.true_divide(arr1, arr2)`: División (`arr1 / arr2`).
*   `np.floor_divide(arr1, arr2)`: División entera (`arr1 // arr2`).
*   `np.power(arr1, arr2)`: Potencia (`arr1 ** arr2`).
*   `np.maximum(arr1, arr2)`, `np.minimum(arr1, arr2)`: Máximo/mínimo elemento a elemento.
*   `np.mod(arr1, arr2)`: Resto elemento a elemento (`arr1 % arr2`).
*   `np.greater(arr1, arr2)`, `np.less(arr1, arr2)`, `np.equal(arr1, arr2)`, etc.: Comparaciones (`>`, `<`, `==`).
*   Y muchas más...

```python
arr = np.arange(1, 6) # [1 2 3 4 5]
print(f"\nArray para ufuncs: {arr}")

print(f"Raíz cuadrada (np.sqrt): {np.sqrt(arr)}")
print(f"Exponencial (np.exp): {np.exp(arr)}")
print(f"Seno (np.sin): {np.sin(arr)}")

arr_a = np.array([1, 5, 10])
arr_b = np.array([2, 3, 12])
print(f"\nArray A: {arr_a}")
print(f"Array B: {arr_b}")

print(f"Máximo elemento a elemento (np.maximum): {np.maximum(arr_a, arr_b)}") # Salida: [ 2  5 12]
print(f"Suma con ufunc (np.add): {np.add(arr_a, arr_b)}") # Salida: [ 3  8 22]
```

## Métodos Estadísticos Básicos

Los arrays de NumPy tienen métodos incorporados para realizar cálculos estadísticos comunes sobre todos los elementos del array o a lo largo de un eje específico (en arrays multidimensionales).

*   `arr.sum()`: Suma de todos los elementos.
*   `arr.mean()`: Media (promedio) de los elementos.
*   `arr.std()`: Desviación estándar.
*   `arr.var()`: Varianza.
*   `arr.min()`, `arr.max()`: Valor mínimo/máximo.
*   `arr.argmin()`, `arr.argmax()`: Índice del valor mínimo/máximo.
*   `arr.cumsum()`: Suma acumulada de los elementos.
*   `arr.cumprod()`: Producto acumulado de los elementos.

**Especificando el Eje (`axis`):**

En arrays multidimensionales, puedes realizar estas operaciones a lo largo de un eje específico:
*   `axis=0`: Opera a lo largo de las **filas** (calcula la estadística para cada columna).
*   `axis=1`: Opera a lo largo de las **columnas** (calcula la estadística para cada fila).

```python
arr_stats = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\nArray para estadísticas:\n{arr_stats}")

print(f"Suma total (sum()): {arr_stats.sum()}")     # Salida: 45
print(f"Media total (mean()): {arr_stats.mean()}")   # Salida: 5.0
print(f"Mínimo total (min()): {arr_stats.min()}")   # Salida: 1
print(f"Máximo total (max()): {arr_stats.max()}")   # Salida: 9

# Operaciones por eje
print(f"\nSuma por columnas (axis=0): {arr_stats.sum(axis=0)}") # Salida: [12 15 18] (1+4+7, 2+5+8, 3+6+9)
print(f"Media por filas (axis=1): {arr_stats.mean(axis=1)}")   # Salida: [2. 5. 8.] ((1+2+3)/3, (4+5+6)/3, (7+8+9)/3)
print(f"Máximo por columnas (axis=0): {arr_stats.max(axis=0)}") # Salida: [7 8 9]
print(f"Mínimo por filas (axis=1): {arr_stats.min(axis=1)}")   # Salida: [1 4 7]

print(f"\nSuma acumulada (cumsum()): {np.arange(5).cumsum()}") # Salida: [ 0  1  3  6 10]
```

## Métodos Booleanos (`any`, `all`)

*   `arr_bool.any()`: Devuelve `True` si **al menos un** elemento en el array booleano es `True`.
*   `arr_bool.all()`: Devuelve `True` si **todos** los elementos en el array booleano son `True`.

```python
arr_bool = np.array([True, False, True])
print(f"\nArray booleano: {arr_bool}")
print(f"¿Hay algún True? (any()): {arr_bool.any()}") # Salida: True
print(f"¿Son todos True? (all()): {arr_bool.all()}") # Salida: False

arr_positivos = np.array([1, 2, 3])
print(f"\n¿Son todos mayores que 0? {(arr_positivos > 0).all()}") # Salida: True
```

Las operaciones vectorizadas y las ufuncs son el núcleo de la eficiencia de NumPy. Permiten escribir código matemático y estadístico conciso y rápido, evitando bucles lentos de Python. Dominar estas operaciones es esencial para el análisis de datos y el machine learning.
