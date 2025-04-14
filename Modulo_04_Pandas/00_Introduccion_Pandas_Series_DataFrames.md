# Módulo 4: Introducción a Pandas: Series y DataFrames

¡Bienvenido/a al Módulo 4! Ahora que tenemos una base sólida en Python y NumPy, nos adentramos en **Pandas**, la biblioteca esencial para la **manipulación y análisis de datos** en Python.

## ¿Qué es Pandas?

Pandas es una biblioteca de código abierto que proporciona estructuras de datos de alto rendimiento y fáciles de usar, junto con herramientas de análisis de datos. Es fundamental para tareas como:

*   **Cargar y guardar datos** desde diversos formatos (CSV, Excel, bases de datos SQL, JSON, etc.).
*   **Limpiar y preparar datos** (manejo de valores faltantes, duplicados, transformación de tipos).
*   **Explorar y analizar datos** (selección, filtrado, agrupación, agregación).
*   **Combinar y remodelar conjuntos de datos**.
*   **Trabajar con series temporales**.

Pandas se construye sobre NumPy, lo que significa que aprovecha la eficiencia de los arrays de NumPy para sus operaciones, pero añade funcionalidades cruciales como **etiquetas (índices)** para filas y columnas, lo que hace que trabajar con datos tabulares sea mucho más intuitivo.

## Importando Pandas

La convención estándar para importar Pandas es usar el alias `pd`:

```python
import pandas as pd
import numpy as np # A menudo se usa junto con NumPy
```

*(Nota: Si no tienes Pandas instalado, abre tu Anaconda Prompt o terminal con tu entorno activado y ejecuta: `conda install pandas` o `pip install pandas`)*

## Estructuras de Datos Principales: Series y DataFrame

Pandas introduce dos estructuras de datos primarias:

### 1. Series

*   **¿Qué es?** Una **Serie** es un array **unidimensional etiquetado**, similar a una columna en una hoja de cálculo o una tabla SQL. Puede contener cualquier tipo de dato (enteros, strings, flotantes, objetos Python, etc.).
*   **Componentes:**
    *   **Valores:** La secuencia de datos (internamente, a menudo un array NumPy).
    *   **Índice (`index`):** Una secuencia de etiquetas asociadas a los valores. Si no se especifica, Pandas crea un índice numérico por defecto (0, 1, 2, ...). El índice no tiene por qué ser numérico, puede ser de strings, fechas, etc., y no tiene por qué ser único (aunque muchas operaciones funcionan mejor con índices únicos).

**Creando Series:**

```python
import pandas as pd
import numpy as np

# Desde una lista (índice por defecto)
datos_lista = [10, 20, 30, 40, 50]
serie_lista = pd.Series(datos_lista)
print(f"Serie desde lista:\n{serie_lista}\n")
# Salida:
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64

# Accediendo a valores e índice
print(f"Valores: {serie_lista.values}") # Devuelve un array NumPy
print(f"Índice: {serie_lista.index}")   # Devuelve un objeto Index

# Desde una lista con índice personalizado
indices = ['a', 'b', 'c', 'd', 'e']
serie_indice_str = pd.Series(datos_lista, index=indices)
print(f"Serie con índice string:\n{serie_indice_str}\n")
# Salida:
# a    10
# b    20
# c    30
# d    40
# e    50
# dtype: int64

# Desde un diccionario (claves se convierten en índice)
datos_dict = {'Juan': 25, 'Ana': 30, 'Luis': 22, 'Eva': 28}
serie_dict = pd.Series(datos_dict)
print(f"Serie desde diccionario:\n{serie_dict}\n")
# Salida:
# Juan    25
# Ana     30
# Luis    22
# Eva     28
# dtype: int64

# Desde un array NumPy
array_np = np.random.randn(4) # Array aleatorio
serie_np = pd.Series(array_np, index=['w', 'x', 'y', 'z'])
print(f"Serie desde NumPy array:\n{serie_np}\n")

# Acceso a elementos (similar a dict y array)
print(f"Elemento índice 'b': {serie_indice_str['b']}") # Salida: 20
print(f"Elemento índice 0: {serie_lista[0]}")       # Salida: 10
print(f"Elemento clave 'Luis': {serie_dict['Luis']}") # Salida: 22

# Slicing (funciona con índice numérico o etiquetas si está ordenado)
print(f"Slice por etiqueta 'b':'d':\n{serie_indice_str['b':'d']}\n") # Incluye 'd'
print(f"Slice por posición 1:3:\n{serie_lista[1:3]}\n") # Excluye índice 3
```

### 2. DataFrame

*   **¿Qué es?** Un **DataFrame** es una estructura de datos **bidimensional (tabular)**, similar a una hoja de cálculo, una tabla SQL o un diccionario de Series. Es la estructura de datos más utilizada en Pandas.
*   **Componentes:**
    *   **Datos:** Organizados en filas y columnas.
    *   **Índice (`index`):** Etiquetas para las **filas**.
    *   **Columnas (`columns`):** Etiquetas para las **columnas**. Cada columna es, en esencia, una Serie de Pandas.

**Creando DataFrames:**

```python
# Desde un diccionario de listas o arrays NumPy (claves son nombres de columna)
datos_df = {
    'Nombre': ['Ana', 'Luis', 'Eva', 'Carlos'],
    'Edad': [28, 34, 29, 42],
    'Ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Valencia']
}
df_dict = pd.DataFrame(datos_df)
print(f"DataFrame desde diccionario de listas:\n{df_dict}\n")

# Desde un array NumPy 2D, especificando nombres de columna e índice
array_2d = np.random.randint(10, 100, size=(4, 3)) # Matriz 4x3
indices_df = ['id1', 'id2', 'id3', 'id4']
columnas_df = ['ValorA', 'ValorB', 'ValorC']
df_np = pd.DataFrame(array_2d, index=indices_df, columns=columnas_df)
print(f"DataFrame desde array NumPy:\n{df_np}\n")

# Desde una lista de diccionarios
lista_dicts = [
    {'a': 1, 'b': 2},
    {'a': 5, 'b': 10, 'c': 20} # Pandas maneja columnas faltantes (NaN)
]
df_lista_dict = pd.DataFrame(lista_dicts)
print(f"DataFrame desde lista de diccionarios:\n{df_lista_dict}\n")
```

**Exploración Básica de DataFrames:**

```python
print(f"DataFrame de ejemplo (df_dict):\n{df_dict}\n")

# Ver las primeras filas
print(f"Primeras 2 filas (head(2)):\n{df_dict.head(2)}\n")

# Ver las últimas filas
print(f"Últimas 2 filas (tail(2)):\n{df_dict.tail(2)}\n")

# Obtener información general (tipos de datos, valores no nulos)
print("Información del DataFrame (info()):")
df_dict.info()
print("\n")

# Obtener estadísticas descriptivas para columnas numéricas
print(f"Estadísticas descriptivas (describe()):\n{df_dict.describe()}\n")

# Obtener el índice y las columnas
print(f"Índice: {df_dict.index}")
print(f"Columnas: {df_dict.columns}")
print(f"Valores (como array NumPy):\n{df_dict.values}\n")

# --- Selección Básica ---

# Seleccionar una columna (devuelve una Serie)
columna_edad = df_dict['Edad']
print(f"Columna 'Edad' (es una Serie):\n{columna_edad}\n")
print(f"Tipo de columna_edad: {type(columna_edad)}\n")

# Seleccionar múltiples columnas (devuelve un DataFrame)
columnas_nombre_ciudad = df_dict[['Nombre', 'Ciudad']]
print(f"Columnas 'Nombre' y 'Ciudad':\n{columnas_nombre_ciudad}\n")

# Selección de filas (introducción - veremos .loc y .iloc en detalle después)
# Por índice de fila (posición) usando slicing
print(f"Filas 1 y 2 (por posición):\n{df_dict[1:3]}\n")
```

Las Series y DataFrames son las herramientas fundamentales de Pandas. En las siguientes secciones, profundizaremos en cómo cargar datos en estas estructuras, cómo seleccionarlos y filtrarlos de maneras más avanzadas (`.loc`, `.iloc`), y cómo realizar operaciones de limpieza y transformación.
