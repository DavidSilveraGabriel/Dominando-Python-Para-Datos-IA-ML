# Ejercicios: Módulo 6 - Evaluación de Modelos: Métricas Comunes

# --- Prerrequisitos ---
# pip install scikit-learn pandas numpy matplotlib seaborn
# o
# conda install scikit-learn pandas numpy matplotlib seaborn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# Modelos para generar predicciones
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.datasets import load_iris, make_regression
# Métricas
from sklearn.metrics import (
    # Clasificación
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    # Regresión
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# --- Función Auxiliar para Matriz de Confusión (reutilizada) ---
def plot_confusion_matrix(y_true, y_pred, classes, title):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=classes, yticklabels=classes)
    plt.ylabel('Valor Real')
    plt.xlabel('Valor Predicho')
    plt.title(title)
    plt.show()

# --- Preparación de Datos y Modelos (para tener predicciones que evaluar) ---

# 1. Datos y Modelo de Clasificación (Iris)
print("--- Preparando datos y modelo de CLASIFICACIÓN ---")
iris = load_iris()
X_iris = iris.data
y_iris = iris.target
class_names_iris = iris.target_names

X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(
    X_iris, y_iris, test_size=0.3, random_state=42, stratify=y_iris
)
scaler_iris = StandardScaler()
X_train_iris_scaled = scaler_iris.fit_transform(X_train_iris)
X_test_iris_scaled = scaler_iris.transform(X_test_iris)

# Entrenar un modelo simple (Regresión Logística)
log_reg_eval = LogisticRegression(random_state=42, max_iter=200)
log_reg_eval.fit(X_train_iris_scaled, y_train_iris)
y_pred_iris = log_reg_eval.predict(X_test_iris_scaled)
print("Predicciones de clasificación generadas (y_test_iris, y_pred_iris).")
print("-" * 20)

# 2. Datos y Modelo de Regresión (Sintético)
print("\n--- Preparando datos y modelo de REGRESIÓN ---")
X_reg, y_reg = make_regression(n_samples=100, n_features=1, noise=15, random_state=42)

X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg, y_reg, test_size=0.3, random_state=42
)

# Entrenar un modelo simple (Regresión Lineal)
lin_reg_eval = LinearRegression()
lin_reg_eval.fit(X_train_reg, y_train_reg)
y_pred_reg = lin_reg_eval.predict(X_test_reg)
print("Predicciones de regresión generadas (y_test_reg, y_pred_reg).")
print("-" * 20)

print("\n" + "="*30 + "\n")


# --- Ejercicio 1: Métricas de Clasificación ---
# Instrucciones:
# Usa `y_test_iris` (valores reales) y `y_pred_iris` (predicciones del modelo).
# 1. Calcula e imprime la Exactitud (Accuracy).
# 2. Calcula, imprime y visualiza la Matriz de Confusión.
# 3. Calcula e imprime la Precisión (Precision).
#    - Nota: Para multiclase, `precision_score` necesita el argumento `average`. Usa `average='weighted'` para calcular la media ponderada por el soporte de cada clase.
# 4. Calcula e imprime la Sensibilidad (Recall). Usa `average='weighted'`.
# 5. Calcula e imprime el F1-Score. Usa `average='weighted'`.
# 6. Genera e imprime el Reporte de Clasificación (`classification_report`), que muestra estas métricas por clase.

print("--- Ejercicio 1: Métricas de Clasificación (Dataset Iris) ---")
# Escribe tu código aquí
# 1. Accuracy
acc_iris = accuracy_score(y_test_iris, y_pred_iris)
print(f"1. Accuracy: {acc_iris:.4f}")

# 2. Matriz de Confusión
print("\n2. Matriz de Confusión:")
print(confusion_matrix(y_test_iris, y_pred_iris))
plot_confusion_matrix(y_test_iris, y_pred_iris, class_names_iris, 'Matriz de Confusión - Iris')

# 3. Precision (Weighted Avg)
prec_iris = precision_score(y_test_iris, y_pred_iris, average='weighted')
print(f"\n3. Precision (Weighted Avg): {prec_iris:.4f}")

# 4. Recall (Weighted Avg)
rec_iris = recall_score(y_test_iris, y_pred_iris, average='weighted')
print(f"4. Recall (Weighted Avg): {rec_iris:.4f}")

# 5. F1-Score (Weighted Avg)
f1_iris = f1_score(y_test_iris, y_pred_iris, average='weighted')
print(f"5. F1-Score (Weighted Avg): {f1_iris:.4f}")

# 6. Classification Report
report_iris = classification_report(y_test_iris, y_pred_iris, target_names=class_names_iris)
print("\n6. Classification Report:")
print(report_iris)
print("-" * 20)


# --- Ejercicio 2: Métricas de Regresión ---
# Instrucciones:
# Usa `y_test_reg` (valores reales) y `y_pred_reg` (predicciones del modelo).
# 1. Calcula e imprime el Error Absoluto Medio (MAE). Explica brevemente qué representa (en comentarios).
# 2. Calcula e imprime el Error Cuadrático Medio (MSE).
# 3. Calcula e imprime la Raíz del Error Cuadrático Medio (RMSE). Explica brevemente qué representa y cómo se relaciona con MAE.
# 4. Calcula e imprime el Coeficiente de Determinación (R²). Explica brevemente qué representa.

print("\n--- Ejercicio 2: Métricas de Regresión ---")
# Escribe tu código aquí
# 1. MAE
mae_reg = mean_absolute_error(y_test_reg, y_pred_reg)
print(f"1. Mean Absolute Error (MAE): {mae_reg:.4f}")
# Representa el promedio de la diferencia absoluta entre el valor real y el predicho.
# Está en las mismas unidades que la variable objetivo 'y'. Indica, en promedio, cuánto se equivoca la predicción.

# 2. MSE
mse_reg = mean_squared_error(y_test_reg, y_pred_reg)
print(f"\n2. Mean Squared Error (MSE): {mse_reg:.4f}")
# Representa el promedio de las diferencias al cuadrado. Penaliza más los errores grandes.
# Sus unidades son las de 'y' al cuadrado, menos interpretable directamente.

# 3. RMSE
rmse_reg = np.sqrt(mse_reg) # O mean_squared_error(y_test_reg, y_pred_reg, squared=False)
print(f"\n3. Root Mean Squared Error (RMSE): {rmse_reg:.4f}")
# Es la raíz cuadrada del MSE. Vuelve a estar en las mismas unidades que 'y'.
# Representa la desviación estándar de los errores de predicción. Como MAE, indica el error promedio,
# pero al basarse en MSE, da más peso a los errores grandes.

# 4. R-squared (R²)
r2_reg = r2_score(y_test_reg, y_pred_reg)
print(f"\n4. R-squared (R²): {r2_reg:.4f}")
# Representa la proporción de la varianza de la variable objetivo ('y') que es explicada
# por el modelo. Un valor cercano a 1 indica que el modelo explica gran parte de la variabilidad.
# Un valor cercano a 0 indica que el modelo no explica la variabilidad mejor que simplemente predecir la media.
# Puede ser negativo si el modelo es peor que predecir la media.

print("-" * 20)


# --- Ejercicio 3: Interpretación y Selección de Métricas (Conceptual) ---
# Instrucciones:
# Responde a las siguientes preguntas como comentarios.

# Pregunta A: En un problema de detección de fraude (clasificación binaria), donde detectar un fraude (positivo) es crucial, pero marcar una transacción legítima como fraude (falso positivo) es problemático pero menos grave que no detectar un fraude (falso negativo), ¿qué métrica(s) serían más importantes: Precision o Recall? ¿Por qué?
# Respuesta A: Recall (Sensibilidad) sería probablemente más importante. Queremos minimizar los Falsos Negativos (fraudes no detectados), incluso si eso significa aumentar un poco los Falsos Positivos (transacciones legítimas marcadas). Un alto Recall asegura que capturemos la mayoría de los fraudes reales. La Precision también es relevante para no molestar demasiado a los clientes legítimos, por lo que F1-Score podría ser una buena métrica de balance.

# Pregunta B: Estás prediciendo precios de casas (regresión). Tienes dos modelos:
#    - Modelo 1: MAE = $15,000, RMSE = $25,000
#    - Modelo 2: MAE = $18,000, RMSE = $22,000
#    ¿Qué te dice la diferencia entre MAE y RMSE sobre los errores de cada modelo? ¿Qué modelo podrías preferir si quieres evitar errores muy grandes ocasionales?
# Respuesta B:
# - El Modelo 1 tiene un error absoluto promedio más bajo ($15k vs $18k), lo que sugiere que en general sus predicciones están más cerca del valor real. Sin embargo, su RMSE es mayor ($25k vs $22k).
# - Dado que RMSE penaliza más los errores grandes que MAE, una diferencia mayor entre RMSE y MAE (como en el Modelo 1: $25k - $15k = $10k) en comparación con el Modelo 2 ($22k - $18k = $4k) sugiere que el Modelo 1, aunque más preciso en promedio, comete algunos errores ocasionales *muy grandes* que inflan su RMSE.
# - Si quieres evitar errores muy grandes ocasionales, podrías preferir el Modelo 2, ya que su RMSE es menor, indicando una menor dispersión de los errores y menos errores extremadamente grandes, aunque su error promedio (MAE) sea ligeramente mayor. La elección final depende de la tolerancia a diferentes tipos de error en el contexto del problema.

# Pregunta C: ¿Por qué la Accuracy puede ser una métrica engañosa en datasets de clasificación desbalanceados?
# Respuesta C: En un dataset desbalanceado (ej. 99% clase A, 1% clase B), un modelo trivial que *siempre* predice la clase mayoritaria (clase A) lograría una Accuracy del 99%. Sin embargo, este modelo es completamente inútil para identificar la clase minoritaria (clase B), que suele ser la de interés (ej. detección de enfermedades raras, fraude). Por eso, en casos desbalanceados, métricas como Precision, Recall, F1-Score o el análisis de la Matriz de Confusión son mucho más informativas que la Accuracy sola.

print("\n--- Ejercicio 3: Interpretación y Selección de Métricas ---")
print("Ver comentarios en el código para las respuestas.")
print("-" * 20)

# --- Fin de los ejercicios ---
