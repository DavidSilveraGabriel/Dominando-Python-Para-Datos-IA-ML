# Ejercicios: Módulo 6 - Selección de Características y Reducción de Dimensionalidad (PCA)

# --- Prerrequisitos ---
# pip install scikit-learn pandas numpy matplotlib seaborn
# o
# conda install scikit-learn pandas numpy matplotlib seaborn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris # Usaremos el dataset Iris de nuevo

# --- Cargar Datos ---
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name='species')
class_names = iris.target_names

print("--- Dataset Iris Cargado ---")
print("Características Originales (X) - Primeras 5 filas:")
print(X.head())
print(f"\nForma Original de X: {X.shape}") # 4 características
print("\n" + "="*30 + "\n")

# --- Ejercicio 1: Escalado de Datos ---
# Instrucciones:
# 1. PCA es sensible a la escala de las características. Crea una instancia de `StandardScaler`.
# 2. Ajusta y transforma (`fit_transform`) el DataFrame `X` completo usando el scaler. Guarda el resultado en `X_scaled`.
# 3. Imprime las primeras 5 filas de `X_scaled` (será un array NumPy).
# 4. Verifica calculando la media de la primera columna de `X_scaled` (debería ser cercana a 0).

print("--- Ejercicio 1: Escalado de Datos ---")
# Escribe tu código aquí
# 1. Crear scaler
scaler = StandardScaler()

# 2. Ajustar y transformar
X_scaled = scaler.fit_transform(X)

# 3. Imprimir datos escalados (primeras filas)
print("Datos Escalados (X_scaled) - Primeras 5 filas:")
print(X_scaled[:5, :])

# 4. Verificar media (ej. primera columna)
media_col0_scaled = X_scaled[:, 0].mean()
print(f"\nMedia de la primera columna escalada: {media_col0_scaled:.4f} (debería ser cercana a 0)")
print("-" * 20)


# --- Ejercicio 2: Aplicación de PCA ---
# Instrucciones:
# 1. Crea una instancia de `PCA`. Especifica que quieres reducir a 2 componentes principales (`n_components=2`).
# 2. Ajusta (`fit`) el objeto PCA a los datos **escalados** (`X_scaled`).
# 3. Transforma (`transform`) los datos escalados usando el PCA ajustado. Guarda el resultado en `X_pca`.
# 4. Imprime la forma (shape) de `X_pca`. ¿Cuántas dimensiones tiene ahora?
# 5. Imprime la varianza explicada por cada uno de los 2 componentes seleccionados (`pca.explained_variance_ratio_`).
# 6. Imprime la suma de la varianza explicada por estos 2 componentes. ¿Qué porcentaje de la información original (varianza) retienen estos 2 componentes?

print("\n--- Ejercicio 2: Aplicación de PCA ---")
# Escribe tu código aquí
# 1. Crear instancia PCA
pca = PCA(n_components=2)

# 2. Ajustar PCA
pca.fit(X_scaled)
print("PCA ajustado a los datos escalados.")

# 3. Transformar datos
X_pca = pca.transform(X_scaled)

# 4. Imprimir forma resultante
print(f"\nForma de los datos después de PCA: {X_pca.shape}") # Debería ser (n_samples, 2)

# 5. Imprimir varianza explicada por componente
print(f"Varianza explicada por cada componente: {pca.explained_variance_ratio_}")

# 6. Imprimir varianza total explicada
varianza_total = pca.explained_variance_ratio_.sum()
print(f"Varianza total explicada por 2 componentes: {varianza_total:.4f} ({varianza_total*100:.2f}%)")
print("-" * 20)


# --- Ejercicio 3: Visualización de Componentes Principales ---
# Instrucciones:
# 1. Crea un nuevo DataFrame `df_pca` a partir del array `X_pca`. Nombra las columnas 'Componente Principal 1' y 'Componente Principal 2'.
# 2. Añade la columna original de especies (`y`) al `df_pca`. Puedes mapear los números (0, 1, 2) a los nombres de las clases (`class_names`) para la leyenda.
# 3. Usa `seaborn.scatterplot` para crear un gráfico de dispersión:
#    - Eje X: 'Componente Principal 1'
#    - Eje Y: 'Componente Principal 2'
#    - Colorea los puntos (`hue`) según la columna 'species' (con los nombres mapeados).
# 4. Añade un título al gráfico: "Visualización PCA del Dataset Iris (2 Componentes)".
# 5. Muestra el gráfico. ¿Qué observas sobre la separación de las clases en este espacio reducido de 2 dimensiones?

print("\n--- Ejercicio 3: Visualización de Componentes Principales ---")
# Escribe tu código aquí
# 1. Crear DataFrame PCA
df_pca = pd.DataFrame(X_pca, columns=['Componente Principal 1', 'Componente Principal 2'])

# 2. Añadir columna de especies (mapeando a nombres)
df_pca['species'] = y.map({0: class_names[0], 1: class_names[1], 2: class_names[2]})
print("\nDataFrame con Componentes Principales y Especies (primeras filas):")
print(df_pca.head())

# 3. Crear scatter plot con Seaborn
plt.figure(figsize=(9, 7))
sns.scatterplot(
    x='Componente Principal 1',
    y='Componente Principal 2',
    hue='species',
    data=df_pca,
    palette='viridis', # Puedes elegir otra paleta
    alpha=0.8,
    s=70 # Tamaño de los puntos
)

# 4. Añadir título
plt.title("Visualización PCA del Dataset Iris (2 Componentes)")
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.grid(True, linestyle='--', alpha=0.6)

# 5. Mostrar gráfico
plt.show()

print("\nObservación: Se puede ver que los 2 componentes principales capturan una gran parte")
print("de la estructura que separa las clases. La clase 'setosa' está claramente separada,")
print("mientras que 'versicolor' y 'virginica' están más mezcladas, pero aún así muestran")
print("cierta separación en este espacio 2D reducido.")
print("-" * 20)


# --- Ejercicio 4: PCA para determinar número de componentes ---
# Instrucciones:
# 1. Crea una nueva instancia de `PCA` pero esta vez **no especifiques `n_components`** (o ponlo a `None`). Esto calculará todos los componentes posibles (igual al número original de características).
# 2. Ajusta este nuevo PCA a los datos **escalados** (`X_scaled`).
# 3. Calcula la suma acumulada de la varianza explicada por los componentes (`np.cumsum(pca_full.explained_variance_ratio_)`).
# 4. Crea un gráfico de líneas (`plt.plot`) que muestre:
#    - Eje X: Número de componentes (desde 1 hasta el total).
#    - Eje Y: La varianza explicada acumulada calculada en el paso 3.
# 5. Añade una línea horizontal (`plt.axhline`) en y=0.95 (95% de varianza) para referencia.
# 6. Añade etiquetas, título ("Varianza Explicada Acumulada por Componentes") y una cuadrícula.
# 7. Muestra el gráfico. ¿Cuántos componentes parecen ser necesarios para capturar aproximadamente el 95% de la varianza?

print("\n--- Ejercicio 4: PCA para determinar número de componentes ---")
# Escribe tu código aquí
# 1. Crear PCA sin n_components especificado
pca_full = PCA(n_components=None)

# 2. Ajustar PCA
pca_full.fit(X_scaled)
print(f"Número total de componentes calculados: {pca_full.n_components_}")

# 3. Calcular varianza acumulada
varianza_acumulada = np.cumsum(pca_full.explained_variance_ratio_)
print("\nVarianza explicada acumulada:")
print(varianza_acumulada)

# 4. Crear gráfico de líneas
plt.figure(figsize=(8, 5))
num_componentes = range(1, pca_full.n_components_ + 1)
plt.plot(num_componentes, varianza_acumulada, marker='o', linestyle='--')

# 5. Añadir línea de referencia (95%)
plt.axhline(y=0.95, color='red', linestyle=':', label='95% Varianza Explicada')

# 6. Añadir etiquetas, título, etc.
plt.xlabel("Número de Componentes Principales")
plt.ylabel("Varianza Explicada Acumulada")
plt.title("Varianza Explicada Acumulada por Componentes (PCA)")
plt.xticks(num_componentes) # Asegurar ticks para cada número de componente
plt.ylim(0, 1.05) # Ajustar límites Y
plt.grid(True)
plt.legend(loc='best')

# 7. Mostrar gráfico
plt.show()

print("\nObservación del gráfico: Generalmente, se observa que con 2 o 3 componentes")
print("se captura la gran mayoría (más del 95%) de la varianza en el dataset Iris.")
print("-" * 20)


# --- Fin de los ejercicios ---
