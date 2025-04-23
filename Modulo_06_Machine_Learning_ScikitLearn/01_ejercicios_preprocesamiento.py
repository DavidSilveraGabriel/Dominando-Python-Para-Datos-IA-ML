# Ejercicios: Módulo 6 - Preprocesamiento de Datos (Escalado y Codificación)

# --- Prerrequisitos ---
# pip install scikit-learn pandas numpy
# o
# conda install scikit-learn pandas numpy

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split # Para el ejercicio 3

# --- Datos de Ejemplo ---
# Combinaremos datos numéricos y categóricos
data_ejemplo = pd.DataFrame({
    'Edad': [25, 42, 31, 55, 22, 38, 45, 29],
    'Ingresos_Anuales': [50000, 95000, 62000, 120000, 45000, 75000, 110000, 58000],
    'Experiencia_Anios': [2, 15, 5, 25, 1, 10, 18, 4],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Madrid', 'Valencia', 'Barcelona', 'Madrid', 'Sevilla'],
    'Nivel_Estudios': ['Master', 'Grado', 'Master', 'Doctorado', 'Grado', 'Master', 'Doctorado', 'Grado'] # Ordinal?
})

print("--- DataFrame Original ---")
print(data_ejemplo)
print("\nTipos de datos originales:")
print(data_ejemplo.dtypes)
print("\n" + "="*30 + "\n")

# Separar características numéricas y categóricas
features_numericas = ['Edad', 'Ingresos_Anuales', 'Experiencia_Anios']
features_categoricas = ['Ciudad', 'Nivel_Estudios']

X_num = data_ejemplo[features_numericas]
X_cat = data_ejemplo[features_categoricas]

# --- Ejercicio 1: Escalado de Características Numéricas ---
# Instrucciones:
# 1. Crea una instancia de `StandardScaler`.
# 2. Ajusta (`fit`) el scaler a los datos numéricos (`X_num`).
# 3. Transforma (`transform`) los datos numéricos usando el scaler ajustado. Guarda el resultado en `X_num_std_scaled`.
# 4. Convierte `X_num_std_scaled` (que es un array NumPy) de nuevo a un DataFrame de Pandas con las columnas originales para facilitar la visualización. Imprímelo.
# 5. Calcula e imprime la media y la desviación estándar de cada columna del DataFrame escalado (deberían ser cercanas a 0 y 1 respectivamente).
# 6. Repite los pasos 1-5 usando `MinMaxScaler` (guarda en `X_num_minmax_scaled`). Calcula e imprime el mínimo y máximo de cada columna escalada (deberían ser 0 y 1).

print("--- Ejercicio 1: Escalado de Características Numéricas ---")
# Escribe tu código aquí

# StandardScaler
print("--- StandardScaler ---")
# 1. Crear instancia
scaler_std = StandardScaler()
# 2. Ajustar
scaler_std.fit(X_num)
# 3. Transformar
X_num_std_scaled_array = scaler_std.transform(X_num)
# 4. Convertir a DataFrame
X_num_std_scaled = pd.DataFrame(X_num_std_scaled_array, columns=features_numericas, index=X_num.index)
print("Datos Numéricos Estandarizados:")
print(X_num_std_scaled)
# 5. Verificar media y desviación estándar
print("\nMedia (StandardScaler):")
print(X_num_std_scaled.mean())
print("\nDesviación Estándar (StandardScaler):")
print(X_num_std_scaled.std())
print("-" * 20)

# MinMaxScaler
print("\n--- MinMaxScaler ---")
# 1. Crear instancia
scaler_minmax = MinMaxScaler()
# 2. Ajustar
scaler_minmax.fit(X_num)
# 3. Transformar
X_num_minmax_scaled_array = scaler_minmax.transform(X_num)
# 4. Convertir a DataFrame
X_num_minmax_scaled = pd.DataFrame(X_num_minmax_scaled_array, columns=features_numericas, index=X_num.index)
print("Datos Numéricos Normalizados (0-1):")
print(X_num_minmax_scaled)
# 5. Verificar mínimo y máximo
print("\nMínimo (MinMaxScaler):")
print(X_num_minmax_scaled.min())
print("\nMáximo (MinMaxScaler):")
print(X_num_minmax_scaled.max())
print("-" * 20)


# --- Ejercicio 2: Codificación de Características Categóricas ---
# Instrucciones:
# 1. Crea una instancia de `OneHotEncoder`. Configúralo para que devuelva un array denso (`sparse_output=False`) y maneje categorías desconocidas (`handle_unknown='ignore'`).
# 2. Ajusta y transforma (`fit_transform`) la columna 'Ciudad' (que es nominal) usando el OneHotEncoder.
# 3. Obtén los nombres de las nuevas columnas generadas usando `get_feature_names_out(['Ciudad'])`.
# 4. Crea un DataFrame `df_ciudad_onehot` con los datos codificados y los nombres de columna obtenidos. Imprímelo.
# 5. Crea una instancia de `LabelEncoder`.
# 6. Ajusta y transforma (`fit_transform`) la columna 'Nivel_Estudios'. Guarda el resultado en una nueva columna en `data_ejemplo` llamada 'Nivel_Estudios_Encoded'.
# 7. Imprime las clases aprendidas por el LabelEncoder (`label_encoder.classes_`). ¿El orden asignado (0, 1, 2...) tiene sentido si consideramos 'Nivel_Estudios' como ordinal? (Comenta tu respuesta).
# 8. Imprime las primeras 5 filas de `data_ejemplo` para ver la nueva columna codificada.

print("\n--- Ejercicio 2: Codificación de Características Categóricas ---")
# Escribe tu código aquí

# OneHotEncoder para 'Ciudad'
print("--- OneHotEncoder ('Ciudad') ---")
# 1. Crear instancia
onehot_encoder_ciudad = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
# 2. Ajustar y transformar
ciudad_encoded_array = onehot_encoder_ciudad.fit_transform(X_cat[['Ciudad']]) # Pasar como DataFrame
# 3. Obtener nombres de columnas
nombres_onehot_ciudad = onehot_encoder_ciudad.get_feature_names_out(['Ciudad'])
# 4. Crear DataFrame
df_ciudad_onehot = pd.DataFrame(ciudad_encoded_array, columns=nombres_onehot_ciudad, index=X_cat.index)
print("Columna 'Ciudad' Codificada (One-Hot):")
print(df_ciudad_onehot)
print("-" * 20)

# LabelEncoder para 'Nivel_Estudios'
print("\n--- LabelEncoder ('Nivel_Estudios') ---")
# 5. Crear instancia
label_encoder_estudios = LabelEncoder()
# 6. Ajustar y transformar
data_ejemplo['Nivel_Estudios_Encoded'] = label_encoder_estudios.fit_transform(data_ejemplo['Nivel_Estudios'])
# 7. Imprimir clases y comentar
print("Clases aprendidas por LabelEncoder ('Nivel_Estudios'):", label_encoder_estudios.classes_)
# Comentario: El orden asignado es ['Doctorado' 'Grado' 'Master'], lo que corresponde a 0, 1, 2.
# Este orden alfabético NO necesariamente refleja el orden jerárquico natural (Grado < Master < Doctorado).
# Por lo tanto, LabelEncoder no es ideal aquí si queremos preservar el orden.
# Sería mejor usar OrdinalEncoder especificando el orden correcto de las categorías.
# 8. Imprimir DataFrame con la nueva columna
print("\nDataFrame original con 'Nivel_Estudios_Encoded':")
print(data_ejemplo.head())
print("-" * 20)


# --- Ejercicio 3: Aplicación Correcta en Train/Test Split ---
# Instrucciones:
# Este ejercicio es más conceptual para reforzar el flujo correcto.
# 1. Divide `X_num` en conjuntos de entrenamiento y prueba (`X_num_train`, `X_num_test`) usando `train_test_split`. Usa `test_size=0.25` y `random_state=42`.
# 2. Crea una NUEVA instancia de `StandardScaler`.
# 3. Ajusta (`fit`) este nuevo scaler **SOLAMENTE** a `X_num_train`.
# 4. Transforma (`transform`) **TANTO** `X_num_train` como `X_num_test` usando el scaler ajustado en el paso 3. Guarda los resultados en `X_num_train_scaled` y `X_num_test_scaled`.
# 5. Imprime las formas (shapes) de los 4 DataFrames/arrays resultantes (`X_num_train`, `X_num_test`, `X_num_train_scaled`, `X_num_test_scaled`).
# 6. Calcula e imprime la media de `X_num_train_scaled` (debería ser cercana a 0).
# 7. Calcula e imprime la media de `X_num_test_scaled` (NO necesariamente será 0, ya que se usó la media/std del train set).

print("\n--- Ejercicio 3: Aplicación Correcta en Train/Test Split ---")
# Escribe tu código aquí
# 1. Dividir datos numéricos
X_num_train, X_num_test = train_test_split(X_num, test_size=0.25, random_state=42)

# 2. Crear nueva instancia de StandardScaler
scaler_split = StandardScaler()

# 3. Ajustar SOLO en train
scaler_split.fit(X_num_train)

# 4. Transformar train y test
X_num_train_scaled = scaler_split.transform(X_num_train)
X_num_test_scaled = scaler_split.transform(X_num_test)

# 5. Imprimir formas
print(f"Forma X_num_train: {X_num_train.shape}")
print(f"Forma X_num_test: {X_num_test.shape}")
print(f"Forma X_num_train_scaled: {X_num_train_scaled.shape}")
print(f"Forma X_num_test_scaled: {X_num_test_scaled.shape}")

# 6. Media del train set escalado
print("\nMedia de X_num_train_scaled (columnas):")
print(X_num_train_scaled.mean(axis=0)) # axis=0 calcula la media por columna

# 7. Media del test set escalado
print("\nMedia de X_num_test_scaled (columnas):")
print(X_num_test_scaled.mean(axis=0)) # No tiene por qué ser 0

print("\nRecordatorio: El ajuste (fit) se hace solo en los datos de entrenamiento.")
print("-" * 20)

# --- Fin de los ejercicios ---
