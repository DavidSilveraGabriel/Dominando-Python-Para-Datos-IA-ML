![Curso Python Banner](assets/banner.png)

# Bienvenido al Curso Completo de Python para Ciencia de Datos, IA y ML en Español

¡Prepárate para un viaje completo en el mundo de Python aplicado a la Ciencia de Datos, Inteligencia Artificial y Machine Learning! Este curso está diseñado para llevarte desde CERO hasta ser capaz de construir y desplegar tus propias aplicaciones, creando un portafolio sólido en el proceso.

Nos enfocaremos en las **mejores prácticas** tanto del desarrollo de software como de la aplicación de Python en el análisis de datos y la IA, siguiendo la guía de estilo **PEP 8** para un código limpio y legible.

# 🚀 Configuración Inicial

Para seguir este curso y ejecutar los ejemplos y ejercicios, es recomendable configurar un entorno virtual aislado. Esto asegura que las dependencias del proyecto no interfieran con otras instalaciones de Python en tu sistema.

1.  **Clona el Repositorio (si aún no lo has hecho):**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_CARPETA_DEL_REPOSITORIO>
    ```

2.  **Crea el Entorno Virtual:**
    Abre una terminal en la carpeta raíz del proyecto y ejecuta:
    ```bash
    # Crear el entorno virtual (se creará una carpeta .venv)
    python -m venv .venv
    ```

3.  **Activa el Entorno Virtual:**
    *   **Windows (cmd/powershell):**
        ```bash
        .\.venv\Scripts\activate
        ```
    *   **macOS/Linux (bash/zsh):**
        ```bash
        source .venv/bin/activate
        ```
    Una vez activado, verás `(.venv)` al inicio de la línea de tu terminal.

4.  **Instala las Dependencias:**
    Asegúrate de tener el archivo `requirements.txt` en la raíz del proyecto. Luego, instala todas las librerías necesarias con:
    ```bash
    # Instalar las librerías necesarias
    pip install -r requirements.txt
    ```

¡Listo! Ahora tienes un entorno limpio y configurado para trabajar con el material del curso. Recuerda activar el entorno (`source .venv/bin/activate` o `.\.venv\Scripts\activate`) cada vez que abras una nueva terminal para trabajar en este proyecto.

## Estructura del Curso

El curso se divide en los siguientes módulos, diseñados para un aprendizaje progresivo. Cada lección teórica se complementa con ejercicios prácticos diseñados para reforzar tu aprendizaje.

**Módulo 0: Introducción y Configuración del Entorno**
*   Bienvenida y objetivos del curso. [📝](Modulo_00_Introduccion_Configuracion/00_Bienvenida_Objetivos.md)
*   ¿Por qué Python para Ciencia de Datos, IA y ML? [📝](Modulo_00_Introduccion_Configuracion/01_Por_Que_Python.md)
*   Instalación de Python y Anaconda/Miniconda. [📝](Modulo_00_Introduccion_Configuracion/02_Instalacion_Python_Anaconda.md)
*   Uso de la terminal/línea de comandos. [📝](Modulo_00_Introduccion_Configuracion/03_Uso_Terminal.md)
*   Introducción a los IDEs (VS Code, Jupyter Notebooks/Lab). [📝](Modulo_00_Introduccion_Configuracion/04_Introduccion_IDEs.md)
*   Gestión de entornos virtuales (`conda`, `venv`). [📝](Modulo_00_Introduccion_Configuracion/05_Entornos_Virtuales.md)
*   Introducción a Git y GitHub para control de versiones. [📝](Modulo_00_Introduccion_Configuracion/06_Introduccion_Git_GitHub.md)

**Módulo 1: Fundamentos de Python (Nivelación)**
*   Sintaxis básica, comentarios, sangría. [📝](Modulo_01_Fundamentos_Python/00_Sintaxis_Comentarios_Sangria.md) [💻](Modulo_01_Fundamentos_Python/00_ejercicios_sintaxis.py)
*   Variables y tipos de datos primitivos (int, float, bool, str). [📝](Modulo_01_Fundamentos_Python/01_Variables_Tipos_Datos.md) [💻](Modulo_01_Fundamentos_Python/01_ejercicios_variables.py)
*   Operadores (aritméticos, comparación, lógicos). [📝](Modulo_01_Fundamentos_Python/02_Operadores.md) [💻](Modulo_01_Fundamentos_Python/02_ejercicios_operadores.py)
*   Estructuras de datos: Listas, Tuplas, Diccionarios, Conjuntos (Sets). [📝](Modulo_01_Fundamentos_Python/03_Estructuras_Datos.md) [💻](Modulo_01_Fundamentos_Python/03_ejercicios_estructuras.py)
*   Control de flujo: Condicionales (`if`, `elif`, `else`). [📝](Modulo_01_Fundamentos_Python/04_Control_Flujo_Condicionales.md) [💻](Modulo_01_Fundamentos_Python/04_ejercicios_condicionales.py)
*   Bucles: `for` y `while`. `break`, `continue`. [📝](Modulo_01_Fundamentos_Python/05_Control_Flujo_Bucles.md) [💻](Modulo_01_Fundamentos_Python/05_ejercicios_bucles.py)
*   Funciones: Definición, parámetros, retorno, scope. [📝](Modulo_01_Fundamentos_Python/06_Funciones.md) [💻](Modulo_01_Fundamentos_Python/06_ejercicios_funciones.py)
*   Manejo de errores básicos (`try`, `except`). [📝](Modulo_01_Fundamentos_Python/07_Manejo_Errores.md) [💻](Modulo_01_Fundamentos_Python/07_ejercicios_errores.py)
*   Buenas prácticas iniciales y PEP 8. [📝](Modulo_01_Fundamentos_Python/08_Buenas_Practicas_PEP8.md) [💻](Modulo_01_Fundamentos_Python/08_ejercicios_pep8.py)

**Módulo 2: Python Intermedio y Estructura de Proyectos**
*   Programación Orientada a Objetos (Clases, objetos). [📝](Modulo_02_Python_Intermedio_Estructura/00_POO_Clases_Objetos.md) [💻](Modulo_02_Python_Intermedio_Estructura/00_ejercicios_poo_clases_objetos.py)
*   Programación Orientada a Objetos (Herencia). [📝](Modulo_02_Python_Intermedio_Estructura/01_POO_Herencia.md) [💻](Modulo_02_Python_Intermedio_Estructura/01_ejercicios_poo_herencia.py)
*   Programación Orientada a Objetos (Encapsulamiento). [📝](Modulo_02_Python_Intermedio_Estructura/02_POO_Encapsulamiento.md) [💻](Modulo_02_Python_Intermedio_Estructura/02_ejercicios_poo_encapsulamiento.py)
*   Módulos y Paquetes: Importación, creación. [📝](Modulo_02_Python_Intermedio_Estructura/03_Modulos_Paquetes.md) [💻](Modulo_02_Python_Intermedio_Estructura/03_ejercicios_modulos_paquetes.py)
*   Manejo de Ficheros (lectura, escritura). [📝](Modulo_02_Python_Intermedio_Estructura/04_Manejo_Ficheros.md) [💻](Modulo_02_Python_Intermedio_Estructura/04_ejercicios_manejo_ficheros.py)
*   Comprensión de listas, diccionarios y sets. [📝](Modulo_02_Python_Intermedio_Estructura/05_Comprensiones.md) [💻](Modulo_02_Python_Intermedio_Estructura/05_ejercicios_comprensiones.py)
*   Funciones Lambda, `map`, `filter`. [📝](Modulo_02_Python_Intermedio_Estructura/06_Lambdas_Map_Filter.md) [💻](Modulo_02_Python_Intermedio_Estructura/06_ejercicios_lambdas_map_filter.py)
*   Introducción a Decoradores. [📝](Modulo_02_Python_Intermedio_Estructura/07_Decoradores.md) [💻](Modulo_02_Python_Intermedio_Estructura/07_ejercicios_decoradores.py)
*   Estructura de un proyecto Python estándar. [📝](Modulo_02_Python_Intermedio_Estructura/08_Estructura_Proyecto.md) [💻](Modulo_02_Python_Intermedio_Estructura/08_ejercicios_estructura_proyecto.py)
*   Introducción a las pruebas unitarias (`unittest` o `pytest`). [📝](Modulo_02_Python_Intermedio_Estructura/09_Pruebas_Unitarias.md) [💻](Modulo_02_Python_Intermedio_Estructura/09_ejercicios_pruebas_unitarias.py)

**Módulo 3: NumPy - Computación Numérica**
*   Introducción a NumPy: Arrays (`ndarray`). [📝](Modulo_03_NumPy/00_Introduccion_NumPy_Arrays.md) [💻](Modulo_03_NumPy/00_ejercicios_introduccion.py)
*   Creación de arrays, indexación, slicing. [📝](Modulo_03_NumPy/01_Creacion_Arrays_Indexacion_Slicing.md) [💻](Modulo_03_NumPy/01_ejercicios_creacion_indexacion_slicing.py)
*   Operaciones matemáticas y estadísticas vectorizadas. [📝](Modulo_03_NumPy/02_Operaciones_Vectorizadas.md) [💻](Modulo_03_NumPy/02_ejercicios_operaciones_vectorizadas.py)
*   Broadcasting. [📝](Modulo_03_NumPy/03_Broadcasting.md) [💻](Modulo_03_NumPy/03_ejercicios_broadcasting.py)
*   Ejercicios prácticos con datos numéricos. [📝](Modulo_03_NumPy/04_Ejercicios_NumPy.md)

**Módulo 4: Pandas - Manipulación y Análisis de Datos**
*   Introducción a Pandas: Series y DataFrames. [📝](Modulo_04_Pandas/00_Introduccion_Pandas_Series_DataFrames.md) [💻](Modulo_04_Pandas/00_ejercicios_introduccion_pandas.py)
*   Lectura y escritura de datos (CSV, Excel, etc.). [📝](Modulo_04_Pandas/01_Lectura_Escritura_Datos.md) [💻](Modulo_04_Pandas/01_ejercicios_lectura_escritura.py)
*   Selección, filtrado, indexación (loc, iloc). [📝](Modulo_04_Pandas/02_Seleccion_Filtrado_Indexacion.md) [💻](Modulo_04_Pandas/02_ejercicios_seleccion_filtrado.py)
*   Limpieza de datos: Nulos, duplicados. [📝](Modulo_04_Pandas/03_Limpieza_Datos_Nulos_Duplicados.md) [💻](Modulo_04_Pandas/03_ejercicios_limpieza_datos.py)
*   Agrupación de datos (`groupby`). [📝](Modulo_04_Pandas/04_Agrupacion_Datos_Groupby.md) [💻](Modulo_04_Pandas/04_ejercicios_agrupacion_groupby.py)
*   Combinación de DataFrames (`merge`, `join`, `concat`). [📝](Modulo_04_Pandas/05_Combinacion_DataFrames.md) [💻](Modulo_04_Pandas/05_ejercicios_combinacion_dataframes.py)
*   Series temporales (básico). [📝](Modulo_04_Pandas/06_Series_Temporales.md) [💻](Modulo_04_Pandas/06_ejercicios_series_temporales.py)
*   Ejercicios de análisis exploratorio de datos (EDA). [📝](Modulo_04_Pandas/07_Ejercicios_Pandas_EDA.md)

**Módulo 5: Visualización de Datos**
*   Introducción a Matplotlib: Gráficos básicos. [📝](Modulo_05_Visualizacion_Datos/00_Introduccion_Matplotlib_Basico.md) [💻](Modulo_05_Visualizacion_Datos/00_ejercicios_matplotlib_basico.py)
*   Personalización de gráficos con Matplotlib. [📝](Modulo_05_Visualizacion_Datos/01_Personalizacion_Matplotlib.md) [💻](Modulo_05_Visualizacion_Datos/01_ejercicios_personalizacion_matplotlib.py)
*   Introducción a Seaborn: Gráficos estadísticos. [📝](Modulo_05_Visualizacion_Datos/02_Introduccion_Seaborn.md) [💻](Modulo_05_Visualizacion_Datos/02_ejercicios_introduccion_seaborn.py)
*   Visualización de relaciones, distribuciones, categorías con Seaborn. [📝](Modulo_05_Visualizacion_Datos/03_Seaborn_Relaciones_Distribuciones_Categorias.md) [💻](Modulo_05_Visualizacion_Datos/03_ejercicios_seaborn_rel_dist_cat.py)
*   (Opcional) Gráficos interactivos (Plotly/Streamlit). [📝](Modulo_05_Visualizacion_Datos/04_Graficos_Interactivos_Plotly_Streamlit.md) [💻](Modulo_05_Visualizacion_Datos/04_ejercicios_plotly_streamlit.py)

**Módulo 6: Fundamentos de Machine Learning con Scikit-learn**
*   Conceptos clave: Supervisado vs. No supervisado, entrenamiento, prueba. [📝](Modulo_06_Machine_Learning_ScikitLearn/00_Conceptos_Clave_ML.md) [💻](Modulo_06_Machine_Learning_ScikitLearn/00_ejercicios_conceptos_ml.py)
*   Preprocesamiento de datos: Escalado, codificación. [📝](Modulo_06_Machine_Learning_ScikitLearn/01_Preprocesamiento_Escalado_Codificacion.md) [💻](Modulo_06_Machine_Learning_ScikitLearn/01_ejercicios_preprocesamiento.py)
*   División de datos (train/test split). [📝](Modulo_06_Machine_Learning_ScikitLearn/02_Division_Datos_Train_Test.md) [💻](Modulo_06_Machine_Learning_ScikitLearn/02_ejercicios_division_datos.py)
*   Modelos de Regresión (Lineal, etc.). [📝](Modulo_06_Machine_Learning_ScikitLearn/03_Modelos_Regresion.md) [💻](Modulo_06_Machine_Learning_ScikitLearn/03_ejercicios_regresion.py)
*   Modelos de Clasificación (Logística, K-NN, SVM, Árboles). [📝](Modulo_06_Machine_Learning_ScikitLearn/04_Modelos_Clasificacion.md) [💻](Modulo_06_Machine_Learning_ScikitLearn/04_ejercicios_clasificacion.py)
*   Evaluación de modelos: Métricas comunes. [📝](Modulo_06_Machine_Learning_ScikitLearn/05_Evaluacion_Modelos.md) [💻](Modulo_06_Machine_Learning_ScikitLearn/05_ejercicios_evaluacion_modelos.py)
*   Selección de características y reducción de dimensionalidad (PCA básico). [📝](Modulo_06_Machine_Learning_ScikitLearn/06_Seleccion_Caracteristicas_PCA.md) [💻](Modulo_06_Machine_Learning_ScikitLearn/06_ejercicios_pca.py)
*   Flujo de trabajo de un proyecto de ML. [📝](Modulo_06_Machine_Learning_ScikitLearn/07_Flujo_Trabajo_ML.md) [💻](Modulo_06_Machine_Learning_ScikitLearn/07_ejercicios_flujo_trabajo_ml.py)

**Módulo 7: Introducción a la Inteligencia Artificial y Deep Learning**
*   Diferencias entre IA, ML y DL. [📝](Modulo_07_Intro_IA_DeepLearning/00_Diferencias_IA_ML_DL.md) [💻](Modulo_07_Intro_IA_DeepLearning/00_ejercicios_conceptos_ia.py)
*   Introducción a las redes neuronales. [📝](Modulo_07_Intro_IA_DeepLearning/01_Intro_Redes_Neuronales.md) [💻](Modulo_07_Intro_IA_DeepLearning/01_ejercicios_redes_neuronales.py)
*   Frameworks populares: TensorFlow y/o PyTorch (conceptos básicos). [📝](Modulo_07_Intro_IA_DeepLearning/02_Frameworks_TensorFlow_PyTorch.md) [💻](Modulo_07_Intro_IA_DeepLearning/02_ejercicios_frameworks_dl.py)
*   Visión general de áreas: NLP, Visión por Computador, Sistemas de Recomendación. [📝](Modulo_07_Intro_IA_DeepLearning/03_Vision_General_Areas_IA.md) [💻](Modulo_07_Intro_IA_DeepLearning/03_ejercicios_areas_ia.py)
*   Creación de un modelo simple (ej. clasificación MNIST). [📝](Modulo_07_Intro_IA_DeepLearning/04_Creacion_Modelo_Simple_MNIST.md) [💻](Modulo_07_Intro_IA_DeepLearning/04_ejercicios_modelo_simple_mnist.py)
*   Ética en la IA. [📝](Modulo_07_Intro_IA_DeepLearning/05_Etica_IA.md) [💻](Modulo_07_Intro_IA_DeepLearning/05_ejercicios_etica_ia.py)

**Módulo 8: Python Avanzado**
*   Generadores y Expresiones Generadoras. [📝](Modulo_08_Python_Avanzado/00_Generadores.md) [💻](Modulo_08_Python_Avanzado/00_ejercicios_generadores.py)
*   Decoradores (uso avanzado). [📝](Modulo_08_Python_Avanzado/01_Decoradores_Avanzado.md) [💻](Modulo_08_Python_Avanzado/01_ejercicios_decoradores_avanzado.py)
*   Context Managers (`with` statement). [📝](Modulo_08_Python_Avanzado/02_Context_Managers.md) [💻](Modulo_08_Python_Avanzado/02_ejercicios_context_managers.py)
*   Manejo Avanzado de Excepciones. [📝](Modulo_08_Python_Avanzado/03_Manejo_Excepciones_Avanzado.md) [💻](Modulo_08_Python_Avanzado/03_ejercicios_excepciones_avanzado.py)
*   Programación Funcional Avanzada (`functools`, `itertools`). [📝](Modulo_08_Python_Avanzado/04_Programacion_Funcional.md) [💻](Modulo_08_Python_Avanzado/04_ejercicios_programacion_funcional.py)
*   Tipado Estático (Type Hinting). [📝](Modulo_08_Python_Avanzado/05_Tipado_Estatico.md) [💻](Modulo_08_Python_Avanzado/05_ejercicios_tipado_estatico.py)
*   (Opcional) Introducción a Concurrencia/Paralelismo. [📝](Modulo_08_Python_Avanzado/06_Concurrencia_Paralelismo.md) [💻](Modulo_08_Python_Avanzado/06_ejercicios_concurrencia_paralelismo.py)

**Módulo 9: Proyectos de Portafolio y Despliegue**
*   Desarrollo guiado de 2-3 proyectos completos. [📝](Modulo_09_Proyectos_Despliegue/00_Proyectos_Guiados.md) [💻](Modulo_09_Proyectos_Despliegue/00_ejercicios_proyectos_guiados.py)
*   Creación de APIs simples con Flask/FastAPI. [📝](Modulo_09_Proyectos_Despliegue/01_APIs_Simples_Flask_FastAPI.md) [💻](Modulo_09_Proyectos_Despliegue/01_ejercicios_apis_simples.py)
*   **Despliegue con Docker:** Contenerización de aplicaciones/modelos. [📝](Modulo_09_Proyectos_Despliegue/02_Despliegue_Docker.md) [💻](Modulo_09_Proyectos_Despliegue/02_ejercicios_docker.py)
*   Visión general de otras opciones de despliegue (Streamlit Cloud, Heroku, etc.). [📝](Modulo_09_Proyectos_Despliegue/03_Otras_Opciones_Despliegue.md) [💻](Modulo_09_Proyectos_Despliegue/03_ejercicios_otras_opciones_despliegue.py)
*   Consejos para construir y presentar el portafolio. [📝](Modulo_09_Proyectos_Despliegue/04_Consejos_Portafolio.md) [💻](Modulo_09_Proyectos_Despliegue/04_ejercicios_portafolio.py)

## ¡Empecemos!

Este `README.md` servirá como nuestra guía principal. ¡Estamos listos para comenzar a construir este increíble curso!
