# Módulo 0: Introducción a Git y GitHub para Control de Versiones

Mientras desarrollas tus proyectos, tu código cambiará constantemente. Añadirás nuevas características, corregirás errores, experimentarás con ideas... ¿Cómo llevas un registro de todos estos cambios? ¿Qué pasa si introduces un error y necesitas volver a una versión anterior que funcionaba? ¿Cómo colaboras con otros desarrolladores en el mismo código?

La respuesta es el **Control de Versiones**, y las herramientas estándar para ello son **Git** y **GitHub**.

**¿Qué es Git?**

*   **Git** es un **sistema de control de versiones distribuido**. Es un software que se ejecuta en tu computadora local.
*   **Función Principal:** Rastrea los cambios realizados en los archivos de tu proyecto a lo largo del tiempo. Guarda "instantáneas" (llamadas *commits*) de tu proyecto en diferentes puntos.
*   **Beneficios:**
    *   **Historial Completo:** Puedes ver quién hizo qué cambio, cuándo y por qué (si escribes buenos mensajes de commit).
    *   **Revertir Cambios:** Si algo sale mal, puedes volver fácilmente a una versión anterior estable de tu código.
    *   **Experimentación Segura (Ramas - Branches):** Puedes crear "ramas" para trabajar en nuevas características o correcciones de errores de forma aislada, sin afectar la versión principal estable (*main* o *master*). Luego, puedes fusionar (*merge*) tus cambios de nuevo en la rama principal cuando estén listos.
    *   **Trabajo Offline:** Como es distribuido, puedes hacer commits y ver el historial sin necesidad de conexión a internet.

**¿Qué es GitHub (o GitLab, Bitbucket)?**

*   **GitHub** es una **plataforma de alojamiento basada en la web para repositorios Git**. Es un servicio (en su mayoría gratuito para uso público y privado básico) que te permite almacenar tus repositorios Git en la nube.
*   **Función Principal:** Sirve como un repositorio central remoto donde puedes "empujar" (*push*) tus cambios locales (commits) y desde donde otros (o tú mismo desde otra máquina) pueden "jalar" (*pull*) esos cambios.
*   **Beneficios:**
    *   **Copia de Seguridad (Backup):** Tu código está seguro en la nube, incluso si tu disco duro falla.
    *   **Colaboración:** Facilita enormemente que varios desarrolladores trabajen en el mismo proyecto. Pueden clonar el repositorio, trabajar en ramas separadas, y proponer cambios a través de *Pull Requests*.
    *   **Portafolio:** ¡GitHub es tu portafolio como desarrollador! Los reclutadores y otros desarrolladores pueden ver tus proyectos públicos, tu actividad y la calidad de tu código.
    *   **Integración:** Se integra con muchas otras herramientas de desarrollo y despliegue.

**Conceptos Básicos de Git:**

*   **Repositorio (Repository / Repo):** Es la carpeta de tu proyecto que está siendo rastreada por Git. Contiene todos los archivos del proyecto y el historial de cambios (en una subcarpeta oculta llamada `.git`).
*   **Commit:** Una "instantánea" guardada de los cambios en tus archivos en un momento específico. Cada commit tiene un identificador único y un mensaje descriptivo.
*   **Branch (Rama):** Una línea independiente de desarrollo. La rama principal suele llamarse `main` (o `master`). Puedes crear otras ramas para trabajar en paralelo.
*   **Merge (Fusión):** Combinar los cambios de una rama en otra.
*   **Clone (Clonar):** Crear una copia local de un repositorio remoto (ej. desde GitHub).
*   **Push (Empujar):** Enviar tus commits locales a un repositorio remoto.
*   **Pull (Jalar):** Traer los cambios desde un repositorio remoto a tu repositorio local.
*   **Add (Añadir):** Marcar los archivos modificados que quieres incluir en el próximo commit (ponerlos en el "staging area").
*   **Status (Estado):** Ver qué archivos han sido modificados, cuáles están en el staging area y cuáles no están siendo rastreados por Git.

**Instalación de Git:**

*   Ve al sitio web oficial de Git: [https://git-scm.com/downloads](https://git-scm.com/downloads)
*   Descarga el instalador para tu sistema operativo (Windows, macOS, Linux) y sigue las instrucciones. Acepta las opciones por defecto si no estás seguro.
*   **Verificación:** Abre tu terminal (o Anaconda Prompt) y ejecuta `git --version`. Deberías ver la versión de Git instalada.

**Crear una Cuenta en GitHub:**

*   Ve a [https://github.com/](https://github.com/) y regístrate para obtener una cuenta gratuita.

**Flujo de Trabajo Básico (Muy Simplificado):**

1.  **Inicializar Git en tu proyecto local:** `git init` (dentro de la carpeta de tu proyecto)
2.  **Hacer cambios** en tus archivos.
3.  **Añadir los cambios al staging area:** `git add <nombre_archivo>` o `git add .` (para añadir todo)
4.  **Hacer commit de los cambios:** `git commit -m "Mensaje descriptivo del cambio"`
5.  **(Opcional - con GitHub):**
    *   Crear un repositorio nuevo en GitHub.
    *   Conectar tu repositorio local al remoto: `git remote add origin <URL_del_repo_en_GitHub>`
    *   Empujar tus commits al remoto: `git push -u origin main`

**Importancia para el Curso:**

*   **Guardar tu Progreso:** Te recomendamos encarecidamente usar Git y GitHub desde el principio para guardar tu trabajo en cada módulo y ejercicio.
*   **Construir tu Portafolio:** Al final del curso, tendrás varios proyectos en tu GitHub listos para mostrar.
*   **Buenas Prácticas:** Usar control de versiones es una habilidad esencial para cualquier desarrollador profesional.

Dedicaremos tiempo a lo largo del curso a practicar los comandos básicos de Git y a interactuar con GitHub. ¡No te preocupes si parece mucho al principio, lo aprenderemos paso a paso!

¡Con esto concluimos la configuración inicial! Estás listo/a para sumergirte en los fundamentos de Python en el Módulo 1.
