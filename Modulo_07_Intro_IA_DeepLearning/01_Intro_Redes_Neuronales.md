# Módulo 7: Introducción a las Redes Neuronales Artificiales (ANN)

Las **Redes Neuronales Artificiales (ANNs)**, o simplemente redes neuronales, son el corazón del Deep Learning. Son modelos computacionales inspirados (muy libremente) en la estructura y el funcionamiento de las redes neuronales biológicas del cerebro.

## Inspiración Biológica (Simplificada)

*   El cerebro está compuesto por miles de millones de **neuronas** interconectadas.
*   Cada neurona recibe señales de otras neuronas a través de **dendritas**.
*   Si la suma de estas señales supera un cierto **umbral**, la neurona se "activa" y envía una señal a otras neuronas a través de su **axón**.
*   La fuerza de la conexión entre neuronas (la **sinapsis**) puede cambiar con el aprendizaje.

## Componentes de una Neurona Artificial (Perceptrón Simple)

Una neurona artificial, a menudo llamada **nodo** o **unidad**, es un modelo matemático simplificado:

1.  **Entradas (`x1, x2, ..., xn`):** Recibe señales (valores numéricos) de otras neuronas o directamente de los datos de entrada (features).
2.  **Pesos (`w1, w2, ..., wn`):** Cada entrada tiene un peso asociado, que representa la "fuerza" o importancia de esa conexión. El aprendizaje consiste en ajustar estos pesos.
3.  **Suma Ponderada:** La neurona calcula la suma ponderada de sus entradas: `suma = (x1*w1) + (x2*w2) + ... + (xn*wn)`.
4.  **Sesgo (Bias - `b`):** Se añade un término de sesgo a la suma ponderada: `z = suma + b`. El sesgo permite a la neurona ajustar su umbral de activación independientemente de las entradas.
5.  **Función de Activación (`f`):** La suma ponderada más el sesgo (`z`) pasa a través de una función de activación no lineal. Esta función introduce no linealidad en el modelo, permitiendo a la red aprender relaciones complejas (sin ella, una red multicapa sería equivalente a una sola capa lineal). El resultado `a = f(z)` es la **salida** de la neurona.

![Neurona Artificial Simple](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F6%2F60%2FArtificialNeuronModel_english.png%2F1200px-ArtificialNeuronModel_english.png&f=1&nofb=1&ipt=e9f8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a&ipo=images)
*(Diagrama: Entradas (x) multiplicadas por pesos (w), sumadas con sesgo (b), y pasadas por función de activación (f) para producir salida (a))*

## Funciones de Activación Comunes

*   **Sigmoide:** `f(z) = 1 / (1 + exp(-z))`. Comprime la salida al rango (0, 1). Usada históricamente, especialmente en capas de salida para clasificación binaria (interpretada como probabilidad), pero puede sufrir de "gradientes desvanecientes" en redes profundas.
*   **Tangente Hiperbólica (tanh):** `f(z) = tanh(z)`. Comprime la salida al rango (-1, 1). Similar a sigmoide pero centrada en cero. También puede sufrir de gradientes desvanecientes.
*   **ReLU (Rectified Linear Unit):** `f(z) = max(0, z)`. Es la función de activación más popular en capas ocultas actualmente. Es computacionalmente eficiente y ayuda a mitigar el problema de los gradientes desvanecientes. Si la entrada es negativa, la salida es 0; si es positiva, la salida es igual a la entrada.
*   **Softmax:** Se usa típicamente en la **capa de salida** para clasificación **multiclase**. Convierte las salidas brutas de la red en una distribución de probabilidad sobre las clases (los valores suman 1).

## Estructura de una Red Neuronal (Feedforward)

Las neuronas se organizan en **capas**:

1.  **Capa de Entrada (Input Layer):** Recibe los datos brutos (las características `X`). El número de neuronas en esta capa es igual al número de características de entrada. No realiza cálculos, solo pasa los datos.
2.  **Capas Ocultas (Hidden Layers):** Una o más capas entre la entrada y la salida. Aquí es donde ocurre la mayor parte del procesamiento y aprendizaje de patrones complejos. El número de capas ocultas y el número de neuronas en cada capa son **hiperparámetros** clave del diseño de la red. Una red con una o más capas ocultas puede aprender relaciones no lineales.
3.  **Capa de Salida (Output Layer):** Produce el resultado final de la red (la predicción). El número de neuronas y la función de activación en esta capa dependen de la tarea:
    *   **Regresión:** Generalmente una neurona con activación lineal (o sin activación).
    *   **Clasificación Binaria:** Generalmente una neurona con activación sigmoide.
    *   **Clasificación Multiclase:** Generalmente N neuronas (una por clase) con activación softmax.

En una red **Feedforward** (la más común inicialmente), la información fluye en una sola dirección: desde la capa de entrada, a través de las capas ocultas, hasta la capa de salida, sin ciclos.

![Red Neuronal Feedforward Simple](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F0%2F00%2FMulti-Layer_Neural_Network-vector.svg%2F1200px-Multi-Layer_Neural_Network-vector.svg.png&f=1&nofb=1&ipt=e9f8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a1b8a&ipo=images)
*(Diagrama: Capa de entrada, una o más capas ocultas, capa de salida. Conexiones hacia adelante.)*

## ¿Cómo Aprenden las Redes Neuronales? (Intuición)

1.  **Inicialización:** Los pesos y sesgos se inicializan con valores pequeños (a menudo aleatorios).
2.  **Propagación Hacia Adelante (Forward Propagation):** Se presenta una instancia de entrenamiento a la capa de entrada. La información fluye a través de la red, capa por capa, calculando las sumas ponderadas y aplicando las funciones de activación, hasta generar una predicción en la capa de salida.
3.  **Cálculo de la Pérdida (Loss Function):** Se compara la predicción de la red con la etiqueta real (en aprendizaje supervisado) usando una **función de pérdida** (o función de coste) que mide qué tan "equivocada" está la predicción (ej. Error Cuadrático Medio para regresión, Entropía Cruzada para clasificación).
4.  **Propagación Hacia Atrás (Backpropagation):** Se calcula el **gradiente** de la función de pérdida con respecto a cada peso y sesgo en la red. Este gradiente indica en qué dirección se deben ajustar los pesos/sesgos para *reducir* el error. La "magia" de backpropagation es que calcula estos gradientes eficientemente, propagando el error hacia atrás desde la capa de salida hasta la de entrada.
5.  **Actualización de Pesos:** Se utiliza un algoritmo de optimización (el más común es el **Descenso de Gradiente - Gradient Descent** y sus variantes como Adam, RMSprop) para ajustar los pesos y sesgos en la dirección opuesta al gradiente, dando pequeños pasos para minimizar la función de pérdida.
6.  **Iteración:** Se repiten los pasos 2-5 para muchas instancias de entrenamiento (a menudo en lotes o "batches") y durante múltiples pasadas completas por el dataset de entrenamiento (llamadas "epochs"), hasta que el modelo converge a un buen rendimiento.

## Deep Learning = Redes Profundas

El **Deep Learning** se refiere específicamente al uso de redes neuronales con **múltiples capas ocultas** (a veces decenas o cientos). Estas capas adicionales permiten a la red aprender jerarquías de características cada vez más abstractas y complejas, lo que las hace especialmente potentes para tareas con datos no estructurados y complejos como imágenes, audio y texto.

Esta es una introducción muy básica. Las redes neuronales y el deep learning son campos vastos con muchas arquitecturas diferentes (Redes Convolucionales - CNNs, Redes Recurrentes - RNNs, Transformers, etc.) y conceptos avanzados. Sin embargo, entender la estructura básica de neuronas, capas, activación y el flujo general de aprendizaje es el primer paso fundamental.
