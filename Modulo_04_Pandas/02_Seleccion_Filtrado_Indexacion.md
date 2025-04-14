# Módulo 4: Selección, Filtrado e Indexación (`.loc`, `.iloc`)

Una vez que tienes tus datos cargados en un DataFrame, la tarea más común es seleccionar subconjuntos específicos de esos datos para analizarlos o modificarlos. Pandas ofrece varias formas de hacerlo, pero las dos más importantes y recomendadas son los **accesores de índice**:

*   **`.loc[]`**: Selección basada en **etiquetas** (labels) del índice y nombres de columna.
*   **`.iloc[]`**: Selección basada en la **posición entera** (integer position) de las filas y columnas (empezando desde 0, como en NumPy o listas).

Entender la diferencia entre `.loc` e `.iloc` es fundamental para usar Pandas eficazmente.

```python
import pandas as pd
import numpy as np

# DataFrame de ejemplo
datos = {
    'ColA': [10, 20, 30, 40, 50],
    'ColB': [100, 200, 300, 400, 500],
    'ColC': ['p', 'q', 'r', 's', 't']
}
indices = ['idx1', 'idx2', 'idx3', 'idx4', 'idx5']
df = pd.DataFrame(datos, index=indices)

print("DataFrame de ejemplo:")
print(df)
print("\n")
```

## Selección con `.loc[]` (Basada en Etiquetas)

`.loc[]` se utiliza para seleccionar datos usando las **etiquetas** del índice (nombres de fila) y los **nombres** de las columnas.

**Sintaxis:**

*   `df.loc[etiqueta_fila]` : Selecciona una fila completa como una Serie.
*   `df.loc[[lista_etiquetas_fila]]` : Selecciona múltiples filas como un DataFrame.
*   `df.loc[:, nombre_columna]` : Selecciona una columna completa como una Serie.
*   `df.loc[:, [lista_nombres_columna]]` : Selecciona múltiples columnas como un DataFrame.
*   `df.loc[etiqueta_fila, nombre_columna]` : Selecciona un valor escalar específico.
*   `df.loc[slice_etiquetas_fila, slice_nombres_columna]` : Selecciona un subconjunto rectangular. **Importante:** ¡El slicing con etiquetas en `.loc` **incluye** el valor final (`stop`)!

**Ejemplos con `.loc[]`:**

```python
print("--- Selección con .loc[] ---")

# Seleccionar fila por etiqueta 'idx2'
fila_idx2 = df.loc['idx2']
print(f"Fila 'idx2' (Serie):\n{fila_idx2}\n")

# Seleccionar filas 'idx1' e 'idx4'
filas_1_4 = df.loc[['idx1', 'idx4']]
print(f"Filas 'idx1' e 'idx4' (DataFrame):\n{filas_1_4}\n")

# Seleccionar columna 'ColB'
col_b = df.loc[:, 'ColB']
print(f"Columna 'ColB' (Serie):\n{col_b}\n")

# Seleccionar columnas 'ColA' y 'ColC'
cols_a_c = df.loc[:, ['ColA', 'ColC']]
print(f"Columnas 'ColA' y 'ColC' (DataFrame):\n{cols_a_c}\n")

# Seleccionar valor específico en fila 'idx3', columna 'ColB'
valor_3_b = df.loc['idx3', 'ColB']
print(f"Valor en ['idx3', 'ColB']: {valor_3_b}\n") # Salida: 300

# Seleccionar slice de filas y columnas por etiqueta
# Filas desde 'idx2' hasta 'idx4' (inclusive)
# Columnas desde 'ColB' hasta 'ColC' (inclusive)
slice_loc = df.loc['idx2':'idx4', 'ColB':'ColC']
print(f"Slice df.loc['idx2':'idx4', 'ColB':'ColC']:\n{slice_loc}\n")
```

## Selección con `.iloc[]` (Basada en Posición Entera)

`.iloc[]` se utiliza para seleccionar datos usando las **posiciones enteras** (índices numéricos base 0) de las filas y columnas, similar a NumPy o listas de Python.

**Sintaxis:**

*   `df.iloc[indice_fila]` : Selecciona una fila completa como una Serie.
*   `df.iloc[[lista_indices_fila]]` : Selecciona múltiples filas como un DataFrame.
*   `df.iloc[:, indice_columna]` : Selecciona una columna completa como una Serie.
*   `df.iloc[:, [lista_indices_columna]]` : Selecciona múltiples columnas como un DataFrame.
*   `df.iloc[indice_fila, indice_columna]` : Selecciona un valor escalar específico.
*   `df.iloc[slice_indices_fila, slice_indices_columna]` : Selecciona un subconjunto rectangular. **Importante:** ¡El slicing con enteros en `.iloc` **excluye** el valor final (`stop`), igual que en Python estándar!

**Ejemplos con `.iloc[]`:**

```python
print("--- Selección con .iloc[] ---")

# Seleccionar la primera fila (posición 0)
fila_0 = df.iloc[0]
print(f"Primera fila (iloc[0]):\n{fila_0}\n")

# Seleccionar la tercera fila (posición 2)
fila_2 = df.iloc[2]
print(f"Tercera fila (iloc[2]):\n{fila_2}\n")

# Seleccionar filas en posiciones 0 y 3
filas_0_3 = df.iloc[[0, 3]]
print(f"Filas 0 y 3 (iloc[[0, 3]]):\n{filas_0_3}\n")

# Seleccionar la segunda columna (posición 1)
col_1 = df.iloc[:, 1]
print(f"Segunda columna (iloc[:, 1]):\n{col_1}\n")

# Seleccionar columnas en posiciones 0 y 2
cols_0_2 = df.iloc[:, [0, 2]]
print(f"Columnas 0 y 2 (iloc[:, [0, 2]]):\n{cols_0_2}\n")

# Seleccionar valor específico en fila 1, columna 2
valor_1_2 = df.iloc[1, 2]
print(f"Valor en [1, 2]: {valor_1_2}\n") # Salida: q

# Seleccionar slice de filas y columnas por posición
# Filas desde 1 hasta 4 (exclusive) -> filas 1, 2, 3
# Columnas desde 0 hasta 2 (exclusive) -> columnas 0, 1
slice_iloc = df.iloc[1:4, 0:2]
print(f"Slice df.iloc[1:4, 0:2]:\n{slice_iloc}\n")
```

## Filtrado con Condiciones Booleanas

Una forma muy potente de seleccionar filas es usando **indexación booleana**. Creas una Serie booleana (True/False) basada en una condición sobre una columna (o varias) y luego usas esa Serie dentro de `.loc[]` (o directamente con `[]` aunque `.loc` es más explícito) para filtrar las filas donde la condición es `True`.

```python
print("--- Filtrado con Condiciones Booleanas ---")

# Condición: Filas donde ColA > 25
condicion_a = df['ColA'] > 25
print(f"Condición (ColA > 25):\n{condicion_a}\n")
# Salida:
# idx1    False
# idx2    False
# idx3     True
# idx4     True
# idx5     True
# Name: ColA, dtype: bool

# Aplicar la condición para filtrar filas (usando .loc[])
df_filtrado_a = df.loc[condicion_a]
print(f"DataFrame filtrado (ColA > 25):\n{df_filtrado_a}\n")

# Aplicar la condición directamente con [] (funciona para filas)
df_filtrado_a_alt = df[condicion_a]
# print(f"DataFrame filtrado (alt):\n{df_filtrado_a_alt}\n") # Mismo resultado

# Condición combinada: ColA > 20 Y ColC == 's'
condicion_combinada = (df['ColA'] > 20) & (df['ColC'] == 's') # Usa '&' para AND, '|' para OR, '~' para NOT
print(f"Condición combinada:\n{condicion_combinada}\n")
# Salida:
# idx1    False
# idx2    False
# idx3    False
# idx4     True
# idx5    False
# dtype: bool

df_filtrado_comb = df.loc[condicion_combinada]
print(f"DataFrame filtrado (combinado):\n{df_filtrado_comb}\n")

# Filtrar y seleccionar columnas específicas a la vez
df_filtrado_cols = df.loc[df['ColB'] >= 300, ['Nombre', 'ColC']] # Añadimos una columna Nombre para el ejemplo
# (Necesitarías añadir la columna 'Nombre' al df original para que esto funcione)
# df['Nombre'] = ['Alfa', 'Beta', 'Gamma', 'Delta', 'Epsilon']
# print(f"Filtrado y selección de columnas:\n{df_filtrado_cols}\n")
```

**Resumen `.loc` vs `.iloc`:**

*   Usa `.loc[]` cuando quieras seleccionar basado en las **etiquetas** del índice y los **nombres** de las columnas. El slicing **incluye** el final.
*   Usa `.iloc[]` cuando quieras seleccionar basado en las **posiciones enteras** (0, 1, 2...). El slicing **excluye** el final.
*   Para filtrado basado en condiciones, generalmente se crea una Serie booleana y se usa dentro de `.loc[]` o `[]`.

Dominar `.loc` e `.iloc` es esencial para cualquier tarea de manipulación de datos con Pandas. Te permiten acceder y modificar precisamente los datos que necesitas.
