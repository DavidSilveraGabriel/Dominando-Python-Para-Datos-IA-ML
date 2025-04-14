# Módulo 8: Programación Funcional Avanzada (`itertools`, `functools`)

Python, aunque es un lenguaje multiparadigma, soporta muchos conceptos de la **programación funcional**. Este paradigma enfatiza el uso de **funciones puras** (que no tienen efectos secundarios y siempre devuelven lo mismo para las mismas entradas), la **inmutabilidad** de los datos y el tratamiento de las **funciones como ciudadanos de primera clase** (first-class functions - que ya hemos visto: pasarlas como argumentos, devolverlas, asignarlas a variables).

Dos módulos de la biblioteca estándar son particularmente útiles para un estilo de programación más funcional: `itertools` y `functools`.

## `itertools`: Iteradores Eficientes

El módulo `itertools` proporciona una colección de herramientas para construir y trabajar con **iteradores** de manera eficiente en términos de memoria y computación. Los iteradores, como vimos con los generadores, producen elementos bajo demanda (lazy evaluation).

`itertools` ofrece funciones para crear iteradores:

*   **Infinitos:** `count()`, `cycle()`, `repeat()`.
*   **Que terminan en la secuencia de entrada más corta:** `accumulate()`, `chain()`, `compress()`, `dropwhile()`, `filterfalse()`, `groupby()`, `islice()`, `starmap()`, `takewhile()`, `tee()`, `zip_longest()`.
*   **Combinatorios:** `product()`, `permutations()`, `combinations()`, `combinations_with_replacement()`.

Veamos algunos ejemplos comunes:

```python
import itertools

# --- Iteradores Infinitos (¡cuidado con usarlos sin límite!) ---
# count(start=0, step=1): Cuenta números indefinidamente
counter = itertools.count(10, 2) # Empieza en 10, de 2 en 2
print("itertools.count(10, 2):")
print(next(counter)) # 10
print(next(counter)) # 12
print(next(counter)) # 14

# cycle(iterable): Repite los elementos de un iterable indefinidamente
colors = ['Rojo', 'Verde', 'Azul']
color_cycler = itertools.cycle(colors)
print("\nitertools.cycle(['Rojo', 'Verde', 'Azul']):")
print(next(color_cycler)) # Rojo
print(next(color_cycler)) # Verde
print(next(color_cycler)) # Azul
print(next(color_cycler)) # Rojo (vuelve a empezar)

# repeat(object [, times]): Repite un objeto un número de veces (o infinitamente)
repeater = itertools.repeat("Hola", times=3)
print("\nitertools.repeat('Hola', times=3):")
print(list(repeater)) # ['Hola', 'Hola', 'Hola']

# --- Iteradores que Terminan ---
# chain(*iterables): Concatena múltiples iterables
letras = ['a', 'b', 'c']
numeros = [1, 2, 3]
combinado = itertools.chain(letras, numeros)
print("\nitertools.chain(letras, numeros):")
print(list(combinado)) # ['a', 'b', 'c', 1, 2, 3]

# islice(iterable, stop) o islice(iterable, start, stop [, step]):
# Obtiene un slice de un iterador sin copiarlo (lazy)
primeros_cinco_pares = itertools.islice(itertools.count(0, 2), 5) # Los primeros 5 pares
print("\nitertools.islice(itertools.count(0, 2), 5):")
print(list(primeros_cinco_pares)) # [0, 2, 4, 6, 8]

# takewhile(predicate, iterable): Toma elementos MIENTRAS la condición (predicate) sea True
numeros_seq = [1, 3, 5, 6, 7, 9, 2]
menores_que_6 = itertools.takewhile(lambda x: x < 6, numeros_seq)
print("\nitertools.takewhile(lambda x: x < 6, [1, 3, 5, 6, 7, 9, 2]):")
print(list(menores_que_6)) # [1, 3, 5] (se detiene en el 6)

# dropwhile(predicate, iterable): Descarta elementos MIENTRAS la condición sea True, luego devuelve el resto
mayores_o_igual_a_5 = itertools.dropwhile(lambda x: x < 5, numeros_seq)
print("\nitertools.dropwhile(lambda x: x < 5, [1, 3, 5, 6, 7, 9, 2]):")
print(list(mayores_o_igual_a_5)) # [5, 6, 7, 9, 2] (empieza a devolver desde el 5)

# --- Iteradores Combinatorios ---
# product(*iterables, repeat=1): Producto cartesiano
print("\nitertools.product('AB', [1, 2]):")
print(list(itertools.product('AB', [1, 2]))) # [('A', 1), ('A', 2), ('B', 1), ('B', 2)]

# permutations(iterable, r=None): Permutaciones de longitud r (o todas si r=None)
print("\nitertools.permutations('ABC', 2):")
print(list(itertools.permutations('ABC', 2))) # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# combinations(iterable, r): Combinaciones (sin orden, sin repetición) de longitud r
print("\nitertools.combinations('ABC', 2):")
print(list(itertools.combinations('ABC', 2))) # [('A', 'B'), ('A', 'C'), ('B', 'C')]
```
`itertools` es excelente para crear pipelines de procesamiento de datos eficientes y expresivos.

## `functools`: Herramientas para Funciones

El módulo `functools` proporciona funciones de orden superior (funciones que actúan sobre o devuelven otras funciones) y operaciones sobre objetos llamables.

**`functools.partial`:**

Permite "congelar" algunos de los argumentos de una función, creando una nueva función más especializada con una firma más simple.

```python
import functools

def potencia(base, exponente):
    """Calcula base^exponente."""
    return base ** exponente

# Crear una función especializada para calcular cuadrados usando partial
cuadrado = functools.partial(potencia, exponente=2)
# Ahora 'cuadrado' es como una función que solo necesita el argumento 'base'

# Crear una función para calcular 2^exponente
potencia_de_dos = functools.partial(potencia, 2) # Congela el primer argumento 'base'

print("\n--- functools.partial ---")
print(f"cuadrado(5): {cuadrado(5)}") # Salida: 25
print(f"cuadrado(10): {cuadrado(10)}") # Salida: 100
print(f"potencia_de_dos(3): {potencia_de_dos(3)}") # Salida: 8 (2^3)
print(f"potencia_de_dos(10): {potencia_de_dos(10)}") # Salida: 1024 (2^10)
```
`partial` es útil para adaptar funciones existentes a interfaces que esperan menos argumentos (ej. en callbacks, `map`).

**`functools.reduce`:**

Aplica una función de dos argumentos acumulativamente a los elementos de una secuencia, de izquierda a derecha, para reducir la secuencia a un solo valor.

```python
import functools
from operator import add, mul # Funciones add(a,b) y mul(a,b)

numeros = [1, 2, 3, 4, 5]

# Calcular la suma usando reduce
suma_total = functools.reduce(add, numeros)
# Equivalente a: add(add(add(add(1, 2), 3), 4), 5)
print(f"\nSuma con reduce(add, ...): {suma_total}") # Salida: 15 (igual que sum(numeros))

# Calcular el producto usando reduce
producto_total = functools.reduce(mul, numeros)
# Equivalente a: mul(mul(mul(mul(1, 2), 3), 4), 5)
print(f"Producto con reduce(mul, ...): {producto_total}") # Salida: 120

# Se puede usar con una función lambda
# Encontrar el máximo
maximo = functools.reduce(lambda x, y: x if x > y else y, numeros)
print(f"Máximo con reduce(lambda...): {maximo}") # Salida: 5 (igual que max(numeros))
```
Aunque `reduce` es potente, a menudo funciones incorporadas como `sum()`, `max()`, `min()` o bucles `for` explícitos son más legibles para operaciones comunes. `reduce` brilla en operaciones acumulativas más complejas.

**`@functools.lru_cache` (Decorador):**

Un decorador muy útil para implementar **memoization** o caching simple. Guarda los resultados de llamadas a funciones costosas y devuelve el resultado cacheado si se vuelve a llamar a la función con los mismos argumentos.

```python
import functools
import time

@functools.lru_cache(maxsize=None) # maxsize=None para caché ilimitada
def fibonacci(n):
    """Calcula el número de Fibonacci recursivamente (ineficiente sin caché)."""
    if n < 2:
        return n
    # print(f"Calculando fibonacci({n})") # Descomentar para ver llamadas
    return fibonacci(n-1) + fibonacci(n-2)

print("\n--- functools.lru_cache ---")
start_time = time.time()
resultado_fib = fibonacci(35) # Sin caché, esto sería MUY lento
end_time = time.time()
print(f"Fibonacci(35) = {resultado_fib}")
print(f"Tiempo con caché: {end_time - start_time:.6f} segundos")

# La segunda llamada con el mismo argumento será instantánea
start_time_2 = time.time()
resultado_fib_2 = fibonacci(35)
end_time_2 = time.time()
print(f"Fibonacci(35) (2da llamada) = {resultado_fib_2}")
print(f"Tiempo 2da llamada: {end_time_2 - start_time_2:.6f} segundos")
```

`itertools` y `functools` ofrecen herramientas poderosas para adoptar un estilo más funcional en Python, lo que puede llevar a código más conciso, eficiente y expresivo, especialmente útil en el procesamiento de datos y algoritmos.
