# Módulo 1: Manejo de Errores Básicos (`try`, `except`)

Cuando ejecutas tu código Python, a veces ocurren errores. Estos pueden ser:

*   **Errores de Sintaxis (`SyntaxError`):** Ocurren cuando escribes código que no sigue las reglas gramaticales de Python (ej. falta de dos puntos, sangría incorrecta, palabra clave mal escrita). Estos errores impiden que el programa se ejecute siquiera. Debes corregirlos antes de poder ejecutar.
*   **Excepciones (Errores en Tiempo de Ejecución):** Ocurren *mientras* el programa se está ejecutando porque sucede algo inesperado (ej. intentar dividir por cero, intentar acceder a un índice de lista que no existe, intentar abrir un archivo que no se encuentra, intentar convertir a número un texto que no es numérico). Si no se manejan, las excepciones detienen abruptamente la ejecución del programa y muestran un mensaje de error (traceback).

El **manejo de excepciones** nos permite "atrapar" estos errores en tiempo de ejecución y ejecutar un código alternativo para manejar la situación, evitando que el programa se detenga por completo.

## La Estructura `try...except`

La forma básica de manejar excepciones en Python es usando un bloque `try...except`.

**Sintaxis:**

```python
try:
    # Bloque de código donde PUEDE ocurrir una excepción
    # Se intenta ejecutar este código normalmente.
    print("Intentando ejecutar código propenso a errores...")
    resultado = 10 / 0 # Esto causará una ZeroDivisionError
    print("Esta línea no se ejecutará si ocurre un error antes.")

except NombreDelErrorEspecifico:
    # Bloque de código que se ejecuta SI Y SOLO SI
    # ocurre la excepción 'NombreDelErrorEspecifico' en el bloque 'try'.
    print("¡Oops! Ocurrió un error específico.")

except OtroErrorEspecifico:
    # Puedes tener múltiples bloques 'except' para diferentes tipos de error.
    print("¡Oops! Ocurrió otro tipo de error.")

except:
    # Un 'except' sin especificar el tipo de error atrapará CUALQUIER excepción.
    # (Generalmente no es la mejor práctica ser tan genérico, es mejor
    # capturar errores específicos que esperas).
    print("¡Oops! Ocurrió algún error inesperado.")

print("El programa continúa después del try-except.")
```

**Flujo de Ejecución:**

1.  Python ejecuta el código dentro del bloque `try`.
2.  **Si no ocurre ninguna excepción** en el bloque `try`, el bloque (o bloques) `except` se omiten por completo, y la ejecución continúa después de toda la estructura `try...except`.
3.  **Si ocurre una excepción** en el bloque `try`:
    *   Python detiene inmediatamente la ejecución del resto del código dentro del `try`.
    *   Busca un bloque `except` que coincida con el tipo de excepción ocurrida.
    *   Si encuentra un `except` que coincide, ejecuta el código dentro de ese bloque `except`. Después de ejecutar el bloque `except`, la ejecución continúa *después* de la estructura `try...except` (el programa no se detiene).
    *   Si no encuentra ningún `except` que coincida (y no hay un `except:` genérico), la excepción no se maneja, y el programa se detiene mostrando el error (traceback), como si no hubiéramos usado `try...except`.

**Ejemplos:**

```python
# Ejemplo 1: División por cero (ZeroDivisionError)
try:
    numerador = 10
    denominador = int(input("Introduce el denominador (intenta 0): "))
    division = numerador / denominador
    print(f"El resultado es: {division}")
except ZeroDivisionError:
    print("Error: No puedes dividir por cero.")
except ValueError:
    print("Error: Debes introducir un número entero.")

print("--- Fin del Ejemplo 1 ---")

# Ejemplo 2: Acceso a índice inválido (IndexError)
mi_lista = [10, 20, 30]
try:
    indice = int(input(f"Introduce un índice (0 a {len(mi_lista)-1}): "))
    print(f"El elemento en el índice {indice} es: {mi_lista[indice]}")
except IndexError:
    print(f"Error: El índice {indice} está fuera de rango.")
except ValueError:
    print("Error: Debes introducir un número entero como índice.")

print("--- Fin del Ejemplo 2 ---")
```

## Capturando la Información del Error

Puedes capturar el objeto de la excepción para obtener más detalles sobre el error usando `as nombre_variable` en el `except`.

```python
try:
    x = int("hola") # Esto causará un ValueError
except ValueError as e: # Capturamos la excepción en la variable 'e'
    print(f"Ocurrió un error de valor: {e}")
    print(f"Tipo de error: {type(e)}")
```
**Salida:**
```
Ocurrió un error de valor: invalid literal for int() with base 10: 'hola'
Tipo de error: <class 'ValueError'>
```

## Bloques `else` y `finally` (Opcionales)

La estructura `try...except` puede extenderse con bloques `else` y `finally`:

*   **`else`:** El bloque `else` se ejecuta **solo si no ocurrió ninguna excepción** en el bloque `try`. Es útil para poner código que debe ejecutarse solo si el `try` fue exitoso.
*   **`finally`:** El bloque `finally` se ejecuta **siempre**, haya ocurrido una excepción o no, e incluso si se usó `return`, `break` o `continue` dentro del `try` o `except`. Se usa típicamente para tareas de "limpieza" que deben realizarse sí o sí (como cerrar un archivo o una conexión de red).

**Sintaxis Completa:**

```python
try:
    # Código propenso a errores
    print("Intentando...")
    # ...
except MiErrorEspecifico as e:
    # Manejar MiErrorEspecifico
    print(f"Manejando error: {e}")
    # ...
else:
    # Código a ejecutar si NO hubo excepciones en el try
    print("El bloque try se completó sin errores.")
    # ...
finally:
    # Código que se ejecuta SIEMPRE (limpieza)
    print("Este bloque finally siempre se ejecuta.")
    # ...
```

**Ejemplo con `else` y `finally`:**

```python
archivo = None # Inicializamos la variable fuera del try
try:
    nombre_archivo = "mi_archivo_inexistente.txt"
    print(f"Intentando abrir '{nombre_archivo}'...")
    archivo = open(nombre_archivo, "r") # Esto dará FileNotFoundError
    contenido = archivo.read()
    print("Archivo leído exitosamente.")
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
except Exception as e: # Captura otros posibles errores
    print(f"Ocurrió un error inesperado: {e}")
else:
    # Esto solo se ejecutaría si el archivo se abre y lee sin problemas
    print("Contenido del archivo:")
    print(contenido)
finally:
    # Esto se ejecuta siempre, para asegurarnos de cerrar el archivo si se abrió
    if archivo: # Verificamos si el archivo se llegó a abrir
        print("Cerrando el archivo (en finally).")
        archivo.close()
    else:
        print("El archivo no se abrió (en finally).")

print("--- Fin del programa ---")
```

El manejo básico de errores con `try` y `except` es crucial para escribir programas robustos que puedan recuperarse de situaciones inesperadas sin detenerse por completo.
