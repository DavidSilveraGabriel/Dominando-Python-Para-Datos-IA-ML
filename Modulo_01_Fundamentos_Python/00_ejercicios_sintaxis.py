# Ejercicios: Módulo 1 - Sintaxis Básica, Comentarios y Sangría

# --- Ejercicio 1: La Función print() ---
# Utiliza la función print() para mostrar los siguientes mensajes en la consola:
# 1. Tu nombre completo.
# 2. El nombre de tu ciudad o país.
# 3. Tu comida o bebida favorita.
# Asegúrate de que cada mensaje aparezca en una línea separada.

print("--- Ejercicio 1 ---")
# Escribe tu código aquí
print("Nombre Completo Ejemplo")
print("Ciudad Ejemplo")
print("Comida Favorita Ejemplo")


# --- Ejercicio 2: Comentarios ---
# Añade comentarios a las siguientes líneas de código para explicar qué hacen:

print("\n--- Ejercicio 2 ---")

# Calcula el área de un rectángulo
largo = 10
ancho = 5
area = largo * ancho
# Imprime el resultado del cálculo del área
print(f"El área del rectángulo es: {area}")

# Convierte grados Celsius a Fahrenheit
grados_celsius = 25
grados_fahrenheit = (grados_celsius * 9/5) + 32
# Muestra la temperatura convertida
print(f"{grados_celsius}°C equivalen a {grados_fahrenheit}°F")


# --- Ejercicio 3: Sangría (Indentation) ---
# El siguiente código tiene errores de sangría. Corrígelo para que funcione correctamente.
# El código debe verificar si un número es positivo y mostrar un mensaje.

print("\n--- Ejercicio 3 ---")

numero = 7

# Inicio del bloque if corregido
if numero > 0:
    # Este print pertenece al bloque if
    print("El número es positivo.")
    # Este también pertenece al bloque if
    print("¡Genial!")
# Este print está fuera del bloque if
print("Fin de la comprobación.")

# --- Ejercicio 4: Ejecución de Script ---
# Guarda este archivo como '00_ejercicios_sintaxis.py'.
# Abre tu terminal o línea de comandos.
# Navega hasta el directorio donde guardaste el archivo.
# Ejecuta el script usando el comando: python 00_ejercicios_sintaxis.py
# Observa la salida en la consola. ¡Ya estás ejecutando tus propios scripts!

print("\n--- Ejercicio 4 ---")
print("Si ves este mensaje, ¡has ejecutado el script correctamente!")

# --- Fin de los ejercicios ---
