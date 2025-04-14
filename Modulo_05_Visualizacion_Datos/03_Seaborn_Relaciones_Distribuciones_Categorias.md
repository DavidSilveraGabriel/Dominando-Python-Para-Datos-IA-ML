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
