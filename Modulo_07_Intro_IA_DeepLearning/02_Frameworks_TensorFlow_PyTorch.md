# Módulo 7: Frameworks Populares: TensorFlow y PyTorch (Conceptos Básicos)

Construir y entrenar redes neuronales desde cero usando solo NumPy sería extremadamente tedioso y propenso a errores, especialmente para redes profundas. Afortunadamente, existen **frameworks de Deep Learning** que abstraen muchos de los detalles de bajo nivel y proporcionan bloques de construcción optimizados.

Los dos frameworks más dominantes y ampliamente utilizados en la actualidad son **TensorFlow** (desarrollado por Google) y **PyTorch** (desarrollado por Meta/Facebook AI).

## ¿Qué Ofrecen estos Frameworks?

*   **Operaciones con Tensores:** Equivalente a los arrays multidimensionales de NumPy, pero con capacidades adicionales cruciales para DL. Los **tensores** son la estructura de datos fundamental.
*   **Cálculo Acelerado (GPU):** Pueden ejecutar operaciones masivamente paralelas en **GPUs** (Unidades de Procesamiento Gráfico), lo cual es esencial para entrenar redes profundas en tiempos razonables.
*   **Diferenciación Automática (Autograd):** Calculan automáticamente los **gradientes** necesarios para la retropropagación (backpropagation) y el entrenamiento del modelo. Esta es una de sus características más importantes, ya que evita tener que calcular derivadas complejas manualmente.
*   **Bloques de Construcción Predefinidos:** Ofrecen capas de red comunes (lineales/densas, convolucionales, recurrentes), funciones de activación, funciones de pérdida y optimizadores listos para usar.
*   **APIs Flexibles:** Permiten definir arquitecturas de red personalizadas.
*   **Herramientas para Despliegue:** Facilitan guardar modelos entrenados y desplegarlos en diferentes plataformas (servidores, móviles, web).
*   **Gran Comunidad y Ecosistema:** Ambos tienen comunidades muy activas, abundante documentación, tutoriales y bibliotecas complementarias.

## TensorFlow y Keras

*   **TensorFlow:** Es un framework muy potente y maduro, originalmente conocido por su enfoque de **grafos de computación estáticos** (definir el grafo primero, luego ejecutarlo). Aunque ahora también soporta ejecución "eager" (más dinámica, similar a PyTorch).
*   **Keras:** Es una **API de alto nivel** para redes neuronales, escrita en Python, que puede ejecutarse sobre diferentes backends (TensorFlow, Theano -aunque menos común ahora-, CNTK). **Keras está ahora profundamente integrado dentro de TensorFlow (`tf.keras`)** y es la forma recomendada y más fácil de empezar a construir modelos con TensorFlow. Se enfoca en la facilidad de uso y la creación rápida de prototipos.

**Conceptos Clave (tf.keras):**

*   **Modelo Secuencial (`tf.keras.models.Sequential`):** Una forma simple de construir modelos apilando capas linealmente.
*   **API Funcional:** Una forma más flexible de definir modelos complejos con múltiples entradas/salidas o ramas.
*   **Capas (`tf.keras.layers`):** Bloques de construcción como `Dense` (totalmente conectada), `Conv2D` (convolucional), `LSTM` (recurrente), `Dropout`, `BatchNormalization`, etc.
*   **Compilación (`model.compile()`):** Configura el proceso de entrenamiento especificando el **optimizador** (ej. `'adam'`, `'sgd'`), la **función de pérdida** (ej. `'binary_crossentropy'`, `'categorical_crossentropy'`, `'mse'`) y las **métricas** a monitorizar (ej. `['accuracy']`).
*   **Entrenamiento (`model.fit()`):** Entrena el modelo con los datos de entrenamiento (`X_train`, `y_train`), especificando el número de épocas (pasadas por los datos) y el tamaño del lote (batch size).
*   **Evaluación (`model.evaluate()`):** Evalúa el modelo entrenado en los datos de prueba.
*   **Predicción (`model.predict()`):** Realiza predicciones sobre nuevos datos.

**Instalación (Ejemplo Básico - CPU):**
`pip install tensorflow` o `conda install tensorflow`
*(La instalación con soporte para GPU es más compleja y requiere drivers específicos y CUDA/cuDNN).*

## PyTorch

*   **Enfoque:** PyTorch es conocido por su enfoque de **grafos de computación dinámicos** ("Define-by-Run"). El grafo se construye sobre la marcha a medida que se ejecuta el código, lo que muchos encuentran más intuitivo y "Pythonico", facilitando la depuración.
*   **Popularidad:** Ha ganado una enorme popularidad, especialmente en la comunidad de investigación, debido a su flexibilidad y facilidad de uso.
*   **API:** Su API principal es más de bajo nivel que Keras, pero muy potente. También existen bibliotecas de alto nivel construidas sobre PyTorch (como `pytorch-lightning`, `fastai`).

**Conceptos Clave:**

*   **Tensores (`torch.Tensor`):** El objeto central, similar al `ndarray` de NumPy pero con soporte para GPU y autograd.
*   **Autograd (`torch.autograd`):** El motor de diferenciación automática. Los tensores pueden rastrear su historial de operaciones (`requires_grad=True`).
*   **Módulos (`torch.nn.Module`):** Las redes y las capas se definen como clases que heredan de `nn.Module`. Deben implementar un método `forward()` que define cómo se procesa la entrada.
*   **Capas (`torch.nn`):** Contiene capas predefinidas (`Linear`, `Conv2d`, `LSTM`, etc.).
*   **Funciones de Pérdida (`torch.nn`):** `BCELoss`, `CrossEntropyLoss`, `MSELoss`, etc.
*   **Optimizadores (`torch.optim`):** `Adam`, `SGD`, `RMSprop`, etc.
*   **Bucle de Entrenamiento:** En PyTorch, típicamente escribes el bucle de entrenamiento manualmente, lo que da más control pero requiere un poco más de código que `model.fit()` de Keras:
    1.  Poner el modelo en modo entrenamiento (`model.train()`).
    2.  Iterar sobre los datos en lotes (batches).
    3.  Poner a cero los gradientes del optimizador (`optimizer.zero_grad()`).
    4.  Realizar la pasada hacia adelante (`outputs = model(inputs)`).
    5.  Calcular la pérdida (`loss = criterion(outputs, labels)`).
    6.  Realizar la retropropagación (`loss.backward()`).
    7.  Actualizar los pesos (`optimizer.step()`).

**Instalación (Visita la web oficial):**
La instalación de PyTorch se realiza preferentemente siguiendo las instrucciones de su web oficial ([https://pytorch.org/](https://pytorch.org/)), ya que te permite seleccionar tu sistema operativo, gestor de paquetes (pip/conda) y versión de CUDA (si necesitas soporte GPU) para obtener el comando de instalación correcto.

## TensorFlow/Keras vs. PyTorch

*   **Facilidad de Uso (Principiantes):** Keras (sobre TensorFlow) suele considerarse ligeramente más fácil para empezar debido a su API de alto nivel y funciones como `model.fit()`.
*   **Flexibilidad y Depuración:** PyTorch, con sus grafos dinámicos, a menudo se considera más flexible y fácil de depurar para arquitecturas complejas o investigación.
*   **Despliegue:** TensorFlow históricamente tenía una ventaja en herramientas de despliegue (TensorFlow Serving, TensorFlow Lite), aunque PyTorch ha mejorado mucho en esta área (TorchServe, PyTorch Mobile).
*   **Comunidad:** Ambos tienen comunidades enormes y activas. PyTorch ha ganado mucha tracción en investigación recientemente.

**¿Cuál elegir?** ¡Ambos son excelentes!
*   Si buscas una curva de aprendizaje más suave y prototipado rápido, **Keras/TensorFlow** puede ser una buena opción inicial.
*   Si valoras la flexibilidad, un enfoque más "Pythonico" y estás interesado en investigación, **PyTorch** es una opción muy fuerte.
*   Conocer los conceptos básicos de ambos es beneficioso.

En este curso, nos limitaremos a los conceptos. Construir y entrenar modelos requiere una configuración más detallada y tiempo computacional, pero entender qué son estos frameworks es el primer paso para adentrarse en el Deep Learning práctico.
