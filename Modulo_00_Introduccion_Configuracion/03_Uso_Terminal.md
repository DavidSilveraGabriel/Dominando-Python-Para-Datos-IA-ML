# Módulo 0: Uso Básico de la Terminal / Línea de Comandos

La terminal (también llamada línea de comandos, consola, shell, o prompt) es una interfaz basada en texto que te permite interactuar directamente con el sistema operativo de tu computadora. Aunque al principio pueda parecer intimidante, es una herramienta **fundamental** para cualquier desarrollador, especialmente en el mundo de Python y la Ciencia de Datos.

**¿Por qué es importante?**

*   **Ejecutar Comandos:** Usaremos la terminal para ejecutar comandos de `conda` (gestión de paquetes y entornos), `git` (control de versiones), `python` (ejecutar scripts), y otras herramientas.
*   **Navegación:** Te permite moverte entre carpetas (directorios) de tu sistema.
*   **Gestión de Archivos:** Puedes crear, mover, copiar y eliminar archivos y carpetas.
*   **Automatización:** Permite escribir scripts para automatizar tareas repetitivas.

**Terminal a Usar:**

*   **Windows:** Utilizaremos principalmente el **"Anaconda Prompt"** (o "Anaconda Powershell Prompt") que se instaló con Anaconda/Miniconda. Estos prompts ya tienen el entorno de `conda` configurado correctamente.
*   **macOS:** Usarás la aplicación **"Terminal"** que viene preinstalada (puedes encontrarla en Aplicaciones > Utilidades).
*   **Linux:** Usarás la **terminal** predeterminada de tu distribución (Gnome Terminal, Konsole, xterm, etc.).

**Conceptos y Comandos Básicos:**

1.  **Prompt:** Es el texto que aparece indicando que la terminal está lista para recibir un comando. Suele mostrar tu usuario, el nombre de la máquina y el directorio actual. Ejemplo en Windows (Anaconda Prompt): `(base) C:\Users\TuUsuario>`
    *   `(base)` indica el entorno `conda` activo actualmente.
    *   `C:\Users\TuUsuario>` es la ruta del directorio actual (tu carpeta de usuario en este caso).

2.  **Comandos:** Son las instrucciones que le das a la terminal. Se escriben y se ejecutan presionando `Enter`.

3.  **Navegación de Directorios:**
    *   `pwd` (Print Working Directory - macOS/Linux) / `cd` (sin argumentos - Windows): Muestra la ruta completa del directorio actual en el que te encuentras.
    *   `ls` (List - macOS/Linux) / `dir` (Directory - Windows): Lista los archivos y carpetas dentro del directorio actual.
    *   `cd <nombre_directorio>` (Change Directory): Cambia al directorio especificado. Ejemplo: `cd Documentos`
    *   `cd ..`: Sube un nivel en la jerarquía de directorios (va al directorio padre).
    *   `cd ~` (macOS/Linux) / `cd %USERPROFILE%` (Windows): Va directamente a tu directorio "home" o de usuario.
    *   `cd /` (macOS/Linux) / `cd C:\` (Windows): Va al directorio raíz del sistema.
    *   **Autocompletado:** ¡Usa la tecla `Tab`! Empieza a escribir el nombre de un archivo o directorio y presiona `Tab`. La terminal intentará autocompletar el nombre. Si hay varias opciones, presiona `Tab` dos veces para verlas. ¡Esto ahorra mucho tiempo y evita errores de tipeo!

4.  **Crear Directorios:**
    *   `mkdir <nombre_nuevo_directorio>` (Make Directory): Crea una nueva carpeta. Ejemplo: `mkdir MiProyectoPython`

5.  **Ejecutar Scripts de Python:**
    *   `python <nombre_del_script.py>`: Ejecuta un archivo de Python. Asegúrate de estar en el directorio donde se encuentra el script o proporciona la ruta completa al archivo.

6.  **Limpiar la Pantalla:**
    *   `clear` (macOS/Linux) / `cls` (Windows): Limpia la pantalla de la terminal.

**Ejemplo Práctico (Windows - Anaconda Prompt):**

```bash
# Ver dónde estoy
(base) C:\Users\TuUsuario> cd

# Listar contenido de mi carpeta de usuario
(base) C:\Users\TuUsuario> dir

# Ir al Escritorio (Desktop)
(base) C:\Users\TuUsuario> cd Desktop

# Crear una carpeta para el curso
(base) C:\Users\TuUsuario\Desktop> mkdir CursoPythonDS

# Entrar a la nueva carpeta
(base) C:\Users\TuUsuario\Desktop> cd CursoPythonDS

# Verificar que estoy dentro
(base) C:\Users\TuUsuario\Desktop\CursoPythonDS> cd

# Volver a mi carpeta de usuario
(base) C:\Users\TuUsuario\Desktop\CursoPythonDS> cd ..
(base) C:\Users\TuUsuario\Desktop> cd ..
(base) C:\Users\TuUsuario> cd

# Limpiar la pantalla
(base) C:\Users\TuUsuario> cls
```

**¡Practica!**

La mejor forma de familiarizarse con la terminal es usándola. Intenta navegar por tus carpetas, listar archivos y crear directorios de prueba. No tengas miedo de experimentar (¡pero ten cuidado con comandos como `rm` o `del` que borran archivos!).

Dominar estos comandos básicos te dará una base sólida para seguir las instrucciones del curso y trabajar de manera más eficiente.
