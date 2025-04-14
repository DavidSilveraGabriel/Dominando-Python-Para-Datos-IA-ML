# Módulo 3: Ejercicios Prácticos con NumPy

¡Es hora de poner en práctica lo aprendido sobre NumPy! Resuelve los siguientes ejercicios para afianzar tus conocimientos sobre creación de arrays, indexación, slicing, operaciones vectorizadas y broadcasting.

Intenta resolverlos por tu cuenta primero. Las soluciones se encuentran al final.

```python
# Importa NumPy como siempre
import numpy as np
```

---

**Ejercicio 1: Creación y Atributos**

1.  Crea un array NumPy 1D llamado `vector` con los números enteros del 5 al 15 (ambos inclusive).
2.  Crea una matriz NumPy 2D llamada `matriz` de forma (3, 4) llena de unos, con tipo de dato entero.
3.  Imprime el `vector` y la `matriz`.
4.  Imprime el número de dimensiones (`ndim`), la forma (`shape`), el tamaño total (`size`) y el tipo de dato (`dtype`) de la `matriz`.

---

**Ejercicio 2: Indexación y Slicing**

Usando el `vector` y la `matriz` del ejercicio anterior:

1.  Accede e imprime el primer elemento del `vector`.
2.  Accede e imprime el último elemento del `vector`.
3.  Crea un slice `sub_vector` que contenga los elementos del `vector` desde el índice 2 hasta el índice 7 (exclusive). Imprímelo.
4.  Accede e imprime el elemento en la segunda fila, tercera columna de la `matriz`.
5.  Crea un slice `sub_matriz` que contenga las primeras dos filas y las últimas dos columnas de la `matriz`. Imprímelo.
6.  Crea un slice que contenga solo la última columna completa de la `matriz`. Imprímelo.

---

**Ejercicio 3: Operaciones Vectorizadas**

1.  Crea dos arrays 1D, `a = np.array([1, 2, 3])` y `b = np.array([10, 20, 30])`.
2.  Calcula e imprime la suma, resta, multiplicación y división elemento a elemento de `a` y `b`.
3.  Calcula e imprime `a` elevado al cuadrado.
4.  Calcula e imprime la raíz cuadrada de `b` usando una ufunc de NumPy.
5.  Comprueba (e imprime el resultado booleano) si todos los elementos de `a` son menores que los elementos correspondientes en `b`.

---

**Ejercicio 4: Broadcasting**

1.  Crea una matriz `m = np.arange(1, 10).reshape((3, 3))` (números del 1 al 9).
2.  Crea un vector fila `v = np.array([100, 200, 300])`.
3.  Suma `m` y `v` usando broadcasting e imprime el resultado.
4.  Crea un vector columna `c = np.array([[10], [20], [30]])`.
5.  Multiplica `m` y `c` usando broadcasting e imprime el resultado.

---

**Ejercicio 5: Métodos Estadísticos**

Usando la matriz `m` del ejercicio anterior:

1.  Calcula e imprime la suma total de todos los elementos de `m`.
2.  Calcula e imprime la media de todos los elementos de `m`.
3.  Calcula e imprime el valor máximo de `m`.
4.  Calcula e imprime la suma de cada columna (a lo largo del eje 0).
5.  Calcula e imprime el mínimo de cada fila (a lo largo del eje 1).

---

**Ejercicio 6: Indexación Booleana**

Usando la matriz `m` del ejercicio 4:

1.  Crea un array booleano `condicion` que sea `True` donde los elementos de `m` sean mayores que 5. Imprime `condicion`.
2.  Usa `condicion` para seleccionar e imprimir solo los elementos de `m` que son mayores que 5.
3.  Modifica la matriz `m` original para que todos los elementos pares se conviertan en 0. Imprime la matriz `m` modificada.

---
---

## Soluciones

```python
import numpy as np

# --- Solución Ejercicio 1 ---
print("--- Ejercicio 1 ---")
vector = np.arange(5, 16)
matriz = np.ones((3, 4), dtype=int)
print(f"Vector:\n{vector}")
print(f"Matriz:\n{matriz}")
print(f"Matriz ndim: {matriz.ndim}")
print(f"Matriz shape: {matriz.shape}")
print(f"Matriz size: {matriz.size}")
print(f"Matriz dtype: {matriz.dtype}")

# --- Solución Ejercicio 2 ---
print("\n--- Ejercicio 2 ---")
print(f"Primer elemento vector: {vector[0]}")
print(f"Último elemento vector: {vector[-1]}")
sub_vector = vector[2:7]
print(f"Sub-vector [2:7]: {sub_vector}")
print(f"Elemento matriz[1, 2]: {matriz[1, 2]}") # Segunda fila (índice 1), tercera columna (índice 2)
sub_matriz = matriz[0:2, -2:] # Filas 0,1 y últimas 2 columnas
print(f"Sub-matriz (primeras 2 filas, últimas 2 cols):\n{sub_matriz}")
ultima_columna = matriz[:, -1]
print(f"Última columna:\n{ultima_columna}")

# --- Solución Ejercicio 3 ---
print("\n--- Ejercicio 3 ---")
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(f"a: {a}")
print(f"b: {b}")
print(f"a + b: {a + b}")
print(f"a - b: {a - b}")
print(f"a * b: {a * b}")
print(f"a / b: {a / b}")
print(f"a al cuadrado: {a**2}") # o np.square(a)
print(f"Raíz cuadrada de b: {np.sqrt(b)}")
print(f"¿Todos a < b?: {(a < b).all()}")

# --- Solución Ejercicio 4 ---
print("\n--- Ejercicio 4 ---")
m = np.arange(1, 10).reshape((3, 3))
v = np.array([100, 200, 300])
c = np.array([[10], [20], [30]])
print(f"Matriz m:\n{m}")
print(f"Vector v: {v}")
print(f"Vector c:\n{c}")
print(f"m + v:\n{m + v}")
print(f"m * c:\n{m * c}")

# --- Solución Ejercicio 5 ---
print("\n--- Ejercicio 5 ---")
print(f"Suma total de m: {m.sum()}")
print(f"Media total de m: {m.mean()}")
print(f"Máximo de m: {m.max()}")
print(f"Suma por columnas (axis=0): {m.sum(axis=0)}")
print(f"Mínimo por filas (axis=1): {m.min(axis=1)}")

# --- Solución Ejercicio 6 ---
print("\n--- Ejercicio 6 ---")
condicion = m > 5
print(f"Condición (m > 5):\n{condicion}")
print(f"Elementos > 5: {m[condicion]}")
m[m % 2 == 0] = 0 # Selecciona elementos pares y los asigna a 0
print(f"Matriz m con pares a 0:\n{m}")

```

¡Revisa tus respuestas y asegúrate de entender cómo funciona cada operación! La práctica constante es clave para dominar NumPy.
