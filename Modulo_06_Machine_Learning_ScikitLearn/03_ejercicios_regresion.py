# Ejercicios: Módulo 6 - Modelos de Regresión (Lineal)

# --- Prerrequisitos ---
# pip install scikit-learn pandas numpy matplotlib
# o
# conda install scikit-learn pandas numpy matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score # Importamos métricas ahora
from sklearn.preprocessing import StandardScaler # Para Ridge/Lasso

# --- Datos de Ejemplo Sintéticos ---
# Crearemos datos donde 'y' depende linealmente de 'X1' y 'X2' con algo de ruido
np.random.seed(0)
n_samples = 150
X1 = 5 * np.random.rand(n_samples, 1)
X2 = 2 * np.random.rand(n_samples, 1) + 3 # Feature con diferente escala
# Relación lineal: y = 2 + 5*X1 - 1.5*X2 + ruido
y = 2 + 5 * X1 - 1.5 * X2 + np.random.randn(n_samples, 1) * 2

# Convertir a DataFrame de Pandas para mejor manejo
X = pd.DataFrame(np.hstack([X1, X2]), columns=['Rendimiento_Motor', 'Peso_Vehiculo'])
y_series = pd.Series(y.ravel(), name='Consumo_Combustible') # .ravel() para convertir a 1D

print("--- Datos Sintéticos para Regresión ---")
print("Primeras filas de X:")
print(X.head())
print("\nPrimeras filas de y:")
print(y_series.head())
print(f"\nForma de X: {X.shape}")
print(f"Forma de y: {y_series.shape}")
print("\n" + "="*30 + "\n")


# --- Ejercicio 1: Regresión Lineal Simple ---
# Instrucciones:
# 1. Selecciona solo la primera característica ('Rendimiento_Motor') como `X_simple`.
# 2. Divide `X_simple` y `y_series` en conjuntos de entrenamiento y prueba (80% train, 20% test, `random_state=42`). Guarda como `X_simple_train`, `X_simple_test`, etc.
# 3. Crea una instancia del modelo `LinearRegression`.
# 4. Entrena el modelo usando `X_simple_train` y `y_train`.
# 5. Imprime el coeficiente (`.coef_`) y el intercepto (`.intercept_`) aprendidos por el modelo. ¿Se acerca el coeficiente al valor esperado (5)?
# 6. Realiza predicciones sobre `X_simple_test` y guárdalas en `y_simple_pred`.
# 7. Calcula e imprime el Error Cuadrático Medio (MSE) y el R-cuadrado (R²) comparando `y_test` con `y_simple_pred`.
# 8. (Opcional) Crea un gráfico de dispersión de `X_simple_test` vs `y_test` y superpón la línea de regresión ( `X_simple_test` vs `y_simple_pred`).

print("--- Ejercicio 1: Regresión Lineal Simple ---")
# Escribe tu código aquí
# 1. Seleccionar una característica
X_simple = X[['Rendimiento_Motor']] # Mantener como DataFrame

# 2. Dividir datos
X_simple_train, X_simple_test, y_train, y_test = train_test_split(
    X_simple, y_series, test_size=0.2, random_state=42
)

# 3. Crear modelo
lin_reg_simple = LinearRegression()

# 4. Entrenar modelo
lin_reg_simple.fit(X_simple_train, y_train)

# 5. Imprimir coeficientes
print(f"Intercepto (b0) aprendido (simple): {lin_reg_simple.intercept_:.4f}")
print(f"Coeficiente (b1) aprendido (simple): {lin_reg_simple.coef_[0]:.4f}")
# Nota: El coeficiente puede no ser exactamente 5 debido al ruido y a la influencia omitida de X2.

# 6. Hacer predicciones
y_simple_pred = lin_reg_simple.predict(X_simple_test)

# 7. Calcular métricas
mse_simple = mean_squared_error(y_test, y_simple_pred)
r2_simple = r2_score(y_test, y_simple_pred)
print(f"\nMSE (simple): {mse_simple:.4f}")
print(f"R² (simple): {r2_simple:.4f}")

# 8. Visualización (Opcional)
plt.figure(figsize=(8, 5))
plt.scatter(X_simple_test, y_test, alpha=0.7, label='Datos Reales (Test)')
plt.plot(X_simple_test, y_simple_pred, color='red', linewidth=2, label='Predicciones (Línea Regresión)')
plt.xlabel('Rendimiento Motor')
plt.ylabel('Consumo Combustible')
plt.title('Regresión Lineal Simple')
plt.legend()
plt.grid(True)
plt.show()
print("-" * 20)


# --- Ejercicio 2: Regresión Lineal Múltiple ---
# Instrucciones:
# 1. Ahora usa el DataFrame `X` completo (con ambas características).
# 2. Divide `X` y `y_series` en conjuntos de entrenamiento y prueba (80% train, 20% test, `random_state=42`). Guarda como `X_multi_train`, `X_multi_test`, etc.
# 3. Crea una nueva instancia de `LinearRegression`.
# 4. Entrena el modelo usando `X_multi_train` y `y_train_multi` (usa las mismas y_train/y_test que antes).
# 5. Imprime el intercepto y los coeficientes (`.coef_`). ¿Se acercan más a los valores originales (b0=2, b1=5, b2=-1.5)?
# 6. Realiza predicciones sobre `X_multi_test` y guárdalas en `y_multi_pred`.
# 7. Calcula e imprime el MSE y R² comparando `y_test` con `y_multi_pred`. ¿Mejoró el rendimiento respecto a la regresión simple?

print("\n--- Ejercicio 2: Regresión Lineal Múltiple ---")
# Escribe tu código aquí
# 1. Usar X completo
# 2. Dividir datos (reutilizamos y_train, y_test del split anterior)
X_multi_train, X_multi_test, y_train_multi, y_test_multi = train_test_split(
    X, y_series, test_size=0.2, random_state=42
)
# Asegurarse de usar las mismas y_train/y_test que en el ejercicio 1 para comparar métricas
y_train_multi = y_train
y_test_multi = y_test

# 3. Crear modelo
lin_reg_multi = LinearRegression()

# 4. Entrenar modelo
lin_reg_multi.fit(X_multi_train, y_train_multi)

# 5. Imprimir coeficientes
print(f"Intercepto (b0) aprendido (múltiple): {lin_reg_multi.intercept_:.4f}") # Cerca de 2
print(f"Coeficientes (b1, b2) aprendidos (múltiple): {lin_reg_multi.coef_}") # Cerca de [5, -1.5]

# 6. Hacer predicciones
y_multi_pred = lin_reg_multi.predict(X_multi_test)

# 7. Calcular métricas
mse_multi = mean_squared_error(y_test_multi, y_multi_pred)
r2_multi = r2_score(y_test_multi, y_multi_pred)
print(f"\nMSE (múltiple): {mse_multi:.4f}")
print(f"R² (múltiple): {r2_multi:.4f}")
print(f"\nComparación R²: Simple={r2_simple:.4f}, Múltiple={r2_multi:.4f}")
print("El modelo múltiple generalmente mejora el rendimiento (R² más alto, MSE más bajo) al incluir más información relevante.")
print("-" * 20)


# --- Ejercicio 3: Regresión Ridge (Regularización L2) ---
# Instrucciones:
# 1. **Importante:** La regularización es sensible a la escala. Escala las características de `X_multi_train` y `X_multi_test` usando `StandardScaler`. Recuerda ajustar el scaler SOLO en el train set. Guarda los resultados escalados.
# 2. Crea una instancia de `Ridge`. El parámetro principal es `alpha`, que controla la fuerza de la regularización (un `alpha` más alto significa más regularización). Empieza con `alpha=1.0`.
# 3. Entrena el modelo Ridge usando los datos de entrenamiento **escalados**.
# 4. Imprime el intercepto y los coeficientes del modelo Ridge. Compara los coeficientes con los de la regresión lineal múltiple. ¿Son más pequeños en magnitud (debido a la penalización)?
# 5. Realiza predicciones sobre los datos de prueba **escalados**.
# 6. Calcula e imprime el MSE y R² para el modelo Ridge. Compara con la regresión lineal múltiple (en este dataset simple, la diferencia puede ser pequeña).

print("\n--- Ejercicio 3: Regresión Ridge (Regularización L2) ---")
# Escribe tu código aquí
# 1. Escalar datos
scaler = StandardScaler()
X_multi_train_scaled = scaler.fit_transform(X_multi_train)
X_multi_test_scaled = scaler.transform(X_multi_test) # Usar el mismo scaler ajustado

# 2. Crear modelo Ridge
ridge_reg = Ridge(alpha=1.0)

# 3. Entrenar modelo Ridge
ridge_reg.fit(X_multi_train_scaled, y_train_multi)

# 4. Imprimir coeficientes
print(f"Intercepto (b0) aprendido (Ridge): {ridge_reg.intercept_:.4f}")
print(f"Coeficientes (b1, b2) aprendidos (Ridge): {ridge_reg.coef_}")
print(f"Coeficientes (b1, b2) aprendidos (Lineal): {lin_reg_multi.coef_}")
# Nota: Los coeficientes de Ridge pueden ser ligeramente menores en magnitud.

# 5. Hacer predicciones
y_ridge_pred = ridge_reg.predict(X_multi_test_scaled)

# 6. Calcular métricas
mse_ridge = mean_squared_error(y_test_multi, y_ridge_pred)
r2_ridge = r2_score(y_test_multi, y_ridge_pred)
print(f"\nMSE (Ridge, alpha=1.0): {mse_ridge:.4f}")
print(f"R² (Ridge, alpha=1.0): {r2_ridge:.4f}")
print(f"Comparación R²: Lineal={r2_multi:.4f}, Ridge={r2_ridge:.4f}")
print("Con alpha=1.0 y datos no muy complejos, la diferencia puede ser mínima.")
print("-" * 20)

# --- Ejercicio 4: Regresión Lasso (Regularización L1) ---
# Instrucciones:
# 1. Crea una instancia de `Lasso` con `alpha=0.1` (Lasso a menudo requiere alphas más pequeños que Ridge).
# 2. Entrena el modelo Lasso usando los datos de entrenamiento **escalados**.
# 3. Imprime el intercepto y los coeficientes del modelo Lasso. ¿Alguno de los coeficientes se ha vuelto cero (o muy cercano a cero)? Esto indica selección de características.
# 4. Realiza predicciones sobre los datos de prueba **escalados**.
# 5. Calcula e imprime el MSE y R² para el modelo Lasso.

print("\n--- Ejercicio 4: Regresión Lasso (Regularización L1) ---")
# Escribe tu código aquí
# 1. Crear modelo Lasso
lasso_reg = Lasso(alpha=0.1)

# 2. Entrenar modelo Lasso
lasso_reg.fit(X_multi_train_scaled, y_train_multi)

# 3. Imprimir coeficientes
print(f"Intercepto (b0) aprendido (Lasso): {lasso_reg.intercept_:.4f}")
print(f"Coeficientes (b1, b2) aprendidos (Lasso): {lasso_reg.coef_}")
# Nota: Con alpha=0.1, es posible que los coeficientes no sean cero aún.
# Prueba aumentar alpha (ej. alpha=1.0) para ver si fuerza algún coeficiente a cero.
# lasso_reg_strong = Lasso(alpha=1.0).fit(X_multi_train_scaled, y_train_multi)
# print(f"Coeficientes (Lasso, alpha=1.0): {lasso_reg_strong.coef_}")

# 4. Hacer predicciones
y_lasso_pred = lasso_reg.predict(X_multi_test_scaled)

# 5. Calcular métricas
mse_lasso = mean_squared_error(y_test_multi, y_lasso_pred)
r2_lasso = r2_score(y_test_multi, y_lasso_pred)
print(f"\nMSE (Lasso, alpha=0.1): {mse_lasso:.4f}")
print(f"R² (Lasso, alpha=0.1): {r2_lasso:.4f}")
print("-" * 20)

# --- Fin de los ejercicios ---
