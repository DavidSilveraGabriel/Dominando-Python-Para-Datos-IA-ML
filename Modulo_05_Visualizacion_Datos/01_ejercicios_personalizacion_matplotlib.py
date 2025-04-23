# Ejercicios: Módulo 5 - Personalización de Gráficos con Matplotlib

import matplotlib.pyplot as plt
import numpy as np

# --- Datos de Ejemplo ---
x = np.linspace(0, 10, 100)
y_exp = np.exp(x / 5)
y_log = np.log(x + 1) * 5 # Sumamos 1 para evitar log(0)
y_noise = y_exp + np.random.randn(100) * 3 # Datos con ruido

# --- Ejercicio 1: Colores, Estilos y Marcadores ---
# Instrucciones:
# 1. Crea una figura y ejes usando `plt.subplots()`. Tamaño (10, 6).
# 2. Grafica `y_exp` vs `x` con:
#    - Color: 'darkorange'
#    - Estilo de línea: discontinua ('--')
#    - Grosor de línea (linewidth): 2.5
#    - Etiqueta: 'Exponencial (y=exp(x/5))'
# 3. Grafica `y_log` vs `x` con:
#    - Formato abreviado: 'm:.' (magenta, punteado, marcador de punto)
#    - Tamaño de marcador (markersize): 8
#    - Etiqueta: 'Logarítmica (y=5*log(x+1))'
# 4. Añade título "Gráfico Personalizado: Estilos", etiquetas "Eje X", "Eje Y" y leyenda.
# 5. Muestra el gráfico.

print("--- Ejercicio 1: Colores, Estilos y Marcadores ---")
# Escribe tu código aquí
# 1. Crear figura y ejes
fig1, ax1 = plt.subplots(figsize=(10, 6))

# 2. Graficar exponencial
ax1.plot(x, y_exp, color='darkorange', linestyle='--', linewidth=2.5, label='Exponencial (y=exp(x/5))')

# 3. Graficar logarítmica
ax1.plot(x, y_log, 'm:.', markersize=8, label='Logarítmica (y=5*log(x+1))') # Magenta, punteado, punto

# 4. Añadir títulos, etiquetas y leyenda
ax1.set_title("Gráfico Personalizado: Estilos")
ax1.set_xlabel("Eje X")
ax1.set_ylabel("Eje Y")
ax1.legend()

# 5. Mostrar gráfico
plt.show()
print("-" * 20)


# --- Ejercicio 2: Límites de Ejes y Cuadrícula ---
# Instrucciones:
# 1. Crea una nueva figura y ejes. Tamaño (8, 5).
# 2. Grafica `y_noise` vs `x` usando un gráfico de dispersión (`ax.scatter()`):
#    - Color: 'steelblue'
#    - Marcador: 'x'
#    - Tamaño de puntos (s): 30
#    - Transparencia (alpha): 0.7
#    - Etiqueta: 'Datos Ruidosos'
# 3. Establece los límites del eje X entre -0.5 y 10.5 (`ax.set_xlim()`).
# 4. Establece los límites del eje Y entre -5 y 35 (`ax.set_ylim()`).
# 5. Añade una cuadrícula (`ax.grid()`) con:
#    - Estilo de línea: punteado (':')
#    - Color: 'gray'
#    - Transparencia (alpha): 0.6
# 6. Añade título "Límites y Cuadrícula" y etiquetas de ejes.
# 7. Muestra el gráfico.

print("\n--- Ejercicio 2: Límites de Ejes y Cuadrícula ---")
# Escribe tu código aquí
# 1. Crear figura y ejes
fig2, ax2 = plt.subplots(figsize=(8, 5))

# 2. Graficar dispersión
ax2.scatter(x, y_noise, color='steelblue', marker='x', s=30, alpha=0.7, label='Datos Ruidosos')

# 3. Establecer límites X
ax2.set_xlim(-0.5, 10.5)

# 4. Establecer límites Y
ax2.set_ylim(-5, 35)

# 5. Añadir cuadrícula personalizada
ax2.grid(True, linestyle=':', color='gray', alpha=0.6)

# 6. Añadir título y etiquetas
ax2.set_title("Límites y Cuadrícula")
ax2.set_xlabel("Tiempo")
ax2.set_ylabel("Medición")
ax2.legend() # Para mostrar la etiqueta de scatter

# 7. Mostrar gráfico
plt.show()
print("-" * 20)


# --- Ejercicio 3: Texto y Anotaciones ---
# Instrucciones:
# 1. Crea una nueva figura y ejes. Tamaño (9, 6).
# 2. Grafica `y_exp` vs `x` como una línea sólida azul ('b-').
# 3. Añade texto en la posición (x=1, y=5) que diga "Inicio de la curva" con tamaño de fuente 12. Usa `ax.text()`.
# 4. Encuentra el índice del valor máximo de `y_exp`. Usa `np.argmax()`.
# 5. Obtén las coordenadas (x_max, y_max) correspondientes a ese índice máximo.
# 6. Añade una anotación (`ax.annotate()`) que:
#    - Tenga el texto "Punto Máximo".
#    - Señale al punto (x_max, y_max) (`xy=...`).
#    - Coloque el texto en (x_max - 2, y_max - 4) (`xytext=...`).
#    - Use una flecha con estilo '->' (`arrowprops=dict(arrowstyle='->')`).
# 7. Añade título "Texto y Anotaciones" y etiquetas de ejes.
# 8. Muestra el gráfico.

print("\n--- Ejercicio 3: Texto y Anotaciones ---")
# Escribe tu código aquí
# 1. Crear figura y ejes
fig3, ax3 = plt.subplots(figsize=(9, 6))

# 2. Graficar exponencial
ax3.plot(x, y_exp, 'b-', label='y=exp(x/5)')

# 3. Añadir texto
ax3.text(1, 5, "Inicio de la curva", fontsize=12)

# 4. Encontrar índice máximo
idx_max = np.argmax(y_exp)

# 5. Obtener coordenadas máximas
x_max = x[idx_max]
y_max = y_exp[idx_max]

# 6. Añadir anotación
ax3.annotate('Punto Máximo',
             xy=(x_max, y_max),
             xytext=(x_max - 3, y_max - 5), # Ajustar posición del texto
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2')) # Estilo de flecha y conexión

# 7. Añadir título y etiquetas
ax3.set_title("Texto y Anotaciones")
ax3.set_xlabel("Variable X")
ax3.set_ylabel("Variable Y Exponencial")
ax3.legend()

# 8. Mostrar gráfico
plt.show()
print("-" * 20)


# --- Ejercicio 4: Guardar Figura ---
# Instrucciones:
# 1. Reutiliza la figura y ejes (`fig1`, `ax1`) del Ejercicio 1.
# 2. Cambia la ubicación de la leyenda a 'upper center' (`ax1.legend(loc='upper center')`).
# 3. Guarda la figura (`fig1`) en un archivo llamado "grafico_estilos.png" con una resolución de 150 dpi. Usa `fig1.savefig()`.
# 4. Guarda la misma figura en un archivo PDF llamado "grafico_estilos.pdf".
# 5. (Opcional) Verifica que los archivos se hayan creado en tu directorio.
# 6. Muestra el gráfico modificado (`fig1`) usando `plt.show()`.

print("\n--- Ejercicio 4: Guardar Figura ---")
# Escribe tu código aquí
# 1. Reutilizar fig1, ax1

# 2. Cambiar ubicación de leyenda
ax1.legend(loc='upper center')

# 3. Guardar como PNG
try:
    fig1.savefig("grafico_estilos.png", dpi=150)
    print("Figura guardada como grafico_estilos.png")
except Exception as e:
    print(f"Error guardando PNG: {e}")

# 4. Guardar como PDF
try:
    fig1.savefig("grafico_estilos.pdf")
    print("Figura guardada como grafico_estilos.pdf")
except Exception as e:
    print(f"Error guardando PDF: {e}")

# 6. Mostrar gráfico modificado
plt.show()
print("-" * 20)

# --- Fin de los ejercicios ---
