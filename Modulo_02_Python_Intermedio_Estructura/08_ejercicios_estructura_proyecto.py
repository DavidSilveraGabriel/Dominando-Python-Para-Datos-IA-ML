# Ejercicios: Módulo 2 - Estructura de un Proyecto Python Estándar

# --- Introducción ---
# Este archivo de ejercicios es diferente. No ejecutaremos código complejo,
# sino que usaremos este espacio para reflexionar sobre cómo organizarías
# un proyecto Python basándote en la lección sobre estructura de proyectos.

print("--- Ejercicio de Reflexión: Estructura de Proyecto ---")
print("Lee los comentarios y las preguntas en este archivo.")

# --- Ejercicio 1: Componentes Clave ---
# Instrucciones: Repasa mentalmente la estructura de proyecto típica mostrada
# en la lección. ¿Puedes recordar para qué sirven los siguientes archivos/directorios?
# Escribe tus respuestas como comentarios o simplemente piénsalo.

# 1. `README.md`
#    Respuesta: Describe el proyecto, cómo instalarlo, usarlo, etc. Esencial.

# 2. `requirements.txt`
#    Respuesta: Lista las dependencias externas del proyecto para `pip`.

# 3. `src/` (o el directorio del paquete principal)
#    Respuesta: Contiene el código fuente principal de la aplicación/biblioteca.

# 4. `tests/`
#    Respuesta: Contiene el código de las pruebas (unitarias, integración, etc.).

# 5. `.gitignore`
#    Respuesta: Indica a Git qué archivos/carpetas ignorar (no incluir en el repositorio).

print("\n--- Ejercicio 2: Escenario - Calculadora Simple ---")
print("Imagina que estás creando un proyecto para una calculadora simple.")
print("El proyecto tendrá:")
print("- El código principal de la calculadora (ej. en un módulo `operaciones.py`).")
print("- Pruebas para las operaciones (ej. en `test_operaciones.py`).")
print("- Un archivo README explicando cómo usarla.")
print("- Una dependencia externa (hipotética) listada en `requirements.txt`.")
print("- Tu paquete principal se llamará `calculadora_simple`.")

# Pregunta: ¿Dónde colocarías los siguientes archivos dentro de la estructura estándar?
# (Considera la opción de usar un directorio `src/`)

# 1. `README.md`
#    Ubicación Sugerida: En la raíz del proyecto (`nombre_del_proyecto/README.md`).

# 2. `requirements.txt`
#    Ubicación Sugerida: En la raíz del proyecto (`nombre_del_proyecto/requirements.txt`).

# 3. El paquete `calculadora_simple` (que contiene `__init__.py` y `operaciones.py`)
#    Ubicación Sugerida (Opción 1 - con src): `nombre_del_proyecto/src/calculadora_simple/`
#    Ubicación Sugerida (Opción 2 - sin src): `nombre_del_proyecto/calculadora_simple/`

# 4. `test_operaciones.py`
#    Ubicación Sugerida: Dentro del directorio `tests/` (`nombre_del_proyecto/tests/test_operaciones.py`).

print("\nReflexiona sobre las ubicaciones sugeridas. ¿Coinciden con lo que pensaste?")


# --- Ejercicio 3: Ventajas del Layout `src/` ---
# Pregunta: ¿Cuál es la principal ventaja mencionada en la lección para usar
# un directorio `src/` en lugar de poner tu paquete directamente en la raíz?

# Respuesta Sugerida:
# Ayuda a separar claramente el código fuente instalable de otros archivos del proyecto
# (como tests, scripts, configuración). También previene problemas de importación
# accidentales que pueden ocurrir si tienes archivos con el mismo nombre en la raíz
# y dentro de tu paquete, especialmente durante el desarrollo y las pruebas.

print("\n--- Ejercicio 4: Adaptación ---")
print("Recuerda que la estructura es una guía, no una regla inflexible.")
print("Para un script muy simple de un solo archivo, probablemente no necesites")
print("toda esta estructura. Sin embargo, adoptarla temprano para proyectos")
print("que esperas que crezcan puede ahorrarte tiempo y esfuerzo a largo plazo.")

# --- Fin de los ejercicios ---
print("\n¡Buen trabajo reflexionando sobre la estructura de proyectos!")
print("Mantener tus proyectos organizados es una habilidad clave.")
