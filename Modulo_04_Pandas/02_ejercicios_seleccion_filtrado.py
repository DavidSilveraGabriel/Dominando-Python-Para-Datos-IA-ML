# Ejercicios: Módulo 4 - Selección, Filtrado e Indexación (.loc, .iloc)

import pandas as pd
import numpy as np

# --- DataFrame de Ejemplo ---
# Usaremos un DataFrame similar al de la lección, pero con más datos
np.random.seed(42) # Para reproducibilidad
datos = {
    'Temperatura': np.random.uniform(15, 30, size=8),
    'Humedad': np.random.randint(40, 80, size=8),
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Madrid', 'Valencia', 'Barcelona', 'Bilbao', 'Madrid'],
    'Sensor_ID': [f'S{101+i}' for i in range(8)]
}
indices_fecha = pd.date_range('2024-04-15', periods=8, freq='D')
df = pd.DataFrame(datos, index=indices_fecha)
# Añadimos una columna con valores booleanos para filtrar
df['Alerta'] = df['Temperatura'] > 25

print("DataFrame de Ejemplo:")
print(df)
print("\n" + "="*30 + "\n")

# --- Ejercicio 1: Selección con .loc[] (Etiquetas) ---
# Instrucciones:
# 1. Selecciona e imprime la fila correspondiente a la fecha '2024-04-17'.
# 2. Selecciona e imprime las filas correspondientes a las fechas '2024-04-16' y '2024-04-20'.
# 3. Selecciona e imprime la columna 'Ciudad' completa como una Serie.
# 4. Selecciona e imprime las columnas 'Temperatura' y 'Alerta' como un DataFrame.
# 5. Selecciona e imprime el valor de 'Humedad' para la fecha '2024-04-18'.
# 6. Selecciona e imprime un slice de filas desde '2024-04-16' hasta '2024-04-19' (inclusive)
#    y solo las columnas 'Ciudad' y 'Sensor_ID'.

print("--- Ejercicio 1: Selección con .loc[] ---")
# Escribe tu código aquí
# 1. Fila por etiqueta
print("Fila '2024-04-17':")
print(df.loc['2024-04-17'])
print("-" * 20)

# 2. Múltiples filas por etiqueta
print("Filas '2024-04-16' y '2024-04-20':")
print(df.loc[['2024-04-16', '2024-04-20']])
print("-" * 20)

# 3. Columna por nombre
print("Columna 'Ciudad':")
print(df.loc[:, 'Ciudad'])
print("-" * 20)

# 4. Múltiples columnas por nombre
print("Columnas 'Temperatura' y 'Alerta':")
print(df.loc[:, ['Temperatura', 'Alerta']])
print("-" * 20)

# 5. Valor específico
humedad_18 = df.loc['2024-04-18', 'Humedad']
print(f"Humedad en '2024-04-18': {humedad_18}")
print("-" * 20)

# 6. Slice de filas y columnas
slice_loc = df.loc['2024-04-16':'2024-04-19', ['Ciudad', 'Sensor_ID']]
print("Slice .loc['2024-04-16':'2024-04-19', ['Ciudad', 'Sensor_ID']:")
print(slice_loc)
print("-" * 20)


print("\n--- Ejercicio 2: Selección con .iloc[] (Posición Entera) ---")
# Instrucciones:
# 1. Selecciona e imprime la segunda fila (posición 1).
# 2. Selecciona e imprime las filas en las posiciones 0, 3 y 5.
# 3. Selecciona e imprime la última columna (posición -1) como una Serie.
# 4. Selecciona e imprime las dos primeras columnas (posiciones 0 y 1) como un DataFrame.
# 5. Selecciona e imprime el valor en la tercera fila (posición 2) y la primera columna (posición 0).
# 6. Selecciona e imprime un slice que incluya las filas de la 2 a la 5 (exclusive) y las columnas de la 1 a la 3 (exclusive).

# Escribe tu código aquí
# 1. Fila por posición
print("Segunda fila (iloc[1]):")
print(df.iloc[1])
print("-" * 20)

# 2. Múltiples filas por posición
print("Filas en posiciones 0, 3, 5:")
print(df.iloc[[0, 3, 5]])
print("-" * 20)

# 3. Columna por posición
print("Última columna (iloc[:, -1]):")
print(df.iloc[:, -1])
print("-" * 20)

# 4. Múltiples columnas por posición
print("Primeras dos columnas (iloc[:, [0, 1]] o iloc[:, 0:2]):")
print(df.iloc[:, :2]) # Usando slicing para columnas
print("-" * 20)

# 5. Valor específico por posición
valor_2_0 = df.iloc[2, 0]
print(f"Valor en [2, 0]: {valor_2_0:.2f}") # Formateamos float
print("-" * 20)

# 6. Slice de filas y columnas
slice_iloc = df.iloc[2:5, 1:3] # Filas 2,3,4 y Columnas 1,2
print("Slice .iloc[2:5, 1:3]:")
print(slice_iloc)
print("-" * 20)


print("\n--- Ejercicio 3: Filtrado con Condiciones Booleanas ---")
# Instrucciones:
# 1. Selecciona e imprime todas las filas donde la 'Temperatura' sea mayor a 28 grados.
# 2. Selecciona e imprime todas las filas donde la 'Ciudad' sea 'Madrid'.
# 3. Selecciona e imprime todas las filas donde la 'Humedad' sea menor a 50 Y la 'Alerta' sea True.
# 4. Selecciona e imprime todas las filas donde la 'Ciudad' NO sea 'Barcelona'.
# 5. Selecciona solo las columnas 'Temperatura' y 'Ciudad' para las filas donde la 'Humedad' sea mayor o igual a 70.

# Escribe tu código aquí
# 1. Temperatura > 28
print("Filas con Temperatura > 28:")
print(df.loc[df['Temperatura'] > 28])
print("-" * 20)

# 2. Ciudad == 'Madrid'
print("Filas donde Ciudad es 'Madrid':")
print(df.loc[df['Ciudad'] == 'Madrid'])
print("-" * 20)

# 3. Humedad < 50 Y Alerta == True
print("Filas con Humedad < 50 Y Alerta == True:")
condicion_comb = (df['Humedad'] < 50) & (df['Alerta'] == True) # Alerta ya es booleana
print(df.loc[condicion_comb])
print("-" * 20)

# 4. Ciudad != 'Barcelona'
print("Filas donde Ciudad NO es 'Barcelona':")
print(df.loc[df['Ciudad'] != 'Barcelona'])
print("-" * 20)

# 5. Filtrar filas y seleccionar columnas
print("Columnas Temp y Ciudad donde Humedad >= 70:")
print(df.loc[df['Humedad'] >= 70, ['Temperatura', 'Ciudad']])
print("-" * 20)


# --- Fin de los ejercicios ---
