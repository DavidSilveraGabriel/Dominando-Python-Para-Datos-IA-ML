# Módulo 1: Control de Flujo - Bucles (`for`, `while`, `break`, `continue`)

Los bucles son estructuras de control que nos permiten ejecutar un bloque de código múltiples veces. Son fundamentales para procesar colecciones de datos o realizar tareas repetitivas sin tener que escribir el mismo código una y otra vez.

Python tiene dos tipos principales de bucles: `for` y `while`.

## Bucle `for`

El bucle `for` se utiliza para **iterar sobre una secuencia** (como una lista, tupla, diccionario, conjunto o cadena de texto) u otros objetos iterables. Ejecuta el bloque de código una vez por cada elemento en la secuencia.

**Sintaxis:**

```python
for variable_temporal in secuencia_o_iterable:
    # Bloque de código a ejecutar para cada elemento
    # La variable_temporal tomará el valor de cada elemento en cada iteración
    print(variable_temporal)
print("Fin del bucle for.")
```

*   `variable_temporal`: Es una variable que creas en el momento. En cada pasada (iteración) del bucle, tomará el valor del siguiente elemento de la `secuencia_o_iterable`. Puedes nombrarla como quieras (ej. `elemento`, `numero`, `fruta`, `letra`).
*   `secuencia_o_iterable`: Es la colección sobre la que quieres iterar.
*   El bloque de código indentado se ejecuta para cada elemento.

**Ejemplos:**

```python
# Iterar sobre una lista
frutas = ["manzana", "banana", "cereza"]
print("Iterando sobre lista de frutas:")
for fruta in frutas:
    print(f"- {fruta}")

# Iterar sobre una cadena de texto (string)
mensaje = "Hola"
print("\nIterando sobre un string:")
for letra in mensaje:
    print(letra)

# Iterar sobre una secuencia de números usando range()
# range(n): genera números desde 0 hasta n-1
# range(inicio, fin): genera números desde inicio hasta fin-1
# range(inicio, fin, paso): genera números desde inicio hasta fin-1, con un incremento de 'paso'
print("\nIterando con range(5):")
for i in range(5): # Genera 0, 1, 2, 3, 4
    print(i)

print("\nIterando con range(2, 7):")
for num in range(2, 7): # Genera 2, 3, 4, 5, 6
    print(num)

print("\nIterando con range(0, 10, 2):")
for par in range(0, 10, 2): # Genera 0, 2, 4, 6, 8
    print(par)

# Iterar sobre las claves de un diccionario
estudiante = {"nombre": "Ana", "edad": 21, "curso": "Biología"}
print("\nIterando sobre claves de diccionario:")
for clave in estudiante: # Por defecto itera sobre las claves
    print(f"Clave: {clave}, Valor: {estudiante[clave]}")

# Iterar sobre los valores de un diccionario
print("\nIterando sobre valores de diccionario:")
for valor in estudiante.values():
    print(valor)

# Iterar sobre los pares clave-valor de un diccionario
print("\nIterando sobre items (clave-valor) de diccionario:")
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")
```

## Bucle `while`

El bucle `while` ejecuta un bloque de código **mientras** una condición especificada sea `True`.

**Sintaxis:**

```python
while condicion:
    # Bloque de código a ejecutar mientras la condicion sea True
    # ¡Importante! Dentro del bucle, algo debe eventualmente
    # hacer que la condicion se vuelva False, o tendrás un bucle infinito.
    print("La condición sigue siendo verdadera.")
    # ...hacer algo que afecte la condición...
print("Fin del bucle while (la condición se volvió falsa).")
```

*   `condicion`: Expresión booleana. El bucle se ejecuta repetidamente mientras esta condición sea `True`.
*   El bloque indentado se ejecuta en cada iteración.
*   **¡Peligro de Bucle Infinito!** Si la condición nunca se vuelve `False`, el bucle se ejecutará para siempre (o hasta que interrumpas el programa manualmente). Asegúrate de que algo dentro del bucle modifique las variables involucradas en la condición.

**Ejemplos:**

```python
# Contar hasta 5
contador = 0
print("Bucle while contando hasta 4:")
while contador < 5:
    print(f"Contador es: {contador}")
    contador += 1 # ¡Fundamental! Modificamos la variable de la condición
print("Fin del conteo.")

# Esperar una entrada específica del usuario
entrada = ""
print("\nBucle while esperando 'salir':")
while entrada.lower() != "salir":
    entrada = input("Escribe 'salir' para terminar: ")
    print(f"Escribiste: {entrada}")
print("¡Saliste del bucle!")
```

## `break` y `continue`

Estas dos declaraciones permiten controlar el flujo dentro de los bucles:

1.  **`break`:**
    *   Termina **inmediatamente** el bucle actual (tanto `for` como `while`), incluso si la condición del `while` sigue siendo `True` o si quedan elementos por iterar en el `for`.
    *   La ejecución continúa en la primera línea *después* del bucle.

2.  **`continue`:**
    *   Salta **el resto de la iteración actual** del bucle.
    *   La ejecución pasa directamente al **inicio de la siguiente iteración**.
    *   En un `while`, se vuelve a evaluar la condición.
    *   En un `for`, se pasa al siguiente elemento de la secuencia.

**Ejemplos:**

```python
# Ejemplo con break: encontrar el primer número divisible por 7
numeros = [12, 15, 21, 25, 30, 35, 40]
print("\nBuscando el primer divisible por 7 (con break):")
numero_encontrado = None
for num in numeros:
    print(f"Probando {num}...")
    if num % 7 == 0:
        numero_encontrado = num
        print(f"¡Encontrado! {num} es divisible por 7.")
        break # Salimos del bucle for inmediatamente
print(f"El primer número divisible por 7 es: {numero_encontrado}")

# Ejemplo con continue: imprimir solo números impares
print("\nImprimiendo solo impares (con continue):")
for i in range(10): # Números del 0 al 9
    if i % 2 == 0: # Si es par...
        continue   # ...saltamos al siguiente número, no ejecutamos el print
    print(f"Impar: {i}")

# Ejemplo while con break
print("\nBucle while con break:")
contador_infinito = 0
while True: # Bucle potencialmente infinito
    print(f"Iteración {contador_infinito}")
    contador_infinito += 1
    if contador_infinito >= 5:
        print("Alcanzado el límite, saliendo con break.")
        break
```

Los bucles `for` y `while`, junto con `break` y `continue`, te dan un control muy preciso sobre cómo y cuántas veces se repite una porción de tu código. Son herramientas esenciales para la automatización y el procesamiento de datos.
