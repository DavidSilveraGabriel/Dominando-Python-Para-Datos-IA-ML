# Módulo 2: Comprensión de Listas, Diccionarios y Conjuntos

Las **comprensiones** (Comprehensions) son una característica muy "Pythonica" que ofrece una sintaxis concisa y legible para crear nuevas listas, diccionarios o conjuntos a partir de secuencias existentes (u otros iterables). A menudo, pueden reemplazar bucles `for` más largos y explícitos para tareas comunes de creación de colecciones.

## 1. Comprensión de Listas (List Comprehensions)

Permiten crear nuevas listas aplicando una expresión a cada elemento de una secuencia iterable, opcionalmente filtrando elementos con una condición.

**Sintaxis Básica:**

```python
nueva_lista = [expresion for elemento in iterable]
```

**Sintaxis con Condición (`if`):**

```python
nueva_lista = [expresion for elemento in iterable if condicion]
```

**Sintaxis con `if-else` (Expresión Condicional):**

```python
nueva_lista = [expresion_si_true if condicion else expresion_si_false for elemento in iterable]
```

**Equivalencia con Bucle `for`:**

La sintaxis básica `[expresion for elemento in iterable]` es equivalente a:

```python
nueva_lista = []
for elemento in iterable:
    nueva_lista.append(expresion)
```

La sintaxis con `if` `[expresion for elemento in iterable if condicion]` es equivalente a:

```python
nueva_lista = []
for elemento in iterable:
    if condicion:
        nueva_lista.append(expresion)
```

**Ejemplos:**

```python
# Ejemplo 1: Crear una lista con los cuadrados de los números del 0 al 9
# Usando bucle for tradicional
cuadrados_for = []
for x in range(10):
    cuadrados_for.append(x**2)
print(f"Cuadrados (for): {cuadrados_for}")

# Usando list comprehension (más conciso)
cuadrados_comp = [x**2 for x in range(10)]
print(f"Cuadrados (comp): {cuadrados_comp}")

# Ejemplo 2: Crear una lista con los números pares del 0 al 9
# Usando bucle for con if
pares_for = []
for x in range(10):
    if x % 2 == 0:
        pares_for.append(x)
print(f"Pares (for): {pares_for}")

# Usando list comprehension con if
pares_comp = [x for x in range(10) if x % 2 == 0]
print(f"Pares (comp): {pares_comp}")

# Ejemplo 3: Crear una lista de frutas en mayúsculas
frutas = ["manzana", "banana", "cereza"]
mayusculas_comp = [fruta.upper() for fruta in frutas]
print(f"Frutas mayúsculas: {mayusculas_comp}")

# Ejemplo 4: Crear una lista indicando si cada número es par o impar
numeros = [0, 1, 2, 3, 4, 5]
par_impar_comp = ["Par" if num % 2 == 0 else "Impar" for num in numeros]
print(f"Par/Impar: {par_impar_comp}")

# Ejemplo 5: Comprensiones anidadas (crear pares)
pares_anidados = [(x, y) for x in [1, 2] for y in [3, 4]]
# Equivalente a:
# pares_anidados_for = []
# for x in [1, 2]:
#     for y in [3, 4]:
#         pares_anidados_for.append((x, y))
print(f"Pares anidados: {pares_anidados}") # Salida: [(1, 3), (1, 4), (2, 3), (2, 4)]
```

## 2. Comprensión de Diccionarios (Dictionary Comprehensions)

Similar a las listas, pero crean diccionarios. Se usan llaves `{}` y se especifica un par `clave: valor`.

**Sintaxis Básica:**

```python
nuevo_dict = {clave_expresion: valor_expresion for elemento in iterable}
```

**Sintaxis con Condición (`if`):**

```python
nuevo_dict = {clave_expresion: valor_expresion for elemento in iterable if condicion}
```

**Ejemplos:**

```python
# Ejemplo 1: Crear un diccionario con números y sus cuadrados
cuadrados_dict = {x: x**2 for x in range(5)}
print(f"Dict cuadrados: {cuadrados_dict}")
# Salida: Dict cuadrados: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Ejemplo 2: Crear un diccionario a partir de dos listas (nombres y edades)
nombres = ["Ana", "Luis", "Eva"]
edades = [25, 30, 22]
# Usando zip para emparejar las listas
personas_dict = {nombre: edad for nombre, edad in zip(nombres, edades)}
print(f"Dict personas: {personas_dict}")
# Salida: Dict personas: {'Ana': 25, 'Luis': 30, 'Eva': 22}

# Ejemplo 3: Crear un diccionario con palabras y su longitud, solo para palabras largas
texto = "esta es una frase de ejemplo con algunas palabras"
palabras = texto.split() # Divide el string en una lista de palabras
largas_dict = {palabra: len(palabra) for palabra in palabras if len(palabra) > 4}
print(f"Dict palabras largas: {largas_dict}")
# Salida: Dict palabras largas: {'frase': 5, 'ejemplo': 7, 'algunas': 7, 'palabras': 8}

# Ejemplo 4: Invertir un diccionario (claves por valores) - ¡Cuidado si los valores no son únicos!
original_dict = {'a': 1, 'b': 2, 'c': 3}
invertido_dict = {valor: clave for clave, valor in original_dict.items()}
print(f"Dict invertido: {invertido_dict}")
# Salida: Dict invertido: {1: 'a', 2: 'b', 3: 'c'}
```

## 3. Comprensión de Conjuntos (Set Comprehensions)

Crean conjuntos (`set`). La sintaxis es similar a la de listas, pero usando llaves `{}` y sin especificar un par clave-valor (solo la expresión para el elemento). Recuerda que los conjuntos solo almacenan elementos únicos.

**Sintaxis Básica:**

```python
nuevo_set = {expresion for elemento in iterable}
```

**Sintaxis con Condición (`if`):**

```python
nuevo_set = {expresion for elemento in iterable if condicion}
```

**Ejemplos:**

```python
# Ejemplo 1: Crear un conjunto con los cuadrados de números (duplicados se eliminan)
numeros_lista = [1, 2, 2, 3, 3, 3, 4]
cuadrados_set = {x**2 for x in numeros_lista}
print(f"Set cuadrados: {cuadrados_set}")
# Salida: Set cuadrados: {1, 4, 9, 16}

# Ejemplo 2: Crear un conjunto con las iniciales en mayúscula de una lista de nombres
nombres = ["ana", "luis", "eva", "ana"]
iniciales_set = {nombre[0].upper() for nombre in nombres}
print(f"Set iniciales: {iniciales_set}")
# Salida: Set iniciales: {'E', 'A', 'L'}

# Ejemplo 3: Crear un conjunto de números divisibles por 3 del 0 al 15
divisibles_3_set = {n for n in range(16) if n % 3 == 0}
print(f"Set divisibles por 3: {divisibles_3_set}")
# Salida: Set divisibles por 3: {0, 3, 6, 9, 12, 15}
```

**Ventajas de las Comprensiones:**

*   **Concisión:** Código más corto y a menudo más legible que los bucles `for` equivalentes.
*   **Eficiencia:** Suelen ser ligeramente más rápidas que los bucles `for` explícitos para crear colecciones, ya que están optimizadas internamente en CPython.

**Cuándo usarlas:**

Son ideales para crear colecciones basadas en transformaciones o filtrados simples de otras secuencias. Si la lógica para crear cada elemento es muy compleja (múltiples `if/else`, cálculos extensos), un bucle `for` tradicional podría ser más legible.
