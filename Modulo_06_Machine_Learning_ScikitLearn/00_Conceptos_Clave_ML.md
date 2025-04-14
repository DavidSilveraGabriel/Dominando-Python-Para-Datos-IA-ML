# Módulo 6: Conceptos Clave de Machine Learning (Supervisado vs. No Supervisado, Features, Labels, Train/Test)

¡Bienvenido/a al Módulo 6! Entramos en el emocionante mundo del **Machine Learning (ML)** o Aprendizaje Automático. El ML es un subcampo de la Inteligencia Artificial que se enfoca en desarrollar sistemas que pueden **aprender de los datos** e identificar patrones para tomar decisiones o hacer predicciones con mínima intervención humana.

En lugar de programar reglas explícitas para cada posible escenario, en ML "entrenamos" un modelo con datos para que aprenda esas reglas por sí mismo.

## ¿Qué es Scikit-learn?

**Scikit-learn** es la biblioteca de ML más popular y completa para Python (excluyendo Deep Learning, que tiene sus propios frameworks como TensorFlow/PyTorch). Ofrece:

*   Implementaciones eficientes de una gran variedad de algoritmos de ML (clasificación, regresión, clustering, reducción de dimensionalidad).
*   Herramientas para la evaluación de modelos, selección de características y preprocesamiento de datos.
*   Una API (Interfaz de Programación de Aplicaciones) consistente y fácil de usar.

**Instalación:**
`conda install scikit-learn` o `pip install scikit-learn`
*(A menudo ya viene incluido con distribuciones como Anaconda).*

## Tipos Principales de Machine Learning

Aunque hay más subdivisiones, los dos tipos principales de ML que abordaremos inicialmente son:

1.  **Aprendizaje Supervisado (Supervised Learning):**
    *   **Objetivo:** Aprender una función que mapea entradas (features) a salidas (labels) basándose en **ejemplos etiquetados** de pares entrada-salida.
    *   **Datos:** Se necesita un conjunto de datos donde para cada ejemplo de entrada, ya conocemos la salida correcta (la "etiqueta" o "label").
    *   **Subtipos:**
        *   **Clasificación:** La salida (label) es una **categoría discreta**. El objetivo es asignar nuevas entradas a una de estas categorías predefinidas. (Ej: ¿Es este correo spam o no spam? ¿Es este tumor benigno o maligno? ¿Qué tipo de flor es esta?).
        *   **Regresión:** La salida (label) es un **valor numérico continuo**. El objetivo es predecir un número. (Ej: ¿Cuál será el precio de esta casa? ¿Cuántos clics recibirá este anuncio? ¿Cuál será la temperatura mañana?).

2.  **Aprendizaje No Supervisado (Unsupervised Learning):**
    *   **Objetivo:** Encontrar patrones, estructuras o relaciones interesantes en los datos **sin usar etiquetas predefinidas**. El algoritmo explora los datos por sí mismo.
    *   **Datos:** Solo se necesitan los datos de entrada (features), no se requieren salidas conocidas.
    *   **Subtipos Comunes:**
        *   **Clustering (Agrupamiento):** Agrupar automáticamente datos similares en clústeres o grupos. (Ej: Agrupar clientes con comportamientos de compra similares, agrupar documentos por tema).
        *   **Reducción de Dimensionalidad:** Reducir el número de variables (features) de entrada, manteniendo la mayor cantidad de información relevante posible. Útil para visualización o para mejorar el rendimiento de otros algoritmos de ML. (Ej: Principal Component Analysis - PCA).
        *   **Detección de Anomalías:** Identificar puntos de datos que son significativamente diferentes del resto. (Ej: Detectar transacciones fraudulentas, identificar fallos en sensores).

*(Existe también el Aprendizaje por Refuerzo (Reinforcement Learning), donde un agente aprende a tomar acciones en un entorno para maximizar una recompensa, pero no lo cubriremos en esta introducción).*

## Terminología Clave

*   **Dataset (Conjunto de Datos):** La colección de datos que usamos para entrenar y evaluar nuestro modelo. Generalmente se representa como una tabla (como un DataFrame de Pandas).
*   **Instancia (Instance) / Muestra (Sample) / Observación (Observation):** Una fila individual en el dataset, representando un ejemplo particular.
*   **Característica (Feature):** Una columna individual en el dataset que representa una propiedad medible o característica de una instancia. Son las **entradas** del modelo. (Ej: edad del cliente, precio del producto, tamaño de la casa, palabra en un texto). A menudo se representan como un vector o matriz `X`.
*   **Etiqueta (Label) / Objetivo (Target) / Respuesta (Response):** La columna que representa la **salida** que queremos predecir en el aprendizaje supervisado. (Ej: si el cliente compró o no, el tipo de flor, el precio de la casa). A menudo se representa como un vector `y`.
*   **Modelo (Model):** El algoritmo o sistema entrenado que aprende patrones de los datos y puede hacer predicciones sobre datos nuevos y no vistos.
*   **Entrenamiento (Training):** El proceso de alimentar el dataset (features `X` y, en supervisado, labels `y`) a un algoritmo de ML para que aprenda los patrones y ajuste sus parámetros internos. El resultado es un modelo entrenado.
*   **Prueba (Testing) / Evaluación (Evaluation):** El proceso de usar un conjunto de datos separado (que el modelo no vio durante el entrenamiento) para evaluar qué tan bien generaliza el modelo entrenado a datos nuevos. Medimos su rendimiento usando métricas apropiadas (como precisión, exactitud, error cuadrático medio, etc.).
*   **Predicción (Prediction) / Inferencia (Inference):** El acto de usar un modelo ya entrenado para generar una salida (una etiqueta o un valor) para una nueva instancia de entrada cuyas características (`X`) conocemos, pero cuya etiqueta (`y`) no.

## El Flujo de Trabajo Básico en Scikit-learn (Supervisado)

1.  **Preparar los Datos:** Cargar, limpiar, preprocesar los datos (lo veremos en la siguiente sección). Separar las características (`X`) de la etiqueta (`y`).
2.  **Dividir los Datos:** Separar el dataset en un conjunto de **entrenamiento (train set)** y un conjunto de **prueba (test set)**. Esto es **crucial** para evaluar si el modelo generaliza bien a datos no vistos. Usualmente se usa un 70-80% para entrenamiento y un 20-30% para prueba. Scikit-learn tiene `train_test_split` para esto.
3.  **Elegir un Modelo:** Seleccionar un algoritmo de ML apropiado para la tarea (ej. `LinearRegression` para regresión, `LogisticRegression` o `KNeighborsClassifier` para clasificación).
4.  **Entrenar el Modelo:** Llamar al método `.fit(X_train, y_train)` del modelo, pasándole los datos de entrenamiento.
5.  **Hacer Predicciones:** Llamar al método `.predict(X_test)` del modelo entrenado, pasándole las características del conjunto de prueba.
6.  **Evaluar el Modelo:** Comparar las predicciones (`y_pred`) con las etiquetas reales del conjunto de prueba (`y_test`) usando métricas de evaluación adecuadas (ej. `accuracy_score`, `mean_squared_error`).

Entender estos conceptos y el flujo general es el primer paso para aplicar Machine Learning de manera efectiva. En las siguientes secciones, veremos cómo implementar estos pasos con Scikit-learn.
