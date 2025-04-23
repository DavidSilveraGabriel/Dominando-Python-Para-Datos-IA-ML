# Ejercicios: Módulo 4 - Agrupación de Datos (`groupby`)

import pandas as pd
import numpy as np

# --- DataFrame de Ejemplo ---
# Usaremos un DataFrame de ventas similar al de la lección
datos = {
    'Tienda': ['A', 'B', 'A', 'B', 'A', 'C', 'B', 'C', 'A', 'B'],
    'Producto': ['Manzana', 'Naranja', 'Manzana', 'Plátano', 'Naranja', 'Manzana', 'Naranja', 'Plátano', 'Manzana', 'Naranja'],
    'Ventas': [100, 150, 120, 200, 80, 90, 130, 210, 110, 160],
    'Clientes': [10, 12, 11, 15, 8, 9, 11, 16, 9, 14]
}
df_ventas = pd.DataFrame(datos)

print("DataFrame de Ventas original:")
print(df_ventas)
print("\n" + "="*30 + "\n")

# --- Ejercicio 1: Agrupación Simple y Agregación ---
# Instrucciones:
# 1. Agrupa `df_ventas` por la columna 'Tienda'. Guarda el objeto GroupBy en `grupos_por_tienda`.
# 2. Calcula la suma total de 'Ventas' para cada tienda usando el objeto `grupos_por_tienda`. Imprime el resultado.
# 3. Calcula la media de 'Clientes' para cada tienda. Imprime el resultado.
# 4. Cuenta el número de registros (ventas) en cada tienda usando `.size()`. Imprime el resultado.
# 5. Obtén el valor máximo de 'Ventas' para cada tienda. Imprime el resultado.

print("--- Ejercicio 1: Agrupación Simple y Agregación ---")
# Escribe tu código aquí
# 1. Agrupar por Tienda
grupos_por_tienda = df_ventas.groupby('Tienda')
print("Objeto GroupBy creado.")

# 2. Suma de Ventas por Tienda
suma_ventas_tienda = grupos_por_tienda['Ventas'].sum()
print("\nSuma de Ventas por Tienda:")
print(suma_ventas_tienda)
print("-" * 20)

# 3. Media de Clientes por Tienda
media_clientes_tienda = grupos_por_tienda['Clientes'].mean()
print("\nMedia de Clientes por Tienda:")
print(media_clientes_tienda)
print("-" * 20)

# 4. Número de registros por Tienda
num_registros_tienda = grupos_por_tienda.size()
print("\nNúmero de registros (ventas) por Tienda:")
print(num_registros_tienda)
print("-" * 20)

# 5. Venta máxima por Tienda
max_ventas_tienda = grupos_por_tienda['Ventas'].max()
print("\nVenta Máxima por Tienda:")
print(max_ventas_tienda)
print("-" * 20)


print("\n--- Ejercicio 2: Agrupación por Múltiples Columnas ---")
# Instrucciones:
# 1. Agrupa `df_ventas` primero por 'Tienda' y luego por 'Producto'. Guarda el objeto GroupBy en `grupos_tienda_prod`.
# 2. Calcula la suma de 'Ventas' para cada combinación de Tienda y Producto. Imprime el resultado (será una Serie con MultiIndex).
# 3. Calcula la media de 'Ventas' y 'Clientes' para cada combinación. Imprime el resultado (será un DataFrame con MultiIndex).

# Escribe tu código aquí
# 1. Agrupar por Tienda y Producto
grupos_tienda_prod = df_ventas.groupby(['Tienda', 'Producto'])
print("Objeto GroupBy (Tienda, Producto) creado.")

# 2. Suma de Ventas por Tienda y Producto
suma_ventas_tienda_prod = grupos_tienda_prod['Ventas'].sum()
print("\nSuma de Ventas por Tienda y Producto:")
print(suma_ventas_tienda_prod)
print("-" * 20)

# 3. Media de Ventas y Clientes por Tienda y Producto
media_tienda_prod = grupos_tienda_prod.mean() # Calcula media para columnas numéricas
print("\nMedia de Ventas y Clientes por Tienda y Producto:")
print(media_tienda_prod)
print("-" * 20)


print("\n--- Ejercicio 3: Agregación Múltiple con `.agg()` ---")
# Instrucciones:
# 1. Usando `grupos_por_tienda` (agrupado solo por 'Tienda'):
#    a. Aplica las funciones 'sum' y 'mean' a la columna 'Ventas'. Imprime el resultado.
#    b. Aplica la función 'count' a la columna 'Producto' (para contar cuántos productos diferentes se vendieron por tienda, aunque aquí se repiten) y 'mean' a la columna 'Clientes'. Usa un diccionario en `.agg()`. Imprime el resultado.
# 2. Usando `grupos_tienda_prod` (agrupado por 'Tienda' y 'Producto'):
#    a. Calcula la suma total de 'Ventas' y el número promedio de 'Clientes' para cada grupo. Renombra las columnas resultantes a 'Ventas_Totales' y 'Clientes_Promedio' usando la sintaxis de tupla en `.agg()`. Imprime el resultado.

# Escribe tu código aquí
# 1.a. agg en grupos_por_tienda ('Ventas')
print("Agregación múltiple en 'Ventas' por Tienda:")
agg_ventas = grupos_por_tienda['Ventas'].agg(['sum', 'mean'])
print(agg_ventas)
print("-" * 20)

# 1.b. agg en grupos_por_tienda (diccionario)
print("\nAgregación específica por columna por Tienda:")
agg_dict_tienda = grupos_por_tienda.agg({
    'Producto': 'count', # Cuenta ocurrencias de productos
    'Clientes': 'mean'
})
print(agg_dict_tienda)
print("-" * 20)

# 2.a. agg en grupos_tienda_prod con renombrado
print("\nAgregación con renombrado por Tienda y Producto:")
agg_renombrado_tienda_prod = grupos_tienda_prod.agg(
    Ventas_Totales=('Ventas', 'sum'),
    Clientes_Promedio=('Clientes', 'mean')
)
print(agg_renombrado_tienda_prod)
print("-" * 20)


print("\n--- Ejercicio 4: Iteración sobre Grupos ---")
# Instrucciones:
# 1. Itera sobre `grupos_por_tienda`. En cada iteración:
#    a. Imprime el nombre de la tienda.
#    b. Imprime las primeras 2 filas del sub-DataFrame correspondiente a esa tienda.
#    c. Calcula e imprime la diferencia entre la venta máxima y mínima dentro de esa tienda.

# Escribe tu código aquí
print("Iterando sobre grupos de Tienda:")
for nombre_tienda, df_grupo in grupos_por_tienda:
    print(f"\n--- Tienda: {nombre_tienda} ---")
    print("Primeras 2 filas del grupo:")
    print(df_grupo.head(2))
    rango_ventas = df_grupo['Ventas'].max() - df_grupo['Ventas'].min()
    print(f"Rango de Ventas (max - min): {rango_ventas}")
print("-" * 20)

# --- Fin de los ejercicios ---
