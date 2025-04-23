# Ejercicios: Módulo 5 - Introducción a Seaborn: Gráficos Estadísticos

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
# Aplicaremos un tema para mejorar la estética general
sns.set_theme(style="whitegrid")

# --- Datos de Ejemplo ---
# Usaremos un dataset simulado de calificaciones de estudiantes
np.random.seed(123)
n_estudiantes = 100
datos_calificaciones = {
    'ID_Estudiante': range(1, n_estudiantes + 1),
    'Horas_Estudio': np.random.uniform(1, 10, n_estudiantes).round(1),
    'Calificacion_Parcial': lambda df: (df['Horas_Estudio'] * 7 + np.random.normal(0, 8, n_estudiantes)).clip(0, 100),
    'Asistencia': np.random.randint(70, 100, n_estudiantes),
    'Curso': np.random.choice(['Matemáticas', 'Física', 'Química'], n_estudiantes, p=[0.4, 0.3, 0.3])
}
df_calificaciones = pd.DataFrame(datos_calificaciones)
# Calcular Calificacion_Parcial usando la lambda
df_calificaciones['Calificacion_Parcial'] = df_calificaciones.apply(datos_calificaciones['Calificacion_Parcial'], axis=0).round(1)

print("--- DataFrame de Calificaciones de Ejemplo ---")
print(df_calificaciones.head())
print("\n" + "="*30 + "\n")


# --- Ejercicio 1: Gráfico de Dispersión con Regresión (`regplot`) ---
# Instrucciones:
# 1. Usa `sns.regplot()` para visualizar la relación entre 'Horas_Estudio' (eje x) y 'Calificacion_Parcial' (eje y) del `df_calificaciones`.
# 2. Personaliza el gráfico de dispersión dentro de `regplot` usando `scatter_kws`:
#    - Dale un tamaño (s) de 40.
#    - Dale una transparencia (alpha) de 0.6.
# 3. Personaliza la línea de regresión usando `line_kws`:
#    - Dale un color 'darkred'.
# 4. Añade un título al gráfico usando `plt.title()`: "Calificación vs Horas de Estudio".
# 5. Muestra el gráfico usando `plt.show()`.

print("--- Ejercicio 1: Gráfico de Dispersión con Regresión ---")
# Escribe tu código aquí
plt.figure(figsize=(8, 5)) # Ajustar tamaño figura

# 1. Crear regplot
sns.regplot(x='Horas_Estudio', y='Calificacion_Parcial', data=df_calificaciones,
            # 2. Personalizar scatter
            scatter_kws={'s': 40, 'alpha': 0.6},
            # 3. Personalizar línea
            line_kws={'color': 'darkred'})

# 4. Añadir título
plt.title("Calificación vs Horas de Estudio")

# 5. Mostrar gráfico
plt.show()
print("-" * 20)


# --- Ejercicio 2: Gráfico de Cajas (`boxplot`) ---
# Instrucciones:
# 1. Usa `sns.boxplot()` para comparar la distribución de 'Calificacion_Parcial' entre los diferentes 'Curso'.
# 2. Usa la paleta de colores 'pastel' (`palette='pastel'`).
# 3. Añade un título: "Distribución de Calificaciones por Curso".
# 4. Muestra el gráfico.

print("\n--- Ejercicio 2: Gráfico de Cajas ---")
# Escribe tu código aquí
plt.figure(figsize=(8, 6))

# 1. Crear boxplot
sns.boxplot(x='Curso', y='Calificacion_Parcial', data=df_calificaciones,
            # 2. Paleta de colores
            palette='pastel')

# 3. Añadir título
plt.title("Distribución de Calificaciones por Curso")

# 4. Mostrar gráfico
plt.show()
print("-" * 20)


# --- Ejercicio 3: Gráfico de Violín (`violinplot`) ---
# Instrucciones:
# 1. Usa `sns.violinplot()` para visualizar la distribución de 'Asistencia' para cada 'Curso'.
# 2. Muestra los cuartiles dentro de los violines (`inner='quartile'`).
# 3. Usa la paleta de colores 'muted'.
# 4. Añade un título: "Distribución de Asistencia por Curso".
# 5. Muestra el gráfico.

print("\n--- Ejercicio 3: Gráfico de Violín ---")
# Escribe tu código aquí
plt.figure(figsize=(8, 6))

# 1. Crear violinplot
sns.violinplot(x='Curso', y='Asistencia', data=df_calificaciones,
               # 2. Mostrar cuartiles
               inner='quartile',
               # 3. Paleta de colores
               palette='muted')

# 4. Añadir título
plt.title("Distribución de Asistencia por Curso")

# 5. Mostrar gráfico
plt.show()
print("-" * 20)


# --- Ejercicio 4: Mapa de Calor (`heatmap`) ---
# Instrucciones:
# 1. Calcula la matriz de correlación de las columnas numéricas de `df_calificaciones`.
#    - Selecciona solo las columnas 'Horas_Estudio', 'Calificacion_Parcial', 'Asistencia'.
#    - Usa el método `.corr()` sobre el DataFrame resultante. Guarda la matriz en `matriz_corr`.
# 2. Usa `sns.heatmap()` para visualizar `matriz_corr`.
# 3. Muestra los valores de correlación en el mapa (`annot=True`).
# 4. Usa el mapa de color 'coolwarm' (`cmap='coolwarm'`).
# 5. Formatea los números anotados para que muestren 2 decimales (`fmt=".2f"`).
# 6. Añade un título: "Mapa de Calor de Correlaciones".
# 7. Muestra el gráfico.

print("\n--- Ejercicio 4: Mapa de Calor ---")
# Escribe tu código aquí
# 1. Calcular matriz de correlación
columnas_numericas = ['Horas_Estudio', 'Calificacion_Parcial', 'Asistencia']
matriz_corr = df_calificaciones[columnas_numericas].corr()
print("Matriz de Correlación:")
print(matriz_corr)

plt.figure(figsize=(7, 6))

# 2. Crear heatmap
sns.heatmap(matriz_corr,
            # 3. Anotar valores
            annot=True,
            # 4. Mapa de color
            cmap='coolwarm',
            # 5. Formato de anotación
            fmt=".2f",
            linewidths=0.5) # Añadir líneas para separar celdas

# 6. Añadir título
plt.title("Mapa de Calor de Correlaciones")

# 7. Mostrar gráfico
plt.show()
print("-" * 20)


# --- Ejercicio 5: Gráfico de Conteo (`countplot`) ---
# Instrucciones:
# 1. Usa `sns.countplot()` para mostrar cuántos estudiantes hay en cada 'Curso'.
# 2. Ordena las barras por la frecuencia de los cursos (de mayor a menor). Usa el argumento `order`.
# 3. Usa la paleta de colores 'Set3'.
# 4. Añade un título: "Número de Estudiantes por Curso".
# 5. Muestra el gráfico.

print("\n--- Ejercicio 5: Gráfico de Conteo ---")
# Escribe tu código aquí
plt.figure(figsize=(7, 5))

# 1. Crear countplot
sns.countplot(x='Curso', data=df_calificaciones,
              # 2. Ordenar barras
              order=df_calificaciones['Curso'].value_counts().index,
              # 3. Paleta de colores
              palette='Set3')

# 4. Añadir título
plt.title("Número de Estudiantes por Curso")

# 5. Mostrar gráfico
plt.show()
print("-" * 20)


# --- Ejercicio 6: Combinando Seaborn y Matplotlib ---
# Instrucciones:
# 1. Crea un `sns.boxplot()` como en el Ejercicio 2 (Calificación por Curso).
# 2. Después de crear el gráfico con Seaborn, usa funciones de `matplotlib.pyplot` (`plt`) para:
#    - Cambiar la etiqueta del eje Y a "Nota Final del Parcial".
#    - Establecer el límite del eje Y entre 0 y 110.
#    - Añadir una línea horizontal roja discontinua en y=50 (representando el aprobado) usando `plt.axhline()`.
# 3. Muestra el gráfico.

print("\n--- Ejercicio 6: Combinando Seaborn y Matplotlib ---")
# Escribe tu código aquí
plt.figure(figsize=(8, 6))

# 1. Crear boxplot (Seaborn)
sns.boxplot(x='Curso', y='Calificacion_Parcial', data=df_calificaciones, palette='pastel')
plt.title("Distribución de Calificaciones por Curso (con Aprobado)") # Título general

# 2. Personalizar con Matplotlib
plt.ylabel("Nota Final del Parcial") # Cambiar etiqueta Y
plt.ylim(0, 110) # Establecer límite Y
plt.axhline(50, color='red', linestyle='--', linewidth=1.5, label='Aprobado (50)') # Línea horizontal

plt.legend() # Mostrar leyenda para la línea horizontal

# 3. Mostrar gráfico
plt.show()
print("-" * 20)

# --- Fin de los ejercicios ---
