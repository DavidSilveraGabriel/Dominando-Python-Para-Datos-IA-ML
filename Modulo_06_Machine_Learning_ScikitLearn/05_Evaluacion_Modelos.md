# Módulo 6: Evaluación de Modelos: Métricas Comunes

Entrenar un modelo es solo una parte del proceso. Necesitamos saber qué tan bien funciona, especialmente con datos que no ha visto antes (el conjunto de prueba). La **evaluación del modelo** utiliza **métricas** específicas para cuantificar su rendimiento. Las métricas adecuadas dependen del tipo de problema (regresión o clasificación) y de los objetivos específicos del proyecto.

Scikit-learn proporciona muchas de estas métricas en el módulo `sklearn.metrics`.

```python
# Importaciones necesarias (asumiendo que tenemos y_test, y_pred de ejemplos anteriores)
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
import numpy as np # Para RMSE
import seaborn as sns # Para visualizar matriz de confusión
import matplotlib.pyplot as plt # Para visualizar matriz de confusión

# --- Asumimos que tenemos y_test y y_pred de los ejemplos anteriores ---
# Ejemplo: y_test_clas y y_pred_clas (para clasificación)
# Ejemplo: y_test_reg y y_pred_reg (para regresión)
# (Si ejecutas este código, necesitarás generar o cargar estos valores)

# --- Datos de ejemplo simulados para demostración ---
# Clasificación (Binaria)
y_test_clas = np.array([1, 0, 1, 1, 0, 0, 1, 0, 1, 0])
y_pred_clas = np.array([1, 0, 1, 0, 0, 1, 1, 0, 1, 0]) # Algunas predicciones correctas, otras incorrectas

# Regresión
y_test_reg = np.array([10, 15, 12, 18, 25, 22])
y_pred_reg = np.array([11, 14, 13, 17, 23, 21])
```

## Métricas de Evaluación para Clasificación

Evalúan qué tan bien el modelo asigna las instancias a las clases correctas.

1.  **Accuracy (Exactitud):**
    *   **¿Qué mide?** La proporción de predicciones correctas sobre el total de predicciones. `(TP + TN) / (TP + TN + FP + FN)`
    *   **Función:** `accuracy_score(y_true, y_pred)`
    *   **Cuándo usar:** Es una métrica simple y útil cuando las clases están **balanceadas** (aproximadamente el mismo número de instancias por clase).
    *   **Limitación:** Puede ser **engañosa** en datasets **desbalanceados**. Un modelo que siempre predice la clase mayoritaria puede tener alta accuracy pero ser inútil.

    ```python
    acc = accuracy_score(y_test_clas, y_pred_clas)
    print(f"--- Métricas de Clasificación ---")
    print(f"Accuracy: {acc:.4f}")
    ```

2.  **Matriz de Confusión:**
    *   **¿Qué es?** Una tabla que resume el rendimiento de un clasificador. Compara las clases reales con las clases predichas. Para clasificación binaria:
        *   **Verdaderos Positivos (TP):** Real = 1, Predicho = 1
        *   **Verdaderos Negativos (TN):** Real = 0, Predicho = 0
        *   **Falsos Positivos (FP) / Error Tipo I:** Real = 0, Predicho = 1 (predijo positivo incorrectamente)
        *   **Falsos Negativos (FN) / Error Tipo II:** Real = 1, Predicho = 0 (predijo negativo incorrectamente)
    *   **Función:** `confusion_matrix(y_true, y_pred)`
    *   **Utilidad:** Permite ver exactamente qué tipos de errores está cometiendo el modelo.

    ```python
    cm = confusion_matrix(y_test_clas, y_pred_clas)
    print(f"\nMatriz de Confusión:\n{cm}")
    # Visualización (opcional pero útil)
    plt.figure(figsize=(4,3))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Pred Neg (0)', 'Pred Pos (1)'], yticklabels=['Real Neg (0)', 'Real Pos (1)'])
    plt.ylabel('Valor Real')
    plt.xlabel('Valor Predicho')
    plt.title('Matriz de Confusión')
    plt.show()
    ```

3.  **Precision (Precisión):**
    *   **¿Qué mide?** De todas las instancias que el modelo predijo como positivas, ¿cuántas eran *realmente* positivas? `TP / (TP + FP)`
    *   **Función:** `precision_score(y_true, y_pred)`
    *   **Cuándo es importante:** Cuando el coste de un **Falso Positivo** es alto. (Ej: Marcar un correo importante como spam, diagnosticar erróneamente una enfermedad grave). Quieres estar seguro cuando predices positivo.

    ```python
    prec = precision_score(y_test_clas, y_pred_clas)
    print(f"\nPrecision: {prec:.4f}")
    ```

4.  **Recall (Sensibilidad, Exhaustividad, Tasa de Verdaderos Positivos):**
    *   **¿Qué mide?** De todas las instancias que eran *realmente* positivas, ¿cuántas identificó *correctamente* el modelo? `TP / (TP + FN)`
    *   **Función:** `recall_score(y_true, y_pred)`
    *   **Cuándo es importante:** Cuando el coste de un **Falso Negativo** es alto. (Ej: No detectar una transacción fraudulenta, no diagnosticar a un paciente enfermo). Quieres encontrar tantos positivos reales como sea posible.

    ```python
    rec = recall_score(y_test_clas, y_pred_clas)
    print(f"Recall (Sensitivity): {rec:.4f}")
    ```

5.  **F1-Score:**
    *   **¿Qué mide?** La **media armónica** de Precision y Recall. Proporciona una única métrica que balancea ambas. `2 * (Precision * Recall) / (Precision + Recall)`
    *   **Función:** `f1_score(y_true, y_pred)`
    *   **Cuándo usar:** Útil cuando buscas un equilibrio entre Precision y Recall, especialmente en datasets desbalanceados donde la Accuracy puede ser engañosa.

    ```python
    f1 = f1_score(y_test_clas, y_pred_clas)
    print(f"F1-Score: {f1:.4f}")
    ```

6.  **Classification Report:**
    *   **¿Qué es?** Una función que muestra un resumen de las principales métricas (precision, recall, f1-score) para **cada clase**, además de la accuracy general. Muy útil para obtener una visión completa.
    *   **Función:** `classification_report(y_true, y_pred)`

    ```python
    report = classification_report(y_test_clas, y_pred_clas)
    print(f"\nClassification Report:\n{report}")
    ```

*(Otras métricas importantes incluyen la Curva ROC y el Área Bajo la Curva (AUC), que evalúan el rendimiento del clasificador a través de diferentes umbrales de probabilidad).*

## Métricas de Evaluación para Regresión

Evalúan qué tan cerca están las predicciones numéricas del modelo de los valores reales.

1.  **Mean Absolute Error (MAE - Error Absoluto Medio):**
    *   **¿Qué mide?** El promedio de las diferencias absolutas entre los valores reales y los predichos. `(1/n) * Σ|y_real - y_pred|`
    *   **Función:** `mean_absolute_error(y_true, y_pred)`
    *   **Interpretación:** Está en las **mismas unidades** que la variable objetivo. Un MAE de 5 significa que, en promedio, las predicciones se desvían 5 unidades del valor real. Es menos sensible a outliers que MSE.

    ```python
    mae = mean_absolute_error(y_test_reg, y_pred_reg)
    print(f"\n--- Métricas de Regresión ---")
    print(f"Mean Absolute Error (MAE): {mae:.4f}")
    ```

2.  **Mean Squared Error (MSE - Error Cuadrático Medio):**
    *   **¿Qué mide?** El promedio de las diferencias al cuadrado entre los valores reales y los predichos. `(1/n) * Σ(y_real - y_pred)^2`
    *   **Función:** `mean_squared_error(y_true, y_pred)`
    *   **Interpretación:** Las unidades están **al cuadrado**, lo que lo hace menos interpretable directamente. **Penaliza más los errores grandes** debido al cuadrado. Es comúnmente usado como función de coste a minimizar durante el entrenamiento.

    ```python
    mse = mean_squared_error(y_test_reg, y_pred_reg)
    print(f"Mean Squared Error (MSE): {mse:.4f}")
    ```

3.  **Root Mean Squared Error (RMSE - Raíz del Error Cuadrático Medio):**
    *   **¿Qué mide?** La raíz cuadrada del MSE. `sqrt(MSE)`
    *   **Cálculo:** `np.sqrt(mean_squared_error(y_true, y_pred))`
    *   **Interpretación:** Vuelve a estar en las **mismas unidades** que la variable objetivo, haciéndolo más interpretable que MSE. Representa la desviación estándar de los errores de predicción. Penaliza errores grandes (debido al MSE subyacente).

    ```python
    rmse = np.sqrt(mse) # O mean_squared_error(..., squared=False) en versiones recientes
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
    ```

4.  **R-squared (R² - Coeficiente de Determinación):**
    *   **¿Qué mide?** La **proporción de la varianza** en la variable objetivo que es **explicable** por las características de entrada (el modelo). Varía entre -∞ y 1.
    *   **Función:** `r2_score(y_true, y_pred)`
    *   **Interpretación:**
        *   `R² = 1`: El modelo explica toda la variabilidad (ajuste perfecto).
        *   `R² = 0`: El modelo no explica nada de la variabilidad (equivale a predecir siempre la media).
        *   `R² < 0`: El modelo es peor que simplemente predecir la media.
    *   Un valor más cercano a 1 indica un mejor ajuste del modelo a los datos. Es una métrica relativa.

    ```python
    r2 = r2_score(y_test_reg, y_pred_reg)
    print(f"R-squared (R²): {r2:.4f}")
    ```

Elegir la métrica de evaluación correcta es crucial. No te bases solo en una métrica (especialmente accuracy en clasificación). Considera el contexto del problema, el coste de los diferentes tipos de errores y utiliza varias métricas para obtener una imagen completa del rendimiento de tu modelo.
