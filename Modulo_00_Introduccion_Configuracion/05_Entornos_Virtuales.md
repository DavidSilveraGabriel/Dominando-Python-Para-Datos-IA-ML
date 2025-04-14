# Módulo 0: Gestión de Entornos Virtuales (`conda` / `venv`)

Imagina que trabajas en dos proyectos Python diferentes:

*   **Proyecto A:** Requiere la versión 1.0 de una librería llamada `SuperLib`.
*   **Proyecto B:** Requiere la versión 2.5 de la misma librería `SuperLib`.

Si instalas las librerías directamente en tu sistema principal de Python, tendrás un problema: solo puedes tener una versión de `SuperLib` instalada a la vez. Instalar la v2.5 romperá el Proyecto A, e instalar la v1.0 romperá el Proyecto B. ¡Un caos!

Aquí es donde entran los **Entornos Virtuales**.

**¿Qué es un Entorno Virtual?**

Un entorno virtual es un directorio aislado que contiene una instalación específica de Python y un conjunto independiente de librerías (paquetes) instaladas en él. Piensa en ello como una "burbuja" autocontenida para cada uno de tus proyectos.

**¿Por Qué Son Fundamentales?**

*   **Aislamiento de Dependencias:** Cada proyecto puede tener sus propias versiones de librerías sin afectar a otros proyectos ni a la instalación global de Python. ¡Adiós a los conflictos!
*   **Reproducibilidad:** Facilitan compartir tu proyecto con otros o desplegarlo en un servidor, ya que puedes especificar exactamente qué librerías y versiones necesita (generalmente a través de un archivo como `environment.yml` para conda o `requirements.txt` para pip/venv).
*   **Organización:** Mantienen tu sistema limpio, ya que las librerías específicas del proyecto no se instalan globalmente.

**Herramientas para Gestionar Entornos:**

1.  **`conda` (Recomendado para este curso):**
    *   Viene con Anaconda/Miniconda.
    *   Gestiona tanto paquetes de Python como de otros lenguajes y dependencias del sistema (ej. librerías C).
    *   Es especialmente robusto para el ecosistema científico y de ciencia de datos.

2.  **`venv` (Estándar de Python):**
    *   Módulo incorporado en Python 3.3+.
    *   Funciona bien para proyectos que solo usan paquetes de Python instalables vía `pip`.
    *   No gestiona dependencias no-Python tan fácilmente como `conda`.

**Usando `conda` para Gestionar Entornos (Comandos Esenciales):**

(Ejecuta estos comandos en el **Anaconda Prompt** en Windows, o en la **Terminal** en macOS/Linux)

1.  **Crear un Nuevo Entorno:**
    ```bash
    conda create --name <nombre_entorno> python=3.x <librerias_opcionales>
    ```
    *   `--name <nombre_entorno>`: Especifica el nombre que le quieres dar a tu entorno (ej. `curso_ds`, `mi_proyecto_web`).
    *   `python=3.x`: Especifica la versión de Python que quieres usar en este entorno (ej. `python=3.10`, `python=3.11`). ¡Es buena práctica especificarla!
    *   `<librerias_opcionales>`: Puedes añadir nombres de librerías que quieras instalar al crear el entorno (ej. `numpy pandas jupyterlab`).
    *   **Ejemplo:** `conda create --name curso_ds python=3.10 numpy pandas matplotlib scikit-learn jupyterlab`
    *   `conda` te preguntará si quieres proceder. Escribe `y` y presiona Enter.

2.  **Activar un Entorno:**
    *   Antes de poder usar un entorno (instalar paquetes en él o ejecutar código que dependa de sus paquetes), necesitas activarlo.
    ```bash
    conda activate <nombre_entorno>
    ```
    *   **Ejemplo:** `conda activate curso_ds`
    *   Notarás que el `(base)` al inicio de tu prompt cambia a `(<nombre_entorno>)`. Esto indica que el entorno está activo.

3.  **Desactivar el Entorno Actual:**
    *   Para volver al entorno `base` (o al entorno anterior).
    ```bash
    conda deactivate
    ```
    *   El prompt volverá a mostrar `(base)`.

4.  **Listar Entornos Disponibles:**
    ```bash
    conda env list
    ```
    *   O también: `conda info --envs`
    *   Muestra todos los entornos que has creado y sus ubicaciones. El entorno activo estará marcado con un `*`.

5.  **Instalar Paquetes en el Entorno Activo:**
    *   **¡Asegúrate de tener el entorno correcto activado primero!**
    ```bash
    conda install <nombre_paquete>
    conda install <paquete1> <paquete2>
    conda install <paquete>=<version> # Instalar una versión específica
    ```
    *   **Ejemplo (con `curso_ds` activo):** `conda install seaborn`

6.  **Listar Paquetes Instalados en el Entorno Activo:**
    *   **¡Asegúrate de tener el entorno correcto activado!**
    ```bash
    conda list
    ```

7.  **Eliminar un Entorno:**
    *   **¡Asegúrate de que el entorno NO esté activo!** (Usa `conda deactivate` si es necesario).
    ```bash
    conda env remove --name <nombre_entorno>
    ```
    *   **Ejemplo:** `conda env remove --name curso_ds`
    *   Esto borrará el entorno y todos los paquetes instalados en él.

**Recomendación para el Curso:**

Crearemos un entorno `conda` específico para este curso al inicio del Módulo 1 (o puedes crearlo ahora si quieres practicar) e instalaremos allí todas las librerías necesarias. **¡Acostúmbrate a trabajar SIEMPRE dentro de un entorno virtual activado para cada proyecto!**
