# Ejercicios: Módulo 7 - Ética en la IA

# --- Prerrequisitos ---
# No se requiere código específico, es un ejercicio conceptual y de reflexión.

print("--- Reflexiones sobre Ética en la IA ---")

# --- Ejercicio 1: Identificar Preocupaciones Éticas ---
# Instrucciones:
# Para cada uno de los siguientes escenarios hipotéticos de IA, identifica al menos
# una preocupación ética principal que podría surgir. Explica brevemente por qué.

# Escenario A: Un sistema de IA utilizado por una empresa para filtrar currículums y seleccionar candidatos para entrevistas de trabajo. El sistema fue entrenado con datos históricos de contrataciones de la empresa.
# Preocupación Ética Principal: Sesgo (Bias) y Discriminación.
# Explicación: Si los datos históricos reflejan sesgos pasados en la contratación (ej. preferencia por ciertos grupos demográficos, universidades, etc.), la IA aprenderá y perpetuará esos sesgos, discriminando injustamente a candidatos cualificados de grupos subrepresentados. Falta de transparencia en por qué se rechaza a un candidato.

# Escenario B: Un sistema de reconocimiento facial implementado en cámaras de seguridad públicas para identificar personas de interés buscadas por la policía.
# Preocupación Ética Principal: Privacidad, Vigilancia Masiva, Potencial de Error y Falsos Positivos.
# Explicación: La vigilancia constante invade la privacidad de los ciudadanos. Los errores en el reconocimiento (especialmente en ciertos grupos demográficos donde los sistemas suelen ser menos precisos) pueden llevar a identificaciones erróneas y acusaciones injustas. El potencial de abuso por parte de las autoridades es alto.

# Escenario C: Un chatbot de IA diseñado para ofrecer apoyo emocional básico y conversación a personas que se sienten solas.
# Preocupación Ética Principal: Seguridad Emocional, Dependencia, Falta de Empatía Real, Privacidad de Datos Sensibles.
# Explicación: ¿Puede la IA realmente reemplazar la conexión humana? ¿Qué pasa si da un consejo perjudicial? ¿Cómo maneja situaciones de crisis? Los usuarios podrían volverse dependientes o compartir información muy personal que podría ser vulnerable si no se maneja con extrema seguridad y privacidad.

# Escenario D: Vehículos autónomos que deben tomar decisiones en fracciones de segundo en situaciones de accidente inevitables (ej. el "dilema del tranvía").
# Preocupación Ética Principal: Toma de Decisiones Morales, Responsabilidad (Accountability).
# Explicación: ¿Cómo se programa la "moralidad" en una máquina? ¿Debe priorizar la vida de los ocupantes, la de los peatones, minimizar el número total de víctimas? ¿Quién es responsable en caso de un accidente causado por una decisión algorítmica (el fabricante, el programador, el propietario)?

# Escenario E: Un sistema de IA que genera automáticamente artículos de noticias basados en comunicados de prensa y datos financieros.
# Preocupación Ética Principal: Desinformación (Disinformation), Pérdida de Empleos, Calidad y Veracidad.
# Explicación: La IA podría generar noticias sesgadas, incompletas o incluso falsas si no se supervisa adecuadamente o si los datos de entrada son defectuosos. Podría desplazar a periodistas humanos. La falta de juicio editorial humano podría llevar a la difusión de información engañosa.

print("Ejercicio 1: Identificar Preocupaciones Éticas - Ver comentarios.")
print("-" * 20)


# --- Ejercicio 2: Principios Éticos Fundamentales ---
# Instrucciones:
# La lección mencionó varios principios éticos clave para el desarrollo de IA. Elige tres de ellos y explica brevemente por qué son importantes.

# Principios Comunes (puedes elegir otros si se mencionaron):
# - Justicia y Equidad (Fairness)
# - Transparencia y Explicabilidad (Transparency & Explainability)
# - Responsabilidad y Rendición de Cuentas (Accountability)
# - Privacidad (Privacy)
# - Seguridad y Fiabilidad (Safety & Reliability)
# - Beneficio Social / No Maleficencia (Social Benefit / Non-maleficence)

# Ejemplo de Respuesta:
# 1. Justicia y Equidad (Fairness):
#    Importancia: Es crucial para evitar que los sistemas de IA discriminen o traten injustamente a ciertos individuos o grupos, especialmente aquellos históricamente marginados. Busca mitigar y corregir sesgos en los datos y algoritmos.
# 2. Transparencia y Explicabilidad:
#    Importancia: Permite entender cómo un sistema de IA llega a una decisión o predicción. Es vital para la confianza del usuario, la depuración de errores, la identificación de sesgos y para poder auditar y cuestionar los resultados, especialmente en aplicaciones de alto riesgo (médicas, legales, financieras).
# 3. Responsabilidad (Accountability):
#    Importancia: Establece quién es responsable cuando un sistema de IA causa daño o comete errores. Implica tener mecanismos claros para la supervisión, la auditoría y la corrección de problemas, asegurando que haya líneas claras de responsabilidad humana en el ciclo de vida de la IA.

print("\nEjercicio 2: Principios Éticos Fundamentales - Ver ejemplo en comentarios.")
print("-" * 20)


# --- Ejercicio 3: El Rol del Desarrollador ---
# Instrucciones:
# Reflexiona sobre el papel que juega un desarrollador o científico de datos en la promoción de una IA ética. Menciona al menos dos acciones concretas que pueden tomar.

# Respuesta Sugerida:
# El desarrollador tiene un rol fundamental en la construcción de sistemas éticos. Algunas acciones incluyen:
# 1. Selección y Auditoría de Datos: Ser consciente de los posibles sesgos en los datos de entrenamiento y tomar medidas para mitigarlos (ej. re-muestreo, aumento de datos, uso de métricas de equidad). Cuestionar el origen y la representatividad de los datos.
# 2. Elección de Métricas y Evaluación Rigurosa: No basarse únicamente en la accuracy, especialmente en datasets desbalanceados. Utilizar métricas de equidad (fairness metrics) además de las métricas de rendimiento estándar. Evaluar el modelo en diferentes subgrupos demográficos para detectar disparidades.
# 3. Diseño y Transparencia: Cuando sea posible, elegir modelos más interpretables o utilizar técnicas de explicabilidad (XAI) para entender las decisiones del modelo. Documentar claramente el funcionamiento, las limitaciones y los riesgos potenciales del sistema.
# 4. Consideración del Impacto: Pensar activamente en las posibles consecuencias sociales y éticas del sistema que se está construyendo y plantear preocupaciones si es necesario. Abogar por pruebas rigurosas y mecanismos de supervisión humana.

print("\nEjercicio 3: El Rol del Desarrollador - Ver comentarios.")
print("-" * 20)

print("\nLa ética es una consideración fundamental y continua en el desarrollo y despliegue de la IA.")

# --- Fin de los ejercicios ---
