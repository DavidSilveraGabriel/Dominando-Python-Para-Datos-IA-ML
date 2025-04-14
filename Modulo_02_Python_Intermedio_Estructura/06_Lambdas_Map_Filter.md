# Módulo 2: Funciones Lambda, `map` y `filter`

Python ofrece herramientas que facilitan un estilo de programación más funcional, permitiendo operar sobre secuencias de datos de forma concisa. Tres de estas herramientas son las funciones lambda, `map()` y `filter()`.

## Funciones Lambda (Funciones Anónimas)

*   **¿Qué son?** Son funciones pequeñas y **anónimas** (sin nombre definido con `def`) que se definen usando la palabra clave `lambda`.
*   **Sintaxis:** `lambda argumentos: expresion`
*   **Características:**
    *   Pueden tener cualquier número de `argumentos`, pero solo **una única `expresion`**.
    *   La `expresion` se evalúa y su resultado es lo que la función lambda **devuelve implícitamente** (no se usa `return`).
    *   Son útiles cuando necesitas una función simple por un corto período de tiempo, especialmente como argumento para otras funciones de orden superior (como `map`, `filter`, `sorted`).

**Ejemplos:**

```python
# Función normal para sumar 5
def sumar_cinco_def(x):
    return x + 5

# Función lambda equivalente
sumar_cinco_lambda = lambda x: x + 5

print(f"Usando def: {sumar_cinco_def(10)}")    # Salida: Usando def: 15
print(f"Usando lambda: {sumar_cinco_lambda(10)}") # Salida: Usando lambda: 15

# Lambda con múltiples argumentos
multiplicar = lambda a, b: a * b
print(f"Multiplicar (lambda): {multiplicar(6, 7)}") # Salida: Multiplicar (lambda): 42

# Uso común: como argumento para ordenar una lista de tuplas por el segundo elemento
puntos = [(1, 5), (3, 2), (5, 8), (2, 1)]
puntos_ordenados = sorted(puntos, key=lambda punto: punto[1]) # Usa lambda para extraer el 2do elemento como clave de ordenación
print(f"Puntos ordenados por Y: {puntos_ordenados}")
# Salida: Puntos ordenados por Y: [(2, 1), (3, 2), (1, 5), (5, 8)]
```

Aunque puedes asignar una lambda a una variable (como `sumar_cinco_lambda`), PEP 8 generalmente recomienda usar `def` para funciones con nombre, ya que mejora la legibilidad y la depuración. El verdadero poder de lambda reside en su uso directo como argumento.

## La Función `map()`

*   **¿Qué hace?** Aplica una función dada a **cada elemento** de una secuencia iterable (lista, tupla, etc.) y devuelve un **iterador** con los resultados.
*   **Sintaxis:** `map(funcion, iterable1, [iterable2, ...])`
*   **Características:**
    *   `funcion`: La función que se aplicará a cada elemento. Puede ser una función definida con `def` o una `lambda`.
    *   `iterable`: La secuencia cuyos elementos serán procesados. Puedes pasar múltiples iterables si la función toma múltiples argumentos.
    *   **Devuelve un iterador `map`:** No devuelve una lista directamente. Necesitas convertirlo a una lista (u otro tipo) si quieres ver todos los resultados a la vez (ej. `list(map(...))`). Esto lo hace eficiente en memoria para secuencias grandes, ya que procesa los elementos bajo demanda.

**Ejemplos:**

```python
numeros = [1, 2, 3, 4, 5]

# Ejemplo 1: Elevar al cuadrado cada número usando map y una función def
def cuadrado(n):
    return n**2

cuadrados_map_def = map(cuadrado, numeros)
print(f"Objeto map (def): {cuadrados_map_def}") # Salida: Objeto map (def): <map object at 0x...>
print(f"Lista de cuadrados (def): {list(cuadrados_map_def)}") # Salida: Lista de cuadrados (def): [1, 4, 9, 16, 25]

# Ejemplo 2: Elevar al cuadrado usando map y lambda (más conciso)
cuadrados_map_lambda = map(lambda x: x**2, numeros)
print(f"Lista de cuadrados (lambda): {list(cuadrados_map_lambda)}") # Salida: Lista de cuadrados (lambda): [1, 4, 9, 16, 25]

# Ejemplo 3: Convertir lista de strings a mayúsculas
palabras = ["hola", "mundo", "python"]
mayusculas_map = map(str.upper, palabras) # str.upper es un método, se pasa sin ()
print(f"Mayúsculas (map): {list(mayusculas_map)}") # Salida: Mayúsculas (map): ['HOLA', 'MUNDO', 'PYTHON']

# Ejemplo 4: Sumar elementos de dos listas
lista1 = [1, 2, 3]
lista2 = [10, 20, 30]
sumas_map = map(lambda x, y: x + y, lista1, lista2)
print(f"Sumas de listas (map): {list(sumas_map)}") # Salida: Sumas de listas (map): [11, 22, 33]

# Comparación con List Comprehension (a menudo más legible para casos simples)
cuadrados_comp = [x**2 for x in numeros]
print(f"Cuadrados (comp): {cuadrados_comp}") # Salida: Cuadrados (comp): [1, 4, 9, 16, 25]
```

## La Función `filter()`

*   **¿Qué hace?** Filtra elementos de una secuencia iterable, manteniendo solo aquellos para los cuales una función dada devuelve `True`. Devuelve un **iterador** con los elementos que pasaron el filtro.
*   **Sintaxis:** `filter(funcion_booleana, iterable)`
*   **Características:**
    *   `funcion_booleana`: Una función que recibe un elemento del iterable y devuelve `True` (para mantener el elemento) o `False` (para descartarlo). Puede ser una función `def` o una `lambda`. Si se pasa `None` como función, `filter` elimina los elementos que son considerados "falsy" en Python (0, "", [], {}, False, None).
    *   `iterable`: La secuencia a filtrar.
    *   **Devuelve un iterador `filter`:** Al igual que `map`, necesitas convertirlo (ej. `list(filter(...))`) para ver los resultados.

**Ejemplos:**

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ejemplo 1: Filtrar números pares usando filter y una función def
def es_par(n):
    return n % 2 == 0

pares_filter_def = filter(es_par, numeros)
print(f"Objeto filter (def): {pares_filter_def}") # Salida: Objeto filter (def): <filter object at 0x...>
print(f"Lista de pares (def): {list(pares_filter_def)}") # Salida: Lista de pares (def): [2, 4, 6, 8, 10]

# Ejemplo 2: Filtrar números pares usando filter y lambda
pares_filter_lambda = filter(lambda x: x % 2 == 0, numeros)
print(f"Lista de pares (lambda): {list(pares_filter_lambda)}") # Salida: Lista de pares (lambda): [2, 4, 6, 8, 10]

# Ejemplo 3: Filtrar palabras que empiezan con 'P' (ignorando mayúsculas/minúsculas)
palabras = ["Python", "es", "poderoso", "pero", "practica"]
palabras_p = filter(lambda p: p.lower().startswith('p'), palabras)
print(f"Palabras con P (filter): {list(palabras_p)}") # Salida: Palabras con P (filter): ['Python', 'poderoso', 'pero', 'practica']

# Ejemplo 4: Filtrar elementos "falsy" usando None como función
mezcla = [0, "Hola", "", None, 100, False, True, [], [1,2]]
verdaderos = filter(None, mezcla)
print(f"Elementos 'truthy' (filter None): {list(verdaderos)}")
# Salida: Elementos 'truthy' (filter None): ['Hola', 100, True, [1, 2]]

# Comparación con List Comprehension (a menudo más legible)
pares_comp = [x for x in numeros if x % 2 == 0]
print(f"Pares (comp): {pares_comp}") # Salida: Pares (comp): [2, 4, 6, 8, 10]
```

**`map` vs. `filter` vs. List Comprehension:**

*   `map`: Aplica una función a *todos* los elementos para transformarlos. El número de elementos resultante es el mismo que el original.
*   `filter`: Selecciona un *subconjunto* de elementos basado en una condición. El número de elementos resultante es menor o igual que el original.
*   **List Comprehensions:** Pueden realizar tanto mapeo (`[expresion for ...]`) como filtrado (`[... for ... if condicion]`) en una sola expresión, y a menudo resultan más legibles para casos comunes. Sin embargo, `map` y `filter` pueden ser útiles con funciones más complejas o cuando se prefiere un estilo puramente funcional, y su naturaleza de iteradores puede ser más eficiente en memoria para datos muy grandes.

Dominar `lambda`, `map` y `filter` te proporciona herramientas poderosas para procesar datos de manera eficiente y concisa en Python.
