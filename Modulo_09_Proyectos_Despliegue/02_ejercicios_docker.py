# Ejercicios: Módulo 9 - Despliegue con Docker

# --- Prerrequisitos ---
# Comprensión básica de qué es una API (como las vistas con Flask/FastAPI).
# Docker Desktop instalado (o Docker Engine en Linux) si quieres probar los comandos localmente.
# (La ejecución de comandos Docker no se hará desde este script).

print("--- Despliegue con Docker ---")

# --- Ejercicio 1: Conceptos Clave de Docker ---
# Instrucciones:
# Define brevemente (en comentarios) los siguientes conceptos de Docker:

# a) Imagen Docker (Docker Image):
# Respuesta A: Una plantilla inmutable y ligera que contiene todo lo necesario para ejecutar una aplicación:
#             el código, las dependencias (bibliotecas), las variables de entorno, los archivos de configuración,
#             y el runtime. Es como una "receta" o un "snapshot" del entorno de la aplicación.

# b) Contenedor Docker (Docker Container):
# Respuesta B: Una instancia *ejecutable* de una Imagen Docker. Es un proceso aislado que corre en el sistema
#             operativo anfitrión pero tiene su propio sistema de archivos, red y espacio de procesos.
#             Puedes iniciar, detener, mover y eliminar contenedores basados en la misma imagen.

# c) Dockerfile:
# Respuesta C: Un archivo de texto plano que contiene una serie de instrucciones paso a paso
#             (comandos) que Docker utiliza para construir automáticamente una Imagen Docker.
#             Define la imagen base, copia los archivos de la aplicación, instala dependencias,
#             configura el entorno y especifica el comando a ejecutar cuando se inicie un contenedor.

# d) Docker Hub (o Registro de Contenedores):
# Respuesta D: Un servicio (Docker Hub es el más popular, pero hay otros como GCR, ECR) que actúa
#             como un repositorio centralizado para almacenar y compartir Imágenes Docker. Permite
#             descargar imágenes pre-construidas (ej. `python:3.9-slim`) y subir tus propias imágenes.

print("--- Ejercicio 1: Conceptos Clave de Docker ---")
print("Ver comentarios en el código para las definiciones.")
print("-" * 20)


# --- Ejercicio 2: Escribir un Dockerfile Simple ---
# Instrucciones:
# 1. Imagina que tienes una aplicación Flask simple en un archivo llamado `mi_api_flask.py`
#    (puedes basarte en el Ejercicio 1 de `01_ejercicios_apis_simples.py`).
# 2. Supón que esta aplicación necesita la biblioteca `Flask`, listada en un archivo `requirements.txt`.
# 3. Escribe (como un string multilínea o comentarios) un `Dockerfile` básico que haga lo siguiente:
#    a. Use una imagen base oficial de Python (ej. `python:3.9-slim`).
#    b. Establezca un directorio de trabajo dentro de la imagen (ej. `/app`).
#    c. Copie el archivo `requirements.txt` al directorio de trabajo.
#    d. Ejecute `pip install` para instalar las dependencias del `requirements.txt`.
#    e. Copie el resto de los archivos de la aplicación (en este caso, `mi_api_flask.py`) al directorio de trabajo.
#    f. Exponga el puerto que usa Flask (por defecto, 5000).
#    g. Defina el comando por defecto para ejecutar la aplicación Flask cuando el contenedor inicie
#       (ej. `CMD ["python", "mi_api_flask.py"]`). Asegúrate de que el script Flask se ejecute en `host='0.0.0.0'`.

print("\n--- Ejercicio 2: Escribir un Dockerfile Simple ---")

# Archivo `mi_api_flask.py` (Simulado para referencia):
# ```python
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello():
#     return "Hola desde Docker!"
# if __name__ == '__main__':
#     app.run(debug=False, host='0.0.0.0', port=5000) # Escuchar en todas las interfaces
# ```

# Archivo `requirements.txt` (Simulado para referencia):
# ```
# Flask>=2.0
# ```

# 3. Dockerfile (como string multilínea)
dockerfile_content = """
# a. Usar una imagen base oficial de Python
FROM python:3.9-slim

# b. Establecer el directorio de trabajo
WORKDIR /app

# c. Copiar el archivo de requerimientos primero (aprovecha caché de Docker)
COPY requirements.txt .

# d. Instalar dependencias
#    --no-cache-dir evita guardar caché de pip, --upgrade pip actualiza pip
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# e. Copiar el resto del código de la aplicación
COPY . .
# Alternativa más específica si solo es un archivo: COPY mi_api_flask.py .

# f. Exponer el puerto que usará la aplicación Flask
EXPOSE 5000

# g. Comando para ejecutar la aplicación cuando inicie el contenedor
#    Usamos la forma de lista para evitar problemas con shells.
#    Asegúrate de que tu script Flask escuche en 0.0.0.0
CMD ["python", "mi_api_flask.py"]
"""

print("Contenido del Dockerfile (ejemplo):")
print(dockerfile_content)
print("-" * 20)


# --- Ejercicio 3: Comandos Docker (Conceptual) ---
# Instrucciones:
# Escribe (como comentarios) los comandos básicos de Docker que usarías para:
# a) Construir la imagen Docker a partir del `Dockerfile` del ejercicio anterior.
#    Asigna un nombre y etiqueta a la imagen (ej. `mi-flask-app:v1`).
# b) Listar las imágenes Docker que tienes localmente.
# c) Ejecutar un contenedor en segundo plano (`-d`) a partir de la imagen construida.
#    Mapea el puerto 5000 del contenedor al puerto 8080 de tu máquina local (`-p 8080:5000`).
#    Dale un nombre al contenedor (ej. `flask_container`).
# d) Listar los contenedores Docker que están actualmente en ejecución.
# e) Ver los logs (salida) del contenedor en ejecución.
# f) Detener el contenedor en ejecución.
# g) Eliminar el contenedor detenido.
# h) Eliminar la imagen Docker local.

print("\n--- Ejercicio 3: Comandos Docker (Conceptual) ---")
# Escribe tus respuestas como comentarios

# a) Construir la imagen:
#    (Asegúrate de estar en el directorio que contiene el Dockerfile y el código)
#    docker build -t mi-flask-app:v1 .
#    (-t asigna nombre:tag, '.' indica que el contexto es el directorio actual)

# b) Listar imágenes locales:
#    docker images
#    (o docker image ls)

# c) Ejecutar un contenedor:
#    docker run -d -p 8080:5000 --name flask_container mi-flask-app:v1
#    (-d: detached/background, -p host:container, --name: nombre contenedor)

# d) Listar contenedores en ejecución:
#    docker ps
#    (Para ver todos, incluyendo detenidos: docker ps -a)

# e) Ver logs del contenedor:
#    docker logs flask_container
#    (Para seguir los logs en tiempo real: docker logs -f flask_container)

# f) Detener el contenedor:
#    docker stop flask_container

# g) Eliminar el contenedor (debe estar detenido):
#    docker rm flask_container

# h) Eliminar la imagen local:
#    docker rmi mi-flask-app:v1
#    (Puede fallar si hay contenedores (incluso detenidos) basados en ella)

print("Ver comentarios en el código para los comandos Docker.")
print("-" * 20)


# --- Ejercicio 4: Beneficios de Docker ---
# Instrucciones:
# Enumera al menos tres beneficios clave de usar Docker para el despliegue de aplicaciones.

# Respuesta (en comentarios):
# 1. Consistencia del Entorno: Las imágenes Docker empaquetan la aplicación y *todas* sus dependencias.
#    Esto asegura que la aplicación se ejecute de la misma manera en desarrollo, pruebas y producción,
#    eliminando el problema de "funciona en mi máquina".
# 2. Aislamiento: Los contenedores están aislados entre sí y del sistema anfitrión, lo que mejora
#    la seguridad y evita conflictos entre dependencias de diferentes aplicaciones.
# 3. Portabilidad: Una imagen Docker construida en una máquina se puede ejecutar en cualquier otra
#    máquina que tenga Docker instalado (Linux, Windows, macOS, Cloud), facilitando el despliegue
#    en diferentes entornos.
# 4. Eficiencia de Recursos: Los contenedores son mucho más ligeros que las máquinas virtuales
#    tradicionales, ya que comparten el kernel del sistema operativo anfitrión. Esto permite
#    ejecutar más contenedores en el mismo hardware.
# 5. Escalabilidad y Orquestación: Docker se integra bien con herramientas de orquestación
#    (como Kubernetes) que permiten gestionar, escalar y automatizar el despliegue de
#    aplicaciones contenerizadas a gran escala.
# 6. Rapidez de Despliegue: Construir y ejecutar contenedores suele ser mucho más rápido que
#    configurar máquinas virtuales o entornos manualmente.

print("\n--- Ejercicio 4: Beneficios de Docker ---")
print("Ver comentarios en el código para los beneficios.")
print("-" * 20)

# --- Fin de los ejercicios ---
