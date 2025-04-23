# Ejercicios: Módulo 9 - Otras Opciones de Despliegue

print("--- Otras Opciones de Despliegue (Conceptual) ---")

# --- Ejercicio 1: Identificar Tipos de Despliegue ---
# Instrucciones:
# Para cada descripción, identifica el tipo de plataforma o enfoque de despliegue
# que mejor se ajusta (ej. IaaS, PaaS, Serverless, On-Premise, Contenedores como Servicio).

# Descripción A: Alquilas máquinas virtuales (servidores) en la nube y eres responsable
#                de instalar el sistema operativo, las dependencias, configurar la red
#                y desplegar tu aplicación. Tienes control total sobre el entorno.
# Respuesta A: IaaS (Infrastructure as a Service) - Ej: AWS EC2, Google Compute Engine, Azure Virtual Machines.

# Descripción B: Una plataforma que abstrae la infraestructura subyacente. Solo necesitas
#                subir tu código (y quizás un archivo de configuración simple), y la
#                plataforma se encarga del servidor, sistema operativo, escalado básico
#                y despliegue.
# Respuesta B: PaaS (Platform as a Service) - Ej: Heroku, Google App Engine, AWS Elastic Beanstalk, PythonAnywhere.

# Descripción C: Ejecutas tu código en respuesta a eventos sin gestionar ningún servidor.
#                Pagas solo por el tiempo de cómputo consumido mientras tu código se ejecuta.
#                Ideal para tareas cortas y event-driven.
# Respuesta C: Serverless / FaaS (Function as a Service) - Ej: AWS Lambda, Google Cloud Functions, Azure Functions.

# Descripción D: Despliegas y gestionas tu aplicación en tus propios servidores físicos
#                ubicados en tus instalaciones. Tienes control total pero también toda la
#                responsabilidad del hardware y software.
# Respuesta D: On-Premise (En las instalaciones).

# Descripción E: Un servicio en la nube que gestiona la ejecución y orquestación de
#                contenedores Docker, encargándose del escalado, balanceo de carga y
#                actualizaciones de los contenedores.
# Respuesta E: Contenedores como Servicio (CaaS) / Orquestación de Contenedores - Ej: Kubernetes (EKS, GKE, AKS), AWS ECS, Google Cloud Run (modo contenedor).

print("--- Ejercicio 1: Identificar Tipos de Despliegue ---")
print("Ver comentarios en el código para las respuestas.")
print("-" * 20)


# --- Ejercicio 2: Pros y Contras ---
# Instrucciones:
# Menciona una ventaja (Pro) y una desventaja (Contra) principal para cada uno de los
# siguientes enfoques de despliegue:

# a) IaaS (Máquinas Virtuales en la Nube):
#    - Pro: Máximo control y flexibilidad sobre el entorno (SO, software, configuración de red).
#    - Contra: Mayor responsabilidad de gestión (actualizaciones, seguridad, configuración inicial). Puede ser más complejo de configurar que PaaS.

# b) PaaS (Plataforma como Servicio):
#    - Pro: Facilidad de uso y rapidez de despliegue (abstracción de la infraestructura). Escalado automático (a menudo).
#    - Contra: Menor control sobre el entorno subyacente ("vendor lock-in" potencial), puede ser más costoso a gran escala o tener limitaciones específicas.

# c) Serverless (FaaS):
#    - Pro: Escalado automático y granular, pago por uso (potencialmente muy económico para cargas de trabajo variables), sin gestión de servidores.
#    - Contra: Limitaciones en tiempo de ejecución y recursos, "arranque en frío" (cold starts), dificultad para mantener estado entre ejecuciones, complejidad en arquitecturas complejas (orquestación de funciones).

# d) On-Premise:
#    - Pro: Control total sobre hardware y datos (puede ser necesario por regulaciones o seguridad), sin costes recurrentes de nube (pero sí de capital y mantenimiento).
#    - Contra: Alta inversión inicial (CAPEX), responsabilidad total del mantenimiento, escalado más lento y costoso, requiere personal especializado.

print("\n--- Ejercicio 2: Pros y Contras ---")
print("Ver comentarios en el código para las respuestas.")
print("-" * 20)


# --- Ejercicio 3: Elegir la Plataforma Adecuada ---
# Instrucciones:
# Para cada escenario, sugiere qué tipo de plataforma de despliegue (IaaS, PaaS, Serverless, On-Premise)
# podría ser más adecuada y justifica brevemente tu elección. Pueden existir múltiples respuestas válidas.

# Escenario 1: Una startup tecnológica con un equipo pequeño necesita lanzar rápidamente una API web estándar (ej. Flask/FastAPI) con una base de datos, sin querer preocuparse mucho por la gestión de servidores inicialmente. El tráfico esperado es moderado pero podría crecer.
# Sugerencia 1: PaaS (Heroku, Google App Engine, etc.).
# Justificación: Permite un despliegue muy rápido enfocándose en el código. Maneja el servidor, SO y escalado básico, ideal para equipos pequeños con recursos limitados para operaciones.

# Escenario 2: Una gran empresa financiera con estrictas regulaciones de seguridad y privacidad de datos necesita desplegar una aplicación interna crítica que procesa información muy sensible. Tienen un equipo de TI experimentado.
# Sugerencia 2: On-Premise o Nube Privada (IaaS con controles estrictos).
# Justificación: El control total sobre la infraestructura y la ubicación física de los datos es primordial debido a las regulaciones y la sensibilidad. Un equipo experimentado puede gestionar la complejidad.

# Escenario 3: Una aplicación que necesita procesar subidas de imágenes de usuarios de forma esporádica. Cuando se sube una imagen, se debe redimensionar y guardar en otro lugar. El volumen de subidas es impredecible.
# Sugerencia 3: Serverless (FaaS - AWS Lambda, Google Cloud Functions, etc.).
# Justificación: Ideal para tareas basadas en eventos (subida de imagen) y con carga variable. Se paga solo por la ejecución, escala automáticamente a cero cuando no hay subidas y maneja picos de carga eficientemente sin gestión de servidores.

# Escenario 4: Una aplicación compleja con requisitos muy específicos de configuración del sistema operativo, librerías particulares y control detallado sobre la red, que además necesita escalar a muchas instancias.
# Sugerencia 4: IaaS (AWS EC2, GCE, etc.) o CaaS (Kubernetes sobre IaaS).
# Justificación: IaaS ofrece el control necesario sobre el entorno. Si la aplicación está contenerizada (Docker), CaaS sobre IaaS (como Kubernetes gestionado - EKS, GKE) puede simplificar la orquestación y el escalado manteniendo un alto grado de control.

print("\n--- Ejercicio 3: Elegir la Plataforma Adecuada ---")
print("Ver comentarios en el código para las sugerencias y justificaciones.")
print("-" * 20)

print("\nElegir la estrategia de despliegue correcta depende de muchos factores,")
print("incluyendo coste, escalabilidad, control, mantenimiento y experiencia del equipo.")

# --- Fin de los ejercicios ---
