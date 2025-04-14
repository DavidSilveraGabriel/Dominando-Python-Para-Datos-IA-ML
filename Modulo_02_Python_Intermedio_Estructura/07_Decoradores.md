# Módulo 2: Introducción a Decoradores

Los **Decoradores** son una característica poderosa y expresiva de Python, aunque pueden parecer un poco mágicos al principio. En esencia, un decorador es una **función que toma otra función como argumento, le añade alguna funcionalidad extra, y devuelve otra función**, todo esto sin modificar el código fuente de la función original.

Se utilizan ampliamente para:

*   Logging (registrar cuándo se llama a una función, qué argumentos recibe, etc.).
*   Control de acceso y permisos (ej. verificar si un usuario está logueado antes de ejecutar una función).
*   Instrumentación y temporización (ej. medir cuánto tarda en ejecutarse una función).
*   Validación de argumentos.
*   Caching de resultados.
*   Y mucho más...

## Entendiendo las Bases: Funciones como Objetos

Para entender los decoradores, recuerda que en Python, las funciones son **objetos de primera clase**. Esto significa que puedes:

*   Asignar una función a una variable.
*   Pasar una función como argumento a otra función.
*   Devolver una función desde otra función.
*   Definir una función dentro de otra función (funciones anidadas).

```python
def funcion_original():
    print("Ejecutando la función original.")

# 1. Asignar a variable
mi_variable_funcion = funcion_original
mi_variable_funcion() # Llama a funcion_original

# 2. Pasar como argumento
def ejecutar_funcion(func):
    print("Antes de ejecutar la función pasada.")
    func()
    print("Después de ejecutar la función pasada.")

ejecutar_funcion(funcion_original)

# 3. Devolver una función
def crear_saludador(saludo):
    def saludar_interno(nombre):
        print(f"{saludo}, {nombre}!")
    return saludar_interno # Devuelve la función anidada

saludador_hola = crear_saludador("Hola")
saludador_hola("Mundo") # Salida: Hola, Mundo!
```

## Creando un Decorador Simple

Un decorador es, típicamente, una función que define una función "envoltoria" (wrapper) anidada. Esta envoltoria realiza acciones antes y/o después de llamar a la función original que se le pasó.

```python
# Paso 1: El decorador es una función que recibe otra función (func)
def mi_decorador_simple(func):
    # Paso 2: Define la función envoltoria (wrapper)
    # Esta wrapper recibirá los mismos argumentos que la función original
    def wrapper(*args, **kwargs):
        print("--- Algo ANTES de llamar a la función original ---")
        # Paso 3: Llama a la función original pasada como argumento
        resultado = func(*args, **kwargs) # Pasa los argumentos recibidos
        print("--- Algo DESPUÉS de llamar a la función original ---")
        # Paso 4: La wrapper devuelve el resultado de la función original (si lo hay)
        return resultado
    # Paso 5: El decorador devuelve la función envoltoria
    return wrapper

# --- Aplicando el decorador ---

# Forma 1: Sintaxis Clásica (menos común hoy en día)
def decir_hola():
    print("¡Hola!")

# 'Decoramos' la función manualmente
funcion_decorada = mi_decorador_simple(decir_hola)
print("\nLlamando a la función decorada manualmente:")
funcion_decorada() # Ejecuta la wrapper, que a su vez ejecuta decir_hola

# Forma 2: Usando la sintaxis de azúcar '@' (MUCHO más común y legible)
@mi_decorador_simple
def decir_adios(nombre):
    print(f"¡Adiós, {nombre}!")
    return f"Mensaje de despedida para {nombre}"

print("\nLlamando a la función decorada con '@':")
valor_devuelto = decir_adios("Ana") # Llama directamente a decir_adios, pero se ejecuta la wrapper
print(f"Valor devuelto por la función decorada: {valor_devuelto}")

# ¿Qué hace '@mi_decorador_simple' encima de 'def decir_adios(...):'?
# Es exactamente equivalente a hacer esto después de definir decir_adios:
# decir_adios = mi_decorador_simple(decir_adios)
```

**Explicación del `wrapper(*args, **kwargs)`:**

*   `*args`: Permite a la función `wrapper` aceptar cualquier número de argumentos posicionales. Los recoge en una tupla llamada `args`.
*   `**kwargs`: Permite a la función `wrapper` aceptar cualquier número de argumentos de palabra clave. Los recoge en un diccionario llamado `kwargs`.
*   `func(*args, **kwargs)`: Al llamar a la función original `func`, usamos `*args` y `**kwargs` para "desempaquetar" los argumentos recibidos por `wrapper` y pasárselos correctamente a `func`, sin importar cuántos o qué tipo de argumentos eran. Esto hace que el decorador sea genérico y funcione con funciones que tengan diferentes firmas (diferentes parámetros).

## Ejemplo: Decorador de Temporización

```python
import time

def temporizador(func):
    def wrapper(*args, **kwargs):
        inicio = time.time() # Tiempo antes de ejecutar
        resultado = func(*args, **kwargs) # Ejecuta la función original
        fin = time.time() # Tiempo después de ejecutar
        duracion = fin - inicio
        print(f"'{func.__name__}' tardó {duracion:.6f} segundos en ejecutarse.")
        return resultado
    return wrapper

@temporizador
def calculo_largo(n):
    """Simula un cálculo que toma tiempo."""
    suma = 0
    for i in range(n):
        suma += i
    time.sleep(0.5) # Pausa para simular trabajo
    return suma

@temporizador
def saludar_rapido(nombre):
    return f"Hola {nombre}"

print("\n--- Probando decorador temporizador ---")
resultado_calculo = calculo_largo(100000)
# print(f"Resultado del cálculo: {resultado_calculo}") # Descomentar si quieres ver el resultado
saludo = saludar_rapido("Equipo")
print(saludo)
```

**Salida esperada (los tiempos exactos variarán):**

```
--- Probando decorador temporizador ---
'calculo_largo' tardó 0.50xxxx segundos en ejecutarse.
'saludar_rapido' tardó 0.000xxx segundos en ejecutarse.
Hola Equipo
```

Los decoradores son un concepto clave para escribir código Python avanzado, limpio y reutilizable. Permiten añadir funcionalidades transversales (como logging, timing, control de acceso) a tus funciones de una manera elegante y separada de la lógica principal de la función. Aunque la sintaxis `@` oculta parte de la mecánica, entender cómo funcionan por debajo (funciones que envuelven otras funciones) es fundamental.
