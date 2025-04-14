# Módulo 4: Agrupación de Datos (`groupby`)

La operación `groupby` es una de las herramientas más potentes y flexibles de Pandas para el análisis de datos. Permite implementar el patrón **Split-Apply-Combine**:

1.  **Split (Dividir):** Dividir el DataFrame en grupos basados en los valores de una o más columnas (las "claves" de agrupación).
2.  **Apply (Aplicar):** Aplicar una función a cada grupo de forma independiente (ej. calcular la suma, la media, contar elementos, o aplicar una función personalizada).
3.  **Combine (Combinar):** Combinar los resultados de la aplicación de la función en una nueva estructura de datos (normalmente un DataFrame o una Serie).

```python
import pandas as pd
import numpy as np

# DataFrame de ejemplo: Ventas por tienda y producto
datos = {
    'Tienda': ['A', 'B', 'A', 'B', 'A', 'C', 'B', 'C', 'A'],
    'Producto': ['Manzana', 'Naranja', 'Manzana', 'Plátano', 'Naranja', 'Manzana', 'Naranja', 'Plátano', 'Manzana'],
    'Ventas': [100, 150, 120, 200, 80, 90, 130, 210, 110],
    'Clientes': [10, 12, 11, 15, 8, 9, 11, 16, 9]
}
df_ventas = pd.DataFrame(datos)

print("DataFrame de Ventas original:")
print(df_ventas)
print("\n")
```

## Agrupando por una Columna

El método `.groupby()` se llama sobre el DataFrame, especificando la columna (o columnas) por la que se quiere agrupar. Esto crea un objeto `DataFrameGroupBy`, que contiene la información sobre los grupos.

```python
# Agrupar por la columna 'Tienda'
grupos_por_tienda = df_ventas.groupby('Tienda')

# El objeto groupby en sí no muestra los datos agrupados directamente
print(f"Objeto GroupBy: {grupos_por_tienda}\n")
# Salida: Objeto GroupBy: <pandas.core.groupby.generic.DataFrameGroupBy object at 0x...>
```

## Aplicando Funciones de Agregación

Una vez que tienes el objeto `GroupBy`, puedes aplicar funciones de agregación para calcular estadísticas para cada grupo.

**Funciones Comunes:**

*   `sum()`: Suma de los valores en cada grupo (para columnas numéricas).
*   `mean()`: Media de los valores.
*   `median()`: Mediana.
*   `min()`, `max()`: Mínimo y máximo.
*   `count()`: Número de valores **no nulos** en cada columna del grupo.
*   `size()`: Número total de **filas** en cada grupo (incluye nulos).
*   `std()`, `var()`: Desviación estándar y varianza.
*   `first()`, `last()`: Primer/último valor no nulo.
*   `describe()`: Estadísticas descriptivas para cada grupo.

```python
print("--- Agregaciones por Tienda ---")

# Calcular la suma de Ventas y Clientes para cada tienda
suma_por_tienda = grupos_por_tienda.sum()
print(f"Suma por Tienda:\n{suma_por_tienda}\n")

# Calcular la media de Ventas y Clientes para cada tienda
media_por_tienda = grupos_por_tienda.mean()
print(f"Media por Tienda:\n{media_por_tienda}\n")

# Contar el número de registros (productos vendidos) por tienda
conteo_por_tienda = grupos_por_tienda.size() # Devuelve una Serie
print(f"Número de registros por Tienda (size):\n{conteo_por_tienda}\n")

# Contar valores no nulos por columna para cada tienda
conteo_cols_tienda = grupos_por_tienda.count() # Devuelve un DataFrame
print(f"Conteo de valores no nulos por Tienda (count):\n{conteo_cols_tienda}\n")

# Obtener estadísticas descriptivas para las columnas numéricas por tienda
desc_por_tienda = grupos_por_tienda.describe()
print(f"Descripción por Tienda:\n{desc_por_tienda}\n")

# También puedes seleccionar una columna ANTES o DESPUÉS de groupby y aplicar agregación
ventas_medias_tienda = df_ventas.groupby('Tienda')['Ventas'].mean() # Selecciona 'Ventas' después
# o: ventas_medias_tienda = df_ventas['Ventas'].groupby(df_ventas['Tienda']).mean() # Selecciona 'Ventas' antes
print(f"Ventas medias por Tienda (Serie):\n{ventas_medias_tienda}\n")
```

## Agrupando por Múltiples Columnas

Puedes agrupar por una combinación de columnas pasando una lista de nombres de columna a `groupby()`. Esto crea un índice jerárquico (MultiIndex) en el resultado.

```python
# Agrupar por 'Tienda' y luego por 'Producto'
grupos_tienda_producto = df_ventas.groupby(['Tienda', 'Producto'])

# Calcular la suma de ventas para cada combinación Tienda-Producto
suma_tienda_producto = grupos_tienda_producto['Ventas'].sum()
print(f"Suma de Ventas por Tienda y Producto:\n{suma_tienda_producto}\n")
# El resultado es una Serie con un MultiIndex (Tienda, Producto)

# Calcular la media de Ventas y Clientes
media_tienda_producto = grupos_tienda_producto.mean()
print(f"Media por Tienda y Producto:\n{media_tienda_producto}\n")
# El resultado es un DataFrame con un MultiIndex
```

## Agregación Múltiple (`.agg()`)

El método `.agg()` es muy potente y permite aplicar **múltiples funciones de agregación** a la vez, e incluso aplicar diferentes funciones a diferentes columnas.

```python
print("--- Agregación Múltiple con .agg() ---")

# Agrupar por tienda
grupos_por_tienda = df_ventas.groupby('Tienda')

# Aplicar suma y media a todas las columnas numéricas
agg_suma_media = grupos_por_tienda.agg(['sum', 'mean'])
print(f"Suma y Media por Tienda:\n{agg_suma_media}\n")

# Aplicar diferentes funciones a diferentes columnas
# Pasamos un diccionario: {'columna': [lista_de_funciones]}
agg_especifica = grupos_por_tienda.agg({
    'Ventas': ['sum', 'max'],      # Suma y máximo para Ventas
    'Clientes': ['mean', 'count'] # Media y conteo para Clientes
})
print(f"Agregación específica por columna:\n{agg_especifica}\n")

# También puedes renombrar las columnas resultantes
agg_renombrada = grupos_por_tienda.agg(
    Total_Ventas=('Ventas', 'sum'),
    Venta_Maxima=('Ventas', 'max'),
    Promedio_Clientes=('Clientes', 'mean')
)
print(f"Agregación con columnas renombradas:\n{agg_renombrada}\n")
```

## Iterando sobre Grupos

Aunque menos común que aplicar agregaciones directamente, a veces necesitas iterar sobre los grupos creados por `groupby()`. El objeto `GroupBy` se puede iterar, y en cada iteración devuelve una tupla `(nombre_grupo, sub_dataframe_grupo)`.

```python
print("--- Iterando sobre Grupos (Tienda) ---")
for nombre_tienda, grupo_df in df_ventas.groupby('Tienda'):
    print(f"\nTienda: {nombre_tienda}")
    print(grupo_df)
    # Puedes hacer cálculos específicos con cada sub-DataFrame (grupo_df)
    # print(f"  Venta máxima en esta tienda: {grupo_df['Ventas'].max()}")

print("\n--- Iterando sobre Grupos (Tienda, Producto) ---")
for (nombre_tienda, nombre_producto), grupo_df in df_ventas.groupby(['Tienda', 'Producto']):
     print(f"\nTienda: {nombre_tienda}, Producto: {nombre_producto}")
     print(grupo_df)
```

La operación `groupby` es una de las funcionalidades más importantes de Pandas para el análisis exploratorio de datos y la preparación de datos para modelado. Permite resumir y comparar subconjuntos de tus datos de manera eficiente.
