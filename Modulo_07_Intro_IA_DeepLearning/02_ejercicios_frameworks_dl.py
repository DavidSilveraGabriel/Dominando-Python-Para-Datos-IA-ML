# Ejercicios: Módulo 7 - Frameworks de Deep Learning (TensorFlow y PyTorch)

# --- Prerrequisitos ---
# No se requiere código ejecutable específico para este archivo.
# La instalación de TensorFlow o PyTorch es un proceso más complejo
# y se sale del alcance de estos ejercicios introductorios.
# (Ej. pip install tensorflow o pip install torch torchvision torchaudio)

print("--- Conceptos de Frameworks de Deep Learning ---")

# --- Ejercicio 1: Propósito de los Frameworks ---
# Instrucciones:
# Responde brevemente (en comentarios) a la siguiente pregunta:
# ¿Por qué son necesarios frameworks como TensorFlow y PyTorch para Deep Learning,
# en lugar de implementar todo desde cero con NumPy?

# Respuesta:
# Implementar redes neuronales profundas desde cero con NumPy es posible pero muy complejo y propenso a errores.
# Los frameworks como TensorFlow y PyTorch ofrecen:
# 1. Diferenciación Automática (Autograd): Calculan automáticamente los gradientes necesarios para la retropropagación (backpropagation), lo cual es fundamental para entrenar redes profundas y muy tedioso de hacer manualmente.
# 2. Optimización para Hardware: Incluyen operaciones optimizadas para ejecutarse eficientemente en CPUs y, crucialmente, en GPUs (Unidades de Procesamiento Gráfico), lo que acelera enormemente el entrenamiento de modelos grandes.
# 3. Abstracciones de Alto Nivel: Proporcionan bloques de construcción predefinidos (capas, funciones de pérdida, optimizadores) que simplifican enormemente la definición y el entrenamiento de modelos complejos.
# 4. Ecosistema y Comunidad: Ofrecen modelos pre-entrenados, herramientas de visualización (TensorBoard), utilidades para carga de datos, y cuentan con grandes comunidades que proporcionan soporte y desarrollan extensiones.

print("Ejercicio 1: Propósito de los Frameworks - Ver comentarios.")
print("-" * 20)


# --- Ejercicio 2: TensorFlow vs. PyTorch (Características Clave) ---
# Instrucciones:
# Basándote en la lección, menciona una o dos características distintivas o enfoques diferentes entre TensorFlow y PyTorch en los siguientes aspectos:

# a) Definición del Grafo Computacional:
#    - TensorFlow (históricamente, TF 1.x): Grafos estáticos (Define and Run). Se definía toda la estructura de la red primero y luego se ejecutaba en una sesión. TF 2.x adoptó la ejecución "eager" (similar a PyTorch) por defecto, haciendo los grafos más dinámicos (Define by Run).
#    - PyTorch: Grafos dinámicos (Define by Run). La estructura del grafo se define sobre la marcha a medida que se ejecutan las operaciones, lo que a menudo se considera más "pythónico" y fácil de depurar.

# b) API y Curva de Aprendizaje:
#    - TensorFlow: Ofrece múltiples niveles de API (Keras como API de alto nivel integrada en TF 2.x, APIs de nivel inferior para más control). Keras facilita mucho la entrada.
#    - PyTorch: Su API principal se considera a menudo más cercana a Python/NumPy, lo que puede resultar más intuitivo para quienes vienen de ese ecosistema. La curva de aprendizaje puede ser más suave inicialmente para algunos.

# c) Despliegue y Producción:
#    - TensorFlow: Tradicionalmente considerado más fuerte en despliegue en producción y móvil gracias a herramientas como TensorFlow Serving, TensorFlow Lite y TensorFlow.js.
#    - PyTorch: Ha mejorado mucho en este aspecto con TorchServe y soporte para ONNX, cerrando la brecha significativamente.

# d) Comunidad y Ecosistema:
#    - TensorFlow: Respaldado fuertemente por Google, gran comunidad, excelente documentación y herramientas como TensorBoard.
#    - PyTorch: Impulsado por Meta (Facebook), muy popular en la comunidad de investigación académica, crecimiento muy rápido, buena documentación.

print("\nEjercicio 2: TensorFlow vs. PyTorch - Ver comentarios.")
print("-" * 20)


# --- Ejercicio 3: ¿Qué es Keras? ---
# Instrucciones:
# Explica brevemente (en comentarios) qué es Keras y cómo se relaciona con TensorFlow.

# Respuesta:
# Keras es una API de alto nivel para construir y entrenar redes neuronales. Se enfoca en la facilidad de uso, la creación rápida de prototipos y la legibilidad del código.
# Originalmente era una biblioteca independiente que podía usar diferentes backends (como TensorFlow, Theano, CNTK).
# Desde TensorFlow 2.x, Keras está *profundamente integrada* dentro de TensorFlow (`tf.keras`) y es la API recomendada de alto nivel para la mayoría de los usuarios de TensorFlow. Permite definir modelos complejos de forma modular y sencilla.

print("\nEjercicio 3: ¿Qué es Keras? - Ver comentarios.")
print("-" * 20)


# --- Ejercicio 4: Ejemplo Conceptual de Importación ---
# Instrucciones:
# Escribe las líneas de código Python que usarías típicamente para importar:
# a) TensorFlow (y su módulo Keras integrado)
# b) PyTorch

# Nota: Este código no se ejecutará a menos que tengas las bibliotecas instaladas.

print("\n--- Ejercicio 4: Ejemplo Conceptual de Importación ---")

# a) Importar TensorFlow y Keras
print("# Importar TensorFlow y Keras")
print("import tensorflow as tf")
print("from tensorflow import keras")
print("# O a menudo se accede a Keras directamente vía tf.keras")
print("# from tensorflow.keras.layers import Dense")
print("# from tensorflow.keras.models import Sequential")

# b) Importar PyTorch
print("\n# Importar PyTorch")
print("import torch")
print("import torch.nn as nn")
print("import torch.optim as optim")

print("\nRecordatorio: La instalación y uso real de estos frameworks")
print("requiere pasos adicionales y configuración del entorno.")
print("-" * 20)

# --- Fin de los ejercicios ---
