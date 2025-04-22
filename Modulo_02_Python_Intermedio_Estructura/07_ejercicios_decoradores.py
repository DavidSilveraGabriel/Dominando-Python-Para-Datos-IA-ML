# Ejercicios: Módulo 2 - Introducción a Decoradores

import functools
import time

# --- Ejercicio 1: Funciones como Objetos ---
# Instrucciones:
# 1. Define una función simple llamada `imprimir_mensaje` que imprima "¡Python es divertido!".
# 2. Asigna `imprimir_mensaje` a una nueva variable `mi_funcion`.
# 3. Llama a la función usando la nueva variable `mi_funcion`.
# 4. Define otra función `ejecutar_otra_funcion` que acepte una función `func` como argumento
#    y simplemente la llame dentro de sí misma.
# 5. Llama a `ejecutar_otra_funcion` pasándole `imprimir_mensaje` como argumento.

print("--- Ejercicio 1: Funciones como Objetos ---")

def imprimir_mensaje():
    """Imprime un mensaje simple."""
    print("¡Python es divertido!")

# Escribe tu código aquí
# 2. Asignar a variable
mi_funcion = imprimir_mensaje
# 3. Llamar usando la variable
print("Llamando a través de la variable asignada:")
mi_funcion()

# 4. Función que recibe otra función
def ejecutar_otra_funcion(func):
    """Ejecuta la función que recibe como argumento."""
    print("Dentro de ejecutar_otra_funcion, llamando a func...")
    func()
    print("...func ejecutada.")

# 5. Pasar función como argumento
print("\nPasando función como argumento:")
ejecutar_otra_funcion(imprimir_mensaje)


# --- Ejercicio 2: Decorador Básico ---
# Instrucciones:
# 1. Crea un decorador llamado `decorador_saludo`.
# 2. Este decorador debe imprimir "--- Inicio Saludo ---" antes de llamar a la función original.
# 3. Debe imprimir "--- Fin Saludo ---" después de llamar a la función original.
# 4. Define una función `saludar()` que imprima "¡Hola!".
# 5. Aplica el `decorador_saludo` a la función `saludar()` usando la sintaxis `@`.
# 6. Llama a la función `saludar()` decorada.

print("\n--- Ejercicio 2: Decorador Básico ---")

# Escribe tu código aquí
# 1. Definir el decorador
def decorador_saludo(func):
    # Usamos functools.wraps para preservar metadatos de la función original
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 2. Imprimir antes
        print("--- Inicio Saludo ---")
        # Llamar a la función original
        resultado = func(*args, **kwargs)
        # 3. Imprimir después
        print("--- Fin Saludo ---")
        return resultado
    return wrapper

# 4. Definir la función original
@decorador_saludo # 5. Aplicar el decorador
def saludar():
    """Imprime un saludo simple."""
    print("¡Hola!")

# 6. Llamar a la función decorada
saludar()


# --- Ejercicio 3: Decorador con Argumentos ---
# Instrucciones:
# 1. Usa el mismo `decorador_saludo` del ejercicio anterior.
# 2. Define una nueva función `saludo_personalizado(nombre)` que imprima f"¡Hola, {nombre}!".
# 3. Aplica el `decorador_saludo` a `saludo_personalizado` usando `@`.
# 4. Llama a `saludo_personalizado` con tu nombre como argumento. Asegúrate de que el
#    decorador funcione correctamente con la función que recibe argumentos.

print("\n--- Ejercicio 3: Decorador con Argumentos ---")

# Escribe tu código aquí
# (Reutilizamos decorador_saludo definido arriba)

@decorador_saludo # 3. Aplicar decorador
def saludo_personalizado(nombre):
    """Imprime un saludo personalizado."""
    print(f"¡Hola, {nombre}!")

# 4. Llamar a la función decorada con argumento
saludo_personalizado("Mundo")


# --- Ejercicio 4: Decorador de Registro (Logging Simple) ---
# Instrucciones:
# 1. Crea un decorador llamado `registrar_llamada`.
# 2. La función `wrapper` dentro del decorador debe:
#    a. Imprimir un mensaje indicando que la función está a punto de ser llamada,
#       incluyendo el nombre de la función (`func.__name__`).
#    b. Imprimir los argumentos posicionales (`args`) y de palabra clave (`kwargs`)
#       con los que se llamó a la función.
#    c. Llamar a la función original `func(*args, **kwargs)` y guardar el resultado.
#    d. Imprimir un mensaje indicando que la función ha terminado, incluyendo el nombre
#       y el valor devuelto.
#    e. Devolver el resultado de la función original.
# 3. Define una función `sumar_numeros(a, b, c=0)` que devuelva la suma de a, b y c.
# 4. Aplica el decorador `registrar_llamada` a `sumar_numeros`.
# 5. Llama a `sumar_numeros(10, 5)` y observa la salida del registro.
# 6. Llama a `sumar_numeros(1, 2, c=3)` y observa la salida del registro.

print("\n--- Ejercicio 4: Decorador de Registro ---")

# Escribe tu código aquí
# 1. Definir el decorador
def registrar_llamada(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 2a. Imprimir antes (nombre)
        print(f"Llamando a '{func.__name__}'...")
        # 2b. Imprimir argumentos
        print(f"  args: {args}")
        print(f"  kwargs: {kwargs}")
        # 2c. Llamar y guardar resultado
        resultado = func(*args, **kwargs)
        # 2d. Imprimir después (nombre y resultado)
        print(f"'{func.__name__}' terminó. Devolvió: {resultado}")
        # 2e. Devolver resultado
        return resultado
    return wrapper

# 3. Definir función original
@registrar_llamada # 4. Aplicar decorador
def sumar_numeros(a, b, c=0):
    """Suma tres números (c es opcional)."""
    return a + b + c

# 5. Llamar con argumentos posicionales
print("Primera llamada a sumar_numeros:")
suma1 = sumar_numeros(10, 5)
# print(f"Resultado suma1: {suma1}") # El decorador ya imprime el resultado

# 6. Llamar con argumentos posicionales y de palabra clave
print("\nSegunda llamada a sumar_numeros:")
suma2 = sumar_numeros(1, 2, c=3)
# print(f"Resultado suma2: {suma2}")


# --- Ejercicio 5: Decorador de Temporización (Revisión) ---
# Instrucciones:
# 1. Revisa el decorador `temporizador` del ejemplo de la lección.
# 2. Define una función `proceso_simulado(duracion)` que simplemente use `time.sleep(duracion)`.
# 3. Aplica el decorador `temporizador` a `proceso_simulado`.
# 4. Llama a `proceso_simulado(1.2)` y observa la salida del temporizador.

print("\n--- Ejercicio 5: Decorador de Temporización ---")

def temporizador(func):
    """Decorador que mide el tiempo de ejecución de una función."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        duracion = fin - inicio
        print(f"'{func.__name__}' tardó {duracion:.4f} segundos.")
        return resultado
    return wrapper

# Escribe tu código aquí
# 2. Definir función original
@temporizador # 3. Aplicar decorador
def proceso_simulado(duracion):
    """Simula un proceso que tarda un tiempo específico."""
    print(f"  (Iniciando proceso simulado de {duracion}s...)")
    time.sleep(duracion)
    print("  (...Proceso simulado terminado)")

# 4. Llamar a la función decorada
proceso_simulado(1.2)
proceso_simulado(0.5)


# --- Fin de los ejercicios ---
