# Ejercicios: Módulo 7 - Diferencias entre IA, ML y DL

# --- Prerrequisitos ---
# No se requiere código específico, es un ejercicio conceptual.

print("--- Repaso de Conceptos: IA, ML, DL ---")

# --- Ejercicio 1: Definiciones y Relaciones ---
# Instrucciones:
# Basándote en la lección, responde a las siguientes preguntas con comentarios concisos.

# Pregunta A: Define brevemente Inteligencia Artificial (IA) en tus propias palabras.
# Respuesta A: IA es el campo general de la informática que busca crear máquinas o sistemas
#             capaces de realizar tareas que normalmente requieren inteligencia humana
#             (ej. razonamiento, aprendizaje, percepción, resolución de problemas).

# Pregunta B: Define brevemente Machine Learning (ML) y explica cómo se relaciona con la IA.
# Respuesta B: ML es un subcampo de la IA que se enfoca en desarrollar algoritmos que permiten
#             a las máquinas aprender de los datos sin ser programadas explícitamente para cada tarea.
#             Es una *forma* de lograr la IA.

# Pregunta C: Define brevemente Deep Learning (DL) y explica cómo se relaciona con el ML.
# Respuesta C: DL es un subcampo del ML que utiliza redes neuronales artificiales con múltiples
#             capas (profundas) para aprender representaciones complejas de los datos.
#             Es una técnica específica *dentro* del ML, particularmente potente para tareas
#             con datos no estructurados (imágenes, texto, voz).

# Pregunta D: Dibuja (conceptualmente, con texto/símbolos) la relación jerárquica entre IA, ML y DL.
# Respuesta D:
#   IA (Campo General)
#   └── ML (Subcampo de IA - Aprender de datos)
#       └── DL (Subcampo de ML - Redes Neuronales Profundas)

print("Ejercicio 1: Definiciones y Relaciones - Ver comentarios en el código.")
print("-" * 20)


# --- Ejercicio 2: Identificar la Categoría ---
# Instrucciones:
# Para cada escenario, indica si se alinea más estrechamente con IA (general), ML (específico, aprendizaje de datos) o DL (específico, redes profundas). Puede haber solapamiento.

# Escenario 1: Un sistema de chatbot que puede mantener una conversación básica sobre el clima.
# Respuesta 1: IA (general, implica procesamiento de lenguaje natural, puede o no usar ML/DL internamente).

# Escenario 2: Un algoritmo que predice el precio de las acciones para mañana basándose en datos históricos de precios.
# Respuesta 2: ML (específicamente, aprendizaje supervisado - regresión). Podría usar DL, pero ML es la categoría más directa.

# Escenario 3: Un sistema que reconoce automáticamente caras en fotografías.
# Respuesta 3: DL (Deep Learning). El reconocimiento de imágenes es un área donde DL ha demostrado ser extremadamente efectivo con redes neuronales convolucionales (CNNs). Se enmarca dentro de ML e IA.

# Escenario 4: Un programa de ajedrez que utiliza reglas predefinidas y algoritmos de búsqueda (como minimax) para jugar.
# Respuesta 4: IA (clásica o simbólica). No necesariamente aprende de datos (ML), sino que sigue reglas y heurísticas programadas.

# Escenario 5: Un sistema que agrupa noticias de diferentes fuentes por tema automáticamente.
# Respuesta 5: ML (específicamente, aprendizaje no supervisado - clustering o procesamiento de lenguaje natural). Podría usar DL para entender el texto, pero ML es la categoría principal.

# Escenario 6: Un coche autónomo que utiliza sensores y redes neuronales profundas para interpretar su entorno y tomar decisiones de conducción.
# Respuesta 6: DL y ML dentro del marco de la IA. DL es clave para la percepción (visión por computadora), ML para la toma de decisiones y planificación, todo ello contribuyendo a un sistema de IA.

print("\nEjercicio 2: Identificar la Categoría - Ver comentarios en el código.")
print("-" * 20)


# --- Ejercicio 3: ¿Cuándo usar DL? ---
# Instrucciones:
# Basándote en la lección, menciona al menos dos tipos de problemas o datos donde Deep Learning (DL) suele superar a los enfoques de Machine Learning (ML) más tradicionales.

# Respuesta:
# 1. Datos no estructurados complejos: Como imágenes (reconocimiento de objetos, segmentación), audio (reconocimiento de voz) y texto (traducción automática, análisis de sentimientos), donde DL puede aprender automáticamente características jerárquicas complejas.
# 2. Grandes cantidades de datos: Los modelos de DL a menudo requieren grandes datasets para entrenar eficazmente sus millones de parámetros y tienden a mejorar su rendimiento a medida que aumenta la cantidad de datos, superando a modelos ML tradicionales que pueden estancarse.
# 3. Problemas con relaciones muy complejas o no lineales: Donde las interacciones entre características son sutiles y difíciles de capturar con modelos más simples.

print("\nEjercicio 3: ¿Cuándo usar DL? - Ver comentarios en el código.")
print("-" * 20)

print("\nEste módulo introduce los conceptos básicos de IA, ML y DL.")

# --- Fin de los ejercicios ---
