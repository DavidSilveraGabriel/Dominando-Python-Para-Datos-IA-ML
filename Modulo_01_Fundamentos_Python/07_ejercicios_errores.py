# Ejercicios: Módulo 1 - Manejo de Errores Básicos (`try`, `except`)

# --- Ejercicio 1: División Segura ---
# Instrucciones:
# 1. Define una función llamada `dividir_numeros` que reciba dos argumentos: `dividendo` y `divisor`.
# 2. Dentro de la función, usa un bloque `try...except` para intentar realizar la división `dividendo / divisor`.
# 3. Si la división es exitosa, la función debe devolver el resultado.
# 4. Si ocurre un error `ZeroDivisionError` (división por cero), la función debe imprimir un mensaje
#    "Error: No se puede dividir por cero." y devolver `None`.
# 5. Llama a la función con valores válidos (ej. 10, 2) e imprime el resultado.
# 6. Llama a la función intentando dividir por cero (ej. 5, 0) e imprime el resultado (que debería ser None).

print("--- Ejercicio 1: División Segura ---")
# Escribe tu código aquí
def dividir_numeros(dividendo, divisor):
    """Divide dos números de forma segura, manejando la división por cero."""
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
        return None

# Llamada con valores válidos
resultado_valido = dividir_numeros(10, 2)
print(f"Resultado de 10 / 2: {resultado_valido}")

# Llamada con división por cero
resultado_invalido = dividir_numeros(5, 0)
print(f"Resultado de 5 / 0: {resultado_invalido}")


# --- Ejercicio 2: Conversión Numérica Segura ---
# Instrucciones:
# 1. Escribe un programa que solicite al usuario introducir un número usando `input()`.
# 2. Usa un bloque `try...except` para intentar convertir la entrada del usuario a un número flotante (`float`).
# 3. Si la conversión es exitosa, imprime "Número introducido: [número]".
# 4. Si ocurre un `ValueError` (porque el usuario no introdujo un número válido), imprime
#    "Error: La entrada no es un número válido.".

print("\n--- Ejercicio 2: Conversión Numérica Segura ---")
# Escribe tu código aquí
entrada_usuario = input("Introduce un número: ")
try:
    numero_convertido = float(entrada_usuario)
    print(f"Número introducido: {numero_convertido}")
except ValueError:
    print("Error: La entrada no es un número válido.")


# --- Ejercicio 3: Acceso Seguro a Lista ---
# Instrucciones:
# 1. Define una lista `mi_lista = [10, 20, 30, 40]`.
# 2. Solicita al usuario que introduzca un índice para acceder a la lista.
# 3. Usa un bloque `try...except` para intentar acceder al elemento en el índice proporcionado (`mi_lista[indice]`).
# 4. Si el acceso es exitoso, imprime "Elemento en el índice [indice]: [valor]".
# 5. Si ocurre un `IndexError` (índice fuera de rango), imprime "Error: Índice fuera de rango.".
# 6. Si ocurre un `ValueError` (porque el usuario no introdujo un número entero para el índice),
#    imprime "Error: Debes introducir un número entero como índice.".

print("\n--- Ejercicio 3: Acceso Seguro a Lista ---")
mi_lista = [10, 20, 30, 40]
print(f"Lista actual: {mi_lista}")
# Escribe tu código aquí
try:
    indice_str = input(f"Introduce un índice (0 a {len(mi_lista)-1}): ")
    indice = int(indice_str) # Intentamos convertir a entero
    valor = mi_lista[indice] # Intentamos acceder al índice
    print(f"Elemento en el índice {indice}: {valor}")
except IndexError:
    print(f"Error: Índice {indice_str} fuera de rango.")
except ValueError:
    print(f"Error: '{indice_str}' no es un número entero válido como índice.")


# --- Ejercicio 4: Uso de `else` y `finally` ---
# Instrucciones:
# 1. Modifica el Ejercicio 1 (`dividir_numeros`) para incluir bloques `else` y `finally`.
# 2. El bloque `else` debe ejecutarse solo si la división fue exitosa, imprimiendo
#    "División realizada con éxito.".
# 3. El bloque `finally` debe ejecutarse siempre, imprimiendo "Fin del intento de división.".
# 4. Llama a la función modificada con valores válidos y con división por cero para observar
#    el comportamiento de `else` y `finally`.

print("\n--- Ejercicio 4: Uso de else y finally ---")
# Escribe tu código aquí
def dividir_numeros_completo(dividendo, divisor):
    """Divide dos números manejando errores y usando else/finally."""
    print(f"\nIntentando dividir {dividendo} / {divisor}...")
    resultado = None # Inicializamos resultado
    try:
        resultado = dividendo / divisor
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except TypeError:
        print("Error: Ambos argumentos deben ser números.")
    else:
        # Se ejecuta solo si no hubo excepciones en el try
        print("División realizada con éxito.")
    finally:
        # Se ejecuta siempre
        print("Fin del intento de división.")
    return resultado # Devolvemos el resultado (o None si hubo error)

# Llamadas a la función modificada
print("Llamada válida:")
dividir_numeros_completo(20, 4)

print("\nLlamada con división por cero:")
dividir_numeros_completo(15, 0)

print("\nLlamada con tipo inválido:")
dividir_numeros_completo(10, "a")


# --- Fin de los ejercicios ---
