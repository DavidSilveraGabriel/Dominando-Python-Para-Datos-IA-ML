# Ejercicios: Módulo 5 - Introducción a Matplotlib: Gráficos Básicos

# --- Prerrequisitos ---
# Asegúrate de tener Matplotlib y NumPy instalados.
# pip install matplotlib numpy pandas
# o
# conda install matplotlib numpy pandas

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd # Lo usaremos para algún ejemplo

# --- Configuración para Jupyter Notebook/Lab (opcional) ---
# Descomenta la siguiente línea si trabajas en Jupyter:
# %matplotlib inline

# --- Ejercicio 1: Gráfico de Líneas Básico ---
# Instrucciones:
# 1. Crea un array `x` con 50 puntos linealmente espaciados entre 0 y 2*pi (usa np.linspace).
# 2. Crea un array `y_sin` calculando el seno de `x`.
# 3. Crea un array `y_cos` calculando el coseno de `x`.
# 4. Usando `plt.plot()`, grafica `y_sin` vs `x` con una línea azul.
# 5. En el mismo gráfico, grafica `y_cos` vs `x` con una línea roja discontinua ('r--').
# 6. Añade un título al gráfico: "Funciones Seno y Coseno".
# 7. Añade etiquetas a los ejes: "Eje X (radianes)" y "Eje Y".
# 8. Añade una leyenda para identificar las líneas (usa el argumento `label` en `plt.plot()` y luego `plt.legend()`).
# 9. Muestra el gráfico usando `plt.show()`.

print("--- Ejercicio 1: Gráfico de Líneas Básico ---")
# Escribe tu código aquí
# 1. Crear datos x
x = np.linspace(0, 2 * np.pi, 50)

# 2. Crear datos y_sin
y_sin = np.sin(x)

# 3. Crear datos y_cos
y_cos = np.cos(x)

# 4. Graficar seno
plt.plot(x, y_sin, 'b-', label='Seno(x)') # 'b-' es línea azul sólida

# 5. Graficar coseno
plt.plot(x, y_cos, 'r--', label='Coseno(x)') # 'r--' es línea roja discontinua

# 6. Añadir título
plt.title("Funciones Seno y Coseno")

# 7. Añadir etiquetas a los ejes
plt.xlabel("Eje X (radianes)")
plt.ylabel("Eje Y")

# 8. Añadir leyenda
plt.legend()

# 9. Mostrar gráfico
plt.show()
print("-" * 20)


# --- Ejercicio 2: Gráfico de Dispersión ---
# Instrucciones:
# 1. Genera 100 puntos aleatorios para `x_scatter` entre 0 y 10 (usa np.random.rand(100) * 10).
# 2. Genera 100 puntos para `y_scatter` usando la fórmula y = 3*x + 5 + ruido_gaussiano (usa np.random.randn(100) * 3 para el ruido).
# 3. Crea un gráfico de dispersión (`plt.scatter()`) de `y_scatter` vs `x_scatter`.
# 4. Haz que los puntos sean verdes ('g') y usa marcadores de estrella ('*').
# 5. Añade un título: "Gráfico de Dispersión Simulado".
# 6. Añade etiquetas a los ejes: "Variable Independiente X" y "Variable Dependiente Y".
# 7. Añade una cuadrícula (`plt.grid(True)`).
# 8. Muestra el gráfico.

print("\n--- Ejercicio 2: Gráfico de Dispersión ---")
# Escribe tu código aquí
np.random.seed(1) # Para reproducibilidad

# 1. Generar x_scatter
x_scatter = np.random.rand(100) * 10

# 2. Generar y_scatter
y_scatter = 3 * x_scatter + 5 + np.random.randn(100) * 3

# 3. Crear scatter plot
plt.scatter(x_scatter, y_scatter, color='g', marker='*')

# 5. Añadir título
plt.title("Gráfico de Dispersión Simulado")

# 6. Añadir etiquetas
plt.xlabel("Variable Independiente X")
plt.ylabel("Variable Dependiente Y")

# 7. Añadir cuadrícula
plt.grid(True)

# 8. Mostrar gráfico
plt.show()
print("-" * 20)


# --- Ejercicio 3: Gráfico de Barras ---
# Instrucciones:
# 1. Define una lista de categorías: `productos = ['Manzanas', 'Naranjas', 'Plátanos', 'Uvas']`.
# 2. Define una lista de ventas correspondientes: `ventas = [120, 95, 150, 80]`.
# 3. Crea un gráfico de barras (`plt.bar()`) que muestre las ventas por producto.
# 4. Asigna diferentes colores a cada barra (puedes pasar una lista de colores al argumento `color`).
# 5. Añade un título: "Ventas por Producto".
# 6. Añade etiquetas a los ejes: "Producto" y "Cantidad Vendida".
# 7. Muestra el gráfico.

print("\n--- Ejercicio 3: Gráfico de Barras ---")
# Escribe tu código aquí
# 1. Categorías
productos = ['Manzanas', 'Naranjas', 'Plátanos', 'Uvas']

# 2. Valores
ventas = [120, 95, 150, 80]

# 3. Crear bar plot
colores = ['red', 'orange', 'yellow', 'purple']
plt.bar(productos, ventas, color=colores)

# 5. Añadir título
plt.title("Ventas por Producto")

# 6. Añadir etiquetas
plt.xlabel("Producto")
plt.ylabel("Cantidad Vendida")

# 7. Mostrar gráfico
plt.show()
print("-" * 20)


# --- Ejercicio 4: Histograma ---
# Instrucciones:
# 1. Genera 500 números aleatorios siguiendo una distribución normal con media 50 y desviación estándar 10 (usa `np.random.normal(loc=50, scale=10, size=500)`). Guarda los datos en `datos_normales`.
# 2. Crea un histograma (`plt.hist()`) de `datos_normales`.
# 3. Especifica que quieres 25 'bins' (intervalos).
# 4. Dale al histograma un color 'skyblue' y bordes de barra negros ('black').
# 5. Añade un título: "Distribución de Datos Normales".
# 6. Añade etiquetas a los ejes: "Valor" y "Frecuencia".
# 7. Muestra el gráfico.

print("\n--- Ejercicio 4: Histograma ---")
# Escribe tu código aquí
# 1. Generar datos normales
datos_normales = np.random.normal(loc=50, scale=10, size=500)

# 2. Crear histograma
plt.hist(datos_normales, bins=25, color='skyblue', edgecolor='black')

# 5. Añadir título
plt.title("Distribución de Datos Normales")

# 6. Añadir etiquetas
plt.xlabel("Valor")
plt.ylabel("Frecuencia")

# 7. Mostrar gráfico
plt.show()
print("-" * 20)


# --- Ejercicio 5: Enfoque Orientado a Objetos (OO) ---
# Instrucciones:
# 1. Vuelve a generar los datos `x`, `y_sin`, `y_cos` del Ejercicio 1.
# 2. Crea una figura y un conjunto de ejes explícitamente usando `fig, ax = plt.subplots()`. Define un tamaño de figura de (9, 5).
# 3. Usa los métodos del objeto `ax` para graficar `y_sin` vs `x` (línea sólida azul, marcador 'o') y `y_cos` vs `x` (línea discontinua roja, marcador 'x'). Añade etiquetas (`label`).
# 4. Usa los métodos de `ax` para establecer el título ("Gráfico OO"), las etiquetas de los ejes ("Eje X", "Eje Y") y mostrar la leyenda.
# 5. Usa un método de `ax` para añadir una cuadrícula.
# 6. Muestra el gráfico usando `plt.show()`.

print("\n--- Ejercicio 5: Enfoque Orientado a Objetos (OO) ---")
# Escribe tu código aquí
# 1. Regenerar datos
x = np.linspace(0, 2 * np.pi, 50)
y_sin = np.sin(x)
y_cos = np.cos(x)

# 2. Crear figura y ejes OO
fig, ax = plt.subplots(figsize=(9, 5))

# 3. Graficar usando ax
ax.plot(x, y_sin, 'bo-', label='Seno(x)') # Azul, sólido, círculo
ax.plot(x, y_cos, 'rx--', label='Coseno(x)') # Rojo, discontinuo, x

# 4. Establecer título, etiquetas y leyenda usando ax
ax.set_title("Gráfico OO")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.legend()

# 5. Añadir cuadrícula usando ax
ax.grid(True)

# 6. Mostrar gráfico
plt.show()
print("-" * 20)

# --- Fin de los ejercicios ---
