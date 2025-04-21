# Ejercicios: Módulo 1 - Control de Flujo - Condicionales (`if`, `elif`, `else`)

# --- Ejercicio 1: Mayoría de Edad ---
# Instrucciones: Escribe un programa que solicite al usuario su edad (usando input())
# y determine si es mayor de edad (18 años o más). Imprime un mensaje apropiado.
# Recuerda convertir la entrada del usuario a entero usando int().

print("--- Ejercicio 1: Mayoría de Edad ---")
# Escribe tu código aquí
try:
    edad_usuario = int(input("Introduce tu edad: "))

    if edad_usuario >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")
except ValueError:
    print("Error: Debes introducir un número entero válido para la edad.")


# --- Ejercicio 2: Calificación con Letras ---
# Instrucciones: Escribe un programa que solicite una puntuación numérica (0-100).
# Basado en la puntuación, asigna una calificación con letra:
# - 90 a 100: "A"
# - 80 a 89:  "B"
# - 70 a 79:  "C"
# - 60 a 69:  "D"
# - Menos de 60: "F"
# Imprime la calificación correspondiente. Maneja el caso de que la entrada no sea un número.

print("\n--- Ejercicio 2: Calificación con Letras ---")
# Escribe tu código aquí
try:
    puntuacion = float(input("Introduce tu puntuación (0-100): ")) # Usamos float para permitir decimales

    if puntuacion < 0 or puntuacion > 100:
        print("Error: La puntuación debe estar entre 0 y 100.")
    elif puntuacion >= 90:
        calificacion = "A"
        print(f"Tu calificación es: {calificacion}")
    elif puntuacion >= 80:
        calificacion = "B"
        print(f"Tu calificación es: {calificacion}")
    elif puntuacion >= 70:
        calificacion = "C"
        print(f"Tu calificación es: {calificacion}")
    elif puntuacion >= 60:
        calificacion = "D"
        print(f"Tu calificación es: {calificacion}")
    else: # Menos de 60
        calificacion = "F"
        print(f"Tu calificación es: {calificacion}")

except ValueError:
    print("Error: Debes introducir un valor numérico para la puntuación.")


# --- Ejercicio 3: Número Par o Impar ---
# Instrucciones: Escribe un programa que solicite un número entero al usuario
# y determine si es par o impar. Imprime el resultado.
# Pista: Usa el operador módulo (%).

print("\n--- Ejercicio 3: Número Par o Impar ---")
# Escribe tu código aquí
try:
    numero = int(input("Introduce un número entero: "))

    if numero % 2 == 0:
        print(f"El número {numero} es PAR.")
    else:
        print(f"El número {numero} es IMPAR.")
except ValueError:
    print("Error: Debes introducir un número entero válido.")


# --- Ejercicio 4: Cajero Automático Simple ---
# Instrucciones: Simula un cajero automático simple.
# 1. Define una variable `saldo_cuenta` con un valor inicial (ej. 1000).
# 2. Solicita al usuario la cantidad que desea retirar.
# 3. Verifica si la cantidad a retirar es positiva.
# 4. Verifica si hay saldo suficiente en la cuenta.
# 5. Si ambas condiciones son verdaderas, resta la cantidad del saldo e imprime
#    "Retiro exitoso. Saldo restante: [nuevo saldo]".
# 6. Si la cantidad no es positiva, imprime "Error: La cantidad debe ser positiva."
# 7. Si no hay saldo suficiente (y la cantidad es positiva), imprime
#    "Error: Saldo insuficiente."
# Maneja posibles errores si la entrada no es un número.

print("\n--- Ejercicio 4: Cajero Automático Simple ---")
saldo_cuenta = 1000.00
print(f"Saldo actual: ${saldo_cuenta:.2f}")

# Escribe tu código aquí
try:
    cantidad_retirar = float(input("Introduce la cantidad a retirar: "))

    if cantidad_retirar <= 0:
        print("Error: La cantidad a retirar debe ser positiva.")
    elif cantidad_retirar > saldo_cuenta:
        print(f"Error: Saldo insuficiente. Solo tienes ${saldo_cuenta:.2f} disponibles.")
    else: # Cantidad positiva y saldo suficiente
        saldo_cuenta -= cantidad_retirar
        print(f"Retiro exitoso de ${cantidad_retirar:.2f}.")
        print(f"Saldo restante: ${saldo_cuenta:.2f}")

except ValueError:
    print("Error: Debes introducir un valor numérico para la cantidad a retirar.")


# --- Fin de los ejercicios ---
