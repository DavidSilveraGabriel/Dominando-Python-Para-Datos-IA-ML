# Módulo 4: Combinación de DataFrames (`merge`, `join`, `concat`)

Es muy común que los datos que necesitas para un análisis estén distribuidos en varias tablas o archivos. Pandas ofrece funciones flexibles y potentes para combinar estos datos en un único DataFrame. Las principales son `pd.merge()`, `df.join()` y `pd.concat()`.

```python
import pandas as pd
```

## `pd.merge()` (Estilo SQL Joins)

`pd.merge()` es la función más flexible para combinar DataFrames, similar a las operaciones JOIN en bases de datos SQL. Combina filas basándose en los valores de una o más **columnas clave** comunes o en los índices.

**Sintaxis Principal:**

```python
pd.merge(left_df, right_df, how='inner', on=None, left_on=None, right_on=None,
         left_index=False, right_index=False, suffixes=('_x', '_y'))
```

*   `left_df`, `right_df`: Los dos DataFrames a combinar.
*   `how`: El tipo de join a realizar:
    *   `'inner'` (por defecto): Mantiene solo las filas donde las claves de combinación existen en **ambos** DataFrames.
    *   `'outer'`: Mantiene **todas** las filas de ambos DataFrames. Rellena con NaN donde no hay correspondencia.
    *   `'left'`: Mantiene **todas** las filas del DataFrame izquierdo (`left_df`) y las correspondientes del derecho. Rellena con NaN en las columnas del derecho si no hay correspondencia.
    *   `'right'`: Mantiene **todas** las filas del DataFrame derecho (`right_df`) y las correspondientes del izquierdo. Rellena con NaN en las columnas del izquierdo si no hay correspondencia.
*   `on`: Nombre(s) de la(s) columna(s) clave a usar para la unión. Deben existir en **ambos** DataFrames. Si es `None`, `merge` usa la intersección de los nombres de columna como claves.
*   `left_on`, `right_on`: Nombres de columna a usar como clave en el DataFrame izquierdo y derecho, respectivamente (útil si las columnas clave tienen nombres diferentes).
*   `left_index`, `right_index`: Booleanos. Si es `True`, usa el índice del DataFrame izquierdo/derecho como clave de unión.
*   `suffixes`: Una tupla de sufijos (`_x`, `_y` por defecto) para añadir a los nombres de columnas que se solapan (existen en ambos DataFrames pero no son claves de unión) para evitar ambigüedad.

**Ejemplos:**

```python
# DataFrames de ejemplo
df_clientes = pd.DataFrame({
    'ID_Cliente': [1, 2, 3, 4],
    'Nombre': ['Ana', 'Luis', 'Eva', 'Juan'],
    'Ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Sevilla']
})

df_pedidos = pd.DataFrame({
    'ID_Pedido': [101, 102, 103, 104, 105],
    'ID_Cliente': [2, 3, 1, 3, 5], # Cliente 4 no tiene pedidos, Cliente 5 no está en df_clientes
    'Producto': ['A', 'B', 'C', 'D', 'E'],
    'Cantidad': [5, 2, 1, 3, 4]
})

print("Clientes:")
print(df_clientes)
print("\nPedidos:")
print(df_pedidos)

# --- Inner Join (por defecto) ---
# Une basado en la columna común 'ID_Cliente'
df_inner = pd.merge(df_clientes, df_pedidos, on='ID_Cliente') # how='inner' es el defecto
print("\nInner Join (on='ID_Cliente'):")
print(df_inner) # Solo clientes 1, 2, 3 que están en ambos

# --- Left Join ---
# Mantiene todos los clientes, añade info de pedidos si existe
df_left = pd.merge(df_clientes, df_pedidos, on='ID_Cliente', how='left')
print("\nLeft Join:")
print(df_left) # Cliente 4 tiene NaN en columnas de pedido

# --- Right Join ---
# Mantiene todos los pedidos, añade info de clientes si existe
df_right = pd.merge(df_clientes, df_pedidos, on='ID_Cliente', how='right')
print("\nRight Join:")
print(df_right) # Pedido del Cliente 5 tiene NaN en columnas de cliente

# --- Outer Join ---
# Mantiene todos los clientes y todos los pedidos
df_outer = pd.merge(df_clientes, df_pedidos, on='ID_Cliente', how='outer')
print("\nOuter Join:")
print(df_outer) # Cliente 4 y Pedido de Cliente 5 tienen NaNs

# --- Merge con claves de nombres diferentes ---
df_clientes_v2 = df_clientes.rename(columns={'ID_Cliente': 'Cliente_ID'})
print("\nClientes V2 (clave renombrada):")
print(df_clientes_v2)
df_merge_diff_keys = pd.merge(df_clientes_v2, df_pedidos,
                              left_on='Cliente_ID', right_on='ID_Cliente', how='inner')
print("\nMerge con left_on y right_on:")
print(df_merge_diff_keys)

# --- Merge usando índices ---
df_clientes_idx = df_clientes.set_index('ID_Cliente')
df_pedidos_idx = df_pedidos.set_index('ID_Cliente')
print("\nClientes con índice:")
print(df_clientes_idx)
print("\nPedidos con índice:")
print(df_pedidos_idx)

df_merge_index = pd.merge(df_clientes_idx, df_pedidos_idx,
                          left_index=True, right_index=True, how='inner')
print("\nMerge usando índices:")
print(df_merge_index)
```

## `df.join()` (Basado en Índice)

`df.join()` es un método de DataFrame que une columnas de otro DataFrame. Por defecto, une usando los **índices** de ambos DataFrames. Es una forma conveniente de hacer merges basados en índices (equivalente a `pd.merge(..., left_index=True, right_index=True)`).

**Sintaxis Principal:**

```python
left_df.join(right_df, on=None, how='left', lsuffix='', rsuffix='')
```

*   `right_df`: El DataFrame cuyas columnas se añadirán.
*   `on`: Columna(s) en el DataFrame izquierdo (`left_df`) para usar como clave de unión (se unirá con el *índice* del `right_df`). Si es `None`, une por los índices de ambos.
*   `how`: Tipo de join (`'left'`, `'right'`, `'outer'`, `'inner'`). Por defecto es `'left'`.
*   `lsuffix`, `rsuffix`: Sufijos a añadir a nombres de columna solapados (similar a `suffixes` en `merge`).

**Ejemplo:**

```python
# Usando los DataFrames con índice del ejemplo anterior
print("\n--- Join (basado en índice por defecto) ---")
df_join_index = df_clientes_idx.join(df_pedidos_idx, how='inner') # how='left' es el defecto
print(df_join_index) # Mismo resultado que el merge por índice inner

# Unir usando una columna del izquierdo y el índice del derecho
df_clientes_reset = df_clientes.copy() # Volvemos al df sin índice
df_join_col_idx = df_clientes_reset.join(df_pedidos_idx, on='ID_Cliente', how='inner')
print("\n--- Join (columna 'ID_Cliente' de la izquierda con índice de la derecha) ---")
print(df_join_col_idx)
```

## `pd.concat()` (Apilar/Concatenar)

`pd.concat()` se usa para **apilar** múltiples DataFrames (o Series) juntos, ya sea verticalmente (añadiendo filas, `axis=0`) u horizontalmente (añadiendo columnas, `axis=1`).

**Sintaxis Principal:**

```python
pd.concat(objs, axis=0, join='outer', ignore_index=False)
```

*   `objs`: Una secuencia (lista o tupla) de los DataFrames o Series a concatenar.
*   `axis`: El eje a lo largo del cual concatenar:
    *   `0` (por defecto): Apila verticalmente (añade filas). Los índices se mantienen (a menos que `ignore_index=True`). Las columnas que no coinciden se rellenan con NaN (si `join='outer'`).
    *   `1`: Apila horizontalmente (añade columnas). La unión se basa en el índice. Las filas que no coinciden se rellenan con NaN (si `join='outer'`).
*   `join`: Cómo manejar los índices/columnas en el *otro* eje (el que no es `axis`):
    *   `'outer'` (por defecto): Mantiene todos los índices/columnas del otro eje, rellenando con NaN donde no hay datos.
    *   `'inner'`: Mantiene solo los índices/columnas que son comunes a todos los DataFrames.
*   `ignore_index`: Booleano (por defecto `False`). Si es `True`, no usa los valores de índice originales en el eje de concatenación. Se crea un nuevo índice por defecto (0, 1, 2...). Útil cuando los índices originales no son significativos o tienen duplicados.

**Ejemplos:**

```python
df1 = pd.DataFrame({'A': ['A0', 'A1'], 'B': ['B0', 'B1']}, index=[0, 1])
df2 = pd.DataFrame({'A': ['A2', 'A3'], 'B': ['B2', 'B3']}, index=[2, 3])
df3 = pd.DataFrame({'C': ['C0', 'C1'], 'D': ['D0', 'D1']}, index=[0, 1]) # Columnas diferentes

print("\n--- Concatenación (pd.concat) ---")
print("df1:\n", df1)
print("df2:\n", df2)
print("df3:\n", df3)

# Concatenar verticalmente (axis=0, por defecto)
df_concat_vert = pd.concat([df1, df2])
print("\nConcatenación Vertical (axis=0):")
print(df_concat_vert)

# Concatenar verticalmente ignorando índice original
df_concat_vert_ignore = pd.concat([df1, df2], ignore_index=True)
print("\nConcatenación Vertical (ignore_index=True):")
print(df_concat_vert_ignore)

# Concatenar verticalmente con columnas no alineadas (join='outer')
df_concat_outer = pd.concat([df1, df3], axis=0, join='outer', sort=False)
print("\nConcatenación Vertical (join='outer'):")
print(df_concat_outer) # Rellena con NaN

# Concatenación Vertical (join='inner')
df_concat_inner = pd.concat([df1, df3], axis=0, join='inner')
print("\nConcatenación Vertical (join='inner'):")
print(df_concat_inner) # No quedan columnas comunes (aparte del índice)

# Concatenar horizontalmente (axis=1)
df_concat_horiz = pd.concat([df1, df3], axis=1)
print("\nConcatenación Horizontal (axis=1):")
print(df_concat_horiz) # Une por índice
```

**Elegir la Función Correcta:**

*   Usa `pd.merge()` para uniones tipo base de datos basadas en columnas clave o índices. Es la más flexible para joins complejos.
*   Usa `df.join()` como atajo para uniones basadas principalmente en índices.
*   Usa `pd.concat()` para apilar DataFrames (añadir filas o columnas) sin necesariamente una lógica de clave compartida, aunque la alineación por índice/columna sigue siendo importante.

Dominar estas funciones de combinación es esencial para integrar datos de múltiples fuentes en un único conjunto de datos listo para el análisis.
