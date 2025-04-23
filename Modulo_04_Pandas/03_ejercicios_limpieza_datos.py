# Ejercicios: Módulo 4 - Limpieza de Datos (Valores Nulos y Duplicados)

import pandas as pd
import numpy as np

# --- DataFrame de Ejemplo con Nulos y Duplicados ---
datos = {
    'ID_Usuario': [101, 102, 103, 101, 104, 105, 106, np.nan],
    'Nombre': ['Ana', 'Luis', 'Eva', 'Ana', 'Juan', 'Sofía', None, 'Pedro'],
    'Edad': [25, 30, np.nan, 25, 40, 35, np.nan, 28],
    'Ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Madrid', 'Valencia', np.nan, 'Bilbao', 'Barcelona'],
    'Puntuacion': [8.5, 7.0, 9.0, 8.5, 6.5, np.nan, 7.5, 8.0]
}
df = pd.DataFrame(datos)

print("DataFrame Original (con nulos y duplicados):")
print(df)
print("\n" + "="*30 + "\n")

# --- Ejercicio 1: Detección y Conteo de Nulos ---
# Instrucciones:
# 1. Usa `.isnull()` (o `.isna()`) para obtener un DataFrame booleano indicando la presencia de valores nulos. Imprímelo.
# 2. Usa `.isnull().sum()` para contar cuántos valores nulos hay en CADA columna. Imprime el resultado (es una Serie).
# 3. Calcula e imprime el número TOTAL de valores nulos en todo el DataFrame.

print("--- Ejercicio 1: Detección y Conteo de Nulos ---")
# Escribe tu código aquí
# 1. Detectar nulos
print("DataFrame booleano de nulos (isnull):")
print(df.isnull())
print("-" * 20)

# 2. Contar nulos por columna
print("\nConteo de nulos por columna:")
print(df.isnull().sum())
print("-" * 20)

# 3. Contar nulos totales
total_nulos = df.isnull().sum().sum()
print(f"\nNúmero total de valores nulos: {total_nulos}")
print("-" * 20)


print("\n--- Ejercicio 2: Eliminación de Nulos (`dropna`) ---")
# Instrucciones: (Trabaja con copias para no modificar `df` permanentemente aquí)
# 1. Crea una copia de `df` llamada `df_sin_filas_nan`. Elimina todas las FILAS que contengan al menos un valor nulo. Imprime el resultado.
# 2. Crea una copia de `df` llamada `df_sin_cols_nan`. Elimina todas las COLUMNAS que contengan al menos un valor nulo. Imprime el resultado.
# 3. Crea una copia de `df` llamada `df_sin_nan_edad`. Elimina solo las filas donde la columna 'Edad' sea nula. Imprime el resultado.

# Escribe tu código aquí
# 1. Eliminar filas con algún NaN
df_sin_filas_nan = df.dropna() # axis=0 es el defecto
print("DataFrame después de eliminar filas con algún NaN:")
print(df_sin_filas_nan)
print("-" * 20)

# 2. Eliminar columnas con algún NaN
df_sin_cols_nan = df.dropna(axis=1)
print("\nDataFrame después de eliminar columnas con algún NaN:")
print(df_sin_cols_nan)
print("-" * 20)

# 3. Eliminar filas con NaN en 'Edad'
df_sin_nan_edad = df.dropna(subset=['Edad'])
print("\nDataFrame después de eliminar filas con NaN en 'Edad':")
print(df_sin_nan_edad)
print("-" * 20)


print("\n--- Ejercicio 3: Relleno de Nulos (`fillna`) ---")
# Instrucciones: (Trabaja con copias)
# 1. Crea una copia de `df` llamada `df_relleno`.
# 2. Rellena los valores nulos en la columna 'Edad' con la media de esa columna. Imprime el DataFrame modificado.
# 3. Rellena los valores nulos en la columna 'Ciudad' con la cadena 'Desconocida'. Imprime el DataFrame modificado.
# 4. Rellena los valores nulos en la columna 'Puntuacion' usando forward fill (`method='ffill'`). Imprime el DataFrame modificado.
# 5. Rellena TODOS los nulos restantes en el DataFrame con el valor 0. Imprime el resultado final.

# Escribe tu código aquí
df_relleno = df.copy()
print("DataFrame original para rellenar:")
print(df_relleno)
print("-" * 20)

# 2. Rellenar Edad con la media
media_edad = df_relleno['Edad'].mean()
print(f"\nMedia de Edad: {media_edad:.2f}")
df_relleno['Edad'].fillna(media_edad, inplace=True)
print("DataFrame con Edad NaN rellenada con la media:")
print(df_relleno)
print("-" * 20)

# 3. Rellenar Ciudad con 'Desconocida'
df_relleno['Ciudad'].fillna('Desconocida', inplace=True)
print("\nDataFrame con Ciudad NaN rellenada con 'Desconocida':")
print(df_relleno)
print("-" * 20)

# 4. Rellenar Puntuacion con ffill
df_relleno['Puntuacion'].fillna(method='ffill', inplace=True)
print("\nDataFrame con Puntuacion NaN rellenada con ffill:")
print(df_relleno)
print("-" * 20)

# 5. Rellenar nulos restantes (ID_Usuario, Nombre) con 0
# Nota: Rellenar Nombre con 0 puede no ser ideal, pero es para el ejercicio.
# ID_Usuario podría ser rellenado con un valor único si fuera necesario.
df_relleno.fillna(0, inplace=True)
print("\nDataFrame con todos los NaN restantes rellenados con 0:")
print(df_relleno)
print("-" * 20)


print("\n--- Ejercicio 4: Detección y Eliminación de Duplicados ---")
# Instrucciones: (Usa el `df` original)
# 1. Verifica si hay filas completamente duplicadas en `df`. Imprime la Serie booleana resultante.
# 2. Cuenta cuántas filas duplicadas hay (sin contar la primera ocurrencia).
# 3. Verifica si hay duplicados basados solo en la columna 'ID_Usuario'. Imprime la Serie booleana.
# 4. Crea un nuevo DataFrame `df_sin_duplicados` eliminando las filas completamente duplicadas, manteniendo la primera ocurrencia. Imprime el resultado.
# 5. Crea un nuevo DataFrame `df_sin_dup_id` eliminando las filas duplicadas basándose solo en 'ID_Usuario', pero manteniendo la última ocurrencia. Imprime el resultado.

# Escribe tu código aquí
print("DataFrame original para duplicados:")
print(df)
print("-" * 20)

# 1. Detectar duplicados completos
print("\n¿Filas completamente duplicadas? (keep='first')")
print(df.duplicated())
print("-" * 20)

# 2. Contar duplicados completos
num_duplicados = df.duplicated().sum()
print(f"\nNúmero de filas completamente duplicadas (excl. primera): {num_duplicados}")
print("-" * 20)

# 3. Detectar duplicados en 'ID_Usuario'
print("\n¿Filas duplicadas en 'ID_Usuario'? (keep='first')")
print(df.duplicated(subset=['ID_Usuario']))
print("-" * 20)

# 4. Eliminar duplicados completos (keep='first')
df_sin_duplicados = df.drop_duplicates(keep='first')
print("\nDataFrame sin duplicados completos (keep='first'):")
print(df_sin_duplicados)
print("-" * 20)

# 5. Eliminar duplicados por ID (keep='last')
df_sin_dup_id = df.drop_duplicates(subset=['ID_Usuario'], keep='last')
print("\nDataFrame sin duplicados en 'ID_Usuario' (keep='last'):")
print(df_sin_dup_id)
print("-" * 20)

# --- Fin de los ejercicios ---
