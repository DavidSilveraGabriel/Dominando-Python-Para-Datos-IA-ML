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
