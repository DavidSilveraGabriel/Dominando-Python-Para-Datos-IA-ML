# Ejercicios: Módulo 4 - Combinación de DataFrames (`merge`, `join`, `concat`)

import pandas as pd

# --- DataFrames de Ejemplo ---
df_clientes = pd.DataFrame({
    'ID_Cliente': [1, 2, 3, 4, 5],
    'Nombre': ['Ana', 'Luis', 'Eva', 'Juan', 'Marta'],
    'Ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Sevilla', 'Valencia']
})

df_pedidos = pd.DataFrame({
    'ID_Pedido': [101, 102, 103, 104, 105, 106],
    'ID_Cliente': [2, 3, 1, 3, 5, 2], # Cliente 4 no tiene pedidos, Cliente 2 tiene dos pedidos
    'Producto': ['Teclado', 'Mouse', 'Monitor', 'Webcam', 'Mouse', 'Teclado'],
    'Cantidad': [1, 2, 1, 1, 3, 2]
})

df_info_adicional = pd.DataFrame({
    'ID_Cliente': [1, 2, 4, 6], # Cliente 3 y 5 no están, Cliente 6 no está en df_clientes
    'Email': ['ana@email.com', 'luis@email.com', 'juan@email.com', 'pedro@email.com'],
    'Telefono': ['111-222', '333-444', '555-666', '777-888']
})

df_categorias = pd.DataFrame({
    'Producto': ['Teclado', 'Mouse', 'Monitor', 'Webcam', 'Altavoces'], # Altavoces no está en pedidos
    'Categoria': ['Periférico', 'Periférico', 'Pantalla', 'Periférico', 'Audio']
})


print("--- DataFrames Originales ---")
print("Clientes (df_clientes):")
print(df_clientes)
print("\nPedidos (df_pedidos):")
print(df_pedidos)
print("\nInfo Adicional (df_info_adicional):")
print(df_info_adicional)
print("\nCategorías (df_categorias):")
print(df_categorias)
print("\n" + "="*30 + "\n")


# --- Ejercicio 1: `pd.merge()` Básico (Inner, Left, Right, Outer) ---
# Instrucciones:
# 1. Realiza un 'inner' merge entre `df_clientes` y `df_pedidos` usando 'ID_Cliente' como clave. Guarda en `df_inner`. Imprime el resultado. ¿Qué clientes/pedidos se incluyen?
# 2. Realiza un 'left' merge entre `df_clientes` y `df_pedidos` usando 'ID_Cliente'. Guarda en `df_left`. Imprime el resultado. ¿Qué pasa con el cliente que no tiene pedidos?
# 3. Realiza un 'right' merge entre `df_clientes` y `df_pedidos` usando 'ID_Cliente'. Guarda en `df_right`. Imprime el resultado. ¿Hay alguna diferencia significativa con el 'inner' en este caso? (Pista: ¿Todos los ID_Cliente en df_pedidos existen en df_clientes?)
# 4. Realiza un 'outer' merge entre `df_clientes` y `df_info_adicional` usando 'ID_Cliente'. Guarda en `df_outer`. Imprime el resultado. ¿Qué pasa con los clientes que solo están en uno de los DataFrames?

print("--- Ejercicio 1: pd.merge() Básico ---")
# Escribe tu código aquí
# 1. Inner Merge (Clientes y Pedidos)
df_inner = pd.merge(df_clientes, df_pedidos, on='ID_Cliente', how='inner')
print("\nInner Merge (Clientes y Pedidos):")
print(df_inner)
print("Incluye solo clientes (1, 2, 3, 5) que tienen pedidos.")
print("-" * 20)

# 2. Left Merge (Clientes y Pedidos)
df_left = pd.merge(df_clientes, df_pedidos, on='ID_Cliente', how='left')
print("\nLeft Merge (Clientes y Pedidos):")
print(df_left)
print("Incluye a todos los clientes. Cliente 4 (Juan) tiene NaN en las columnas de pedidos.")
print("-" * 20)

# 3. Right Merge (Clientes y Pedidos)
df_right = pd.merge(df_clientes, df_pedidos, on='ID_Cliente', how='right')
print("\nRight Merge (Clientes y Pedidos):")
print(df_right)
print("En este caso, es igual al Inner Merge porque todos los ID_Cliente en df_pedidos existen en df_clientes.")
print("-" * 20)

# 4. Outer Merge (Clientes e Info Adicional)
df_outer = pd.merge(df_clientes, df_info_adicional, on='ID_Cliente', how='outer')
print("\nOuter Merge (Clientes e Info Adicional):")
print(df_outer)
print("Incluye a todos los clientes de ambos DFs. Clientes 3 y 5 tienen NaN en Email/Telefono. Cliente 6 tiene NaN en Nombre/Ciudad.")
print("-" * 20)


print("\n--- Ejercicio 2: `pd.merge()` con Múltiples Claves y Sufijos ---")
# Instrucciones:
# 1. Crea un DataFrame `df_pedidos_con_categoria` haciendo un 'left' merge entre `df_pedidos` y `df_categorias` usando la columna 'Producto' como clave. Imprime el resultado. ¿Qué pasa con los productos que no tienen categoría definida en `df_categorias` (si los hubiera)?
# 2. Imagina que `df_clientes` tuviera una columna 'Fecha_Registro' y `df_pedidos` una columna 'Fecha_Pedido'. Si hicieras un merge y ambas columnas se llamaran 'Fecha', ¿qué pasaría? (Respuesta teórica). Ahora, realiza un 'inner' merge entre `df_clientes` y `df_pedidos` (usando 'ID_Cliente'), pero añade sufijos personalizados: `suffixes=('_cliente', '_pedido')`. Imprime el resultado y observa los nombres de las columnas.

# Escribe tu código aquí
# 1. Left Merge (Pedidos y Categorías)
df_pedidos_con_categoria = pd.merge(df_pedidos, df_categorias, on='Producto', how='left')
print("\nLeft Merge (Pedidos y Categorías):")
print(df_pedidos_con_categoria)
print("Todos los productos en df_pedidos tenían categoría en df_categorias.")
print("-" * 20)

# 2. Merge con Sufijos
# Respuesta teórica: Si hubiera columnas con el mismo nombre (ej. 'Fecha') que no son claves de unión,
# Pandas añadiría sufijos por defecto ('_x', '_y') para distinguirlas.
df_merge_sufijos = pd.merge(df_clientes, df_pedidos, on='ID_Cliente', how='inner', suffixes=('_cliente', '_pedido'))
print("\nInner Merge con Sufijos Personalizados:")
print(df_merge_sufijos)
print("Observa que no hay columnas solapadas (aparte de la clave), por lo que no se añadieron sufijos.")
# Para ver el efecto, podríamos renombrar una columna antes:
# df_clientes_temp = df_clientes.rename(columns={'Nombre': 'Nombre_o_Producto'})
# df_pedidos_temp = df_pedidos.rename(columns={'Producto': 'Nombre_o_Producto'})
# df_merge_sufijos_ej = pd.merge(df_clientes_temp, df_pedidos_temp, on='ID_Cliente', suffixes=('_cliente', '_pedido'))
# print(df_merge_sufijos_ej) # Aquí sí veríamos Nombre_o_Producto_cliente y Nombre_o_Producto_pedido
print("-" * 20)


print("\n--- Ejercicio 3: `df.join()` (Basado en Índice) ---")
# Instrucciones:
# 1. Establece 'ID_Cliente' como índice para `df_clientes` y `df_info_adicional`. Guarda los nuevos DataFrames como `df_clientes_idx` y `df_info_idx`.
# 2. Usa `df_clientes_idx.join()` para unir `df_info_idx`. Realiza un 'inner' join. Imprime el resultado.
# 3. Usa `df_clientes_idx.join()` para unir `df_info_idx`. Realiza un 'outer' join. Imprime el resultado.
# 4. Reinicia el índice de `df_clientes_idx` para volver a tener `df_clientes`. Ahora, usa `df_clientes.join()` para unir `df_info_idx` usando la columna 'ID_Cliente' del DataFrame izquierdo (`on='ID_Cliente'`) y el índice del derecho. Realiza un 'left' join. Imprime el resultado.

# Escribe tu código aquí
# 1. Establecer índices
df_clientes_idx = df_clientes.set_index('ID_Cliente')
df_info_idx = df_info_adicional.set_index('ID_Cliente')
print("\nDataFrames con Índice:")
print("df_clientes_idx:\n", df_clientes_idx)
print("df_info_idx:\n", df_info_idx)
print("-" * 20)

# 2. Inner Join con join()
df_join_inner = df_clientes_idx.join(df_info_idx, how='inner')
print("\nInner Join con join():")
print(df_join_inner)
print("-" * 20)

# 3. Outer Join con join()
df_join_outer = df_clientes_idx.join(df_info_idx, how='outer')
print("\nOuter Join con join():")
print(df_join_outer)
print("-" * 20)

# 4. Join usando columna 'on' y el índice del otro
df_join_on_col = df_clientes.join(df_info_idx, on='ID_Cliente', how='left')
print("\nLeft Join usando 'on' en el izquierdo y el índice en el derecho:")
print(df_join_on_col)
print("-" * 20)


print("\n--- Ejercicio 4: `pd.concat()` (Apilar DataFrames) ---")
# Instrucciones:
# 1. Crea dos DataFrames pequeños:
#    `df_a = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})`
#    `df_b = pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]})`
# 2. Concatena `df_a` y `df_b` verticalmente (`axis=0`). Imprime el resultado. Observa el índice.
# 3. Concatena `df_a` y `df_b` verticalmente, pero ignora los índices originales (`ignore_index=True`). Imprime el resultado.
# 4. Crea un tercer DataFrame: `df_c = pd.DataFrame({'col3': [9, 10], 'col4': [11, 12]})`
# 5. Concatena `df_a` y `df_c` horizontalmente (`axis=1`). Imprime el resultado. ¿Cómo se alinean?

# Escribe tu código aquí
# 1. Crear DataFrames pequeños
df_a = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df_b = pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]})
print("df_a:\n", df_a)
print("df_b:\n", df_b)
print("-" * 20)

# 2. Concatenar verticalmente (axis=0)
df_concat_v = pd.concat([df_a, df_b], axis=0)
print("\nConcatenación Vertical (axis=0):")
print(df_concat_v)
print("Índice original se mantiene (0, 1, 0, 1).")
print("-" * 20)

# 3. Concatenar verticalmente (ignore_index=True)
df_concat_v_ignore = pd.concat([df_a, df_b], axis=0, ignore_index=True)
print("\nConcatenación Vertical (ignore_index=True):")
print(df_concat_v_ignore)
print("Se crea un nuevo índice (0, 1, 2, 3).")
print("-" * 20)

# 4. Crear df_c
df_c = pd.DataFrame({'col3': [9, 10], 'col4': [11, 12]})
print("df_c:\n", df_c)
print("-" * 20)

# 5. Concatenar horizontalmente (axis=1)
df_concat_h = pd.concat([df_a, df_c], axis=1)
print("\nConcatenación Horizontal (axis=1):")
print(df_concat_h)
print("Se alinean por el índice (0 y 1 en este caso).")
print("-" * 20)

# --- Fin de los ejercicios ---
