# Módulo 6: Modelos de Clasificación (Logística, K-NN, SVM, Árboles)

La **clasificación** es el segundo tipo principal de aprendizaje supervisado. A diferencia de la regresión (que predice un valor continuo), la clasificación predice una **etiqueta de categoría discreta** a la que pertenece una instancia.

**Ejemplos:**
*   Clasificación binaria: Spam o No Spam, Benigno o Maligno, Cliente Comprará o No Comprará.
*   Clasificación multiclase: Tipo de flor (Setosa, Versicolor, Virginica), Dígito escrito a mano (0-9), Categoría de noticia (Deportes, Política, Tecnología).

Scikit-learn ofrece una amplia gama de algoritmos de clasificación. Veremos algunos de los más comunes.

## 1. Regresión Logística (`LogisticRegression`)

*   **A pesar del nombre**, la Regresión Logística es un modelo de **clasificación** (principalmente binaria, aunque Scikit-learn la extiende a multiclase).
*   **Idea:** Modela la **probabilidad** de que una instancia pertenezca a una clase particular (usualmente la clase "positiva", etiquetada como 1) usando una función logística (sigmoide) aplicada a una combinación lineal de las características.
*   **Salida:** Predice la clase directamente (ej. 0 o 1) basándose en si la probabilidad calculada supera un umbral (normalmente 0.5). También puede predecir las probabilidades (`.predict_proba()`).
*   **Ventajas:** Simple, interpretable (los coeficientes indican la influencia de cada característica), computacionalmente eficiente. Buen punto de partida.
*   **Desventajas:** Asume una relación lineal entre las características y el logaritmo de las odds (probabilidad / (1-probabilidad)), puede no capturar relaciones complejas.

## 2. K-Vecinos Más Cercanos (K-Nearest Neighbors - `KNeighborsClassifier`)

*   **Idea:** Es un algoritmo **basado en instancias** o "perezoso" (lazy learner). No aprende un modelo explícito durante el entrenamiento, simplemente almacena los datos de entrenamiento.
*   **Predicción:** Para clasificar una nueva instancia, busca las `k` instancias más cercanas (vecinos) en el conjunto de entrenamiento (según una métrica de distancia, usualmente Euclidiana). La clase predicha es la **clase mayoritaria** entre esos `k` vecinos.
*   **`k`:** Es un hiperparámetro crucial que debes elegir (ej. k=3, k=5). Un `k` pequeño puede ser sensible al ruido, un `k` grande puede suavizar demasiado los límites de decisión.
*   **Ventajas:** Simple de entender e implementar, no hace suposiciones sobre la forma de los datos.
*   **Desventajas:** Computacionalmente costoso en la predicción (necesita calcular distancias a todos los puntos de entrenamiento), sensible a la escala de las características (¡requiere escalado!), sensible a características irrelevantes, no funciona bien con alta dimensionalidad (maldición de la dimensionalidad).

## 3. Máquinas de Vectores de Soporte (Support Vector Machines - `SVC`)

*   **Idea:** Busca encontrar el **hiperplano** (una línea en 2D, un plano en 3D, etc.) que **mejor separa** las diferentes clases en el espacio de características. El "mejor" hiperplano es aquel que tiene el **margen máximo** (la mayor distancia) entre él y los puntos de datos más cercanos de cada clase (llamados **vectores de soporte**).
*   **Kernel Trick:** SVM puede modelar límites de decisión **no lineales** usando el "truco del kernel". Transforma implícitamente los datos a un espacio de mayor dimensión donde sí puedan ser separados linealmente, sin calcular explícitamente las coordenadas en ese espacio. Kernels comunes: `'linear'`, `'poly'`, `'rbf'` (Radial Basis Function - muy popular), `'sigmoid'`.
*   **Hiperparámetros:** `C` (parámetro de regularización, controla el balance entre maximizar el margen y minimizar errores de clasificación) y los parámetros específicos del kernel (como `gamma` para 'rbf').
*   **Ventajas:** Muy efectivo en espacios de alta dimensión, funciona bien cuando el número de dimensiones es mayor que el número de muestras, eficiente en memoria (usa solo los vectores de soporte).
*   **Desventajas:** No funciona tan bien con datasets muy grandes (el entrenamiento puede ser lento), sensible a la elección del kernel y sus hiperparámetros, los resultados no son fácilmente interpretables. Requiere escalado de características.

## 4. Árboles de Decisión (`DecisionTreeClassifier`)

*   **Idea:** Construye un modelo en forma de árbol donde cada nodo interno representa una "prueba" sobre una característica (ej. ¿Edad < 30?), cada rama representa el resultado de la prueba, y cada nodo hoja representa una etiqueta de clase. Para clasificar una nueva instancia, se sigue el camino desde la raíz hasta una hoja según los valores de sus características.
*   **Entrenamiento:** El algoritmo busca recursivamente la mejor característica y el mejor umbral para dividir los datos en cada nodo, usualmente buscando maximizar la "pureza" de los nodos hijos (ej. usando el índice Gini o la entropía).
*   **Ventajas:** Fáciles de entender e interpretar (se pueden visualizar), manejan datos numéricos y categóricos, no requieren escalado de características, pueden capturar interacciones no lineales.
*   **Desventajas:** Propensos al **sobreajuste** (pueden crear árboles muy complejos que memorizan el ruido del entrenamiento), pueden ser inestables (pequeños cambios en los datos pueden llevar a árboles muy diferentes).

*(Nota: El sobreajuste de los árboles de decisión se mitiga usando métodos de ensamblado como Random Forests y Gradient Boosting, que combinan múltiples árboles).*

## Ejemplo Básico de Clasificación con Scikit-learn (Usando Iris Dataset)

El dataset Iris es un clásico para clasificación. Contiene medidas de sépalos y pétalos de 3 especies de flores Iris (Setosa, Versicolor, Virginica).

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler # Para KNN y SVM
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score # Métrica de evaluación simple

# 1. Cargar Datos (Scikit-learn tiene datasets de ejemplo)
from sklearn.datasets import load_iris
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name='species').map({0: 'setosa', 1: 'versicolor', 2: 'virginica'}) # Mapear a nombres

print("Características (X) - Primeras filas:")
print(X.head())
print("\nEtiquetas (y) - Primeras filas:")
print(y.head())
print("\nDistribución de clases:")
print(y.value_counts())

# 2. Dividir Datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# 3. Preprocesamiento (Escalado para KNN y SVM)
# ¡Importante! Ajustar solo en train, transformar en train y test
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# Para Logistic Regression y Decision Tree, el escalado no es estrictamente necesario,
# pero a menudo no perjudica y puede ayudar a la convergencia de algunos solvers.
# Usaremos los datos escalados para todos por simplicidad aquí.

# 4. Entrenar y Evaluar Modelos

# --- Regresión Logística ---
log_reg = LogisticRegression(random_state=42, max_iter=200) # Aumentar max_iter si no converge
log_reg.fit(X_train_scaled, y_train)
y_pred_log = log_reg.predict(X_test_scaled)
acc_log = accuracy_score(y_test, y_pred_log)
print(f"\nAccuracy Regresión Logística: {acc_log:.4f}")

# --- K-Nearest Neighbors (K-NN) ---
knn = KNeighborsClassifier(n_neighbors=5) # Hiperparámetro k=5
knn.fit(X_train_scaled, y_train)
y_pred_knn = knn.predict(X_test_scaled)
acc_knn = accuracy_score(y_test, y_pred_knn)
print(f"Accuracy K-NN (k=5): {acc_knn:.4f}")

# --- Support Vector Machine (SVM) ---
svm_clf = SVC(kernel='rbf', C=1.0, gamma='auto', random_state=42) # Kernel RBF común
svm_clf.fit(X_train_scaled, y_train)
y_pred_svm = svm_clf.predict(X_test_scaled)
acc_svm = accuracy_score(y_test, y_pred_svm)
print(f"Accuracy SVM (kernel=rbf): {acc_svm:.4f}")

# --- Árbol de Decisión ---
tree_clf = DecisionTreeClassifier(max_depth=3, random_state=42) # max_depth limita la profundidad para evitar sobreajuste
tree_clf.fit(X_train_scaled, y_train) # No necesita escalado, pero lo usamos igual
y_pred_tree = tree_clf.predict(X_test_scaled)
acc_tree = accuracy_score(y_test, y_pred_tree)
print(f"Accuracy Árbol de Decisión (max_depth=3): {acc_tree:.4f}")

# (En un proyecto real, haríamos una evaluación más profunda con más métricas
#  y posiblemente validación cruzada para elegir el mejor modelo e hiperparámetros)
```

Scikit-learn proporciona una interfaz consistente (`.fit()`, `.predict()`) para todos estos modelos, lo que facilita experimentar con diferentes algoritmos para tu problema de clasificación. La elección del mejor modelo dependerá de las características específicas de tus datos y de los requisitos de interpretabilidad y rendimiento.
