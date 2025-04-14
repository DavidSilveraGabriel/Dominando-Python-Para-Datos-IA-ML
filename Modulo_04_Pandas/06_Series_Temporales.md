# Módulo 4: Series Temporales (Básico)

Pandas fue desarrollado inicialmente con un fuerte enfoque en el análisis de datos financieros, por lo que tiene herramientas muy robustas y convenientes para trabajar con **series temporales** (datos indexados por fechas u horas).

## Tipos de Datos de Fecha y Hora

Pandas utiliza principalmente el tipo `Timestamp` (para momentos específicos en el tiempo) y `DatetimeIndex` (un índice compuesto por Timestamps). Estos se basan en el tipo `datetime64` de NumPy.

*   **`Timestamp`**: Representa un único punto en el tiempo.
*   **`DatetimeIndex`**: Un índice de Timestamps, usado comúnmente como el índice de Series o DataFrames de series temporales.
*   **`Period`**: Representa un intervalo o lapso de tiempo (ej. un mes específico, un año, un trimestre).
*   **`PeriodIndex`**: Un índice de Periods.
*   **`Timedelta`**: Representa una duración o diferencia entre dos momentos en el tiempo.

## Creando Secuencias de Fechas

Pandas facilita la creación de secuencias de fechas:

*   **`pd.to_datetime()`**: Convierte strings o listas de strings a objetos Timestamp o DatetimeIndex. Es muy flexible interpretando formatos.
*   **`pd.date_range()`**: Genera un DatetimeIndex con fechas espaciadas regularmente.

```python
import pandas as pd

# Convertir un string a Timestamp
fecha_unica = pd.to_datetime('2024-04-14')
print(f"Timestamp único: {fecha_unica}, Tipo: {type(fecha_unica)}\n")

# Convertir una lista de strings a DatetimeIndex
lista_fechas_str = ['2024-01-01', '2024-01-05', '2024-01-10', '2024/02/15'] # Diferentes formatos
indice_fechas = pd.to_datetime(lista_fechas_str)
print(f"DatetimeIndex desde lista:\n{indice_fechas}\n")

# Crear un rango de fechas diarias
# Por defecto, la frecuencia es diaria ('D')
rango_dias = pd.date_range(start='2024-03-01', end='2024-03-07')
print(f"Rango de días (diario):\n{rango_dias}\n")

# Crear un rango especificando el número de periodos
rango_5dias = pd.date_range(start='2024-03-01', periods=5)
print(f"Rango de 5 días:\n{rango_5dias}\n")

# Crear un rango con frecuencia específica (ej. fin de mes 'M', inicio de mes 'MS')
rango_fin_mes = pd.date_range(start='2024-01-01', periods=4, freq='M') # 'M' es fin de mes
print(f"Rango fin de mes ('M'):\n{rango_fin_mes}\n")

rango_inicio_mes = pd.date_range(start='2024-01-01', periods=4, freq='MS') # 'MS' es inicio de mes
print(f"Rango inicio de mes ('MS'):\n{rango_inicio_mes}\n")

# Otras frecuencias comunes: 'H' (hora), 'T' o 'min' (minuto), 'S' (segundo),
# 'B' (día hábil), 'W' (semanal, domingo), 'Q' (trimestral, fin)
rango_horas = pd.date_range(start='2024-04-14 09:00', periods=3, freq='H')
print(f"Rango de horas ('H'):\n{rango_horas}\n")
```

## Series y DataFrames con Índice de Tiempo

La verdadera potencia surge cuando usamos un `DatetimeIndex` como índice de nuestras Series o DataFrames.

```python
# Crear una Serie con índice de tiempo
np.random.seed(42) # Para reproducibilidad
datos_serie = np.random.randn(5) # 5 números aleatorios
fechas_serie = pd.date_range('2024-05-01', periods=5, freq='B') # 5 días hábiles
ts = pd.Series(datos_serie, index=fechas_serie)

print("Serie Temporal:")
print(ts)
print("\n")

# Crear un DataFrame con índice de tiempo
datos_df = np.random.randint(50, 100, size=(6, 3))
fechas_df = pd.date_range('2024-06-01', periods=6, freq='D')
df_ts = pd.DataFrame(datos_df, index=fechas_df, columns=['ProductoA', 'ProductoB', 'ProductoC'])

print("DataFrame Temporal:")
print(df_ts)
print("\n")
```

## Indexación y Selección en Series Temporales

Usar un `DatetimeIndex` permite formas intuitivas de seleccionar datos basadas en fechas:

```python
print("--- Indexación en Serie Temporal (ts) ---")

# Seleccionar por fecha exacta (como etiqueta en .loc)
print(f"Valor en '2024-05-03': {ts['2024-05-03']:.2f}")
# o usando objeto Timestamp
fecha_ts = pd.Timestamp('2024-05-03')
print(f"Valor en Timestamp({fecha_ts.date()}): {ts[fecha_ts]:.2f}\n")

# Seleccionar por año
print(f"Valores en 2024:\n{ts['2024']}\n") # Selecciona todos los de 2024

# Seleccionar por año y mes
print(f"Valores en Mayo 2024:\n{ts['2024-05']}\n")

# Slicing con fechas (¡.loc incluye el final!)
print(f"Valores desde '2024-05-02' hasta '2024-05-06':\n{ts['2024-05-02':'2024-05-06']}\n")

# --- Indexación en DataFrame Temporal (df_ts) ---
print("--- Indexación en DataFrame Temporal (df_ts) ---")

# Seleccionar fila por fecha
print(f"Fila para '2024-06-04':\n{df_ts.loc['2024-06-04']}\n")

# Seleccionar un rango de fechas
print(f"Filas de '2024-06-02' a '2024-06-04':\n{df_ts['2024-06-02':'2024-06-04']}\n")
```

## Funcionalidades Básicas de Series Temporales

*   **Desplazamiento (`shift()`):** Mueve los datos hacia adelante o atrás en el tiempo.
*   **Ventanas Móviles (`rolling()`):** Permite calcular estadísticas (media, suma, etc.) sobre una ventana deslizante de datos.
*   **Remuestreo (`resample()`):** Cambia la frecuencia de la serie temporal (ej. de datos diarios a mensuales). Es similar a `groupby` pero para el tiempo. Requiere una función de agregación.

```python
print("--- Funcionalidades Básicas ---")

# Desplazamiento (shift)
print(f"Serie original:\n{ts}\n")
print(f"Serie desplazada 1 día adelante (shift(1)):\n{ts.shift(1)}\n") # El primer valor se vuelve NaN
print(f"Serie desplazada 1 día atrás (shift(-1)):\n{ts.shift(-1)}\n") # El último valor se vuelve NaN

# Media móvil de 2 días (rolling)
media_movil_2d = ts.rolling(window=2).mean()
print(f"Media móvil de 2 días:\n{media_movil_2d}\n") # El primer valor es NaN

# Remuestreo (resample) - Ejemplo: de diario a suma mensual en df_ts
# Necesitamos más datos para que sea interesante, pero veamos la sintaxis
# df_ts_mensual = df_ts.resample('M').sum() # 'M' es frecuencia de fin de mes
# print(f"Suma mensual (resample('M').sum()):\n{df_ts_mensual}\n")
# (Con los datos actuales, solo mostraría la suma de Junio)
```

**Nota:** Las ventanas móviles y el remuestreo son temas más avanzados, pero es bueno conocer su existencia.

Pandas ofrece un conjunto muy rico de herramientas para trabajar con series temporales, desde la simple indexación basada en fechas hasta análisis más complejos como el remuestreo y las ventanas móviles. Esto lo convierte en una herramienta indispensable para cualquier análisis que involucre datos dependientes del tiempo.
