# Módulo 4: Limpieza de Datos (Valores Nulos y Duplicados)

Rara vez encontrarás conjuntos de datos perfectos en el mundo real. A menudo, los datos contienen **valores faltantes** (también llamados nulos o NaN - Not a Number) o **filas duplicadas**. La limpieza de datos es un paso fundamental en el proceso de análisis para asegurar la calidad y fiabilidad de tus resultados. Pandas ofrece herramientas excelentes para identificar y manejar estos problemas.

```python
import pandas as pd
import numpy as np # Para generar valores NaN
```

## Manejo de Valores Faltantes (NaN)

Los valores faltantes representan información que no está disponible. Pandas los representa típicamente con `np.nan` (un valor especial de NumPy para "Not a Number").

**Creando un DataFrame con datos faltantes:**

```python
datos = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [10, np.nan, np.nan, 40, 50],
    'C': ['x', 'y', 'z', 'x', 'y'],
    'D': [True, False, True, np.nan, True]
}
df_nan = pd.DataFrame(datos, index=['r1', 'r2', 'r3', 'r4', 'r5'])

print("DataFrame con valores NaN:")
print(df_nan)
print("\n")
```

**Detectando Valores Faltantes:**

*   **`isnull()` o `isna()`:** Devuelven un DataFrame booleano del mismo tamaño, donde `True` indica que el valor es NaN y `False` que no lo es. Son equivalentes.
*   **`notnull()` o `notna()`:** Hacen lo contrario, devuelven `True` donde *no* hay NaN.

```python
print("Detectando NaN con isnull():")
print(df_nan.isnull())
print("\n")

# Contar NaN por columna
print("Conteo de NaN por columna (isnull().sum()):")
print(df_nan.isnull().sum())
print("\n")

# Contar NaN en todo el DataFrame
print(f"Conteo total de NaN: {df_nan.isnull().sum().sum()}")
```

**Manejando Valores Faltantes:**

Hay dos estrategias principales:

1.  **Eliminar (Dropping):** Quitar las filas o columnas que contienen NaN.
    *   **`dropna(axis=0)` (por defecto):** Elimina las **filas** que contienen *al menos un* NaN.
    *   **`dropna(axis=1)`:** Elimina las **columnas** que contienen *al menos un* NaN.
    *   **`dropna(how='all')`:** Elimina filas/columnas solo si *todos* sus valores son NaN.
    *   **`dropna(thresh=N)`:** Mantiene filas/columnas que tienen *al menos N* valores no-NaN.
    *   **`dropna(subset=[lista_columnas])`:** Considera NaN solo en las columnas especificadas para decidir qué filas eliminar.
    *   **`inplace=True`:** Modifica el DataFrame original directamente (¡cuidado!). Por defecto es `False` y devuelve una copia modificada.

    ```python
    print("--- Eliminando NaN (dropna) ---")

    # Eliminar filas con algún NaN (devuelve copia)
    df_sin_nan_filas = df_nan.dropna()
    print(f"DataFrame después de dropna() por filas:\n{df_sin_nan_filas}\n")

    # Eliminar columnas con algún NaN (devuelve copia)
    df_sin_nan_cols = df_nan.dropna(axis=1)
    print(f"DataFrame después de dropna() por columnas:\n{df_sin_nan_cols}\n")

    # Eliminar filas donde NaN aparece en columna 'B'
    df_sin_nan_en_b = df_nan.dropna(subset=['B'])
    print(f"DataFrame sin NaN en columna 'B':\n{df_sin_nan_en_b}\n")
    ```

2.  **Rellenar (Filling):** Reemplazar los NaN con algún otro valor.
    *   **`fillna(valor)`:** Rellena todos los NaN con el `valor` especificado.
    *   **`fillna(df.mean())`, `fillna(df.median())`, `fillna(df.mode().iloc[0])`:** Rellena NaN con la media, mediana o moda de cada columna (¡cuidado al aplicar esto a todo el DataFrame si hay columnas no numéricas!). Es mejor aplicarlo columna por columna.
    *   **`fillna(method='ffill')` (Forward Fill):** Rellena NaN con el valor válido anterior en la misma columna.
    *   **`fillna(method='bfill')` (Backward Fill):** Rellena NaN con el valor válido siguiente en la misma columna.
    *   **`inplace=True`:** Modifica el DataFrame original.

    ```python
    print("--- Rellenando NaN (fillna) ---")

    # Rellenar todos los NaN con 0 (devuelve copia)
    df_relleno_0 = df_nan.fillna(0)
    print(f"DataFrame rellenado con 0:\n{df_relleno_0}\n")

    # Rellenar NaN en columna 'A' con la media de 'A'
    media_a = df_nan['A'].mean()
    df_nan_copia = df_nan.copy() # Trabajar sobre una copia
    df_nan_copia['A'].fillna(media_a, inplace=True)
    print(f"DataFrame con NaN en 'A' rellenados con la media ({media_a:.2f}):\n{df_nan_copia}\n")

    # Rellenar con el valor anterior (forward fill)
    df_relleno_ffill = df_nan.fillna(method='ffill')
    print(f"DataFrame rellenado con ffill:\n{df_relleno_ffill}\n")
    ```

La elección entre eliminar o rellenar depende del contexto, la cantidad de datos faltantes y el impacto potencial en el análisis. Eliminar puede ser simple pero reduce el tamaño del dataset. Rellenar conserva los datos pero introduce valores estimados.

## Manejo de Datos Duplicados

Las filas duplicadas pueden distorsionar análisis como conteos o promedios.

**Creando un DataFrame con duplicados:**

```python
datos_dup = {
    'Letra': ['A', 'B', 'C', 'A', 'B', 'D'],
    'Numero': [1, 2, 3, 1, 2, 4]
}
df_dup = pd.DataFrame(datos_dup)
print("DataFrame con duplicados:")
print(df_dup)
print("\n")
```

**Detectando Duplicados:**

*   **`duplicated(subset=None, keep='first')`:** Devuelve una Serie booleana indicando qué filas son duplicadas.
    *   `subset`: Lista de nombres de columna a considerar para identificar duplicados. Por defecto, considera todas las columnas.
    *   `keep`: Determina qué duplicado (si existe) marcar.
        *   `'first'` (por defecto): Marca todas las ocurrencias como duplicadas excepto la primera.
        *   `'last'`: Marca todas las ocurrencias como duplicadas excepto la última.
        *   `False`: Marca todas las ocurrencias duplicadas como `True`.

```python
print("Detectando filas duplicadas (keep='first'):")
print(df_dup.duplicated()) # La fila 3 (A,1) y 4 (B,2) son duplicados de la 0 y 1
print("\n")

print("Detectando filas duplicadas (keep=False):")
print(df_dup.duplicated(keep=False)) # Marca todas las que tienen algún duplicado
print("\n")

# Detectar duplicados solo en la columna 'Letra'
print("Detectando duplicados en columna 'Letra':")
print(df_dup.duplicated(subset=['Letra']))
```

**Eliminando Duplicados:**

*   **`drop_duplicates(subset=None, keep='first', inplace=False)`:** Elimina las filas duplicadas. Los parámetros `subset` y `keep` funcionan igual que en `duplicated()`. `inplace=True` modifica el DataFrame original.

```python
print("--- Eliminando Duplicados (drop_duplicates) ---")

# Eliminar duplicados manteniendo la primera ocurrencia (devuelve copia)
df_sin_dup_first = df_dup.drop_duplicates() # keep='first' es el defecto
print(f"DataFrame sin duplicados (keep='first'):\n{df_sin_dup_first}\n")

# Eliminar duplicados manteniendo la última ocurrencia
df_sin_dup_last = df_dup.drop_duplicates(keep='last')
print(f"DataFrame sin duplicados (keep='last'):\n{df_sin_dup_last}\n")

# Eliminar duplicados basados solo en la columna 'Letra'
df_sin_dup_letra = df_dup.drop_duplicates(subset=['Letra'], keep='first')
print(f"DataFrame sin duplicados en 'Letra' (keep='first'):\n{df_sin_dup_letra}\n")
```

La limpieza de datos, incluyendo el manejo de valores nulos y duplicados, es un paso esencial y a menudo consume una parte significativa del tiempo en un proyecto de análisis de datos. Pandas proporciona las herramientas necesarias para realizar estas tareas de manera eficiente.
