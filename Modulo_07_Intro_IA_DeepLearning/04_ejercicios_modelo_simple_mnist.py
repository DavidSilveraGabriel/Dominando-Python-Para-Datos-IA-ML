# Ejercicios: Módulo 7 - Creación de un Modelo Simple (MNIST)

# --- Prerrequisitos ---
# Se requiere TensorFlow y Matplotlib.
# pip install tensorflow matplotlib numpy
# o (si usas conda y quieres GPU, consulta la documentación de TF)
# conda install tensorflow matplotlib numpy

# Nota: La descarga del dataset MNIST y el entrenamiento pueden tardar.
# Asegúrate de tener conexión a internet la primera vez.

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten # Flatten para aplanar imágenes
from tensorflow.keras.utils import to_categorical # Para one-hot encoding
import matplotlib.pyplot as plt
import numpy as np

print("--- Cargando y Preparando el Dataset MNIST ---")

# --- Ejercicio 1: Cargar y Explorar MNIST ---
# Instrucciones:
# 1. Carga el dataset MNIST usando `mnist.load_data()`. Esto devuelve dos tuplas: (x_train, y_train), (x_test, y_test).
# 2. Imprime las formas (shapes) de `x_train`, `y_train`, `x_test`, `y_test`.
# 3. Muestra algunas imágenes del dataset de entrenamiento usando `plt.imshow()`. Muestra 5 imágenes en una fila, junto con sus etiquetas correspondientes (`y_train`).

# Escribe tu código aquí
# 1. Cargar datos
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 2. Imprimir formas
print(f"Forma x_train: {x_train.shape}") # (60000, 28, 28) - 60k imágenes de 28x28 píxeles
print(f"Forma y_train: {y_train.shape}") # (60000,) - Etiquetas (0 a 9)
print(f"Forma x_test: {x_test.shape}")   # (10000, 28, 28)
print(f"Forma y_test: {y_test.shape}")   # (10000,)

# 3. Mostrar imágenes de ejemplo
print("\nMostrando 5 imágenes de ejemplo del dataset de entrenamiento:")
plt.figure(figsize=(10, 3))
for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(x_train[i], cmap='gray') # Mostrar en escala de grises
    plt.title(f"Etiqueta: {y_train[i]}")
    plt.axis('off') # No mostrar ejes
plt.tight_layout()
plt.show()
print("-" * 20)


# --- Ejercicio 2: Preprocesamiento de Datos ---
# Instrucciones:
# 1. Remodela (`reshape`) las imágenes de entrada (`x_train`, `x_test`) de (N, 28, 28) a (N, 784). Esto las "aplana" en un vector largo para una red neuronal densa simple.
#    - Alternativamente, podrías usar una capa `Flatten(input_shape=(28, 28))` como primera capa del modelo. Haremos el reshape manual aquí.
# 2. Convierte el tipo de datos de las imágenes a `float32`.
# 3. Normaliza los valores de los píxeles dividiéndolos por 255.0 para que estén en el rango [0, 1].
# 4. Convierte las etiquetas (`y_train`, `y_test`) a formato categórico "one-hot" usando `to_categorical()`. Especifica `num_classes=10`.
# 5. Imprime la forma de `x_train` y `y_train` después del preprocesamiento. Imprime el primer vector de etiqueta one-hot (`y_train[0]`).

print("\n--- Ejercicio 2: Preprocesamiento de Datos ---")
# Escribe tu código aquí
# 1. Remodelar imágenes
x_train_flat = x_train.reshape(60000, 784)
x_test_flat = x_test.reshape(10000, 784)
print(f"Forma x_train aplanado: {x_train_flat.shape}")

# 2. Convertir a float32
x_train_flat = x_train_flat.astype('float32')
x_test_flat = x_test_flat.astype('float32')

# 3. Normalizar píxeles
x_train_norm = x_train_flat / 255.0
x_test_norm = x_test_flat / 255.0
print(f"Valor máximo después de normalizar (ej. x_train): {x_train_norm.max()}")

# 4. Codificar etiquetas (One-Hot)
num_classes = 10
y_train_cat = to_categorical(y_train, num_classes)
y_test_cat = to_categorical(y_test, num_classes)

# 5. Imprimir formas y ejemplo de etiqueta
print(f"\nForma x_train final: {x_train_norm.shape}")
print(f"Forma y_train final: {y_train_cat.shape}")
print(f"Ejemplo etiqueta y_train[0] original: {y_train[0]}")
print(f"Ejemplo etiqueta y_train[0] one-hot: {y_train_cat[0]}")
print("-" * 20)


# --- Ejercicio 3: Construir el Modelo Secuencial ---
# Instrucciones:
# 1. Crea un modelo `Sequential` de Keras.
# 2. Añade la primera capa: una capa `Dense` con 128 neuronas, función de activación 'relu', y especifica `input_shape=(784,)` (ya que las imágenes están aplanadas).
# 3. Añade una segunda capa `Dense` con 64 neuronas y activación 'relu'.
# 4. Añade la capa de salida: una capa `Dense` con `num_classes` (10) neuronas y función de activación 'softmax' (adecuada para clasificación multiclase).
# 5. Imprime el resumen del modelo usando `model.summary()`.

print("\n--- Ejercicio 3: Construir el Modelo Secuencial ---")
# Escribe tu código aquí
# 1. Crear modelo secuencial
model = Sequential(name="MLP_Simple_MNIST")

# 2. Añadir primera capa densa
model.add(Dense(128, activation='relu', input_shape=(784,), name='Capa_Oculta_1'))

# 3. Añadir segunda capa densa
model.add(Dense(64, activation='relu', name='Capa_Oculta_2'))

# 4. Añadir capa de salida
model.add(Dense(num_classes, activation='softmax', name='Capa_Salida'))

# 5. Imprimir resumen
model.summary()
print("-" * 20)


# --- Ejercicio 4: Compilar el Modelo ---
# Instrucciones:
# 1. Compila el modelo usando `model.compile()`.
# 2. Especifica los siguientes parámetros:
#    - `loss`: 'categorical_crossentropy' (adecuada para clasificación multiclase con etiquetas one-hot).
#    - `optimizer`: 'adam' (un optimizador popular y eficiente).
#    - `metrics`: ['accuracy'] (para monitorear la exactitud durante el entrenamiento).
# 3. Imprime un mensaje indicando que el modelo ha sido compilado.

print("\n--- Ejercicio 4: Compilar el Modelo ---")
# Escribe tu código aquí
# 1, 2. Compilar
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# 3. Imprimir mensaje
print("Modelo compilado exitosamente.")
print("-" * 20)


# --- Ejercicio 5: Entrenar el Modelo (Conceptual / Opcional Ejecutar) ---
# Instrucciones:
# 1. Llama a `model.fit()` para entrenar el modelo.
# 2. Pasa los datos de entrenamiento preprocesados (`x_train_norm`, `y_train_cat`).
# 3. Especifica un tamaño de batch (`batch_size=128`).
# 4. Especifica el número de épocas (`epochs=5`). Una época es una pasada completa por todo el dataset de entrenamiento.
# 5. Incluye datos de validación para monitorear el rendimiento en datos no vistos durante el entrenamiento: `validation_split=0.1` (usa el 10% de los datos de entrenamiento para validación) o `validation_data=(x_test_norm, y_test_cat)`. Usemos `validation_split`.
# 6. Guarda el historial del entrenamiento en una variable `history`.
# 7. **Importante:** El entrenamiento puede tardar varios minutos dependiendo de tu hardware. Puedes comentar esta sección si no deseas ejecutarla ahora. Si la ejecutas, observa cómo cambian la pérdida (loss) y la exactitud (accuracy) en cada época.

print("\n--- Ejercicio 5: Entrenar el Modelo ---")
print("NOTA: El entrenamiento puede tardar unos minutos...")
# Escribe tu código aquí (puedes comentar las siguientes líneas si no quieres entrenar)

# history = model.fit(x_train_norm, y_train_cat,
#                     batch_size=128,
#                     epochs=5,
#                     validation_split=0.1, # Usa 10% de train para validar
#                     verbose=1) # Muestra barra de progreso

# print("\nEntrenamiento completado (si se ejecutó).")
print("Paso de entrenamiento omitido/comentado en este script de ejercicio.")
print("Descomenta las líneas de 'history = model.fit(...)' si deseas entrenar.")
print("-" * 20)


# --- Ejercicio 6: Evaluar el Modelo (Conceptual / Opcional Ejecutar) ---
# Instrucciones:
# 1. Llama a `model.evaluate()` para evaluar el rendimiento del modelo entrenado en el conjunto de prueba **preprocesado** (`x_test_norm`, `y_test_cat`).
# 2. Guarda los resultados (pérdida y exactitud en el test set) en variables `score`.
# 3. Imprime la pérdida (Test loss) y la exactitud (Test accuracy).
# 4. **Importante:** Solo ejecuta esta sección si ejecutaste el entrenamiento en el Ejercicio 5.

print("\n--- Ejercicio 6: Evaluar el Modelo ---")
# Escribe tu código aquí (puedes comentar si no entrenaste)

# score = model.evaluate(x_test_norm, y_test_cat, verbose=0)
# print(f"Pérdida en el Test set (Test loss): {score[0]:.4f}")
# print(f"Exactitud en el Test set (Test accuracy): {score[1]:.4f}")

print("Paso de evaluación omitido/comentado.")
print("Descomenta las líneas de 'score = model.evaluate(...)' si entrenaste el modelo.")
print("-" * 20)


# --- Ejercicio 7: Hacer Predicciones (Conceptual / Opcional Ejecutar) ---
# Instrucciones:
# 1. Usa `model.predict()` para obtener las probabilidades predichas para las primeras 5 imágenes del conjunto de prueba (`x_test_norm[:5]`).
# 2. Imprime la forma del array de predicciones. Debería ser (5, 10).
# 3. Para cada una de las 5 predicciones, encuentra la clase predicha (el índice con la probabilidad más alta) usando `np.argmax()`.
# 4. Imprime la clase predicha y la clase real (`y_test[:5]`) para esas 5 imágenes.
# 5. **Importante:** Solo ejecuta esta sección si ejecutaste el entrenamiento en el Ejercicio 5.

print("\n--- Ejercicio 7: Hacer Predicciones ---")
# Escribe tu código aquí (puedes comentar si no entrenaste)

# predictions = model.predict(x_test_norm[:5])
# print(f"Forma de las predicciones (probabilidades): {predictions.shape}")
# predicted_classes = np.argmax(predictions, axis=1)
# print(f"\nClases Predichas (primeras 5): {predicted_classes}")
# print(f"Clases Reales (primeras 5):    {y_test[:5]}")

# # Visualizar las imágenes y sus predicciones
# plt.figure(figsize=(10, 4))
# for i in range(5):
#     plt.subplot(1, 5, i + 1)
#     plt.imshow(x_test[i], cmap='gray') # Imagen original sin aplanar
#     plt.title(f"Pred: {predicted_classes[i]}\nReal: {y_test[i]}")
#     plt.axis('off')
# plt.tight_layout()
# plt.show()

print("Paso de predicción omitido/comentado.")
print("Descomenta las líneas si entrenaste el modelo.")
print("-" * 20)


# --- Fin de los ejercicios ---
