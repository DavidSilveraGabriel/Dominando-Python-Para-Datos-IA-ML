# Módulo 4: Ejercicios de Análisis Exploratorio de Datos (EDA) con Pandas

¡Es hora de combinar todo lo aprendido en Pandas! El Análisis Exploratorio de Datos (EDA) es el proceso inicial de investigar un conjunto de datos para descubrir patrones, detectar anomalías, probar hipótesis y verificar suposiciones con la ayuda de resúmenes estadísticos y visualizaciones (aunque la visualización la veremos en detalle en el Módulo 5).

Estos ejercicios te guiarán a través de un flujo de trabajo básico de EDA usando Pandas. Necesitarás los archivos CSV que creamos en la lección de Lectura/Escritura (`productos_ejemplo.csv`) o puedes usar los DataFrames de ejemplo definidos aquí.

```python
import pandas as pd
import numpy as np

# --- Datos de Ejemplo (si no tienes los CSV) ---
# Datos de Productos
datos_productos = {
    'ID_Producto': [101, 102, 103, 104, 105, 101, 103], # ID 101 y 103 duplicados
    'Nombre': ['Teclado', 'Mouse', 'Monitor', 'Webcam', 'Micrófono', 'Teclado', 'Monitor'],
    'Precio': [75.50, 25.99, 300.00, 45.20, 120.00, 75.50, 310.00], # Precio diferente para Monitor duplicado
    'Stock': [50, 120, 30, 75, 40, 50, 25],
    'Categoria': ['Periférico', 'Periférico', 'Monitor', 'Periférico', 'Audio', 'Periférico', 'Monitor']
}
df_prods = pd.DataFrame(datos_productos)

# Datos de Ventas (con algunos NaN y fechas)
fechas_ventas = pd.to_datetime(['2024-03-15', '2024-03-15', '2024-03-16', '2024-03-17',
                                '2024-03-17', '2024-03-18', '2024-03-18', np.nan])
datos_ventas = {
    'ID_Venta': range(1, 9),
    'ID_Producto': [101, 102, 101, 103, 104, 102, 103, 101],
    'Cantidad': [2, 5, 1, 2, 1, 3, 1, 2],
    'Fecha': fechas_ventas,
    'Vendedor': ['Ana', 'Luis', 'Ana', 'Eva', 'Luis', 'Ana', 'Eva', 'Luis']
}
df_vent = pd.DataFrame(datos_ventas)

print("--- DataFrames de Ejemplo ---")
print("Productos (df_prods):")
print(df_prods)
print("\nVentas (df_vent):")
print(df_vent)
print("\n" + "="*30 + "\n")

# --- INICIO DE EJERCICIOS ---
```

---

**Ejercicio 1: Carga y Exploración Inicial**

1.  *(Opcional)* Si tienes los archivos CSV, carga `productos_ejemplo.csv` en un DataFrame llamado `df_prods_csv`. Si no, usa el `df_prods` definido arriba.
2.  Muestra las primeras 5 filas de `df_prods`.
3.  Muestra las últimas 3 filas de `df_prods`.
4.  Obtén información general sobre `df_prods` (tipos de columna, valores no nulos) usando `.info()`.
5.  Obtén estadísticas descriptivas básicas para las columnas numéricas de `df_prods` usando `.describe()`.
6.  Haz lo mismo (pasos 2-5) para el DataFrame `df_vent`.

---

**Ejercicio 2: Limpieza de Datos (Duplicados y Nulos)**

1.  **Productos (`df_prods`):**
    *   Verifica si hay filas completamente duplicadas en `df_prods`.
    *   Verifica si hay duplicados basados solo en `ID_Producto`. ¿Qué observas?
    *   Elimina los duplicados basados en `ID_Producto`, manteniendo la **última** ocurrencia (para quedarnos con el precio más reciente del Monitor). Guarda el resultado en `df_prods_limpio`. Verifica que los duplicados se eliminaron.
2.  **Ventas (`df_vent`):**
    *   Cuenta cuántos valores nulos hay en cada columna de `df_vent`.
    *   Elimina las filas donde la columna `Fecha` tenga un valor nulo. Guarda el resultado en `df_vent_limpio`. Verifica que la fila con fecha nula se eliminó.

---

**Ejercicio 3: Selección y Filtrado**

Usando los DataFrames limpios (`df_prods_limpio`, `df_vent_limpio`):

1.  Selecciona y muestra solo las columnas `Nombre` y `Precio` de `df_prods_limpio`.
2.  Selecciona y muestra los productos de `df_prods_limpio` que cuestan más de 100.
3.  Selecciona y muestra los productos que pertenecen a la categoría 'Periférico'.
4.  Selecciona y muestra las ventas (`df_vent_limpio`) realizadas por 'Ana'.
5.  Selecciona y muestra las ventas donde la `Cantidad` vendida fue mayor a 2.
6.  Selecciona y muestra las ventas realizadas por 'Luis' O 'Eva'.
7.  Selecciona y muestra las ventas de 'Ana' donde la `Cantidad` fue 1.

---

**Ejercicio 4: Combinación de Datos (`merge`)**

1.  Combina `df_prods_limpio` y `df_vent_limpio` usando un **inner join** basado en la columna `ID_Producto`. Guarda el resultado en `df_combinado`.
2.  Muestra las primeras filas de `df_combinado`.
3.  ¿Cuántas filas tiene `df_combinado`? ¿Tiene sentido este número comparado con las filas de `df_vent_limpio`? (Pista: ¿Había algún ID_Producto en `df_vent_limpio` que no estuviera en `df_prods_limpio` después de la limpieza?)

---

**Ejercicio 5: Agrupación y Agregación (`groupby`)**

Usando `df_combinado`:

1.  Calcula las ventas totales (`Cantidad`) por cada `Nombre` de producto.
2.  Calcula el precio promedio (`Precio`) de los productos vendidos por cada `Vendedor`. (Pista: agrupa por vendedor, selecciona precio, calcula media).
3.  Calcula la cantidad total vendida y la cantidad de ventas distintas (conteo) para cada `Categoria`.
4.  Calcula la venta total (`Cantidad`) por `Tienda` (si tuvieras esa columna) y `Producto`. (Nota: Como no tenemos 'Tienda', agrupa solo por `Categoria` y `Nombre` para practicar agrupación múltiple).

---

**Ejercicio 6: Operaciones con Fechas (Básico)**

Usando `df_combinado`:

1.  Asegúrate de que la columna `Fecha` sea de tipo datetime (debería serlo si se cargó bien).
2.  Establece la columna `Fecha` como el índice del DataFrame `df_combinado`. Llama al nuevo DataFrame `df_combinado_ts`.
3.  Selecciona y muestra las ventas realizadas el '2024-03-17'.
4.  Selecciona y muestra las ventas realizadas desde '2024-03-16' hasta '2024-03-17' (inclusive).

---
---

## Soluciones

```python
import pandas as pd
import numpy as np

# --- Datos de Ejemplo (si no tienes los CSV) ---
datos_productos = {
    'ID_Producto': [101, 102, 103, 104, 105, 101, 103],
    'Nombre': ['Teclado', 'Mouse', 'Monitor', 'Webcam', 'Micrófono', 'Teclado', 'Monitor'],
    'Precio': [75.50, 25.99, 300.00, 45.20, 120.00, 75.50, 310.00],
    'Stock': [50, 120, 30, 75, 40, 50, 25],
    'Categoria': ['Periférico', 'Periférico', 'Monitor', 'Periférico', 'Audio', 'Periférico', 'Monitor']
}
df_prods = pd.DataFrame(datos_productos)
fechas_ventas = pd.to_datetime(['2024-03-15', '2024-03-15', '2024-03-16', '2024-03-17',
                                '2024-03-17', '2024-03-18', '2024-03-18', np.nan])
datos_ventas = {
    'ID_Venta': range(1, 9),
    'ID_Producto': [101, 102, 101, 103, 104, 102, 103, 101],
    'Cantidad': [2, 5, 1, 2, 1, 3, 1, 2],
    'Fecha': fechas_ventas,
    'Vendedor': ['Ana', 'Luis', 'Ana', 'Eva', 'Luis', 'Ana', 'Eva', 'Luis']
}
df_vent = pd.DataFrame(datos_ventas)

print("--- DataFrames de Ejemplo ---")
print("Productos (df_prods):")
print(df_prods)
print("\nVentas (df_vent):")
print(df_vent)
print("\n" + "="*30 + "\n")


# --- Solución Ejercicio 1 ---
print("--- Solución Ejercicio 1 ---")
# 1. (Asumimos que usamos df_prods definido arriba)
# df_prods_csv = pd.read_csv('productos_ejemplo.csv') # Si usaras el CSV
print("Primeras 5 filas df_prods:")
print(df_prods.head()) # head(5) es el defecto
print("\nÚltimas 3 filas df_prods:")
print(df_prods.tail(3))
print("\nInfo df_prods:")
df_prods.info()
print("\nDescribe df_prods:")
print(df_prods.describe())

print("\nPrimeras 5 filas df_vent:")
print(df_vent.head())
print("\nÚltimas 3 filas df_vent:")
print(df_vent.tail(3))
print("\nInfo df_vent:")
df_vent.info()
print("\nDescribe df_vent:")
print(df_vent.describe())


# --- Solución Ejercicio 2 ---
print("\n--- Solución Ejercicio 2 ---")
# 1. Productos
print(f"\n¿Filas duplicadas en df_prods?: {df_prods.duplicated().any()}")
print("Filas duplicadas basadas en ID_Producto:")
print(df_prods.duplicated(subset=['ID_Producto'])) # Fila 5 (101) y 6 (103) son True
df_prods_limpio = df_prods.drop_duplicates(subset=['ID_Producto'], keep='last')
print("\ndf_prods_limpio (después de drop_duplicates):")
print(df_prods_limpio)
print(f"¿Duplicados en ID_Producto restantes?: {df_prods_limpio.duplicated(subset=['ID_Producto']).any()}")

# 2. Ventas
print("\nNaN por columna en df_vent:")
print(df_vent.isnull().sum())
df_vent_limpio = df_vent.dropna(subset=['Fecha'])
print("\ndf_vent_limpio (después de dropna en Fecha):")
print(df_vent_limpio)
print(f"NaN restantes en Fecha: {df_vent_limpio['Fecha'].isnull().any()}")


# --- Solución Ejercicio 3 ---
print("\n--- Solución Ejercicio 3 ---")
print("\nColumnas Nombre y Precio de df_prods_limpio:")
print(df_prods_limpio[['Nombre', 'Precio']])
print("\nProductos con Precio > 100:")
print(df_prods_limpio[df_prods_limpio['Precio'] > 100])
print("\nProductos de categoría 'Periférico':")
print(df_prods_limpio[df_prods_limpio['Categoria'] == 'Periférico'])
print("\nVentas de 'Ana':")
print(df_vent_limpio[df_vent_limpio['Vendedor'] == 'Ana'])
print("\nVentas con Cantidad > 2:")
print(df_vent_limpio[df_vent_limpio['Cantidad'] > 2])
print("\nVentas de 'Luis' o 'Eva':")
print(df_vent_limpio[df_vent_limpio['Vendedor'].isin(['Luis', 'Eva'])]) # .isin() es útil para múltiples valores
# Alternativa: print(df_vent_limpio[(df_vent_limpio['Vendedor'] == 'Luis') | (df_vent_limpio['Vendedor'] == 'Eva')])
print("\nVentas de 'Ana' con Cantidad = 1:")
print(df_vent_limpio[(df_vent_limpio['Vendedor'] == 'Ana') & (df_vent_limpio['Cantidad'] == 1)])


# --- Solución Ejercicio 4 ---
print("\n--- Solución Ejercicio 4 ---")
df_combinado = pd.merge(df_prods_limpio, df_vent_limpio, on='ID_Producto', how='inner')
print("\nPrimeras filas de df_combinado:")
print(df_combinado.head())
print(f"\nNúmero de filas en df_combinado: {len(df_combinado)}")
print(f"Número de filas en df_vent_limpio: {len(df_vent_limpio)}")
# Tiene sentido, todos los ID_Producto en df_vent_limpio existían en df_prods_limpio.


# --- Solución Ejercicio 5 ---
print("\n--- Solución Ejercicio 5 ---")
print("\nVentas totales (Cantidad) por Nombre de producto:")
print(df_combinado.groupby('Nombre')['Cantidad'].sum())
print("\nPrecio promedio por Vendedor:")
print(df_combinado.groupby('Vendedor')['Precio'].mean())
print("\nCantidad total y conteo de ventas por Categoria:")
print(df_combinado.groupby('Categoria').agg(
    Cantidad_Total=('Cantidad', 'sum'),
    Num_Ventas=('ID_Venta', 'count') # Contamos ID_Venta como proxy de número de ventas
))
print("\nVenta total (Cantidad) por Categoria y Nombre:")
print(df_combinado.groupby(['Categoria', 'Nombre'])['Cantidad'].sum())


# --- Solución Ejercicio 6 ---
print("\n--- Solución Ejercicio 6 ---")
# 1. Ya debería ser datetime por pd.to_datetime, verificamos:
print(f"Tipo de columna Fecha: {df_combinado['Fecha'].dtype}")
# 2. Establecer índice
df_combinado_ts = df_combinado.set_index('Fecha')
print("\nDataFrame con índice de Fecha:")
print(df_combinado_ts.head())
# 3. Seleccionar fecha exacta
print("\nVentas del 2024-03-17:")
print(df_combinado_ts.loc['2024-03-17'])
# 4. Seleccionar rango de fechas
print("\nVentas del 2024-03-16 al 2024-03-17:")
print(df_combinado_ts.loc['2024-03-16':'2024-03-17'])

```

Estos ejercicios cubren un flujo básico pero representativo de lo que harías al empezar a explorar un nuevo conjunto de datos con Pandas. ¡La práctica es clave!
