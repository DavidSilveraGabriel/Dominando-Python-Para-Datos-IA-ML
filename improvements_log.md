# Registro de Mejoras del Curso de Python

Este documento sirve como un "banco de memoria" para registrar ideas de mejora, planificaciones y el seguimiento de las implementaciones en el curso.

---

## 1. Mejoras Planificadas

### Módulo 0: Introducción y Configuración

#### Contenido (`.md` files)
*   **00_Bienvenida_Objetivos.md:**
    *   [ ] Añadir una sección "Cómo sacar el máximo provecho del curso" (ej. practicar, preguntar, construir).
*   **01_Por_Que_Python.md:**
    *   [ ] Incluir un pequeño gráfico o infografía que compare Python con otros lenguajes en DS/ML (ej. R, Julia).
*   **02_Instalacion_Python_Anaconda.md:**
    *   [ ] Añadir una sección de "Troubleshooting" para problemas comunes de instalación.
    *   [ ] Considerar un video corto de instalación para cada OS.
*   **03_Uso_Terminal.md:**
    *   [ ] Añadir un mini-ejercicio interactivo donde el alumno deba ejecutar comandos básicos.
*   **04_Introduccion_IDEs.md:**
    *   [ ] Enlazar a recursos externos para configuración inicial de VS Code (extensiones recomendadas, atajos).
*   **05_Entornos_Virtuales.md:**
    *   [ ] Diagrama de flujo más interactivo sobre el ciclo de vida de un entorno virtual (crear, activar, instalar, desactivar, eliminar).
*   **06_Introduccion_Git_GitHub.md:**
    *   [ ] Añadir un ejercicio guiado para el primer commit y push a un repositorio de GitHub.

#### Diseño y Estructura (Diapositivas HTML & CSS)
*   **General:**
    *   [ ] Implementar un sistema de navegación entre diapositivas (flechas, barra de progreso).
    *   [ ] Revisar y refactorizar `style.css` para consolidar estilos redundantes y mejorar la modularidad.
    *   [ ] Ajustar el diseño de las diapositivas para ser más responsivo en diferentes tamaños de pantalla (uso de `vw`/`vh`, media queries).
    *   [ ] Estandarizar la gestión de fuentes en `style.css` para evitar overrides excesivos.
    *   [ ] Añadir animaciones sutiles a elementos clave al cargar la diapositiva o al interactuar.
*   **Específico por diapositiva (ejemplos):**
    *   **1.html (Bienvenida):**
        *   [ ] Mejorar la animación del icono de Python.
        *   [ ] Considerar un carrusel o animación para los "Objetivos Clave".
    *   **2.html (Por Qué Python):**
        *   [ ] Hacer las "burbujas" de librerías interactivas (ej. hover para ver descripción corta).
    *   **3.html (Instalación):**
        *   [ ] Mejorar la visualización de los pasos de instalación, quizás con un diagrama de flujo animado.
    *   **4.html (Terminal):**
        *   [ ] Simulación de terminal más interactiva donde el alumno pueda "escribir" comandos.
    *   **5.html (IDEs):**
        *   [ ] Añadir un "tour" visual rápido de VS Code y JupyterLab (capturas de pantalla anotadas o GIFs).
    *   **6.html (Entornos Virtuales):**
        *   [ ] Visualización interactiva del aislamiento de entornos (ej. dos "burbujas" de proyectos con diferentes versiones de librerías).
    *   **7.html (Git/GitHub):**
        *   [ ] Diagrama de flujo de Git más dinámico/animado.
        *   [ ] Integrar un widget de GitHub (si es posible y seguro) para mostrar un repositorio de ejemplo.

---

## 2. Mejoras Implementadas

*   **2025-06-09 - Sistema de navegación entre diapositivas (flechas, barra de progreso):** `Modulo_00_Introduccion_Configuracion/diapositivas/1.html`, `scripts/script.js`, `styles/style.css`
    *   Se añadió la estructura HTML para las flechas de navegación y la barra de progreso en `1.html`.
    *   Se creó `scripts/script.js` con la lógica JavaScript para la navegación y actualización de la barra de progreso.
    *   Se añadieron estilos CSS para las flechas y la barra de progreso en `styles/style.css`.

---

## 3. Feedback y Notas

*   **[Fecha] - [Fuente]:** [Detalle del feedback]
    *   Acciones tomadas o consideraciones.
