# Ejercicios: Módulo 1 - Control de Flujo - Bucles (`for`, `while`, `break`, `continue`)

# --- Ejercicio 1: Bucle `for` con Listas ---
# Instrucciones: Dada la lista `nombres = ["Ana", "Luis", "Marta", "Juan", "Sofía"]`,
# usa un bucle `for` para imprimir un saludo personalizado para cada nombre,
# por ejemplo: "¡Hola, Ana!".

print("--- Ejercicio 1: Bucle for con Listas ---")
nombres = ["Ana", "Luis", "Marta", "Juan", "Sofía"]

# Escribe tu código aquí
for nombre in nombres:
    print(f"¡Hola, {nombre}!")


# --- Ejercicio 2: Bucle `for` con `range()` ---
# Instrucciones:
# 1. Usa un bucle `for` y la función `range()` para imprimir los números del 1 al 10 (ambos inclusive).
# 2. Usa otro bucle `for` y `range()` para imprimir los números pares del 2 al 20 (ambos inclusive).
# 3. Usa otro bucle `for` y `range()` para imprimir los números del 10 al 1 en orden descendente.

print("\n--- Ejercicio 2: Bucle for con range() ---")
# 1. Números del 1 al 10
print("Números del 1 al 10:")
# Escribe tu código aquí
for i in range(1, 11): # range(inicio, fin_no_incluido)
    print(i)

# 2. Números pares del 2 al 20
print("\nNúmeros pares del 2 al 20:")
# Escribe tu código aquí
for i in range(2, 21, 2): # range(inicio, fin_no_incluido, paso)
    print(i)

# 3. Números del 10 al 1
print("\nNúmeros del 10 al 1:")
# Escribe tu código aquí
for i in range(10, 0, -1): # range(inicio, fin_no_incluido, paso_negativo)
    print(i)


# --- Ejercicio 3: Bucle `while` ---
# Instrucciones: Escribe un programa que simule una cuenta atrás desde 5 hasta 1.
# Usa un bucle `while` y luego imprime "¡Despegue!".

print("\n--- Ejercicio 3: Bucle while ---")
# Escribe tu código aquí
contador = 5
while contador >= 1:
    print(contador)
    contador -= 1 # Decrementamos el contador
print("¡Despegue!")


# --- Ejercicio 4: Bucle `while` con Entrada del Usuario ---
# Instrucciones: Escribe un programa que pida al usuario que adivine un número secreto (ej. 7).
# El programa debe seguir pidiendo un número hasta que el usuario adivine correctamente.
# Imprime un mensaje de felicitación cuando adivine.
# Maneja el caso de que el usuario introduzca algo que no sea un número.

print("\n--- Ejercicio 4: Adivina el Número ---")
numero_secreto = 7
adivinado = False

# Escribe tu código aquí
while not adivinado:
    try:
        intento = int(input("Adivina el número secreto (pista: es < 10): "))
        if intento == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número {numero_secreto}.")
            adivinado = True # Terminamos el bucle
        else:
            print("Incorrecto. Intenta de nuevo.")
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número entero.")


# --- Ejercicio 5: Uso de `break` ---
# Instrucciones: Dada la lista `numeros = [2, 4, 6, 8, 9, 10, 12]`, usa un bucle `for`
# para buscar el primer número impar. Si lo encuentras, imprime un mensaje indicando
# cuál es y termina el bucle inmediatamente usando `break`. Si el bucle termina sin
# encontrar un número impar, imprime "No se encontraron números impares".
# Pista: Puedes usar un `else` asociado al `for` para el caso en que no se use `break`.

print("\n--- Ejercicio 5: Uso de break ---")
numeros = [2, 4, 6, 8, 9, 10, 12]
# Escribe tu código aquí
for num in numeros:
    if num % 2 != 0: # Si es impar
        print(f"Primer número impar encontrado: {num}")
        break # Salimos del bucle
else:
    # Este bloque else se ejecuta SOLO si el bucle for termina
    # de forma natural (sin un break)
    print("No se encontraron números impares en la lista.")


# --- Ejercicio 6: Uso de `continue` ---
# Instrucciones: Usa un bucle `for` para iterar sobre los números del 1 al 15.
# Imprime cada número, excepto aquellos que sean múltiplos de 3. Usa `continue`
# para saltar la impresión de los múltiplos de 3.

print("\n--- Ejercicio 6: Uso de continue ---")
# Escribe tu código aquí
for i in range(1, 16):
    if i % 3 == 0:
        continue # Saltamos al siguiente número si es múltiplo de 3
    print(i)


# --- Fin de los ejercicios ---
