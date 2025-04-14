# Módulo 1: Estructuras de Datos (Listas, Tuplas, Diccionarios, Conjuntos)

Además de los tipos de datos primitivos (int, float, bool, str), Python ofrece estructuras de datos incorporadas muy potentes para agrupar y organizar información. Las más importantes son:

## 1. Listas (`list`)

*   **¿Qué son?** Colecciones **ordenadas** y **mutables** (modificables) de elementos. Pueden contener elementos de diferentes tipos.
*   **Sintaxis:** Se definen usando corchetes `[]`, con los elementos separados por comas.
*   **Características Clave:**
    *   **Ordenadas:** Los elementos mantienen el orden en que se añadieron.
    *   **Mutables:** Puedes añadir, eliminar o modificar elementos después de crear la lista.
    *   **Indexadas:** Puedes acceder a los elementos por su posición (índice), empezando desde 0.
    *   **Permiten Duplicados:** Una lista puede contener el mismo elemento varias veces.

```python
# Crear listas
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", "cereza"]
mixta = [10, "hola", True, 3.14]
vacia = []

print(numeros)   # Salida: [1, 2, 3, 4, 5]
print(frutas)    # Salida: ['manzana', 'banana', 'cereza']
print(mixta)     # Salida: [10, 'hola', True, 3.14]

# Acceder a elementos por índice (base 0)
print(frutas[0])  # Salida: manzana
print(frutas[1])  # Salida: banana
print(numeros[-1]) # Índice negativo: empieza desde el final (-1 es el último) -> Salida: 5

# Modificar elementos (mutabilidad)
frutas[1] = "pera"
print(frutas)     # Salida: ['manzana', 'pera', 'cereza']

# Añadir elementos
frutas.append("naranja") # Añade al final
print(frutas)     # Salida: ['manzana', 'pera', 'cereza', 'naranja']
frutas.insert(1, "kiwi") # Inserta en una posición específica
print(frutas)     # Salida: ['manzana', 'kiwi', 'pera', 'cereza', 'naranja']

# Eliminar elementos
frutas.remove("pera") # Elimina la primera ocurrencia del valor
print(frutas)     # Salida: ['manzana', 'kiwi', 'cereza', 'naranja']
elemento_eliminado = frutas.pop(2) # Elimina por índice y devuelve el elemento
print(frutas)     # Salida: ['manzana', 'kiwi', 'naranja']
print(f"Elemento eliminado: {elemento_eliminado}") # Salida: Elemento eliminado: cereza
del frutas[0]     # Elimina por índice usando 'del'
print(frutas)     # Salida: ['kiwi', 'naranja']

# Longitud de la lista
print(len(frutas)) # Salida: 2

# Verificar si un elemento está en la lista
print("kiwi" in frutas) # Salida: True
print("uva" not in frutas) # Salida: True
```

## 2. Tuplas (`tuple`)

*   **¿Qué son?** Colecciones **ordenadas** e **inmutables** (no modificables) de elementos.
*   **Sintaxis:** Se definen usando paréntesis `()`, con los elementos separados por comas. (Los paréntesis son opcionales en algunos casos, pero recomendados por claridad).
*   **Características Clave:**
    *   **Ordenadas:** Mantienen el orden.
    *   **Inmutables:** Una vez creadas, no puedes añadir, eliminar ni modificar sus elementos.
    *   **Indexadas:** Puedes acceder a los elementos por su índice (base 0).
    *   **Permiten Duplicados:** Pueden contener elementos repetidos.
    *   **Más eficientes (en memoria y velocidad) que las listas para datos fijos.**

```python
# Crear tuplas
coordenadas = (10.5, -3.2)
colores_rgb = (255, 0, 128)
un_elemento = (5,) # ¡Ojo! Coma final necesaria para tupla de un solo elemento
mixta_tupla = (1, "dos", False)
vacia_tupla = ()

print(coordenadas)    # Salida: (10.5, -3.2)
print(colores_rgb)    # Salida: (255, 0, 128)
print(un_elemento)    # Salida: (5,)

# Acceder a elementos por índice
print(coordenadas[0]) # Salida: 10.5
print(colores_rgb[-1])# Salida: 128

# Intentar modificar una tupla dará error (TypeError)
# coordenadas[0] = 5.0 # Esto generaría un error

# Longitud de la tupla
print(len(colores_rgb)) # Salida: 3

# Verificar pertenencia
print(255 in colores_rgb) # Salida: True

# Usos comunes: coordenadas, registros de bases de datos, claves de diccionario compuestas (lo veremos).
```

## 3. Diccionarios (`dict`)

*   **¿Qué son?** Colecciones **desordenadas** (en versiones de Python < 3.7, ordenadas por inserción en >= 3.7) y **mutables** de pares **clave-valor**.
*   **Sintaxis:** Se definen usando llaves `{}`, con pares `clave: valor` separados por comas.
*   **Características Clave:**
    *   **Clave-Valor:** Cada elemento tiene una clave única que se usa para acceder a su valor asociado.
    *   **Claves Únicas e Inmutables:** Las claves deben ser únicas dentro del diccionario y deben ser de un tipo inmutable (strings, números, tuplas son comunes).
    *   **Mutables:** Puedes añadir, eliminar o modificar pares clave-valor.
    *   **Acceso por Clave:** No se accede por índice numérico, sino por la clave.
    *   **Optimizados para Búsqueda:** Muy eficientes para buscar un valor si conoces su clave.

```python
# Crear diccionarios
estudiante = {
    "nombre": "Carlos",
    "edad": 22,
    "curso": "Ingeniería",
    "activo": True
}
capitales = {"España": "Madrid", "Francia": "París", "Italia": "Roma"}
vacio_dict = {}

print(estudiante)
print(capitales)

# Acceder a valores por clave
print(estudiante["nombre"])  # Salida: Carlos
print(capitales["Francia"]) # Salida: París
# print(estudiante["apellido"]) # Daría KeyError si la clave no existe

# Acceso seguro con .get() (devuelve None si no existe, o un valor por defecto)
print(estudiante.get("edad"))      # Salida: 22
print(estudiante.get("apellido"))  # Salida: None
print(estudiante.get("apellido", "No especificado")) # Salida: No especificado

# Modificar valores
estudiante["edad"] = 23
print(estudiante)

# Añadir nuevos pares clave-valor
estudiante["universidad"] = "Universidad XYZ"
capitales["Alemania"] = "Berlín"
print(estudiante)
print(capitales)

# Eliminar pares clave-valor
del estudiante["activo"]
print(estudiante)
valor_eliminado = capitales.pop("Italia")
print(capitales)
print(f"Capital eliminada: {valor_eliminado}") # Salida: Capital eliminada: Roma

# Obtener claves, valores o pares (clave, valor)
print(list(estudiante.keys()))   # Salida: ['nombre', 'edad', 'curso', 'universidad'] (convertido a lista)
print(list(estudiante.values())) # Salida: ['Carlos', 23, 'Ingeniería', 'Universidad XYZ']
print(list(estudiante.items()))  # Salida: [('nombre', 'Carlos'), ('edad', 23), ('curso', 'Ingeniería'), ('universidad', 'Universidad XYZ')]

# Longitud (número de pares)
print(len(estudiante)) # Salida: 4

# Verificar si una clave existe
print("nombre" in estudiante) # Salida: True
print("Paris" in capitales)  # Salida: False (busca en claves, no valores)
```

## 4. Conjuntos (`set`)

*   **¿Qué son?** Colecciones **desordenadas** y **mutables** de elementos **únicos**.
*   **Sintaxis:** Se definen usando llaves `{}` o la función `set()`, con elementos separados por comas. ¡Ojo! `{}` crea un diccionario vacío, para un conjunto vacío usa `set()`.
*   **Características Clave:**
    *   **Desordenados:** No garantizan ningún orden específico de los elementos.
    *   **Elementos Únicos:** No permiten elementos duplicados. Si intentas añadir un elemento que ya existe, simplemente se ignora.
    *   **Mutables:** Puedes añadir o eliminar elementos.
    *   **No Indexados:** No puedes acceder a elementos por índice.
    *   **Optimizados para Pertenencia:** Muy eficientes para comprobar si un elemento está presente en el conjunto.
    *   **Operaciones de Conjuntos:** Soportan operaciones matemáticas como unión, intersección, diferencia.

```python
# Crear conjuntos
numeros_set = {1, 2, 3, 4, 5, 5, 5} # Los duplicados se eliminan
letras = set("hola mundo") # Crea un conjunto con las letras únicas
vacio_set = set() # Conjunto vacío

print(numeros_set) # Salida: {1, 2, 3, 4, 5} (el orden puede variar)
print(letras)      # Salida: {'o', 'u', 'd', 'l', 'h', ' ', 'n', 'm'} (el orden puede variar)
print(vacio_set)   # Salida: set()

# Añadir elementos
numeros_set.add(6)
numeros_set.add(3) # No hace nada porque 3 ya está
print(numeros_set) # Salida: {1, 2, 3, 4, 5, 6}

# Eliminar elementos
numeros_set.remove(4) # Elimina el elemento. Da KeyError si no existe.
print(numeros_set) # Salida: {1, 2, 3, 5, 6}
numeros_set.discard(2) # Elimina si existe, no da error si no existe.
numeros_set.discard(10) # No hace nada, no da error.
print(numeros_set) # Salida: {1, 3, 5, 6}
elemento_pop = numeros_set.pop() # Elimina y devuelve un elemento arbitrario
print(f"Elemento eliminado con pop: {elemento_pop}")
print(numeros_set)

# Longitud
print(len(letras))

# Verificar pertenencia (muy rápido)
print('a' in letras) # Salida: True
print('z' in letras) # Salida: False

# Operaciones de conjuntos
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

union = set_a.union(set_b) # o set_a | set_b
print(f"Unión: {union}") # Salida: Unión: {1, 2, 3, 4, 5, 6}

interseccion = set_a.intersection(set_b) # o set_a & set_b
print(f"Intersección: {interseccion}") # Salida: Intersección: {3, 4}

diferencia = set_a.difference(set_b) # o set_a - set_b (elementos en A pero no en B)
print(f"Diferencia (A-B): {diferencia}") # Salida: Diferencia (A-B): {1, 2}

diferencia_simetrica = set_a.symmetric_difference(set_b) # o set_a ^ set_b (elementos en A o B, pero no en ambos)
print(f"Diferencia Simétrica: {diferencia_simetrica}") # Salida: Diferencia Simétrica: {1, 2, 5, 6}
```

Elegir la estructura de datos correcta (lista, tupla, diccionario o conjunto) depende de lo que necesites hacer con tus datos: ¿necesitas orden? ¿modificabilidad? ¿unicidad? ¿acceso rápido por clave? Entender sus diferencias es clave para escribir código Python eficiente y efectivo.
