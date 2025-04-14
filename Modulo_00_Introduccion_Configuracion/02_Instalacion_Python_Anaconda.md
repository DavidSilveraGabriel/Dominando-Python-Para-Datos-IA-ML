# Módulo 0: Instalación de Python y Anaconda/Miniconda

Para empezar a escribir y ejecutar código Python, necesitas tener Python instalado en tu sistema. Además, para facilitar la gestión de las librerías que usaremos en Ciencia de Datos, IA y ML, **recomendamos encarecidamente usar la distribución Anaconda o su versión más ligera, Miniconda.**

**¿Por qué Anaconda/Miniconda?**

*   **Incluye Python:** Vienen con una versión de Python lista para usar.
*   **Gestor de Paquetes (`conda`):** `conda` es una herramienta poderosa para instalar, actualizar y gestionar librerías (paquetes) de Python y otros lenguajes. Es especialmente bueno manejando dependencias complejas, comunes en el ecosistema científico.
*   **Gestor de Entornos:** `conda` permite crear entornos virtuales aislados. Esto es **fundamental** para evitar conflictos entre las dependencias de diferentes proyectos. Cada proyecto puede tener su propio conjunto de librerías y versiones específicas.
*   **Anaconda vs. Miniconda:**
    *   **Anaconda:** Es una distribución completa que incluye Python, `conda`, y cientos de las librerías científicas más populares preinstaladas (NumPy, Pandas, Matplotlib, Scikit-learn, Jupyter, etc.). Es ideal si tienes espacio en disco y quieres tener todo listo desde el principio.
    *   **Miniconda:** Es una versión mínima que solo incluye Python, `conda` y sus dependencias básicas. Tú instalas manualmente las librerías que necesitas. Es ideal si prefieres una instalación más ligera y controlar exactamente qué paquetes se instalan.

**Recomendación para este curso:** Puedes usar cualquiera de las dos. Si eres principiante y tienes espacio, **Anaconda** puede ser más sencillo al inicio. Si prefieres control total o tienes espacio limitado, **Miniconda** es excelente (solo tendrás que instalar las librerías a medida que las necesitemos usando `conda install <nombre_libreria>`).

**Pasos de Instalación (Ejemplo con Anaconda en Windows):**

1.  **Descarga:** Ve al sitio web oficial de Anaconda: [https://www.anaconda.com/download](https://www.anaconda.com/download)
2.  **Selecciona tu Sistema Operativo:** Elige el instalador para Windows (asegúrate de elegir la versión de 64-bit si tu sistema lo es, que es lo más común hoy en día). Descarga la versión más reciente de Python 3.x.
3.  **Ejecuta el Instalador:** Haz doble clic en el archivo descargado `.exe`.
4.  **Sigue las Instrucciones:**
    *   Acepta la licencia.
    *   Elige el tipo de instalación: "Just Me" (Recomendado) o "All Users".
    *   **Directorio de Instalación:** Puedes dejar el directorio por defecto (usualmente en tu carpeta de usuario) o elegir otro. **¡Recuerda esta ruta!**
    *   **Opciones Avanzadas (Importante):**
        *   **"Add Anaconda3 to my PATH environment variable" (Añadir Anaconda3 a mi variable de entorno PATH):** El instalador **NO recomienda** marcar esta opción directamente. La forma recomendada de usar Anaconda es a través del **Anaconda Prompt** (o Anaconda Powershell Prompt) que se instalará en tu menú de inicio. Si marcas esta opción, puede interferir con otras instalaciones de Python que tengas. **Es mejor NO marcarla.**
        *   **"Register Anaconda3 as my default Python 3.x":** Esta opción sí es recomendable marcarla si no tienes otra instalación de Python que quieras mantener como predeterminada.
5.  **Completa la Instalación:** Haz clic en "Install" y espera a que termine el proceso. Puede tardar unos minutos.
6.  **Verificación (Opcional pero Recomendado):**
    *   Abre el **"Anaconda Prompt"** desde el menú de inicio de Windows.
    *   Escribe `python --version` y presiona Enter. Deberías ver la versión de Python que instalaste.
    *   Escribe `conda --version` y presiona Enter. Deberías ver la versión de conda.
    *   Escribe `conda list` y presiona Enter. Verás una larga lista de los paquetes preinstalados si usaste Anaconda.

**Instalación en macOS y Linux:**

*   El proceso es similar. Descarga el instalador `.pkg` (macOS) o `.sh` (Linux) desde el sitio de Anaconda.
*   **macOS:** Ejecuta el `.pkg` y sigue las instrucciones gráficas.
*   **Linux:** Abre una terminal, navega al directorio donde descargaste el archivo `.sh` y ejecútalo con `bash Anaconda3-XXXX.XX-Linux-x86_64.sh` (reemplaza XXXX.XX con la versión descargada). Sigue las instrucciones en la terminal (lee cuidadosamente, acepta la licencia, confirma la ruta de instalación y **responde "yes"** cuando pregunte si quieres que el instalador inicialice Anaconda3 ejecutando `conda init`). Después de la instalación, cierra y vuelve a abrir tu terminal para que los cambios surtan efecto.
*   La verificación se hace igual desde la terminal (`python --version`, `conda --version`).

**Si eliges Miniconda:**

*   El proceso de instalación es idéntico, pero descarga el instalador desde la página de Miniconda: [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
*   Después de instalar, tendrás que instalar las librerías manualmente usando el Anaconda Prompt (o terminal en macOS/Linux) con comandos como:
    *   `conda install numpy pandas matplotlib seaborn scikit-learn jupyterlab`

¡Listo! Con Python y conda instalados, estás preparado/a para configurar tu entorno de desarrollo y empezar a programar.
