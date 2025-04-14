# Módulo 6: División de Datos (Train/Test Split)

Uno de los errores más comunes al empezar con Machine Learning es evaluar el modelo usando los mismos datos con los que fue entrenado. Esto lleva a una **evaluación demasiado optimista** del rendimiento, porque el modelo simplemente puede haber "memorizado" los datos de entrenamiento, incluyendo su ruido, en lugar de aprender patrones generalizables.

Para obtener una estimación realista de cómo funcionará tu modelo con datos nuevos y no vistos (que es el objetivo final), necesitas **dividir tu conjunto de datos original** en (al menos) dos partes separadas:

1.  **Conjunto de Entrenamiento (Training Set):** Se utiliza para **entrenar** el modelo. El modelo aprende los patrones y ajusta sus parámetros basándose en estos datos.
2.  **Conjunto de Prueba (Test Set):** Se utiliza para **evaluar** el rendimiento del modelo **después** de que ha sido entrenado. Estos datos deben ser completamente nuevos para el modelo (no deben haberse usado durante el entrenamiento).

## ¿Por Qué Dividir?

*   **Evaluación Imparcial:** Permite medir qué tan bien **generaliza** el modelo a datos que no ha visto antes.
*   **Detección de Sobreajuste (Overfitting):** El sobreajuste ocurre cuando un modelo aprende demasiado bien los datos de entrenamiento (incluyendo el ruido) y, como resultado, funciona mal con datos nuevos. Si un modelo tiene un rendimiento excelente en el conjunto de entrenamiento pero muy pobre en el conjunto de prueba, es una señal clara de sobreajuste.
*   **Ajuste de Hiperparámetros (Hyperparameter Tuning):** A menudo se introduce un tercer conjunto, el **conjunto de validación (validation set)**, o se usa **validación cruzada (cross-validation)** sobre el conjunto de entrenamiento para ajustar los hiperparámetros del modelo (parámetros que no se aprenden directamente de los datos, como la `k` en K-NN o la profundidad de un árbol de decisión) sin "contaminar" el conjunto de prueba final.

## Usando `train_test_split` de Scikit-learn

Scikit-learn proporciona una función muy conveniente, `train_test_split`, para realizar esta división de manera aleatoria.

**Sintaxis:**

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=None
)
```

*   `X`: El array o DataFrame que contiene las **características (features)**.
*   `y`: El array o Serie que contiene las **etiquetas (labels)** (para aprendizaje supervisado).
*   `test_size`: La proporción del dataset que se asignará al conjunto de prueba. Puede ser:
    *   Un número flotante entre 0.0 y 1.0 (ej. `0.3` para 30% de prueba).
    *   Un número entero que representa el número absoluto de muestras de prueba.
    *   Si no se especifica `test_size`, a menudo se usa `train_size` para indicar la proporción de entrenamiento. Si ninguno se especifica, el valor por defecto para `test_size` suele ser 0.25 (25%).
*   `random_state`: Un número entero (seed) para el generador de números aleatorios. Usar un `random_state` fijo asegura que la división sea **reproducible**; cada vez que ejecutes el código con el mismo `random_state`, obtendrás la misma división. Esto es crucial para comparar modelos o depurar. Si es `None`, la división será diferente cada vez. Un valor común es `42`.
*   `stratify`: (Opcional, principalmente para **clasificación**) Si se proporciona `y` (las etiquetas), `stratify=y` asegura que la proporción de las diferentes clases de etiquetas sea aproximadamente la **misma** tanto en el conjunto de entrenamiento como en el de prueba. Esto es muy importante si tienes un **dataset desbalanceado** (una clase es mucho más frecuente que otra).

**Salida:** La función devuelve 4 conjuntos de datos:
*   `X_train`: Características para entrenamiento.
*   `X_test`: Características para prueba.
*   `y_train`: Etiquetas para entrenamiento.
*   `y_test`: Etiquetas para prueba (se usan para comparar con las predicciones del modelo sobre `X_test`).

**Ejemplo:**

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Crear datos de ejemplo (simulados)
np.random.seed(0)
n_samples = 100
X = pd.DataFrame({
    'feature1': np.random.rand(n_samples) * 10,
    'feature2': np.random.rand(n_samples) * 5 + 20,
    'feature3': np.random.randn(n_samples)
})
# Crear una etiqueta 'y' simple para clasificación (ej. basada en feature1)
y = (X['feature1'] > 5).astype(int) # 1 si feature1 > 5, 0 si no

print("Forma de X original:", X.shape)
print("Forma de y original:", y.shape)
print("Distribución de clases en y original:\n", y.value_counts(normalize=True)) # normalize=True da proporciones

# Dividir los datos (70% entrenamiento, 30% prueba)
# Usamos stratify=y para mantener la proporción de clases 0 y 1
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

print("\n--- Después de train_test_split ---")
print("Forma de X_train:", X_train.shape)
print("Forma de X_test:", X_test.shape)
print("Forma de y_train:", y_train.shape)
print("Forma de y_test:", y_test.shape)

print("\nDistribución de clases en y_train:\n", y_train.value_counts(normalize=True))
print("\nDistribución de clases en y_test:\n", y_test.value_counts(normalize=True))
# Notar que las proporciones son muy similares gracias a stratify=y
```

**¡Importante!**

*   La división train/test debe hacerse **antes** de cualquier preprocesamiento que se ajuste a los datos (como `StandardScaler.fit()` o `OneHotEncoder.fit()`). Ajusta los preprocesadores solo en `X_train` y luego úsalos para transformar tanto `X_train` como `X_test`.
*   El conjunto de prueba (`X_test`, `y_test`) solo debe usarse para la **evaluación final** del modelo elegido. No lo uses para tomar decisiones sobre qué modelo elegir o cómo ajustar sus hiperparámetros, ya que eso "contaminaría" la evaluación final. Para eso se usa la validación cruzada o un conjunto de validación separado.

La división adecuada de los datos es un paso fundamental para construir y evaluar modelos de Machine Learning de manera fiable. `train_test_split` es la herramienta estándar para realizar esta tarea en Scikit-learn.
