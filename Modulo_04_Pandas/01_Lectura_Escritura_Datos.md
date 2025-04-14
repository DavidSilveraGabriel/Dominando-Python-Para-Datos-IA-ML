# Módulo 4: Lectura y Escritura de Datos (CSV, Excel, etc.)

Pandas es excepcionalmente bueno para leer datos desde una gran variedad de formatos de archivo y también para guardar tus DataFrames procesados en diferentes formatos. Los más comunes son CSV y Excel.

```python
import pandas as pd
import numpy as np # Lo usaremos para crear datos de ejemplo
```

## Archivos CSV (Comma Separated Values)

Los archivos CSV son uno de los formatos más comunes para almacenar datos tabulares. Son archivos de texto simple donde cada línea representa una fila de datos y los valores dentro de cada fila están separados por un delimitador, comúnmente una coma (`,`).

**Creando un archivo CSV de ejemplo:**

```python
# Primero, creemos un DataFrame de ejemplo para guardarlo
datos_ejemplo = {
    'ID_Producto': [101, 102, 103, 104, 105],
    'Nombre': ['Teclado', 'Mouse', 'Monitor', 'Webcam', 'Micrófono'],
    'Precio': [75.50, 25.99, 300.00, 45.20, 120.00],
    'Stock': [50, 120, 30, 75, 40]
}
df_ejemplo = pd.DataFrame(datos_ejemplo)

# Guardar el DataFrame a un archivo CSV
try:
    # index=False evita que Pandas escriba el índice del DataFrame como una columna en el CSV
    df_ejemplo.to_csv('productos_ejemplo.csv', index=False)
    print("Archivo 'productos_ejemplo.csv' guardado exitosamente.")
except Exception as e:
    print(f"Error guardando CSV: {e}")
```

**Leyendo un archivo CSV:**

La función principal es `pd.read_csv()`. Tiene muchísimos parámetros para manejar diferentes variaciones de archivos CSV.

```python
print("\n--- Leyendo archivo CSV ---")
try:
    # Lectura básica
    df_leido = pd.read_csv('productos_ejemplo.csv')
    print("DataFrame leído desde CSV:")
    print(df_leido)
    print("\nInformación del DataFrame leído:")
    df_leido.info()

except FileNotFoundError:
    print("Error: El archivo 'productos_ejemplo.csv' no se encontró.")
except Exception as e:
    print(f"Error leyendo CSV: {e}")
```

**Parámetros Comunes de `pd.read_csv()`:**

*   `filepath_or_buffer`: La ruta al archivo CSV (string) o un objeto similar a archivo.
*   `sep` o `delimiter`: El carácter usado para separar los valores (por defecto es `,`). Si tu archivo usa punto y coma (`;`), tabulación (`\t`), u otro, especifícalo aquí (ej. `sep=';'`).
*   `header`: El número de la fila (empezando en 0) que contiene los nombres de las columnas. Por defecto es `0` (la primera línea). Si no hay encabezado, usa `header=None`.
*   `names`: Una lista de nombres de columna para usar si el archivo no tiene encabezado (`header=None`).
*   `index_col`: Especifica qué columna(s) usar como índice de filas del DataFrame. Puede ser un número de columna o un nombre de columna.
*   `usecols`: Una lista de nombres o índices de columna que quieres leer específicamente (ignora las demás).
*   `dtype`: Un diccionario para especificar el tipo de dato de columnas específicas (ej. `dtype={'ID_Producto': str}`).
*   `na_values`: Una lista de strings que deben ser interpretados como valores NaN (Not a Number - valores faltantes).
*   `skiprows`: Número de filas a saltar al principio del archivo.
*   `nrows`: Número máximo de filas a leer desde el principio.

```python
# Ejemplo con más parámetros
try:
    # Suponiendo un CSV con ';' como separador y sin encabezado
    # (Necesitarías crear 'otro_ejemplo.csv' manualmente para probar esto)
    # df_otro = pd.read_csv('otro_ejemplo.csv', sep=';', header=None, names=['ColA', 'ColB'])
    # print("\nDataFrame leído desde 'otro_ejemplo.csv':")
    # print(df_otro)

    # Leer solo columnas específicas
    df_columnas_selectas = pd.read_csv('productos_ejemplo.csv', usecols=['Nombre', 'Precio'])
    print("\nDataFrame con columnas seleccionadas:")
    print(df_columnas_selectas)

except FileNotFoundError:
    print("Error: Archivo no encontrado para ejemplos adicionales.")
except Exception as e:
    print(f"Error en lectura CSV adicional: {e}")
```

**Escribiendo a un archivo CSV (`to_csv()`):**

```python
# Modificar el DataFrame leído
df_leido['Descuento'] = df_leido['Precio'] * 0.10 # Añadir columna de descuento

print("\n--- Escribiendo archivo CSV modificado ---")
try:
    # Guardar con punto y coma como separador y sin índice
    df_leido.to_csv('productos_modificado.csv', sep=';', index=False)
    print("Archivo 'productos_modificado.csv' guardado con separador ';'.")

    # Guardar solo columnas específicas
    df_leido.to_csv('productos_nombre_stock.csv', columns=['Nombre', 'Stock'], index=False)
    print("Archivo 'productos_nombre_stock.csv' guardado.")
except Exception as e:
    print(f"Error guardando CSV modificado: {e}")
```

**Parámetros Comunes de `to_csv()`:**

*   `path_or_buf`: Ruta donde guardar el archivo.
*   `sep`: Delimitador a usar (por defecto `,`).
*   `index`: Booleano, si se debe escribir el índice del DataFrame como una columna (por defecto `True`). A menudo se pone a `False`.
*   `header`: Booleano o lista de strings. Si se deben escribir los nombres de columna (por defecto `True`).
*   `columns`: Lista de nombres de columna a escribir (ignora las demás).
*   `mode`: Modo de escritura (`'w'` para sobrescribir, `'a'` para añadir - ¡cuidado con añadir encabezados si el archivo ya existe!).
*   `encoding`: Codificación a usar (ej. `'utf-8'`).
*   `float_format`: String de formato para números flotantes (ej. `'%.2f'` para dos decimales).

## Archivos Excel

Pandas también puede leer y escribir archivos Excel (`.xls` y `.xlsx`). Necesita tener instaladas bibliotecas adicionales como `openpyxl` (para `.xlsx`) y/o `xlrd` (para `.xls` más antiguos).

*   Instalación: `conda install openpyxl xlrd` o `pip install openpyxl xlrd`

**Leyendo un archivo Excel (`pd.read_excel()`):**

```python
print("\n--- Leyendo archivo Excel ---")
# Primero, guardamos nuestro DataFrame de ejemplo en Excel
try:
    df_ejemplo.to_excel('productos_ejemplo.xlsx', sheet_name='Inventario', index=False)
    print("Archivo 'productos_ejemplo.xlsx' guardado.")
except Exception as e:
    print(f"Error guardando Excel: {e}")

# Ahora lo leemos
try:
    df_excel = pd.read_excel('productos_ejemplo.xlsx', sheet_name='Inventario')
    print("\nDataFrame leído desde Excel:")
    print(df_excel)
except FileNotFoundError:
    print("Error: El archivo 'productos_ejemplo.xlsx' no se encontró.")
except Exception as e:
    print(f"Error leyendo Excel: {e}")
```

**Parámetros Comunes de `pd.read_excel()`:**

*   `io`: Ruta al archivo Excel.
*   `sheet_name`: Nombre de la hoja (string) o índice (int, empezando en 0) a leer. Por defecto es 0 (la primera hoja). Puede ser una lista de nombres/índices para leer múltiples hojas en un diccionario de DataFrames, o `None` para leer todas las hojas.
*   `header`: Fila a usar como encabezado (índice base 0).
*   `names`: Nombres de columna a usar si no hay encabezado.
*   `index_col`: Columna a usar como índice de filas.
*   `usecols`: Columnas específicas a leer.
*   `dtype`: Especificar tipos de datos.
*   `skiprows`: Filas a saltar al inicio.
*   `nrows`: Número de filas a leer.

**Escribiendo a un archivo Excel (`to_excel()`):**

```python
print("\n--- Escribiendo archivo Excel modificado ---")
df_excel['Precio_Oferta'] = df_excel['Precio'] * 0.9 # Añadir columna

try:
    # Guardar en una nueva hoja, sin índice
    df_excel.to_excel('productos_modificado.xlsx', sheet_name='Ofertas', index=False)
    print("Archivo 'productos_modificado.xlsx' guardado.")

    # Escribir múltiples DataFrames en diferentes hojas del MISMO archivo
    with pd.ExcelWriter('reporte_completo.xlsx') as writer:
        df_ejemplo.to_excel(writer, sheet_name='Original', index=False)
        df_excel.to_excel(writer, sheet_name='Con_Ofertas', index=False)
    print("Archivo 'reporte_completo.xlsx' con múltiples hojas guardado.")

except Exception as e:
    print(f"Error guardando Excel modificado: {e}")
```

**Parámetros Comunes de `to_excel()`:**

*   `excel_writer`: Ruta del archivo o un objeto `ExcelWriter`.
*   `sheet_name`: Nombre de la hoja donde guardar (por defecto `'Sheet1'`).
*   `index`: Escribir índice del DataFrame (por defecto `True`).
*   `header`: Escribir nombres de columna (por defecto `True`).
*   `columns`: Columnas específicas a escribir.
*   `startrow`, `startcol`: Celda superior izquierda donde empezar a escribir (base 0).

## Otros Formatos

Pandas soporta muchos otros formatos, incluyendo:

*   **JSON:** `pd.read_json()`, `df.to_json()`
*   **HTML:** `pd.read_html()` (lee tablas de páginas web), `df.to_html()`
*   **SQL:** `pd.read_sql()`, `df.to_sql()` (requiere SQLAlchemy u otro conector de base de datos)
*   **HDF5:** `pd.read_hdf()`, `df.to_hdf()` (formato binario eficiente, requiere `tables`)
*   **Parquet:** `pd.read_parquet()`, `df.to_parquet()` (formato columnar binario eficiente, requiere `pyarrow` o `fastparquet`)
*   **Pickle:** `pd.read_pickle()`, `df.to_pickle()` (formato de serialización binario específico de Python)

La capacidad de leer y escribir fácilmente desde/hacia diversos formatos es una de las grandes fortalezas de Pandas, haciendo que la integración con diferentes fuentes de datos sea mucho más sencilla.
