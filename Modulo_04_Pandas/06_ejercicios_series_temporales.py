# Ejercicios: Módulo 4 - Series Temporales (Básico)

import pandas as pd
import numpy as np

# --- Ejercicio 1: Creación de Fechas y Rangos ---
# Instrucciones:
# 1. Convierte el string '2024-07-15' a un objeto Timestamp de Pandas. Imprímelo y muestra su tipo.
# 2. Crea una lista de strings de fechas: `fechas_str = ['2024/01/10', '2024/01/15', '2024/01/20']`. Conviértela a un DatetimeIndex. Imprímelo.
# 3. Genera un DatetimeIndex con todas las fechas diarias desde '2024-02-25' hasta '2024-03-02' (inclusive) usando `pd.date_range()`. Imprímelo.
# 4. Genera un DatetimeIndex que contenga 6 fechas, comenzando en '2024-05-01' con una frecuencia de días hábiles ('B'). Imprímelo.
# 5. Genera un DatetimeIndex con 4 periodos, comenzando en '2023-12-31', con frecuencia trimestral que termine en el mes ('Q'). Imprímelo.

print("--- Ejercicio 1: Creación de Fechas y Rangos ---")
# Escribe tu código aquí
# 1. Timestamp único
fecha_ts = pd.to_datetime('2024-07-15')
print(f"Timestamp: {fecha_ts}, Tipo: {type(fecha_ts)}")
print("-" * 20)

# 2. DatetimeIndex desde lista
fechas_str = ['2024/01/10', '2024/01/15', '2024/01/20']
idx_fechas = pd.to_datetime(fechas_str)
print("\nDatetimeIndex desde lista:")
print(idx_fechas)
print("-" * 20)

# 3. Rango diario
rango_diario = pd.date_range(start='2024-02-25', end='2024-03-02', freq='D') # freq='D' es el defecto
print("\nRango diario ('2024-02-25' a '2024-03-02'):")
print(rango_diario)
print("-" * 20)

# 4. Rango días hábiles
rango_habiles = pd.date_range(start='2024-05-01', periods=6, freq='B')
print("\nRango de 6 días hábiles desde '2024-05-01':")
print(rango_habiles)
print("-" * 20)

# 5. Rango trimestral
rango_trimestral = pd.date_range(start='2023-12-31', periods=4, freq='Q')
print("\nRango de 4 trimestres desde '2023-12-31':")
print(rango_trimestral)
print("-" * 20)


print("\n--- Ejercicio 2: Creación de Series y DataFrames Temporales ---")
# Instrucciones:
# 1. Crea un DatetimeIndex `idx_temp` con 7 fechas diarias comenzando en '2024-08-10'.
# 2. Crea una Serie `serie_temp` usando `idx_temp` como índice y datos aleatorios generados con `np.random.rand(7)`. Imprime la serie.
# 3. Crea un DataFrame `df_temp` usando `idx_temp` como índice, con dos columnas 'ValorA' y 'ValorB', y datos aleatorios enteros entre 10 y 50 (`np.random.randint(10, 50, size=(7, 2))`). Imprime el DataFrame.

# Escribe tu código aquí
# 1. Crear índice temporal
idx_temp = pd.date_range(start='2024-08-10', periods=7, freq='D')
print("Índice temporal creado:")
print(idx_temp)
print("-" * 20)

# 2. Crear Serie temporal
np.random.seed(0) # Para reproducibilidad
serie_temp = pd.Series(np.random.rand(7), index=idx_temp)
print("\nSerie Temporal:")
print(serie_temp)
print("-" * 20)

# 3. Crear DataFrame temporal
df_temp = pd.DataFrame(np.random.randint(10, 50, size=(7, 2)),
                       index=idx_temp,
                       columns=['ValorA', 'ValorB'])
print("\nDataFrame Temporal:")
print(df_temp)
print("-" * 20)


print("\n--- Ejercicio 3: Indexación y Selección Temporal ---")
# Instrucciones: Usa `serie_temp` y `df_temp` creados en el Ejercicio 2.
# 1. Selecciona e imprime el valor de `serie_temp` para la fecha '2024-08-12'.
# 2. Selecciona e imprime los valores de `serie_temp` para el mes de Agosto de 2024 (`'2024-08'`).
# 3. Selecciona e imprime las filas de `df_temp` desde '2024-08-11' hasta '2024-08-14' (inclusive).
# 4. Selecciona e imprime la columna 'ValorB' de `df_temp` para las fechas '2024-08-15' y '2024-08-16'.

# Escribe tu código aquí
# 1. Seleccionar valor exacto en Serie
valor_fecha = serie_temp['2024-08-12']
print(f"\nValor de la serie en '2024-08-12': {valor_fecha:.4f}")
print("-" * 20)

# 2. Seleccionar por mes en Serie
valores_agosto = serie_temp['2024-08']
print("\nValores de la serie en Agosto 2024:")
print(valores_agosto)
print("-" * 20)

# 3. Seleccionar rango de fechas en DataFrame
slice_df = df_temp.loc['2024-08-11':'2024-08-14']
print("\nFilas del DataFrame desde '2024-08-11' hasta '2024-08-14':")
print(slice_df)
print("-" * 20)

# 4. Seleccionar columna y fechas específicas en DataFrame
valorB_fechas = df_temp.loc[['2024-08-15', '2024-08-16'], 'ValorB']
print("\nColumna 'ValorB' para '2024-08-15' y '2024-08-16':")
print(valorB_fechas)
print("-" * 20)


print("\n--- Ejercicio 4: Funcionalidades Básicas (shift, resample) ---")
# Instrucciones: Usa `serie_temp` y `df_temp`.
# 1. Crea una nueva serie `serie_desplazada` desplazando `serie_temp` un periodo hacia adelante (`shift(1)`). Imprime las primeras 5 filas de ambas series (original y desplazada) para comparar.
# 2. Crea un DataFrame `df_desplazado` desplazando `df_temp` dos periodos hacia atrás (`shift(-2)`). Imprime las últimas 5 filas de ambos DataFrames para comparar.
# 3. (Concepto) Si tuvieras datos diarios en `df_temp` durante varios meses, ¿cómo calcularías la suma mensual de 'ValorA'? (No necesitas ejecutarlo si solo tienes datos de Agosto, solo escribe el código como comentario).

# Escribe tu código aquí
# 1. Desplazar Serie hacia adelante
serie_desplazada = serie_temp.shift(1)
print("\nComparación Serie Original y Desplazada (shift(1)):")
print("Original (head):")
print(serie_temp.head())
print("\nDesplazada (head):")
print(serie_desplazada.head())
print("-" * 20)

# 2. Desplazar DataFrame hacia atrás
df_desplazado = df_temp.shift(-2)
print("\nComparación DataFrame Original y Desplazado (shift(-2)):")
print("Original (tail):")
print(df_temp.tail())
print("\nDesplazado (tail):")
print(df_desplazado.tail())
print("-" * 20)

# 3. Resample (conceptual)
# Para calcular la suma mensual de 'ValorA':
# suma_mensual_A = df_temp['ValorA'].resample('M').sum()
# print("\nSuma Mensual de ValorA (conceptual):")
# print(suma_mensual_A)
print("\nCódigo conceptual para suma mensual de 'ValorA':")
print("# suma_mensual_A = df_temp['ValorA'].resample('M').sum()")
print("-" * 20)

# --- Fin de los ejercicios ---
