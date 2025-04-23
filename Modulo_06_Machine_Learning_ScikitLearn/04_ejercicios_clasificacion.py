# Ejercicios: Módulo 6 - Modelos de Clasificación

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
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix # Importamos métricas
from sklearn.datasets import load_iris # Usaremos el dataset Iris

# --- Cargar Datos ---
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
# Usaremos las etiquetas numéricas (0, 1, 2) para Scikit-learn
y = pd.Series(iris.target, name='species')
# Guardamos los nombres de las clases para usarlos en visualizaciones
class_names = iris.target_names

print("--- Dataset Iris Cargado ---")
print("Características (X) - Primeras 5 filas:")
print(X.head())
print("\nEtiquetas (y) - Primeras 5 filas:")
print(y.head())
print(f"\nForma de X: {X.shape}")
print(f"Forma de y: {y.shape}")
print("\nNombres de las clases:", class_names)
print("Distribución de clases:\n", y.value_counts())
print("\n" + "="*30 + "\n")

# --- División y Escalado de Datos ---
# Dividimos ANTES de escalar
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Escalamos DESPUÉS de dividir (ajustamos solo en train)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Datos divididos y escalados.")
print(f"Forma X_train_scaled: {X_train_scaled.shape}, Forma y_train: {y_train.shape}")
print(f"Forma X_test_scaled: {X_test_scaled.shape}, Forma y_test: {y_test.shape}")
print("\n" + "="*30 + "\n")

# --- Función Auxiliar para Matriz de Confusión ---
def plot_confusion_matrix(y_true, y_pred, classes, title):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=classes, yticklabels=classes)
    plt.ylabel('Valor Real')
    plt.xlabel('Valor Predicho')
    plt.title(title)
    plt.show()

# --- Ejercicio 1: Regresión Logística ---
# Instrucciones:
# 1. Crea una instancia de `LogisticRegression`. Usa `random_state=42` y `max_iter=200` (para asegurar convergencia).
# 2. Entrena el modelo usando los datos de entrenamiento **escalados** (`X_train_scaled`, `y_train`).
# 3. Realiza predicciones sobre los datos de prueba **escalados** (`X_test_scaled`). Guarda en `y_pred_log`.
# 4. Calcula e imprime la exactitud (accuracy) del modelo comparando `y_test` con `y_pred_log`.
# 5. (Opcional) Genera y muestra la matriz de confusión usando la función auxiliar `plot_confusion_matrix`.

print("--- Ejercicio 1: Regresión Logística ---")
# Escribe tu código aquí
# 1. Crear modelo
log_reg = LogisticRegression(random_state=42, max_iter=200)

# 2. Entrenar
log_reg.fit(X_train_scaled, y_train)
print("Modelo de Regresión Logística entrenado.")

# 3. Predecir
y_pred_log = log_reg.predict(X_test_scaled)

# 4. Calcular Accuracy
acc_log = accuracy_score(y_test, y_pred_log)
print(f"Accuracy (Regresión Logística): {acc_log:.4f}")

# 5. Matriz de Confusión (Opcional)
plot_confusion_matrix(y_test, y_pred_log, class_names, 'Matriz de Confusión - Regresión Logística')
print("-" * 20)


# --- Ejercicio 2: K-Nearest Neighbors (K-NN) ---
# Instrucciones:
# 1. Crea una instancia de `KNeighborsClassifier` con `n_neighbors=5`.
# 2. Entrena el modelo usando los datos de entrenamiento **escalados**.
# 3. Realiza predicciones sobre los datos de prueba **escalados**. Guarda en `y_pred_knn`.
# 4. Calcula e imprime la exactitud (accuracy).
# 5. (Opcional) Prueba cambiando el valor de `n_neighbors` (ej. a 3 o 7) y observa si la accuracy cambia.

print("\n--- Ejercicio 2: K-Nearest Neighbors (K-NN) ---")
# Escribe tu código aquí
# 1. Crear modelo (k=5)
knn = KNeighborsClassifier(n_neighbors=5)

# 2. Entrenar
knn.fit(X_train_scaled, y_train)
print("Modelo K-NN (k=5) entrenado.")

# 3. Predecir
y_pred_knn = knn.predict(X_test_scaled)

# 4. Calcular Accuracy
acc_knn = accuracy_score(y_test, y_pred_knn)
print(f"Accuracy (K-NN, k=5): {acc_knn:.4f}")

# 5. Opcional: Probar con k=3
knn_3 = KNeighborsClassifier(n_neighbors=3).fit(X_train_scaled, y_train)
y_pred_knn_3 = knn_3.predict(X_test_scaled)
acc_knn_3 = accuracy_score(y_test, y_pred_knn_3)
print(f"Accuracy (K-NN, k=3): {acc_knn_3:.4f}")

plot_confusion_matrix(y_test, y_pred_knn, class_names, 'Matriz de Confusión - K-NN (k=5)')
print("-" * 20)


# --- Ejercicio 3: Support Vector Machine (SVM) ---
# Instrucciones:
# 1. Crea una instancia de `SVC` (Support Vector Classifier). Usa `kernel='rbf'` (común por defecto), `C=1.0`, `gamma='auto'` y `random_state=42`.
# 2. Entrena el modelo usando los datos de entrenamiento **escalados**.
# 3. Realiza predicciones sobre los datos de prueba **escalados**. Guarda en `y_pred_svm`.
# 4. Calcula e imprime la exactitud (accuracy).
# 5. (Opcional) Prueba con `kernel='linear'`. ¿Cambia la accuracy?

print("\n--- Ejercicio 3: Support Vector Machine (SVM) ---")
# Escribe tu código aquí
# 1. Crear modelo (RBF kernel)
svm_rbf = SVC(kernel='rbf', C=1.0, gamma='auto', random_state=42)

# 2. Entrenar
svm_rbf.fit(X_train_scaled, y_train)
print("Modelo SVM (kernel RBF) entrenado.")

# 3. Predecir
y_pred_svm = svm_rbf.predict(X_test_scaled)

# 4. Calcular Accuracy
acc_svm = accuracy_score(y_test, y_pred_svm)
print(f"Accuracy (SVM, kernel=rbf): {acc_svm:.4f}")

# 5. Opcional: Probar con kernel lineal
svm_linear = SVC(kernel='linear', random_state=42).fit(X_train_scaled, y_train)
y_pred_svm_lin = svm_linear.predict(X_test_scaled)
acc_svm_lin = accuracy_score(y_test, y_pred_svm_lin)
print(f"Accuracy (SVM, kernel=linear): {acc_svm_lin:.4f}")

plot_confusion_matrix(y_test, y_pred_svm, class_names, 'Matriz de Confusión - SVM (RBF)')
print("-" * 20)


# --- Ejercicio 4: Árbol de Decisión ---
# Instrucciones:
# 1. Crea una instancia de `DecisionTreeClassifier`. Usa `max_depth=3` para limitar la complejidad y `random_state=42`.
# 2. Entrena el modelo. Puedes usar los datos escalados (`X_train_scaled`) o los originales (`X_train`), ya que los árboles son menos sensibles a la escala. Usemos los **escalados** por consistencia en este script.
# 3. Realiza predicciones sobre los datos de prueba **escalados** (`X_test_scaled`). Guarda en `y_pred_tree`.
# 4. Calcula e imprime la exactitud (accuracy).
# 5. (Opcional) Intenta sin `max_depth` o con un `max_depth` mayor. ¿Cómo afecta a la accuracy (podría sobreajustar)?

print("\n--- Ejercicio 4: Árbol de Decisión ---")
# Escribe tu código aquí
# 1. Crear modelo (max_depth=3)
tree_clf = DecisionTreeClassifier(max_depth=3, random_state=42)

# 2. Entrenar (con datos escalados por consistencia)
tree_clf.fit(X_train_scaled, y_train)
print("Modelo Árbol de Decisión (max_depth=3) entrenado.")

# 3. Predecir
y_pred_tree = tree_clf.predict(X_test_scaled)

# 4. Calcular Accuracy
acc_tree = accuracy_score(y_test, y_pred_tree)
print(f"Accuracy (Árbol Decisión, max_depth=3): {acc_tree:.4f}")

# 5. Opcional: Probar sin max_depth
tree_full = DecisionTreeClassifier(random_state=42).fit(X_train_scaled, y_train)
y_pred_tree_full = tree_full.predict(X_test_scaled)
acc_tree_full = accuracy_score(y_test, y_pred_tree_full)
print(f"Accuracy (Árbol Decisión, sin max_depth): {acc_tree_full:.4f}") # Puede ser igual o ligeramente diferente

plot_confusion_matrix(y_test, y_pred_tree, class_names, 'Matriz de Confusión - Árbol (max_depth=3)')
print("-" * 20)

# --- Fin de los ejercicios ---
