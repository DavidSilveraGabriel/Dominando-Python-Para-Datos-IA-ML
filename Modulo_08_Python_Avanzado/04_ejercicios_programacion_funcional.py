# Ejercicios: Módulo 8 - Programación Funcional

from functools import reduce, partial

print("--- Conceptos de Programación Funcional ---")

# --- Ejercicio 1: Funciones Puras vs. Impuras ---
# Instrucciones:
# Analiza las siguientes funciones y determina (en comentarios) si son puras o impuras,
# explicando brevemente por qué.

# Función A
lista_global = []
def agregar_a_lista(elemento):
    lista_global.append(elemento)
    print(f"Lista global ahora: {lista_global}")
# Respuesta A: Impura. Modifica un estado externo (lista_global) y tiene un efecto secundario (imprimir).

# Función B
def sumar_dos(a, b):
    return a + b
# Respuesta B: Pura. Para las mismas entradas (a, b), siempre devuelve la misma salida (a+b) y no tiene efectos secundarios.

# Función C
import random
def obtener_numero_aleatorio(limite):
    return random.randint(0, limite)
# Respuesta C: Impura. No siempre devuelve la misma salida para la misma entrada (limite) debido a la aleatoriedad.

# Función D
def calcular_cuadrado(numero):
    resultado = numero * numero
    # print(f"El cuadrado de {numero} es {resultado}") # Si descomentamos, se vuelve impura
    return resultado
# Respuesta D: Pura (tal como está escrita). Devuelve siempre el mismo resultado para la misma entrada y no tiene efectos secundarios. Si tuviera el print, sería impura.

print("--- Ejercicio 1: Funciones Puras vs. Impuras ---")
print("Ver comentarios en el código para las respuestas.")
print("-" * 20)


# --- Ejercicio 2: `map()` ---
# Instrucciones:
# 1. Tienes una lista de números: `numeros = [1, 2, 3, 4, 5, 6]`.
# 2. Usa la función `map()` junto con una función `lambda` para crear un *iterador*
#    que produzca el triple de cada número en la lista `numeros`.
# 3. Convierte el iterador resultante a una lista e imprímela.

print("\n--- Ejercicio 2: `map()` ---")
# Escribe tu código aquí
# 1. Lista original
numeros = [1, 2, 3, 4, 5, 6]
print(f"Lista original: {numeros}")

# 2. Usar map con lambda
iterador_triples = map(lambda x: x * 3, numeros)
print(f"Tipo de iterador_triples: {type(iterador_triples)}")

# 3. Convertir a lista e imprimir
lista_triples = list(iterador_triples)
print(f"Lista con el triple de cada número: {lista_triples}")
print("-" * 20)


# --- Ejercicio 3: `filter()` ---
# Instrucciones:
# 1. Tienes una lista de palabras: `palabras = ["python", "programacion", "funcional", "lambda", "map", "filter", "reduce"]`.
# 2. Usa la función `filter()` junto con una función `lambda` para crear un *iterador*
#    que contenga solo las palabras de la lista `palabras` que tengan más de 6 caracteres.
# 3. Convierte el iterador resultante a una lista e imprímela.

print("\n--- Ejercicio 3: `filter()` ---")
# Escribe tu código aquí
# 1. Lista original
palabras = ["python", "programacion", "funcional", "lambda", "map", "filter", "reduce"]
print(f"Lista original: {palabras}")

# 2. Usar filter con lambda
iterador_largas = filter(lambda p: len(p) > 6, palabras)
print(f"Tipo de iterador_largas: {type(iterador_largas)}")

# 3. Convertir a lista e imprimir
lista_largas = list(iterador_largas)
print(f"Palabras con más de 6 caracteres: {lista_largas}")
print("-" * 20)


# --- Ejercicio 4: `functools.reduce()` ---
# Instrucciones:
# 1. Importa `reduce` desde `functools`.
# 2. Tienes la lista de números: `numeros_reduce = [5, 2, 3, 8, 1]`.
# 3. Usa `reduce()` con una función `lambda` para calcular el producto de todos los números en `numeros_reduce`.
# 4. Imprime el resultado.
# 5. Usa `reduce()` con una función `lambda` para encontrar el número más grande en `numeros_reduce`.
# 6. Imprime el resultado.

print("\n--- Ejercicio 4: `functools.reduce()` ---")
# 1. Importar (hecho al principio)
# from functools import reduce

# 2. Lista original
numeros_reduce = [5, 2, 3, 8, 1]
print(f"Lista original: {numeros_reduce}")

# 3. Calcular producto con reduce
producto_total = reduce(lambda acumulador, elemento: acumulador * elemento, numeros_reduce)
# Paso a paso (aproximado):
# 5 * 2 = 10
# 10 * 3 = 30
# 30 * 8 = 240
# 240 * 1 = 240

# 4. Imprimir producto
print(f"Producto de todos los números: {producto_total}")

# 5. Encontrar el máximo con reduce
maximo_numero = reduce(lambda max_actual, elemento: elemento if elemento > max_actual else max_actual, numeros_reduce)
# Alternativa: reduce(max, numeros_reduce) si importas max o usas la built-in

# 6. Imprimir máximo
print(f"Número máximo en la lista: {maximo_numero}")
print("-" * 20)


# --- Ejercicio 5: `functools.partial` ---
# Instrucciones:
# 1. Importa `partial` desde `functools`.
# 2. Define una función `potencia(base, exponente)` que devuelva `base ** exponente`.
# 3. Usa `partial()` para crear una nueva función `cuadrado` que sea una versión
#    parcial de `potencia` donde el `exponente` siempre sea 2.
# 4. Usa `partial()` para crear otra función `cubo` donde el `exponente` siempre sea 3.
# 5. Llama a `cuadrado(5)` e imprime el resultado (debería ser 25).
# 6. Llama a `cubo(3)` e imprime el resultado (debería ser 27).
# 7. Usa `partial()` para crear una función `potencia_de_dos` donde la `base` siempre sea 2.
# 8. Llama a `potencia_de_dos(10)` e imprime el resultado (debería ser 1024).

print("\n--- Ejercicio 5: `functools.partial` ---")
# 1. Importar (hecho al principio)
# from functools import partial

# 2. Definir función original
def potencia(base, exponente):
    """Calcula la potencia de una base."""
    print(f"Calculando {base} ** {exponente}")
    return base ** exponente

# 3. Crear función 'cuadrado'
cuadrado = partial(potencia, exponente=2)
# cuadrado(x) es ahora equivalente a potencia(x, exponente=2)

# 4. Crear función 'cubo'
cubo = partial(potencia, exponente=3)
# cubo(x) es ahora equivalente a potencia(x, exponente=3)

# 5. Llamar a cuadrado
res_cuadrado = cuadrado(5)
print(f"cuadrado(5) = {res_cuadrado}")

# 6. Llamar a cubo
res_cubo = cubo(3)
print(f"cubo(3) = {res_cubo}")

# 7. Crear función 'potencia_de_dos'
potencia_de_dos = partial(potencia, base=2)
# potencia_de_dos(y) es ahora equivalente a potencia(base=2, exponente=y)

# 8. Llamar a potencia_de_dos
res_pot_dos = potencia_de_dos(10)
print(f"potencia_de_dos(10) = {res_pot_dos}")
print("-" * 20)

# --- Fin de los ejercicios ---
