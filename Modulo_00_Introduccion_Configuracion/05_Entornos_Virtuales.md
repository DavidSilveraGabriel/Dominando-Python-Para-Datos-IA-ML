# Módulo 0: Gestión de Entornos Virtuales con `venv` y `pip`

Imagina que trabajas en dos proyectos Python diferentes:

*   **Proyecto A:** Requiere la versión 1.0 de una librería llamada `SuperLib`.
*   **Proyecto B:** Requiere la versión 2.5 de la misma librería `SuperLib`.

Si instalas las librerías directamente en tu sistema principal de Python, tendrás un problema: solo puedes tener una versión de `SuperLib` instalada a la vez. Instalar la v2.5 romperá el Proyecto A, e instalar la v1.0 romperá el Proyecto B. ¡Un caos!

Aquí es donde entran los **Entornos Virtuales**.

**¿Qué es un Entorno Virtual?**

Un entorno virtual es un directorio aislado que contiene una instalación específica de Python (o un enlace a ella) y un conjunto independiente de librerías (paquetes) instaladas en él. Piensa en ello como una "burbuja" autocontenida para cada uno de tus proyectos.

**¿Por Qué Son Fundamentales?**

*   **Aislamiento de Dependencias:** Cada proyecto puede tener sus propias versiones de librerías sin afectar a otros proyectos ni a la instalación global de Python. ¡Adiós a los conflictos!
*   **Reproducibilidad:** Facilitan compartir tu proyecto con otros o desplegarlo en un servidor, ya que puedes especificar exactamente qué librerías y versiones necesita a través de un archivo `requirements.txt`.
*   **Organización:** Mantienen tu sistema limpio, ya que las librerías específicas del proyecto no se instalan globalmente.

**Herramientas Estándar: `venv` y `pip`**

Python incluye herramientas incorporadas para gestionar entornos y paquetes:

1.  **`venv` (Módulo Estándar):**
    *   Incluido en Python 3.3+. Es la herramienta recomendada y estándar para crear entornos virtuales.
    *   Crea un entorno ligero que utiliza el intérprete Python con el que se creó.
    *   Funciona perfectamente para la mayoría de los proyectos Python.

2.  **`pip` (Instalador de Paquetes):**
    *   Es el gestor de paquetes estándar para Python. Se utiliza para instalar, actualizar y desinstalar librerías desde el Python Package Index (PyPI) y otras fuentes.
    *   `pip` se instala automáticamente al crear un entorno con `venv`.

**Usando `venv` y `pip` (Comandos Esenciales):**

(Ejecuta estos comandos en tu **Terminal** o **Símbolo del sistema** habitual)

1.  **Crear un Nuevo Entorno Virtual:**
    *   Navega en tu terminal hasta el directorio raíz de tu proyecto.
    *   Ejecuta el siguiente comando:
    ```bash
    python -m venv <nombre_entorno>
    ```
    *   `<nombre_entorno>`: Es el nombre que le darás al directorio del entorno. Una convención común es llamarlo `venv` o `.venv`.
    *   **Ejemplo:** `python -m venv venv`
    *   Esto creará una carpeta llamada `venv` (o el nombre que elijas) en tu directorio actual. Esta carpeta contiene una copia o enlace del intérprete de Python y la estructura necesaria para instalar paquetes de forma aislada.
    *   **¡Importante!** Añade el nombre de tu carpeta de entorno virtual (ej. `venv/`) a tu archivo `.gitignore` si usas Git, para no incluirla en tu repositorio.

2.  **Activar el Entorno Virtual:**
    *   Antes de poder usar un entorno (instalar paquetes en él o ejecutar código que dependa de sus paquetes), necesitas activarlo. El comando varía según tu sistema operativo:
    *   **Windows (cmd.exe):**
        ```bash
        <nombre_entorno>\Scripts\activate
        ```
        *   **Ejemplo:** `venv\Scripts\activate`
    *   **Windows (PowerShell):**
        ```powershell
        .\<nombre_entorno>\Scripts\Activate.ps1
        ```
        *   **Ejemplo:** `.\venv\Scripts\Activate.ps1`
        *   (Puede que necesites ajustar la política de ejecución de scripts: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`)
    *   **macOS / Linux (bash/zsh):**
        ```bash
        source <nombre_entorno>/bin/activate
        ```
        *   **Ejemplo:** `source venv/bin/activate`
    *   Una vez activado, notarás que el nombre del entorno aparece entre paréntesis al inicio de tu prompt (ej. `(venv) C:\ruta\a\tu\proyecto>`), indicando que el entorno está activo.

3.  **Instalar Paquetes con `pip`:**
    *   **¡Asegúrate de tener el entorno correcto activado primero!**
    *   Usa `pip install` para añadir librerías a tu entorno activo:
    ```bash
    pip install <nombre_paquete>
    pip install <paquete1> <paquete2>
    pip install <paquete>==<version> # Instalar una versión específica
    pip install --upgrade <paquete> # Actualizar un paquete
    ```
    *   **Ejemplo (con `venv` activo):** `pip install requests`
    *   **Instalar desde un archivo de requerimientos:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Listar Paquetes Instalados:**
    *   Para ver qué paquetes y versiones están instalados en el entorno activo:
    ```bash
    pip list
    ```

5.  **Generar `requirements.txt`:**
    *   Este archivo lista los paquetes y sus versiones exactas instaladas en el entorno, permitiendo a otros (o a ti mismo en otro lugar) recrear el mismo entorno.
    *   **¡Asegúrate de tener el entorno correcto activado!**
    ```bash
    pip freeze > requirements.txt
    ```
    *   Esto crea (o sobrescribe) un archivo `requirements.txt` en tu directorio actual con el listado de paquetes. Es buena práctica mantener este archivo actualizado y subirlo a tu control de versiones (Git).

6.  **Desactivar el Entorno Virtual:**
    *   Cuando termines de trabajar en el proyecto, puedes desactivar el entorno:
    ```bash
    deactivate
    ```
    *   Esto funciona en todos los sistemas operativos una vez que el entorno está activo. El prompt volverá a la normalidad.

7.  **Eliminar un Entorno:**
    *   Simplemente elimina la carpeta del entorno virtual:
    *   **Windows:** `rmdir /s /q <nombre_entorno>`
    *   **macOS / Linux:** `rm -rf <nombre_entorno>`
    *   **Ejemplo:** `rm -rf venv`

**Alternativa: `conda`**

Aunque `venv` y `pip` son el estándar, es útil conocer `conda`:

*   Viene con las distribuciones Anaconda y Miniconda.
*   Gestiona tanto entornos como paquetes.
*   Puede gestionar paquetes de Python y dependencias que no son de Python (ej. librerías C/C++, R), lo cual es una gran ventaja en el ecosistema científico y de ciencia de datos.
*   Los comandos son diferentes (ej. `conda create --name mi_env python=3.10`, `conda activate mi_env`, `conda install numpy`, `conda deactivate`).

Si trabajas principalmente en ciencia de datos o necesitas gestionar dependencias complejas no-Python, `conda` puede ser una opción más robusta. Para desarrollo general de Python, `venv` y `pip` suelen ser suficientes y más ligeros.

**Recomendación para el Curso:**

Utilizaremos `venv` y `pip` como herramientas principales en este curso. **¡Acostúmbrate a crear y activar SIEMPRE un entorno virtual para cada nuevo proyecto Python que inicies!** Esto te ahorrará muchos problemas de dependencias en el futuro.
