# Módulo 8: Context Managers (`with` statement)

Ya hemos visto la declaración `with` en acción cuando trabajamos con archivos:

```python
with open("mi_archivo.txt", "w") as f:
    f.write("Hola")
# El archivo se cierra automáticamente aquí
```

Esta sintaxis es posible gracias al concepto de **Context Managers** (Administradores de Contexto). Son una herramienta poderosa para gestionar **recursos** de manera eficiente y segura, garantizando que las acciones de configuración (`setup`) y limpieza (`teardown`) se ejecuten correctamente, incluso si ocurren errores dentro del bloque `with`.

## ¿Qué Problema Resuelven?

Imagina que necesitas realizar una secuencia de operaciones que involucran un recurso que debe ser liberado al final, como:

*   Abrir y cerrar archivos.
*   Adquirir y liberar bloqueos (locks) en programación concurrente.
*   Abrir y cerrar conexiones de red o bases de datos.
*   Establecer y restaurar temporalmente algún estado o configuración global.

Si no gestionas la limpieza adecuadamente (ej. olvidarte de `f.close()`, no liberar un lock), puedes causar fugas de recursos, corrupción de datos o bloqueos en tu programa. El manejo de errores con `try...finally` puede volverse verboso si tienes que asegurar la limpieza en todos los casos.

```python
# Forma manual (más propensa a errores y verbosa)
f = open("mi_archivo.txt", "w")
try:
    # Hacer algo con el archivo...
    f.write("Contenido")
    # Podría ocurrir un error aquí...
    # x = 1 / 0
finally:
    # ¡Esto DEBE ejecutarse siempre para cerrar el archivo!
    print("Cerrando archivo en finally.")
    f.close()
```

La declaración `with` simplifica enormemente esto.

## El Protocolo de Context Manager

Un objeto puede actuar como un context manager si implementa dos métodos especiales:

*   **`__enter__(self)`:**
    *   Se ejecuta **al entrar** en el bloque `with`.
    *   Realiza la configuración inicial del recurso (ej. abrir el archivo, adquirir el lock).
    *   El valor que **retorna** este método es el que se asigna a la variable después de `as` en la declaración `with` (si se usa `as`). Si no se necesita un objeto específico dentro del bloque `with`, puede retornar `None` o `self`.
*   **`__exit__(self, exc_type, exc_val, exc_tb)`:**
    *   Se ejecuta **al salir** del bloque `with`, ya sea normalmente o debido a una excepción.
    *   Realiza las tareas de limpieza (ej. cerrar el archivo, liberar el lock).
    *   Recibe tres argumentos si ocurrió una excepción dentro del bloque `with`:
        *   `exc_type`: El tipo de la excepción.
        *   `exc_val`: El valor (instancia) de la excepción.
        *   `exc_tb`: El objeto traceback (información de la pila de llamadas).
        *   Si no ocurrió ninguna excepción, estos tres argumentos serán `None`.
    *   **Comportamiento ante excepciones:**
        *   Si `__exit__` devuelve `True`, indica que la excepción ha sido **manejada** y debe ser suprimida (no se propagará fuera del `with`).
        *   Si `__exit__` devuelve `False` (o `None`, que es el valor por defecto si no hay `return`), la excepción **no** ha sido manejada por el context manager y se **propagará** fuera de la declaración `with` después de que `__exit__` termine.

## Creando Context Managers Personalizados

Hay dos formas principales de crear tus propios context managers:

**1. Usando una Clase:** Implementando `__enter__` y `__exit__`.

```python
import time

class TemporizadorSimple:
    def __init__(self, nombre="Bloque"):
        self.nombre = nombre
        print(f"Inicializando Temporizador '{self.nombre}'")

    def __enter__(self):
        """Se ejecuta al entrar al 'with'. Guarda el tiempo inicial."""
        print(f"Entrando al bloque '{self.nombre}'...")
        self.inicio = time.time()
        # Retornamos 'self' si queremos que la instancia esté disponible con 'as'
        # o podríamos retornar otro objeto útil. Aquí retornamos None.
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Se ejecuta al salir del 'with'. Calcula e imprime la duración."""
        fin = time.time()
        duracion = fin - self.inicio
        print(f"Saliendo del bloque '{self.nombre}'. Duración: {duracion:.4f} segundos.")
        # Si hubo una excepción, exc_type, exc_val, exc_tb tendrán valores.
        if exc_type:
            print(f"  Ocurrió una excepción dentro del bloque: {exc_type.__name__}: {exc_val}")
        # Devolvemos False (o nada) para que las excepciones se propaguen si ocurren.
        # Si quisiéramos suprimir la excepción, devolveríamos True.
        return False # Propagar excepciones

# --- Uso del Context Manager de Clase ---
print("\n--- Usando TemporizadorSimple con 'with' ---")
with TemporizadorSimple("Proceso A"):
    print("  Realizando tarea 1...")
    time.sleep(0.5)
    print("  Tarea 1 completada.")

print("\n--- Usando TemporizadorSimple con error ---")
try:
    with TemporizadorSimple("Proceso B con Error"):
        print("  Realizando tarea 2...")
        time.sleep(0.2)
        resultado = 10 / 0 # Provocamos un error
        print("  Esta línea no se ejecuta.")
except ZeroDivisionError:
    print("Excepción ZeroDivisionError capturada fuera del 'with'.")

```

**2. Usando el Decorador `@contextmanager` del Módulo `contextlib`:**

Esta es a menudo una forma más concisa y legible de crear context managers simples, especialmente si se basan en funciones generadoras.

*   Importa `contextmanager` de `contextlib`.
*   Define una **función generadora** que use `yield` **una sola vez**.
*   Decora esa función con `@contextmanager`.
*   El código **antes** del `yield` actúa como el `__enter__`.
*   El valor **cedido** por `yield` es lo que se asigna a la variable con `as`.
*   El código **después** del `yield` actúa como el `__exit__`. La limpieza se coloca típicamente en un bloque `finally` dentro de la función generadora para garantizar su ejecución.

```python
from contextlib import contextmanager

@contextmanager
def temporizador_funcional(nombre="Bloque Funcional"):
    """Context manager creado con @contextmanager."""
    print(f"FUNC: Entrando al bloque '{nombre}'...")
    inicio = time.time()
    try:
        # El código antes del yield es el __enter__
        # El valor cedido es lo que va después de 'as' (aquí None)
        yield
        # El código después del yield (si no hay error)
        print(f"FUNC: Bloque '{nombre}' completado sin errores.")
    except Exception as e:
        # Manejo de excepciones si es necesario dentro del context manager
        print(f"FUNC: Ocurrió una excepción en '{nombre}': {type(e).__name__}")
        # Si no relanzamos la excepción aquí (raise), se suprime.
        # Para propagarla, simplemente no la captures o usa 'raise'.
        raise # Relanzamos la excepción para que se propague fuera del 'with'
    finally:
        # El código en finally SIEMPRE se ejecuta (equivale a __exit__)
        fin = time.time()
        duracion = fin - inicio
        print(f"FUNC: Saliendo del bloque '{nombre}'. Duración: {duracion:.4f} segundos.")

# --- Uso del Context Manager funcional ---
print("\n--- Usando temporizador_funcional con 'with' ---")
with temporizador_funcional("Proceso C"):
    print("  Realizando tarea 3...")
    time.sleep(0.3)

print("\n--- Usando temporizador_funcional con error ---")
try:
    with temporizador_funcional("Proceso D con Error"):
        print("  Realizando tarea 4...")
        x = int("no es numero") # Provocamos un ValueError
except ValueError:
    print("Excepción ValueError capturada fuera del 'with'.")

```

Los Context Managers y la declaración `with` son herramientas idiomáticas de Python para la gestión robusta de recursos, haciendo el código más limpio y seguro al garantizar que las tareas de limpieza se realicen correctamente.
