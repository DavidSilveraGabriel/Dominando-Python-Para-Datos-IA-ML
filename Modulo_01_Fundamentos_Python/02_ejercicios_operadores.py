# Ejercicios: Módulo 1 - Operadores

# --- Ejercicio 1: Operadores Aritméticos ---
# Instrucciones: Dados dos números, `num1 = 18` y `num2 = 4`, realiza las siguientes operaciones
# e imprime los resultados:
# 1. Suma
# 2. Resta (num1 - num2)
# 3. Multiplicación
# 4. División (resultado float)
# 5. División Entera
# 6. Módulo (Resto)
# 7. Potencia (num1 elevado a num2)

print("--- Ejercicio 1: Operadores Aritméticos ---")
num1 = 18
num2 = 4

# Escribe tu código aquí
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
division_entera = num1 // num2
modulo = num1 % num2
potencia = num1 ** num2

print(f"{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} * {num2} = {multiplicacion}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} // {num2} = {division_entera}")
print(f"{num1} % {num2} = {modulo}")
print(f"{num1} ** {num2} = {potencia}")


# --- Ejercicio 2: Operadores de Comparación ---
# Instrucciones: Dadas las variables `edad = 25` y `altura = 1.75`, evalúa las siguientes
# condiciones e imprime el resultado booleano (`True` o `False`):
# 1. ¿Es la edad mayor o igual a 18?
# 2. ¿Es la altura diferente de 1.80?
# 3. ¿Es la edad exactamente 25?
# 4. ¿Es la altura menor o igual que la edad? (Conceptualmente no tiene sentido, pero practica la sintaxis)

print("\n--- Ejercicio 2: Operadores de Comparación ---")
edad = 25
altura = 1.75

# Escribe tu código aquí
print(f"¿Edad >= 18? {edad >= 18}")
print(f"¿Altura != 1.80? {altura != 1.80}")
print(f"¿Edad == 25? {edad == 25}")
print(f"¿Altura <= Edad? {altura <= edad}")


# --- Ejercicio 3: Operadores Lógicos ---
# Instrucciones: Dadas las variables booleanas `es_estudiante = True` y `trabaja = False`,
# evalúa e imprime el resultado de las siguientes expresiones lógicas:
# 1. ¿Es estudiante Y trabaja?
# 2. ¿Es estudiante O trabaja?
# 3. ¿NO es estudiante?
# 4. ¿NO trabaja?

print("\n--- Ejercicio 3: Operadores Lógicos ---")
es_estudiante = True
trabaja = False

# Escribe tu código aquí
print(f"¿Es estudiante Y trabaja? {es_estudiante and trabaja}")
print(f"¿Es estudiante O trabaja? {es_estudiante or trabaja}")
print(f"¿NO es estudiante? {not es_estudiante}")
print(f"¿NO trabaja? {not trabaja}")


# --- Ejercicio 4: Operadores de Asignación ---
# Instrucciones:
# 1. Crea una variable `puntuacion` inicializada en 100.
# 2. Usa un operador de asignación para restarle 15 a `puntuacion`. Imprime el resultado.
# 3. Usa un operador de asignación para multiplicar `puntuacion` por 2. Imprime el resultado.
# 4. Usa un operador de asignación para dividir `puntuacion` entre 3 (división real). Imprime el resultado.

print("\n--- Ejercicio 4: Operadores de Asignación ---")
# Escribe tu código aquí
puntuacion = 100
print(f"Puntuación inicial: {puntuacion}")

puntuacion -= 15
print(f"Después de restar 15: {puntuacion}")

puntuacion *= 2
print(f"Después de multiplicar por 2: {puntuacion}")

puntuacion /= 3
print(f"Después de dividir entre 3: {puntuacion}")


# --- Ejercicio 5: Combinación de Operadores ---
# Instrucciones: Calcula el resultado de la siguiente expresión compleja, prestando atención
# al orden de operaciones (PEMDAS/BODMAS): `resultado = 10 + 20 * 3 / 2 - 5`
# Imprime el resultado final.

print("\n--- Ejercicio 5: Combinación de Operadores ---")
# Escribe tu código aquí
# Orden:
# 1. Multiplicación: 20 * 3 = 60
# 2. División: 60 / 2 = 30.0
# 3. Suma: 10 + 30.0 = 40.0
# 4. Resta: 40.0 - 5 = 35.0
resultado_calculado = 10 + 20 * 3 / 2 - 5
resultado_esperado = 35.0

print(f"Resultado de 10 + 20 * 3 / 2 - 5 = {resultado_calculado}")
print(f"¿Es el resultado igual a {resultado_esperado}? {resultado_calculado == resultado_esperado}")


# --- Fin de los ejercicios ---
