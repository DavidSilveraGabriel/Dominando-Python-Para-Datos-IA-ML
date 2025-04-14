# Módulo 2: Estructura de un Proyecto Python Estándar

Cuando empiezas un nuevo proyecto en Python, especialmente uno que crecerá más allá de un simple script, es crucial adoptar una **estructura de directorios organizada y estándar**. Esto ofrece múltiples beneficios:

*   **Claridad:** Es más fácil para ti y para otros entender dónde encontrar cada tipo de archivo (código fuente, pruebas, documentación, configuración, etc.).
*   **Mantenibilidad:** Simplifica la modificación y la adición de nuevas funcionalidades.
*   **Reutilización:** Facilita la conversión de tu proyecto en un paquete instalable si es necesario.
*   **Colaboración:** Permite que los miembros del equipo trabajen de manera más eficiente al seguir convenciones conocidas.
*   **Herramientas:** Muchas herramientas de desarrollo (testing, documentación, empaquetado) esperan una cierta estructura.

No existe una única estructura "oficial" obligatoria, pero sí hay patrones y convenciones muy extendidos en la comunidad Python. A continuación, se describe una estructura común y recomendada para muchos tipos de proyectos.

## Estructura Típica

```
nombre_del_proyecto/
│
├── .gitignore             # Archivos/patrones a ignorar por Git
├── README.md              # Descripción del proyecto, instrucciones de uso/instalación
├── requirements.txt       # Lista de dependencias (para pip)
├── environment.yml        # Lista de dependencias (para conda - opcional/alternativo)
├── setup.py               # Metadatos y script de instalación (más tradicional)
│   o pyproject.toml       # Metadatos y configuración de build (más moderno)
│
├── src/                   # Directorio principal del código fuente (opción 1)
│   └── nombre_paquete/    # El paquete Python real de tu proyecto
│       ├── __init__.py    # Marca el directorio como paquete
│       ├── modulo1.py
│       ├── modulo2.py
│       └── subpaquete/
│           ├── __init__.py
│           └── modulo3.py
│
├── nombre_paquete/        # Directorio principal del código fuente (opción 2 - si no usas src/)
│   ├── __init__.py
│   ├── modulo1.py
│   └── ...
│
├── tests/                 # Directorio para las pruebas unitarias/integración
│   ├── __init__.py        # A veces necesario para que pytest descubra tests
│   ├── test_modulo1.py
│   └── test_subpaquete/
│       └── test_modulo3.py
│
├── docs/                  # Directorio para la documentación (ej. Sphinx)
│   ├── conf.py
│   ├── index.rst
│   └── ...
│
├── data/                  # Directorio para archivos de datos (opcional)
│   ├── raw/
│   └── processed/
│
└── scripts/               # Directorios para scripts auxiliares (opcional)
    ├── procesar_datos.py
    └── generar_reporte.py

```

## Descripción de Componentes:

*   **Directorio Raíz (`nombre_del_proyecto/`)**: La carpeta principal que contiene todo el proyecto. Debería ser un repositorio Git (`git init` aquí).
*   **`.gitignore`**: Especifica qué archivos o directorios Git debe ignorar (ej. `__pycache__/`, `*.pyc`, `*.env`, `*.log`, entornos virtuales como `venv/` o `env/`). Es fundamental para mantener limpio el repositorio.
*   **`README.md`**: Archivo Markdown esencial que describe el proyecto: qué hace, cómo instalarlo, cómo ejecutarlo, cómo contribuir, etc. Es lo primero que alguien (¡incluido tu yo futuro!) verá.
*   **`requirements.txt`**: Lista las dependencias externas del proyecto que se instalan con `pip`. Se genera comúnmente con `pip freeze > requirements.txt` (dentro del entorno virtual activado). Se usa para instalar dependencias con `pip install -r requirements.txt`.
*   **`environment.yml`**: Alternativa (o complemento) a `requirements.txt` si usas `conda`. Define el entorno `conda`, incluyendo la versión de Python y las dependencias (de conda y pip). Se usa para crear el entorno con `conda env create -f environment.yml`. Muy común en proyectos de ciencia de datos.
*   **`setup.py` / `pyproject.toml`**: Archivos de metadatos utilizados por herramientas como `setuptools` y `pip` para construir, empaquetar y distribuir tu proyecto como una biblioteca instalable. `pyproject.toml` es el estándar más moderno para definir dependencias de construcción y metadatos.
*   **`src/` (Directorio Fuente - Opción 1, Recomendada)**:
    *   Contiene el código fuente principal de tu aplicación o biblioteca, organizado como un paquete Python (`nombre_paquete/`).
    *   **Ventaja:** Separa claramente el código fuente de los archivos de configuración, pruebas, etc., en la raíz. Evita problemas de importación accidentales si tienes un archivo con el mismo nombre en la raíz y dentro del paquete.
*   **`nombre_paquete/` (Directorio Fuente - Opción 2)**:
    *   Alternativamente, puedes colocar tu paquete Python directamente en la raíz del proyecto. Es más simple para proyectos pequeños, pero puede volverse menos claro a medida que el proyecto crece.
*   **`nombre_paquete/__init__.py`**: Marca el directorio `nombre_paquete` como un paquete Python, permitiendo importaciones como `import nombre_paquete.modulo1`. Puede estar vacío o contener inicialización del paquete.
*   **`tests/`**: Contiene todo el código de prueba (unitarias, de integración, etc.). La estructura de `tests/` a menudo refleja la estructura de tu paquete fuente para facilitar la localización de las pruebas correspondientes a cada módulo. Herramientas como `pytest` suelen descubrir y ejecutar pruebas automáticamente desde este directorio.
*   **`docs/`**: Contiene archivos para generar la documentación del proyecto. Herramientas como Sphinx son comunes para esto, utilizando formatos como reStructuredText (`.rst`) o Markdown (`.md`).
*   **`data/` (Opcional)**: Para almacenar archivos de datos necesarios para el proyecto, a menudo separados en subdirectorios como `raw` (datos originales) y `processed` (datos limpios o transformados). **Importante:** Si los datos son muy grandes, considera no incluirlos directamente en el repositorio Git (usa `.gitignore`) y proporciona instrucciones sobre cómo obtenerlos.
*   **`scripts/` (Opcional)**: Para scripts auxiliares que no forman parte de la biblioteca principal pero son útiles para el desarrollo, despliegue, procesamiento de datos, etc.

**Adaptaciones:**

Esta estructura es una guía. Puedes adaptarla según las necesidades de tu proyecto:

*   Proyectos muy pequeños pueden omitir `src/` o `docs/`.
*   Proyectos web (Django/Flask) tienen sus propias estructuras generadas por los frameworks, aunque a menudo incorporan elementos de esta estructura general.
*   Proyectos de ciencia de datos pueden tener carpetas adicionales como `notebooks/` para Jupyter Notebooks de exploración.

Adoptar una estructura de proyecto estándar desde el principio te ahorrará muchos dolores de cabeza a medida que tu proyecto evolucione. Facilita la navegación, las pruebas, la documentación y la colaboración.
