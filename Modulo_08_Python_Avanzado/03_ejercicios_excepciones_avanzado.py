# Ejercicios: Módulo 8 - Manejo de Excepciones Avanzado

print("--- Manejo de Excepciones Avanzado ---")

# --- Ejercicio 1: Bloques `else` y `finally` ---
# Instrucciones:
# 1. Escribe una función `dividir_numeros(a, b)` que intente dividir `a` entre `b`.
# 2. Usa un bloque `try...except` para capturar específicamente la excepción `ZeroDivisionError`.
#    - Dentro del `except`, imprime un mensaje de error claro (ej. "Error: No se puede dividir por cero.").
# 3. Añade un bloque `else` que se ejecute solo si la división fue exitosa (no hubo excepción).
#    - Dentro del `else`, imprime el resultado de la división.
# 4. Añade un bloque `finally` que se ejecute siempre, independientemente de si hubo excepción o no.
#    - Dentro del `finally`, imprime "--- Fin del intento de división ---".
# 5. Llama a la función `dividir_numeros` dos veces: una con valores válidos (ej. 10, 2) y otra que cause la división por cero (ej. 5, 0). Observa la salida en ambos casos.

print("--- Ejercicio 1: Bloques `else` y `finally` ---")

# 1, 2, 3, 4. Definir función con try/except/else/finally
def dividir_numeros(a, b):
    """Intenta dividir a / b y maneja ZeroDivisionError."""
    print(f"\nIntentando dividir {a} / {b}...")
    resultado = None
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except TypeError:
        print(f"Error: Tipos no válidos para división ({type(a)}, {type(b)}).")
    else:
        # Se ejecuta solo si no hubo excepciones en el try
        print(f"División exitosa. Resultado: {resultado}")
    finally:
        # Se ejecuta siempre
        print("--- Fin del intento de división ---")
    return resultado # Devolvemos None si hubo error

# 5. Llamar a la función
dividir_numeros(10, 2)
dividir_numeros(5, 0)
dividir_numeros(10, "a") # Para probar TypeError

print("-" * 20)


# --- Ejercicio 2: Crear Excepciones Personalizadas ---
# Instrucciones:
# 1. Define una clase de excepción personalizada llamada `ErrorValorInvalido` que herede de `Exception`.
#    - Puedes dejar el cuerpo de la clase vacío (`pass`) o añadir un docstring.
# 2. Define otra excepción personalizada `ErrorValorDemasiadoAlto` que herede de `ErrorValorInvalido`.
# 3. Crea una función `validar_edad(edad)` que:
#    - Lance (`raise`) un `TypeError` si la `edad` no es un entero.
#    - Lance tu excepción `ErrorValorInvalido` si la `edad` es negativa.
#    - Lance tu excepción `ErrorValorDemasiadoAlto` si la `edad` es mayor a 120.
#    - Si la edad es válida (0-120), imprima "Edad válida.".
# 4. Llama a `validar_edad` con diferentes valores (un string, -5, 150, 30) dentro de bloques `try...except` para capturar y manejar específicamente tus excepciones personalizadas y `TypeError`. Imprime mensajes adecuados en cada bloque `except`.

print("\n--- Ejercicio 2: Excepciones Personalizadas ---")

# 1. Definir ErrorValorInvalido
class ErrorValorInvalido(Exception):
    """Excepción base para errores de valor en nuestra validación."""
    pass

# 2. Definir ErrorValorDemasiadoAlto
class ErrorValorDemasiadoAlto(ErrorValorInvalido):
    """Excepción para valores que exceden un límite superior."""
    pass

# 3. Definir función de validación
def validar_edad(edad):
    print(f"\nValidando edad: {edad} (Tipo: {type(edad)})")
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero.")
    if edad < 0:
        raise ErrorValorInvalido("La edad no puede ser negativa.")
    if edad > 120:
        raise ErrorValorDemasiadoAlto("La edad parece demasiado alta (mayor a 120).")
    print("Edad válida.")

# 4. Probar la función y capturar excepciones
edades_a_probar = ["treinta", -5, 150, 30]

for edad_test in edades_a_probar:
    try:
        validar_edad(edad_test)
    except TypeError as e:
        print(f"  Error Capturado (TypeError): {e}")
    except ErrorValorDemasiadoAlto as e: # Capturar la más específica primero
        print(f"  Error Capturado (Valor Alto): {e}")
    except ErrorValorInvalido as e: # Capturar la base después
        print(f"  Error Capturado (Valor Inválido): {e}")
    except Exception as e: # Captura genérica por si acaso
        print(f"  Error inesperado capturado: {e}")

print("-" * 20)


# --- Ejercicio 3: Encadenamiento de Excepciones (`raise from`) ---
# Instrucciones:
# 1. Imagina una función `procesar_datos(datos)` que internamente llama a otra función `cargar_configuracion(path)`.
# 2. La función `cargar_configuracion` puede lanzar `FileNotFoundError` si el archivo no existe.
# 3. Modifica `procesar_datos` para que:
#    a. Llame a `cargar_configuracion` dentro de un bloque `try`.
#    b. Si `cargar_configuracion` lanza `FileNotFoundError`, captura esa excepción.
#    c. Dentro del `except`, lanza (`raise`) una nueva excepción personalizada (puedes usar `ErrorValorInvalido` del ejercicio anterior o crear una nueva como `ErrorProcesamiento`) indicando que falló el procesamiento debido a un problema de configuración, y usa `from e` para encadenar la excepción original (`FileNotFoundError`).
# 4. Define una función `cargar_configuracion(path)` simulada que lance `FileNotFoundError` si el `path` no es "config.txt".
# 5. Llama a `procesar_datos` con un path incorrecto (ej. "config_erronea.txt") dentro de un `try...except` externo para ver la traza de errores encadenados.

print("\n--- Ejercicio 3: Encadenamiento de Excepciones ---")

# Excepción personalizada para este ejercicio
class ErrorProcesamiento(Exception):
    """Error durante el procesamiento de datos."""
    pass

# 4. Función simulada que puede fallar
def cargar_configuracion(path):
    print(f"Intentando cargar configuración desde: '{path}'")
    if path != "config.txt":
        raise FileNotFoundError(f"El archivo de configuración '{path}' no existe.")
    else:
        print("Configuración cargada exitosamente (simulado).")
        return {"parametro": "valor"} # Simular datos de config

# 1, 2, 3. Función que maneja y encadena la excepción
def procesar_datos(path_config):
    print(f"\nIniciando procesamiento con config: '{path_config}'")
    config = None
    try:
        config = cargar_configuracion(path_config)
        # ... aquí iría el resto del procesamiento si la config se carga ...
        print("Procesamiento de datos completado (simulado).")
    except FileNotFoundError as e:
        # Lanzar una nueva excepción manteniendo la información de la original
        raise ErrorProcesamiento("Falló el procesamiento: Problema al cargar configuración.") from e
    except Exception as e_gen: # Capturar otros posibles errores
        raise ErrorProcesamiento(f"Falló el procesamiento por error inesperado: {e_gen}") from e_gen
    return config

# 5. Llamar a la función que puede fallar y capturar la excepción encadenada
try:
    resultado_proceso = procesar_datos("config_erronea.txt")
except ErrorProcesamiento as e:
    print(f"\nError Capturado (ErrorProcesamiento): {e}")
    # Python automáticamente imprime la cadena de excepciones ("The above exception was the direct cause...")
    # print("\nCausa original (si existe):")
    # print(e.__cause__) # Muestra la excepción original (FileNotFoundError)

print("\nIntento con configuración correcta:")
try:
    resultado_proceso_ok = procesar_datos("config.txt")
    print(f"Resultado del proceso OK: {resultado_proceso_ok}")
except ErrorProcesamiento as e:
     print(f"\nError Capturado (ErrorProcesamiento): {e}")


print("-" * 20)

# --- Fin de los ejercicios ---
