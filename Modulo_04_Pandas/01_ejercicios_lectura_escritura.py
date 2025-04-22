# Ejercicios: Módulo 4 - Lectura y Escritura de Datos

# --- Prerrequisito ---
# Asegúrate de tener Pandas instalado y que el archivo 'ejemplo_productos.csv'
# (creado en el paso anterior) esté en el MISMO directorio que este script.
# Para los ejercicios de Excel, necesitarás 'openpyxl':
# pip install openpyxl
# o
# conda install openpyxl

import pandas as pd
import os # Usaremos os para verificar si los archivos se crean

# Nombre del archivo CSV de entrada
archivo_csv_entrada = "ejemplo_productos.csv"
# Nombres para los archivos de salida
archivo_csv_salida = "productos_modificado.csv"
archivo_excel_salida = "productos_excel.xlsx"

print(f"--- Usando archivo de entrada: {archivo_csv_entrada} ---")

# --- Ejercicio 1: Lectura Básica de CSV ---
# Instrucciones:
# 1. Lee el archivo `archivo_csv_entrada` en un DataFrame llamado `df_productos`.
# 2. Imprime las primeras 5 filas del DataFrame usando `.head()`.
# 3. Imprime la información general del DataFrame usando `.info()`.
# Maneja la excepción `FileNotFoundError` si el archivo no existe.

print("\n--- Ejercicio 1: Lectura Básica de CSV ---")
df_productos = None # Inicializar por si falla la lectura
try:
    # 1. Leer CSV
    df_productos = pd.read_csv(archivo_csv_entrada)

    # 2. Imprimir head
    print("Primeras filas del DataFrame leído:")
    print(df_productos.head())

    # 3. Imprimir info
    print("\nInformación del DataFrame:")
    df_productos.info()

except FileNotFoundError:
    print(f"ERROR: No se encontró el archivo '{archivo_csv_entrada}'. Asegúrate de que existe.")
except Exception as e:
    print(f"Ocurrió un error inesperado al leer el CSV: {e}")


# --- Ejercicio 2: Lectura de CSV con Parámetros ---
# Instrucciones:
# 1. Vuelve a leer `archivo_csv_entrada`, pero esta vez:
#    - Usa la columna 'ID' como índice del DataFrame (`index_col='ID'`).
#    - Lee únicamente las columnas 'Nombre' y 'Precio' (`usecols=['ID', 'Nombre', 'Precio']`).
#    Guarda el resultado en `df_productos_idx`.
# 2. Imprime el DataFrame `df_productos_idx`.
# 3. Imprime el índice (`.index`) del nuevo DataFrame.

print("\n--- Ejercicio 2: Lectura de CSV con Parámetros ---")
if os.path.exists(archivo_csv_entrada): # Solo intentar si el archivo existe
    try:
        # 1. Leer con parámetros
        df_productos_idx = pd.read_csv(
            archivo_csv_entrada,
            index_col='ID',
            usecols=['ID', 'Nombre', 'Precio']
        )
        # 2. Imprimir DataFrame
        print("DataFrame leído con ID como índice y columnas seleccionadas:")
        print(df_productos_idx)
        # 3. Imprimir índice
        print(f"\nÍndice del DataFrame: {df_productos_idx.index}")

    except ValueError as ve:
        print(f"Error de valor al leer CSV (¿columna no encontrada?): {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer el CSV con parámetros: {e}")
else:
    print(f"Saltando Ejercicio 2 porque '{archivo_csv_entrada}' no se encontró.")


# --- Ejercicio 3: Escritura a CSV ---
# Instrucciones:
# 1. Si `df_productos` se leyó correctamente en el Ejercicio 1:
#    a. Añade una nueva columna llamada 'IVA' al DataFrame `df_productos`.
#       Calcula el IVA como el 21% del 'Precio' (`df_productos['Precio'] * 0.21`).
#    b. Guarda el DataFrame modificado en un NUEVO archivo CSV llamado `archivo_csv_salida`.
#       - No incluyas el índice de Pandas en el archivo (`index=False`).
#       - Usa el punto y coma (`;`) como separador (`sep=';'`).
# 2. Imprime un mensaje confirmando que el archivo se ha guardado (o un error si ocurrió).
# 3. (Opcional) Abre el archivo CSV generado manualmente para verificar su contenido y formato.

print(f"\n--- Ejercicio 3: Escritura a CSV ('{archivo_csv_salida}') ---")
if df_productos is not None: # Verificar si df_productos existe
    try:
        # 1a. Añadir columna IVA
        df_productos['IVA'] = df_productos['Precio'] * 0.21
        print("DataFrame con columna 'IVA' añadida:")
        print(df_productos.head()) # Mostrar cómo quedó

        # 1b. Guardar a CSV modificado
        df_productos.to_csv(archivo_csv_salida, index=False, sep=';')

        # 2. Confirmar guardado
        if os.path.exists(archivo_csv_salida):
            print(f"\nArchivo '{archivo_csv_salida}' guardado correctamente con separador ';'.")
        else:
            print(f"ERROR: El archivo '{archivo_csv_salida}' no se pudo crear.")

    except Exception as e:
        print(f"Ocurrió un error inesperado al modificar o guardar el CSV: {e}")
else:
    print("Saltando Ejercicio 3 porque df_productos no se cargó correctamente.")


# --- Ejercicio 4: Escritura a Excel ---
# Instrucciones:
# 1. Si `df_productos` se modificó correctamente en el Ejercicio 3:
#    a. Guarda el DataFrame `df_productos` (con la columna 'IVA') en un archivo Excel
#       llamado `archivo_excel_salida`.
#    b. Especifica el nombre de la hoja como 'Inventario'.
#    c. No incluyas el índice de Pandas (`index=False`).
# 2. Imprime un mensaje confirmando que el archivo Excel se ha guardado.

print(f"\n--- Ejercicio 4: Escritura a Excel ('{archivo_excel_salida}') ---")
if df_productos is not None and 'IVA' in df_productos.columns: # Verificar si df_productos existe y tiene IVA
    try:
        # 1. Guardar a Excel
        df_productos.to_excel(archivo_excel_salida, sheet_name='Inventario', index=False)

        # 2. Confirmar guardado
        if os.path.exists(archivo_excel_salida):
            print(f"Archivo '{archivo_excel_salida}' guardado correctamente.")
        else:
            print(f"ERROR: El archivo '{archivo_excel_salida}' no se pudo crear.")

    except ImportError:
        print("ERROR: Necesitas instalar 'openpyxl' para escribir archivos Excel.")
        print("Ejecuta: pip install openpyxl  o  conda install openpyxl")
    except Exception as e:
        print(f"Ocurrió un error inesperado al guardar el archivo Excel: {e}")
else:
    print("Saltando Ejercicio 4 porque df_productos no se modificó correctamente.")


# --- Ejercicio 5: Lectura desde Excel ---
# Instrucciones:
# 1. Lee la hoja 'Inventario' del archivo Excel `archivo_excel_salida` (creado en el ejercicio anterior)
#    en un nuevo DataFrame llamado `df_desde_excel`.
# 2. Imprime las primeras filas de `df_desde_excel`.
# Maneja las excepciones si el archivo no existe o si falta la librería `openpyxl`.

print(f"\n--- Ejercicio 5: Lectura desde Excel ('{archivo_excel_salida}') ---")
if os.path.exists(archivo_excel_salida): # Solo intentar si el archivo existe
    try:
        # 1. Leer desde Excel
        df_desde_excel = pd.read_excel(archivo_excel_salida, sheet_name='Inventario')

        # 2. Imprimir head
        print("Primeras filas leídas desde Excel:")
        print(df_desde_excel.head())

    except FileNotFoundError:
         print(f"ERROR: No se encontró el archivo '{archivo_excel_salida}'.")
    except ImportError:
        print("ERROR: Necesitas instalar 'openpyxl' para leer archivos Excel.")
        print("Ejecuta: pip install openpyxl  o  conda install openpyxl")
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer el archivo Excel: {e}")
else:
    print(f"Saltando Ejercicio 5 porque '{archivo_excel_salida}' no existe.")


# --- Limpieza Opcional ---
# Descomenta estas líneas si quieres eliminar los archivos generados al final
# if os.path.exists(archivo_csv_salida):
#     os.remove(archivo_csv_salida)
#     print(f"\nArchivo '{archivo_csv_salida}' eliminado.")
# if os.path.exists(archivo_excel_salida):
#     os.remove(archivo_excel_salida)
#     print(f"Archivo '{archivo_excel_salida}' eliminado.")

# --- Fin de los ejercicios ---
