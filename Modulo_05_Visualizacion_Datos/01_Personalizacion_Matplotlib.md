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
