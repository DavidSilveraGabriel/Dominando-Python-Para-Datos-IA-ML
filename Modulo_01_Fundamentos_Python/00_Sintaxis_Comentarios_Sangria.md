# Módulo 1: Sintaxis Básica, Comentarios y Sangría

¡Bienvenido/a al Módulo 1! Aquí empezamos a escribir código Python real. Cubriremos los elementos más fundamentales de la sintaxis del lenguaje.

## Ejecutando Código Python

Hay varias formas de ejecutar código Python:

1.  **Modo Interactivo (REPL):**
    *   Abre tu terminal (o Anaconda Prompt).
    *   Escribe `python` y presiona Enter.
    *   Verás un prompt como `>>>`. Aquí puedes escribir código Python línea por línea y ver el resultado inmediatamente.
    *   Es útil para pruebas rápidas y experimentar.
    *   Para salir, escribe `exit()` o presiona `Ctrl+Z` (Windows) / `Ctrl+D` (macOS/Linux) y Enter.

    ```python
    >>> print("¡Hola, Python interactivo!")
    ¡Hola, Python interactivo!
    >>> 2 + 3
    5
    >>> exit()
    ```

2.  **Scripts (`.py`):**
    *   Escribe tu código en un archivo de texto con la extensión `.py` (ej. `mi_script.py`) usando un editor como VS Code.
    *   Guarda el archivo.
    *   Abre tu terminal, navega hasta el directorio donde guardaste el archivo usando `cd`.
    *   Ejecuta el script escribiendo: `python mi_script.py`

    ```python
    # Contenido de mi_script.py
    mensaje = "¡Hola desde un script!"
    print(mensaje)
    numero = 10 + 5
    print(f"El resultado es: {numero}")
    ```
    *   En la terminal: `python mi_script.py`

3.  **Jupyter Notebooks/Lab:**
    *   Como vimos en el Módulo 0, puedes escribir y ejecutar código en celdas dentro de un entorno interactivo basado en web. Ideal para análisis de datos.

## La Función `print()`

La función `print()` es una de las más usadas. Sirve para mostrar mensajes o los valores de las variables en la consola o en la salida de la celda de Jupyter.

```python
print("Este es un mensaje.")
nombre = "Ana"
edad = 30
print("Nombre:", nombre, "Edad:", edad)
print(f"Forma moderna (f-string): Mi nombre es {nombre} y tengo {edad} años.") # f-strings son muy útiles!
```

## Comentarios

Los comentarios son líneas en tu código que Python ignora al ejecutarse. Sirven para explicar qué hace el código, dejar notas o deshabilitar temporalmente alguna línea.

*   **Comentario de una línea:** Empieza con el símbolo `#`. Todo lo que sigue en esa línea es un comentario.
*   **Comentario multilínea (Docstring - uso específico):** Se usan tres comillas dobles `"""` o simples `'''` al inicio y al final. Aunque técnicamente son strings, se usan comúnmente al inicio de funciones, clases o módulos para documentar su propósito (lo veremos más adelante).

```python
# Esto es un comentario de una sola línea. Explica la siguiente línea.
velocidad = 90 # km/h - También puedes poner comentarios al final de una línea de código.

# print("Esta línea no se ejecutará porque está comentada")

"""
Esto es un string multilínea,
a menudo usado como 'docstring' para documentar.
Python no lo ejecuta como código, pero no es un comentario
en el mismo sentido que #. Lo veremos en funciones.
"""
```

## Sangría (Indentation) - ¡CRÍTICO EN PYTHON!

A diferencia de muchos otros lenguajes que usan llaves `{}` o palabras clave como `begin`/`end` para definir bloques de código (como el cuerpo de un `if`, un bucle `for` o una función), **Python usa la sangría**.

*   **¿Qué es?** Son los espacios en blanco al inicio de una línea.
*   **¿Por qué es importante?** ¡Define la estructura del programa! Las líneas de código que pertenecen al mismo bloque *deben* tener el mismo nivel de sangría.
*   **Estándar:** La convención (definida en PEP 8) es usar **4 espacios** por cada nivel de sangría. **No mezcles tabulaciones y espacios.** Configura tu editor (VS Code) para que inserte 4 espacios cuando presiones la tecla `Tab`.
*   **Errores:** Una sangría incorrecta (`IndentationError`) es uno de los errores más comunes al empezar con Python.

```python
# Ejemplo CORRECTO
puntaje = 75

if puntaje > 50:
    print("¡Aprobado!") # Este print pertenece al bloque del if (tiene 4 espacios de sangría)
    print("Felicidades.") # Esta línea también pertenece al if
print("Fin de la evaluación.") # Esta línea está fuera del if (sin sangría)

# Ejemplo INCORRECTO (causará IndentationError)
# if puntaje > 50:
# print("Error de sangría") # Falta la sangría

# Ejemplo INCORRECTO (causará IndentationError)
# if puntaje > 50:
#     print("Nivel 1")
#        print("Nivel 2 incorrecto") # Sangría inconsistente
```

**¡La sangría es obligatoria y fundamental en Python!** Acostúmbrate a ser consistente con ella desde el principio.

Con estos conceptos básicos de sintaxis, comentarios y la crucial sangría, estás listo/a para aprender sobre variables y tipos de datos.
