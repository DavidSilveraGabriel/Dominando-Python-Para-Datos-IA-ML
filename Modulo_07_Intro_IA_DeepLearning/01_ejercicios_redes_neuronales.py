# Ejercicios: Módulo 7 - Introducción a Redes Neuronales

# --- Prerrequisitos ---
# Se requiere NumPy para algunos cálculos simples.
# pip install numpy
# o
# conda install numpy

import numpy as np

print("--- Conceptos de Redes Neuronales ---")

# --- Ejercicio 1: Componentes de una Neurona Artificial ---
# Instrucciones:
# Describe brevemente (en comentarios) cada uno de los siguientes componentes de una neurona artificial simple:
# a) Entradas (Inputs)
# b) Pesos (Weights)
# c) Sesgo (Bias)
# d) Suma Ponderada (Weighted Sum)
# e) Función de Activación (Activation Function)
# f) Salida (Output)

# Respuestas:
# a) Entradas: Los valores numéricos que recibe la neurona (pueden ser las características originales o salidas de neuronas anteriores).
# b) Pesos: Valores numéricos asociados a cada entrada, que determinan la *importancia* o *influencia* de esa entrada en la salida de la neurona. Se ajustan durante el entrenamiento.
# c) Sesgo: Un valor numérico adicional que se suma a la suma ponderada. Permite a la neurona ajustar su umbral de activación, independientemente de las entradas. También se ajusta durante el entrenamiento.
# d) Suma Ponderada: El resultado de multiplicar cada entrada por su peso correspondiente y sumar todos esos productos. (Σ(entrada_i * peso_i)).
# e) Función de Activación: Una función matemática (generalmente no lineal) que se aplica a la suma ponderada más el sesgo. Introduce no linealidad en la red, permitiéndole aprender patrones complejos. Determina la salida final de la neurona.
# f) Salida: El valor final producido por la neurona después de aplicar la función de activación. Sirve como entrada para otras neuronas o como la predicción final de la red.

print("Ejercicio 1: Componentes de una Neurona - Ver comentarios.")
print("-" * 20)


# --- Ejercicio 2: Cálculo en una Neurona Simple (Sin Activación) ---
# Instrucciones:
# Imagina una neurona con 3 entradas y un sesgo.
# - Entradas (x): [0.5, -1.0, 2.0]
# - Pesos (w): [0.8, 0.2, -0.5]
# - Sesgo (b): 0.1
# 1. Calcula la Suma Ponderada (Σ(x_i * w_i)).
# 2. Calcula la salida de la neurona *antes* de aplicar cualquier función de activación (es decir, Suma Ponderada + Sesgo).

print("\n--- Ejercicio 2: Cálculo en Neurona Simple ---")
# Datos
entradas = np.array([0.5, -1.0, 2.0])
pesos = np.array([0.8, 0.2, -0.5])
sesgo = 0.1

# 1. Calcular Suma Ponderada
suma_ponderada = np.dot(entradas, pesos) # Producto punto es eficiente: (0.5*0.8) + (-1.0*0.2) + (2.0*-0.5)
print(f"Entradas: {entradas}")
print(f"Pesos: {pesos}")
print(f"Suma Ponderada (Σ(x_i * w_i)): {suma_ponderada:.4f}")

# 2. Calcular Salida antes de activación
salida_lineal = suma_ponderada + sesgo
print(f"Sesgo: {sesgo}")
print(f"Salida Lineal (Suma Ponderada + Sesgo): {salida_lineal:.4f}")
print("-" * 20)


# --- Ejercicio 3: Funciones de Activación Comunes ---
# Instrucciones:
# 1. Define una función simple en Python para la activación Sigmoide: sigmoid(x) = 1 / (1 + exp(-x)).
# 2. Define una función simple para la activación ReLU (Rectified Linear Unit): relu(x) = max(0, x).
# 3. Calcula la salida de la neurona del Ejercicio 2 *después* de aplicar la función Sigmoide a `salida_lineal`.
# 4. Calcula la salida de la neurona del Ejercicio 2 *después* de aplicar la función ReLU a `salida_lineal`.
# 5. ¿Por qué son importantes las funciones de activación no lineales (como Sigmoide o ReLU) en las redes neuronales? (Responde en un comentario).

print("\n--- Ejercicio 3: Funciones de Activación ---")

# 1. Función Sigmoide
def sigmoid(x):
  return 1 / (1 + np.exp(-x))

# 2. Función ReLU
def relu(x):
  return np.maximum(0, x)

# Usar la salida_lineal del ejercicio anterior
print(f"Salida Lineal (pre-activación): {salida_lineal:.4f}")

# 3. Aplicar Sigmoide
salida_sigmoide = sigmoid(salida_lineal)
print(f"Salida con Activación Sigmoide: {salida_sigmoide:.4f}")

# 4. Aplicar ReLU
salida_relu = relu(salida_lineal)
print(f"Salida con Activación ReLU: {salida_relu:.4f}")

# 5. Importancia de la No Linealidad
# Respuesta: Las funciones de activación no lineales son cruciales porque permiten a las redes
#            neuronales aprender relaciones y patrones complejos y no lineales en los datos.
#            Si todas las activaciones fueran lineales, una red neuronal profunda (con muchas capas)
#            sería matemáticamente equivalente a una red de una sola capa (una simple transformación lineal),
#            limitando enormemente su capacidad de modelado. La no linealidad introduce la complejidad
#            necesaria para tareas como el reconocimiento de imágenes o el procesamiento del lenguaje.

print("\nImportancia No Linealidad: Ver comentario en el código.")
print("-" * 20)


# --- Ejercicio 4: Estructura de una Red Neuronal ---
# Instrucciones:
# Describe brevemente (en comentarios) el propósito de cada una de las siguientes capas en una red neuronal típica:
# a) Capa de Entrada (Input Layer)
# b) Capas Ocultas (Hidden Layers)
# c) Capa de Salida (Output Layer)

# Respuestas:
# a) Capa de Entrada: Recibe los datos brutos o las características iniciales del problema.
#    El número de neuronas en esta capa suele corresponder al número de características de entrada.
#    No realiza cálculos complejos, simplemente pasa los datos a la primera capa oculta.
# b) Capas Ocultas: Son las capas intermedias entre la entrada y la salida. Aquí es donde
#    ocurre la mayor parte del procesamiento y aprendizaje. Cada neurona recibe entradas de la
#    capa anterior, realiza el cálculo (suma ponderada + sesgo -> activación) y pasa su salida
#    a la siguiente capa. Pueden haber una o muchas capas ocultas (lo que da lugar al "Deep" Learning).
#    Aprenden representaciones cada vez más abstractas de los datos.
# c) Capa de Salida: Produce el resultado final o la predicción de la red. El número de neuronas
#    y la función de activación utilizada en esta capa dependen del tipo de problema:
#    - Regresión: A menudo una sola neurona con activación lineal (o ninguna).
#    - Clasificación Binaria: A menudo una sola neurona con activación Sigmoide (probabilidad).
#    - Clasificación Multiclase: A menudo N neuronas (una por clase) con activación Softmax (distribución de probabilidad sobre las clases).

print("\nEjercicio 4: Estructura de una Red - Ver comentarios.")
print("-" * 20)


# --- Ejercicio 5: Forward vs. Backward Propagation (Conceptual) ---
# Instrucciones:
# Describe brevemente (en comentarios) la diferencia fundamental entre:
# a) Propagación hacia Adelante (Forward Propagation)
# b) Propagación hacia Atrás (Backward Propagation) y Descenso de Gradiente

# Respuestas:
# a) Propagación hacia Adelante: Es el proceso de pasar los datos de entrada a través de la red,
#    capa por capa, desde la entrada hasta la salida, calculando las activaciones de cada neurona
#    usando los pesos y sesgos actuales. El resultado final es la predicción de la red para esa entrada.
# b) Propagación hacia Atrás y Descenso de Gradiente: Es el proceso de *aprendizaje* de la red.
#    1. Se calcula el *error* entre la predicción de la red (obtenida por forward propagation) y el valor real esperado.
#    2. El error se propaga *hacia atrás* a través de la red (desde la salida hacia la entrada).
#    3. Se calcula cuánto contribuyó cada peso y sesgo al error total (calculando gradientes - derivadas parciales - de la función de error respecto a cada parámetro).
#    4. Se utiliza un algoritmo de optimización como el Descenso de Gradiente para *ajustar* los pesos y sesgos en la dirección que *reduce* el error.
#    Este ciclo (Forward -> Calcular Error -> Backward -> Actualizar Pesos) se repite muchas veces con los datos de entrenamiento.

print("\nEjercicio 5: Forward vs Backward Propagation - Ver comentarios.")
print("-" * 20)

# --- Fin de los ejercicios ---
