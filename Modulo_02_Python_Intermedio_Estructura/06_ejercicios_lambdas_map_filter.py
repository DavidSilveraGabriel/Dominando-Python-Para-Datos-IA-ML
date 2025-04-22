# Ejercicios: Módulo 2 - Funciones Lambda, map y filter

# --- Ejercicio 1: Funciones Lambda ---
# Instrucciones:
# 1. Crea una función lambda llamada `area_triangulo` que acepte `base` y `altura`
#    y devuelva el área (base * altura / 2).
# 2. Llama a la lambda `area_triangulo` con una base de 10 y altura de 5 e imprime el resultado.
# 3. Dada la lista `numeros = [-5, 10, -15, 20, -25]`, usa la función `sorted()` y una
#    lambda como `key` para ordenar la lista basándose en el valor absoluto de los números.
#    Imprime la lista ordenada.

print("--- Ejercicio 1: Funciones Lambda ---")
# Escribe tu código aquí
# 1. Lambda para área de triángulo
area_triangulo = lambda base, altura: (base * altura) / 2

# 2. Llamada a la lambda
base_t = 10
altura_t = 5
area_calculada = area_triangulo(base_t, altura_t)
print(f"Área del triángulo ({base_t}x{altura_t}): {area_calculada}")

# 3. Ordenar por valor absoluto usando lambda
numeros = [-5, 10, -15, 20, -25]
numeros_ordenados_abs = sorted(numeros, key=lambda x: abs(x))
print(f"Lista original: {numeros}")
print(f"Lista ordenada por valor absoluto: {numeros_ordenados_abs}")


# --- Ejercicio 2: Función `map()` ---
# Instrucciones:
# 1. Dada la lista `cadenas = ["hola", "python", "mundo"]`, usa `map()` y una lambda
#    para crear una nueva lista (o iterador) que contenga la longitud de cada cadena.
# 2. Convierte el resultado de `map()` a una lista e imprímela.
# 3. Dada la lista `grados_celsius = [0, 10, 20, 30, 100]`, usa `map()` y una lambda
#    para convertir cada temperatura a grados Fahrenheit usando la fórmula: F = (C * 9/5) + 32.
# 4. Convierte el resultado a una lista e imprímela (puedes redondear los resultados si quieres).

print("\n--- Ejercicio 2: Función map() ---")
# Escribe tu código aquí
# 1. Longitud de cadenas con map y lambda
cadenas = ["hola", "python", "mundo"]
longitudes_iter = map(lambda s: len(s), cadenas)

# 2. Convertir a lista e imprimir
longitudes_lista = list(longitudes_iter)
print(f"Lista original de cadenas: {cadenas}")
print(f"Longitudes calculadas con map: {longitudes_lista}")

# 3. Convertir Celsius a Fahrenheit con map y lambda
grados_celsius = [0, 10, 20, 30, 100]
grados_fahrenheit_iter = map(lambda c: (c * 9/5) + 32, grados_celsius)

# 4. Convertir a lista e imprimir
grados_fahrenheit_lista = list(grados_fahrenheit_iter)
print(f"Grados Celsius: {grados_celsius}")
print(f"Grados Fahrenheit (map): {grados_fahrenheit_lista}")


# --- Ejercicio 3: Función `filter()` ---
# Instrucciones:
# 1. Dada la lista `numeros = list(range(1, 21))` (números del 1 al 20), usa `filter()`
#    y una lambda para obtener solo los números que son múltiplos de 3.
# 2. Convierte el resultado de `filter()` a una lista e imprímela.
# 3. Dada la lista `mezcla = ["texto", None, 100, "", 0, True, [], "datos"]`, usa `filter()`
#    con `None` como primer argumento para obtener solo los elementos que son considerados "Truthy".
# 4. Convierte el resultado a una lista e imprímela.

print("\n--- Ejercicio 3: Función filter() ---")
# Escribe tu código aquí
# 1. Filtrar múltiplos de 3
numeros = list(range(1, 21))
multiplos_3_iter = filter(lambda n: n % 3 == 0, numeros)

# 2. Convertir a lista e imprimir
multiplos_3_lista = list(multiplos_3_iter)
print(f"Números del 1 al 20: {numeros}")
print(f"Múltiplos de 3 (filter): {multiplos_3_lista}")

# 3. Filtrar elementos "Truthy"
mezcla = ["texto", None, 100, "", 0, True, [], "datos"]
elementos_truthy_iter = filter(None, mezcla)

# 4. Convertir a lista e imprimir
elementos_truthy_lista = list(elementos_truthy_iter)
print(f"Lista original mezclada: {mezcla}")
print(f"Elementos 'Truthy' (filter None): {elementos_truthy_lista}")


# --- Ejercicio 4: Combinando `map` y `filter` ---
# Instrucciones:
# 1. Dada la lista `numeros = list(range(1, 11))` (números del 1 al 10).
# 2. Primero, usa `filter()` y una lambda para obtener solo los números pares.
# 3. Luego, usa `map()` y una lambda sobre el resultado del filtro para calcular el cuadrado de cada número par.
# 4. Convierte el resultado final a una lista e imprímela. (Deberías obtener [4, 16, 36, 64, 100]).

print("\n--- Ejercicio 4: Combinando map y filter ---")
numeros = list(range(1, 11))
# Escribe tu código aquí
# Paso 1: Filtrar pares
numeros_pares_iter = filter(lambda x: x % 2 == 0, numeros)

# Paso 2: Mapear a cuadrados sobre el resultado del filtro
cuadrados_pares_iter = map(lambda x: x**2, numeros_pares_iter)

# Paso 3: Convertir a lista e imprimir
cuadrados_pares_lista = list(cuadrados_pares_iter)
print(f"Números originales: {numeros}")
print(f"Cuadrados de los números pares: {cuadrados_pares_lista}")

# Alternativa con List Comprehension (más concisa para este caso)
cuadrados_pares_comp = [x**2 for x in numeros if x % 2 == 0]
print(f"Cuadrados pares (List Comp): {cuadrados_pares_comp}")


# --- Fin de los ejercicios ---
