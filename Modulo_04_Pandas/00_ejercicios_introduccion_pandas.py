# Ejercicios: Módulo 4 - Introducción a Pandas: Series y DataFrames

# --- Prerrequisito ---
# Asegúrate de tener Pandas y NumPy instalados. Si no, ejecuta en tu terminal:
# pip install pandas numpy
# o
# conda install pandas numpy

import pandas as pd
import numpy as np

print("--- Ejercicio 1: Creación de Series ---")
# Instrucciones:
# 1. Crea una lista de Python `temperaturas = [22.5, 23.1, 19.8, 21.0, 24.5]`.
# 2. Crea una Serie de Pandas `temps_series` a partir de `temperaturas` (con índice por defecto). Imprímela.
# 3. Imprime los valores (`.values`) y el índice (`.index`) de `temps_series`.
# 4. Crea una lista de índices `dias = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie']`.
# 5. Crea una nueva Serie `temps_dias_series` a partir de `temperaturas` pero usando `dias` como índice. Imprímela.
# 6. Crea un diccionario `poblacion = {'Madrid': 3.2, 'Barcelona': 1.6, 'Valencia': 0.8}` (en millones).
# 7. Crea una Serie `poblacion_series` a partir del diccionario. Imprímela.

# Escribe tu código aquí
# 1. Lista
temperaturas = [22.5, 23.1, 19.8, 21.0, 24.5]
print(f"Lista original: {temperaturas}")

# 2. Serie con índice por defecto
temps_series = pd.Series(temperaturas)
print(f"\nSerie con índice por defecto:\n{temps_series}")

# 3. Valores e índice
print(f"\nValores de la Serie: {temps_series.values}")
print(f"Índice de la Serie: {temps_series.index}")

# 4. Lista de índices
dias = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie']
print(f"\nÍndices personalizados: {dias}")

# 5. Serie con índice personalizado
temps_dias_series = pd.Series(temperaturas, index=dias)
print(f"\nSerie con índice de días:\n{temps_dias_series}")

# 6. Diccionario
poblacion = {'Madrid': 3.2, 'Barcelona': 1.6, 'Valencia': 0.8}
print(f"\nDiccionario original: {poblacion}")

# 7. Serie desde diccionario
poblacion_series = pd.Series(poblacion)
print(f"\nSerie desde diccionario:\n{poblacion_series}")


print("\n--- Ejercicio 2: Acceso a Elementos de Series ---")
# Instrucciones: Usando las Series creadas en el Ejercicio 1:
# 1. Accede e imprime el elemento con índice 'Mié' de `temps_dias_series`.
# 2. Accede e imprime el segundo elemento (posición 1) de `temps_series`.
# 3. Accede e imprime la población de 'Barcelona' de `poblacion_series`.
# 4. Obtén un slice de `temps_dias_series` desde 'Mar' hasta 'Jue' (inclusive). Imprímelo.

# Escribe tu código aquí
print(f"Temperatura del Miércoles: {temps_dias_series['Mié']}")
print(f"Temperatura en posición 1 (índice defecto): {temps_series[1]}")
print(f"Población de Barcelona: {poblacion_series['Barcelona']}")
print(f"\nSlice de temperaturas ('Mar':'Jue'):\n{temps_dias_series['Mar':'Jue']}")


print("\n--- Ejercicio 3: Creación de DataFrames ---")
# Instrucciones:
# 1. Crea un diccionario `datos_estudiantes` con las siguientes claves y listas de valores:
#    'Nombre': ['Laura', 'Pedro', 'Marta']
#    'Edad': [21, 23, 20]
#    'Nota': [8.5, 7.8, 9.2]
# 2. Crea un DataFrame `df_estudiantes` a partir del diccionario. Imprímelo.
# 3. Crea un array de NumPy 2D `datos_ventas = np.array([[10, 15], [20, 25], [5, 8]])`.
# 4. Crea un DataFrame `df_ventas` a partir de `datos_ventas`, especificando:
#    - Nombres de columna: ['ProductoA', 'ProductoB']
#    - Nombres de índice (filas): ['Tienda1', 'Tienda2', 'Tienda3']
# 5. Imprime el DataFrame `df_ventas`.

# Escribe tu código aquí
# 1. Diccionario
datos_estudiantes = {
    'Nombre': ['Laura', 'Pedro', 'Marta'],
    'Edad': [21, 23, 20],
    'Nota': [8.5, 7.8, 9.2]
}
print(f"Diccionario estudiantes: {datos_estudiantes}")

# 2. DataFrame desde diccionario
df_estudiantes = pd.DataFrame(datos_estudiantes)
print(f"\nDataFrame Estudiantes:\n{df_estudiantes}")

# 3. Array NumPy
datos_ventas = np.array([[10, 15], [20, 25], [5, 8]])
print(f"\nArray NumPy ventas:\n{datos_ventas}")

# 4. DataFrame desde NumPy con índices/columnas
nombres_col = ['ProductoA', 'ProductoB']
nombres_idx = ['Tienda1', 'Tienda2', 'Tienda3']
df_ventas = pd.DataFrame(datos_ventas, index=nombres_idx, columns=nombres_col)

# 5. Imprimir DataFrame
print(f"\nDataFrame Ventas:\n{df_ventas}")


print("\n--- Ejercicio 4: Exploración Básica de DataFrames ---")
# Instrucciones: Usando el DataFrame `df_estudiantes` del Ejercicio 3:
# 1. Muestra las primeras 2 filas usando `.head()`.
# 2. Muestra la información general del DataFrame usando `.info()`.
# 3. Muestra las estadísticas descriptivas usando `.describe()`.
# 4. Imprime el índice (`.index`).
# 5. Imprime las columnas (`.columns`).
# 6. Selecciona e imprime solo la columna 'Nombre' (esto devolverá una Serie).
# 7. Selecciona e imprime las columnas 'Nombre' y 'Nota' (esto devolverá un DataFrame).

# Escribe tu código aquí
print("Explorando df_estudiantes:")
print("\nPrimeras 2 filas (head):")
print(df_estudiantes.head(2))

print("\nInformación general (info):")
df_estudiantes.info()

print("\nEstadísticas descriptivas (describe):")
print(df_estudiantes.describe())

print(f"\nÍndice: {df_estudiantes.index}")
print(f"Columnas: {df_estudiantes.columns}")

print("\nColumna 'Nombre' (Serie):")
print(df_estudiantes['Nombre'])

print("\nColumnas 'Nombre' y 'Nota' (DataFrame):")
print(df_estudiantes[['Nombre', 'Nota']])


# --- Fin de los ejercicios ---
