# Módulo 5: Introducción a Seaborn: Gráficos Estadísticos

Matplotlib es la base de la visualización en Python, pero para ciertos tipos de gráficos, especialmente los **estadísticos**, la biblioteca **Seaborn** ofrece una interfaz de más alto nivel que permite crear visualizaciones complejas y estéticamente agradables con menos código.

## ¿Qué es Seaborn?

*   Es una biblioteca de visualización de datos de Python **basada en Matplotlib**.
*   Proporciona una interfaz de alto nivel para dibujar gráficos estadísticos atractivos e informativos.
*   Se integra muy bien con estructuras de datos de **Pandas** (DataFrames).
*   Simplifica la creación de tipos de gráficos complejos como mapas de calor, violin plots, pair plots, etc.
*   Ofrece paletas de colores y estilos estéticos por defecto que suelen ser más agradables que los de Matplotlib base.

## Importando Seaborn

La convención estándar es importar Seaborn con el alias `sns`:

```python
import seaborn as sns
import matplotlib.pyplot as plt # A menudo se usa junto con Matplotlib para personalizar
import pandas as pd
import numpy as np

# Seaborn tiene estilos visuales incorporados
sns.set_theme(style="whitegrid") # Aplica un tema visual (opcional)
# Otros estilos: "darkgrid", "white", "ticks", "dark"
```

*(Nota: Si no tienes Seaborn instalado, abre tu Anaconda Prompt o terminal con tu entorno activado y ejecuta: `conda install seaborn` o `pip install seaborn`)*

## Gráficos Estadísticos Comunes con Seaborn

Seaborn sobresale en visualizar relaciones, distribuciones y comparaciones estadísticas. A menudo, puedes pasarle directamente un DataFrame de Pandas y especificar los nombres de las columnas para los ejes x, y, color (hue), etc.

**1. Gráfico de Dispersión con Regresión (`sns.regplot()` o `sns.lmplot()`):**

Muestra la relación entre dos variables numéricas y ajusta (y dibuja) automáticamente un modelo de regresión lineal.

```python
# Datos de ejemplo (reutilizando los de Matplotlib)
np.random.seed(42)
x_scatter = np.random.rand(50) * 10
y_scatter = 2 * x_scatter + 1 + np.random.randn(50) * 2
df_scatter = pd.DataFrame({'X': x_scatter, 'Y': y_scatter})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=df_scatter, scatter_kws={'s': 50, 'alpha': 0.7}, line_kws={'color': 'red'})
# scatter_kws y line_kws pasan argumentos a las funciones subyacentes de scatter y plot de Matplotlib

plt.title("Gráfico de Dispersión con Regresión (Seaborn)")
plt.show()

# sns.lmplot() es más potente, permite crear facetas (múltiples gráficos basados en categorías)
# sns.lmplot(x='X', y='Y', data=df_scatter)
# plt.show()
```

**2. Gráfico de Cajas (`sns.boxplot()`):**

Visualiza la distribución de una variable numérica a través de diferentes categorías. Muestra la mediana, los cuartiles, y los "bigotes" (whiskers) que indican el rango, además de posibles outliers.

```python
# Datos de ejemplo (reutilizando df_ventas de Pandas)
datos_ventas = {
    'Vendedor': ['Ana', 'Luis', 'Ana', 'Eva', 'Luis', 'Ana', 'Eva', 'Luis'],
    'Producto': ['A', 'B', 'A', 'C', 'D', 'B', 'C', 'A'],
    'Cantidad': [2, 5, 1, 2, 1, 3, 1, 2]
}
df_ventas = pd.DataFrame(datos_ventas)

plt.figure(figsize=(7, 5))
sns.boxplot(x='Vendedor', y='Cantidad', data=df_ventas, palette='pastel') # palette define esquema de colores

plt.title("Distribución de Cantidad por Vendedor (Boxplot)")
plt.show()
```

**3. Gráfico de Violín (`sns.violinplot()`):**

Similar al boxplot, pero también muestra la densidad de probabilidad de los datos en diferentes valores (la "forma" de la distribución). Es como combinar un boxplot con una estimación de densidad kernel (KDE).

```python
plt.figure(figsize=(7, 5))
sns.violinplot(x='Vendedor', y='Cantidad', data=df_ventas, palette='muted', inner='quartile')
# inner='quartile' muestra los cuartiles dentro del violín

plt.title("Distribución de Cantidad por Vendedor (Violinplot)")
plt.show()
```

**4. Mapa de Calor (`sns.heatmap()`):**

Visualiza datos matriciales (2D) donde los valores se representan mediante colores. Muy útil para mostrar matrices de correlación o confusión.

```python
# Datos de ejemplo: Matriz de correlación simulada
np.random.seed(10)
data_heatmap = np.random.rand(5, 5)
# Hacemos que sea simétrica como una matriz de correlación real (aproximado)
data_heatmap = (data_heatmap + data_heatmap.T) / 2
np.fill_diagonal(data_heatmap, 1) # Correlación consigo mismo es 1
columnas = ['Var1', 'Var2', 'Var3', 'Var4', 'Var5']
df_heatmap = pd.DataFrame(data_heatmap, index=columnas, columns=columnas)

plt.figure(figsize=(7, 6))
sns.heatmap(df_heatmap, annot=True, cmap='viridis', fmt=".2f", linewidths=.5)
# annot=True: muestra los valores en las celdas
# cmap='viridis': paleta de colores
# fmt=".2f": formato de los números anotados (2 decimales float)
# linewidths: líneas entre celdas

plt.title("Mapa de Calor (Ej: Matriz de Correlación)")
plt.show()
```

**5. Gráfico de Pares (`sns.pairplot()`):**

Crea una matriz de gráficos de dispersión para todas las combinaciones de variables numéricas en un DataFrame, y opcionalmente histogramas o KDEs en la diagonal. Es excelente para una visión rápida de las relaciones bivariadas.

```python
# Ejemplo con un dataset clásico de Seaborn (iris)
# Necesitarías conexión a internet la primera vez o tener el dataset
try:
    iris = sns.load_dataset("iris") # Carga dataset de ejemplo
    print("\nDataset Iris (primeras filas):")
    print(iris.head())

    # Crear pairplot, coloreando por especie
    sns.pairplot(iris, hue='species', markers=["o", "s", "D"])
    # hue='species': colorea los puntos según la columna 'species'

    plt.suptitle("Pairplot del Dataset Iris", y=1.02) # Título superior ajustado
    plt.show()
except Exception as e:
    print(f"\nNo se pudo cargar el dataset 'iris'. Error: {e}")
    print("Omitiendo ejemplo de pairplot.")

```

**6. Gráfico de Conteo (`sns.countplot()`):**

Muestra el número de ocurrencias de cada categoría en una variable categórica (similar a un histograma para categorías).

```python
plt.figure(figsize=(7, 5))
sns.countplot(x='Vendedor', data=df_ventas, palette='Set2', order=df_ventas['Vendedor'].value_counts().index)
# order: ordena las barras por frecuencia descendente

plt.title("Número de Ventas por Vendedor")
plt.show()
```

## Seaborn y Matplotlib Juntos

Como Seaborn se basa en Matplotlib, puedes usar funciones de `plt` para personalizar gráficos generados por Seaborn (añadir títulos, etiquetas, ajustar límites, etc.) después de haber llamado a la función de Seaborn.

```python
plt.figure(figsize=(7, 5))
sns.boxplot(x='Vendedor', y='Cantidad', data=df_ventas)
plt.title("Boxplot Personalizado con Matplotlib") # Título con plt
plt.xlabel("Nombre del Vendedor") # Etiqueta X con plt
plt.ylabel("Unidades Vendidas") # Etiqueta Y con plt
plt.ylim(0, 7) # Límite Y con plt
plt.grid(axis='y', linestyle='--', alpha=0.7) # Cuadrícula Y con plt
plt.show()
```

Seaborn simplifica enormemente la creación de gráficos estadísticos comunes y visualmente atractivos. Es una herramienta esencial para el análisis exploratorio de datos en Python, complementando perfectamente las capacidades de Matplotlib y Pandas.
