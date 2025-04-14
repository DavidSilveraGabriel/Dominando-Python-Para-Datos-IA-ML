# Módulo 6: Modelos de Regresión (Lineal, etc.)

La **regresión** es un tipo de tarea de aprendizaje supervisado donde el objetivo es predecir un **valor numérico continuo**. Por ejemplo, predecir el precio de una casa, la temperatura de mañana, o las ventas del próximo mes.

Scikit-learn ofrece varios modelos de regresión. Empezaremos con el más fundamental: la Regresión Lineal.

## Regresión Lineal (`LinearRegression`)

La Regresión Lineal es uno de los algoritmos de ML más simples y conocidos. Asume que existe una **relación lineal** entre las características de entrada (`X`) y la variable objetivo (`y`).

*   **Regresión Lineal Simple:** Hay una sola característica de entrada (`X`). El modelo busca encontrar la línea recta que mejor se ajusta a los datos. La ecuación es: `y = b0 + b1*x`
    *   `b0`: Intercepto (ordenada al origen) - el valor de `y` cuando `x` es 0.
    *   `b1`: Coeficiente (pendiente) - cuánto cambia `y` por cada unidad de cambio en `x`.
*   **Regresión Lineal Múltiple:** Hay múltiples características de entrada (`X1, X2, ..., Xn`). El modelo busca encontrar el hiperplano que mejor se ajusta a los datos. La ecuación es: `y = b0 + b1*x1 + b2*x2 + ... + bn*xn`
    *   `b0`: Intercepto.
    *   `b1, b2, ..., bn`: Coeficientes para cada característica, indican cuánto cambia `y` por un cambio unitario en la característica correspondiente, manteniendo las demás constantes.

El objetivo del algoritmo durante el entrenamiento (`.fit()`) es encontrar los valores de los coeficientes (`b1, ..., bn`) y el intercepto (`b0`) que minimizan la diferencia entre los valores predichos por el modelo y los valores reales de `y` en los datos de entrenamiento (comúnmente minimizando la suma de los errores al cuadrado - Mínimos Cuadrados Ordinarios).

**Ejemplo Básico con Scikit-learn:**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# Importaremos métricas de evaluación más adelante
# from sklearn.metrics import mean_squared_error, r2_score

# 1. Crear Datos Sintéticos (Simulando una relación lineal con ruido)
np.random.seed(42)
X = 2 * np.random.rand(100, 1) # Una característica, 100 muestras
y = 4 + 3 * X + np.random.randn(100, 1) # y = 4 + 3*X + ruido gaussiano

# Visualizar los datos (opcional pero recomendado)
plt.figure(figsize=(8, 5))
plt.scatter(X, y, alpha=0.7)
plt.xlabel("Característica (X)")
plt.ylabel("Etiqueta (y)")
plt.title("Datos Sintéticos para Regresión Lineal")
plt.grid(True)
plt.show()

# 2. Dividir Datos (Aunque con datos sintéticos simples podríamos omitirlo, es buena práctica)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Forma X_train: {X_train.shape}, Forma y_train: {y_train.shape}")
print(f"Forma X_test: {X_test.shape}, Forma y_test: {y_test.shape}")

# 3. Crear y Entrenar el Modelo
lin_reg = LinearRegression() # Instanciar el modelo
lin_reg.fit(X_train, y_train) # Entrenar con datos de entrenamiento

# 4. Inspeccionar el Modelo Entrenado
# El modelo ha aprendido el intercepto (b0) y el coeficiente (b1)
print(f"\nIntercepto (b0) aprendido: {lin_reg.intercept_[0]:.4f}") # Debería estar cerca de 4
print(f"Coeficiente (b1) aprendido: {lin_reg.coef_[0][0]:.4f}")   # Debería estar cerca de 3

# 5. Hacer Predicciones
# Predecir sobre los datos de prueba (no vistos durante el entrenamiento)
y_pred = lin_reg.predict(X_test)

# Predecir para un nuevo valor (ej. X_new = [[1.5]])
X_new = np.array([[1.5]])
y_new_pred = lin_reg.predict(X_new)
print(f"\nPredicción para X = 1.5: {y_new_pred[0][0]:.4f}")
# Esperaríamos algo cercano a 4 + 3 * 1.5 = 8.5

# 6. Visualizar la línea de regresión (opcional)
plt.figure(figsize=(8, 5))
plt.scatter(X_test, y_test, alpha=0.7, label='Datos de Prueba Reales')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicciones (Línea de Regresión)')
plt.xlabel("Característica (X)")
plt.ylabel("Etiqueta (y)")
plt.title("Regresión Lineal - Datos de Prueba vs Predicciones")
plt.legend()
plt.grid(True)
plt.show()

# 7. Evaluación (la veremos en detalle después)
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print(f"\nError Cuadrático Medio (MSE): {mse:.4f}")
# print(f"Coeficiente de Determinación (R^2): {r2:.4f}")
```

## Otros Modelos de Regresión Comunes en Scikit-learn

Scikit-learn ofrece muchas otras variantes y modelos de regresión:

*   **Regresión Ridge (`Ridge`):** Regresión lineal con regularización L2. Ayuda a prevenir el sobreajuste penalizando coeficientes grandes. Útil cuando hay multicolinealidad (características correlacionadas).
*   **Regresión Lasso (`Lasso`):** Regresión lineal con regularización L1. También previene el sobreajuste y, además, puede realizar **selección de características** (tiende a llevar algunos coeficientes exactamente a cero).
*   **Elastic Net (`ElasticNet`):** Combina regularización L1 y L2.
*   **Regresión Polinómica:** No es un modelo diferente, sino que se aplica transformando primero las características originales en características polinómicas (ej. `x^2`, `x^3`, `x1*x2`) usando `PolynomialFeatures` y luego aplicando `LinearRegression` a esas nuevas características. Permite modelar relaciones no lineales.
*   **Support Vector Regression (SVR):** Versión de las Máquinas de Vectores de Soporte para regresión.
*   **Árboles de Decisión para Regresión (`DecisionTreeRegressor`):** Modelos basados en árboles que dividen los datos recursivamente.
*   **Random Forest Regressor (`RandomForestRegressor`):** Ensamblado de múltiples árboles de decisión para mejorar la robustez y reducir el sobreajuste.
*   **Gradient Boosting Regressor (`GradientBoostingRegressor`):** Otro potente método de ensamblado que construye árboles secuencialmente.

La elección del modelo depende de la naturaleza de los datos, la cantidad de características, la presencia de no linealidades y los requisitos específicos del problema. La Regresión Lineal es un excelente punto de partida por su simplicidad e interpretabilidad.
