# Ejercicios: Módulo 9 - APIs Simples con Flask/FastAPI

# --- Prerrequisitos ---
# Necesitarás instalar Flask y/o FastAPI, y un servidor ASGI como uvicorn para FastAPI.
# pip install Flask fastapi uvicorn[standard]
# o
# conda install flask fastapi uvicorn

# Nota: Estos ejercicios definen las APIs. Para ejecutarlas, necesitarás guardar
# cada ejemplo (Flask o FastAPI) en su propio archivo .py y ejecutarlo desde
# la terminal (ver comentarios en cada ejercicio).

from flask import Flask, request, jsonify
# from fastapi import FastAPI # Descomentar para FastAPI
# import uvicorn            # Descomentar para FastAPI
# from pydantic import BaseModel # Descomentar para FastAPI (validación de datos)

print("--- APIs Simples con Flask y FastAPI ---")

# --- Ejercicio 1: API "Hola Mundo" con Flask ---
# Instrucciones:
# 1. Importa `Flask` desde `flask`.
# 2. Crea una instancia de la aplicación Flask: `app_flask = Flask(__name__)`.
# 3. Define una ruta para la raíz (`'/'`) usando el decorador `@app_flask.route('/')`.
# 4. Crea una función `index()` asociada a esa ruta que devuelva el string "¡Hola, Mundo con Flask!".
# 5. (Conceptual) Añade un bloque `if __name__ == '__main__':` para ejecutar la app
#    en modo debug (`app_flask.run(debug=True)`).
# 6. (Conceptual) Explica en un comentario cómo ejecutarías esta app Flask.

print("--- Ejercicio 1: API 'Hola Mundo' con Flask ---")

# 1. Importar Flask (hecho arriba)
# 2. Crear instancia de Flask
app_flask = Flask(__name__)

# 3. Definir ruta raíz
@app_flask.route('/')
# 4. Función para la ruta
def index_flask():
    """Ruta principal de la API Flask."""
    return "¡Hola, Mundo con Flask!"

# 5. Bloque para ejecutar (conceptual)
# if __name__ == '__main__':
#     # host='0.0.0.0' permite acceso desde la red local
#     # port=5000 es el puerto por defecto
#     app_flask.run(debug=True, host='0.0.0.0', port=5000)

# 6. Cómo ejecutar (conceptual)
#    a. Guarda este bloque de código Flask (desde la importación hasta app.run)
#       en un archivo, por ejemplo, `app_flask_ej1.py`.
#    b. Abre una terminal en el directorio donde guardaste el archivo.
#    c. Ejecuta el comando: python app_flask_ej1.py
#    d. Abre tu navegador web y ve a http://127.0.0.1:5000/ (o la IP/puerto que muestre la terminal).
#       Deberías ver el mensaje "¡Hola, Mundo con Flask!".
#    e. Presiona Ctrl+C en la terminal para detener el servidor.

print("Código de la API Flask definido.")
print("Ver comentarios para instrucciones de ejecución.")
print("-" * 20)


# --- Ejercicio 2: Ruta con Parámetros en Flask ---
# Instrucciones:
# 1. Usando la misma `app_flask` del ejercicio anterior.
# 2. Define una nueva ruta `/saludar/<nombre>` que acepte un parámetro `nombre` en la URL.
#    Usa el decorador `@app_flask.route('/saludar/<string:nombre>')`. El `<string:nombre>`
#    captura la parte de la URL y la pasa como argumento string a la función.
# 3. Crea una función `saludar_nombre(nombre)` asociada a esa ruta que devuelva un saludo
#    personalizado, ej. f"¡Hola, {nombre}!".
# 4. (Conceptual) Reinicia la app Flask (si la tenías corriendo) y prueba a acceder
#    en tu navegador a `http://127.0.0.1:5000/saludar/Ana` (o con otro nombre).

print("\n--- Ejercicio 2: Ruta con Parámetros en Flask ---")

# 1. Reutilizar app_flask
# 2. Definir ruta con parámetro
@app_flask.route('/saludar/<string:nombre>')
# 3. Función para la ruta
def saludar_nombre_flask(nombre: str):
    """Saluda a la persona indicada en la URL."""
    return f"¡Hola, {nombre}!"

# 4. Cómo probar (conceptual)
#    a. Asegúrate de que el código Flask (incluyendo esta nueva ruta) esté en
#       tu archivo `app_flask_ej1.py` (o como lo hayas llamado).
#    b. Ejecuta `python app_flask_ej1.py` en la terminal.
#    c. Abre tu navegador y ve a:
#       - http://127.0.0.1:5000/saludar/Carlos -> Debería mostrar "¡Hola, Carlos!"
#       - http://127.0.0.1:5000/saludar/Maria -> Debería mostrar "¡Hola, Maria!"

print("Ruta '/saludar/<nombre>' definida para Flask.")
print("Ver comentarios para instrucciones de prueba.")
print("-" * 20)


# --- Ejercicio 3: Ruta POST con JSON en Flask ---
# Instrucciones:
# 1. Importa `request` y `jsonify` desde `flask`.
# 2. Define una nueva ruta `/sumar` que acepte peticiones POST (`methods=['POST']`).
# 3. Crea una función `sumar_numeros()` asociada a esa ruta.
# 4. Dentro de la función:
#    a. Obtén los datos JSON de la petición usando `request.get_json()`.
#    b. Verifica si se recibieron los datos y si contienen las claves 'a' y 'b'.
#    c. Si los datos son válidos, calcula la suma `a + b`.
#    d. Devuelve el resultado como una respuesta JSON usando `jsonify()`, ej. `jsonify({'resultado': suma})`.
#    e. Si los datos no son válidos, devuelve un error JSON con un código de estado 400 (Bad Request).
# 5. (Conceptual) Explica cómo probarías esta ruta POST (no puedes hacerlo directamente desde el navegador).

print("\n--- Ejercicio 3: Ruta POST con JSON en Flask ---")

# 1. Importar request y jsonify (hecho arriba)
# 2. Definir ruta POST
@app_flask.route('/sumar', methods=['POST'])
# 3. Función para la ruta
def sumar_numeros_flask():
    """Recibe dos números 'a' y 'b' en JSON y devuelve su suma."""
    # 4a. Obtener JSON
    datos = request.get_json()

    # 4b. Validar datos
    if not datos or 'a' not in datos or 'b' not in datos:
        return jsonify({"error": "Faltan los parámetros 'a' y 'b' en el JSON."}), 400 # Bad Request

    try:
        # 4c. Calcular suma
        a = float(datos['a'])
        b = float(datos['b'])
        suma = a + b
        # 4d. Devolver resultado JSON
        return jsonify({'resultado': suma})
    except (TypeError, ValueError):
        # 4e. Manejar error si 'a' o 'b' no son números
        return jsonify({"error": "Los parámetros 'a' y 'b' deben ser numéricos."}), 400

# 5. Cómo probar (conceptual)
#    - Las peticiones POST no se pueden hacer fácilmente escribiendo una URL en el navegador.
#    - Necesitas una herramienta cliente HTTP como:
#      - `curl` (línea de comandos):
#        ```bash
#        curl -X POST -H "Content-Type: application/json" -d '{"a": 10, "b": 5}' http://127.0.0.1:5000/sumar
#        ```
#      - Postman (aplicación gráfica).
#      - Insomnia (aplicación gráfica).
#      - Extensiones de navegador para hacer peticiones (ej. RESTED para Firefox/Chrome).
#      - Código Python usando la biblioteca `requests`:
#        ```python
#        import requests
#        response = requests.post('http://127.0.0.1:5000/sumar', json={'a': 20, 'b': 7})
#        print(response.json())
#        ```

print("Ruta '/sumar' (POST) definida para Flask.")
print("Ver comentarios para instrucciones de prueba.")
print("-" * 20)


# --- Ejercicio 4: API Equivalente con FastAPI (Conceptual) ---
# Instrucciones:
# 1. Comenta el código Flask anterior o escribe este en una sección separada.
# 2. Importa `FastAPI` desde `fastapi`.
# 3. (Opcional) Importa `BaseModel` de `pydantic` para validación de datos en POST.
# 4. Crea una instancia de la aplicación FastAPI: `app_fastapi = FastAPI()`.
# 5. Define las rutas equivalentes a los ejercicios 1, 2 y 3 usando los decoradores de FastAPI (`@app_fastapi.get('/')`, `@app_fastapi.get('/saludar/{nombre}')`, `@app_fastapi.post('/sumar')`).
#    - Para la ruta `/saludar/{nombre}`, el parámetro se define directamente en la firma de la función (`nombre: str`).
#    - Para la ruta `/sumar` (POST):
#      - Define una clase `SumaInput` que herede de `BaseModel` con atributos `a: float` y `b: float`.
#      - La función `sumar_numeros_fastapi` debe tomar un argumento `datos: SumaInput`. FastAPI manejará automáticamente la validación y extracción del JSON.
#      - Devuelve directamente un diccionario (FastAPI lo convierte a JSON).
# 6. (Conceptual) Añade comentarios explicando cómo ejecutarías esta app FastAPI usando `uvicorn`.

print("\n--- Ejercicio 4: API Equivalente con FastAPI (Conceptual) ---")
# Escribe tu código aquí (puedes comentar el código Flask si interfiere)

# --- Código FastAPI (Conceptual) ---
# from fastapi import FastAPI
# from pydantic import BaseModel
# import uvicorn

# # 4. Crear instancia FastAPI
# app_fastapi = FastAPI()

# # 5a. Ruta raíz GET
# @app_fastapi.get('/')
# async def index_fastapi(): # Las funciones pueden ser async o no
#     return {"mensaje": "¡Hola, Mundo con FastAPI!"}

# # 5b. Ruta GET con parámetro de path
# @app_fastapi.get('/saludar/{nombre}')
# async def saludar_nombre_fastapi(nombre: str):
#     return {"saludo": f"¡Hola, {nombre}!"}

# # 5c. Ruta POST con validación Pydantic
# class SumaInput(BaseModel):
#     a: float
#     b: float

# @app_fastapi.post('/sumar')
# async def sumar_numeros_fastapi(datos: SumaInput):
#     suma = datos.a + datos.b
#     return {'resultado': suma}

# # 6. Cómo ejecutar (conceptual)
# #    a. Guarda este bloque de código FastAPI en un archivo, por ejemplo, `app_fastapi_ej4.py`.
# #    b. Abre una terminal en el directorio donde guardaste el archivo.
# #    c. Ejecuta el comando: uvicorn app_fastapi_ej4:app_fastapi --reload
# #       - `app_fastapi_ej4`: el nombre del archivo Python (sin .py).
# #       - `app_fastapi`: el nombre de la instancia de FastAPI dentro del archivo.
# #       - `--reload`: hace que el servidor se reinicie automáticamente si cambias el código (útil en desarrollo).
# #    d. Abre tu navegador y ve a:
# #       - http://127.0.0.1:8000/ -> Debería mostrar {"mensaje": "¡Hola, Mundo con FastAPI!"}
# #       - http://127.0.0.1:8000/saludar/Fast -> Debería mostrar {"saludo": "¡Hola, Fast!"}
# #       - http://127.0.0.1:8000/docs -> FastAPI genera automáticamente documentación interactiva (Swagger UI).
# #    e. Usa una herramienta como `curl` o Postman para probar la ruta POST `/sumar`:
# #       ```bash
# #       curl -X POST -H "Content-Type: application/json" -d '{"a": 100, "b": 50}' http://127.0.0.1:8000/sumar
# #       ```
# #       Debería devolver: {"resultado": 150.0}
# #    f. Presiona Ctrl+C en la terminal para detener el servidor uvicorn.

print("Código conceptual de la API FastAPI definido.")
print("Ver comentarios para instrucciones de ejecución.")
print("-" * 20)

# --- Fin de los ejercicios ---
