# Módulo 3: Introducción a NumPy y Arrays (`ndarray`)

¡Bienvenido/a al Módulo 3! Aquí nos sumergimos en el corazón de la computación numérica y científica en Python: la biblioteca **NumPy**.

## ¿Qué es NumPy?

NumPy (Numerical Python) es la biblioteca fundamental para la computación científica en Python. Proporciona:

1.  Un objeto **array N-dimensional (`ndarray`)** potente y eficiente.
2.  Funciones para realizar operaciones matemáticas y lógicas rápidas sobre estos arrays.
3.  Herramientas para álgebra lineal, transformadas de Fourier y generación de números aleatorios.
4.  Mecanismos para integrar código C/C++ y Fortran.

Es la base sobre la que se construyen muchas otras bibliotecas científicas y de análisis de datos en Python, incluyendo **Pandas**, Scikit-learn, SciPy y más.

**¿Por qué usar NumPy en lugar de las listas de Python?**

*   **Eficiencia:** Los arrays de NumPy son mucho más eficientes en términos de memoria y velocidad para operaciones numéricas que las listas estándar de Python. Esto se debe a que NumPy utiliza implementaciones optimizadas en C y almacena los datos de forma contigua en memoria.
*   **Conveniencia:** Permite realizar operaciones matemáticas complejas sobre arrays completos de forma concisa (operaciones vectorizadas), sin necesidad de escribir bucles `for` explícitos.
*   **Funcionalidad:** Ofrece una vasta colección de funciones matemáticas y científicas optimizadas para trabajar con arrays.

## El Objeto `ndarray` (N-dimensional array)

El objeto central de NumPy es el `ndarray` (a menudo llamado simplemente "array"). Representa una **cuadrícula multidimensional** de elementos del **mismo tipo** y de **tamaño fijo**.

**Características Clave del `ndarray`:**

*   **Multidimensional:** Puede tener una dimensión (vector), dos dimensiones (matriz), tres o más. El número de dimensiones se llama **rango** o **rank**.
*   **Homogéneo:** Todos los elementos dentro de un array deben ser del **mismo tipo de dato** (ej. todos `int64`, todos `float64`). Esto es clave para su eficiencia.
*   **Tamaño Fijo:** El tamaño de un array de NumPy se fija en el momento de su creación. Cambiar el tamaño implica crear un nuevo array (aunque hay funciones que lo hacen parecer transparente).
*   **Indexado:** Se accede a los elementos usando índices basados en cero, similar a las listas, pero extendido a múltiples dimensiones.

## Importando NumPy

La convención estándar y universalmente aceptada para importar NumPy es usar el alias `np`:

```python
import numpy as np
```
Casi siempre verás `np` en el código que usa NumPy. ¡Acostúmbrate a usarlo!

*(Nota: Si no tienes NumPy instalado, abre tu Anaconda Prompt o terminal con tu entorno activado y ejecuta: `conda install numpy` o `pip install numpy`)*

## Creando Arrays Básicos

La forma más común de crear un array es a partir de una lista o tupla de Python usando `np.array()`.

```python
import numpy as np

# Crear un array de 1 dimensión (vector) desde una lista
lista_simple = [1, 2, 3, 4, 5]
array_1d = np.array(lista_simple)

print(f"Lista original: {lista_simple}")
print(f"Tipo de lista: {type(lista_simple)}")
print(f"Array 1D: {array_1d}")
print(f"Tipo de array: {type(array_1d)}") # Salida: <class 'numpy.ndarray'>
print(f"Tipo de datos del array (dtype): {array_1d.dtype}") # Salida: int32 o int64 (depende del sistema)
print(f"Número de dimensiones (ndim): {array_1d.ndim}") # Salida: 1
print(f"Forma (shape): {array_1d.shape}") # Salida: (5,) -> una tupla indicando tamaño en cada dimensión
print(f"Tamaño total (size): {array_1d.size}") # Salida: 5

# Crear un array de 2 dimensiones (matriz) desde una lista de listas
lista_anidada = [[1, 2, 3], [4, 5, 6]]
array_2d = np.array(lista_anidada)

print(f"\nArray 2D:\n{array_2d}")
print(f"Tipo de datos (dtype): {array_2d.dtype}")
print(f"Número de dimensiones (ndim): {array_2d.ndim}") # Salida: 2
print(f"Forma (shape): {array_2d.shape}") # Salida: (2, 3) -> 2 filas, 3 columnas
print(f"Tamaño total (size): {array_2d.size}") # Salida: 6 (2 * 3)

# Crear un array especificando el tipo de dato (dtype)
array_float = np.array([1, 2, 3], dtype=np.float64)
print(f"\nArray float: {array_float}")
print(f"Dtype de array_float: {array_float.dtype}") # Salida: float64

array_bool = np.array([0, 1, -1, 0], dtype=bool) # 0 es False, cualquier otro número es True
print(f"\nArray bool: {array_bool}") # Salida: [False  True  True False]
print(f"Dtype de array_bool: {array_bool.dtype}") # Salida: bool
```

**Atributos Importantes del `ndarray`:**

*   `ndarray.ndim`: El número de dimensiones (ejes) del array.
*   `ndarray.shape`: Una tupla de enteros que indica el tamaño del array en cada dimensión. Para una matriz con `n` filas y `m` columnas, `shape` será `(n, m)`.
*   `ndarray.size`: El número total de elementos en el array. Es igual al producto de los elementos de `shape`.
*   `ndarray.dtype`: Un objeto que describe el tipo de dato de los elementos en el array (ej. `numpy.int64`, `numpy.float32`, `numpy.bool_`).
*   `ndarray.itemsize`: El tamaño en bytes de cada elemento del array.
*   `ndarray.data`: El buffer de memoria que contiene los elementos reales del array. Normalmente no necesitas acceder a esto directamente.

Esta es solo la introducción. En las siguientes secciones exploraremos las diversas formas de crear arrays (ceros, unos, rangos, etc.), cómo acceder y modificar sus elementos (indexación y slicing), y las potentes operaciones matemáticas que NumPy permite realizar sobre ellos.
