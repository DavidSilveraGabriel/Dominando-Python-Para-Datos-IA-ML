# Ejercicios: Módulo 1 - Variables y Tipos de Datos Primitivos

# --- Ejercicio 1: Creación de Variables ---
# Instrucciones: Declara (crea) las siguientes variables y asígnales valores apropiados.
# 1. Una variable llamada `nombre_curso` que almacene el nombre de este curso (como string).
# 2. Una variable llamada `numero_modulo` que almacene el número de este módulo (como entero).
# 3. Una variable llamada `duracion_horas` que almacene una estimación de cuántas horas dura el módulo (puede ser float).
# 4. Una variable llamada `es_introductorio` que indique si este módulo es introductorio (como booleano).
# Imprime el valor de cada variable usando print().

print("--- Ejercicio 1 ---")
# Escribe tu código aquí
nombre_curso = "Curso Completo de Python"
numero_modulo = 1
duracion_horas = 15.5
es_introductorio = True

print(f"Nombre del curso: {nombre_curso}")
print(f"Número del módulo: {numero_modulo}")
print(f"Duración estimada (horas): {duracion_horas}")
print(f"¿Es introductorio?: {es_introductorio}")


# --- Ejercicio 2: Verificación de Tipos ---
# Instrucciones: Utiliza la función type() para verificar el tipo de dato de cada una de las
# variables creadas en el Ejercicio 1. Imprime el tipo de cada variable.

print("\n--- Ejercicio 2 ---")
# Escribe tu código aquí
print(f"Tipo de nombre_curso: {type(nombre_curso)}")
print(f"Tipo de numero_modulo: {type(numero_modulo)}")
print(f"Tipo de duracion_horas: {type(duracion_horas)}")
print(f"Tipo de es_introductorio: {type(es_introductorio)}")


# --- Ejercicio 3: Nombres de Variables (Identificación) ---
# Instrucciones: Indica cuáles de los siguientes nombres de variables son válidos y recomendados
# según PEP 8, cuáles son válidos pero no recomendados, y cuáles son inválidos.
# Escribe tus respuestas como comentarios (# Respuesta: ...).

print("\n--- Ejercicio 3 ---")

# 1. edadUsuario
# Respuesta: Válido, pero no recomendado (PEP 8 prefiere snake_case: edad_usuario)

# 2. tasa_interes_anual
# Respuesta: Válido y recomendado (snake_case)

# 3. 2doNombre
# Respuesta: Inválido (no puede empezar con número)

# 4. True
# Respuesta: Inválido (palabra reservada)

# 5. _variable_privada
# Respuesta: Válido y recomendado (convención para indicar uso interno)

# 6. mi-variable-con-guiones
# Respuesta: Inválido (no se permiten guiones medios en nombres de variables)

# 7. nombre completo
# Respuesta: Inválido (no se permiten espacios)

# 8. PI
# Respuesta: Válido y recomendado para constantes (UPPERCASE_SNAKE_CASE)


# --- Ejercicio 4: Reasignación y Tipado Dinámico ---
# Instrucciones:
# 1. Crea una variable llamada `valor` y asígnale un número entero. Imprime su valor y tipo.
# 2. Reasigna la variable `valor` con un texto (string). Imprime su nuevo valor y tipo.
# 3. Reasigna la variable `valor` con un valor booleano. Imprime su último valor y tipo.
# Observa cómo el tipo de la variable cambia.

print("\n--- Ejercicio 4 ---")
# Escribe tu código aquí
valor = 100
print(f"Valor inicial: {valor}, Tipo: {type(valor)}")

valor = "Cambié a string"
print(f"Valor reasignado: {valor}, Tipo: {type(valor)}")

valor = False
print(f"Último valor: {valor}, Tipo: {type(valor)}")


# --- Fin de los ejercicios ---
