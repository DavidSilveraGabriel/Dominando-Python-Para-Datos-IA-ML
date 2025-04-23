# Ejercicios: Módulo 5 - Seaborn: Relaciones, Distribuciones y Categorías

# --- Prerrequisitos ---
# Asegúrate de tener Seaborn, Matplotlib, Pandas y NumPy instalados.
# pip install seaborn matplotlib pandas numpy
# o
# conda install seaborn matplotlib pandas numpy

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- Configuración de Estilo Seaborn ---
sns.set_theme(style="ticks") # Usaremos 'ticks' esta vez

# --- Datos de Ejemplo ---
# Cargaremos el dataset 'tips' que viene con Seaborn
try:
    tips = sns.load_dataset("tips")
    print("--- Dataset 'tips' Cargado ---")
    print(tips.head())
except Exception as e:
    print(f"No se pudo cargar el dataset 'tips'. Error: {e}")
    # Crear un DataFrame de respaldo si falla la carga
    tips_data = {
        'total_bill': np.random.rand(100) * 45 + 5,
        'tip': lambda df: df['total_bill'] * (np.random.rand(100) * 0.15 + 0.05),
        'sex': np.random.choice(['Male', 'Female'], 100),
        'smoker': np.random.choice(['Yes', 'No'], 100),
        'day': np.random.choice(['Thur', 'Fri', 'Sat', 'Sun'], 100),
        'time': np.random.choice(['Lunch', 'Dinner'], 100),
        'size': np.random.randint(1, 7, 100)
    }
    tips = pd.DataFrame(tips_data)
    tips['tip'] = tips.apply(tips_data['tip'], axis=0).round(2) # type: ignore
    print("\n--- Usando DataFrame de respaldo para 'tips' ---")
    print(tips.head())

print("\n" + "="*30 + "\n")


# --- Ejercicio 1: Gráficos Relacionales (`relplot`) ---
# Instrucciones:
# 1. Usa `sns.relplot()` para crear un gráfico de dispersión (`kind='scatter'`) de 'tip' vs 'total_bill'.
# 2. Colorea los puntos (`hue`) según si la persona es fumadora ('smoker').
# 3. Crea facetas por columnas (`col`) basadas en el momento del día ('time').
# 4. Añade un título general a la figura usando `plt.suptitle()` (ajusta la posición y si es necesario).
# 5. Muestra el gráfico.

print("--- Ejercicio 1: Gráficos Relacionales (relplot - scatter) ---")
# Escribe tu código aquí
# 1, 2, 3. Crear relplot scatter
g1 = sns.relplot(
    data=tips,
    x="total_bill", y="tip",
    kind="scatter",
    hue="smoker",
    col="time"
)

# 4. Añadir título general
g1.fig.suptitle("Propina vs Cuenta por Momento del Día y Fumador", y=1.03) # y ajusta la posición vertical

# 5. Mostrar gráfico
plt.show()
print("-" * 20)


# --- Ejercicio 2: Gráficos de Distribución (`displot`) ---
# Instrucciones:
# 1. Usa `sns.displot()` para crear histogramas (`kind='hist'`) de la 'total_bill'.
# 2. Crea facetas por filas (`row`) basadas en el día ('day'), ordena las filas con `row_order`.
# 3. Superpón una estimación de densidad kernel (`kde=True`).
# 4. Ajusta la altura de cada faceta a 2 pulgadas (`height=2`) y la relación de aspecto a 3 (`aspect=3`).
# 5. Muestra el gráfico.

print("\n--- Ejercicio 2: Gráficos de Distribución (displot - hist) ---")
# Escribe tu código aquí
# 1, 2, 3, 4. Crear displot hist
g2 = sns.displot(
    data=tips,
    x="total_bill",
    kind="hist",
    row="day",
    row_order=['Thur', 'Fri', 'Sat', 'Sun'],
    kde=True,
    height=2,
    aspect=3,
    palette='viridis' # Añadir una paleta
)
g2.fig.suptitle("Distribución de la Cuenta Total por Día", y=1.03)

# 5. Mostrar gráfico
plt.show()
print("-" * 20)


# --- Ejercicio 3: Gráficos Categóricos (`catplot` - boxplot) ---
# Instrucciones:
# 1. Usa `sns.catplot()` para crear gráficos de cajas (`kind='box'`) que muestren la distribución de 'tip' (propina).
# 2. Usa 'day' como la variable categórica principal en el eje x, ordena los días.
# 3. Colorea las cajas (`hue`) según el sexo ('sex').
# 4. Crea facetas por columnas (`col`) basadas en si es fumador ('smoker').
# 5. Muestra el gráfico.

print("\n--- Ejercicio 3: Gráficos Categóricos (catplot - box) ---")
# Escribe tu código aquí
# 1, 2, 3, 4. Crear catplot box
g3 = sns.catplot(
    data=tips,
    x="day", y="tip",
    kind="box",
    order=['Thur', 'Fri', 'Sat', 'Sun'],
    hue="sex",
    col="smoker",
    palette='Set2'
)
g3.fig.suptitle("Distribución de Propinas (Día, Sexo, Fumador)", y=1.03)

# 5. Mostrar gráfico
plt.show()
print("-" * 20)


# --- Ejercicio 4: Gráficos Categóricos (`catplot` - barplot) ---
# Instrucciones:
# 1. Usa `sns.catplot()` para crear gráficos de barras (`kind='bar'`) que muestren la media de 'total_bill'.
# 2. Usa 'day' en el eje x (ordenado) y 'sex' para colorear (`hue`).
# 3. Crea facetas por filas (`row`) basadas en el momento del día ('time').
# 4. Desactiva las barras de error (`errorbar=None`).
# 5. Muestra el gráfico.

print("\n--- Ejercicio 4: Gráficos Categóricos (catplot - bar) ---")
# Escribe tu código aquí
# 1, 2, 3, 4. Crear catplot bar
g4 = sns.catplot(
    data=tips,
    x="day", y="total_bill",
    kind="bar",
    order=['Thur', 'Fri', 'Sat', 'Sun'],
    hue="sex",
    row="time",
    errorbar=None, # Desactivar barras de error (muestran intervalo de confianza por defecto)
    palette='rocket'
)
g4.fig.suptitle("Cuenta Promedio (Día, Sexo, Momento)", y=1.03)

# 5. Mostrar gráfico
plt.show()
print("-" * 20)


# --- Ejercicio 5: Gráficos Categóricos (`catplot` - violinplot) ---
# Instrucciones:
# 1. Usa `sns.catplot()` para crear gráficos de violín (`kind='violin'`) mostrando la distribución de 'tip'.
# 2. Usa 'time' en el eje x.
# 3. Colorea (`hue`) por 'smoker'.
# 4. Divide los violines por 'hue' usando `split=True`.
# 5. Crea facetas por columnas (`col`) basadas en el día ('day'), ordenadas.
# 6. Muestra el gráfico.

print("\n--- Ejercicio 5: Gráficos Categóricos (catplot - violin) ---")
# Escribe tu código aquí
# 1, 2, 3, 4, 5. Crear catplot violin
g5 = sns.catplot(
    data=tips,
    x="time", y="tip",
    kind="violin",
    hue="smoker",
    split=True,
    col="day",
    col_order=['Thur', 'Fri', 'Sat', 'Sun'],
    palette='muted',
    inner='quartile' # Mostrar cuartiles dentro
)
g5.fig.suptitle("Distribución de Propinas (Momento, Fumador, Día)", y=1.03)

# 6. Mostrar gráfico
plt.show()
print("-" * 20)

# --- Fin de los ejercicios ---
