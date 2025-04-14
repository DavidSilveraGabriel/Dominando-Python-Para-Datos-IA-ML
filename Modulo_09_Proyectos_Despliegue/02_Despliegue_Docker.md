# Módulo 9: Despliegue con Docker: Contenerización

Una vez que has desarrollado tu aplicación de ciencia de datos o tu API de modelo de ML, el siguiente paso es **desplegarla** para que otros puedan usarla o para que se ejecute en un entorno de producción. Desplegar aplicaciones puede ser complicado debido a las diferencias entre entornos (tu máquina vs. el servidor, diferentes sistemas operativos, versiones de bibliotecas, etc.).

**Docker** es una tecnología de **contenedores** que resuelve muchos de estos problemas.

## ¿Qué es Docker y los Contenedores?

*   **Contenedor:** Es una unidad estándar y ligera de software que **empaqueta el código y todas sus dependencias** (bibliotecas, herramientas del sistema, configuraciones) para que la aplicación se ejecute de forma rápida y fiable de un entorno informático a otro.
*   **Imagen Docker:** Es una **plantilla** ligera, independiente y ejecutable que incluye todo lo necesario para ejecutar una pieza de software: el código, un runtime (ej. Python), herramientas del sistema, bibliotecas y configuraciones. Las imágenes se usan para crear contenedores.
*   **Docker:** Es la **plataforma** de código abierto para desarrollar, enviar y ejecutar aplicaciones dentro de contenedores. Proporciona las herramientas para construir imágenes y ejecutar contenedores.

**Analogía:** Piensa en los contenedores de transporte marítimo. Contienen diferentes tipos de carga, pero todos tienen una forma estándar que permite moverlos y apilarlos fácilmente usando la misma maquinaria (grúas, barcos, trenes). Docker hace lo mismo para el software.

**Ventajas de usar Docker para Despliegue:**

*   **Consistencia:** Tu aplicación se ejecuta igual en tu máquina, en la de un compañero, en el servidor de pruebas y en producción, porque el contenedor incluye todo el entorno necesario. ¡Adiós al "funciona en mi máquina"!
*   **Aislamiento:** Los contenedores aíslan las aplicaciones entre sí y del sistema operativo subyacente. Puedes tener diferentes versiones de Python o bibliotecas en contenedores separados sin conflictos.
*   **Portabilidad:** Las imágenes Docker se pueden ejecutar en cualquier sistema que tenga Docker instalado (Linux, Windows, macOS, nubes como AWS, Azure, GCP).
*   **Eficiencia:** Los contenedores son mucho más ligeros que las máquinas virtuales tradicionales porque comparten el kernel del sistema operativo host. Se inician más rápido y consumen menos recursos.
*   **Escalabilidad:** Es fácil crear y destruir contenedores rápidamente para escalar tu aplicación horizontalmente.
*   **Reproducibilidad:** El `Dockerfile` (ver abajo) define exactamente cómo se construye la imagen, haciendo que el proceso sea reproducible.

## Componentes Clave de Docker

1.  **Dockerfile:**
    *   Es un **archivo de texto** que contiene una serie de **instrucciones** paso a paso sobre cómo construir una imagen Docker.
    *   Define la imagen base (ej. una imagen oficial de Python), copia el código de tu aplicación, instala dependencias, configura el entorno y especifica el comando a ejecutar cuando se inicie un contenedor desde la imagen.

2.  **Imagen Docker (Image):**
    *   La plantilla creada a partir de un `Dockerfile` usando el comando `docker build`.
    *   Las imágenes se componen de capas de solo lectura.
    *   Se pueden almacenar localmente o en registros como Docker Hub (público) o registros privados.

3.  **Contenedor Docker (Container):**
    *   Una **instancia en ejecución** de una imagen Docker.
    *   Es la capa superior escribible sobre la imagen base.
    *   Se crea y se inicia usando el comando `docker run`. Puedes tener múltiples contenedores ejecutándose a partir de la misma imagen.

## Ejemplo: Dockerizando una API Simple (Flask)

Supongamos que tenemos la API Flask del archivo anterior (`app_flask.py`) y queremos dockerizarla.

**Paso 1: Crear el `Dockerfile`**

Crea un archivo llamado `Dockerfile` (sin extensión) en la raíz de tu proyecto, junto a `app_flask.py` y `requirements.txt`.

```dockerfile
# Dockerfile

# 1. Usar una imagen base oficial de Python
# Elige una versión específica (ej. 3.10-slim para una imagen más ligera)
FROM python:3.10-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar el archivo de dependencias PRIMERO
# (Aprovecha el caché de Docker: si requirements.txt no cambia, no reinstala)
COPY requirements.txt .

# 4. Instalar las dependencias
# --no-cache-dir reduce el tamaño de la imagen
# --upgrade pip asegura tener la última versión de pip
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 5. Copiar el resto del código de la aplicación al directorio de trabajo
COPY . .

# 6. Exponer el puerto que usará la aplicación Flask (ej. 5000)
EXPOSE 5000

# 7. Comando para ejecutar la aplicación cuando se inicie el contenedor
# Usamos 'flask run --host=0.0.0.0' para que sea accesible desde fuera del contenedor
# (En producción real, a menudo se usa un servidor WSGI como Gunicorn o uWSGI)
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
```

**Paso 2: Crear el archivo `requirements.txt`**

Asegúrate de tener un archivo `requirements.txt` que liste las dependencias. Para nuestro ejemplo simple de Flask:

```txt
# requirements.txt
Flask>=2.0
numpy>=1.20 # Asumiendo que el modelo lo necesita
# joblib>=1.0 # Si cargas modelo con joblib
# scikit-learn>=1.0 # Si usas scaler u otros de sklearn
```
*(Genera este archivo en tu entorno virtual activado con `pip freeze > requirements.txt` para capturar todas tus dependencias y versiones exactas).*

**Paso 3: Construir la Imagen Docker**

Abre tu terminal en el directorio raíz del proyecto (donde está el `Dockerfile`) y ejecuta:

```bash
# docker build -t nombre_imagen[:tag] ruta_al_contexto
# -t: etiqueta (nombre y opcionalmente tag) para la imagen
# .: indica que el contexto de construcción (Dockerfile y archivos a copiar) es el directorio actual
docker build -t mi-flask-api:v1 .
```
Docker ejecutará las instrucciones del `Dockerfile` paso a paso. Esto puede tardar un poco la primera vez mientras descarga la imagen base e instala dependencias.

**Paso 4: Ejecutar el Contenedor**

Una vez construida la imagen, puedes crear y ejecutar un contenedor a partir de ella:

```bash
# docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
# -d: Ejecuta el contenedor en segundo plano (detached)
# -p host_port:container_port : Mapea un puerto de tu máquina (host) al puerto expuesto por el contenedor
# --name nombre_contenedor: Asigna un nombre al contenedor (opcional)
docker run -d -p 5001:5000 --name flask_api_container mi-flask-api:v1
```

*   `-d`: Corre en modo detached.
*   `-p 5001:5000`: Mapea el puerto 5001 de tu máquina al puerto 5000 dentro del contenedor (el que expusimos y donde corre Flask).
*   `--name flask_api_container`: Le da un nombre fácil de recordar al contenedor.
*   `mi-flask-api:v1`: El nombre y tag de la imagen que construimos.

**Paso 5: Probar la API Contenerizada**

Ahora, tu API Flask debería estar corriendo dentro del contenedor y ser accesible desde tu máquina en el puerto `5001`. Puedes probarla con `curl`, Postman, o el script `test_api.py` (modificando la URL a `http://127.0.0.1:5001/predict`).

**Comandos Docker Útiles:**

*   `docker images`: Lista las imágenes locales.
*   `docker ps`: Lista los contenedores en ejecución.
*   `docker ps -a`: Lista todos los contenedores (incluidos los detenidos).
*   `docker logs nombre_contenedor`: Muestra los logs (salida) del contenedor.
*   `docker stop nombre_contenedor`: Detiene un contenedor en ejecución.
*   `docker start nombre_contenedor`: Inicia un contenedor detenido.
*   `docker rm nombre_contenedor`: Elimina un contenedor detenido (¡se pierden los datos dentro!).
*   `docker rmi nombre_imagen`: Elimina una imagen local (si no hay contenedores usándola).
*   `docker exec -it nombre_contenedor bash`: Abre una terminal interactiva dentro de un contenedor en ejecución (muy útil para depurar).

Docker simplifica enormemente el proceso de empaquetar y desplegar aplicaciones, asegurando la consistencia entre entornos y facilitando la gestión de dependencias. Es una habilidad fundamental para desarrolladores y científicos de datos que necesitan poner sus creaciones en producción.
