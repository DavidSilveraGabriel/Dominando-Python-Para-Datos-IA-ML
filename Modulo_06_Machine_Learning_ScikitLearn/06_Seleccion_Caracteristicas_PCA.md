# Módulo 6: Selección de Características y Reducción de Dimensionalidad (PCA Básico)

En muchos problemas de Machine Learning, especialmente con datasets del mundo real, nos encontramos con una gran cantidad de **características (features)**. No todas estas características son necesariamente útiles para construir un buen modelo predictivo. Algunas pueden ser:

*   **Irrelevantes:** No tienen relación con la variable objetivo.
*   **Redundantes:** Están altamente correlacionadas con otras características (aportan poca información nueva).
*   **Ruidosas:** Contienen más ruido que señal útil.

Trabajar con demasiadas características (alta dimensionalidad) puede llevar a varios problemas, conocidos como la **"maldición de la dimensionalidad"**:

*   **Mayor riesgo de sobreajuste (Overfitting):** El modelo puede aprender patrones espurios del ruido en los datos de entrenamiento.
*   **Mayor costo computacional:** Entrenar modelos y hacer predicciones es más lento y requiere más memoria.
*   **Dificultad de interpretación:** Es más difícil entender qué características son realmente importantes para las predicciones del modelo.
*   **Necesidad de más datos:** Se necesitan exponencialmente más datos para cubrir adecuadamente el espacio de características a medida que aumenta la dimensionalidad.

Para mitigar estos problemas, se utilizan técnicas de **Selección de Características** y **Reducción de Dimensionalidad**.

## Selección de Características (Feature Selection)

*   **Objetivo:** Seleccionar un **subconjunto** de las características originales que sean más relevantes para la tarea de predicción, descartando las menos útiles.
*   **Métodos Comunes (Scikit-learn ofrece herramientas para muchos de ellos):**
    *   **Métodos de Filtro:** Evalúan la relevancia de cada característica de forma independiente del modelo (ej. usando correlación con la variable objetivo, pruebas estadísticas como ANOVA o chi-cuadrado). Son rápidos pero no consideran interacciones entre características. (`SelectKBest`, `SelectPercentile`).
    *   **Métodos Wrapper:** Utilizan un modelo específico para evaluar subconjuntos de características. Buscan el subconjunto que da el mejor rendimiento para ese modelo (ej. Selección Recursiva de Características - RFE). Son más costosos computacionalmente pero pueden dar mejores resultados. (`RFE`, `SequentialFeatureSelector`).
    *   **Métodos Embebidos (Embedded):** La selección de características se realiza como parte intrínseca del proceso de entrenamiento del modelo. (Ej. Regularización L1 en Lasso, importancia de características en modelos basados en árboles como Random Forest).

## Reducción de Dimensionalidad (Dimensionality Reduction)

*   **Objetivo:** Transformar las características originales de alta dimensión en un **nuevo conjunto de características de menor dimensión**, tratando de **preservar la mayor cantidad de información relevante** posible. Las nuevas características son combinaciones de las originales y pueden no ser directamente interpretables.
*   **Usos:** Visualización de datos de alta dimensión (reduciendo a 2D o 3D), compresión de datos, mejora del rendimiento de otros algoritmos de ML al eliminar ruido o redundancia.

**Principal Component Analysis (PCA - Análisis de Componentes Principales):**

*   **¿Qué es?** Es la técnica de reducción de dimensionalidad **no supervisada** más popular.
*   **Idea:** Encuentra las **direcciones (componentes principales)** en los datos a lo largo de las cuales la **varianza es máxima**. Estas direcciones son combinaciones lineales de las características originales y son ortogonales (no correlacionadas) entre sí.
*   **Proceso:**
    1.  Estandariza los datos (importante porque PCA es sensible a la escala).
    2.  Calcula la matriz de covarianza o utiliza la Descomposición en Valores Singulares (SVD) de los datos.
    3.  Obtiene los vectores propios (eigenvectors) y valores propios (eigenvalues) de la matriz de covarianza (o de la SVD). Los vectores propios representan las direcciones de los componentes principales, y los valores propios indican la cantidad de varianza explicada por cada componente.
    4.  Ordena los componentes principales de mayor a menor según la varianza explicada.
    5.  Selecciona los `k` componentes principales que explican la mayor parte de la varianza (ej. 95% de la varianza total).
    6.  Proyecta los datos originales sobre estos `k` componentes principales para obtener el nuevo dataset de menor dimensión.
*   **Implementación en Scikit-learn:** `sklearn.decomposition.PCA`

**Ejemplo Básico de PCA:**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris # Usaremos Iris de nuevo

# 1. Cargar Datos
iris = load_iris()
X = iris.data # Características (4 dimensiones)
y = iris.target # Etiquetas (especies)
feature_names = iris.feature_names

print("Forma original de X:", X.shape)

# 2. Escalar los Datos (¡Esencial para PCA!)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Aplicar PCA
# Queremos reducir a 2 dimensiones para visualizar
n_components = 2
pca = PCA(n_components=n_components)

# Ajustar PCA a los datos escalados y transformar
X_pca = pca.fit_transform(X_scaled)

print(f"Forma de X después de PCA ({n_components} componentes): {X_pca.shape}")

# 4. Varianza Explicada
# pca.explained_variance_ratio_ nos dice qué proporción de la varianza
# explica cada componente principal seleccionado.
print(f"\nVarianza explicada por cada componente: {pca.explained_variance_ratio_}")
print(f"Varianza total explicada por {n_components} componentes: {pca.explained_variance_ratio_.sum():.4f}")

# 5. Visualizar los datos reducidos (2D)
df_pca = pd.DataFrame(data=X_pca, columns=['Componente Principal 1', 'Componente Principal 2'])
df_pca['Especie'] = pd.Series(y).map({0: 'setosa', 1: 'versicolor', 2: 'virginica'}) # Añadir etiquetas para colorear

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Componente Principal 1', y='Componente Principal 2', hue='Especie', data=df_pca, alpha=0.8)
plt.title('Dataset Iris Proyectado en 2 Componentes Principales (PCA)')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.grid(True)
plt.show()
```
*   Observa cómo PCA (una técnica no supervisada, no usó las etiquetas `y` para el ajuste) logra encontrar una proyección 2D donde las clases (especies) están bastante bien separadas, capturando la estructura principal de los datos originales de 4 dimensiones.

**Otras Técnicas:**

*   **Linear Discriminant Analysis (LDA):** Técnica de reducción de dimensionalidad **supervisada** (usa las etiquetas `y`) que busca maximizar la separabilidad entre clases.
*   **t-SNE (t-Distributed Stochastic Neighbor Embedding):** Técnica no lineal popular para visualización de alta dimensión, especialmente buena para revelar clústeres locales (pero no preserva bien las distancias globales).

La selección de características y la reducción de dimensionalidad son herramientas valiosas para mejorar los modelos, reducir la complejidad computacional y facilitar la visualización y comprensión de datos de alta dimensión. PCA es una de las técnicas más fundamentales y ampliamente utilizadas en este ámbito.
