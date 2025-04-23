# Ejercicios: Módulo 6 - Flujo de Trabajo de un Proyecto de Machine Learning

# --- Prerrequisitos ---
# No se requiere código ejecutable específico para este archivo.
# Es un resumen conceptual del flujo de trabajo.

print("--- Repaso del Flujo de Trabajo de ML ---")

# --- Ejercicio 1: Ordenar los Pasos del Flujo de Trabajo ---
# Instrucciones:
# A continuación se listan los pasos principales de un proyecto de ML en desorden.
# Ordénalos según el flujo típico visto en la lección. Escribe el orden correcto
# como un comentario (ej. B, A, D, C...).

# Pasos Desordenados:
# A. División de Datos (Train/Test/Validación)
# B. Adquisición de Datos
# C. Ajuste de Hiperparámetros
# D. Despliegue y Monitorización
# E. Selección y Entrenamiento del Modelo
# F. Definición del Problema y Objetivos
# G. Análisis Exploratorio de Datos (EDA) y Preprocesamiento
# H. Evaluación del Modelo
# I. Selección e Ingeniería de Características (Feature Engineering)

# Orden Correcto Sugerido:
# F, B, G, I, A, E, H, C, D
# (F. Definición -> B. Adquisición -> G. EDA/Preproc -> I. Features -> A. División ->
#  E. Entrenamiento -> H. Evaluación -> C. Ajuste Hiperparám. -> D. Despliegue)
# Nota: Este orden es típico, pero el proceso es iterativo. Por ejemplo,
# la evaluación (H) puede llevar a redefinir características (I) o elegir otro modelo (E).
# El ajuste (C) a menudo se hace antes de la evaluación final en el test set, usando validación cruzada.

print("Ejercicio 1: Ordenar Pasos - Ver comentarios en el código.")
print("-" * 20)


# --- Ejercicio 2: Reflexión sobre los Pasos ---
# Instrucciones:
# Para cada uno de los siguientes puntos, reflexiona brevemente (en comentarios)
# por qué es importante dentro del flujo de trabajo de ML.

# Punto 1: ¿Por qué es crucial la Definición del Problema y Objetivos (Paso F)?
# Respuesta 1: Define el propósito del proyecto, qué se quiere lograr y cómo se medirá el éxito.
#             Sin un objetivo claro, es imposible saber si el modelo final es útil o exitoso.
#             Guía todas las decisiones posteriores (qué datos recoger, qué modelo usar, qué métrica optimizar).

# Punto 2: ¿Por qué se realiza el EDA y Preprocesamiento (Paso G) antes de entrenar modelos?
# Respuesta 2: Para entender los datos (distribuciones, relaciones, outliers, valores faltantes),
#             limpiarlos (manejar NaN, duplicados) y transformarlos a un formato adecuado
#             para los algoritmos de ML (escalado numérico, codificación categórica).
#             Entrenar con datos "sucios" o mal formateados lleva a modelos poco fiables o erróneos.

# Punto 3: ¿Cuál es el propósito principal de dividir los datos (Paso A)?
# Respuesta 3: Obtener una evaluación imparcial del rendimiento del modelo en datos no vistos.
#             Evita el sobreajuste (overfitting) al no evaluar el modelo con los mismos datos
#             con los que aprendió. Permite estimar cómo generalizará el modelo a situaciones reales.

# Punto 4: ¿Por qué la Evaluación del Modelo (Paso H) no es el último paso antes del despliegue?
# Respuesta 4: Porque la evaluación inicial puede revelar que el modelo no cumple los objetivos
#             o que se puede mejorar. Esto puede llevar a iteraciones: probar otros modelos (E),
#             ajustar hiperparámetros (C), o incluso volver a la ingeniería de características (I)
#             o al preprocesamiento (G). La evaluación guía las mejoras. El ajuste de hiperparámetros (C)
#             suele hacerse después de una evaluación inicial para optimizar el modelo elegido.

# Punto 5: ¿Por qué es importante la Monitorización (parte del Paso D) después del despliegue?
# Respuesta 5: Porque el rendimiento del modelo puede degradarse con el tiempo a medida que
#             cambian los patrones en los datos del mundo real ("data drift" o "concept drift").
#             La monitorización permite detectar esta degradación y decidir cuándo es necesario
#             reentrenar o actualizar el modelo para mantener su efectividad.

print("\nEjercicio 2: Reflexión sobre Pasos - Ver comentarios en el código.")
print("-" * 20)


# --- Ejercicio 3: Aplicando el Flujo (Conceptual) ---
# Instrucciones:
# Imagina que te dan un nuevo proyecto: "Predecir si un cliente abandonará
# (churn) un servicio de suscripción en los próximos 3 meses, basándose en
# su historial de uso, datos demográficos y tickets de soporte."
# Describe brevemente (1-2 frases por punto) qué harías en los siguientes pasos
# del flujo de trabajo:

# a) Definición del Problema y Objetivos:
#    - Problema: Clasificación binaria (Churn / No Churn).
#    - Objetivo: Predecir con alta precisión y/o recall (dependiendo del coste de perder un cliente vs. intervenir innecesariamente) qué clientes tienen riesgo de abandono.
#    - Métrica: F1-score, Recall, Precision, AUC (dependiendo del balance de clases y objetivos de negocio).

# b) Adquisición de Datos:
#    - Recopilar datos de uso (frecuencia login, funciones usadas), demográficos (edad, ubicación si disponible), historial de soporte (nº tickets, tiempo resolución) y estado de churn pasado.
#    - Unir las diferentes fuentes de datos por ID de cliente.

# c) EDA y Preprocesamiento:
#    - Analizar distribuciones (ej. nº tickets), buscar valores faltantes (ej. en demografía), visualizar relaciones (ej. uso vs churn).
#    - Codificar variables categóricas (ej. ubicación), escalar numéricas (ej. frecuencia login), manejar NaN.

# d) División de Datos:
#    - Separar X (features de uso, demografía, soporte) de y (churn sí/no).
#    - Dividir en train/test (ej. 80/20) usando `train_test_split`, probablemente con `stratify=y` debido a que el churn suele ser desbalanceado.

# e) Selección y Entrenamiento del Modelo:
#    - Probar modelos de clasificación como LogisticRegression, RandomForestClassifier, GradientBoostingClassifier.
#    - Entrenar cada modelo con `X_train` (preprocesado) y `y_train`.

# f) Evaluación del Modelo:
#    - Predecir en `X_test` (preprocesado).
#    - Calcular métricas (Accuracy, Precision, Recall, F1, Matriz de Confusión) comparando `y_pred` con `y_test`.
#    - Analizar qué modelo funciona mejor según la métrica objetivo definida en (a).

print("\nEjercicio 3: Aplicando el Flujo (Conceptual) - Ver comentarios en el código.")
print("-" * 20)

print("\nEste módulo ha cubierto los fundamentos de Scikit-learn y el flujo de trabajo de ML.")
print("¡La práctica continua es clave para dominar estos conceptos!")

# --- Fin de los ejercicios ---
