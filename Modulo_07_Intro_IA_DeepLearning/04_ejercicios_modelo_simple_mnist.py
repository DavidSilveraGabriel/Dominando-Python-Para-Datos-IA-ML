# Ejercicios: Módulo 7 - Creación de un Modelo Simple con PyTorch (MNIST)

# --- Prerrequisitos ---
# Se requiere PyTorch, Torchvision y Matplotlib.
# pip install torch torchvision matplotlib numpy
# o (si usas conda)
# conda install pytorch torchvision matplotlib numpy -c pytorch

# Nota: La descarga del dataset MNIST y el entrenamiento pueden tardar.
# Asegúrate de tener conexión a internet la primera vez.

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import numpy as np

print("--- Cargando y Preparando el Dataset MNIST con PyTorch ---")

# --- Configuración del Dispositivo ---
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Usando dispositivo: {device}")

# --- Ejercicio 1: Cargar y Explorar MNIST ---
# Instrucciones:
# 1. Define las transformaciones para el dataset: convertir a Tensor y normalizar.
#    - La normalización para MNIST suele ser con media 0.1307 y desviación estándar 0.3081.
# 2. Carga los datasets de entrenamiento y prueba usando `datasets.MNIST`. Aplica las transformaciones.
# 3. Crea DataLoaders para los datasets de entrenamiento y prueba. Usa un `batch_size` de 64.
# 4. Obtén un batch de datos del DataLoader de entrenamiento.
# 5. Imprime las formas (shapes) de las imágenes y etiquetas del batch.
# 6. Muestra algunas imágenes del batch usando `plt.imshow()`. Muestra 5 imágenes en una fila, junto con sus etiquetas correspondientes.

# Escribe tu código aquí
# 1. Definir transformaciones
transform = transforms.Compose([
    transforms.ToTensor(), # Convierte la imagen PIL a Tensor (rango [0, 1])
    transforms.Normalize((0.1307,), (0.3081,)) # Normaliza con media y std de MNIST
])

# 2. Cargar datasets
train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)

# 3. Crear DataLoaders
batch_size = 64
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

# 4. Obtener un batch
dataiter = iter(train_loader)
images, labels = next(dataiter) # Obtener el primer batch

# 5. Imprimir formas
print(f"\nForma del batch de imágenes: {images.shape}") # [batch_size, canales, altura, ancho] -> [64, 1, 28, 28]
print(f"Forma del batch de etiquetas: {labels.shape}") # [batch_size] -> [64]

# 6. Mostrar imágenes de ejemplo
print("\nMostrando 5 imágenes de ejemplo del primer batch:")
plt.figure(figsize=(10, 3))
for i in range(5):
    plt.subplot(1, 5, i + 1)
    # PyTorch usa [C, H, W], Matplotlib espera [H, W, C] o [H, W]
    # Quitamos la dimensión del canal (que es 1) y desnormalizamos (aproximado) para visualizar
    img_display = images[i].squeeze().numpy() * 0.3081 + 0.1307
    plt.imshow(img_display, cmap='gray')
    plt.title(f"Etiqueta: {labels[i].item()}") # .item() para obtener el valor escalar del tensor
    plt.axis('off')
plt.tight_layout()
plt.show()
print("-" * 20)


# --- Ejercicio 2: Preprocesamiento de Datos (Realizado en Ejercicio 1) ---
# Instrucciones:
# En PyTorch, el preprocesamiento como la normalización y conversión a Tensor se maneja
# comúnmente a través de `transforms` al cargar los datos. El aplanamiento
# (reshape de [N, 1, 28, 28] a [N, 784]) se hará dentro del modelo con `nn.Flatten`.
# Las etiquetas en PyTorch para `nn.CrossEntropyLoss` deben ser índices de clase (0, 1, ..., 9),
# no vectores one-hot. El DataLoader ya proporciona las etiquetas en este formato.

print("\n--- Ejercicio 2: Preprocesamiento de Datos ---")
print("El preprocesamiento principal (ToTensor, Normalize) se aplicó con transforms.")
print("El aplanamiento se hará en el modelo.")
print("Las etiquetas ya están en el formato correcto (índices de clase).")
print(f"Ejemplo primera etiqueta del batch: {labels[0].item()}")
print("-" * 20)


# --- Ejercicio 3: Construir el Modelo (Red Neuronal Simple - MLP) ---
# Instrucciones:
# 1. Define una clase `MLP` que herede de `nn.Module`.
# 2. En el constructor (`__init__`):
#    - Llama al constructor de la clase padre (`super().__init__()`).
#    - Define una capa `nn.Flatten()` para aplanar la imagen de entrada.
#    - Define una secuencia `nn.Sequential` que contenga:
#      - Una capa lineal (`nn.Linear`) de 784 (28*28) a 128 neuronas.
#      - Una función de activación `nn.ReLU()`.
#      - Una segunda capa lineal de 128 a 64 neuronas.
#      - Otra `nn.ReLU()`.
#      - La capa de salida lineal de 64 a 10 neuronas (una por clase).
# 3. En el método `forward(self, x)`:
#    - Pasa la entrada `x` a través de la capa flatten.
#    - Pasa el resultado a través de la secuencia lineal.
#    - Devuelve el resultado (logits).
# 4. Crea una instancia del modelo `MLP`.
# 5. Mueve el modelo al dispositivo configurado (`.to(device)`).
# 6. Imprime la estructura del modelo.

print("\n--- Ejercicio 3: Construir el Modelo (MLP) ---")
# Escribe tu código aquí
# 1, 2, 3. Definir la clase del modelo
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten() # Capa para aplanar [N, 1, 28, 28] a [N, 784]
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 128), # Capa Oculta 1
            nn.ReLU(),
            nn.Linear(128, 64),    # Capa Oculta 2
            nn.ReLU(),
            nn.Linear(64, 10)      # Capa Salida (logits)
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

# 4. Crear instancia del modelo
model = MLP()

# 5. Mover al dispositivo
model.to(device)

# 6. Imprimir estructura
print(model)
print("-" * 20)


# --- Ejercicio 4: Definir Pérdida y Optimizador ---
# Instrucciones:
# 1. Define la función de pérdida (loss function). Usa `nn.CrossEntropyLoss`.
#    Esta función combina `nn.LogSoftmax` y `nn.NLLLoss`, por lo que es adecuada para
#    clasificación multiclase y espera logits como entrada del modelo.
# 2. Define el optimizador. Usa `optim.Adam`. Pasa los parámetros del modelo (`model.parameters()`)
#    y una tasa de aprendizaje (`lr=1e-3` es un buen punto de partida).
# 3. Imprime los nombres de la función de pérdida y el optimizador definidos.

print("\n--- Ejercicio 4: Definir Pérdida y Optimizador ---")
# Escribe tu código aquí
# 1. Definir función de pérdida
loss_fn = nn.CrossEntropyLoss()

# 2. Definir optimizador
optimizer = optim.Adam(model.parameters(), lr=1e-3)

# 3. Imprimir información
print(f"Función de Pérdida: {loss_fn}")
print(f"Optimizador: {optimizer}")
print("-" * 20)


# --- Ejercicio 5: Entrenar el Modelo (Conceptual / Opcional Ejecutar) ---
# Instrucciones:
# 1. Define una función `train_loop(dataloader, model, loss_fn, optimizer, device)`.
# 2. Dentro de la función:
#    - Pon el modelo en modo entrenamiento (`model.train()`).
#    - Itera sobre los batches del `dataloader`.
#    - Mueve las imágenes (`X`) y etiquetas (`y`) al `device`.
#    - Realiza la pasada hacia adelante (forward pass): `pred = model(X)`.
#    - Calcula la pérdida: `loss = loss_fn(pred, y)`.
#    - Realiza la pasada hacia atrás (backpropagation):
#      - `optimizer.zero_grad()` (limpia gradientes anteriores).
#      - `loss.backward()` (calcula gradientes).
#      - `optimizer.step()` (actualiza pesos).
#    - (Opcional) Imprime la pérdida cada cierto número de batches.
# 3. Define una función `test_loop(dataloader, model, loss_fn, device)`.
# 4. Dentro de la función:
#    - Pon el modelo en modo evaluación (`model.eval()`).
#    - Desactiva el cálculo de gradientes (`with torch.no_grad():`).
#    - Itera sobre los batches del `dataloader`.
#    - Mueve las imágenes (`X`) y etiquetas (`y`) al `device`.
#    - Calcula las predicciones y la pérdida.
#    - Acumula la pérdida total y el número de predicciones correctas.
#    - Calcula la exactitud promedio y la pérdida promedio.
#    - Imprime la exactitud y la pérdida en el conjunto de prueba.
# 5. Define el número de épocas (`epochs = 5`).
# 6. Crea un bucle que itere por el número de épocas.
# 7. Dentro del bucle, llama a `train_loop` y `test_loop`.
# 8. **Importante:** El entrenamiento puede tardar. Comenta las llamadas a las funciones si no deseas ejecutarlo.

print("\n--- Ejercicio 5: Entrenar el Modelo ---")

def train_loop(dataloader, model, loss_fn, optimizer, device):
    size = len(dataloader.dataset)
    model.train() # Poner el modelo en modo entrenamiento
    for batch, (X, y) in enumerate(dataloader):
        # Mover datos al dispositivo
        X, y = X.to(device), y.to(device)

        # Calcular predicción y pérdida
        pred = model(X)
        loss = loss_fn(pred, y)

        # Backpropagation
        optimizer.zero_grad() # Limpiar gradientes
        loss.backward()       # Calcular gradientes
        optimizer.step()      # Actualizar pesos

        if batch % 100 == 0: # Imprimir progreso cada 100 batches
            loss_val, current = loss.item(), batch * len(X)
            print(f"  loss: {loss_val:>7f}  [{current:>5d}/{size:>5d}]")

def test_loop(dataloader, model, loss_fn, device):
    model.eval() # Poner el modelo en modo evaluación
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    test_loss, correct = 0, 0

    with torch.no_grad(): # Desactivar cálculo de gradientes
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            # Obtener la clase predicha (índice del valor máximo en los logits)
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()

    test_loss /= num_batches
    correct /= size
    print(f"Test Error: \n  Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")

# --- Bucle de Entrenamiento (Comentado por defecto) ---
# epochs = 5
# print("NOTA: El entrenamiento puede tardar unos minutos...")
# for t in range(epochs):
#     print(f"Epoch {t+1}\n-------------------------------")
#     train_loop(train_loader, model, loss_fn, optimizer, device)
#     test_loop(test_loader, model, loss_fn, device)
# print("Entrenamiento completado (si se ejecutó).")

print("Paso de entrenamiento omitido/comentado en este script de ejercicio.")
print("Descomenta el bucle de épocas si deseas entrenar.")
print("-" * 20)


# --- Ejercicio 6: Evaluar el Modelo (Realizado en Ejercicio 5) ---
# Instrucciones:
# La evaluación en el conjunto de prueba se realiza dentro del bucle de entrenamiento
# mediante la función `test_loop` al final de cada época.

print("\n--- Ejercicio 6: Evaluar el Modelo ---")
print("La evaluación se realiza en la función test_loop (ver Ejercicio 5).")
print("Descomenta el bucle de entrenamiento para ver los resultados de evaluación.")
print("-" * 20)


# --- Ejercicio 7: Hacer Predicciones (Conceptual / Opcional Ejecutar) ---
# Instrucciones:
# 1. Pon el modelo en modo evaluación (`model.eval()`).
# 2. Obtén un batch de datos del `test_loader`.
# 3. Mueve las imágenes del batch al `device`.
# 4. Desactiva el cálculo de gradientes (`with torch.no_grad():`).
# 5. Pasa las imágenes por el modelo para obtener los logits (`pred = model(images)`).
# 6. Obtén las clases predichas encontrando el índice del logit máximo (`predicted_classes = pred.argmax(1)`).
# 7. Mueve las predicciones y las imágenes de vuelta a la CPU (`.cpu()`) si es necesario para visualizarlas.
# 8. Muestra las primeras 5 imágenes del batch junto con su clase predicha y su clase real.
# 9. **Importante:** Solo ejecuta esta sección si entrenaste el modelo en el Ejercicio 5.

print("\n--- Ejercicio 7: Hacer Predicciones ---")
# Escribe tu código aquí (puedes comentar si no entrenaste)

# model.eval()
# test_iter = iter(test_loader)
# images_test, labels_test = next(test_iter)
# images_test_dev = images_test.to(device) # Mover a GPU/CPU

# with torch.no_grad():
#     pred_logits = model(images_test_dev)
#     predicted_classes = pred_logits.argmax(1).cpu() # Mover predicciones a CPU

# # Mover imágenes originales a CPU para matplotlib
# images_display = images_test.cpu()
# labels_display = labels_test.cpu()

# print(f"Clases Predichas (primeras 5): {predicted_classes[:5].numpy()}")
# print(f"Clases Reales (primeras 5):    {labels_display[:5].numpy()}")

# # Visualizar las imágenes y sus predicciones
# plt.figure(figsize=(10, 4))
# for i in range(5):
#     plt.subplot(1, 5, i + 1)
#     img_disp = images_display[i].squeeze().numpy() * 0.3081 + 0.1307 # Desnormalizar aprox.
#     plt.imshow(img_disp, cmap='gray')
#     plt.title(f"Pred: {predicted_classes[i].item()}\nReal: {labels_display[i].item()}")
#     plt.axis('off')
# plt.tight_layout()
# plt.show()

print("Paso de predicción omitido/comentado.")
print("Descomenta las líneas si entrenaste el modelo.")
print("-" * 20)


# --- Fin de los ejercicios ---
