# Ejercicios: Módulo 2 - Comprensión de Listas, Diccionarios y Conjuntos

# --- Ejercicio 1: List Comprehension Básica ---
# Instrucciones: Dada la lista `numeros = [1, 2, 3, 4, 5, 6]`, crea una nueva lista
# llamada `triples` que contenga el triple de cada número en la lista original,
# usando una list comprehension. Imprime la lista `triples`.

print("--- Ejercicio 1: List Comprehension Básica ---")
numeros = [1, 2, 3, 4, 5, 6]
# Escribe tu código aquí
triples = [n * 3 for n in numeros]
print(f"Lista original: {numeros}")
print(f"Lista de triples: {triples}")


# --- Ejercicio 2: List Comprehension con Condición (`if`) ---
# Instrucciones: Dada la lista `numeros = [10, 5, 20, 15, 30, 25]`, crea una nueva lista
# llamada `mayores_a_15` que contenga solo los números de la lista original que
# sean estrictamente mayores que 15, usando list comprehension con `if`. Imprime la lista resultante.

print("\n--- Ejercicio 2: List Comprehension con if ---")
numeros = [10, 5, 20, 15, 30, 25]
# Escribe tu código aquí
mayores_a_15 = [n for n in numeros if n > 15]
print(f"Lista original: {numeros}")
print(f"Números mayores a 15: {mayores_a_15}")


# --- Ejercicio 3: List Comprehension con `if-else` ---
# Instrucciones: Dada la lista `palabras = ["python", "es", "genial", "y", "útil"]`,
# crea una nueva lista llamada `longitud_clasificada` donde cada elemento sea:
# - La palabra misma si su longitud es mayor a 4.
# - La cadena "corta" si la longitud de la palabra es 4 o menor.
# Usa list comprehension con una expresión condicional `if-else`. Imprime la lista resultante.

print("\n--- Ejercicio 3: List Comprehension con if-else ---")
palabras = ["python", "es", "genial", "y", "útil"]
# Escribe tu código aquí
longitud_clasificada = [p if len(p) > 4 else "corta" for p in palabras]
print(f"Lista original: {palabras}")
print(f"Longitud clasificada: {longitud_clasificada}")


# --- Ejercicio 4: Dictionary Comprehension ---
# Instrucciones: Dada la lista `paises = ["España", "Francia", "Alemania"]`, crea un
# diccionario llamado `iniciales_paises` donde las claves sean los nombres de los países
# y los valores sean sus dos primeras letras en mayúsculas (ej. "ES", "FR", "AL").
# Usa una dictionary comprehension. Imprime el diccionario resultante.

print("\n--- Ejercicio 4: Dictionary Comprehension ---")
paises = ["España", "Francia", "Alemania"]
# Escribe tu código aquí
iniciales_paises = {pais: pais[:2].upper() for pais in paises}
print(f"Lista original: {paises}")
print(f"Diccionario de iniciales: {iniciales_paises}")


# --- Ejercicio 5: Dictionary Comprehension con Condición (`if`) ---
# Instrucciones: Dado el diccionario `productos = {"manzana": 0.5, "pera": 0.7, "naranja": 0.4, "uva": 1.2}`,
# crea un nuevo diccionario llamado `productos_caros` que contenga solo los productos
# cuyo precio (valor) sea mayor a 0.6. Usa dictionary comprehension con `if`. Imprime el resultado.

print("\n--- Ejercicio 5: Dictionary Comprehension con if ---")
productos = {"manzana": 0.5, "pera": 0.7, "naranja": 0.4, "uva": 1.2}
# Escribe tu código aquí
productos_caros = {nombre: precio for nombre, precio in productos.items() if precio > 0.6}
print(f"Diccionario original: {productos}")
print(f"Productos caros (> 0.6): {productos_caros}")


# --- Ejercicio 6: Set Comprehension ---
# Instrucciones: Dada la lista `numeros_duplicados = [1, 5, 2, 8, 5, 3, 1, 9, 2]`,
# crea un conjunto (`set`) llamado `numeros_unicos_pares` que contenga solo los números
# pares únicos de la lista original. Usa una set comprehension con `if`. Imprime el conjunto resultante.

print("\n--- Ejercicio 6: Set Comprehension con if ---")
numeros_duplicados = [1, 5, 2, 8, 5, 3, 1, 9, 2]
# Escribe tu código aquí
numeros_unicos_pares = {n for n in numeros_duplicados if n % 2 == 0}
print(f"Lista original: {numeros_duplicados}")
print(f"Conjunto de números pares únicos: {numeros_unicos_pares}")


# --- Fin de los ejercicios ---
