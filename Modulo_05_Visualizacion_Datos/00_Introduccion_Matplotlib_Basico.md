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
