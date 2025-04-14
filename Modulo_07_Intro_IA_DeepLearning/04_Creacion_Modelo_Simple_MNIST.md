# Módulo 7: Creación de un Modelo Simple (Ej: Clasificación MNIST con Keras)

Para tener una idea más concreta de cómo se construye y entrena una red neuronal simple, vamos a usar TensorFlow con su API de alto nivel Keras para abordar un problema clásico: la clasificación de dígitos escritos a mano del dataset **MNIST**.

MNIST contiene 70,000 imágenes en escala de grises (28x28 píxeles) de dígitos del 0 al 9 (60,000 para entrenamiento, 10,000 para prueba). Nuestro objetivo es entrenar una red neuronal que pueda mirar una de estas imágenes y predecir qué dígito es.

**Nota:** Este ejemplo es introductorio. Entrenar modelos de Deep Learning puede requerir una configuración más compleja (especialmente para GPUs) y tiempos de entrenamiento significativos. Aquí nos centramos en la estructura del código.

**Requisitos:** Necesitarás TensorFlow instalado (`pip install tensorflow` o `conda install tensorflow`).

```python
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras # Importar Keras desde TensorFlow

# Opcional: Configurar para usar GPU si está disponible y configurada
# gpus = tf.config.experimental.list_physical_devices('GPU')
# if gpus:
#     try:
#         for gpu in gpus:
#             tf.config.experimental.set_memory_growth(gpu, True)
#         print(f"GPUs disponibles: {len(gpus)}")
#     except RuntimeError as e:
#         print(e)

print(f"TensorFlow Version: {tf.__version__}")
print(f"Keras Version: {keras.__version__}")

# 1. Cargar el Dataset MNIST
# Keras incluye funciones para cargar datasets comunes
(X_train_full, y_train_full), (X_test, y_test) = keras.datasets.mnist.load_data()

print(f"\nForma datos entrenamiento (X_train_full): {X_train_full.shape}") # (60000, 28, 28)
print(f"Forma etiquetas entrenamiento (y_train_full): {y_train_full.shape}") # (60000,)
print(f"Forma datos prueba (X_test): {X_test.shape}") # (10000, 28, 28)
print(f"Forma etiquetas prueba (y_test): {y_test.shape}") # (10000,)

# 2. Preprocesamiento Básico
# a) Escalar los píxeles: Los valores de píxeles van de 0 a 255. Es buena práctica
#    escalarlos a un rango [0, 1] dividiendo por 255.0 (usamos float).
X_train_full = X_train_full / 255.0
X_test = X_test / 255.0

# b) Crear un conjunto de validación: Separamos parte del entrenamiento original
#    para ajustar hiperparámetros o para monitorear el sobreajuste durante el entrenamiento.
#    Usaremos los primeros 5000 para validación.
X_valid, X_train = X_train_full[:5000], X_train_full[5000:]
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]

print(f"\nForma X_train: {X_train.shape}")
print(f"Forma X_valid: {X_valid.shape}")

# c) Visualizar una imagen (opcional)
plt.figure()
plt.imshow(X_train[0], cmap="binary") # Mostrar la primera imagen en blanco y negro
plt.title(f"Etiqueta: {y_train[0]}")
plt.axis("off")
plt.show()

# 3. Construir el Modelo (Red Neuronal Densa Simple)
# Usaremos un modelo secuencial (capas apiladas)

model = keras.models.Sequential([
    # Capa Flatten: Convierte cada imagen 28x28 en un vector plano de 784 píxeles (28*28).
    # Es la capa de entrada.
    keras.layers.Flatten(input_shape=[28, 28]),

    # Primera Capa Oculta Densa: 300 neuronas, función de activación ReLU.
    # 'Dense' significa que cada neurona está conectada a todas las neuronas de la capa anterior.
    keras.layers.Dense(300, activation="relu"),

    # Segunda Capa Oculta Densa: 100 neuronas, activación ReLU.
    keras.layers.Dense(100, activation="relu"),

    # Capa de Salida: 10 neuronas (una por cada dígito 0-9).
    # Función de activación 'softmax' para obtener probabilidades multiclase.
    keras.layers.Dense(10, activation="softmax")
])

# Ver un resumen del modelo
print("\nResumen del Modelo:")
model.summary()
# Nota: 'Param #' indica el número de parámetros entrenables (pesos + sesgos) en cada capa.

# 4. Compilar el Modelo
# Aquí definimos la función de pérdida, el optimizador y las métricas.
model.compile(loss="sparse_categorical_crossentropy", # Buena para clasificación multiclase con etiquetas enteras
              optimizer="sgd", # Descenso de Gradiente Estocástico (un optimizador simple)
              metrics=["accuracy"]) # Queremos monitorizar la exactitud

# 5. Entrenar el Modelo
print("\n--- Iniciando Entrenamiento ---")
# Entrenamos usando los datos de entrenamiento y validamos con el conjunto de validación.
# 'epochs' es el número de veces que el modelo verá el dataset completo.
history = model.fit(X_train, y_train, epochs=10, # Usamos pocas épocas para un ejemplo rápido
                    validation_data=(X_valid, y_valid))
print("--- Entrenamiento Finalizado ---")

# El objeto 'history' contiene información sobre el entrenamiento (pérdida y métricas por época)
# pd.DataFrame(history.history).plot(figsize=(8, 5))
# plt.grid(True)
# plt.gca().set_ylim(0, 1) # Rango del eje Y entre 0 y 1
# plt.title("Curvas de Aprendizaje")
# plt.show()

# 6. Evaluar el Modelo
# Evaluamos el rendimiento final en el conjunto de prueba (nunca visto antes)
print("\n--- Evaluando en Conjunto de Prueba ---")
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Pérdida en Test: {loss:.4f}")
print(f"Accuracy en Test: {accuracy:.4f}")

# 7. Hacer Predicciones (Opcional)
# Tomar las primeras 3 imágenes de prueba
X_new = X_test[:3]
# Obtener las probabilidades predichas para cada clase (dígito)
y_proba = model.predict(X_new)
print("\nProbabilidades predichas para las primeras 3 imágenes de prueba:")
print(np.round(y_proba, 2)) # Redondear para legibilidad

# Obtener la clase con la mayor probabilidad para cada imagen
y_pred_classes = np.argmax(y_proba, axis=1)
print(f"\nClases predichas: {y_pred_classes}")
print(f"Clases reales:    {y_test[:3]}")
```

Este ejemplo ilustra los pasos básicos para construir, compilar, entrenar y evaluar una red neuronal simple usando Keras/TensorFlow. Aunque el modelo es básico, ya puede alcanzar una buena precisión en MNIST. Para problemas más complejos (como imágenes más grandes o en color, texto, etc.), se utilizan arquitecturas más sofisticadas como las Redes Neuronales Convolucionales (CNNs) o Transformers.
