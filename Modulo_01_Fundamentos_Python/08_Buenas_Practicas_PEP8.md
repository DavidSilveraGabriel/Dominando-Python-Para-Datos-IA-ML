# Módulo 1: Buenas Prácticas Iniciales y PEP 8

¡Felicidades por llegar hasta aquí! Ya conoces los bloques de construcción fundamentales de Python. Ahora, hablemos de cómo escribir código no solo funcional, sino también **limpio, legible y mantenible**. Esto es crucial para tu propio entendimiento futuro y para colaborar con otros.

La comunidad Python valora mucho la legibilidad del código. Existe una guía de estilo oficial llamada **PEP 8** (Python Enhancement Proposal 8) que describe las convenciones recomendadas para escribir código Python. Seguir PEP 8 hace que el código sea más consistente y fácil de leer para cualquier programador Python.

Puedes encontrar la guía completa aquí: [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)

No necesitas memorizarla toda de golpe, pero es importante conocer y aplicar los puntos clave desde el principio. Herramientas como los linters (que veremos más adelante) pueden ayudarte a verificar si tu código cumple con PEP 8.

## Puntos Clave de PEP 8 para Empezar:

1.  **Sangría (Indentation):**
    *   Usa **4 espacios** por nivel de sangría. ¡No uses tabulaciones ni mezcles tabulaciones y espacios! Configura tu editor para que inserte espacios al presionar Tab. Ya vimos lo crucial que es la sangría para la estructura del código.

2.  **Longitud Máxima de Línea:**
    *   Limita todas las líneas a un máximo de **79 caracteres**.
    *   Para líneas largas, puedes dividirlas usando paréntesis `()`, corchetes `[]`, llaves `{}` o la barra invertida `\` (esta última con menos frecuencia). La sangría de continuación ayuda a la legibilidad.
    ```python
    # Ejemplo de línea larga dividida
    def funcion_con_muchos_parametros(param1, param2, param3, param4,
                                      param5, param6):
        print("Llamada con muchos parámetros")

    resultado_largo = (variable1 + variable2 + variable3
                       - variable4 * variable5)
    ```

3.  **Líneas en Blanco:**
    *   Usa líneas en blanco para separar bloques lógicos de código y mejorar la legibilidad.
    *   Separa las definiciones de funciones y clases de nivel superior con **dos** líneas en blanco.
    *   Separa las definiciones de métodos dentro de una clase con **una** línea en blanco.
    *   Usa líneas en blanco con moderación dentro de las funciones para separar pasos lógicos.

4.  **Importaciones (`import`):**
    *   Las importaciones deben ir siempre al **principio del archivo**, justo después de los comentarios del módulo y docstrings, y antes de las variables globales y definiciones.
    *   Importa **un módulo por línea**.
        ```python
        # Correcto:
        import os
        import sys

        # Incorrecto:
        # import os, sys
        ```
    *   Agrupa las importaciones en este orden, separadas por una línea en blanco:
        1.  Importaciones de la biblioteca estándar (ej. `os`, `sys`, `math`).
        2.  Importaciones de terceros relacionados (ej. `numpy`, `pandas`, `flask`).
        3.  Importaciones de tu propia aplicación/biblioteca local.

5.  **Espacios en Blanco en Expresiones y Declaraciones:**
    *   **Evita espacios innecesarios:** justo dentro de paréntesis/corchetes/llaves, antes de una coma.
    *   **Usa espacios alrededor de operadores:** asignación (`=`), comparación (`==`, `!=`, `>`, `<`), aritméticos (`+`, `-`, `*`, `/`), lógicos (`and`, `or`), etc. (Excepto alrededor de `**`).
        ```python
        # Correcto:
        x = 5
        y = x + 2
        if x > y and x != 0:
            mi_lista[1] = z * 3

        # Incorrecto:
        # x=5
        # y = x+2
        # if x>y and x!=0 :
        #     mi_lista [ 1 ] = z*3
        ```
    *   Usa un espacio después de la coma (`,`) en listas, tuplas, diccionarios, argumentos de funciones.

6.  **Nombres (Naming Conventions):** (Ya lo mencionamos, pero reforzamos)
    *   `snake_case`: Para variables, funciones y métodos (minúsculas con guion bajo). Ej: `mi_variable`, `calcular_total()`.
    *   `CapWords` o `PascalCase`: Para clases. Ej: `MiClase`, `CalculadoraDeImpuestos`.
    *   `UPPERCASE_SNAKE_CASE`: Para constantes. Ej: `PI = 3.14159`, `TASA_MAXIMA`.
    *   Nombres descriptivos y evitar abreviaturas ambiguas.

7.  **Comentarios:**
    *   Escribe comentarios claros y concisos que expliquen el *por qué* o el *cómo* de un código complejo, no el *qué* (si el código es legible, el qué debería ser obvio).
    *   Mantén los comentarios actualizados si cambias el código.
    *   Usa comentarios de bloque (`#`) para explicar secciones y comentarios en línea (`#`) con moderación para aclarar líneas específicas.
    *   Usa **Docstrings** (`"""Docstring"""`) para documentar funciones, clases y módulos (explicar su propósito, parámetros, etc.).

**¿Por qué seguir estas prácticas?**

*   **Legibilidad:** Otros (¡y tu yo futuro!) podrán entender tu código más fácilmente.
*   **Mantenibilidad:** Es más fácil encontrar errores y modificar código bien formateado.
*   **Colaboración:** Permite que los equipos trabajen juntos de manera más eficiente usando un estilo consistente.
*   **Profesionalismo:** Demuestra atención al detalle y buenas prácticas de ingeniería de software.

**Conclusión del Módulo 1:**

Has aprendido los fundamentos esenciales de Python: sintaxis, variables, tipos de datos, operadores, estructuras de datos básicas, control de flujo (condicionales y bucles), funciones, manejo básico de errores y la importancia de escribir código limpio siguiendo PEP 8.

¡Estás listo/a para pasar al siguiente nivel en el Módulo 2, donde exploraremos conceptos más intermedios como la Programación Orientada a Objetos!
