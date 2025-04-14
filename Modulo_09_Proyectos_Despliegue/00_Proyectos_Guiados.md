# Módulo 9: Desarrollo Guiado de Proyectos de Portafolio

¡Felicidades por llegar al último módulo de contenido teórico! Ahora es el momento de aplicar todo lo que has aprendido en proyectos prácticos que demuestren tus habilidades y que puedas incluir en tu portafolio profesional.

Este módulo se centrará en guiarte paso a paso a través del desarrollo de 2 o 3 proyectos completos, desde la obtención de datos hasta (en algunos casos) un prototipo o análisis final. El objetivo es integrar los conocimientos de Python, NumPy, Pandas, Matplotlib/Seaborn y Scikit-learn.

**Nota:** Este archivo describe las *ideas* de los proyectos. La implementación detallada (código, explicaciones paso a paso) se proporcionaría en los materiales correspondientes del curso (videos, notebooks guiados, etc.).

## Ideas de Proyectos Guiados:

Aquí tienes algunas ideas de proyectos que podríamos desarrollar, cubriendo diferentes aspectos del curso:

**Proyecto 1: Análisis Exploratorio de Datos (EDA) de un Dataset Público**

*   **Objetivo:** Aplicar técnicas de limpieza, manipulación, agregación y visualización para extraer insights de un dataset real.
*   **Dataset Sugerido:**
    *   Dataset de Supervivencia del Titanic (clásico para empezar).
    *   Dataset de Precios de Viviendas (ej. Ames Housing dataset).
    *   Dataset de Películas (ej. IMDb o MovieLens).
    *   Un dataset de tu interés encontrado en plataformas como Kaggle, UCI Machine Learning Repository, Google Datasets.
*   **Pasos Guiados:**
    1.  **Carga de Datos:** Leer el dataset usando Pandas (`pd.read_csv`, etc.).
    2.  **Exploración Inicial:** `info()`, `describe()`, `head()`, `value_counts()`.
    3.  **Limpieza:** Identificar y manejar valores nulos (`isnull()`, `fillna()`, `dropna()`) y duplicados (`duplicated()`, `drop_duplicates()`). Corregir tipos de datos si es necesario.
    4.  **Ingeniería de Características (Básica):** Crear nuevas columnas a partir de las existentes si es relevante (ej. extraer mes de una fecha, crear categorías de edad).
    5.  **Análisis Univariado:** Visualizar la distribución de variables individuales (histogramas, boxplots, countplots con Matplotlib/Seaborn).
    6.  **Análisis Bivariado:** Explorar relaciones entre pares de variables (scatter plots, boxplots por categoría, mapas de calor de correlación).
    7.  **Agregación:** Usar `groupby()` para calcular estadísticas resumidas por categorías (ej. precio medio por ciudad, tasa de supervivencia por clase en Titanic).
    8.  **Conclusiones:** Resumir los hallazgos clave y posibles próximos pasos.

**Proyecto 2: Modelo Predictivo Simple (Clasificación o Regresión)**

*   **Objetivo:** Construir un modelo de Machine Learning básico con Scikit-learn para predecir una variable objetivo, siguiendo el flujo de trabajo de ML.
*   **Dataset Sugerido:**
    *   **Clasificación:** Dataset Iris (predecir especie), Dataset de Cáncer de Mama Wisconsin, Dataset de Calidad del Vino (clasificar calidad).
    *   **Regresión:** Dataset de Diabetes, Dataset de Precios de Viviendas de Boston (datasets clásicos incluidos en Scikit-learn o fáciles de encontrar).
*   **Pasos Guiados:**
    1.  **Carga y Preparación:** Cargar datos, realizar EDA básico y limpieza (similar al Proyecto 1).
    2.  **Selección de Features y Target:** Separar `X` e `y`.
    3.  **Preprocesamiento:** Escalar características numéricas (`StandardScaler`), codificar características categóricas si las hay (`OneHotEncoder`).
    4.  **División Train/Test:** Usar `train_test_split`.
    5.  **Selección y Entrenamiento:** Elegir un modelo simple (ej. `LogisticRegression` o `KNeighborsClassifier` para clasificación; `LinearRegression` o `Ridge` para regresión) y entrenarlo con `.fit(X_train, y_train)`.
    6.  **Predicción:** Hacer predicciones en el conjunto de prueba con `.predict(X_test)`.
    7.  **Evaluación:** Calcular métricas apropiadas (accuracy, precision, recall, F1, matriz de confusión para clasificación; MAE, MSE, RMSE, R² para regresión).
    8.  **Interpretación (Básica):** Si es posible (ej. coeficientes de Regresión Lineal), intentar interpretar qué características influyen más.
    9.  **Conclusiones:** Discutir el rendimiento del modelo y posibles mejoras.

**Proyecto 3 (Opcional/Avanzado): Creación de una API Simple para un Modelo o Dashboard Interactivo**

*   **Objetivo:** Exponer un modelo de ML entrenado a través de una API web simple o crear un dashboard interactivo para explorar datos o resultados del modelo.
*   **Herramientas Sugeridas:**
    *   **API:** Flask o FastAPI.
    *   **Dashboard:** Streamlit o Plotly Dash.
*   **Pasos Guiados (Esquemático):**
    1.  **Entrenar y Guardar Modelo:** Entrenar un modelo (como en el Proyecto 2) y guardarlo (ej. con `joblib`).
    2.  **Desarrollo de API (Flask/FastAPI):**
        *   Crear un endpoint (ruta) que reciba datos de entrada (features).
        *   Cargar el modelo guardado.
        *   Preprocesar los datos de entrada de la misma forma que en el entrenamiento.
        *   Hacer la predicción usando el modelo cargado.
        *   Devolver la predicción (ej. en formato JSON).
    3.  **Desarrollo de Dashboard (Streamlit):**
        *   Crear un script de Streamlit.
        *   Añadir títulos, texto explicativo.
        *   Cargar datos (o permitir carga de archivos).
        *   Añadir widgets interactivos (sliders, selectores) para filtrar datos o seleccionar parámetros.
        *   Mostrar DataFrames filtrados.
        *   Generar y mostrar gráficos interactivos (usando Plotly o Seaborn/Matplotlib dentro de Streamlit) basados en las selecciones del usuario.
        *   (Opcional) Cargar un modelo pre-entrenado y permitir al usuario introducir datos para obtener predicciones.

Estos proyectos te permitirán consolidar tus conocimientos y construir piezas valiosas para tu portafolio, demostrando tu capacidad para aplicar Python y sus bibliotecas a problemas reales de ciencia de datos y machine learning.
