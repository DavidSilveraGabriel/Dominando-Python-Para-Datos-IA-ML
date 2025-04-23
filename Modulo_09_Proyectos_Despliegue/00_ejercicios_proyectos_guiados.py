# Ejercicios: Módulo 9 - Proyectos Guiados (Conceptual)

print("--- Planificación y Reflexión sobre Proyectos ---")

# --- Ejercicio 1: Elegir un Proyecto ---
# Instrucciones:
# 1. Revisa las ideas de proyectos presentadas en `00_Proyectos_Guiados.md` (o piensa en una idea propia que combine los temas del curso: Python, NumPy, Pandas, Visualización, ML/IA).
# 2. Elige UN proyecto que te interese desarrollar.
# 3. Describe brevemente (en comentarios) el proyecto elegido y por qué te interesa.

# Ejemplo de Respuesta:
# Proyecto Elegido: Análisis de Sentimientos en Reseñas de Películas.
# Interés: Me interesa porque combina NLP (un área de IA/ML), manejo de texto con Python/Pandas,
#          y visualización de resultados. Además, parece un problema práctico y relevante.

print("--- Ejercicio 1: Elegir un Proyecto ---")
print("# Escribe tu elección y justificación como comentario en el código.")
# Respuesta Ejercicio 1:
# Proyecto Elegido: [Escribe aquí el nombre o descripción breve del proyecto]
# Interés: [Explica aquí por qué te interesa este proyecto]
print("-" * 20)


# --- Ejercicio 2: Definir Objetivos y Alcance ---
# Instrucciones:
# Para el proyecto que elegiste en el Ejercicio 1:
# 1. Define el objetivo principal del proyecto de forma clara y concisa (¿Qué problema resuelve? ¿Qué resultado se espera?).
# 2. Define el alcance inicial del proyecto (¿Qué funcionalidades *mínimas* debería tener la primera versión? ¿Qué *no* incluirás inicialmente para mantenerlo manejable?).

# Ejemplo de Respuesta (para Análisis de Sentimientos):
# 1. Objetivo Principal: Clasificar automáticamente reseñas de películas como 'positivas' o 'negativas' basándose en su texto, y visualizar la proporción de sentimientos.
# 2. Alcance Inicial:
#    - Incluir: Cargar un dataset de reseñas etiquetadas, preprocesar el texto (limpieza básica), entrenar un modelo simple de clasificación (ej. Logistic Regression con TF-IDF), evaluar el modelo (accuracy, F1), mostrar la clasificación para nuevas reseñas de ejemplo.
#    - No Incluir Inicialmente: Modelos de DL complejos (BERT), análisis de aspectos específicos (actuación, guion), interfaz web interactiva, manejo de múltiples idiomas.

print("\n--- Ejercicio 2: Definir Objetivos y Alcance ---")
print("# Escribe los objetivos y el alcance de tu proyecto como comentarios.")
# Respuesta Ejercicio 2:
# 1. Objetivo Principal: [Describe aquí el objetivo principal]
# 2. Alcance Inicial:
#    - Incluir: [Enumera las funcionalidades mínimas]
#    - No Incluir Inicialmente: [Enumera funcionalidades que dejarás para después]
print("-" * 20)


# --- Ejercicio 3: Identificar Pasos y Herramientas ---
# Instrucciones:
# Para tu proyecto elegido:
# 1. Enumera los pasos principales que seguirías para desarrollarlo (basándote en el flujo de trabajo de ML/Análisis de Datos).
# 2. Menciona las bibliotecas principales de Python que probablemente necesitarías para cada paso (o para el proyecto en general).

# Ejemplo de Respuesta (para Análisis de Sentimientos):
# 1. Pasos Principales:
#    a. Adquisición/Carga de Datos (reseñas y etiquetas).
#    b. EDA y Preprocesamiento de Texto (limpieza, tokenización, eliminación de stopwords).
#    c. Vectorización de Texto (ej. TF-IDF).
#    d. División Train/Test.
#    e. Selección y Entrenamiento del Modelo (ej. Logistic Regression, Naive Bayes).
#    f. Evaluación del Modelo (accuracy, F1, matriz de confusión).
#    g. (Opcional) Creación de función para predecir nuevas reseñas.
#    h. (Opcional) Visualización de resultados (ej. distribución de sentimientos).
# 2. Bibliotecas Probables:
#    - Pandas (para cargar y manipular datos si están en CSV/DataFrame).
#    - NLTK o spaCy (para preprocesamiento de texto).
#    - Scikit-learn (para vectorización TF-IDF, modelos de clasificación, métricas, train/test split).
#    - Matplotlib/Seaborn (para visualización).

print("\n--- Ejercicio 3: Identificar Pasos y Herramientas ---")
print("# Enumera los pasos y bibliotecas para tu proyecto como comentarios.")
# Respuesta Ejercicio 3:
# 1. Pasos Principales:
#    a. [Paso 1]
#    b. [Paso 2]
#    c. [...]
# 2. Bibliotecas Probables: [Enumera las bibliotecas]
print("-" * 20)


# --- Ejercicio 4: Posibles Desafíos ---
# Instrucciones:
# Piensa en al menos dos desafíos potenciales que podrías encontrar al desarrollar tu proyecto elegido.

# Ejemplo de Respuesta (para Análisis de Sentimientos):
# 1. Desafío 1: Manejo de la negación, sarcasmo e ironía en el texto, que pueden confundir a modelos simples.
# 2. Desafío 2: Obtener un dataset etiquetado de buena calidad y tamaño suficiente. El rendimiento del modelo depende mucho de los datos de entrenamiento.
# 3. Desafío 3: Interpretar por qué el modelo clasifica una reseña de cierta manera (explicabilidad).

print("\n--- Ejercicio 4: Posibles Desafíos ---")
print("# Enumera posibles desafíos para tu proyecto como comentarios.")
# Respuesta Ejercicio 4:
# 1. Desafío 1: [Describe un desafío]
# 2. Desafío 2: [Describe otro desafío]
# 3. (Opcional) Desafío 3: [...]
print("-" * 20)

print("\nPlanificar un proyecto es el primer paso hacia su realización exitosa.")

# --- Fin de los ejercicios ---
