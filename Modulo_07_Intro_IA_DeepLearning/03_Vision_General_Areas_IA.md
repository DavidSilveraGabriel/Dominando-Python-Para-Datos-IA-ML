# Módulo 7: Visión General de Áreas de Aplicación (NLP, Visión por Computador, Sistemas de Recomendación)

El Machine Learning y, en particular, el Deep Learning, han revolucionado numerosas áreas de aplicación. Aquí presentamos una breve visión general de tres campos muy activos donde estas técnicas tienen un impacto enorme:

## 1. Procesamiento del Lenguaje Natural (NLP - Natural Language Processing)

*   **¿Qué es?** Es el campo de la IA enfocado en permitir que las computadoras **entiendan, interpreten y generen lenguaje humano** (texto y habla) de una manera útil.
*   **Desafíos:** El lenguaje humano es inherentemente ambiguo, depende del contexto, evoluciona constantemente y tiene estructuras gramaticales complejas.
*   **Tareas Comunes:**
    *   **Clasificación de Texto:** Asignar categorías a documentos (ej. análisis de sentimiento - positivo/negativo/neutro, detección de spam, clasificación de noticias por tema).
    *   **Reconocimiento de Entidades Nombradas (NER):** Identificar y clasificar entidades como nombres de personas, organizaciones, lugares, fechas en un texto.
    *   **Traducción Automática:** Traducir texto de un idioma a otro (ej. Google Translate).
    *   **Generación de Texto:** Crear texto coherente y relevante (ej. completar frases, escribir resúmenes, chatbots como ChatGPT).
    *   **Sistemas de Preguntas y Respuestas (Q&A):** Responder preguntas formuladas en lenguaje natural, a menudo buscando información en una base de conocimiento o un conjunto de documentos.
    *   **Análisis de Sentimiento:** Determinar la actitud u opinión expresada en un texto.
    *   **Modelado de Temas (Topic Modeling):** Descubrir los temas abstractos principales que ocurren en una colección de documentos.
*   **Técnicas Clave (DL):** Redes Neuronales Recurrentes (RNNs, LSTM, GRU), Mecanismos de Atención, Transformers (arquitectura fundamental para modelos como BERT, GPT), Word Embeddings (Word2Vec, GloVe).
*   **Bibliotecas Populares:** NLTK, spaCy, Transformers (de Hugging Face), Gensim, TensorFlow/Keras, PyTorch.

## 2. Visión por Computador (Computer Vision)

*   **¿Qué es?** Es el campo de la IA que busca permitir que las computadoras **"vean" y entiendan el contenido de imágenes y videos** digitales de manera similar a como lo hacen los humanos.
*   **Desafíos:** Variabilidad en la iluminación, escala, orientación, oclusión (objetos parcialmente cubiertos), deformación de objetos, grandes volúmenes de datos (píxeles).
*   **Tareas Comunes:**
    *   **Clasificación de Imágenes:** Asignar una etiqueta a una imagen completa (ej. "gato", "perro", "coche").
    *   **Detección de Objetos:** Identificar la ubicación (mediante un cuadro delimitador - bounding box) y la clase de múltiples objetos dentro de una imagen.
    *   **Segmentación de Imágenes:** Asignar una etiqueta de clase a **cada píxel** de una imagen.
        *   *Segmentación Semántica:* Etiqueta cada píxel con la clase del objeto al que pertenece (ej. todos los píxeles de coche son "coche").
        *   *Segmentación de Instancia:* Diferencia instancias individuales del mismo objeto (ej. etiqueta "coche1", "coche2").
    *   **Reconocimiento Facial:** Identificar o verificar la identidad de una persona a partir de una imagen de su rostro.
    *   **Análisis de Video:** Tareas como seguimiento de objetos, reconocimiento de acciones, etc.
    *   **Generación de Imágenes:** Crear imágenes nuevas o modificar existentes (ej. StyleGAN, Stable Diffusion).
*   **Técnicas Clave (DL):** Redes Neuronales Convolucionales (CNNs - Convolutional Neural Networks) son la piedra angular (arquitecturas como LeNet, AlexNet, VGG, ResNet, Inception), Transformers también se usan cada vez más (Vision Transformers - ViT).
*   **Bibliotecas Populares:** OpenCV, Pillow, TensorFlow/Keras, PyTorch, Scikit-image.

## 3. Sistemas de Recomendación (Recommender Systems)

*   **¿Qué son?** Son sistemas que buscan **predecir la preferencia o calificación** que un usuario daría a un ítem (ej. película, producto, canción, noticia) y recomiendan los ítems que probablemente le gusten más.
*   **Objetivo:** Ayudar a los usuarios a descubrir ítems relevantes en medio de una gran sobrecarga de información.
*   **Tipos Principales:**
    *   **Filtrado Colaborativo (Collaborative Filtering):** Recomienda ítems basándose en las preferencias de **usuarios similares** o en la similitud entre **ítems** (basado en cómo otros usuarios los han calificado/interactuado). No necesita conocer las características de los ítems o usuarios.
        *   *Basado en Usuario:* Encuentra usuarios similares al usuario actual y recomienda ítems que a esos usuarios similares les gustaron.
        *   *Basado en Ítem:* Encuentra ítems similares a los que le han gustado al usuario actual y recomienda esos ítems similares.
    *   **Filtrado Basado en Contenido (Content-Based Filtering):** Recomienda ítems **similares** a aquellos que le han gustado al usuario en el pasado, basándose en las **características** (contenido) de los ítems y el perfil del usuario.
    *   **Sistemas Híbridos:** Combinan enfoques colaborativos y basados en contenido para mitigar las limitaciones de cada uno (ej. problema del "arranque en frío" - cold start).
*   **Técnicas:** Factorización de Matrices (SVD, NMF), Algoritmos basados en Vecindad (K-NN), Deep Learning (usando redes neuronales para aprender representaciones latentes de usuarios e ítems).
*   **Bibliotecas Populares:** Surprise, LightFM, TensorFlow Recommenders, PyTorch (para modelos DL personalizados), Scikit-learn (para algunos componentes).

Estos son solo tres ejemplos prominentes. El ML y DL se aplican en muchísimos otros dominios, como la bioinformática, finanzas, robótica, juegos, detección de fraudes, análisis de datos de sensores, y más. La elección de las técnicas y algoritmos adecuados depende en gran medida del tipo de datos disponibles y del problema específico que se busca resolver.
