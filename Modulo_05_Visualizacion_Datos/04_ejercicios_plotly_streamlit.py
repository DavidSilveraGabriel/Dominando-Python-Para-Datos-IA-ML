# Ejercicios: Módulo 5 - Gráficos Interactivos (Plotly / Streamlit)

# --- Prerrequisitos ---
# Asegúrate de tener Plotly, Pandas y NumPy instalados.
# Para la parte de Streamlit (conceptual), necesitarías instalarlo por separado.
# pip install plotly pandas numpy plotly-express
# o
# conda install plotly pandas numpy plotly-express
# Para Streamlit: pip install streamlit

import plotly.express as px
import pandas as pd
import numpy as np
# import streamlit as st # Lo importaremos conceptualmente más adelante

# --- Datos de Ejemplo ---
# Usaremos el dataset 'gapminder' que viene con Plotly Express
# Contiene información sobre esperanza de vida, PBI per cápita y población por país y año.
try:
    gapminder = px.data.gapminder()
    print("--- Dataset 'gapminder' Cargado ---")
    print(gapminder.head())
except Exception as e:
    print(f"No se pudo cargar el dataset 'gapminder'. Error: {e}")
    # Crear DataFrame de respaldo si falla
    gapminder_data = {
        'country': np.repeat(['Pais A', 'Pais B', 'Pais C'], 10),
        'continent': np.repeat(['Continente X', 'Continente Y', 'Continente X'], 10),
        'year': np.tile(range(1952, 2002, 5), 3),
        'lifeExp': np.random.uniform(40, 80, 30),
        'pop': np.random.randint(1000000, 100000000, 30),
        'gdpPercap': np.random.uniform(500, 40000, 30),
        'iso_alpha': np.repeat(['PA', 'PB', 'PC'], 10), # Simplificado
        'iso_num': np.repeat([101, 102, 103], 10)      # Simplificado
    }
    gapminder = pd.DataFrame(gapminder_data)
    print("\n--- Usando DataFrame de respaldo para 'gapminder' ---")
    print(gapminder.head())

print("\n" + "="*30 + "\n")


# --- Ejercicio 1: Scatter Plot Interactivo con Plotly Express ---
# Instrucciones:
# 1. Filtra el DataFrame `gapminder` para obtener solo los datos del año 2007.
# 2. Crea un scatter plot interactivo usando `px.scatter()` con los datos filtrados:
#    - Eje X: 'gdpPercap' (PBI per cápita)
#    - Eje Y: 'lifeExp' (Esperanza de vida)
#    - Color de los puntos (`color`): 'continent' (Continente)
#    - Tamaño de los puntos (`size`): 'pop' (Población)
#    - Texto al pasar el ratón (`hover_name`): 'country' (País)
# 3. Añade un título: "Esperanza de Vida vs PBI per cápita (2007)".
# 4. Configura el eje X para que sea logarítmico (`log_x=True`).
# 5. Muestra el gráfico usando `fig.show()`. Interactúa con él (zoom, pan, hover).

print("--- Ejercicio 1: Scatter Plot Interactivo (Plotly Express) ---")
# Escribe tu código aquí
# 1. Filtrar datos para 2007
gapminder_2007 = gapminder[gapminder['year'] == 2007]

# 2. Crear scatter plot interactivo
fig1 = px.scatter(
    gapminder_2007,
    x="gdpPercap",
    y="lifeExp",
    color="continent",
    size="pop",
    hover_name="country",
    # 3. Añadir título
    title="Esperanza de Vida vs PBI per cápita (2007)",
    # 4. Eje X logarítmico
    log_x=True,
    size_max=60 # Limitar tamaño máximo de burbuja para mejor visualización
)

# 5. Mostrar gráfico
fig1.show()
print("Gráfico 1 mostrado (revisa tu navegador o entorno).")
print("-" * 20)


# --- Ejercicio 2: Bar Plot Interactivo con Plotly Express ---
# Instrucciones:
# 1. Calcula la población total por continente en el año 2007 usando `gapminder_2007`. Agrupa por 'continent' y suma 'pop'. Guarda el resultado en `pop_continente_2007`.
# 2. Crea un bar plot interactivo usando `px.bar()` con `pop_continente_2007`:
#    - Eje X: 'continent'
#    - Eje Y: 'pop'
#    - Color de las barras (`color`): 'continent'
#    - Texto en las barras (`text`): 'pop' (para mostrar el valor)
# 3. Añade un título: "Población Total por Continente (2007)".
# 4. Personaliza las etiquetas de los ejes usando `labels={'pop': 'Población Total', 'continent': 'Continente'}`.
# 5. Muestra el gráfico usando `fig.show()`.

print("\n--- Ejercicio 2: Bar Plot Interactivo (Plotly Express) ---")
# Escribe tu código aquí
# 1. Calcular población por continente
pop_continente_2007 = gapminder_2007.groupby('continent')['pop'].sum().reset_index()
print("Población por Continente (2007):")
print(pop_continente_2007)

# 2. Crear bar plot interactivo
fig2 = px.bar(
    pop_continente_2007,
    x='continent',
    y='pop',
    color='continent',
    text='pop', # Mostrar valor en la barra
    # 3. Añadir título
    title="Población Total por Continente (2007)",
    # 4. Personalizar etiquetas
    labels={'pop': 'Población Total', 'continent': 'Continente'}
)

# Mejorar formato del texto en barras
fig2.update_traces(texttemplate='%{text:.2s}', textposition='outside') # Formato (ej. 1.2B)

# 5. Mostrar gráfico
fig2.show()
print("Gráfico 2 mostrado.")
print("-" * 20)


# --- Ejercicio 3: Line Plot Interactivo con Plotly Express ---
# Instrucciones:
# 1. Calcula la esperanza de vida promedio por año para el continente 'Asia'. Filtra `gapminder` por 'Asia', agrupa por 'year' y calcula la media de 'lifeExp'. Guarda en `asia_life_exp_año`.
# 2. Crea un line plot interactivo usando `px.line()` con `asia_life_exp_año`:
#    - Eje X: 'year'
#    - Eje Y: 'lifeExp'
#    - Marcadores en los puntos (`markers=True`).
# 3. Añade un título: "Evolución de la Esperanza de Vida Promedio en Asia".
# 4. Personaliza las etiquetas de los ejes.
# 5. Muestra el gráfico usando `fig.show()`.

print("\n--- Ejercicio 3: Line Plot Interactivo (Plotly Express) ---")
# Escribe tu código aquí
# 1. Calcular esperanza de vida promedio en Asia
asia_life_exp_año = gapminder[gapminder['continent'] == 'Asia'].groupby('year')['lifeExp'].mean().reset_index()
print("Esperanza de Vida Promedio en Asia por Año:")
print(asia_life_exp_año)

# 2. Crear line plot interactivo
fig3 = px.line(
    asia_life_exp_año,
    x='year',
    y='lifeExp',
    markers=True, # Mostrar marcadores
    # 3. Añadir título
    title="Evolución de la Esperanza de Vida Promedio en Asia",
    # 4. Personalizar etiquetas
    labels={'year': 'Año', 'lifeExp': 'Esperanza de Vida Promedio'}
)

# 5. Mostrar gráfico
fig3.show()
print("Gráfico 3 mostrado.")
print("-" * 20)


# --- Ejercicio 4: Conceptual - Integración con Streamlit ---
# Instrucciones:
# 1. Imagina que quieres crear una pequeña aplicación web con Streamlit para mostrar el scatter plot del Ejercicio 1.
# 2. Escribe (como comentarios o strings) el código Python básico que usarías en un archivo `.py` para:
#    a. Importar `streamlit` as `st` y `plotly.express` as `px`.
#    b. Añadir un título a la aplicación Streamlit: "Dashboard Gapminder".
#    c. Incluir un widget (por ejemplo, un `st.slider` o `st.selectbox`) para seleccionar un año específico (en lugar de filtrar manualmente por 2007).
#    d. Filtrar el DataFrame `gapminder` según el año seleccionado en el widget.
#    e. Generar el scatter plot de Plotly Express (`px.scatter`) con los datos filtrados (similar al Ejercicio 1).
#    f. Mostrar el gráfico Plotly dentro de la aplicación Streamlit usando `st.plotly_chart()`.
# 3. Añade un comentario explicando cómo ejecutarías esta aplicación Streamlit desde la terminal.

print("\n--- Ejercicio 4: Conceptual - Integración con Streamlit ---")
# Escribe tu código conceptual aquí (como comentarios o string multilínea)

codigo_streamlit = """
import streamlit as st
import plotly.express as px
import pandas as pd

# --- a. Importaciones ---
# (Ya hechas arriba)

# --- b. Título de la App ---
st.title("Dashboard Gapminder Interactivo")

# --- Cargar Datos (función para cachear es buena práctica) ---
@st.cache_data
def cargar_gapminder():
    try:
        df = px.data.gapminder()
        return df
    except Exception:
        # Aquí podrías poner el código para crear el DF de respaldo
        st.error("No se pudieron cargar los datos de Gapminder.")
        return pd.DataFrame() # Retorna DF vacío en caso de error

gapminder_df = cargar_gapminder()

if not gapminder_df.empty:
    # --- c. Widget para seleccionar año ---
    st.header("Selecciona un Año")
    lista_anios = sorted(gapminder_df['year'].unique())
    anio_seleccionado = st.selectbox("Año:", options=lista_anios, index=len(lista_anios)-1) # Default al último año

    # --- d. Filtrar DataFrame ---
    gapminder_filtrado = gapminder_df[gapminder_df['year'] == anio_seleccionado]

    st.header(f"Datos para el año {anio_seleccionado}")

    # --- e. Generar Scatter Plot ---
    fig_scatter_st = px.scatter(
        gapminder_filtrado,
        x="gdpPercap",
        y="lifeExp",
        color="continent",
        size="pop",
        hover_name="country",
        title=f"Esperanza de Vida vs PBI per cápita ({anio_seleccionado})",
        log_x=True,
        size_max=60
    )

    # --- f. Mostrar Gráfico en Streamlit ---
    st.plotly_chart(fig_scatter_st, use_container_width=True) # Ajusta al ancho del contenedor

    # Podrías añadir más gráficos o información aquí...
    st.dataframe(gapminder_filtrado.head())

else:
    st.warning("No se pudieron cargar los datos para mostrar el dashboard.")

"""

print("Código conceptual para la App Streamlit:")
print(codigo_streamlit)

# 3. Cómo ejecutar la App Streamlit:
print("\n--- Cómo ejecutar la App Streamlit ---")
print("1. Guarda el código anterior en un archivo (ej. 'mi_dashboard.py').")
print("2. Abre tu terminal o Anaconda Prompt.")
print("3. Navega hasta el directorio donde guardaste el archivo.")
print("4. Ejecuta el comando: streamlit run mi_dashboard.py")
print("5. Se abrirá una pestaña en tu navegador con la aplicación interactiva.")
print("-" * 20)

# --- Fin de los ejercicios ---
