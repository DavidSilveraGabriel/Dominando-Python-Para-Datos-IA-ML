# Módulo 5: Introducción a Matplotlib: Gráficos Básicos

¡Bienvenido/a al Módulo 5! Después de aprender a manipular datos con NumPy y Pandas, es hora de **visualizarlos**. La visualización de datos es crucial para entender patrones, tendencias, relaciones y para comunicar tus hallazgos de manera efectiva.

**Matplotlib** es la biblioteca de visualización más fundamental y ampliamente utilizada en el ecosistema científico de Python. Sirve como base para muchas otras bibliotecas de visualización (como Seaborn).

## ¿Qué es Matplotlib?

*   Es una biblioteca completa para crear visualizaciones estáticas, animadas e interactivas en Python.
*   Ofrece un control muy detallado sobre cada aspecto de un gráfico (figuras, ejes, líneas, texto, etc.).
*   Su interfaz más comúnmente utilizada es `matplotlib.pyplot`, que proporciona una interfaz similar a MATLAB para crear gráficos rápidamente.

## Importando Matplotlib

La convención estándar es importar el módulo `pyplot` con el alias `plt`:

```python
import matplotlib.pyplot as plt
import numpy as np # Necesario para generar datos de ejemplo
import pandas as pd # A menudo se usa para preparar los datos
```

*(Nota: Si no tienes Matplotlib instalado, abre tu Anaconda Prompt o terminal con tu entorno activado y ejecuta: `conda install matplotlib` o `pip install matplotlib`)*

**Configuración para Jupyter Notebook/Lab (Importante):**

Si estás trabajando en un entorno como Jupyter Notebook o JupyterLab, a menudo querrás que los gráficos aparezcan directamente en tu notebook. Puedes usar la "magic command":

```python
%matplotlib inline
```
Coloca esta línea en una celda al principio de tu notebook. Hará que los gráficos se muestren debajo de la celda donde se generan. Alternativamente, `%matplotlib notebook` o `%matplotlib widget` pueden habilitar gráficos interactivos dentro del notebook (pueden requerir instalación adicional).

## Anatomía Básica de un Gráfico Matplotlib

*   **Figure (Figura):** Es el contenedor de nivel superior para todos los elementos del gráfico. Puedes pensar en ella como el lienzo completo. Una figura puede contener uno o más `Axes`.
*   **Axes (Ejes):** Es el área donde se dibujan los datos con sus coordenadas (el gráfico en sí). Un objeto `Axes` tiene un eje X (`xaxis`) y un eje Y (`yaxis`), y puede tener títulos, etiquetas, etc. **No confundir `Axes` (el objeto de trazado) con `axis` (la dimensión de un array NumPy).**
*   **Axis (Eje):** Objetos que controlan los límites de los datos, las marcas (ticks) y las etiquetas de las marcas (ticklabels).

## Creando Gráficos Básicos con `pyplot`

La interfaz `pyplot` (`plt`) mantiene un estado interno. Cuando llamas a funciones como `plt.plot()`, opera sobre la figura y los ejes "actuales".

**1. Gráfico de Líneas (`plt.plot()`):** Ideal para visualizar tendencias a lo largo del tiempo o secuencias ordenadas.

```python
# Datos de ejemplo
x = np.linspace(0, 10, 100) # 100 puntos entre 0 y 10
y_seno = np.sin(x)
y_coseno = np.cos(x)

# Crear la figura y los ejes implícitamente con pyplot
plt.figure(figsize=(8, 4)) # Opcional: define el tamaño de la figura

plt.plot(x, y_seno, label='Seno(x)')    # Grafica y vs x para el seno
plt.plot(x, y_coseno, label='Coseno(x)') # Grafica y vs x para el coseno

# Añadir elementos al gráfico
plt.title("Gráfico de Seno y Coseno") # Título del gráfico
plt.xlabel("Eje X")                   # Etiqueta del eje X
plt.ylabel("Eje Y")                   # Etiqueta del eje Y
plt.legend()                          # Muestra la leyenda (basada en 'label')
plt.grid(True)                        # Añade una cuadrícula

# Mostrar el gráfico
plt.show() # Necesario si no usas %matplotlib inline o similar
```

**2. Gráfico de Dispersión (`plt.scatter()`):** Útil para visualizar la relación entre dos variables numéricas.

```python
# Datos de ejemplo
np.random.seed(42)
x_scatter = np.random.rand(50) * 10 # 50 valores aleatorios entre 0 y 10
y_scatter = 2 * x_scatter + 1 + np.random.randn(50) * 2 # y = 2x + 1 + ruido

plt.figure(figsize=(7, 5))
plt.scatter(x_scatter, y_scatter, label='Datos Observados', color='red', marker='o') # x, y, etiqueta, color, marcador

plt.title("Gráfico de Dispersión")
plt.xlabel("Variable X")
plt.ylabel("Variable Y")
plt.legend()
plt.grid(True)
plt.show()
```

**3. Gráfico de Barras (`plt.bar()`):** Bueno para comparar cantidades entre diferentes categorías.

```python
# Datos de ejemplo
categorias = ['A', 'B', 'C', 'D']
valores = [23, 45, 56, 12]

plt.figure(figsize=(6, 4))
plt.bar(categorias, valores, color=['skyblue', 'lightgreen', 'salmon', 'gold']) # Categorías, alturas, colores opcionales

plt.title("Gráfico de Barras")
plt.xlabel("Categoría")
plt.ylabel("Valor")
# plt.xticks(rotation=45) # Opcional: rotar etiquetas del eje x si son largas
plt.show()
```

**4. Histograma (`plt.hist()`):** Muestra la distribución de una única variable numérica dividiendo los datos en "bins" (intervalos) y contando cuántas observaciones caen en cada bin.

```python
# Datos de ejemplo (distribución normal)
datos_hist = np.random.randn(1000) # 1000 puntos de una normal estándar

plt.figure(figsize=(7, 5))
plt.hist(datos_hist, bins=30, color='lightblue', edgecolor='black') # Datos, número de bins, color, borde

plt.title("Histograma")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()
```

## El Enfoque Orientado a Objetos (Más Control)

Aunque `pyplot` es rápido para gráficos simples, para mayor control y gráficos más complejos (ej. múltiples subgráficos en una figura), se prefiere el enfoque orientado a objetos.

1.  Creas explícitamente una `Figure` y uno o más `Axes` (subgráficos).
2.  Llamas a los métodos de trazado directamente sobre el objeto `Axes` (ej. `ax.plot()`, `ax.scatter()`).

```python
# Datos
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Crear figura y ejes explícitamente
fig, ax = plt.subplots(figsize=(8, 4)) # Crea una figura y un conjunto de ejes (ax)

# Usar los métodos del objeto 'ax'
ax.plot(x, y1, label='Seno')
ax.plot(x, y2, label='Coseno')

# Configurar usando métodos de 'ax'
ax.set_title("Gráfico OO de Seno y Coseno")
ax.set_xlabel("Radianes")
ax.set_ylabel("Valor")
ax.legend()
ax.grid(True)

plt.show() # Sigue siendo necesario para mostrar la figura
```

Este enfoque OO es más verboso pero mucho más flexible y es el recomendado para desarrollar gráficos complejos o reutilizables.

Matplotlib es una herramienta vasta. Hemos cubierto solo lo básico. En la siguiente sección, veremos cómo personalizar más estos gráficos (colores, estilos de línea, marcadores, anotaciones) y luego introduciremos Seaborn, que se basa en Matplotlib para crear gráficos estadísticos más atractivos con menos código.
# Módulo 5: Personalización de Gráficos con Matplotlib

Los gráficos básicos que creamos con Matplotlib son funcionales, pero a menudo queremos personalizarlos para mejorar su claridad, estética o para resaltar información específica. Matplotlib ofrece un control muy granular sobre casi todos los elementos de un gráfico.

```python
import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
x = np.linspace(0, 10, 50) # 50 puntos entre 0 y 10
y1 = np.sin(x)
y2 = np.cos(x)
y3 = y1 * 0.5
y4 = y2 * 0.5

# Usaremos el enfoque OO para mayor claridad en la personalización
fig, ax = plt.subplots(figsize=(10, 6)) # Crear figura y ejes
```

## Colores, Estilos de Línea y Marcadores

Puedes controlar la apariencia de las líneas y puntos en `plot()` y `scatter()` con varios argumentos:

*   **`color`**: Especifica el color. Puedes usar:
    *   Nombres de color básicos (ej. `'blue'`, `'green'`, `'red'`, `'cyan'`, `'magenta'`, `'yellow'`, `'black'`, `'white'`).
    *   Códigos de formato corto (ej. `'b'`, `'g'`, `'r'`, `'c'`, `'m'`, `'y'`, `'k'`, `'w'`).
    *   Escala de grises (string de un número entre 0 y 1, ej. `'0.75'`).
    *   Códigos hexadecimales (ej. `'#FFDD44'`, `'#aaccff'`).
    *   Tuplas RGB o RGBA (ej. `(0.1, 0.2, 0.5)`, `(0.1, 0.2, 0.5, 0.8)` con transparencia alfa).
*   **`linestyle` o `ls`**: Define el estilo de la línea:
    *   `'-'` o `'solid'` (sólida - por defecto)
    *   `'--'` o `'dashed'` (discontinua)
    *   `':'` o `'dotted'` (punteada)
    *   `'-.'` o `'dashdot'` (raya-punto)
    *   `'None'` o `' '` (sin línea)
*   **`linewidth` o `lw`**: Grosor de la línea (número flotante).
*   **`marker`**: El tipo de marcador para cada punto de datos:
    *   `'.'` (punto)
    *   `','` (píxel)
    *   `'o'` (círculo)
    *   `'v'`, `'^'`, `'<'`, `'>'` (triángulos)
    *   `'s'` (cuadrado - square)
    *   `'p'` (pentágono)
    *   `'*'` (estrella)
    *   `'+'` (más)
    *   `'x'` (equis)
    *   `'D'` (diamante)
    *   Y muchos más...
*   **`markersize` o `ms`**: Tamaño del marcador.
*   **`markerfacecolor`**, **`markeredgecolor`**: Colores del relleno y borde del marcador.

**Formato Abreviado:** Puedes combinar color, marcador y estilo de línea en una sola cadena de formato (ej. `'ro--'` para rojo, círculos, línea discontinua).

```python
# --- Personalizando plot() ---
ax.plot(x, y1, color='blue', linestyle='-', linewidth=2, marker='o', markersize=5, label='Seno (Azul, Sólido, Círculo)')
ax.plot(x, y2, color='#FF8C00', ls='--', lw=1.5, marker='x', ms=6, label='Coseno (Naranja, Discontinuo, X)') # Naranja oscuro
ax.plot(x, y3, 'g:^', label='0.5*Seno (Verde, Punteado, Triángulo)') # Formato abreviado
ax.plot(x, y4, color=(0.5, 0.2, 0.8), linestyle='None', marker='s', label='0.5*Coseno (Púrpura, Sin línea, Cuadrado)')

ax.set_title("Gráfico Personalizado")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.legend(loc='lower left') # Ubicación de la leyenda
ax.grid(True, linestyle=':', alpha=0.7) # Cuadrícula personalizada

# plt.show() # Mostramos al final después de más personalizaciones
```

## Límites de los Ejes

Puedes controlar el rango visible de los ejes X e Y.

*   `plt.xlim(min, max)`, `plt.ylim(min, max)` (interfaz pyplot)
*   `ax.set_xlim(min, max)`, `ax.set_ylim(min, max)` (interfaz OO)
*   `ax.axis([xmin, xmax, ymin, ymax])`: Establece ambos límites a la vez.
*   `ax.axis('tight')`: Ajusta los límites para que encajen justo los datos.
*   `ax.axis('equal')`: Asegura que las escalas en X e Y sean iguales (útil para círculos).

```python
# Establecer límites específicos
ax.set_xlim(-1, 11)
ax.set_ylim(-1.5, 1.5)

# Podríamos haber usado: ax.axis([-1, 11, -1.5, 1.5])
```

## Etiquetas, Títulos y Leyendas

Ya hemos visto lo básico:

*   `plt.title()`, `plt.xlabel()`, `plt.ylabel()` / `ax.set_title()`, `ax.set_xlabel()`, `ax.set_ylabel()`
*   `plt.legend()` / `ax.legend()`: Requiere que hayas añadido la etiqueta `label='...'` en las llamadas a `plot()`. Puedes controlar la ubicación con `loc` (ej. `'upper right'`, `'lower left'`, `'center'`, `'best'`).

## Texto y Anotaciones

Puedes añadir texto en cualquier lugar del gráfico o anotaciones que señalen puntos específicos.

*   **`plt.text(x, y, 'texto')` / `ax.text(x, y, 'texto', ...)`**: Añade texto en las coordenadas `(x, y)` (en términos de los datos). Puedes personalizar fuente, tamaño, color, alineación, etc.
*   **`plt.annotate('texto', xy=(px, py), xytext=(tx, ty), arrowprops=dict(...))` / `ax.annotate(...)`**: Añade una anotación.
    *   `'texto'`: El texto de la anotación.
    *   `xy=(px, py)`: La coordenada del punto al que se quiere señalar (en datos).
    *   `xytext=(tx, ty)`: La coordenada donde se quiere colocar el texto.
    *   `arrowprops`: Un diccionario para configurar la flecha que conecta `xytext` con `xy` (ej. `arrowstyle='->'`, `connectionstyle='arc3,rad=.2'`, `color='gray'`).

```python
# Añadir texto
ax.text(1, 1, "Texto en (1, 1)", fontsize=12, color='darkred')

# Añadir una anotación
punto_interesante_x = x[25] # Aproximadamente pi/2
punto_interesante_y = y1[25] # El pico del seno
ax.annotate('Pico del Seno',
            xy=(punto_interesante_x, punto_interesante_y), # Punto a señalar
            xytext=(punto_interesante_x + 1, punto_interesante_y + 0.5), # Posición del texto
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8))
```

## Escalas Logarítmicas

Para datos que abarcan varios órdenes de magnitud, una escala logarítmica puede ser más apropiada.

*   `plt.xscale('log')`, `plt.yscale('log')`
*   `ax.set_xscale('log')`, `ax.set_yscale('log')`

```python
# Ejemplo rápido de escala log (en un nuevo gráfico para no mezclar)
fig_log, ax_log = plt.subplots()
x_log = np.linspace(1, 100, 100)
y_log = x_log**2
ax_log.plot(x_log, y_log)
ax_log.set_yscale('log') # Poner eje Y en escala logarítmica
ax_log.set_title("Gráfico con Eje Y Logarítmico")
# plt.show() # Mostraría este gráfico logarítmico
```

## Guardando Figuras (`savefig()`)

Puedes guardar tus gráficos en archivos de imagen (PNG, JPG, PDF, SVG, etc.).

*   `plt.savefig('nombre_archivo.png')` (interfaz pyplot)
*   `fig.savefig('nombre_archivo.png')` (interfaz OO - recomendado)

**Parámetros útiles:**

*   `dpi`: Puntos por pulgada (resolución).
*   `bbox_inches='tight'`: Intenta ajustar la figura para que no se corten las etiquetas.
*   `transparent=True`: Fondo transparente.

```python
# Guardar la figura principal que hemos estado personalizando
try:
    fig.savefig("grafico_personalizado.png", dpi=300, bbox_inches='tight')
    print("\nGráfico guardado como 'grafico_personalizado.png'")
except Exception as e:
    print(f"\nError guardando gráfico: {e}")

# Finalmente, mostrar el gráfico principal
plt.show()
```

Matplotlib ofrece muchísimas más opciones de personalización (ticks de los ejes, subplots múltiples, gráficos 3D, etc.). Explorar la galería de ejemplos de Matplotlib ([https://matplotlib.org/stable/gallery/index.html](https://matplotlib.org/stable/gallery/index.html)) es una excelente manera de descubrir lo que es posible y encontrar inspiración.
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
# Módulo 5: Visualización de Relaciones, Distribuciones y Categorías con Seaborn

Seaborn organiza sus funciones de trazado en categorías basadas en el tipo de información que ayudan a visualizar. Las principales categorías son:

1.  **Gráficos Relacionales:** Muestran la relación entre dos variables numéricas (`scatterplot`, `lineplot`).
2.  **Gráficos de Distribución:** Visualizan la distribución de una o más variables (`histplot`, `kdeplot`, `ecdfplot`, `rugplot`).
3.  **Gráficos Categóricos:** Muestran la relación entre una variable numérica y una (o más) variables categóricas (`stripplot`, `swarmplot`, `boxplot`, `violinplot`, `boxenplot`, `pointplot`, `barplot`, `countplot`).

Muchas de estas funciones comparten una API similar y pueden combinarse o usarse a través de funciones de "nivel de figura" como `relplot()`, `displot()`, y `catplot()` que facilitan la creación de múltiples subgráficos (facetas).

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Cargar dataset de ejemplo 'tips' (propinas en un restaurante)
try:
    tips = sns.load_dataset("tips")
    print("Dataset 'tips' (primeras filas):")
    print(tips.head())
except Exception as e:
    print(f"No se pudo cargar el dataset 'tips'. Error: {e}")
    # Crear un DataFrame de respaldo si falla la carga
    tips_data = {
        'total_bill': np.random.rand(50) * 40 + 10,
        'tip': lambda df: df['total_bill'] * (np.random.rand(50) * 0.1 + 0.1),
        'sex': np.random.choice(['Male', 'Female'], 50),
        'smoker': np.random.choice(['Yes', 'No'], 50),
        'day': np.random.choice(['Thur', 'Fri', 'Sat', 'Sun'], 50),
        'time': np.random.choice(['Lunch', 'Dinner'], 50),
        'size': np.random.randint(1, 6, 50)
    }
    # La lambda necesita acceso al df parcial, lo hacemos en dos pasos
    tips = pd.DataFrame(tips_data)
    tips['tip'] = tips.apply(tips_data['tip'], axis=0) # type: ignore
    print("\nUsando DataFrame de respaldo para 'tips'.")

print("\n" + "="*30 + "\n")
```

## 1. Gráficos Relacionales (`relplot`, `scatterplot`, `lineplot`)

*   **`sns.scatterplot()`**: El gráfico de dispersión básico. Muestra la relación entre dos variables numéricas. Se pueden añadir variables semánticas como `hue` (color), `size` (tamaño del punto) y `style` (estilo del marcador) para representar dimensiones adicionales.
*   **`sns.lineplot()`**: Dibuja una línea conectando puntos de datos, útil para visualizar tendencias, a menudo a lo largo del tiempo. Puede mostrar la media y un intervalo de confianza si hay múltiples observaciones para cada punto x.
*   **`sns.relplot()`**: Función de nivel de figura que usa `scatterplot` o `lineplot` (controlado por `kind=`) por debajo. Su principal ventaja es que permite crear fácilmente **facetas** (subplots) basadas en categorías usando los argumentos `col` y `row`.

```python
print("--- Gráficos Relacionales ---")

# Scatterplot básico: propina vs cuenta total
plt.figure(figsize=(7, 5)) # Necesario si no usamos relplot
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Propina vs Cuenta Total (scatterplot)")
plt.show()

# Scatterplot con semántica adicional (hue, size, style)
plt.figure(figsize=(9, 6))
sns.scatterplot(x="total_bill", y="tip", hue="smoker", style="time", size="size", data=tips, alpha=0.8)
plt.title("Propina vs Cuenta Total (con Semántica)")
plt.show()

# Lineplot (útil si tuviéramos datos a lo largo del tiempo, aquí solo como ejemplo)
# Ordenamos por total_bill para que la línea tenga sentido
tips_sorted = tips.sort_values("total_bill")
plt.figure(figsize=(8, 5))
sns.lineplot(x="total_bill", y="tip", data=tips_sorted, marker='o')
plt.title("Propina vs Cuenta Total (lineplot - ejemplo)")
plt.show()

# Usando relplot para crear facetas
# Gráficos de dispersión separados por día (columnas) y tiempo (filas)
sns.relplot(x="total_bill", y="tip", data=tips,
            kind="scatter", # tipo de gráfico subyacente
            col="day",      # columnas basadas en la categoría 'day'
            row="time",     # filas basadas en la categoría 'time'
            hue="smoker",   # color basado en 'smoker'
            col_order=['Thur', 'Fri', 'Sat', 'Sun']) # Orden específico para columnas
plt.suptitle("Propina vs Cuenta (Facetas con relplot)", y=1.03)
plt.show()
```

## 2. Gráficos de Distribución (`displot`, `histplot`, `kdeplot`, `ecdfplot`)

*   **`sns.histplot()`**: Crea histogramas para visualizar la distribución de una variable numérica. Puede superponer una curva KDE.
*   **`sns.kdeplot()`**: Estima y dibuja la Densidad de Probabilidad Kernel (Kernel Density Estimate), una versión suavizada del histograma. Puede visualizar distribuciones univariadas o bivariadas.
*   **`sns.ecdfplot()`**: Dibuja la Función de Distribución Acumulada Empírica. Muestra la proporción de datos por debajo de cada valor x.
*   **`sns.displot()`**: Función de nivel de figura para gráficos de distribución (`histplot`, `kdeplot`, `ecdfplot`). Permite crear facetas con `col` y `row`, y superponer diferentes tipos de gráficos.

```python
print("\n--- Gráficos de Distribución ---")

# Histograma de la cuenta total
plt.figure(figsize=(7, 5))
sns.histplot(data=tips, x="total_bill", bins=20, kde=True) # kde=True añade curva KDE
plt.title("Distribución de la Cuenta Total (histplot)")
plt.show()

# KDE de la cuenta total
plt.figure(figsize=(7, 5))
sns.kdeplot(data=tips, x="total_bill", fill=True, color='skyblue') # fill=True rellena el área
plt.title("Estimación de Densidad Kernel (KDE) de la Cuenta Total")
plt.show()

# KDE bivariado (relación de densidad entre dos variables)
sns.kdeplot(data=tips, x="total_bill", y="tip", cmap="Blues", fill=True)
plt.title("KDE Bivariado (Cuenta vs Propina)")
plt.show()

# Usando displot para histogramas facetados por día
sns.displot(data=tips, x="total_bill", col="day", kde=True,
            col_order=['Thur', 'Fri', 'Sat', 'Sun'])
plt.suptitle("Distribución de Cuenta por Día (displot)", y=1.03)
plt.show()

# Usando displot para KDEs superpuestos por sexo
sns.displot(data=tips, x="tip", kind="kde", hue="sex", fill=True)
plt.title("Distribución de Propina por Sexo (KDE con displot)")
plt.show()
```

## 3. Gráficos Categóricos (`catplot`, `boxplot`, `violinplot`, `barplot`, `countplot`, etc.)

Estos gráficos muestran la relación entre una variable numérica y una o más variables categóricas.

*   **Gráficos de dispersión categóricos:**
    *   `sns.stripplot()`: Gráfico de dispersión donde un eje es categórico (puede haber solapamiento).
    *   `sns.swarmplot()`: Similar a `stripplot`, pero ajusta los puntos para evitar solapamiento (no escala bien a muchos datos).
*   **Gráficos de distribución categóricos:**
    *   `sns.boxplot()`: Muestra cuartiles y outliers por categoría.
    *   `sns.violinplot()`: Combina boxplot con KDE por categoría.
    *   `sns.boxenplot()`: Variante del boxplot, mejor para datasets grandes, muestra más cuantiles.
*   **Gráficos de estimación estadística categóricos:**
    *   `sns.pointplot()`: Muestra la estimación puntual (ej. media) y el intervalo de confianza.
    *   `sns.barplot()`: Muestra la estimación puntual (media por defecto) como altura de barra.
    *   `sns.countplot()`: Muestra el conteo de observaciones en cada categoría (como un histograma categórico).
*   **`sns.catplot()`**: Función de nivel de figura para gráficos categóricos. Permite usar cualquiera de los tipos anteriores (con `kind=`) y crear facetas con `col` y `row`.

```python
print("\n--- Gráficos Categóricos ---")

# Boxplot: propina por día de la semana
plt.figure(figsize=(8, 5))
sns.boxplot(x="day", y="tip", data=tips, order=['Thur', 'Fri', 'Sat', 'Sun'])
plt.title("Propina por Día de la Semana (boxplot)")
plt.show()

# Violinplot: cuenta total por día, separado por fumador (hue)
plt.figure(figsize=(10, 6))
sns.violinplot(x="day", y="total_bill", hue="smoker", data=tips,
               split=True, # Dibuja medios violines para comparar hue
               order=['Thur', 'Fri', 'Sat', 'Sun'], palette='muted')
plt.title("Cuenta Total por Día y Fumador (violinplot)")
plt.show()

# Barplot: muestra la media de la propina por día (por defecto calcula media)
plt.figure(figsize=(8, 5))
sns.barplot(x="day", y="tip", data=tips, order=['Thur', 'Fri', 'Sat', 'Sun'],
            palette="viridis", errorbar='sd') # errorbar='sd' muestra desviación estándar
plt.title("Propina Media por Día (barplot)")
plt.show()

# Countplot: número de comidas por día
plt.figure(figsize=(8, 5))
sns.countplot(x="day", data=tips, order=['Thur', 'Fri', 'Sat', 'Sun'], palette='Set1')
plt.title("Número de Comidas por Día (countplot)")
plt.show()

# Usando catplot para un barplot facetado por tiempo
sns.catplot(x="day", y="total_bill", data=tips, kind="bar", # kind="bar" especifica barplot
            col="time", # Facetas por columna
            order=['Thur', 'Fri', 'Sat', 'Sun'],
            height=4, aspect=1.2) # Controla tamaño de facetas
plt.suptitle("Cuenta Media por Día y Momento (catplot)", y=1.03)
plt.show()
```

Seaborn ofrece una manera conveniente y potente de crear rápidamente visualizaciones estadísticas informativas. Al combinarlo con Matplotlib para ajustes finos, puedes crear gráficos de calidad profesional para explorar y comunicar tus análisis de datos.
# Módulo 5: (Opcional) Gráficos Interactivos (Plotly / Streamlit)

Si bien Matplotlib y Seaborn son fantásticos para crear gráficos estáticos de alta calidad, a veces necesitas que tus visualizaciones sean **interactivas**. La interactividad permite a los usuarios (o a ti mismo) explorar los datos de forma más dinámica: hacer zoom, desplazarse (pan), pasar el ratón por encima para ver valores (hover), seleccionar subconjuntos, etc.

Dos bibliotecas populares en Python para crear visualizaciones interactivas y dashboards son **Plotly** y **Streamlit** (que a menudo usa Plotly u otras bibliotecas por debajo).

*(Nota: Esta es una introducción básica. Estas bibliotecas son muy extensas y potentes.)*

## Plotly

*   **¿Qué es?** Plotly es una biblioteca de gráficos de Python que crea visualizaciones interactivas y de calidad de publicación. Puede generar gráficos HTML independientes o integrarse en aplicaciones web y notebooks.
*   **Plotly Express:** Es una interfaz de alto nivel para Plotly (similar a Seaborn para Matplotlib) que facilita la creación de muchos tipos de gráficos comunes con muy poco código.
*   **Ventajas:** Gráficos muy atractivos, interactividad incorporada (zoom, pan, hover), amplio rango de tipos de gráficos (incluyendo 3D, mapas, financieros), exportación a HTML.

**Instalación:**
`conda install plotly` o `pip install plotly`
`conda install -c plotly plotly-express` o `pip install plotly-express`

**Ejemplo Básico con Plotly Express:**

```python
import plotly.express as px
import pandas as pd

# Usar el dataset 'tips' de Seaborn (o tu propio DataFrame)
try:
    tips = px.data.tips() # Plotly express tiene datasets de ejemplo
    print("Dataset 'tips' de Plotly Express:")
    print(tips.head())
except Exception as e:
    print(f"No se pudo cargar dataset 'tips' de Plotly. Error: {e}")
    # Crear DataFrame de respaldo si falla
    tips_data = {
        'total_bill': np.random.rand(50) * 40 + 10,
        'tip': lambda df: df['total_bill'] * (np.random.rand(50) * 0.1 + 0.1),
        'sex': np.random.choice(['Male', 'Female'], 50),
        'smoker': np.random.choice(['Yes', 'No'], 50),
        'day': np.random.choice(['Thur', 'Fri', 'Sat', 'Sun'], 50),
        'time': np.random.choice(['Lunch', 'Dinner'], 50),
        'size': np.random.randint(1, 6, 50)
    }
    tips = pd.DataFrame(tips_data)
    tips['tip'] = tips.apply(tips_data['tip'], axis=0) # type: ignore
    print("\nUsando DataFrame de respaldo para 'tips'.")


print("\n--- Gráfico Interactivo con Plotly Express ---")

# Scatter plot interactivo
# Similar a Seaborn, pasas el DataFrame y los nombres de columna
fig_scatter_px = px.scatter(tips, x="total_bill", y="tip",
                            color="sex", # Color por sexo
                            size="size", # Tamaño del punto por tamaño de grupo
                            hover_data=['day', 'smoker'], # Datos extra al pasar el ratón
                            title="Propina vs Cuenta Total (Plotly Express)")

# Mostrar el gráfico (se abrirá en el navegador o se incrustará en el notebook)
fig_scatter_px.show()

# Bar plot interactivo
tips_grouped_day = tips.groupby('day')['total_bill'].mean().reset_index()
fig_bar_px = px.bar(tips_grouped_day, x='day', y='total_bill',
                    color='day', # Colorear barras por día
                    title="Cuenta Promedio por Día (Plotly Express)",
                    labels={'total_bill': 'Cuenta Promedio ($)'}) # Renombrar ejes

fig_bar_px.show()
```

*   Al ejecutar `.show()`, Plotly genera un archivo HTML temporal y lo abre en tu navegador, o si estás en un entorno compatible (como JupyterLab con las extensiones correctas), puede mostrarlo directamente.
*   ¡Interactúa con los gráficos! Prueba hacer zoom, seleccionar, pasar el ratón por encima.

## Streamlit

*   **¿Qué es?** Streamlit es un framework de Python de código abierto para crear y compartir **aplicaciones web personalizadas para machine learning y ciencia de datos** de forma increíblemente rápida y sencilla. No es una biblioteca de gráficos *per se*, pero facilita enormemente la integración de gráficos (de Plotly, Matplotlib, Seaborn, etc.) en una interfaz web interactiva con widgets (sliders, botones, menús desplegables).
*   **Ventajas:** Muy fácil de aprender, convierte scripts de Python en apps web con pocas líneas de código extra, ideal para crear prototipos, dashboards interactivos y compartir resultados sin ser un experto en desarrollo web frontend.

**Instalación:**
`pip install streamlit` o `conda install streamlit`

**Ejemplo Básico con Streamlit:**

1.  **Crea un archivo Python** (ej. `mi_app_streamlit.py`).
2.  **Escribe tu código Streamlit:**

    ```python
    # Contenido de mi_app_streamlit.py
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px

    # --- Título y Texto ---
    st.title("Mi Primera App con Streamlit")
    st.write("¡Explorando el dataset de propinas!")

    # --- Cargar Datos (similar a antes) ---
    # (Podrías cargar desde un CSV aquí también: df = pd.read_csv(...) )
    @st.cache_data # Cachear los datos para mejorar rendimiento
    def cargar_datos():
        try:
            df = px.data.tips()
            return df
        except Exception as e:
            st.error(f"Error cargando datos: {e}")
            # Crear DataFrame de respaldo
            tips_data = {
                'total_bill': np.random.rand(50) * 40 + 10,
                'tip': lambda df_in: df_in['total_bill'] * (np.random.rand(50) * 0.1 + 0.1),
                'sex': np.random.choice(['Male', 'Female'], 50),
                'smoker': np.random.choice(['Yes', 'No'], 50),
                'day': np.random.choice(['Thur', 'Fri', 'Sat', 'Sun'], 50),
                'time': np.random.choice(['Lunch', 'Dinner'], 50),
                'size': np.random.randint(1, 6, 50)
            }
            df = pd.DataFrame(tips_data)
            df['tip'] = df.apply(tips_data['tip'], axis=0) # type: ignore
            return df

    tips_df = cargar_datos()

    # --- Mostrar Datos ---
    st.header("Vista Previa de los Datos")
    if st.checkbox("Mostrar datos crudos"): # Widget: Checkbox
        st.dataframe(tips_df) # Muestra el DataFrame interactivamente

    # --- Widgets Interactivos ---
    st.header("Filtros Interactivos")
    # Widget: Slider
    min_bill = st.slider("Filtrar por cuenta mínima:",
                         min_value=float(tips_df['total_bill'].min()),
                         max_value=float(tips_df['total_bill'].max()),
                         value=10.0) # Valor inicial

    # Widget: Multiselect
    dias_seleccionados = st.multiselect("Seleccionar días:",
                                        options=tips_df['day'].unique(),
                                        default=tips_df['day'].unique()) # Por defecto todos

    # Filtrar DataFrame basado en widgets
    tips_filtrado = tips_df[
        (tips_df['total_bill'] >= min_bill) &
        (tips_df['day'].isin(dias_seleccionados))
    ]

    st.write(f"Mostrando datos con cuenta >= ${min_bill:.2f} para los días: {', '.join(dias_seleccionados)}")
    st.dataframe(tips_filtrado)

    # --- Gráficos Interactivos (usando Plotly) ---
    st.header("Visualizaciones Interactivas")

    # Scatter plot filtrado
    fig_scatter_st = px.scatter(tips_filtrado, x="total_bill", y="tip",
                                color="sex", title="Propina vs Cuenta (Filtrado)")
    st.plotly_chart(fig_scatter_st) # Muestra gráfico Plotly en Streamlit

    # Histograma filtrado
    fig_hist_st = px.histogram(tips_filtrado, x="total_bill", nbins=20,
                               title="Distribución Cuenta Total (Filtrado)")
    st.plotly_chart(fig_hist_st)

    # También puedes mostrar gráficos de Matplotlib/Seaborn
    # import matplotlib.pyplot as plt
    # import seaborn as sns
    # fig_mpl, ax = plt.subplots()
    # sns.histplot(tips_filtrado, x="tip", ax=ax)
    # st.pyplot(fig_mpl)
    ```

3.  **Ejecuta la App:** Abre tu terminal en el directorio donde guardaste el archivo y ejecuta:
    ```bash
    streamlit run mi_app_streamlit.py
    ```
    Streamlit iniciará un servidor local y abrirá la aplicación en tu navegador web. ¡Interactúa con los widgets (slider, multiselect) y observa cómo se actualizan los datos y los gráficos!

**Conclusión:**

Plotly te permite crear gráficos interactivos individuales, mientras que Streamlit te permite construir rápidamente aplicaciones web completas alrededor de tus análisis y visualizaciones, haciéndolos accesibles e interactivos para otros usuarios sin necesidad de que ellos ejecuten código Python. Ambas son herramientas valiosas para llevar tus visualizaciones al siguiente nivel.
