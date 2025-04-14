# Módulo 8: Generadores y Expresiones Generadoras

Cuando trabajamos con secuencias de datos muy grandes (ej. leer un archivo enorme línea por línea, generar millones de números), crear una lista completa en memoria puede ser ineficiente o incluso imposible debido a las limitaciones de memoria.

Los **Generadores** ofrecen una solución elegante a este problema. Son un tipo especial de **iterador** que genera valores **bajo demanda (lazy evaluation)**, uno a la vez, en lugar de almacenar toda la secuencia en memoria de golpe.

## ¿Qué es un Iterador?

Antes de hablar de generadores, recordemos qué es un iterador:

*   Es un objeto que representa un flujo de datos.
*   Implementa el **protocolo iterador**, que consiste principalmente en el método `__next__()`.
*   Cada vez que llamas a `next(iterador)`, devuelve el siguiente elemento de la secuencia.
*   Cuando no hay más elementos, lanza una excepción `StopIteration`.
*   Los bucles `for` en Python funcionan internamente con iteradores.

## Generadores (Funciones con `yield`)

La forma más común de crear un generador es definiendo una **función que usa la palabra clave `yield`**.

*   Cuando una función contiene `yield`, se convierte automáticamente en una **función generadora**.
*   Cuando llamas a una función generadora, no ejecuta el cuerpo de la función inmediatamente. En su lugar, devuelve un **objeto generador** (que es un tipo de iterador).
*   Cada vez que se llama a `next()` sobre el objeto generador (o cuando el bucle `for` lo pide), la ejecución de la función **continúa desde donde se quedó** hasta que encuentra una declaración `yield`.
*   El valor especificado en `yield` se devuelve como el siguiente elemento de la secuencia.
*   El estado de la función (variables locales, punto de ejecución) se **suspende** y se guarda entre llamadas a `next()`.
*   Cuando la función generadora termina (llega al final o ejecuta `return`), el generador lanza automáticamente `StopIteration`.

**Sintaxis:**

```python
def mi_funcion_generadora(argumentos):
    # Código de inicialización (se ejecuta la primera vez que se pide un valor)
    # ...
    while condicion: # O un bucle for, o lógica secuencial
        # ... calcular valor ...
        yield valor_a_devolver # Pausa aquí y devuelve el valor
        # ... código después de yield (se ejecuta en la siguiente llamada a next()) ...
    # Al salir del bucle o terminar la función, se lanza StopIteration
```

**Ejemplo: Generador de Números Pares**

```python
def generador_pares(maximo):
    """Genera números pares hasta un máximo (exclusive)."""
    n = 0
    print("Generador iniciado.")
    while n < maximo:
        if n % 2 == 0:
            print(f"Yielding {n}")
            yield n # Devuelve el valor y pausa
            print("Generador reanudado.")
        n += 1
    print("Generador finalizado.")

# Crear el objeto generador (no ejecuta el código aún)
pares = generador_pares(10)
print(f"Tipo de 'pares': {type(pares)}") # Salida: <class 'generator'>

# Obtener valores uno por uno con next()
print("\nUsando next():")
print(f"Primer valor: {next(pares)}") # Ejecuta hasta el primer yield
print(f"Segundo valor: {next(pares)}") # Reanuda y ejecuta hasta el siguiente yield
print(f"Tercer valor: {next(pares)}")

# Usar el generador en un bucle for (forma más común)
print("\nUsando bucle for:")
# El bucle for llama a next() automáticamente y maneja StopIteration
for par in generador_pares(6): # Creamos un nuevo generador
    print(f"  Recibido en for: {par}")

# Intentar obtener más valores después de agotado lanza StopIteration
# print(next(pares)) # Esto daría StopIteration si ya se consumió en el for
```

**Ventajas de los Generadores:**

*   **Eficiencia de Memoria:** No almacenan toda la secuencia. Ideal para secuencias infinitas o muy grandes.
*   **Lazy Evaluation:** Los valores se generan solo cuando se necesitan.
*   **Código Más Limpio:** A menudo más legible que crear una clase iteradora manualmente con `__iter__` y `__next__`.

## Expresiones Generadoras

Son una forma aún más concisa de crear generadores simples, usando una sintaxis similar a la de las comprensiones de listas, pero con **paréntesis `()`** en lugar de corchetes `[]`.

**Sintaxis:**

```python
(expresion for elemento in iterable if condicion)
```
*(El `if condicion` es opcional)*

**Ejemplo:**

```python
# Comprensión de lista (crea la lista completa en memoria)
cuadrados_lista = [x**2 for x in range(1000000)]
# print(cuadrados_lista) # ¡Ocuparía mucha memoria!

# Expresión generadora (crea un objeto generador, no calcula todo de golpe)
cuadrados_gen = (x**2 for x in range(1000000))
print(f"\nTipo de expresión generadora: {type(cuadrados_gen)}") # Salida: <class 'generator'>

# Podemos iterar sobre él como cualquier generador
print("Primeros 5 cuadrados del generador:")
for i in range(5):
    print(next(cuadrados_gen))

# O usarlo directamente en funciones que aceptan iterables
suma_primeros_10_cuadrados = sum(x**2 for x in range(10)) # No necesita paréntesis extra aquí
print(f"\nSuma de los primeros 10 cuadrados: {suma_primeros_10_cuadrados}")
```

**Generadores vs. Expresiones Generadoras:**

*   Usa **funciones generadoras (`yield`)** cuando la lógica para generar el siguiente valor es más compleja o necesitas mantener un estado interno más elaborado entre iteraciones.
*   Usa **expresiones generadoras (`(...)`)** para casos más simples, similares a las comprensiones de listas, pero donde quieres la eficiencia de memoria y la evaluación perezosa.

Los generadores son una herramienta fundamental en Python para escribir código eficiente y elegante al trabajar con secuencias de datos, especialmente cuando son grandes o potencialmente infinitas.
