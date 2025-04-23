# Ejercicios: Módulo 8 - Decoradores Avanzados

import functools
import time

print("--- Decoradores Avanzados ---")

# --- Ejercicio 1: Decorador con Argumentos ---
# Instrucciones:
# 1. Crea un decorador llamado `repetir(n)` que tome un argumento entero `n`.
# 2. El decorador debe hacer que la función decorada se ejecute `n` veces.
# 3. Define una función simple `saludar(nombre)` que imprima un saludo.
# 4. Decora `saludar` con `@repetir(3)` para que el saludo se imprima 3 veces.
# 5. Llama a la función decorada `saludar("Mundo")`.

print("--- Ejercicio 1: Decorador con Argumentos ---")

# 1, 2. Definir decorador con argumentos
def repetir(n):
    """Decorador que repite la ejecución de una función n veces."""
    def decorador_real(funcion_original):
        @functools.wraps(funcion_original) # Preservar metadatos
        def wrapper(*args, **kwargs):
            print(f"--- Ejecutando {funcion_original.__name__} {n} veces ---")
            resultado_final = None # Para guardar el resultado de la última ejecución
            for i in range(n):
                print(f"Ejecución {i+1}/{n}:")
                resultado_final = funcion_original(*args, **kwargs)
            print("--- Fin repeticiones ---")
            return resultado_final # Devolver el resultado de la última llamada
        return wrapper
    return decorador_real

# 3. Definir función simple
def saludar(nombre):
    """Imprime un saludo."""
    print(f"¡Hola, {nombre}!")

# 4. Decorar la función
@repetir(3)
def saludar_repetido(nombre):
    """Imprime un saludo (decorada para repetir)."""
    print(f"¡Hola, {nombre}!")

# 5. Llamar a la función decorada
print("\nLlamando a la función decorada saludar_repetido('Mundo'):")
saludar_repetido("Mundo")

# Verificar metadatos (opcional)
print(f"\nNombre de la función decorada: {saludar_repetido.__name__}")
print(f"Docstring: {saludar_repetido.__doc__}")

print("-" * 20)


# --- Ejercicio 2: Preservando Metadatos con `functools.wraps` ---
# Instrucciones:
# 1. Crea un decorador simple `imprimir_args` que imprima los argumentos
#    posicionales y de palabra clave con los que se llama a la función decorada,
#    antes de ejecutarla.
# 2. Define una función `sumar(a, b, c=0)` que sume sus argumentos. Incluye un docstring.
# 3. Decora `sumar` con `@imprimir_args`.
# 4. Imprime el nombre (`__name__`) y el docstring (`__doc__`) de la función `sumar` *antes* de aplicar `functools.wraps` al decorador (puedes comentar `@functools.wraps` temporalmente). ¿Qué observas?
# 5. Ahora, añade `@functools.wraps(funcion_original)` dentro de tu decorador `imprimir_args` (en la función `wrapper`).
# 6. Vuelve a imprimir el nombre y docstring de la función `sumar` decorada. ¿Qué observas ahora?
# 7. Llama a `sumar(1, 2, c=5)`.

print("\n--- Ejercicio 2: Preservando Metadatos (`functools.wraps`) ---")

# 1. Definir decorador (inicialmente sin wraps)
def imprimir_args_sin_wraps(funcion_original):
    # @functools.wraps(funcion_original) # Comentado inicialmente
    def wrapper(*args, **kwargs):
        print(f"Llamando a '{funcion_original.__name__}' con:")
        if args:
            print(f"  args: {args}")
        if kwargs:
            print(f"  kwargs: {kwargs}")
        resultado = funcion_original(*args, **kwargs)
        print(f"'{funcion_original.__name__}' devolvió: {resultado}")
        return resultado
    return wrapper

# 2. Definir función a decorar
def sumar_sin_wraps(a, b, c=0):
    """Suma tres números (c es opcional)."""
    return a + b + c

# 3. Decorar
@imprimir_args_sin_wraps
def sumar_decorada_sin_wraps(a, b, c=0):
    """Suma tres números (c es opcional)."""
    return a + b + c

# 4. Imprimir metadatos ANTES de wraps
print("\nMetadatos SIN @functools.wraps:")
print(f"Nombre: {sumar_decorada_sin_wraps.__name__}") # Imprime 'wrapper'
print(f"Docstring: {sumar_decorada_sin_wraps.__doc__}") # Imprime None o el docstring de wrapper si tuviera
print("Observación: Los metadatos originales de 'sumar' se pierden.")

# --- Ahora con wraps ---

def imprimir_args_con_wraps(funcion_original):
    @functools.wraps(funcion_original) # <--- Añadido
    def wrapper(*args, **kwargs):
        print(f"Llamando a '{funcion_original.__name__}' con:")
        if args:
            print(f"  args: {args}")
        if kwargs:
            print(f"  kwargs: {kwargs}")
        resultado = funcion_original(*args, **kwargs)
        print(f"'{funcion_original.__name__}' devolvió: {resultado}")
        return resultado
    return wrapper

@imprimir_args_con_wraps
def sumar_decorada_con_wraps(a, b, c=0):
    """Suma tres números (c es opcional)."""
    return a + b + c

# 6. Imprimir metadatos DESPUÉS de wraps
print("\nMetadatos CON @functools.wraps:")
print(f"Nombre: {sumar_decorada_con_wraps.__name__}") # Imprime 'sumar_decorada_con_wraps'
print(f"Docstring: {sumar_decorada_con_wraps.__doc__}") # Imprime el docstring original
print("Observación: Los metadatos originales se preservan.")

# 7. Llamar a la función
print("\nLlamando a la función decorada (con wraps):")
resultado_suma = sumar_decorada_con_wraps(1, 2, c=5)
print(f"Resultado final: {resultado_suma}")

print("-" * 20)


# --- Ejercicio 3: Decorador de Clase (Conceptual) ---
# Instrucciones:
# 1. Define una clase `ContadorLlamadas` que actúe como un decorador.
# 2. El constructor (`__init__`) debe aceptar la función original y almacenar una variable `_num_llamadas` inicializada a 0.
# 3. Implementa el método `__call__` para que:
#    a. Incremente `_num_llamadas`.
#    b. Imprima cuántas veces se ha llamado a la función hasta ahora.
#    c. Llame y devuelva el resultado de la función original.
# 4. Define una función `potencia(base, exp)` que calcule `base ** exp`.
# 5. Decora `potencia` con `@ContadorLlamadas`.
# 6. Llama a la función `potencia` decorada varias veces (ej. `potencia(2, 3)`, `potencia(10, 2)`).

print("\n--- Ejercicio 3: Decorador de Clase ---")

# 1, 2, 3. Definir clase decoradora
class ContadorLlamadas:
    def __init__(self, funcion_original):
        functools.update_wrapper(self, funcion_original) # Preservar metadatos también en clases
        self._funcion = funcion_original
        self._num_llamadas = 0
        print(f"Decorador ContadorLlamadas inicializado para '{self._funcion.__name__}'")

    def __call__(self, *args, **kwargs):
        self._num_llamadas += 1
        print(f"Llamada número {self._num_llamadas} a '{self._funcion.__name__}'")
        return self._funcion(*args, **kwargs)

# 4. Definir función a decorar
def potencia_original(base, exp):
    """Calcula la potencia de una base."""
    return base ** exp

# 5. Decorar con la clase
@ContadorLlamadas
def potencia(base, exp):
    """Calcula la potencia de una base."""
    return base ** exp

# 6. Llamar varias veces
print("\nLlamando a la función decorada 'potencia':")
res1 = potencia(2, 3)
print(f"Resultado 1: {res1}")
res2 = potencia(10, 2)
print(f"Resultado 2: {res2}")
res3 = potencia(5, 0)
print(f"Resultado 3: {res3}")

# Verificar metadatos (opcional)
print(f"\nNombre de la función decorada: {potencia.__name__}")
print(f"Docstring: {potencia.__doc__}")

print("-" * 20)

# --- Fin de los ejercicios ---
