# Módulo 6: Preprocesamiento de Datos (Escalado y Codificación)

Los algoritmos de Machine Learning a menudo son sensibles a la **escala** de las características numéricas y no pueden trabajar directamente con **datos categóricos** (texto). Por lo tanto, el **preprocesamiento de datos** es un paso crucial antes de entrenar la mayoría de los modelos.

Scikit-learn ofrece un conjunto de herramientas muy útiles en su módulo `sklearn.preprocessing`.

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder, LabelEncoder
# Necesitaremos train_test_split más adelante, pero lo importamos aquí por contexto
from sklearn.model_selection import train_test_split
```

## ¿Por Qué Preprocesar?

*   **Algoritmos Sensibles a la Escala:** Muchos algoritmos (ej. SVM, K-NN, Redes Neuronales, Regresión Lineal con regularización, PCA) se basan en distancias o gradientes. Si una característica tiene un rango de valores mucho mayor que otras (ej. salario vs. edad), dominará los cálculos y el modelo podría no aprender adecuadamente de las otras características. El **escalado** pone todas las características numéricas en una escala comparable.
*   **Datos Categóricos:** La mayoría de los algoritmos de ML requieren entradas numéricas. Las características categóricas (ej. 'Ciudad', 'Color', 'Tipo de Producto') deben convertirse a una representación numérica. Esto se llama **codificación**.

## Escalado de Características Numéricas (Feature Scaling)

El objetivo es transformar las características numéricas para que tengan un rango o distribución similar. Los métodos más comunes son:

1.  **Estandarización (`StandardScaler`):**
    *   Transforma los datos para que tengan **media 0 y desviación estándar 1**.
    *   Fórmula: `z = (x - media) / desviacion_estandar`
    *   Es útil para algoritmos que asumen una distribución normal (aunque no es estrictamente necesario) o que son sensibles a outliers (ya que no limita el rango).
    *   **Importante:** Se ajusta (`fit`) el scaler **solo** con los datos de **entrenamiento** y luego se usa para transformar (`transform`) tanto los datos de entrenamiento como los de prueba (para evitar fuga de información del conjunto de prueba al de entrenamiento).

2.  **Normalización (Min-Max Scaling - `MinMaxScaler`):**
    *   Transforma los datos para que queden en un rango específico, típicamente **[0, 1]**.
    *   Fórmula: `x_scaled = (x - min) / (max - min)`
    *   Es útil cuando el algoritmo no hace suposiciones sobre la distribución (ej. K-NN) o cuando se necesita un rango acotado.
    *   Es más sensible a outliers que la estandarización.
    *   También se ajusta (`fit`) solo en los datos de entrenamiento.

**Ejemplo de Escalado:**

```python
# Datos numéricos de ejemplo
data = pd.DataFrame({
    'Edad': [25, 42, 31, 55, 22],
    'Salario': [50000, 95000, 62000, 120000, 45000]
})
print("Datos Originales:")
print(data)

# --- StandardScaler ---
scaler_std = StandardScaler()
# Ajustar y transformar (común hacerlo en un paso con fit_transform en entrenamiento)
data_std_scaled = scaler_std.fit_transform(data)
# Convertir de vuelta a DataFrame para mejor visualización
df_std_scaled = pd.DataFrame(data_std_scaled, columns=data.columns, index=data.index)
print("\nDatos Estandarizados (StandardScaler):")
print(df_std_scaled)
print(f"Media después de StandardScaler:\n{df_std_scaled.mean()}") # Cercano a 0
print(f"Desv. Estándar después de StandardScaler:\n{df_std_scaled.std()}") # Cercano a 1

# --- MinMaxScaler ---
scaler_minmax = MinMaxScaler()
data_minmax_scaled = scaler_minmax.fit_transform(data)
df_minmax_scaled = pd.DataFrame(data_minmax_scaled, columns=data.columns, index=data.index)
print("\nDatos Normalizados (MinMaxScaler [0, 1]):")
print(df_minmax_scaled)
print(f"Mínimo después de MinMaxScaler:\n{df_minmax_scaled.min()}") # Cercano a 0
print(f"Máximo después de MinMaxScaler:\n{df_minmax_scaled.max()}") # Cercano a 1

# --- Aplicación en Train/Test Split (Flujo Correcto) ---
# Supongamos que 'data' es nuestro X completo
# X_train, X_test = train_test_split(data, test_size=0.3, random_state=42) # Dividir datos

# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train) # Ajustar y transformar en train
# X_test_scaled = scaler.transform(X_test)       # SOLO transformar en test (usando media/std de train)
```

## Codificación de Características Categóricas

Convertir texto o categorías en números que el modelo pueda entender.

1.  **Codificación One-Hot (`OneHotEncoder`):**
    *   Crea **nuevas columnas binarias (0 o 1)** para cada categoría presente en la característica original.
    *   Si una categoría está presente en una fila, la columna correspondiente tendrá un 1 y las demás un 0.
    *   Es el método **preferido para características nominales** (categorías sin orden intrínseco, ej. 'Ciudad', 'Color') porque no introduce un orden artificial.
    *   Puede generar muchas columnas si la característica tiene muchas categorías (posible "maldición de la dimensionalidad").
    *   **Importante:** Ajustar (`fit`) solo en datos de entrenamiento para conocer todas las categorías posibles y luego transformar (`transform`) ambos conjuntos. Maneja categorías desconocidas en el test set (opcionalmente).

2.  **Codificación de Etiquetas (`LabelEncoder`):**
    *   Asigna un **número entero único** (0, 1, 2, ...) a cada categoría.
    *   **¡Precaución!** Introduce un **orden artificial** entre las categorías (ej. si asigna 0 a 'Rojo', 1 a 'Verde', 2 a 'Azul', el modelo podría interpretar que 'Azul' > 'Verde' > 'Rojo').
    *   **Generalmente NO se recomienda para características de entrada (features)**, a menos que las categorías tengan un orden intrínseco real (características ordinales, ej. 'Bajo', 'Medio', 'Alto').
    *   Se usa comúnmente para codificar la **variable objetivo (la etiqueta `y`)** en problemas de clasificación.

**Ejemplo de Codificación:**

```python
# DataFrame de ejemplo con datos categóricos
data_cat = pd.DataFrame({
    'Color': ['Rojo', 'Verde', 'Azul', 'Verde', 'Rojo'],
    'Talla': ['M', 'L', 'S', 'M', 'L'], # Ordinal (podría usar LabelEncoder con cuidado o OrdinalEncoder)
    'Ciudad': ['Madrid', 'Bcn', 'Sev', 'Madrid', 'Bcn'] # Nominal
})
print("\nDatos Categóricos Originales:")
print(data_cat)

# --- OneHotEncoder (para 'Ciudad' y 'Color' - nominales) ---
# Seleccionar columnas categóricas a codificar
cols_a_codificar = ['Ciudad', 'Color']
datos_nominales = data_cat[cols_a_codificar]

onehot_encoder = OneHotEncoder(sparse_output=False, # Devuelve array denso en lugar de matriz dispersa
                               handle_unknown='ignore') # Ignora categorías no vistas en fit

# Ajustar y transformar
datos_onehot_encoded = onehot_encoder.fit_transform(datos_nominales)

# Obtener nombres de las nuevas columnas
nuevas_columnas_onehot = onehot_encoder.get_feature_names_out(cols_a_codificar)

# Crear DataFrame con los datos codificados
df_onehot = pd.DataFrame(datos_onehot_encoded, columns=nuevas_columnas_onehot, index=data_cat.index)
print("\nDatos Categóricos Codificados (OneHotEncoder):")
print(df_onehot)

# Unir con el resto de columnas (si las hubiera)
# df_final = pd.concat([data_cat.drop(cols_a_codificar, axis=1), df_onehot], axis=1)
# print("\nDataFrame final con OneHot:")
# print(df_final)


# --- LabelEncoder (Ejemplo para 'Talla' - ordinal, o para variable objetivo 'y') ---
label_encoder_talla = LabelEncoder()

# Ajustar y transformar la columna 'Talla'
data_cat['Talla_Encoded'] = label_encoder_talla.fit_transform(data_cat['Talla'])
print("\nDataFrame con LabelEncoder para 'Talla':")
print(data_cat)

# Ver las clases aprendidas por LabelEncoder
print(f"Clases aprendidas por LabelEncoder (Talla): {label_encoder_talla.classes_}")
# Salida: ['L' 'M' 'S'] -> L=0, M=1, S=2 (¡Ojo con este orden si no es el deseado!)
# Para ordinales, sklearn.preprocessing.OrdinalEncoder es más robusto y permite especificar el orden.
```

**Consideraciones:**

*   El preprocesamiento (escalado, codificación) debe hacerse **después** de dividir los datos en conjuntos de entrenamiento y prueba.
*   Ajusta (`fit` o `fit_transform`) los transformadores **solo** con los datos de **entrenamiento**.
*   Aplica la transformación (`transform`) a **ambos** conjuntos (entrenamiento y prueba) usando el mismo objeto transformador ajustado.
*   Scikit-learn ofrece `Pipeline` y `ColumnTransformer` para organizar y aplicar estos pasos de preprocesamiento de forma más sistemática y evitar errores.

El preprocesamiento adecuado es esencial para obtener el mejor rendimiento de tus modelos de Machine Learning. Elegir la técnica correcta (StandardScaler vs. MinMaxScaler, OneHotEncoder vs. LabelEncoder/OrdinalEncoder) depende de los datos y del algoritmo que planeas usar.
