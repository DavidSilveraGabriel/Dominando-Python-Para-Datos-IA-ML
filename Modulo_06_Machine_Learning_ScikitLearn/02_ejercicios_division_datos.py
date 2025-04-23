# Ejercicios: Módulo 6 - División de Datos (Train/Test Split)

# --- Prerrequisitos ---
# pip install scikit-learn pandas numpy
# o
# conda install scikit-learn pandas numpy

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# --- Datos de Ejemplo ---
# Crearemos un dataset más grande para ver mejor el efecto de la división
np.random.seed(0)
n_samples = 200
X = pd.DataFrame({
    'feature_A': np.random.rand(n_samples) * 100,
    'feature_B': np.random.normal(50, 15, n_samples),
    'feature_C': np.random.randint(0, 10, n_samples)
})
# Crear una etiqueta 'y' para clasificación (desbalanceada a propósito)
# Clase 0 será más frecuente que Clase 1
prob_clase_1 = 0.2 # 20% de probabilidad de ser clase 1
y = (np.random.rand(n_samples) < prob_clase_1).astype(int)
y_series = pd.Series(y, name='Target') # Convertir a Serie de Pandas

print("--- Datos Originales ---")
print("Primeras filas de X:")
print(X.head())
print("\nPrimeras filas de y:")
print(y_series.head())
print(f"\nForma de X original: {X.shape}")
print(f"Forma de y original: {y_series.shape}")
print("\nDistribución de clases en y original:")
print(y_series.value_counts(normalize=True)) # normalize=True muestra proporciones
print("\n" + "="*30 + "\n")


# --- Ejercicio 1: División Simple (Train/Test) ---
# Instrucciones:
# 1. Usa `train_test_split` para dividir `X` y `y_series` en conjuntos de entrenamiento y prueba.
# 2. Asigna el 20% de los datos al conjunto de prueba (`test_size=0.2`).
# 3. Usa `random_state=42` para asegurar que la división sea reproducible.
# 4. Guarda los resultados en `X_train`, `X_test`, `y_train`, `y_test`.
# 5. Imprime las formas (shapes) de los cuatro conjuntos de datos resultantes para verificar los tamaños.

print("--- Ejercicio 1: División Simple (Train/Test) ---")
# Escribe tu código aquí
# 1, 2, 3, 4. Dividir los datos
X_train, X_test, y_train, y_test = train_test_split(
    X, y_series, test_size=0.2, random_state=42
)

# 5. Imprimir formas
print(f"Forma de X_train: {X_train.shape}")
print(f"Forma de X_test: {X_test.shape}")
print(f"Forma de y_train: {y_train.shape}")
print(f"Forma de y_test: {y_test.shape}")

# Verificar proporciones (sin stratify, pueden variar)
print("\nDistribución de clases en y_train (sin stratify):")
print(y_train.value_counts(normalize=True))
print("\nDistribución de clases en y_test (sin stratify):")
print(y_test.value_counts(normalize=True))
print("-" * 20)


# --- Ejercicio 2: División Estratificada ---
# Instrucciones:
# 1. Vuelve a dividir `X` y `y_series` usando `train_test_split`.
# 2. Usa de nuevo `test_size=0.2` y `random_state=42`.
# 3. **Añade el argumento `stratify=y_series`** para asegurar que la proporción de clases sea la misma en los conjuntos de entrenamiento y prueba.
# 4. Guarda los resultados en `X_train_strat`, `X_test_strat`, `y_train_strat`, `y_test_strat`.
# 5. Imprime las formas de los cuatro conjuntos resultantes.
# 6. Imprime la distribución de clases (proporciones) en `y_train_strat` y `y_test_strat`. Compara estas proporciones con las del dataset original y con las del Ejercicio 1. ¿Qué observas?

print("\n--- Ejercicio 2: División Estratificada ---")
# Escribe tu código aquí
# 1, 2, 3, 4. Dividir los datos con stratify
X_train_strat, X_test_strat, y_train_strat, y_test_strat = train_test_split(
    X, y_series, test_size=0.2, random_state=42, stratify=y_series
)

# 5. Imprimir formas
print(f"Forma de X_train_strat: {X_train_strat.shape}")
print(f"Forma de X_test_strat: {X_test_strat.shape}")
print(f"Forma de y_train_strat: {y_train_strat.shape}")
print(f"Forma de y_test_strat: {y_test_strat.shape}")

# 6. Imprimir distribución de clases
print("\nDistribución de clases en y_train (con stratify):")
print(y_train_strat.value_counts(normalize=True))
print("\nDistribución de clases en y_test (con stratify):")
print(y_test_strat.value_counts(normalize=True))

print("\nObservación: Al usar 'stratify=y', las proporciones de la clase 0 y la clase 1")
print("en los conjuntos de entrenamiento y prueba son casi idénticas a las del")
print("conjunto de datos original. Esto es especialmente importante en datasets")
print("desbalanceados para asegurar que ambos conjuntos sean representativos.")
print("-" * 20)


# --- Ejercicio 3: Importancia del `random_state` ---
# Instrucciones:
# 1. Ejecuta `train_test_split` dos veces sobre `X` y `y_series` con los mismos parámetros (`test_size=0.3`), pero **sin** especificar `random_state` en ninguna de las llamadas.
# 2. Guarda los resultados de la primera llamada en `X_train1`, `X_test1`, `y_train1`, `y_test1`.
# 3. Guarda los resultados de la segunda llamada en `X_train2`, `X_test2`, `y_train2`, `y_test2`.
# 4. Compara si `X_train1` es igual a `X_train2` usando `X_train1.equals(X_train2)`. Imprime el resultado. ¿Son iguales?
# 5. Ahora, ejecuta `train_test_split` dos veces más, pero esta vez **especifica `random_state=123`** en ambas llamadas.
# 6. Guarda los resultados en `X_train3`, `X_test3`, ... y `X_train4`, `X_test4`, ...
# 7. Compara si `X_train3` es igual a `X_train4` usando `X_train3.equals(X_train4)`. Imprime el resultado. ¿Son iguales ahora?
# 8. Comenta por qué es importante usar `random_state` en la práctica.

print("\n--- Ejercicio 3: Importancia del `random_state` ---")
# Escribe tu código aquí
# 1, 2, 3. Primera división sin random_state
X_train1, X_test1, y_train1, y_test1 = train_test_split(X, y_series, test_size=0.3)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X, y_series, test_size=0.3)

# 4. Comparar (sin random_state)
son_iguales12 = X_train1.equals(X_train2)
print(f"¿Son iguales X_train1 y X_train2 (sin random_state)? {son_iguales12}")

# 5, 6. Divisiones con random_state=123
X_train3, X_test3, y_train3, y_test3 = train_test_split(X, y_series, test_size=0.3, random_state=123)
X_train4, X_test4, y_train4, y_test4 = train_test_split(X, y_series, test_size=0.3, random_state=123)

# 7. Comparar (con random_state)
son_iguales34 = X_train3.equals(X_train4)
print(f"¿Son iguales X_train3 y X_train4 (con random_state=123)? {son_iguales34}")

# 8. Comentario
print("\nImportancia de random_state:")
print("Usar un valor fijo para 'random_state' asegura que la división aleatoria")
print("sea siempre la misma cada vez que se ejecuta el código. Esto es crucial para:")
print(" - Reproducibilidad: Otros (o tú mismo en el futuro) pueden obtener los mismos resultados.")
print(" - Depuración: Si algo va mal, puedes estar seguro de que no es por una división diferente.")
print(" - Comparación justa: Al comparar diferentes modelos o hiperparámetros, te aseguras")
print("   de que todos se entrenan y evalúan con exactamente la misma división de datos.")
print("-" * 20)

# --- Fin de los ejercicios ---
