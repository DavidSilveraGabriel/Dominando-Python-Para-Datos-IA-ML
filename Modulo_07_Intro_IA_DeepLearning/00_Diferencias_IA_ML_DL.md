# Módulo 7: Diferencias entre IA, ML y DL

Los términos Inteligencia Artificial (IA), Machine Learning (ML) y Deep Learning (DL) a menudo se usan indistintamente, pero representan conceptos distintos con una relación jerárquica. Entender sus diferencias es clave para navegar por este campo.

Piensa en ellos como muñecas rusas (matrioskas): DL está dentro de ML, que a su vez está dentro de IA.

![Relación IA, ML, DL](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.scnsoft.com%2Fblog-pictures%2Fartificial-intelligence%2Fai-ml-dl.png&f=1&nofb=1&ipt=9e8a1f8a3e8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a&ipo=images)
*(Diagrama conceptual: AI es el campo más amplio, ML es un subconjunto, DL es un subconjunto de ML)*

## 1. Inteligencia Artificial (IA - Artificial Intelligence)

*   **Concepto General:** Es el campo más amplio de la informática dedicado a crear máquinas o sistemas capaces de realizar tareas que normalmente requieren **inteligencia humana**. Esto incluye razonamiento, aprendizaje, resolución de problemas, percepción, comprensión del lenguaje, toma de decisiones, etc.
*   **Objetivo:** Simular o replicar la inteligencia humana en máquinas.
*   **Alcance:** Abarca una gran variedad de técnicas y enfoques, desde sistemas basados en reglas lógicas (IA simbólica o "clásica") hasta enfoques basados en datos como el Machine Learning.
*   **Ejemplos:** Asistentes virtuales (Siri, Alexa), sistemas de recomendación (Netflix, Amazon), coches autónomos, reconocimiento facial, traducción automática, juegos (ajedrez, Go).

**En resumen: IA es la idea general de máquinas que imitan la inteligencia humana.**

## 2. Machine Learning (ML - Aprendizaje Automático)

*   **Concepto Específico:** Es un **subconjunto de la IA**. Se enfoca en desarrollar algoritmos que permiten a los sistemas **aprender de los datos** sin ser programados explícitamente para cada tarea. En lugar de escribir reglas, proporcionamos datos y el algoritmo aprende los patrones.
*   **Objetivo:** Permitir que las máquinas aprendan y mejoren a partir de la experiencia (datos).
*   **Enfoque:** Utiliza algoritmos estadísticos para encontrar patrones en grandes conjuntos de datos.
*   **Tipos:** Incluye Aprendizaje Supervisado (Clasificación, Regresión), Aprendizaje No Supervisado (Clustering, Reducción de Dimensionalidad), y Aprendizaje por Refuerzo.
*   **Ejemplos:** Los algoritmos que vimos en el Módulo 6 (Regresión Lineal, Regresión Logística, SVM, K-NN, Árboles de Decisión, Random Forest) son todos ejemplos de algoritmos de Machine Learning "clásico". Detección de spam, predicción de precios, sistemas de recomendación basados en historial.

**En resumen: ML es un enfoque dentro de la IA que utiliza algoritmos para aprender patrones a partir de datos.**

## 3. Deep Learning (DL - Aprendizaje Profundo)

*   **Concepto Aún Más Específico:** Es un **subconjunto del Machine Learning**. Se basa en **Redes Neuronales Artificiales (Artificial Neural Networks - ANNs)** con **múltiples capas** (de ahí lo de "profundo" - deep).
*   **Inspiración:** Inspirado libremente en la estructura y función del cerebro humano (neuronas y sus conexiones).
*   **Funcionamiento:** Las redes neuronales profundas aprenden representaciones jerárquicas de los datos. Las capas iniciales aprenden características simples (ej. bordes en una imagen), y las capas posteriores combinan estas características para aprender conceptos más complejos (ej. formas, objetos).
*   **Feature Learning:** Una de las grandes ventajas del DL es que a menudo puede realizar **aprendizaje de características (feature learning)** automáticamente. Mientras que en ML clásico a menudo necesitamos realizar ingeniería de características manual, las redes profundas pueden aprender las representaciones más útiles directamente desde los datos brutos (especialmente datos no estructurados como imágenes, texto y audio).
*   **Requisitos:** Generalmente requiere **grandes cantidades de datos** y una **potencia computacional significativa** (a menudo GPUs - Unidades de Procesamiento Gráfico) para entrenar eficazmente.
*   **Ejemplos:** Reconocimiento de imágenes avanzado (clasificación de objetos, detección facial), Procesamiento del Lenguaje Natural (traducción automática, generación de texto, chatbots como ChatGPT), reconocimiento de voz, coches autónomos (percepción del entorno).

**En resumen: DL es una técnica específica dentro de ML que utiliza redes neuronales profundas para aprender representaciones complejas de los datos, destacando en tareas con datos no estructurados.**

**Relación Clave:**

*   Todo Deep Learning es Machine Learning.
*   Todo Machine Learning es Inteligencia Artificial.
*   No toda la IA es ML (ej. sistemas expertos basados en reglas).
*   No todo el ML es DL (ej. Regresión Lineal, SVM con kernel lineal, K-NN son ML pero no DL).

En este curso, nos hemos centrado principalmente en ML clásico con Scikit-learn. Este módulo introduce los conceptos básicos de DL, sentando las bases para una exploración más profunda si te interesa este campo tan activo.
