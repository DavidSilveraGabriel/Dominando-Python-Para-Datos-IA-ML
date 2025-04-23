# Ejercicios: Módulo 6 - Conceptos Clave de Machine Learning

# --- Prerrequisitos ---
# No se requiere código ejecutable específico para este archivo,
# pero tener Scikit-learn instalado será necesario para los siguientes.
# pip install scikit-learn pandas numpy
# o
# conda install scikit-learn pandas numpy

import pandas as pd
import numpy as np
# from sklearn.model_selection import train_test_split # Ejemplo de importación futura
# from sklearn.linear_model import LinearRegression # Ejemplo de importación futura

print("--- Repaso de Conceptos Clave ---")

# --- Ejercicio 1: Identificar Tipos de Aprendizaje ---
# Instrucciones:
# Para cada uno de los siguientes escenarios, identifica si se trata principalmente de
# Aprendizaje Supervisado (Clasificación o Regresión) o Aprendizaje No Supervisado (Clustering, etc.).
# Escribe tus respuestas como comentarios.

# Escenario A: Predecir el precio de venta de una casa basándose en sus características (tamaño, ubicación, número de habitaciones).
# Respuesta A: Aprendizaje Supervisado (Regresión) - Se predice un valor numérico continuo (precio).

# Escenario B: Agrupar a los clientes de una tienda online en diferentes segmentos según su historial de compras.
# Respuesta B: Aprendizaje No Supervisado (Clustering) - Se buscan grupos naturales sin etiquetas previas.

# Escenario C: Determinar si un correo electrónico es spam o no.
# Respuesta C: Aprendizaje Supervisado (Clasificación) - Se predice una categoría discreta (spam/no spam).

# Escenario D: Detectar transacciones bancarias fraudulentas en un conjunto de datos de transacciones.
# Respuesta D: Puede ser Aprendizaje No Supervisado (Detección de Anomalías) si se buscan patrones inusuales,
#             o Aprendizaje Supervisado (Clasificación) si se tienen ejemplos etiquetados de fraude/no fraude.

# Escenario E: Recomendar películas a un usuario basándose en las películas que ha valorado positivamente en el pasado.
# Respuesta E: A menudo se usan técnicas de Aprendizaje Supervisado (prediciendo la calificación que daría a películas no vistas)
#             o métodos específicos de Sistemas de Recomendación (que pueden combinar enfoques).

print("Ejercicio 1: Tipos de Aprendizaje - Ver comentarios en el código.")


# --- Ejercicio 2: Terminología ---
# Instrucciones:
# Relaciona los términos de la izquierda con su descripción más adecuada de la derecha.
# Escribe las parejas correctas como comentarios (ej. A-3, B-1, ...).

# Términos:
# A. Feature (Característica)
# B. Label (Etiqueta)
# C. Instancia (Instance/Sample)
# D. Modelo (Model)
# E. Entrenamiento (Training)
# F. Prueba (Testing)

# Descripciones:
# 1. Una fila individual en el conjunto de datos.
# 2. El proceso de evaluar el rendimiento del modelo con datos no vistos.
# 3. Una columna de entrada utilizada por el modelo para hacer predicciones.
# 4. El algoritmo aprendido que puede hacer predicciones.
# 5. La variable de salida que se intenta predecir en aprendizaje supervisado.
# 6. El proceso de ajustar los parámetros del modelo usando datos conocidos.

# Respuestas:
# A - 3 (Feature - Columna de entrada)
# B - 5 (Label - Variable de salida a predecir)
# C - 1 (Instancia - Fila individual)
# D - 4 (Modelo - Algoritmo aprendido)
# E - 6 (Entrenamiento - Ajustar parámetros con datos)
# F - 2 (Prueba - Evaluar con datos no vistos)

print("\nEjercicio 2: Terminología - Ver comentarios en el código.")


# --- Ejercicio 3: Flujo de Trabajo (Conceptual) ---
# Instrucciones:
# Ordena los siguientes pasos básicos de un flujo de trabajo de ML supervisado.
# Escribe el orden correcto como comentario (ej. 5, 1, 3, ...).

# Pasos (desordenados):
# 1. Evaluar el Modelo
# 2. Entrenar el Modelo
# 3. Dividir los Datos (Train/Test)
# 4. Hacer Predicciones (sobre el Test set)
# 5. Preparar los Datos (Limpieza, Preprocesamiento, Separar X/y)
# 6. Elegir un Modelo

# Orden Correcto:
# 5, 3, 6, 2, 4, 1
# (5. Preparar Datos -> 3. Dividir Datos -> 6. Elegir Modelo -> 2. Entrenar Modelo -> 4. Hacer Predicciones -> 1. Evaluar Modelo)

print("\nEjercicio 3: Flujo de Trabajo - Ver comentarios en el código.")
print("\nEste archivo es principalmente conceptual. Los ejercicios prácticos comenzarán en los siguientes archivos.")

# --- Fin de los ejercicios ---
