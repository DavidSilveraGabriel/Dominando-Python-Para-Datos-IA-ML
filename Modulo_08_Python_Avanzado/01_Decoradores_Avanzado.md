# Módulo 8: Decoradores (Uso Avanzado)

Ya vimos la idea básica de los decoradores en el Módulo 2: funciones que envuelven a otras funciones para añadir funcionalidad. Ahora exploraremos algunos patrones más avanzados.

## 1. Decoradores con Argumentos

A veces queremos que nuestro decorador sea configurable. Podemos lograr esto haciendo que la función decoradora *acepte argumentos* y *devuelva* el decorador real (que a su vez recibe la función a decorar). Esto implica una capa extra de anidamiento.

**Estructura:**

```python
def decorador_con_argumentos(arg_decorador1, arg_decorador2):
    print(f"Inicializando decorador con argumentos: {arg_decorador1}, {arg_decorador2}")
    # 1. La función externa recibe los argumentos del decorador

    def decorador_real(func):
        # 2. Esta función interna es el decorador real, recibe la función 'func'
        print(f"Aplicando decorador real a '{func.__name__}'")

        def wrapper(*args, **kwargs):
            # 3. La wrapper es la que finalmente se ejecuta en lugar de 'func'
            print(f"Wrapper ejecutándose con argumentos del decorador: {arg_decorador1}, {arg_decorador2}")
            print("Wrapper: Antes de llamar a la función original.")
            resultado = func(*args, **kwargs) # Llama a la función original
            print("Wrapper: Después de llamar a la función original.")
            return resultado
        # 4. El decorador real devuelve la wrapper
        return wrapper
    # 5. La función externa devuelve el decorador real
    return decorador_real

# --- Uso ---
@decorador_con_argumentos("Valor1", arg_decorador2=99)
def mi_funcion_objetivo(x, y):
    print(f"Ejecutando mi_funcion_objetivo con {x}, {y}")
    return x + y

print("\n--- Llamando a la función decorada con argumentos ---")
resultado = mi_funcion_objetivo(10, 20)
print(f"Resultado final: {resultado}")

# ¿Qué pasa con @decorador_con_argumentos(...)?
# 1. Se llama a decorador_con_argumentos("Valor1", arg_decorador2=99).
# 2. Esta llamada devuelve la función 'decorador_real'.
# 3. Python aplica entonces 'decorador_real' a 'mi_funcion_objetivo', como si fuera:
#    mi_funcion_objetivo = decorador_real(mi_funcion_objetivo)
# 4. 'decorador_real' devuelve 'wrapper'.
# 5. Ahora, 'mi_funcion_objetivo' en realidad apunta a 'wrapper'.
# 6. Cuando llamas a mi_funcion_objetivo(10, 20), estás ejecutando 'wrapper(10, 20)'.
# 7. La 'wrapper' tiene acceso a 'arg_decorador1' y 'arg_decorador2' debido al closure.
```

**Ejemplo Práctico: Decorador de Repetición**

```python
import functools # Necesario para functools.wraps

def repetir(num_veces):
    """Decorador que repite la ejecución de una función `num_veces`."""
    def decorador_repetir(func):
        @functools.wraps(func) # Preserva metadatos de la función original (nombre, docstring)
        def wrapper(*args, **kwargs):
            print(f"Repitiendo '{func.__name__}' {num_veces} veces:")
            valor_retorno = None
            for i in range(num_veces):
                print(f"  Ejecución {i+1}: ", end="")
                valor_retorno = func(*args, **kwargs)
            return valor_retorno # Devuelve el resultado de la última ejecución
        return wrapper
    return decorador_repetir

@repetir(3)
def saludar(nombre):
    """Saluda a alguien."""
    print(f"Hola {nombre}!")

print("\n--- Probando decorador @repetir(3) ---")
saludar("Mundo")

# Preservación de Metadatos con `functools.wraps`
# Sin @functools.wraps(func) en la wrapper:
# print(saludar.__name__) # Imprimiría 'wrapper'
# print(saludar.__doc__)  # Imprimiría None
# Con @functools.wraps(func):
print(f"\nNombre de la función decorada: {saludar.__name__}") # Imprime 'saludar'
print(f"Docstring de la función decorada: {saludar.__doc__}") # Imprime 'Saluda a alguien.'
```
Usar `@functools.wraps(func)` dentro de la `wrapper` es una **buena práctica** porque copia atributos importantes (como `__name__`, `__doc__`) de la función original a la función `wrapper`, lo que ayuda con la introspección y la depuración.

## 2. Decoradores de Clases

También puedes usar una **clase** para implementar un decorador. Esto es útil si el decorador necesita mantener un estado interno o si la lógica es más compleja.

Para que una clase funcione como decorador, necesita:

*   Un método `__init__` que reciba la función a decorar (`func`).
*   Un método `__call__` que implemente la lógica de la `wrapper` (se ejecuta cuando se llama a la instancia decorada).

```python
import time

class TemporizadorClase:
    def __init__(self, func):
        functools.update_wrapper(self, func) # Copia metadatos
        self.func = func
        self.num_llamadas = 0 # Estado interno

    def __call__(self, *args, **kwargs):
        self.num_llamadas += 1
        print(f"--- Llamada #{self.num_llamadas} a '{self.func.__name__}' ---")
        inicio = time.time()
        resultado = self.func(*args, **kwargs) # Llama a la función original almacenada
        fin = time.time()
        print(f"'{self.func.__name__}' tardó {fin - inicio:.6f} segundos.")
        return resultado

@TemporizadorClase # Usamos la clase como decorador
def procesar_datos(n):
    """Simula procesamiento."""
    print(f"Procesando {n} elementos...")
    time.sleep(0.2)
    print("Procesamiento terminado.")

print("\n--- Probando decorador de clase ---")
procesar_datos(100)
procesar_datos(200)

# El decorador (que es una instancia de TemporizadorClase) mantiene el estado
# print(f"Número total de llamadas: {procesar_datos.num_llamadas}") # Accederíamos al estado si fuera necesario
```

## 3. Apilamiento de Decoradores

Puedes aplicar múltiples decoradores a una sola función. Se aplican de **abajo hacia arriba** (el más cercano a la función se aplica primero).

```python
def decorador_uno(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(">> Entrando Decorador Uno")
        res = func(*args, **kwargs)
        print("<< Saliendo Decorador Uno")
        return res
    return wrapper

def decorador_dos(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(">>>> Entrando Decorador Dos")
        res = func(*args, **kwargs)
        print("<<<< Saliendo Decorador Dos")
        return res
    return wrapper

@decorador_uno # Se aplica SEGUNDO
@decorador_dos # Se aplica PRIMERO
def mi_funcion_apilada():
    print("    Ejecutando función apilada")

print("\n--- Probando decoradores apilados ---")
mi_funcion_apilada()

# Salida esperada:
# >>>> Entrando Decorador Dos  (Se aplica primero, envuelve a la función original)
# >> Entrando Decorador Uno   (Se aplica segundo, envuelve al resultado del decorador dos)
#     Ejecutando función apilada
# << Saliendo Decorador Uno
# <<<< Saliendo Decorador Dos
```

Los decoradores son una herramienta versátil en Python. Entender cómo pasar argumentos y cómo usar clases como decoradores amplía significativamente las posibilidades para añadir funcionalidades reusables y mantener tu código limpio.
