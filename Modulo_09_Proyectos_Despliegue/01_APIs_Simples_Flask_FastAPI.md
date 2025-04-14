# Módulo 9: Creación de APIs Simples con Flask/FastAPI

Una vez que has entrenado un modelo de Machine Learning o has desarrollado un análisis de datos, a menudo quieres hacerlo accesible para otras aplicaciones o usuarios a través de la web. Una forma común de lograr esto es creando una **API (Interfaz de Programación de Aplicaciones)** web.

Una API web define un conjunto de **endpoints** (URLs) a los que un cliente (como una aplicación web frontend, una aplicación móvil u otro servicio) puede enviar **peticiones (requests)** (normalmente HTTP) para obtener datos o realizar acciones, y la API devuelve una **respuesta (response)** (normalmente en formato JSON).

Dos frameworks muy populares en Python para construir APIs web de forma rápida y sencilla son **Flask** y **FastAPI**.

## Flask

*   **¿Qué es?** Un **microframework** web para Python. "Micro" no significa que le falten funcionalidades, sino que su núcleo es simple y extensible. No impone una estructura de proyecto rígida ni incluye herramientas como ORM (Mapeo Objeto-Relacional) o validación de formularios por defecto, permitiéndote elegir las bibliotecas que prefieras.
*   **Ventajas:** Muy fácil de aprender, flexible, gran cantidad de extensiones disponibles, maduro y con una gran comunidad. Ideal para APIs pequeñas/medianas o prototipos rápidos.
*   **Instalación:** `pip install Flask` o `conda install flask`

**Ejemplo Básico de API con Flask:**

```python
# app_flask.py
from flask import Flask, request, jsonify
import joblib # Para cargar un modelo pre-entrenado (ejemplo)
import numpy as np

# 1. Crear la aplicación Flask
app = Flask(__name__)

# 2. Cargar un modelo (simulado - reemplaza con tu modelo real)
# model = joblib.load('mi_modelo_entrenado.pkl')
# scaler = joblib.load('mi_scaler.pkl') # Si usaste escalado
print("Simulando carga de modelo...")
def simular_prediccion(features):
    # Lógica de predicción simulada (ej. basado en la suma)
    if sum(features) > 10:
        return 1 #"Positivo"
    else:
        return 0 #"Negativo"
model = simular_prediccion

# 3. Definir un endpoint (ruta) y la función que lo maneja
@app.route('/predict', methods=['POST']) # Ruta /predict, acepta peticiones POST
def predict():
    """Recibe datos JSON, hace una predicción y devuelve el resultado."""
    try:
        # Obtener datos JSON de la petición
        data = request.get_json()
        if data is None:
            return jsonify({"error": "No se recibieron datos JSON."}), 400

        # Extraer características (asumiendo una lista o array en la key 'features')
        features = data.get('features')
        if features is None or not isinstance(features, list):
             return jsonify({"error": "Falta la clave 'features' o no es una lista."}), 400

        # Convertir a array NumPy y validar (ej. número de features)
        try:
            features_np = np.array(features).reshape(1, -1) # Asumir una sola muestra
            # Aquí iría el preprocesamiento si es necesario (ej. scaler.transform(features_np))
            # scaled_features = scaler.transform(features_np)
            scaled_features = features_np # Simulación sin escalado real
        except Exception as e:
             return jsonify({"error": f"Error al procesar features: {e}"}), 400

        # Realizar la predicción
        prediction = model(scaled_features[0]) # Llama a nuestra función simulada

        # Devolver la predicción como JSON
        return jsonify({'prediction': prediction})

    except Exception as e:
        # Manejo genérico de errores
        return jsonify({"error": f"Error interno del servidor: {e}"}), 500

# 4. Ejecutar la aplicación (para desarrollo)
if __name__ == '__main__':
    # debug=True activa el modo de depuración (recarga automática, más info de errores)
    # ¡NO USAR debug=True en producción!
    app.run(debug=True, port=5000) # Ejecuta en http://127.0.0.1:5000/
```

**Para probar esta API (una vez ejecutada):**
Puedes usar herramientas como `curl`, Postman, Insomnia, o incluso un script de Python con la biblioteca `requests`:

```python
# test_api.py
import requests
import json

url = 'http://127.0.0.1:5000/predict' # Asegúrate que la app Flask esté corriendo

# Datos de ejemplo a enviar (deben coincidir con lo que espera el modelo)
data_to_send = {'features': [5.1, 3.5, 1.4, 0.2]} # Ejemplo tipo Iris

headers = {'Content-Type': 'application/json'}

try:
    response = requests.post(url, headers=headers, data=json.dumps(data_to_send))
    response.raise_for_status() # Lanza error si la respuesta no es 2xx

    result = response.json()
    print(f"Petición enviada: {data_to_send}")
    print(f"Predicción recibida: {result}")

except requests.exceptions.RequestException as e:
    print(f"Error en la petición: {e}")
except json.JSONDecodeError:
    print(f"Error decodificando JSON. Respuesta recibida: {response.text}")

```

## FastAPI

*   **¿Qué es?** Un framework web moderno de alto rendimiento para construir APIs con Python 3.7+, basado en las type hints estándar de Python.
*   **Ventajas:**
    *   **Muy Rápido:** Comparable en rendimiento a NodeJS y Go, gracias a Starlette (framework ASGI) y Pydantic.
    *   **Fácil y Rápido de Codificar:** Diseñado para minimizar el código necesario.
    *   **Menos Errores:** Usa type hints para validación automática de datos de entrada/salida (con Pydantic) y excelente soporte de editores.
    *   **Documentación Automática:** Genera automáticamente documentación interactiva de la API (Swagger UI y ReDoc) basada en tu código y type hints.
    *   **Basado en Estándares:** Usa OpenAPI (antes Swagger) y JSON Schema.
    *   **Soporte Asíncrono:** Construido sobre ASGI, soporta `async`/`await` de forma nativa para operaciones concurrentes.
*   **Instalación:** `pip install fastapi "uvicorn[standard]"` (Uvicorn es un servidor ASGI rápido).

**Ejemplo Básico de API con FastAPI:**

```python
# app_fastapi.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field # Para validación de datos
import joblib
import numpy as np
from typing import List # Para type hints

# 1. Crear la aplicación FastAPI
app = FastAPI(title="API de Predicción Simple", version="1.0")

# 2. Definir el modelo de datos de entrada usando Pydantic
# Esto valida automáticamente los datos recibidos en la petición
class InputFeatures(BaseModel):
    features: List[float] = Field(..., example=[5.1, 3.5, 1.4, 0.2]) # '...' indica campo requerido

# 3. Definir el modelo de datos de salida (opcional pero bueno para docs)
class PredictionOut(BaseModel):
    prediction: int # O str si predices texto

# 4. Cargar modelo (simulado)
# model = joblib.load('mi_modelo_entrenado.pkl')
# scaler = joblib.load('mi_scaler.pkl')
print("Simulando carga de modelo...")
def simular_prediccion(features):
    if sum(features) > 10: return 1
    else: return 0
model = simular_prediccion

# 5. Definir el endpoint con type hints
# FastAPI usa las hints para validación y documentación
@app.post("/predict", response_model=PredictionOut) # Define el modelo de respuesta
async def predict(input_data: InputFeatures): # Usa el modelo Pydantic como type hint
    """
    Recibe características de entrada y devuelve una predicción (0 o 1).
    """
    try:
        # Los datos ya están validados por Pydantic gracias al type hint
        features_np = np.array(input_data.features).reshape(1, -1)

        # Preprocesamiento (si es necesario)
        # scaled_features = scaler.transform(features_np)
        scaled_features = features_np # Simulación

        # Predicción
        prediction = model(scaled_features[0])

        return PredictionOut(prediction=prediction)

    except Exception as e:
        # Manejo de errores (FastAPI tiene manejo de excepciones más avanzado)
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {e}")

# (FastAPI no necesita el bloque if __name__ == '__main__' para ejecución con Uvicorn)

# 6. Ejecutar la aplicación (desde la terminal)
# Abre tu terminal en el directorio donde guardaste app_fastapi.py y ejecuta:
# uvicorn app_fastapi:app --reload
#
# --reload activa la recarga automática en desarrollo
```

**Para probar esta API (una vez ejecutada con Uvicorn):**
*   Abre tu navegador en `http://127.0.0.1:8000/docs`. Verás la documentación interactiva de Swagger UI generada automáticamente. ¡Puedes probar la API directamente desde allí!
*   O usa `curl`, Postman, o `requests` como en el ejemplo de Flask (apuntando a `http://127.0.0.1:8000/predict`).

## Flask vs. FastAPI

*   **Flask:** Más simple para empezar, muy flexible, ecosistema maduro de extensiones. Ideal si no necesitas validación de datos incorporada o async de forma nativa.
*   **FastAPI:** Más moderno, rendimiento superior, validación de datos y documentación automática excelentes gracias a Pydantic y type hints, soporte async nativo. Ideal para nuevas APIs, especialmente si se espera alto rendimiento o se valora la robustez del tipado.

Ambos son excelentes opciones para exponer tus modelos de ML o análisis como servicios web. La elección depende de tus preferencias, la complejidad del proyecto y los requisitos de rendimiento.
