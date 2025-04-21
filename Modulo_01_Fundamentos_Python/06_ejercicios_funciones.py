# Ejercicios: Módulo 1 - Funciones

# --- Ejercicio 1: Definición y Llamada Simple ---
# Instrucciones:
# 1. Define una función llamada `mostrar_mensaje` que no reciba parámetros e imprima
#    "¡Aprendiendo funciones en Python!".
# 2. Llama a la función `mostrar_mensaje` dos veces.

print("--- Ejercicio 1: Definición y Llamada Simple ---")
# Escribe tu código aquí
def mostrar_mensaje():
    """Imprime un mensaje fijo sobre el aprendizaje de funciones."""
    print("¡Aprendiendo funciones en Python!")

# Llamadas a la función
mostrar_mensaje()
mostrar_mensaje()


# --- Ejercicio 2: Función con Parámetros ---
# Instrucciones:
# 1. Define una función llamada `saludar_usuario` que reciba un parámetro `nombre`.
# 2. Dentro de la función, imprime un saludo personalizado como "¡Hola, [nombre]!".
# 3. Llama a la función `saludar_usuario` pasándole tu nombre como argumento.
# 4. Llama a la función `saludar_usuario` pasándole otro nombre diferente.

print("\n--- Ejercicio 2: Función con Parámetros ---")
# Escribe tu código aquí
def saludar_usuario(nombre):
    """Imprime un saludo personalizado para el nombre dado."""
    print(f"¡Hola, {nombre}!")

# Llamadas a la función con argumentos
saludar_usuario("Carlos")
saludar_usuario("Maria")


# --- Ejercicio 3: Función con Retorno ---
# Instrucciones:
# 1. Define una función llamada `calcular_area_rectangulo` que reciba dos parámetros:
#    `base` y `altura`.
# 2. La función debe calcular el área (base * altura) y devolver el resultado usando `return`.
# 3. Llama a la función con una base de 5 y una altura de 3. Almacena el resultado en una variable.
# 4. Imprime la variable que contiene el resultado.
# 5. Llama a la función con otros valores (ej. base=10, altura=4) e imprime directamente
#    el valor devuelto por la función.

print("\n--- Ejercicio 3: Función con Retorno ---")
# Escribe tu código aquí
def calcular_area_rectangulo(base, altura):
    """Calcula y devuelve el área de un rectángulo."""
    area = base * altura
    return area

# Llamada 1 y almacenamiento del resultado
area_calculada = calcular_area_rectangulo(5, 3)
print(f"El área del rectángulo (5x3) es: {area_calculada}")

# Llamada 2 e impresión directa
print(f"El área del rectángulo (10x4) es: {calcular_area_rectangulo(10, 4)}")


# --- Ejercicio 4: Parámetros con Valores por Defecto ---
# Instrucciones:
# 1. Define una función llamada `potencia` que reciba dos parámetros: `base` y `exponente`.
# 2. Asigna un valor por defecto de 2 al parámetro `exponente`.
# 3. La función debe calcular `base` elevado a `exponente` y devolver el resultado.
# 4. Llama a la función `potencia` solo con el argumento `base` (ej. `potencia(4)`). Imprime el resultado.
# 5. Llama a la función `potencia` proporcionando ambos argumentos (ej. `potencia(3, 3)`). Imprime el resultado.
# 6. Llama a la función usando argumentos de palabra clave para `base` y `exponente` en orden inverso
#    (ej. `potencia(exponente=4, base=2)`). Imprime el resultado.

print("\n--- Ejercicio 4: Parámetros con Valores por Defecto ---")
# Escribe tu código aquí
def potencia(base, exponente=2):
    """Calcula la potencia de una base elevada a un exponente (por defecto 2)."""
    resultado = base ** exponente
    return resultado

# Llamada con valor por defecto para exponente
print(f"Potencia de 4 (exponente por defecto): {potencia(4)}") # 4**2 = 16

# Llamada proporcionando ambos argumentos
print(f"Potencia de 3 elevado a 3: {potencia(3, 3)}") # 3**3 = 27

# Llamada con argumentos de palabra clave en orden inverso
print(f"Potencia de 2 elevado a 4 (keyword args): {potencia(exponente=4, base=2)}") # 2**4 = 16


# --- Ejercicio 5: Alcance de Variables (Scope) ---
# Instrucciones:
# 1. Define una variable global `mensaje_global = "Soy global"`.
# 2. Define una función `probar_scope` que haga lo siguiente:
#    a. Defina una variable local `mensaje_local = "Soy local"`.
#    b. Imprima el valor de `mensaje_local` dentro de la función.
#    c. Imprima el valor de `mensaje_global` dentro de la función.
# 3. Llama a la función `probar_scope`.
# 4. Intenta imprimir `mensaje_local` fuera de la función (esto dará un error, coméntalo).
# 5. Imprime `mensaje_global` fuera de la función.

print("\n--- Ejercicio 5: Alcance de Variables (Scope) ---")
# Variable global
mensaje_global = "Soy global"

# Escribe tu código aquí
def probar_scope():
    """Demuestra el alcance local y global de las variables."""
    mensaje_local = "Soy local"
    print(f"Dentro de la función - Local: {mensaje_local}")
    print(f"Dentro de la función - Global: {mensaje_global}")

# Llamada a la función
probar_scope()

# Intento de acceder a variable local fuera de su scope (comentado para evitar error)
# print(f"Fuera de la función - Local: {mensaje_local}") # NameError: name 'mensaje_local' is not defined

# Acceso a variable global fuera de la función
print(f"Fuera de la función - Global: {mensaje_global}")


# --- Fin de los ejercicios ---
