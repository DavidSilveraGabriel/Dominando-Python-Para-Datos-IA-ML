# Módulo 0: Introducción a los IDEs (VS Code, Jupyter Notebooks/Lab)

Un **Entorno de Desarrollo Integrado (IDE)** es una aplicación de software que proporciona herramientas completas a los programadores para facilitar el desarrollo de software. Simplifica enormemente el proceso de escribir, ejecutar y depurar código.

Si bien puedes escribir código Python en un editor de texto simple y ejecutarlo desde la terminal, usar un IDE (o un editor de código avanzado con extensiones) te hará mucho más productivo/a.

**¿Por qué usar un IDE?**

*   **Resaltado de Sintaxis:** Colorea el código para diferenciar palabras clave, variables, comentarios, etc., mejorando la legibilidad.
*   **Autocompletado de Código:** Sugiere código mientras escribes, ahorrando tiempo y reduciendo errores.
*   **Depuración (Debugging):** Permite ejecutar el código paso a paso, inspeccionar variables y encontrar errores lógicos.
*   **Integración con Herramientas:** Se integra con sistemas de control de versiones (como Git), terminales, gestores de paquetes, etc.
*   **Gestión de Proyectos:** Ayuda a organizar los archivos y carpetas de tu proyecto.

**Herramientas Principales para este Curso:**

Para este curso, nos centraremos en dos herramientas fundamentales en el ecosistema de Python y Ciencia de Datos:

1.  **Visual Studio Code (VS Code):**
    *   **¿Qué es?** Un editor de código fuente gratuito, ligero pero potente, desarrollado por Microsoft. Es altamente extensible y personalizable.
    *   **Fortalezas:**
        *   Excelente para escribir scripts (`.py`), módulos y proyectos completos de Python.
        *   Gran soporte para Python a través de extensiones (como la extensión oficial de Python de Microsoft).
        *   Integración con Git incorporada.
        *   Terminal integrada.
        *   Capacidad de depuración robusta.
        *   Soporte para muchos otros lenguajes y tecnologías.
        *   Puede trabajar con Jupyter Notebooks directamente dentro de VS Code.
    *   **Uso en el curso:** Lo usaremos para desarrollar scripts, módulos, aplicaciones web (con Flask/FastAPI) y para gestionar la estructura general de nuestros proyectos.

2.  **Jupyter Notebook / JupyterLab:**
    *   **¿Qué es?** Una aplicación web de código abierto que permite crear y compartir documentos que contienen código vivo, ecuaciones, visualizaciones y texto narrativo. JupyterLab es la evolución de Jupyter Notebook, ofreciendo una interfaz más flexible y potente (similar a un IDE).
    *   **Fortalezas:**
        *   Ideal para exploración de datos interactiva, análisis y visualización.
        *   Permite ejecutar código en celdas individuales y ver los resultados inmediatamente debajo.
        *   Excelente para documentar el proceso de análisis y compartir resultados (muy usado en investigación y comunicación).
        *   Se integra perfectamente con librerías como Pandas, Matplotlib, Seaborn.
    *   **Uso en el curso:** Será nuestra herramienta principal para los módulos de NumPy, Pandas, Visualización y Machine Learning, donde la exploración interactiva y la visualización son clave.

**Instalación:**

*   **VS Code:**
    *   Descárgalo desde el sitio oficial: [https://code.visualstudio.com/](https://code.visualstudio.com/)
    *   Sigue las instrucciones de instalación para tu sistema operativo.
    *   Una vez instalado, abre VS Code y ve a la pestaña de **Extensiones** (el icono de bloques en la barra lateral izquierda). Busca e instala la extensión **"Python"** de Microsoft. Es posible que también quieras instalar **"Pylance"** (también de Microsoft) para una mejor experiencia de autocompletado y análisis de código.

*   **JupyterLab / Jupyter Notebook:**
    *   Si instalaste **Anaconda**, ¡ya vienen incluidos!
    *   Si instalaste **Miniconda**, abre el Anaconda Prompt (o terminal) y ejecuta:
        ```bash
        conda install jupyterlab notebook
        ```
    *   Para iniciar JupyterLab, abre el Anaconda Prompt (o terminal), navega hasta el directorio donde quieres guardar tus notebooks (`cd ruta/a/tu/carpeta`) y ejecuta:
        ```bash
        jupyter lab
        ```
        Esto abrirá una nueva pestaña en tu navegador web con la interfaz de JupyterLab.
    *   Para iniciar el clásico Jupyter Notebook, ejecuta `jupyter notebook` en su lugar.

**¿Cuándo usar cuál?**

*   **Jupyter:** Ideal para análisis exploratorio, visualización, prototipado rápido de modelos, y documentación interactiva. Piensa en ello como tu "cuaderno de laboratorio digital".
*   **VS Code:** Mejor para escribir código reutilizable (scripts, funciones, clases), construir aplicaciones más grandes, gestionar proyectos complejos y depurar.

A lo largo del curso, utilizaremos ambas herramientas según la tarea que estemos realizando. ¡Familiarízate con ellas!
